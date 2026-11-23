"""Ep003 v3 soundtrack: Fish Audio voices fitted to the original cue sheet + original song (music_gm seed 7) + SFX."""
import json, sys, subprocess, os, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/golu_pipeline"); sys.path.insert(0, "/home/claude/work/lib")
from music_gm import make_song
import plan as P, voicemix as VM
SR = 44100; DUR = 34.0; OUT = sys.argv[1]; W = "/home/claude/work"
plan = json.load(open(f"{W}/plan3.json")); roles = {k[3:]: v for k, v in json.load(open(f"{W}/roles.json")).items() if k.startswith("e3_")}
LD = f"{W}/lines3"; P.render(plan, f"{W}/lines_tr", LD, "e3_")
voice, lips, end = VM.voice_track(plan, LD, roles, DUR)
json.dump(lips, open(f"{OUT}/lips.json", "w")); json.dump(plan, open(f"{OUT}/cues.json", "w"))
N = int(SR * DUR)
WORDS = [0.2, 6.5, 10.5, 14.5, 18.5, 21.5, 24.45, 25.15, 25.9, 26.9]
make_song("/tmp/song_music.wav", DUR, 120, seed=7, prog_id=1, chimes=WORDS, finale=30.5, intro_soft=0.0)
subprocess.run(["cp", "/tmp/song_music.mid", f"{OUT}/song.mid"])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", "/tmp/song_music.wav", "-af", "loudnorm=I=-20:TP=-2", "-ar", "44100", "/tmp/song_music_n.wav"], check=True)
mus, _ = sf.read("/tmp/song_music_n.wav"); mus = np.pad(mus, (0, max(0, N - len(mus))))[:N]
rng = np.random.default_rng(5); sfx = np.zeros(N)
def burst(t0, d, lp, amp, decay):
    n = int(d*SR); x = rng.standard_normal(n); k = max(1, int(SR/lp)); x = np.convolve(x, np.ones(k)/k, "same")
    s = int(t0*SR); sfx[s:s+n] += x*np.exp(-np.arange(n)/(decay*SR))*amp
def splat(t0):
    burst(t0, 0.25, 900, 0.9, 0.05); n = int(0.18*SR); tt = np.arange(n)/SR; s = int(t0*SR)
    sfx[s:s+n] += 0.35*np.sin(2*np.pi*(320-900*tt)*tt)*np.exp(-tt/0.05)
def spray(t0, d):
    n = int(d*SR); x = rng.standard_normal(n); x = x-np.convolve(x, np.ones(6)/6, "same")
    e = np.minimum(1, np.arange(n)/(0.05*SR))*np.minimum(1, (n-np.arange(n))/(0.25*SR)); s = int(t0*SR); sfx[s:s+n] += x*e*0.12
splat(0.55); spray(15.5, 1.0); spray(25.95, 0.6); burst(3.0, 0.12, 1500, 0.4, 0.03)
fx = VM.lib_sfx(N, [("pop", t + .05, .3) for t in WORDS[1:6]] + [("sparkle", 19.7, .3), ("whoosh-short", 24.4, .25), ("chime", 30.5, .3)])
db = VM.final_mix(mus + sfx + fx, voice, f"{OUT}/song.mp3")
print("ok end", round(end, 2), "voice over music dB", db)
