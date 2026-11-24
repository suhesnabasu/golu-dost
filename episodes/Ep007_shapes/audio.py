"""Ep7 soundtrack: voices on the cue sheet + original music_gm song (seed 19, prog 2) + bundled SFX (Pixabay licence) + Golu lip-sync envelope.
usage: python3 audio.py <ep/assets>"""
import json, sys, subprocess, os, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/golu_pipeline")
from music_gm import make_song
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json"))
SR = 44100; FPS = 30; DUR = T["DUR"]
OUT = sys.argv[1]; LD = os.environ.get("GOLU_LINES", "/home/claude/ep7/lines")
info = json.load(open(f"{LD}/info.json"))
CUES = [tuple(c) for c in T["CUES"]]; D = T["D"]; CUE = dict(CUES)
end = -1
for lid, t0 in CUES:
    assert t0 >= end + 0.1 - 1e-6, (lid, t0, end); end = t0 + info[lid]["dur"]
assert end <= DUR, end
N = int(SR * DUR); voice = np.zeros(N)
env = {r: np.zeros(int(DUR * FPS) + 2) for r in ("golu", "kids", "mithu")}
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
    m = np.percentile(e[e > 0], 85); e = np.clip(e / m, 0, 1)
    lips[r] = np.where(e < 0.18, 0, np.where(e < 0.45, 1, np.where(e < 0.75, 2, 3))).astype(int).tolist()
json.dump(lips, open(f"{OUT}/lips.json", "w"))
CH = [T["learn"], T["circ"], T["sq"] + .1, T["tri"] + .1, T["f2"], T["f3"]]
make_song("/tmp/ep7_music.wav", DUR, 120, seed=19, prog_id=2, chimes=CH, finale=T["f3"], intro_soft=0.0)
subprocess.run(["cp", "/tmp/ep7_music.mid", f"{HERE}/song.mid"])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep7_music.wav", "-af", "loudnorm=I=-20:TP=-2", "-ar", "44100", "/tmp/ep7_music_n.wav"], check=True)
mus, _ = sf.read("/tmp/ep7_music_n.wav")
if mus.ndim > 1: mus = mus.mean(1)
mus = np.pad(mus, (0, max(0, N - len(mus))))[:N]
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
# hook: roti whoosh, bonk on the head
hit("whoosh-short", 0.05, .3, False); hit("impact-bass-1", T["land"], .38); hit("pop", T["land"] + .05, .3)
hit("whoosh", T["hop"] + .1, .3)
# cards pop
for t in [T["learn"], T["circ"], T["sq"] + .1, T["tri"] + .1, T["again"], T["bye"]]: hit("pop", t, .3)
# foods leave
hit("whoosh-cinematic", T["sq"] - .1, .3); hit("whoosh-short", T["tri"] - .1, .32)
# corner counts
for k in range(4): hit("click-soft", CUE["d2"] + .05 + k * D["d2"] / 4, .3)
for k in range(3): hit("click-soft", CUE["e2"] + .05 + k * D["e2"] / 3, .3)
# right answers (chorus)
for t in [CUE["c3a"], CUE["d4a"], CUE["e4a"]]: hit("sparkle", t, .28, False)
# recap pops on each word, riser into confetti chime
for k in range(3): hit("pop", T["f2"] + k * D["f2"] / 3, .3)
hit("riser", T["f3"] - 1.0, .22, False); hit("chime", T["f3"], .33, False)
hit("chime", T["bye"] + .1, .28, False); hit("whoosh-short", DUR - .72, .28, False)
json.dump(SFX, open(f"{HERE}/sfx_cues.json", "w"))
mus = mus + sfx
venv = np.convolve(np.abs(voice), np.ones(2205) / 2205, "same")
mix = mus * (1 - 0.7 * np.clip(venv / 0.02, 0, 1)) + voice * 1.0
mix = mix / np.abs(mix).max() * 0.93
sf.write("/tmp/ep7_mix.wav", mix.astype(np.float32), SR)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/ep7_mix.wav", "-af", "loudnorm=I=-14:TP=-1", "-ar", "44100", "-b:a", "192k", f"{OUT}/song.mp3"], check=True)
print("ok", end, len(SFX))
