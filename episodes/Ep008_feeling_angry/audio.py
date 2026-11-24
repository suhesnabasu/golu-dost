"""Ep8 soundtrack: Fish voices on the cue sheet + original music_gm song + bundled SFX (Pixabay licence) + lip-sync envelopes.
usage: python3 audio.py <ep/assets>"""
import json, sys, subprocess, os, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/golu_pipeline")
from music_gm import make_song
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json"))
SR = 44100; FPS = 30; DUR = T["DUR"]
OUT = sys.argv[1]; LD = os.environ.get("GOLU_LINES", f"{HERE}/lines")
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
RB = T["RB"]
CH = [T["place"], RB[0] + .45, RB[1] + .45, RB[2] + 1.4, RB[3] + .45, T["moral"]]
make_song("/tmp/ep8_music.wav", DUR, 120, seed=23, prog_id=0, chimes=CH, finale=T["f2"], intro_soft=0.0)
subprocess.run(["cp", "/tmp/ep8_music.mid", f"{HERE}/song.mid"])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep8_music.wav", "-af", "loudnorm=I=-20:TP=-2", "-ar", "44100", "/tmp/ep8_music_n.wav"], check=True)
mus, _ = sf.read("/tmp/ep8_music_n.wav")
if mus.ndim > 1: mus = mus.mean(1)
mus = np.pad(mus, (0, max(0, N - len(mus))))[:N]
# the music acts the feeling: holds back from the crash, near-quiet for the breathing, opens again on "मुझे गुस्सा आया!"
g = np.ones(N)
def seg(t0, t1, v, ramp=0.4):
    a0, a1, r = int(t0 * SR), int(t1 * SR), int(ramp * SR)
    g[a0:a1] = np.minimum(g[a0:a1], v)
    g[max(0, a0 - r):a0] = np.minimum(g[max(0, a0 - r):a0], np.linspace(1, v, a0 - max(0, a0 - r)))
    g[a1:a1 + r] = np.minimum(g[a1:a1 + r], np.linspace(v, 1, len(g[a1:a1 + r])))
seg(T["crash"] + 0.2, T["in1"] - 0.2, 0.45)
seg(T["in1"] - 0.2, T["calm"], 0.28)
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
C = dict((k, v) for k, v in T["CUES"]); D = T["D"]
hit("pop", T["place"], .3)
hit("whoosh", T["bin"] + .15, .35)
for j in range(3): hit("click-soft", T["skid"] + j * .12, .25)
hit("impact-bass-1", T["crash"] + .45, .3)
for k in range(4): hit("pop" if k % 2 else "click-soft", T["crash"] + .5 + k * .06, .22)
hit("pop", T["hat"], .3)
hit("pop", T["crash"], .3)                     # CRASH card
hit("impact-bass-2", T["stomp"] + .1, .35)
hit("whoosh-short", T["angry"] + .05, .25)
hit("pop", C["b2"], .3); hit("pop", C["c1"], .28); hit("pop", C["c2"], .3)
hit("sparkle", T["freeze"], .25, False)
for k, (i, o) in enumerate([(T["in1"], T["out1"]), (T["in2"], T["out2"]), (T["in3"], T["out3"])]):
    hit("riser", i, .16, False, maxlen=0.9)
    hit("whoosh-short" if k != 1 else "whoosh", o + .1, .25)
    hit("pop", o + .4, .26)                    # badge
hit("click-soft", T["out3"] + .5, .3)          # tiny trunk toot
hit("sparkle", T["calm"], .3, False)
hit("pop", C["d4"], .28); hit("pop", T["felt"], .3); hit("pop", T["ok"], .3); hit("sparkle", C["e4"], .3, False)
for k, t in enumerate(RB):
    land = t + (1.4 if k == 2 else .45)
    hit(["pop", "click-soft", "pop", "click-soft"][k], land, .28)
hit("riser", T["moral"] - .9, .22, False); hit("chime", T["f2"], .35, False)
for k in range(3): hit("pop", T["m1"] + k * D["f1b"] / 3, .25)
hit("chime", T["bye"], .3, False)
hit("whoosh", DUR - 1.0, .3)                   # Bunny zooms off
hit("whoosh-short", DUR - .75, .22)            # loop block lift
json.dump(SFX, open(f"{HERE}/sfx_cues.json", "w"))
mus = mus + sfx
venv = np.convolve(np.abs(voice), np.ones(2205) / 2205, "same")
mix = mus * (1 - 0.7 * np.clip(venv / 0.02, 0, 1)) + voice * 1.0
mix = mix / np.abs(mix).max() * 0.93
sf.write("/tmp/ep8_mix.wav", mix.astype(np.float32), SR)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep8_mix.wav", "-af", "loudnorm=I=-14:TP=-1", "-ar", "44100", "-b:a", "192k", f"{OUT}/song.mp3"], check=True)
print("ok", end, len(SFX))
