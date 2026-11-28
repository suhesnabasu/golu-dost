"""Ep12 soundtrack: Fish voices (chanted rhyme) on the cue sheet + original music_gm song (seed 41 — our OWN melody) + bundled SFX + lip-sync.
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
env = {r: np.zeros(int(DUR * FPS) + 2) for r in ("golu", "kids", "mithu")}
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
CH = [T["pland"], T["cland"], T["hat"], T["recap"]]
make_song("/tmp/ep12_music.wav", DUR, 120, seed=41, prog_id=0, chimes=CH, finale=T["well"], intro_soft=0.0)
if os.path.exists("/tmp/ep12_music.mid"): subprocess.run(["cp", "/tmp/ep12_music.mid", f"{HERE}/song.mid"])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep12_music.wav", "-af", "loudnorm=I=-20:TP=-2", "-ar", "44100", "/tmp/ep12_music_n.wav"], check=True)
mus, _ = sf.read("/tmp/ep12_music_n.wav")
if mus.ndim > 1: mus = mus.mean(1)
mus = np.pad(mus, (0, max(0, N - len(mus))))[:N]
g = np.ones(N)
def seg(t0, t1, v, ramp=0.3):
    a0, a1, r = int(t0 * SR), int(t1 * SR), int(ramp * SR)
    g[a0:a1] = np.minimum(g[a0:a1], v)
    g[max(0, a0 - r):a0] = np.minimum(g[max(0, a0 - r):a0], np.linspace(1, v, a0 - max(0, a0 - r)))
    g[a1:a1 + r] = np.minimum(g[a1:a1 + r], np.linspace(v, 1, len(g[a1:a1 + r])))
seg(T["boing"] - 0.4, T["boing"] - 0.02, 0.35, 0.1)   # music holds its breath on the crouch, opens on BOING
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
def hit(name, t, vol, align_peak=True, maxlen=None, rate=1.0):
    a, pk = load(name)
    if rate != 1.0:
        idx = np.arange(0, len(a) - 1, rate); a = np.interp(idx, np.arange(len(a)), a); pk = pk / rate
    t0 = t + 1 / FPS - (pk if align_peak else 0)
    if maxlen: a = a[:int(maxlen * SR)] * np.linspace(1, 0, int(maxlen * SR))[:len(a[:int(maxlen * SR)])]
    s = max(0, int(t0 * SR)); n = min(len(a), N - s)
    if n > 0: sfx[s:s + n] += vol * a[:n]; SFX.append((name, round(t, 2), vol))
def boing(t, vol=.3, rate=1.0):   # "boing" = a pitched-down pop + soft bass thump (bundled SFX only)
    hit("pop", t, vol, rate=0.55 * rate); hit("impact-bass-1", t, vol * .45)
boing(T["land0"], .32)
hit("pop", C["a1"] + .1, .26)                      # badge 1
for j in range(3): boing(T["swing"] + .2 + j * .85, .2, 1 + .08 * j)
hit("sparkle", C["a3"] + .1, .22, False)
hit("whoosh-short", T["pari"], .24); boing(T["pland"], .24); hit("pop", T["pland"], .26)
for j in range(4): boing(T["e1"] + .1 + j * .55, .16, 1.1 if j % 2 else 1.0)
hit("click-soft", C["e2"] + .2, .22)
hit("sparkle", C["e3"] + .1, .2, False)
hit("pop", C["e4"] + D["e4"] * .4, .2)
hit("whoosh-short", T["chintu"], .24); boing(T["cland"], .24); hit("pop", T["cland"], .26)
for j in range(3): hit("pop", T["count"] + D["c2"] * (.05 + .22 * j), .26)
hit("riser", T["boing"] - .9, .18, False, maxlen=0.9)
boing(T["boing"], .4, .9); hit("impact-bass-2", T["boing"] + .75, .25); hit("whoosh", T["boing"] + .05, .2)
hit("pop", T["hat"], .3); hit("sparkle", T["hat"] + .05, .22, False)
hit("chime", T["well"], .28, False)
for j in range(3): hit("pop", T["recap"] + D["d1"] * (.02 + .3 * j), .26)
hit("click-soft", T["four"] + D["g1"] * .5, .26)
hit("whoosh-short", T["exit"], .22); hit("whoosh-short", T["exit"] + .15, .18)
boing(DUR - 1.0, .2)
hit("whoosh", DUR - .4, .18)
json.dump(SFX, open(f"{HERE}/sfx_cues.json", "w"))
mus = mus + sfx
venv = np.convolve(np.abs(voice), np.ones(2205) / 2205, "same")
mix = mus * (1 - 0.6 * np.clip(venv / 0.02, 0, 1)) + voice * 1.0
mix = mix / np.abs(mix).max() * 0.93
sf.write("/tmp/ep12_mix.wav", mix.astype(np.float32), SR)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep12_mix.wav", "-af", "loudnorm=I=-14:TP=-1", "-ar", "44100", "-b:a", "192k", f"{OUT}/song.mp3"], check=True)
print("ok", end, len(SFX))
