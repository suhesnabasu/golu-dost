"""Ep001 v3 soundtrack: Fish Audio voices fitted to the original cue sheet + the original synthesized song and SFX."""
"""Builds the episode soundtrack (voices + music + sfx) and lip-sync envelopes."""
import json, sys, numpy as np, soundfile as sf
SR = 44100; FPS = 30
sys.path.insert(0, "/home/claude/work/lib"); import plan as P, voicemix as VM
W = "/home/claude/work"; OUT = sys.argv[1]; DUR = 44.5
STEP0, STEP = 8.6, 2.85          # v3: counting moved later so the Fish intro lines fit
plan = json.load(open(f"{W}/plan1.json")); roles = {k[3:]: v for k, v in json.load(open(f"{W}/roles.json")).items() if k.startswith("e1_")}
LD = f"{W}/lines1"; P.render(plan, f"{W}/lines_tr", LD, "e1_")
voice, lips, end = VM.voice_track(plan, LD, roles, DUR)
json.dump(lips, open(f"{OUT}/lips.json", "w")); json.dump(plan, open(f"{OUT}/cues.json", "w"))
N = int(SR * DUR)
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

db = VM.final_mix(mus, voice, f"{OUT}/song.mp3", duck=0.6, vgain=1.25)
print("ok end", round(end, 2), "voice over music dB", db)
