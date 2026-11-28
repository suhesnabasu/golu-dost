"""Ep13 timing: real Fish durations -> cue sheet + event times. usage: python3 timing.py <lines dir> <out timing.json>"""
import json, math, sys
LD, OUT = sys.argv[1], sys.argv[2]
D = {k: v["dur"] for k, v in json.load(open(f"{LD}/info.json")).items()}
CUES = []; END = [0.0]
def cue(lid, want, gap=0.15):
    t = round(max(want, END[0] + gap), 2); CUES.append((lid, t)); END[0] = t + D[lid]; return t
T = {}
PAUSE = 1.2
cue("s1", 0.15)
T["q1"] = cue("q1", END[0] + 0.15)
T["bun_in"] = round(END[0] + 0.05, 2)
T["b1"] = cue("b1", T["bun_in"] + 0.35)
T["x1"] = round(END[0] + 0.05, 2)
T["c1"] = cue("c1", END[0] + 0.3)
T["peek1"] = T["c1"] + 0.2
T["r1"] = cue("r1", END[0] + PAUSE)
cue("m1", END[0] + 0.15)
T["a1"] = cue("a1", END[0] + 0.15)
T["hide1"] = round(END[0] + 0.2, 2)
T["s2"] = cue("s2", END[0] + 0.55)
T["b2"] = cue("b2", END[0] + 0.15)
T["x2"] = round(END[0] + 0.05, 2)
T["c2"] = cue("c2", END[0] + 0.25)
T["c3"] = cue("c3", END[0] + 0.25)
T["peek2"] = T["c3"] + 0.1
T["r2"] = cue("r2", END[0] + PAUSE)
cue("m2", END[0] + 0.15)
T["a2"] = cue("a2", END[0] + 0.15)
T["hide2"] = round(END[0] + 0.2, 2)
T["s3"] = cue("s3", END[0] + 0.55)
T["b3a"] = cue("b3a", END[0] + 0.3)
T["c4"] = cue("c4", END[0] + 0.25)
T["peek3"] = T["c4"] + 0.1
T["b3b"] = cue("b3b", END[0] + PAUSE)
T["r3"] = cue("r3", END[0] + 0.15)
T["m3"] = cue("m3", END[0] + 0.3)
T["feather"] = round(T["m3"] - 0.35, 2)
T["a3"] = cue("a3", END[0] + 0.15)
T["hide3"] = round(END[0] + 0.2, 2)
T["k2"] = cue("k2", END[0] + 0.45)
T["g2"] = cue("g2", END[0] + 0.35)
T["g3"] = cue("g3", END[0] + 0.12)
T["DUR"] = round(math.ceil((END[0] + 0.9) * 4) / 4, 2)
T["CUES"] = CUES; T["D"] = D
json.dump(T, open(OUT, "w"), indent=1)
print("DUR", T["DUR"]); print(CUES)
