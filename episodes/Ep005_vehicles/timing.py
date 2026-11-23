import json, math, os, sys
LD = os.environ.get("GOLU_LINES", "/home/claude/golu_pipeline/lines")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/ep5work/timing.json"
D = {k: v["dur"] for k, v in json.load(open(f"{LD}/info.json")).items()}
def snap(t): return math.ceil(t * 4 - 1e-6) / 4
T = {}; CUES = []
def cue(lid, t): CUES.append((lid, round(t, 2))); return t + D[lid]
e = cue("a1", 0.25)
T["train0"] = 0.55                      # hook train zoom
e = cue("a2", max(snap(e + 0.12), 1.5))
T["intro"] = snap(e + 0.2); e = cue("b1", T["intro"])
V = []
for k, (g, m, kd) in enumerate([("c1", "c2", "c3"), ("d1", "d2", "d3"), ("e1", "e2", "e3"), ("f1", "f2", "f3")]):
    v = {"in": (snap(e + 0.2) if k == 0 else round(e + 0.35, 2))}   # vehicle starts driving in (after the previous one has cleared)
    v["g"] = v["in"] + 0.6              # stops at +0.7, golu line + card
    e = cue(g, v["g"]); v["m"] = snap(e + 0.12); e = cue(m, v["m"])
    v["k"] = snap(e + 0.12); e = cue(kd, v["k"])
    v["out"] = snap(e + 0.12)           # drives off (0.7 s)
    e = v["out"] + (1.3 - 0.35 if k == 0 else 0)
    V.append(v)
T["V"] = V
T["recap"] = snap(e + 0.6); e = cue("g1", T["recap"])
T["h1"] = snap(e + 0.12); e = cue("h1", T["h1"]); T["h2"] = snap(e + 0.12); e = cue("h2", T["h2"])
T["s1"] = snap(e + 0.12); e = cue("s1", T["s1"])
T["end"] = snap(e + 0.2); e = cue("k1", T["end"]); T["k2"] = snap(e + 0.12); e = cue("k2", T["k2"])
T["DUR"] = snap(e + 0.9)
T["CUES"] = CUES; T["D"] = D
json.dump(T, open(OUT, "w"), indent=1)
print("DUR", T["DUR"], [v["in"] for v in V], T["recap"], T["end"])
