"""Ep6 timing: places every voice line (real durations from info.json) and derives the story event times.
usage: python3 timing.py [out timing.json]"""
import json, math, os, sys
LD = os.environ.get("GOLU_LINES", "/home/claude/ep6work/lines")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/ep6work/timing.json"
D = {k: v["dur"] for k, v in json.load(open(f"{LD}/info.json")).items()}
CUES = []; END = [0.0]
def cue(lid, want):
    t = round(max(want, END[0] + 0.15), 2); CUES.append((lid, t)); END[0] = t + D[lid]; return t
T = {}
# HOOK: Bunny zooms in (0.15), climbs, slides, plops (2.0)
T["hook"] = {"in": 0.15, "climb": 0.55, "slide": 1.3, "land": 1.95}
cue("a1", 0.2); cue("a2", 1.35); T["plop1"] = T["hook"]["land"]; cue("a3", 2.4)
# PROBLEM: Pari steps up, Bunny cuts in (no touching); Chintu steps up, Bunny cuts in again
p1 = END[0] + 0.15; T["pari_step"] = p1
T["cut1"] = {"in": p1 + 0.35, "climb": p1 + 0.75, "slide": p1 + 1.35, "land": p1 + 1.95}
cue("b1", p1 + 0.4)
p2 = T["cut1"]["land"] + 0.35; T["chintu_step"] = p2
T["cut2"] = {"in": p2 + 0.35, "climb": p2 + 0.75, "slide": p2 + 1.35, "land": p2 + 1.95}
cue("b2", p2 + 0.5)
T["sad"] = cue("b3", T["cut2"]["land"] + 0.3)
T["lonely"] = cue("b4", END[0] + 0.2)
# LEARN
T["turns"] = cue("c1", END[0] + 0.3)
T["line_up"] = T["turns"] + 0.5
cue("c2", END[0] + 0.15)
T["count"] = cue("c3a", END[0] + 0.15); cue("c3b", END[0] + 0.12)
# RIDES: approach .6, climb 1.0, sit .25, slide .85 -> land at +2.7
RIDE_LEN = 2.7
def ride(start): return {"go": start, "climb": start + 0.6, "slide": start + 1.85, "land": start + RIDE_LEN, "back": start + RIDE_LEN + 0.25}
r1 = ride(END[0] + 0.35); cue("d1", r1["climb"] + 0.45)
r2 = ride(r1["land"] + 0.45); cue("d2", r2["climb"] + 0.45)
T["wait_hard"] = cue("d3a", max(END[0] + 0.2, r2["land"] - 0.2))
cue("d3", END[0] + 0.15); T["breath"] = END[0] + 0.05
T["praise"] = cue("d3b", END[0] + 0.15)
r3 = ride(END[0] + 0.15); cue("d4", r3["climb"] + 0.6)
r4 = ride(max(END[0], r3["land"]) + 0.35); T["golu_says"] = cue("d5", r4["go"] + 0.05)
T["plop2"] = r4["land"]; cue("d6", r4["land"] + 0.2)
T["R"] = [r1, r2, r3, r4]
# PAYOFF + LOOP
T["moral"] = cue("e1", max(END[0] + 0.25, r4["back"] + 0.9))
cue("e2a", END[0] + 0.15); cue("e2b", END[0] + 0.12)
T["together"] = cue("e3", END[0] + 0.2)
T["bye"] = cue("f1", END[0] + 0.2)
T["f2"] = cue("f2", END[0] + 0.15)
T["exit"] = T["f2"] + 0.5
T["DUR"] = round(math.ceil((END[0] + 0.55) * 4) / 4, 2)
T["CUES"] = CUES; T["D"] = D
json.dump(T, open(OUT, "w"), indent=1)
print("DUR", T["DUR"]); print(CUES)
