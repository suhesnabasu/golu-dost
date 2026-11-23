"""Ep6 soundtrack: voices on the cue sheet + original music_gm song + bundled SFX (Pixabay licence) + Golu/Bunny lip-sync envelopes.
usage: python3 audio.py <ep/assets>"""
import json, sys, subprocess, os, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/golu_pipeline")
from music_gm import make_song
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json"))
SR = 44100; FPS = 30; DUR = T["DUR"]
OUT = sys.argv[1]; LD = os.environ.get("GOLU_LINES", "/home/claude/ep6work/lines")
info = json.load(open(f"{LD}/info.json"))
CUES = [tuple(c) for c in T["CUES"]]
end = -1
for lid, t0 in CUES:
    assert t0 >= end + 0.1 - 1e-6, (lid, t0, end); end = t0 + info[lid]["dur"]
assert end <= DUR, end
N = int(SR * DUR); voice = np.zeros(N)
env = {r: np.zeros(int(DUR * FPS) + 2) for r in ("golu", "bunny", "kids", "mithu")}
for lid, t0 in CUES:
    a, _ = sf.read(f"{LD}/{lid}.wav")
    if a.ndim > 1: a = a.mean(1)
    if info[lid]["role"] == "kids": a = a * 1.5
    s = int(t0 * SR); voice[s:s + len(a)] += a[:N - s]
    role = info[lid]["role"]; hop = SR // FPS
    for k in range(len(a) // hop):
        fi = int(round(t0 * FPS)) + k
        if fi < len(env[role]): env[role][fi] = np.sqrt(np.mean(a[k * hop:(k + 1) * hop] ** 2))
lips = {"fps": FPS}
for r, e in env.items():
    m = np.percentile(e[e > 0], 85); e = np.clip(e / m, 0, 1)
    lips[r] = np.where(e < 0.18, 0, np.where(e < 0.45, 1, np.where(e < 0.75, 2, 3))).astype(int).tolist()
json.dump(lips, open(f"{OUT}/lips.json", "w"))
R = T["R"]
CH = [T["turns"], T["count"]] + [r["land"] for r in R] + [T["moral"]]
make_song("/tmp/ep6_music.wav", DUR, 120, seed=17, prog_id=1, chimes=CH, finale=T["moral"], intro_soft=0.0)
subprocess.run(["cp", "/tmp/ep6_music.mid", f"{HERE}/song.mid"])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep6_music.wav", "-af", "loudnorm=I=-20:TP=-2", "-ar", "44100", "/tmp/ep6_music_n.wav"], check=True)
mus, _ = sf.read("/tmp/ep6_music_n.wav")
if mus.ndim > 1: mus = mus.mean(1)
mus = np.pad(mus, (0, max(0, N - len(mus))))[:N]
# softer music under the sad beat (story: the music holds back, then opens on "बारी-बारी")
g = np.ones(N); a0, a1 = int(T["sad"] * SR), int(T["turns"] * SR)
g[a0:a1] = 0.45; ramp = int(0.4 * SR)
g[a0:a0 + ramp] = np.linspace(1, .45, ramp); g[a1 - ramp:a1] = np.linspace(.45, 1, ramp)
mus = mus * g
SFXD = "/home/claude/golu_pipeline/assets/sfx"; cache = {}
def load(name):
    if name not in cache:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{SFXD}/{name}.mp3", "-ac", "1", "-ar", str(SR), f"/tmp/sfx_{name}.wav"], check=True)
        a, _ = sf.read(f"/tmp/sfx_{name}.wav"); a = a / (np.abs(a).max() + 1e-9)
        pk = int(np.argmax(np.abs(a)[:int(SR * 1.0)])) / SR
        cache[name] = (a, pk)
    return cache[name]
sfx = np.zeros(N); SFX = []
def hit(name, t, vol, align_peak=True):
    a, pk = load(name); t0 = t + 1 / FPS - (pk if align_peak else 0)
    s = max(0, int(t0 * SR)); n = min(len(a), N - s)
    if n > 0: sfx[s:s + n] += vol * a[:n]; SFX.append((name, round(t, 2), vol))
W = ["whoosh", "whoosh-short", "whoosh-cinematic"]
# Bunny zooms (hook + two cut-ins) and her exit
for k, z in enumerate([T["hook"], T["cut1"], T["cut2"]]):
    hit(W[k % 2], z["in"] + .15, .35); hit("whoosh-short", z["slide"] + .1, .3)
    hit("impact-bass-1" if k == 0 else "click-soft", z["land"], .35 if k == 0 else .3)
hit("whoosh", T["exit"] + .2, .35)
# word cards pop
for t in [0.1, T["plop1"], T["cut1"]["in"], T["sad"], T["lonely"], T["turns"], T["count"], T["wait_hard"], T["praise"],
          T["plop2"], T["moral"], T["together"], T["bye"]] + [r["go"] + .1 for r in R]:
    hit("pop", t, .3)
# count hops 1-2-3-4
for k in range(4): hit("click-soft", T["count"] + .1 + k * .3, .3)
# rides: climb taps, slide whoosh (rotate takes), landing
for k, r in enumerate(R):
    for j in range(4): hit("click-soft", r["climb"] + .15 + j * .25, .22)
    hit(W[k % 3] if k != 1 else "whoosh-short", r["slide"] + .15, .3)
    if k < 3: hit("sparkle", r["land"], .3, False)
hit("impact-bass-2", T["plop2"], .4)
# Bunny taps her foot while waiting
for j in range(4): hit("click-soft", T["wait_hard"] + .1 + j * .3, .25)
hit("sparkle", T["praise"], .3, False)
hit("riser", T["moral"] - 1.0, .25, False); hit("chime", T["moral"], .35, False)
hit("chime", T["bye"], .3, False)
json.dump(SFX, open(f"{HERE}/sfx_cues.json", "w"))
mus = mus + sfx
venv = np.convolve(np.abs(voice), np.ones(2205) / 2205, "same")
mix = mus * (1 - 0.7 * np.clip(venv / 0.02, 0, 1)) + voice * 1.0
mix = mix / np.abs(mix).max() * 0.93
sf.write("/tmp/ep6_mix.wav", mix.astype(np.float32), SR)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep6_mix.wav", "-af", "loudnorm=I=-14:TP=-1", "-ar", "44100", "-b:a", "192k", f"{OUT}/song.mp3"], check=True)
print("ok", end, len(SFX))
