"""Ep7 timing: places every voice line (real durations from info.json) and derives the shape-lesson event times.
usage: python3 timing.py [out timing.json]"""
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LD = os.environ.get("GOLU_LINES", "/home/claude/ep7/lines")
OUT = sys.argv[1] if len(sys.argv) > 1 else f"{HERE}/timing.json"
D = {k: v["dur"] for k, v in json.load(open(f"{LD}/info.json")).items()}
CUES = []; END = [0.0]
def cue(lid, want):
    t = round(max(want, END[0] + 0.15), 2); CUES.append((lid, t)); END[0] = t + D[lid]; return t
T = {}
# HOOK: roti already flying at frame 0 -> apex -> lands on Golu's head (ठक!)
T["apex"] = 0.45; T["land"] = 1.25
cue("a1", 0.15)
T["a2"] = cue("a2", max(T["land"] + 0.35, END[0] + 0.12))
# SET-UP: roti hops off the head into the show spot
T["hop"] = END[0] + 0.1
T["learn"] = cue("b1", T["hop"] + 0.25); cue("b2", END[0] + 0.12)
# CIRCLE
T["circ"] = END[0] + 0.3; cue("c1", T["circ"] + 0.15)
T["c2"] = cue("c2", END[0] + 0.15); T["c3a"] = cue("c3a", END[0] + 0.15); cue("c3b", END[0] + 0.1)
# SQUARE
T["sq"] = END[0] + 0.4; cue("d1", T["sq"] + 0.3)
T["d2"] = cue("d2", END[0] + 0.15); T["d3"] = cue("d3", END[0] + 0.15)
T["d4a"] = cue("d4a", END[0] + 0.15); cue("d4b", END[0] + 0.1)
# TRIANGLE
T["tri"] = END[0] + 0.4; cue("e1", T["tri"] + 0.3)
T["e2"] = cue("e2", END[0] + 0.15); T["e3"] = cue("e3", END[0] + 0.15)
T["e4a"] = cue("e4a", END[0] + 0.15); cue("e4b", END[0] + 0.1)
# RECAP
T["again"] = cue("f1", END[0] + 0.4)
T["f2"] = cue("f2", END[0] + 0.15); T["f3"] = cue("f3", END[0] + 0.2)
# BYE + LOOP (a new roti flies in from the left at the very end = frame 0)
T["bye"] = cue("g1", END[0] + 0.35); T["g2"] = cue("g2", END[0] + 0.12)
T["DUR"] = round(math.ceil((END[0] + 0.7) * 4) / 4, 2)
T["CUES"] = CUES; T["D"] = D
json.dump(T, open(OUT, "w"), indent=1)
print("DUR", T["DUR"]); print(CUES)
