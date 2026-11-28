"""Ep12 timing: places every voice line (real Fish durations) and derives the action times.
usage: python3 timing.py <lines dir> <out timing.json>"""
import json, math, sys
LD, OUT = sys.argv[1], sys.argv[2]
D = {k: v["dur"] for k, v in json.load(open(f"{LD}/info.json")).items()}
CUES = []; END = [0.0]
def cue(lid, want, gap=0.15):
    t = round(max(want, END[0] + gap), 2); CUES.append((lid, t)); END[0] = round(t + D[lid], 2); return t
T = {}
T["land0"] = 0.25                      # hook: Golu drops onto the web — BOING
cue("a1", 0.35)
cue("m0", END[0] + 0.12)
T["swing"] = cue("a2", END[0] + 0.15)
T["fun1"] = cue("a3", END[0] + 0.15)
T["call1"] = cue("a4", END[0] + 0.15)
T["pari"] = END[0] + 0.05; T["pland"] = round(T["pari"] + 0.6, 2)
cue("b1", T["pland"] + 0.05)
T["e1"] = cue("e1", END[0] + 0.2)
T["e2"] = cue("e2", END[0] + 0.1)
T["fun2"] = cue("e3", END[0] + 0.15)
T["call2"] = cue("e4", END[0] + 0.1)
T["chintu"] = END[0] + 0.05; T["cland"] = round(T["chintu"] + 0.6, 2)
cue("c1", T["cland"] + 0.05)
T["count"] = cue("c2", END[0] + 0.2)
T["boing"] = round(END[0] + 0.2, 2)    # biggest bounce
T["hat"] = round(T["boing"] + 1.45, 2)
cue("m1", T["hat"] + 0.1)
T["well"] = cue("s1", END[0] + 0.15)
T["recap"] = cue("d1", END[0] + 0.25)
T["four"] = cue("g1", END[0] + 0.3)
T["you"] = cue("g2", END[0] + 0.1)
T["bye"] = cue("g3", END[0] + 0.2)
T["exit"] = round(END[0] + 0.05, 2)
cue("g4", END[0] + 0.1)
T["DUR"] = round(math.ceil((END[0] + 1.1) * 4) / 4, 2)
T["CUES"] = CUES; T["D"] = D
json.dump(T, open(OUT, "w"), indent=1)
print("DUR", T["DUR"]); print(CUES)
