import json, math, numpy as np, soundfile as sf
LD="/home/claude/w10/lines"
info=json.load(open(f"{LD}/info.json")); D={k:v["dur"] for k,v in info.items()}
def peak(l):
    a,sr=sf.read(f"{LD}/{l}.wav"); a=a if a.ndim==1 else a.mean(1)
    h=sr//50; e=[np.sqrt(np.mean(a[i:i+h]**2)) for i in range(0,len(a)-h,h)]
    return round(int(np.argmax(e))*h/sr,2)
P={l:peak(l) for l in ("a2","b2","c2")}
T={}; C=[]
def cue(l,t): C.append((l,round(t,2))); return t+D[l]
e=cue("a1",0.15)
e=cue("a2",e+0.1); T["S1"]=round(C[-1][1]+P["a2"],2)
T["hat"]=round(T["S1"]+1.5,2)
e=max(e,T["hat"]); e=cue("m1",T["hat"]+0.1)
T["f2"]=round(e-1.2,2)            # feather drifts back
e=cue("b1",e+0.15)
T["bun"]=round(e-0.2,2)
e=cue("b2",e+0.1); T["S2"]=round(C[-1][1]+P["b2"],2)
e=cue("bn",max(T["S2"]+0.1,e+0.05))
T["pile"]=round(T["S2"]+0.8,2); T["pop"]=round(T["S2"]+1.7,2)
e=max(e,T["pop"]); T["f3"]=round(T["pop"],2)
e=cue("k1",T["pop"]+0.5)
e=cue("c1",e+0.1); T["tuck"]=round(C[-1][1]+0.4,2)
e=cue("c2",e+0.05); T["S3"]=round(C[-1][1]+P["c2"],2)
T["laugh"]=round(e+0.4,2); e=cue("g1",T["laugh"])
e=cue("k2",e+0.1); e=cue("m2",e+0.1)
T["hatfly"]=round(e+0.2,2); T["hatback"]=round(T["hatfly"]+1.0,2)
T["loop"]=round(T["hatback"]+0.8,2)
T["DUR"]=math.ceil((T["loop"]+2.0)*4)/4
T["CUES"]=C; T["D"]=D; T["P"]=P
json.dump(T,open("timing.json","w"),indent=1); print(json.dumps({k:v for k,v in T.items() if k not in("D",)}))
