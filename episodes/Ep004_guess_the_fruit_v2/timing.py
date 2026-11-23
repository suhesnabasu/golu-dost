import json, math, os
LD = os.environ.get("GOLU_LINES", "/home/claude/golu_pipeline/lines")
D = {k: v["dur"] for k, v in json.load(open(f"{LD}/info.json")).items()}
def snap(t): return math.ceil(t * 2 - 1e-6) / 2
T = {}; CUES = []
def cue(lid, t): CUES.append((lid, round(t, 2))); return t + D[lid]
e = cue("a1", 0.30); e = cue("a2", snap(e + 0.15))
T["intro"] = snap(e + 0.15); e = cue("b1", T["intro"]); T["b2"] = snap(e + 0.15); e = cue("b2", T["b2"])
R = []
for c, cen, d1, d2 in [("c1", "c2", "d1", "d2"), ("e1", "e2", "f1", "f2"), ("g1", "g2", "h1", "h2")]:
    t0 = snap(e + 0.3); r = {"t0": t0}
    e = cue(c, t0); r["en"] = snap(e + 0.15); e = cue(cen, r["en"])
    r["q"] = snap(e + 0.15); e = cue("q", r["q"])
    r["cd"] = snap(e + 0.1)          # countdown 3-2-1 on three beats
    r["rev"] = r["cd"] + 1.5
    e = cue(d1, r["rev"] + 0.1); r["en2"] = snap(e + 0.15); e = cue(d2, r["en2"])
    r["end"] = snap(e + 0.3); R.append(r)
T["R"] = R
T["recap"] = snap(e + 0.3); e = cue("i1", T["recap"]); T["i2"] = snap(e + 0.15); e = cue("i2", T["i2"])
T["j1"] = snap(e + 0.2); e = cue("j1", T["j1"]); T["j2"] = snap(e + 0.15); e = cue("j2", T["j2"])
T["end"] = snap(e + 0.4); e = cue("k1", T["end"]); T["k2"] = snap(e + 0.15); e = cue("k2", T["k2"])
T["DUR"] = snap(e + 0.8)
T["CUES"] = CUES; T["D"] = D
json.dump(T, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"timing.json"), "w"), indent=1)
print(T["DUR"], [r["rev"] for r in R], T["recap"], T["end"])
