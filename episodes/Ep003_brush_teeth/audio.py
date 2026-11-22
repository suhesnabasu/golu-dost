import json, sys, subprocess, os, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/golu_pipeline")
from music_gm import make_song
SR=44100; FPS=30; DUR=34.0
OUT=sys.argv[1]; LD=os.environ.get("GOLU_LINES","/home/claude/golu_pipeline/lines")
info=json.load(open(f"{LD}/info.json"))
CUES=[("a1",0.6),("a2",2.0),("b1",3.35),("b2",4.95),("c1",6.65),("c2",7.7),("d1",10.6),("d2",11.7),
      ("e1",14.6),("e2",16.0),("f1",18.6),("f2",19.85),("g1",21.6),("g2",22.8),("h1",24.45),
      ("i1",26.9),("i2",28.7),("j1",30.5),("j2",31.85)]
# overlap guard
end=-1
for lid,t0 in CUES:
    assert t0>=end+0.15-1e-6, (lid,t0,end); end=t0+info[lid]["dur"]
assert end<=DUR, end
N=int(SR*DUR); voice=np.zeros(N); env=np.zeros(int(DUR*FPS)+2)
for lid,t0 in CUES:
    a,_=sf.read(f"{LD}/{lid}.wav"); s=int(t0*SR); voice[s:s+len(a)]+=a[:N-s]
    if info[lid]["role"]!="golu": continue
    hop=SR//FPS
    for k in range(len(a)//hop):
        fi=int(round(t0*FPS))+k
        if fi<len(env): env[fi]=np.sqrt(np.mean(a[k*hop:(k+1)*hop]**2))
m=np.percentile(env[env>0],85); e=np.clip(env/m,0,1)
q=np.where(e<0.18,0,np.where(e<0.45,1,np.where(e<0.75,2,3)))
json.dump({"fps":FPS,"golu":q.astype(int).tolist()},open(f"{OUT}/lips.json","w"))
WORDS=[0.2,6.5,10.5,14.5,18.5,21.5,24.45,25.15,25.9,26.9]
make_song("/tmp/song_music.wav",DUR,120,seed=7,prog_id=1,chimes=WORDS,finale=30.5,intro_soft=0.0)
subprocess.run(["cp","/tmp/song_music.mid",f"{OUT}/song.mid"])
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","/tmp/song_music.wav","-af","loudnorm=I=-20:TP=-2","-ar","44100","/tmp/song_music_n.wav"],check=True)
mus,_=sf.read("/tmp/song_music_n.wav"); mus=np.pad(mus,(0,max(0,N-len(mus))))[:N]
# synthesized SFX (no downloaded sounds): splat + water spray
rng=np.random.default_rng(5); sfx=np.zeros(N)
def burst(t0,d,lp,amp,decay):
    n=int(d*SR); x=rng.standard_normal(n)
    k=max(1,int(SR/lp)); x=np.convolve(x,np.ones(k)/k,"same")
    envl=np.exp(-np.arange(n)/(decay*SR)); s=int(t0*SR); sfx[s:s+n]+=x*envl*amp
def splat(t0):
    burst(t0,0.25,900,0.9,0.05)
    n=int(0.18*SR); tt=np.arange(n)/SR; s=int(t0*SR)
    sfx[s:s+n]+=0.35*np.sin(2*np.pi*(320-900*tt)*tt)*np.exp(-tt/0.05)
def spray(t0,d):
    n=int(d*SR); x=rng.standard_normal(n); x=x-np.convolve(x,np.ones(6)/6,"same")
    envl=np.minimum(1,np.arange(n)/(0.05*SR))*np.minimum(1,(n-np.arange(n))/(0.25*SR)); s=int(t0*SR); sfx[s:s+n]+=x*envl*0.12
splat(0.55); spray(15.5,1.0); spray(25.95,0.6)
for t in (3.0,): burst(t,0.12,1500,0.4,0.03)  # wipe swish
mus=mus+sfx
venv=np.convolve(np.abs(voice),np.ones(2205)/2205,"same")
mix=mus*(1-0.5*np.clip(venv/0.02,0,1))+voice*1.0
mix=mix/np.abs(mix).max()*0.93
sf.write("/tmp/song_mix.wav",mix.astype(np.float32),SR)
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","/tmp/song_mix.wav","-af","loudnorm=I=-14:TP=-1","-b:a","192k",f"{OUT}/song.mp3"],check=True)
print("ok", end)
