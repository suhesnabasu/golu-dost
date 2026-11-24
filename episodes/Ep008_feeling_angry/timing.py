"""Ep8 timing: places every voice line (real durations from info.json) and derives the story event times.
usage: python3 timing.py [out timing.json]"""
import json, math, os, sys
LD = os.environ.get("GOLU_LINES", "/home/claude/ep8/lines")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/ep8/timing.json"
D = {k: v["dur"] for k, v in json.load(open(f"{LD}/info.json")).items()}
CUES = []; END = [0.0]
def cue(lid, want):
    t = round(max(want, END[0] + 0.15), 2); CUES.append((lid, t)); END[0] = t + D[lid]; return t
T = {}
# HOOK: last block goes on (0.0-0.6), Bunny zooms in, skid, CRASH, block-hat on Mithu
cue("a1", 0.15); T["place"] = 0.6
T["bin"] = max(1.0, END[0] - 0.1)                  # Bunny starts zooming in
cue("a2", T["bin"] + 0.2)
T["skid"] = T["bin"] + 0.45
T["crash"] = round(max(END[0] + 0.05, T["skid"] + 0.6), 2)
T["hat"] = T["crash"] + 0.75
cue("a3", T["hat"] + 0.1)
# ANGER take
T["take"] = END[0] + 0.15
cue("b1", T["take"] + 0.1)
T["angry"] = T["take"] + 0.45; T["stomp"] = T["take"] + 0.5
cue("b2", END[0] + 0.15); cue("b3", END[0] + 0.12)
# lifts a block up high, Bunny says sorry, kids: stop! breathe!
T["lift"] = END[0] + 0.1
cue("c1", T["lift"] + 0.35)
T["stop"] = cue("c2", END[0] + 0.2); T["freeze"] = T["stop"] + 0.2
cue("c3", END[0] + 0.12)
T["lower"] = END[0] + 0.1
# BREATHING x3
T["in1"] = cue("d1", T["lower"] + 0.55)
T["out1"] = cue("d2", END[0] + 0.3)
T["in2"] = cue("d3", END[0] + 0.45)
T["out2"] = round(T["in2"] + D["d3"] * 0.55, 2)
cue("d4", END[0] + 0.35)
T["in3"] = END[0] + 0.25; T["out3"] = T["in3"] + 1.1; T["calm"] = T["out3"] + 0.95
# WORDS
T["felt"] = cue("e1", T["calm"] + 0.2)
T["ok"] = cue("e2b", END[0] + 0.3); cue("e2c", END[0] + 0.12)
T["forgive"] = cue("e3", END[0] + 0.3)
T["tog"] = cue("e4", END[0] + 0.15)
# REBUILD: blocks 1,2 on the beat, Bunny slow-motion block 3, block 4
rb = T["tog"] + D["e4"] * 0.5; T["rb"] = rb
T["RB"] = [rb, rb + 0.5, rb + 1.0, rb + 2.6]       # start times; block 3 lands at rb+2.4 (slow-mo)
T["rb_end"] = rb + 3.2
# MORAL + BYE + LOOP
T["moral"] = cue("f1a", rb + 1.3); T["m1"] = cue("f1b", END[0] + 0.15)
T["f2"] = cue("f2", END[0] + 0.15)
T["bye"] = cue("g1", END[0] + 0.25)
cue("g2", END[0] + 0.15)
T["DUR"] = round(math.ceil((END[0] + 0.95) * 4) / 4, 2)
T["CUES"] = CUES; T["D"] = D
json.dump(T, open(OUT, "w"), indent=1)
print("DUR", T["DUR"]); print(CUES)
