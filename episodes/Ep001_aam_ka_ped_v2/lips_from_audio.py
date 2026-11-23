"""Lip-sync levels from a finished mix: RMS of the voice band inside each speaker's cue window."""
import json, sys, numpy as np, soundfile as sf, subprocess
def levels(wav, cues, dur, fps=30, roles=("golu",)):
    subprocess.run(["ffmpeg","-v","error","-y","-i",wav,"-af","highpass=f=250,lowpass=f=3500","-ac","1","-ar","44100","/tmp/_vb.wav"],check=True)
    a,sr=sf.read("/tmp/_vb.wav"); hop=sr//fps; n=int(dur*fps)+2
    rms=np.array([np.sqrt(np.mean(a[i*hop:(i+1)*hop]**2)) if i*hop<len(a) else 0 for i in range(n)])
    # floor = music-only level (frames outside all cue windows)
    inside=np.zeros(n,bool)
    for lid,role,t0,t1 in cues: inside[int(t0*fps):int(t1*fps)]=True
    floor=np.percentile(rms[~inside],60) if (~inside).any() else 0
    out={"fps":fps}
    for r in roles:
        mask=np.zeros(n,bool)
        for lid,role,t0,t1 in cues:
            if role==r: mask[int(t0*fps):int(t1*fps)]=True
        e=np.where(mask,np.clip(rms-floor*1.3,0,None),0)
        if not (e>0).any(): out[r]=[0]*n; continue
        m=np.percentile(e[e>0],85); e=np.clip(e/m,0,1); e=np.convolve(e,[.25,.5,.25],"same")
        q=np.where(e<0.18,0,np.where(e<0.45,1,np.where(e<0.75,2,3)))
        q[~mask]=0
        out[r]=q.astype(int).tolist()
    return out
