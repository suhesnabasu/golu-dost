import json, math, os, sys
LD = os.environ.get("GOLU_LINES", "/home/claude/ep9work/lines")
OUT = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/ep9work/timing.json"
D = {k: v["dur"] for k, v in json.load(open(f"{LD}/info.json")).items()}
def snap(t): return math.ceil(t * 4 - 1e-6) / 4
T = {}; CUES = []
def cue(lid, t): CUES.append((lid, round(t, 2))); return t + D[lid]
e = cue("a1", 0.25)
T["plane0"] = 0.5
e = cue("a2", max(snap(e + 0.12), 1.5))
T["intro"] = round(e + 0.1, 2)
V = []
for k, (g, m, kd) in enumerate([("c1", "c2", "c3"), ("d1", "d2", "d3"), ("e1", "e2", "e3"), ("f1", "f2", "f3")]):
    v = {"in": round(e - 0.3, 2) if k == 0 else round(e - 0.3, 2)}
    v["g"] = round(v["in"] + 0.5, 2)
    e = cue(g, v["g"]); v["m"] = round(e + 0.12, 2); e = cue(m, v["m"])
    v["k"] = round(e + 0.12, 2); e = cue(kd, v["k"])
    if k == 2:
        v["fling"] = round(e - 0.2, 2); v["land"] = round(v["fling"] + 0.6, 2)
        v["hat"] = round(v["land"] + 0.15, 2); e = cue("e4", v["hat"])
    v["out"] = round(e + 0.05, 2)
    e = v["out"] + 0.45
    V.append(v)
T["V"] = V
T["bun"] = round(V[3]["out"] + 0.7, 2)
e = cue("g0", T["bun"] + 0.55)
T["wait"] = round(e, 2)
T["recap"] = round(e + 0.35, 2); e = cue("g1", T["recap"])
for h in ("h1", "h2"):
    T[h] = round(e + 0.12, 2); e = cue(h, T[h])
T["end"] = round(e + 0.25, 2); e = cue("k1", T["end"]); T["k2"] = round(e + 0.12, 2); e = cue("k2", T["k2"])
T["DUR"] = snap(e + 0.9)
T["CUES"] = CUES; T["D"] = D
json.dump(T, open(OUT, "w"), indent=1)
print("DUR", T["DUR"], [v["in"] for v in V], T["recap"], T["end"])
