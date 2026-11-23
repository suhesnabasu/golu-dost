"""Ep004 v2 soundtrack: Fish Audio voices on the original riddle timing structure + original song (music_gm seed 11, prog 2) + SFX."""
import json, sys, subprocess, os, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/golu_pipeline")
from music_gm import make_song
HERE=os.path.dirname(os.path.abspath(__file__)); T = json.load(open(f"{HERE}/timing.json"))
sys.path.insert(0,"/home/claude/work/lib"); import voicemix as VM
SR=44100; FPS=30; DUR=T["DUR"]
OUT=sys.argv[1]; LD=os.environ.get("GOLU_LINES","/home/claude/golu_pipeline/lines")
info=json.load(open(f"{LD}/info.json"))
CUES=[tuple(c) for c in T["CUES"]]
plan=[[l,t,1.0,info[l]["dur"]] for l,t in CUES]
roles={l:info[l]["role"] for l,_ in CUES}
voice,lips,end=VM.voice_track(plan,LD,roles,DUR)
json.dump(lips,open(f"{OUT}/lips.json","w")); json.dump(plan,open(f"{OUT}/cues.json","w"))
N=int(SR*DUR)
R=T["R"]
CH=[0.25,T["intro"]]+[x for r in R for x in (r["t0"],r["rev"])]+[T["recap"],T["j1"],T["j2"]]
make_song("/tmp/song_music.wav",DUR,120,seed=11,prog_id=2,chimes=CH,finale=T["end"],intro_soft=0.0)
subprocess.run(["cp","/tmp/song_music.mid",f"{OUT}/song.mid"])
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","/tmp/song_music.wav","-af","loudnorm=I=-20:TP=-2","-ar","44100","/tmp/song_music_n.wav"],check=True)
mus,_=sf.read("/tmp/song_music_n.wav"); mus=np.pad(mus,(0,max(0,N-len(mus))))[:N]
# synthesized SFX only
rng=np.random.default_rng(4); sfx=np.zeros(N)
def tone(t0,f0,f1,d,amp,dec):
    n=int(d*SR); tt=np.arange(n)/SR; s=int(t0*SR); f=f0+(f1-f0)*tt/d
    sfx[s:s+n]+=amp*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt/dec)
def bonk(t0): tone(t0,520,180,0.3,0.6,0.08); tone(t0,1040,400,0.15,0.2,0.04)
def tick(t0): tone(t0,1500,1500,0.06,0.35,0.015); tone(t0,750,750,0.08,0.2,0.02)
def pop(t0):
    tone(t0,300,1200,0.12,0.5,0.05)
    n=int(0.08*SR); x=rng.standard_normal(n)*np.exp(-np.arange(n)/(0.015*SR)); s=int(t0*SR); sfx[s:s+n]+=0.25*x
def boing(t0): tone(t0,220,660,0.35,0.35,0.15)
bonk(0.2); boing(0.75)
for r in R:
    for k in range(3): tick(r["cd"]+k*0.5)
    pop(r["rev"])
for k in range(3): pop(T["j1"]+k*0.55)
fx=VM.lib_sfx(N,[("whoosh-short",T["intro"]-.1,.3)]+[("sparkle",r["rev"]+.05,.3) for r in R]+[("chime",T["end"],.3)])
db=VM.final_mix(mus+sfx+fx,voice,f"{OUT}/song.mp3")
print("ok end",round(end,2),"voice over music dB",db)
