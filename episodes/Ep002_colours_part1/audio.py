import json, sys, subprocess, numpy as np, soundfile as sf
sys.path.insert(0, "/home/claude/hf/build")
from music_gm import make_song
SR=44100; FPS=30; DUR=22.0
OUT=sys.argv[1]; LD="/home/claude/tts/style2"
info=json.load(open(f"{LD}/info.json"))
CUES=[("s0",0.5),("s0e",1.85)]
for i,c in enumerate("rybg"):
    T=3.0+i*4.0; CUES+=[(c,T+0.6),(c+"e",T+1.6)]
CUES+=[("end",19.0),("ende",19.9)]
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
make_song("/tmp/song_music.wav",DUR,120,seed=3,chimes=[3.0+i*4.0+0.5 for i in range(4)],finale=19.0,intro_soft=2.5)
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","/tmp/song_music.wav","-af","loudnorm=I=-20:TP=-2","-ar","44100","/tmp/song_music_n.wav"],check=True)
mus,_=sf.read("/tmp/song_music_n.wav"); mus=np.pad(mus,(0,max(0,N-len(mus))))[:N]
venv=np.convolve(np.abs(voice),np.ones(2205)/2205,"same")
mix=mus*(1-0.5*np.clip(venv/0.02,0,1))+voice*1.0
mix=mix/np.abs(mix).max()*0.93
sf.write("/tmp/song_mix.wav",mix.astype(np.float32),SR)
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","/tmp/song_mix.wav","-af","loudnorm=I=-14:TP=-1","-b:a","192k",f"{OUT}/song.mp3"],check=True)
print("ok")
