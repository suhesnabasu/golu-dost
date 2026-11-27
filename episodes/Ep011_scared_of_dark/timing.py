"""Ep11 timing: places every voice line (real Fish durations) and derives the story event times.
usage: python3 timing.py <lines dir> <out timing.json>"""
import json, math, sys
LD, OUT = sys.argv[1], sys.argv[2]
D = {k: v["dur"] for k, v in json.load(open(f"{LD}/info.json")).items()}
CUES = []; END = [0.0]
def cue(lid, want, gap=0.15):
    t = round(max(want, END[0] + gap), 2); CUES.append((lid, t)); END[0] = t + D[lid]; return t
T = {}
cue("a1", 0.1); T["click"] = round(min(0.5, 0.1 + D["a1"] * 0.5), 2)
T["shadow"] = T["click"] + 0.25
T["gasp"] = END[0] + 0.05
cue("a2", T["gasp"] + 0.1)
cue("a3", END[0] + 0.15)
T["scared"] = cue("b1", END[0] + 0.25)
cue("b2", END[0] + 0.15)
T["okay"] = cue("c1", END[0] + 0.25)
cue("c2", END[0] + 0.12)
T["breath"] = END[0] + 0.15
T["torch"] = cue("c3", T["breath"] + 1.0)
T["count"] = cue("d1", END[0] + 0.3)
T["light"] = round(T["count"] + D["d1"] * 0.72, 2)
T["pop"] = T["light"] + 0.35
cue("d2", max(END[0] + 0.25, T["pop"] + 0.45))
T["giggle"] = cue("d3", END[0] + 0.2)
T["sock"] = END[0] + 0.1
cue("d4", T["sock"] + 0.55)
T["nl"] = cue("e1", END[0] + 0.35)
T["hug"] = cue("e2", END[0] + 0.25)
T["brave"] = cue("e3", END[0] + 0.25)
cue("e4", END[0] + 0.12)
T["moral"] = cue("f1", END[0] + 0.35)
T["f2"] = cue("f2", END[0] + 0.15)
T["bye"] = cue("g1", END[0] + 0.3)
cue("g2", END[0] + 0.15)
T["DUR"] = round(math.ceil((END[0] + 1.1) * 4) / 4, 2)
T["CUES"] = CUES; T["D"] = D
json.dump(T, open(OUT, "w"), indent=1)
print("DUR", T["DUR"]); print(CUES)
