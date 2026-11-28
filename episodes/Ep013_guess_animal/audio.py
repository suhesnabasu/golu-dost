"""Ep13 soundtrack: Fish voices on the cue sheet + original music_gm song + bundled SFX (Pixabay licence) + lip-sync envelopes.
usage: python3 audio.py <proj/assets> <lines dir>"""
import json, sys, subprocess, os, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/golu_pipeline")
from music_gm import make_song
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json"))
SR = 44100; FPS = 30; DUR = T["DUR"]
OUT, LD = sys.argv[1], sys.argv[2]
info = json.load(open(f"{LD}/info.json"))
CUES = [tuple(c) for c in T["CUES"]]
end = -1
for lid, t0 in CUES:
    assert t0 >= end + 0.1 - 1e-6, (lid, t0, end); end = t0 + info[lid]["dur"]
assert end <= DUR, end
N = int(SR * DUR); voice = np.zeros(N)
env = {r: np.zeros(int(DUR * FPS) + 2) for r in ("golu", "bunny", "kids", "mithu", "nar")}
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
C = dict((k, v) for k, v in T["CUES"]); D = T["D"]
CH = [T["r1"], T["r2"], T["b3b"], T["k2"]]
make_song("/tmp/ep13_music.wav", DUR, 120, seed=43, prog_id=2, chimes=CH, finale=T["k2"], intro_soft=0.0)
subprocess.run(["cp", "/tmp/ep13_music.mid", f"{HERE}/song.mid"])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep13_music.wav", "-af", "loudnorm=I=-20:TP=-2", "-ar", "44100", "/tmp/ep13_music_n.wav"], check=True)
mus, _ = sf.read("/tmp/ep13_music_n.wav")
if mus.ndim > 1: mus = mus.mean(1)
mus = np.pad(mus, (0, max(0, N - len(mus))))[:N]
g = np.ones(N)
def seg(t0, t1, v, ramp=0.25):
    a0, a1, r = int(t0 * SR), int(t1 * SR), int(ramp * SR)
    g[a0:a1] = np.minimum(g[a0:a1], v)
    g[max(0, a0 - r):a0] = np.minimum(g[max(0, a0 - r):a0], np.linspace(1, v, a0 - max(0, a0 - r)))
    g[a1:a1 + r] = np.minimum(g[a1:a1 + r], np.linspace(v, 1, len(g[a1:a1 + r])))
# thinking pauses: music tiptoes so the child can answer
for a, b in (("c1", "r1"), ("c3", "r2"), ("c4", "b3b")):
    seg(C[a] + D[a], C[b], 0.4)
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
def hit(name, t, vol, align_peak=True, maxlen=None):
    a, pk = load(name); t0 = t + 1 / FPS - (pk if align_peak else 0)
    if maxlen: a = a[:int(maxlen * SR)] * np.linspace(1, 0, int(maxlen * SR))[:len(a[:int(maxlen * SR)])]
    s = max(0, int(t0 * SR)); n = min(len(a), N - s)
    if n > 0: sfx[s:s + n] += vol * a[:n]; SFX.append((name, round(t, 2), vol))
for t in (0.02, T["s2"] - .1, T["s3"] - .1, DUR - .55):
    hit("whoosh-short", max(0.02, t), .22)
hit("pop", 0.12, .3)
hit("whoosh", T["bun_in"], .3)
hit("impact-bass-1", T["x1"], .2); hit("click-soft", T["x1"], .35)
hit("impact-bass-1", T["x2"], .2); hit("click-soft", T["x2"], .35)
for k in ("peek1", "peek2", "peek3"): hit("pop", T[k], .26)
for k in ("r1", "r2", "b3b"):
    hit("whoosh-short", T[k] - .05, .2); hit("sparkle", T[k], .32, False)
hit("pop", T["feather"] + .3, .3)
for j in range(3): hit("pop", T["k2"] + D["k2"] * (.1 + .3 * j), .28)
hit("chime", T["g2"], .3, False)
json.dump(SFX, open(f"{HERE}/sfx_cues.json", "w"))
mus = mus + sfx
venv = np.convolve(np.abs(voice), np.ones(2205) / 2205, "same")
mix = mus * (1 - 0.7 * np.clip(venv / 0.02, 0, 1)) + voice * 1.0
mix = mix / np.abs(mix).max() * 0.93
sf.write("/tmp/ep13_mix.wav", mix.astype(np.float32), SR)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep13_mix.wav", "-af", "loudnorm=I=-14:TP=-1", "-ar", "44100", "-b:a", "192k", f"{OUT}/song.mp3"], check=True)
print("ok", end, len(SFX))
