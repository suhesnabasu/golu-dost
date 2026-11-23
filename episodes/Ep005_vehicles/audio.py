"""Ep5 soundtrack: Fish voices on the cue sheet + original music_gm song + bundled SFX (Pixabay licence) + Golu lip-sync envelope."""
import json, sys, subprocess, os, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/golu_pipeline")
from music_gm import make_song
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json"))
SR = 44100; FPS = 30; DUR = T["DUR"]
OUT = sys.argv[1]; LD = os.environ.get("GOLU_LINES", "/home/claude/golu_pipeline/lines")
info = json.load(open(f"{LD}/info.json"))
CUES = [tuple(c) for c in T["CUES"]]
end = -1
for lid, t0 in CUES:
    assert t0 >= end + 0.1 - 1e-6, (lid, t0, end); end = t0 + info[lid]["dur"]
assert end <= DUR, end
N = int(SR * DUR); voice = np.zeros(N); env = np.zeros(int(DUR * FPS) + 2)
for lid, t0 in CUES:
    a, _ = sf.read(f"{LD}/{lid}.wav")
    if a.ndim > 1: a = a.mean(1)
    s = int(t0 * SR); voice[s:s + len(a)] += a[:N - s]
    if info[lid]["role"] != "golu": continue
    hop = SR // FPS
    for k in range(len(a) // hop):
        fi = int(round(t0 * FPS)) + k
        if fi < len(env): env[fi] = np.sqrt(np.mean(a[k * hop:(k + 1) * hop] ** 2))
m = np.percentile(env[env > 0], 85); e = np.clip(env / m, 0, 1)
q = np.where(e < 0.18, 0, np.where(e < 0.45, 1, np.where(e < 0.75, 2, 3)))
json.dump({"fps": FPS, "golu": q.astype(int).tolist()}, open(f"{OUT}/lips.json", "w"))
V = T["V"]
CH = [T["intro"]] + [v["g"] for v in V] + [T["recap"]]
make_song("/tmp/ep5_music.wav", DUR, 120, seed=13, prog_id=0, chimes=CH, finale=T["end"], intro_soft=0.0)
subprocess.run(["cp", "/tmp/ep5_music.mid", f"{OUT}/song.mid"])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep5_music.wav", "-af", "loudnorm=I=-20:TP=-2", "-ar", "44100", "/tmp/ep5_music_n.wav"], check=True)
mus, _ = sf.read("/tmp/ep5_music_n.wav"); mus = np.pad(mus, (0, max(0, N - len(mus))))[:N]
# ---- SFX from the bundled library (assets/sfx), 0.3-0.4, peak one frame after the picture
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
hit("whoosh", T["train0"] + .45, .4)
cards = [0.05, T["CUES"][1][1] - .05, T["intro"]] + [v["g"] for v in V] + [T["recap"], T["end"]] + ([T["s1"]] if "s1" in T else [])
for i, t in enumerate(cards): hit("pop", t, .3)
for k, v in enumerate(V):
    if k > 0: hit(["whoosh-short", "whoosh", "whoosh-short"][k - 1], v["in"] + .25, .3)
    hit(["whoosh", "whoosh-short", "whoosh", "whoosh-short"][k], v["out"] + .35, .3)
    hit("sparkle", v["k"], .3, False)
for k in range(4): hit("click-soft", T["recap"] + .3 + k * .12, .3)
hit("chime", T["h2"] + T["D"]["h2"] - .2, .3, False); hit("chime", T["end"], .35, False)
json.dump(SFX, open(f"{HERE}/sfx_cues.json", "w"))
mus = mus + sfx
venv = np.convolve(np.abs(voice), np.ones(2205) / 2205, "same")
mix = mus * (1 - 0.55 * np.clip(venv / 0.02, 0, 1)) + voice * 1.0
mix = mix / np.abs(mix).max() * 0.93
sf.write("/tmp/ep5_mix.wav", mix.astype(np.float32), SR)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep5_mix.wav", "-af", "loudnorm=I=-14:TP=-1", "-ar", "44100", "-b:a", "192k", f"{OUT}/song.mp3"], check=True)
print("ok", end, len(SFX))
