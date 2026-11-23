"""Fallback: Kokoro voices (voices2.py) with code-mixed lines split into Hindi / English chunks."""
import json, os, re, sys
import numpy as np, soundfile as sf
os.environ.setdefault("KOKORO_DIR", "/home/claude/golu_pipeline")
sys.path.insert(0, "/home/claude/golu_pipeline")
import voices2 as v2
exec(open("/home/claude/ep5work/lines.py").read())
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
def chunks(text):
    parts = re.findall(r"[ऀ-ॿ][ऀ-ॿ\s,!?।\-]*|[A-Za-z][A-Za-z\s,!?'\-]*", text)
    return [(p.strip(), "hi" if re.match(r"[ऀ-ॿ]", p) else "en-us") for p in parts if p.strip()]
info = {}
for lid, role, lang, text in LINES:
    segs = chunks(text)
    if len(segs) == 1 and segs[0][1] == lang:
        v2.make([(lid, role, lang, text)], OUT + "/_tmp")
        a = sf.read(f"{OUT}/_tmp/{lid}.wav")[0]
    else:
        pieces = []
        for j, (t, lg) in enumerate(segs):
            v2.make([(f"{lid}_{j}", role, lg, t)], OUT + "/_tmp")
            pieces += [sf.read(f"{OUT}/_tmp/{lid}_{j}.wav")[0], np.zeros(int(.08 * 44100))]
        a = np.concatenate(pieces[:-1])
    sf.write(f"{OUT}/{lid}.wav", a, 44100)
    info[lid] = {"role": role, "dur": round(len(a) / 44100, 2)}
json.dump(info, open(f"{OUT}/info.json", "w"), indent=1)
print(info)
