"""Ep10 Golu Masti #1 soundtrack: Fish vocal sounds on the cue sheet + original music_gm song + bundled SFX (Pixabay licence) + lip-sync envelopes."""
import json, sys, subprocess, os, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/golu_pipeline")
from music_gm import make_song
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json"))
SR = 44100; FPS = 30; DUR = T["DUR"]
OUT = sys.argv[1]; LD = "/home/claude/w10/lines"
info = json.load(open(f"{LD}/info.json"))
CUES = [tuple(c) for c in T["CUES"]]
end = -1
for lid, t0 in CUES:
    assert t0 >= end + 0.05 - 1e-6, (lid, t0, end); end = t0 + info[lid]["dur"]
assert end <= DUR, end
N = int(SR * DUR); voice = np.zeros(N)
env = {r: np.zeros(int(DUR * FPS) + 2) for r in ("golu", "bunny", "kids", "mithu")}
for lid, t0 in CUES:
    a, _ = sf.read(f"{LD}/{lid}.wav")
    if a.ndim > 1: a = a.mean(1)
    if info[lid]["role"] == "kids": a = a * 1.4
    s = int(t0 * SR); voice[s:s + len(a)] += a[:N - s]
    role = info[lid]["role"]; hop = SR // FPS
    for k in range(len(a) // hop):
        fi = int(round(t0 * FPS)) + k
        if fi < len(env[role]): env[role][fi] = np.sqrt(np.mean(a[k * hop:(k + 1) * hop] ** 2))
lips = {"fps": FPS}
for r, e in env.items():
    m = np.percentile(e[e > 0], 85) if (e > 0).any() else 1; e = np.clip(e / m, 0, 1)
    lips[r] = np.where(e < 0.18, 0, np.where(e < 0.45, 1, np.where(e < 0.75, 2, 3))).astype(int).tolist()
json.dump(lips, open(f"{OUT}/lips.json", "w"))
# music: soft under the build-ups, full on the laugh/finale; chimes on the laugh + hat-back
make_song("/tmp/ep10_music.wav", DUR, 120, seed=31, prog_id=2, chimes=[T["laugh"], T["hatback"]], finale=T["laugh"], intro_soft=0.0)
subprocess.run(["cp", "/tmp/ep10_music.mid", f"{HERE}/song.mid"])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep10_music.wav", "-af", "loudnorm=I=-20:TP=-2", "-ar", "44100", "-ac", "1", "/tmp/ep10_music_n.wav"], check=True)
mus, _ = sf.read("/tmp/ep10_music_n.wav")
if mus.ndim > 1: mus = mus.mean(1)
mus = np.pad(mus, (0, max(0, N - len(mus))))[:N]
# dip the music under each 'आ… आ…' build-up (comic suspense), back up on the sneeze
g = np.ones(N)
for a, b in ((0.15, T["S1"]), (T["CUES"][3][1], T["S2"]), (T["CUES"][7][1], T["S3"])):
    s, e = int(a * SR), int(b * SR); g[s:e] = np.linspace(1, .35, e - s)
mus = mus * g
SFXD = "/home/claude/golu_pipeline/assets/sfx"; cache = {}
def load(name):
    if name not in cache:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{SFXD}/{name}.mp3", "-ac", "1", "-ar", str(SR), f"/tmp/sfx_{name}.wav"], check=True)
        a, _ = sf.read(f"/tmp/sfx_{name}.wav"); a = a / (np.abs(a).max() + 1e-9)
        cache[name] = (a, int(np.argmax(np.abs(a)[:int(SR * 1.0)])) / SR)
    return cache[name]
sfx = np.zeros(N); SFX = []
def hit(name, t, vol, align_peak=True):
    a, pk = load(name); t0 = t + 1 / FPS - (pk if align_peak else 0)
    s = max(0, int(t0 * SR)); n = min(len(a), N - s)
    if n > 0: sfx[s:s + n] += vol * a[:n]; SFX.append((name, round(t, 2), vol))
C = dict((k, v) for k, v in T["CUES"])
hit("pop", 0.05, .25)
hit("whoosh", T["S1"], .4); hit("impact-bass-1", T["S1"], .3); hit("pop", T["S1"], .25)
hit("whoosh-short", T["hat"] - .9, .25); hit("pop", T["hat"], .35); hit("sparkle", T["hat"] + .05, .25, False)
hit("click-soft", T["f2"], .3); hit("pop", C["b1"], .25)
hit("whoosh-short", T["bun"] + .05, .35); hit("click-soft", T["bun"] + .4, .3)
hit("whoosh-cinematic", T["S2"], .4); hit("impact-bass-2", T["S2"], .35); hit("pop", T["S2"], .25)
hit("whoosh", T["S2"] + .3, .3); hit("impact-bass-1", T["pile"], .25); hit("pop", T["pile"] + .02, .3)
hit("pop", T["pop"], .35); hit("sparkle", T["pop"] + .2, .25, False)
hit("click-soft", T["f3"] - .3, .3); hit("pop", C["k1"] - .05, .3)
hit("whoosh-short", T["tuck"], .25); hit("pop", T["S3"], .2); hit("sparkle", T["S3"] + .1, .3, False)
hit("chime", T["laugh"], .3, False); hit("pop", C["k2"], .3)
hit("whoosh-short", T["hatfly"], .25); hit("pop", T["hatback"], .35); hit("sparkle", T["hatback"] + .05, .25, False)
hit("whoosh", T["loop"] - .35, .3); hit("click-soft", T["loop"], .25)
json.dump(SFX, open(f"{HERE}/sfx_cues.json", "w"))
mus = mus + sfx
venv = np.convolve(np.abs(voice), np.ones(2205) / 2205, "same")
mix = mus * (1 - 0.55 * np.clip(venv / 0.02, 0, 1)) + voice * 1.0
mix = mix / np.abs(mix).max() * 0.93
sf.write("/tmp/ep10_mix.wav", mix.astype(np.float32), SR)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep10_mix.wav", "-af", "loudnorm=I=-14:TP=-2", "-ar", "44100", "-b:a", "192k", f"{OUT}/song.mp3"], check=True)
print("ok", end, len(SFX))
