"""Builds the episode soundtrack (voices + music + sfx) and lip-sync envelopes."""
import json, sys, numpy as np, soundfile as sf
SR = 44100; FPS = 30
LINES = "/home/claude/tts/lines_hi"
OUT = sys.argv[1]
DUR = 44.5
STEP0, STEP = 7.0, 3.2          # counting: step i starts at STEP0 + i*STEP, mango lands +0.7
CUES = [("l02", 1.75), ("l01", 3.4), ("l03", 5.55)] + \
       [(f"n{i+1}", STEP0 + i * STEP + 0.78) for i in range(5)] + \
       [("l04", 22.0), ("l05", 23.6), ("l06", 25.7), ("l07", 27.95), ("l08", 29.35),
        ("l09", 31.2), ("l10", 34.4), ("l11", 35.75), ("l12", 37.1), ("l13", 39.1), ("l14", 41.4)]
info = json.load(open(f"{LINES}/info.json"))
N = int(SR * DUR)
voice = np.zeros(N)
env = {c: np.zeros(int(DUR * FPS) + 2) for c in ("golu", "bunny", "mithu", "nar")}
for lid, t0 in CUES:
    a, _ = sf.read(f"{LINES}/{lid}.wav")
    s = int(t0 * SR); voice[s:s + len(a)] += a[:N - s]
    ch = info[lid]["char"]; hop = SR // FPS
    for k in range(len(a) // hop):
        fi = int(round(t0 * FPS)) + k
        if fi < len(env[ch]): env[ch][fi] = np.sqrt(np.mean(a[k * hop:(k + 1) * hop] ** 2))
levels = {}
for c, e in env.items():
    if not (e > 0).any(): continue
    m = np.percentile(e[e > 0], 85); e = np.clip(e / m, 0, 1)
    e = np.convolve(e, [0.25, 0.5, 0.25], "same")
    q = np.where(e < 0.18, 0, np.where(e < 0.45, 1, np.where(e < 0.75, 2, 3)))
    levels[c] = q.astype(int).tolist()
json.dump({"fps": FPS, "levels": levels}, open(f"{OUT}/lipsync.json", "w"))

# ---------------- music + sfx ----------------
rng = np.random.default_rng(3)
mus = np.zeros(N)
def add(sig, start, vol):
    s = int(SR * start)
    if s >= N: return
    seg = sig[:N - s] * vol; mus[s:s + len(seg)] += seg
def tone(f, length, kind="pluck"):
    t = np.arange(int(SR * length)) / SR
    if kind == "pluck":   # ukulele-ish
        w = np.sin(2*np.pi*f*t) + 0.45*np.sin(4*np.pi*f*t) + 0.2*np.sin(6*np.pi*f*t)
        env_ = np.minimum(1, t/0.004) * np.exp(-t*6)
    elif kind == "bass":
        w = np.sin(2*np.pi*f*t); env_ = np.minimum(1, t/0.01) * np.exp(-t*2.2)
    elif kind == "bell":
        w = np.sin(2*np.pi*f*t) + 0.4*np.sin(2*np.pi*f*2.76*t); env_ = np.exp(-t*4)
    elif kind == "glock":
        w = np.sin(2*np.pi*f*t); env_ = np.exp(-t*7)
    else:  # soft pad
        w = sum(np.sin(2*np.pi*f*k*t)/k**2 for k in (1, 2, 3)); env_ = np.minimum(1, t/0.3) * np.minimum(1, (length-t)/0.3)
    return w * env_
def shaker():
    t = np.arange(int(SR*0.06))/SR; return rng.standard_normal(len(t))*np.exp(-t*70)*0.25
def kick():
    t = np.arange(int(SR*0.2))/SR; f = 100*np.exp(-t*25)+50
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*14)
def sweep(dur, f0, f1, wob=0):
    t = np.arange(int(SR*dur))/SR; f = f0+(f1-f0)*(t/dur)+wob*np.sin(2*np.pi*16*t)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.minimum(1, t/0.02)*np.minimum(1, (dur-t)/0.05)
def bonk():
    t = np.arange(int(SR*0.3))/SR; f = 520*np.exp(-t*14)+140
    return (np.sin(2*np.pi*np.cumsum(f)/SR)+0.4*rng.standard_normal(len(t))*np.exp(-t*50))*np.exp(-t*9)
def pop():
    t = np.arange(int(SR*0.08))/SR; return np.sin(2*np.pi*(900-5000*t)*t)*np.exp(-t*50)
def hz(m): return 440*2**((m-69)/12)

BPM = 112; beat = 60/BPM; step = beat/2
mel = [72, 0, 76, 79, 77, 76, 74, 0, 72, 74, 76, 72, 74, 0, 0, 0,
       72, 0, 76, 79, 81, 79, 77, 76, 74, 76, 77, 74, 72, 0, 0, 0]
chords = [(48, 64, 67), (53, 65, 69), (55, 62, 67), (48, 64, 67)]
def music_block(t0, t1, vol=1.0, melody=True):
    i = 0; t = t0
    while t < t1:
        if melody and mel[i % 32]: add(tone(hz(mel[i % 32]), step*1.6), t, 0.085*vol)
        if i % 8 == 0:
            r, a, b = chords[(i//8) % 4]
            add(tone(hz(r), beat*3.8, "bass"), t, 0.16*vol)
            for k, m in enumerate((a, b, a+12)): add(tone(hz(m), beat*0.9), t + k*0.03, 0.05*vol)
        if i % 4 == 0: add(kick(), t, 0.22*vol)
        add(shaker(), t, 0.10*vol)
        t += step; i += 1
# morning: soft pad only while Golu sleeps, then the tune
add(tone(hz(60), 1.6, "pad"), 0, 0.05); add(tone(hz(67), 1.6, "pad"), 0, 0.04)
music_block(1.7, 38.6)
# night: gentle lullaby (no drums)
lull = [79, 76, 72, 76, 74, 71, 67, 0, 72, 76, 79, 81, 79, 0, 0, 0]
for i, m in enumerate(lull):
    if m: add(tone(hz(m), 0.9, "bell"), 38.7 + i*0.36, 0.09)
for k, (r, a, b) in enumerate([(48, 64, 67), (53, 65, 69), (55, 62, 67), (48, 64, 67)]):
    add(tone(hz(r), 1.6, "pad"), 38.7 + k*1.45, 0.05); add(tone(hz(a), 1.6, "pad"), 38.7 + k*1.45, 0.03)

# sfx
add(sweep(0.5, 1300, 500), 0.95, 0.10)   # falling whistle
add(bonk(), 1.45, 0.55)
add(sweep(0.7, 300, 900, wob=60), 1.55, 0.12)
for i in range(5):
    s0 = STEP0 + i*STEP
    add(sweep(0.55, 1100, 450), s0 + 0.12, 0.06)
    add(pop(), s0 + 0.7, 0.35)
    for j, iv in enumerate((0, 4, 7, 12)):
        add(tone(hz(84 + (0, 2, 4, 7, 9)[i] + iv), 0.5, "glock"), s0 + 0.72 + j*0.06, 0.11)
    add(sweep(0.25, 1500, 1900), s0 + 1.55, 0.04)       # flower lands
add(sweep(0.9, 500, 1400, wob=80), 25.2, 0.05)          # leaf letter flies in
for st in (0.5, 1.3, 2.1):
    add(sweep(0.5, 500, 1200), 31.2 + st, 0.06); add(tone(hz(88), 0.6, "bell"), 31.2 + st + 0.55, 0.12)
for j, m in enumerate((72, 76, 79, 84, 88, 91)):
    add(tone(hz(m), 0.9, "bell"), 36.7 + j*0.08, 0.10)    # sash lands
fade = int(SR*1.5); mus[-fade:] *= np.linspace(1, 0, fade)
mus = np.tanh(mus*1.2); mus = mus/np.abs(mus).max()*0.7

# duck music under voices (simple envelope follower)
v_env = np.convolve(np.abs(voice), np.ones(4410)/4410, "same")
duck = 1 - 0.55*np.clip(v_env/0.02, 0, 1)
mix = mus*duck + voice*1.15
mix = mix/np.abs(mix).max()*0.92
sf.write(f"{OUT}/soundtrack.wav", mix.astype(np.float32), SR)
print("ok", DUR, {c: sum(1 for x in v if x) for c, v in levels.items()})
