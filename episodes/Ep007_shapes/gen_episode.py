"""Golu & Dost Ep 7 — गोलू के आकार #1: आकार सीखो | Learn Shapes (soft-3D glossy, Golu's kitchen on a winter morning).
usage: python3 gen_episode.py <project dir>   (needs timing.json next to this file and <proj>/assets/lips.json)"""
import json, math, sys, os, random
PROJ = sys.argv[1]; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json")); DUR = T["DUR"]; D = T["D"]
CUE = dict((k, v) for k, v in T["CUES"])
lips = json.load(open(f"{PROJ}/assets/lips.json"))
END = lambda lid: CUE[lid] + D[lid]

# ---- v2 cast from the series template (GOLU, KIDS, gradients, f3d) + glossy Mithu (Ep4-6 cast file)
tsrc = open("/home/claude/golu_pipeline/gen_episode_template.py").read()
ns = {"math": math}
exec(tsrc[tsrc.index("COLS = ["):tsrc.index("def overlays():")], ns)
rg, GOLU, KIDS, cloud = ns["rg"], ns["GOLU"], ns["KIDS"], ns["cloud"]
# scarf knot fix (bible: yellow knot always visible): the template's knot sits under the trunk; add a big visible knot on the left of the collar
FLAP = '<path d="M-12,-238 l-34,58 l52,-30z" fill="#ff9a5c"/><circle cx="0" cy="-236" r="13" fill="#ffd24a"/>'
assert FLAP in GOLU
GOLU = GOLU.replace(FLAP, FLAP + '<g transform="translate(-52,-220)"><ellipse cx="-17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(-18 -17 0)"/><ellipse cx="17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(18 17 0)"/><circle r="12" fill="#ffd24a" stroke="#e09400" stroke-width="3"/><circle cx="-4" cy="-4" r="4" fill="#fff6c0"/></g>')
F3D = tsrc[tsrc.index('<filter id="f3d"'):tsrc.index('</filter>') + len('</filter>')]
MITHU = open(f"{HERE}/cast/mithu_src.txt").read()
def lg(id_, stops, x2=0, y2=1):
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="{x2}" y2="{y2}">' + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops) + '</linearGradient>'
defs = ns["defs"] + F3D + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    rg("gRoti", [(0, "#fff1c9"), (.55, "#f5d28c"), (1, "#d9a55a")], "40%", "35%", "70%"),
    rg("gBisc", [(0, "#ffe3a3"), (.6, "#f0b85c"), (1, "#c9822e")], "38%", "32%", "80%"),
    rg("gSamo", [(0, "#ffd98a"), (.55, "#eaa645"), (1, "#b8701f")], "45%", "55%", "75%"),
    rg("gGlow", [(0, "#ffffff"), (.55, "#fff7dc"), (1, "#fff7dc00")], "50%", "50%", "50%"),
    rg("gSunW", [(0, "#fff6d0"), (.5, "#ffd98a"), (1, "#ffb86a")], "45%", "40%", "60%"),
    rg("gJar", [(0, "#ffffff"), (.5, "#d8f1ff"), (1, "#9fcde8")], "35%", "30%", "75%"),
    rg("gCup", [(0, "#ffffff"), (.5, "#d6dde6"), (1, "#8e9aa8")], "35%", "30%", "75%"),
    lg("gWall", [(0, "#fff3dc"), (.7, "#ffe6bf"), (1, "#ffd9a6")]),
    lg("gWin", [(0, "#bfe3ff"), (.6, "#e6f2ff"), (1, "#ffe1c4")]),
    lg("gFloor", [(0, "#f6c58f"), (1, "#e9a868")]),
    lg("gWood", [(0, "#d99a5b"), (1, "#a8693a")]),
    lg("gCounter", [(0, "#8fd0c4"), (1, "#5fae9f")]),
    '<filter id="fblur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>',
    '<filter id="fmist" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="10"/></filter>',
])

ka, kb = KIDS[KIDS.index('<g id="kidA"'):KIDS.index('<g id="kidB"')], KIDS[KIDS.index('<g id="kidB"'):]
ka = ka.replace(' transform="translate(150,1880) scale(.78)"', '')
kb = kb.replace(' transform="translate(930,1880) scale(.78)"', '')
GX, GY, GS = 540, 1840, .62          # Golu feet + scale
KS = .5                              # kids scale
SHOW = (540, 1000)                   # the "show spot" where each food is presented
HEAD = (540, 1500)                   # roti-hat spot on Golu's head (world)
ROTI_R, ROTI_SMALL = 150, .42
RY = 860                             # recap row

# ---- on-screen words (Hindi big, English below)
WORDS = [
    ("wFly", "रोटी उड़ी!", "Flying roti!", "#c43e00", "#1565c0"),
    ("wHat", "ठक! टोपी!", "Bonk! A hat!", "#a65500", "#1565c0"),
    ("wLearn", "चलो, आकार सीखें!", "Let's learn shapes!", "#d81b60", "#1565c0"),
    ("wCircle", "गोल", "Circle", "#e91e63", "#1565c0"),
    ("wSquare", "चौकोर", "Square", "#1e63d6", "#c2185b"),
    ("wTri", "तिकोना", "Triangle", "#2e7d32", "#c2185b"),
    ("wAgain", "चलो फिर से!", "Let's do it again!", "#6a1fc2", "#1565c0"),
    ("wBye", "कल फिर मिलेंगे!", "See you tomorrow!", "#6a1fc2", "#1565c0"),
]
RECAP = [("rc0", "गोल", "Circle", "#e91e63", 300), ("rc1", "चौकोर", "Square", "#1e63d6", 540), ("rc2", "तिकोना", "Triangle", "#2e7d32", 780)]
def overlays():
    w = ""
    for i, hi, en, hc, ec in WORDS:
        w += f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div><div class="en" style="color:{ec}">{en}</div></div>'
    for i, hi, en, c, x in RECAP:
        w += f'<div class="rlab" id="{i}" style="left:{x-130}px"><div class="hi" style="color:{c}">{hi}</div><div class="en" style="color:{c}">{en}</div></div>'
    return w + '<div class="badge">गोलू के आकार #1 · Golu\'s Shapes</div>'

J = []
def tl(s): J.append(s)
def f(v): return f"{v:.3f}"
def word_in(i, t, punch=True):
    tl(f'tl.fromTo("#{i}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.35,ease:"back.out(1.5)",immediateRender:false}},{f(t)});')
    if punch: tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.04,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def word_out(i, t): tl(f'tl.to("#{i}",{{opacity:0,scale:.6,duration:.18,ease:"power2.in"}},{f(t)});')
def card(i, t0, t1, punch=True): word_in(i, t0, punch); word_out(i, t1 - .18)
def happy(t0, t1):
    tl(f'tl.set("#g-eyes",{{opacity:0}},{f(t0)}); tl.set("#g-happy",{{opacity:1}},{f(t0)}); tl.set("#g-eyes",{{opacity:1}},{f(t1)}); tl.set("#g-happy",{{opacity:0}},{f(t1)});')
def look(x, t, y=0): tl(f'tl.to(".pup",{{x:{x},y:{y},duration:.2,ease:"power2.out"}},{f(t)});')
def trunk(rot, t, d=.25, ease="back.out(2)"): tl(f'tl.to("#g-trunk",{{rotation:{rot},svgOrigin:"0 -352",duration:{d},ease:"{ease}"}},{f(t)});')
def mithu_talk(t, dur):
    n = max(1, int(round(dur / 0.5)))
    tl(f'tl.to("#m-head",{{rotation:-10,svgOrigin:"18 -140",duration:.25,yoyo:true,repeat:{2*n-1},ease:"sine.inOut"}},{f(t)});')
    tl(f'tl.to("#m-jaw",{{y:8,duration:.125,yoyo:true,repeat:{4*n-1}}},{f(t)});')
    tl(f'tl.to("#m-all",{{y:-24,duration:.25,yoyo:true,repeat:{2*n-1},ease:"power2.out"}},{f(t)});')
def kids_talk(t, dur):
    for k, d in (("A", 0), ("B", .05)):
        n = int(dur / .11)
        tl(f'tl.set("#kid{k} .ksmile",{{opacity:0}},{f(t+d)});')
        for j in range(n):
            big = j % 2 == 0
            tl(f'tl.set("#kid{k} .kmouth",{{opacity:{1 if big else 0}}},{f(t+d+j*.11)}); tl.set("#kid{k} .ksmall",{{opacity:{0 if big else 1}}},{f(t+d+j*.11)});')
        tl(f'tl.set("#kid{k} .kmouth",{{opacity:0}},{f(t+d+n*.11)}); tl.set("#kid{k} .ksmall",{{opacity:0}},{f(t+d+n*.11)}); tl.set("#kid{k} .ksmile",{{opacity:1}},{f(t+d+n*.11)});')
def kids_cheer(t, hold=.8, who=("A", "B")):
    for k, d in (("A", 0), ("B", .07)):
        if k not in who: continue
        tl(f'tl.to("#k{k}-armL",{{rotation:80,duration:.18,ease:"back.out(2)"}},{f(t+d)}); tl.to("#k{k}-armR",{{rotation:-80,duration:.18,ease:"back.out(2)"}},{f(t+d+.05)});')
        tl(f'tl.to("#k{k}-armL",{{rotation:0,duration:.3,ease:"power2.inOut"}},{f(t+d+hold)}); tl.to("#k{k}-armR",{{rotation:0,duration:.3,ease:"power2.inOut"}},{f(t+d+hold+.06)});')
def kid_point(k, t, hold):
    # one arm up towards the food (Pari's right arm / Chintu's left arm point inwards to the centre)
    arm, rot = (f"#k{k}-armR", -55) if k == "A" else (f"#k{k}-armL", 55)
    tl(f'tl.to("{arm}",{{rotation:{rot},duration:.2,ease:"back.out(2)"}},{f(t)}); tl.to("{arm}",{{rotation:{rot*0.85:.0f},duration:.15,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(t+.2)});')
    tl(f'tl.to("{arm}",{{rotation:0,duration:.3,ease:"power2.inOut"}},{f(t+hold)});')
def golu_arm(side, rot, t, hold, wave=False):
    sel, o = ("#g-armR", "128 -226") if side == "R" else ("#g-armL", "-128 -226")
    tl(f'tl.to("{sel}",{{rotation:{rot},svgOrigin:"{o}",duration:.22,ease:"back.out(2)"}},{f(t)});')
    if wave: tl(f'tl.to("{sel}",{{rotation:{rot + (18 if rot < 0 else -18)},svgOrigin:"{o}",duration:.16,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(t+.22)});')
    tl(f'tl.to("{sel}",{{rotation:0,svgOrigin:"{o}",duration:.3,ease:"power2.inOut"}},{f(t+hold)});')
def g_hop(t, h=26):
    tl(f'tl.fromTo("#rgolu",{{y:0}},{{y:{-h},duration:.16,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def g_squash(t, amt=.1):
    tl(f'tl.fromTo("#rgolu",{{scaleX:1,scaleY:1}},{{scaleX:{1+amt},scaleY:{1-amt},svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')

# ---- food positions: wrapper #f<x> holds translate+scale (attr transform), inner #fi<x> spins/squashes
FS = {}
def tf(x, y, s): return f"translate({x:.1f},{y:.1f}) scale({s:.3f})"
def fset(k, x, y, s): FS[k] = (x, y, s); tl(f'gsap.set("#f{k}",{{attr:{{transform:"{tf(x, y, s)}"}}}});')
def fmove(k, t, x, y, s=None, d=.5, ease="power2.inOut"):
    x0, y0, s0 = FS[k]; s = s0 if s is None else s
    tl(f'tl.fromTo("#f{k}",{{attr:{{transform:"{tf(x0, y0, s0)}"}}}},{{attr:{{transform:"{tf(x, y, s)}"}},duration:{d},ease:"{ease}",immediateRender:false}},{f(t)});')
    FS[k] = (x, y, s)
def fpop(k, t, x, y, s=1.0):
    x0, y0, _ = FS[k]
    tl(f'tl.fromTo("#f{k}",{{attr:{{transform:"{tf(x, y, .05)}"}}}},{{attr:{{transform:"{tf(x, y, s)}"}},duration:.4,ease:"back.out(1.8)",immediateRender:false}},{f(t)});')
    FS[k] = (x, y, s)
def at(sel, t, a, b, d, ease="power2.out", yoyo=0):
    y = f",yoyo:true,repeat:{yoyo}" if yoyo else ""
    tl(f'tl.fromTo("{sel}",{{attr:{{transform:"{a}"}}}},{{attr:{{transform:"{b}"}},duration:{d},ease:"{ease}"{y},immediateRender:false}},{f(t)});')
def glow(t0, t1):
    tl(f'tl.fromTo("#glow",{{opacity:0}},{{opacity:1,duration:.4,ease:"power2.out",immediateRender:false}},{f(t0)}); tl.to("#glow",{{opacity:0,duration:.2}},{f(t1-.35)});')
    at("#glowS", t0, "scale(0.6)", "scale(1)", .4)
def trace(sel, length, t, d=1.0, hide=None):
    tl(f'tl.fromTo("{sel}",{{strokeDashoffset:{length},opacity:1}},{{strokeDashoffset:0,duration:{d},ease:"power1.inOut",immediateRender:false}},{f(t)});')
    if hide: tl(f'tl.to("{sel}",{{opacity:0,duration:.2}},{f(hide)});')
def badges(prefix, n, t, step, hide):
    for k in range(n):
        tl(f'tl.fromTo("#{prefix}{k}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,transformOrigin:"50% 50%",duration:.22,ease:"back.out(2)",immediateRender:false}},{f(t+k*step)});')
        tl(f'tl.to("#{prefix}{k}",{{opacity:0,duration:.2}},{f(hide)});')

def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set(".rlab",{opacity:0,scale:.3}); gsap.set(".cbadge",{opacity:0}); gsap.set(".conf",{opacity:0}); gsap.set(".outl",{opacity:0}); gsap.set("#glow",{opacity:0}); gsap.set("#bonk",{opacity:0});')
    tl('gsap.set("#g-trunk",{svgOrigin:"0 -352",rotation:-30}); gsap.set("#g-ear",{svgOrigin:"-90 -380"}); gsap.set("#g-ear2",{svgOrigin:"90 -380"});')
    tl('gsap.set("#kA-armL",{svgOrigin:"-62 -230"}); gsap.set("#kA-armR",{svgOrigin:"62 -230"}); gsap.set("#kB-armL",{svgOrigin:"-60 -232"}); gsap.set("#kB-armR",{svgOrigin:"60 -232"});')
    nb = int(DUR / BEAT)
    # idle life on the beat (offset, never in unison)
    tl(f'tl.to("#g-body",{{scaleY:.955,scaleX:1.022,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-head",{{y:9,rotation:2,svgOrigin:"0 -240",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#kA",{{y:-8,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.1);')
    tl(f'tl.to("#kB",{{y:-7,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.33);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.2);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.45);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#hand",{{rotation:360,svgOrigin:"1005 700",duration:{DUR},ease:"none"}},0);')
    tl(f'tl.to("#steam",{{y:-14,opacity:.35,duration:1.2,yoyo:true,repeat:{int(DUR/1.2)-1},ease:"sine.inOut"}},0);')
    for i, d in enumerate([40, -30]):
        tl(f'tl.fromTo("#mist{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    for k in range(int(DUR / 3)):
        t = 2.2 + k * 3.0
        if t > DUR - 1.5: break
        tl(f'tl.to("#g-ear",{{rotation:-8,duration:.15,yoyo:true,repeat:1}},{t:.2f}); tl.to("#g-ear2",{{rotation:8,duration:.15,yoyo:true,repeat:1}},{t+.12:.2f});')

    # ===== HOOK: a roti is already flying at frame 0 -> apex -> lands on Golu's head like a hat (ठक!)
    tl('tl.set("#wFly",{opacity:1,scale:.85},0); tl.to("#wFly",{scale:1,duration:.3,ease:"back.out(3)"},0.02);')
    fset("r", 150, 880, ROTI_SMALL)
    look(-12, 0, -8); look(0, T["apex"], -14)
    ap, ld = T["apex"], T["land"]
    tl(f'tl.fromTo("#fr",{{attr:{{transform:"{tf(150,880,ROTI_SMALL)}"}}}},{{attr:{{transform:"{tf(360,690,ROTI_SMALL)}"}},duration:{ap},ease:"power2.out",immediateRender:false}},0);')
    tl(f'tl.to("#fr",{{attr:{{transform:"{tf(HEAD[0],HEAD[1],ROTI_SMALL)}"}},duration:{ld-ap},ease:"power2.in"}},{f(ap)});')
    FS["r"] = (HEAD[0], HEAD[1], ROTI_SMALL)
    at("#fir", 0, "rotate(0)", "rotate(540)", ld, "none")
    at("#fiq", 0, "scale(1,1)", "scale(1,0.25)", .15, "sine.inOut", yoyo=3)
    at("#fiq", ld, "scale(1,1)", "scale(1,0.42)", .08, "power2.out")   # flattens into a hat
    g_squash(ld, .12); trunk(-70, ld, .18); trunk(-30, ld + .7, .4, "power2.inOut")
    tl(f'tl.set("#bonk",{{opacity:1}},{f(ld)}); tl.to("#bonk",{{opacity:0,duration:.2}},{f(ld+.7)});')
    at("#bonkS", ld, "scale(0.3)", "scale(1)", .25, "back.out(3)")
    word_out("wFly", ld - .35); card("wHat", ld, T["hop"] + .05)
    tl(f'tl.fromTo("#cam",{{scale:1}},{{scale:1.12,duration:.25,ease:"power2.out",immediateRender:false}},{f(ld)}); tl.to("#cam",{{scale:1,duration:.6,ease:"power2.inOut"}},{f(T["hop"]-.2)});')
    mithu_talk(CUE["a2"], D["a2"]); kids_cheer(ld + .15, .7); happy(ld + .35, T["hop"])
    # ===== SET-UP: the roti hops off the head into the show spot; "चलो, आकार सीखें!"
    hp = T["hop"]
    at("#fiq", hp, "scale(1,0.42)", "scale(1,1)", .2, "back.out(2)")
    at("#fir", hp, "rotate(540)", "rotate(900)", .6, "power2.out")
    fmove("r", hp, SHOW[0], SHOW[1], 1.0, .6, "back.out(1.4)"); g_hop(hp, 18); look(0, hp, -20)
    card("wLearn", T["learn"], T["circ"]); golu_arm("L", 100, T["learn"] + .1, .9); kids_cheer(T["learn"] + .2, .7)
    mithu_talk(CUE["b2"], D["b2"])
    # ===== CIRCLE
    c = T["circ"]; glow(c, T["sq"]); card("wCircle", c, T["sq"]); look(0, c, -18)
    trace("#oC", 1030, CUE["c1"] + .3, max(.8, D["c1"] - .2), hide=T["sq"])
    trunk(-60, CUE["c1"] + .1, .25); trunk(-30, END("c1"), .35, "power2.inOut")
    mithu_talk(CUE["c2"], D["c2"])
    kids_talk(CUE["c3a"], D["c3a"]); kids_talk(CUE["c3b"], D["c3b"]); kids_cheer(CUE["c3a"], .9); happy(CUE["c3a"], END("c3b") + .2)
    at("#fiq", CUE["c3a"], "scale(1,1)", "scale(1.08,1.08)", .25, "sine.inOut", yoyo=1)
    # ===== SQUARE: roti whooshes out, biscuit pops in, Chintu counts the corners
    s = T["sq"]; fmove("r", s - .15, 1320, SHOW[1] - 60, 1.0, .35, "power3.in")
    fset("b", SHOW[0], SHOW[1], .001); fpop("b", s + .1, SHOW[0], SHOW[1], 1.0)
    glow(s + .1, T["tri"]); card("wSquare", s + .1, T["tri"])
    trace("#oS", 1240, CUE["d1"] + .3, max(.8, D["d1"] - .2), hide=T["tri"])
    badges("sb", 4, CUE["d2"] + .05, D["d2"] / 4, T["tri"])
    kid_point("B", CUE["d2"], D["d2"] + .2); kids_talk(CUE["d2"], D["d2"])
    mithu_talk(CUE["d3"], D["d3"])
    kids_talk(CUE["d4a"], D["d4a"]); kids_talk(CUE["d4b"], D["d4b"]); kids_cheer(CUE["d4a"], .9); happy(CUE["d4a"], END("d4b") + .2)
    trunk(-60, CUE["d1"] + .1, .25); trunk(-30, END("d1"), .35, "power2.inOut")
    # ===== TRIANGLE: biscuit out, samosa pops in and wobbles, Pari counts
    r = T["tri"]; fmove("b", r - .15, -260, SHOW[1] - 60, 1.0, .35, "power3.in")
    fset("s", SHOW[0], SHOW[1], .001); fpop("s", r + .1, SHOW[0], SHOW[1], 1.0)
    at("#fis", r + .45, "rotate(-8,0,110)", "rotate(8,0,110)", .18, "sine.inOut", yoyo=3)
    at("#fis", r + 1.2, "rotate(-8,0,110)", "rotate(0,0,110)", .2, "power2.out")
    glow(r + .1, T["again"]); card("wTri", r + .1, T["again"])
    trace("#oT", 1000, CUE["e1"] + .3, max(.8, D["e1"] - .2), hide=T["again"])
    badges("tb", 3, CUE["e2"] + .05, D["e2"] / 3, T["again"])
    kid_point("A", CUE["e2"], D["e2"] + .2); kids_talk(CUE["e2"], D["e2"])
    mithu_talk(CUE["e3"], D["e3"])
    kids_talk(CUE["e4a"], D["e4a"]); kids_talk(CUE["e4b"], D["e4b"]); kids_cheer(CUE["e4a"], .9); happy(CUE["e4a"], END("e4b") + .2)
    trunk(-60, CUE["e1"] + .1, .25); trunk(-30, END("e1"), .35, "power2.inOut")
    # ===== RECAP: "चलो फिर से!" -> the three foods pop in a row on the beat, then the English
    a = T["again"]; fmove("s", a - .1, SHOW[0], SHOW[1] - 40, .05, .25, "power2.in")
    card("wAgain", a, T["f3"] - .05); g_hop(a + .1, 30); trunk(-80, a + .1, .2); trunk(-30, a + .8, .4, "power2.inOut")
    step = D["f2"] / 3
    for k, (key, x) in enumerate([("r", 300), ("b", 540), ("s", 780)]):
        t = T["f2"] + k * step
        if key == "r": tl(f'tl.set("#fir",{{attr:{{transform:"rotate(0)"}}}},{f(t-.01)}); tl.set("#fiq",{{attr:{{transform:"scale(1,1)"}}}},{f(t-.01)});')
        tl(f'tl.fromTo("#f{key}",{{attr:{{transform:"{tf(x,RY,.05)}"}}}},{{attr:{{transform:"{tf(x,RY,.55)}"}},duration:.35,ease:"back.out(2)",immediateRender:false}},{f(t)});')
        FS[key] = (x, RY, .55)
        tl(f'tl.fromTo("#{RECAP[k][0]}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)",immediateRender:false}},{f(t+.05)});')
        tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.03,duration:.12,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
    kids_talk(CUE["f2"], D["f2"]); kids_talk(CUE["f3"], D["f3"]); kids_cheer(CUE["f3"], 1.0)
    for k in range(3):   # English labels light up one by one on the English line
        tl(f'tl.fromTo("#{RECAP[k][0]} .en",{{scale:1}},{{scale:1.25,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(CUE["f3"]+k*D["f3"]/3)});')
    happy(CUE["f3"], END("f3") + .3); golu_arm("L", 110, CUE["f3"], 1.0); golu_arm("R", -110, CUE["f3"] + .06, 1.0)
    random.seed(7)
    for k in range(36):
        x0 = random.uniform(80, 1000); dly = random.uniform(0, .9); rot = random.uniform(-540, 540)
        tl(f'tl.fromTo("#cf{k}",{{x:{x0:.0f},y:700,rotation:0,opacity:1}},{{x:{x0 + random.uniform(-120,120):.0f},y:{random.uniform(1500,1900):.0f},rotation:{rot:.0f},duration:2.4,ease:"power1.in",immediateRender:false}},{f(CUE["f3"]+dly)}); tl.set("#cf{k}",{{opacity:0}},{f(CUE["f3"]+dly+2.4)});')
    # ===== BYE + LOOP: labels and foods leave, Golu waves; a new roti flies in from the left to the frame-0 spot
    by = T["bye"]
    for k, (key, x) in enumerate([("r", 300), ("b", 540), ("s", 780)]):
        tl(f'tl.to("#{RECAP[k][0]}",{{opacity:0,scale:.6,duration:.18}},{f(by-.25+k*.05)});')
        tl(f'tl.to("#f{key}",{{attr:{{transform:"{tf(x,RY,.001)}"}},duration:.22,ease:"power2.in"}},{f(by-.25+k*.05)});')
    word_in("wBye", by); word_out("wBye", DUR - .7); golu_arm("R", -100, by + .1, 1.4, wave=True); happy(by + .1, by + 1.2)
    mithu_talk(CUE["g2"], D["g2"]); kids_cheer(CUE["g2"], .8)
    # loop: new roti (#fr reused) flies in from off-screen left to (150,880) exactly at DUR; Fly card re-arms

    tl(f'tl.fromTo("#fr",{{attr:{{transform:"{tf(-140,1000,ROTI_SMALL)}"}}}},{{attr:{{transform:"{tf(150,880,ROTI_SMALL)}"}},duration:.7,ease:"power2.out",immediateRender:false}},{f(DUR-.72)});')
    at("#fir", DUR - .72, "rotate(-200)", "rotate(0)", .7, "none")
    look(-12, DUR - .5, -8)
    tl(f'tl.fromTo("#wFly",{{opacity:0,scale:.5}},{{opacity:1,scale:.85,duration:.3,ease:"power2.out",immediateRender:false}},{DUR-.35:.2f});')
    # ===== blinks (offset)
    t = 2.6
    while t < DUR - 1:
        if not any(x0 - .3 < t < x1 for x0, x1 in []):
            tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t:.2f});')
            tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.1:.2f});')
            tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+.6:.2f});')
            tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.9:.2f});')
        t += 3.3
    # ===== lip-sync: toggle pre-drawn mouths, scale with svgOrigin (never CSS transform-origin)
    Lv = list(lips["golu"])
    for i in range(1, len(Lv) - 1):
        if Lv[i] and not Lv[i-1] and not Lv[i+1]: Lv[i] = 0
    prev = 0; sc = [0, .5, .8, 1.1]
    for i, v in enumerate(Lv):
        t = round(i / lips["fps"], 3)
        if v == prev: continue
        if v == 0: tl(f'tl.set("#g-mouth",{{opacity:0}},{t});tl.set("#g-smile",{{opacity:1}},{t});')
        else: tl(f'tl.set("#g-mouth",{{opacity:1,scaleY:{sc[v]},svgOrigin:"-62 -314"}},{t});tl.set("#g-smile",{{opacity:0}},{t});')
        prev = v

# ---------------- set: Golu's kitchen, winter morning ----------------
def roti():
    random.seed(3)
    spots = "".join(f'<ellipse cx="{random.uniform(-110,110):.0f}" cy="{random.uniform(-110,110):.0f}" rx="{random.uniform(8,16):.0f}" ry="{random.uniform(5,10):.0f}" fill="#b97a3a" opacity="{random.uniform(.35,.6):.2f}"/>' for _ in range(16))
    return (f'<circle r="{ROTI_R}" fill="#c98f4a"/><circle r="{ROTI_R-6}" fill="url(#gRoti)"/>'
            f'<g clip-path="url(#clipRoti)">{spots}</g><ellipse cx="-40" cy="-60" rx="60" ry="26" fill="#fffbe9" opacity=".55" transform="rotate(-25 -40 -60)"/>')
def biscuit():
    holes = "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="#b8742a" opacity=".7"/>' for x in (-70, 0, 70) for y in (-70, 0, 70))
    return ('<rect x="-140" y="-140" width="280" height="280" rx="22" fill="#b87530"/><rect x="-134" y="-134" width="268" height="268" rx="18" fill="url(#gBisc)"/>'
            '<rect x="-112" y="-112" width="224" height="224" rx="12" fill="none" stroke="#d89a4c" stroke-width="5" stroke-dasharray="10 12" opacity=".8"/>'
            f'{holes}<ellipse cx="-60" cy="-90" rx="55" ry="18" fill="#fff3d0" opacity=".5"/>')
def samosa():
    crimp = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#c47d2a"/>' for x, y in
                    [(-150 + 300 * i / 9, 110) for i in range(1, 9)])
    return ('<path d="M0,-150 Q14,-150 22,-136 L158,96 Q166,116 144,116 L-144,116 Q-166,116 -158,96 L-22,-136 Q-14,-150 0,-150Z" fill="#a8621c"/>'
            '<path d="M0,-138 Q10,-138 16,-127 L146,92 Q151,106 136,106 L-136,106 Q-151,106 -146,92 L-16,-127 Q-10,-138 0,-138Z" fill="url(#gSamo)"/>'
            f'{crimp}<path d="M-30,-70 q-30,40 -50,90" stroke="#fff0c4" stroke-width="14" fill="none" stroke-linecap="round" opacity=".55"/>'
            '<path d="M0,-120 L0,96" stroke="#c98a36" stroke-width="5" opacity=".5"/>')
def kitchen():
    tiles = "".join(f'<rect x="{x}" y="{y}" width="58" height="58" rx="6" fill="{"#e6f6f2" if (x//60 + y//60) % 2 else "#d2eee8"}"/>' for x in range(0, 1080, 60) for y in range(1290, 1400, 60))
    floor = "".join(f'<rect x="{x}" y="{y}" width="118" height="78" fill="{"#f4c08a" if (x//120 + y//80) % 2 else "#eeb070"}"/>' for x in range(0, 1080, 120) for y in range(1500, 1920, 80))
    win = ('<g><rect x="56" y="666" width="300" height="340" rx="26" fill="url(#gWood)"/><rect x="74" y="684" width="264" height="304" rx="16" fill="url(#gWin)"/>'
           '<circle cx="250" cy="930" r="56" fill="url(#gSunW)"/><circle cx="250" cy="930" r="80" fill="#ffe2a8" opacity=".35"/>'
           '<g filter="url(#fblur)"><ellipse cx="130" cy="960" rx="90" ry="30" fill="#8fc78a"/><ellipse cx="290" cy="968" rx="110" ry="34" fill="#9ed197"/></g>'
           '<g filter="url(#fmist)" opacity=".8"><rect id="mist0" x="60" y="900" width="280" height="40" rx="20" fill="#ffffff"/><rect id="mist1" x="60" y="940" width="280" height="36" rx="18" fill="#ffffff"/></g>'
           '<rect x="200" y="684" width="12" height="304" fill="url(#gWood)"/><rect x="74" y="830" width="264" height="12" fill="url(#gWood)"/>'
           '<path d="M50,662 Q120,760 92,1010 L44,1010 Z" fill="#ff8fb3"/><path d="M362,662 Q292,760 320,1010 L368,1010 Z" fill="#ff8fb3"/>'
           '<rect x="40" y="648" width="336" height="22" rx="11" fill="#d4566f"/><rect x="48" y="1000" width="318" height="20" rx="10" fill="url(#gWood)"/></g>')
    clock = ('<g><circle cx="1005" cy="700" r="62" fill="#ff7a59"/><circle cx="1005" cy="700" r="50" fill="#fffaf0"/>'
             + "".join(f'<circle cx="{1005+40*math.sin(a*math.pi/6):.1f}" cy="{700-40*math.cos(a*math.pi/6):.1f}" r="4" fill="#7a4a2a"/>' for a in range(12)) +
             '<path d="M1005,700 L1005,758" stroke="#4a2a1a" stroke-width="7" stroke-linecap="round"/><g id="hand"><path d="M1005,700 L956,700" stroke="#d81b60" stroke-width="5" stroke-linecap="round"/></g><circle cx="1005" cy="700" r="6" fill="#4a2a1a"/></g>')
    shelf = ('<g><rect x="740" y="1248" width="340" height="22" rx="8" fill="url(#gWood)"/><path d="M780,1270 l20,36 M1040,1270 l-20,36" stroke="#a8693a" stroke-width="10" stroke-linecap="round"/>'
             '<g transform="translate(1010,1248)"><rect x="-30" y="-92" width="60" height="92" rx="16" fill="url(#gJar)"/><rect x="-34" y="-104" width="68" height="18" rx="7" fill="#ff7a59"/><rect x="-24" y="-40" width="48" height="36" rx="10" fill="#ffd36a" opacity=".85"/></g>'
             '<g transform="translate(1060,1248)"><rect x="-18" y="-62" width="36" height="62" rx="12" fill="url(#gJar)"/><rect x="-21" y="-72" width="42" height="14" rx="6" fill="#4fb3ff"/></g>'
             '<g transform="translate(790,1248)"><path d="M-26,-54 L26,-54 L20,0 L-20,0Z" fill="url(#gCup)"/><path d="M26,-42 q22,4 4,30" stroke="#b9c2cc" stroke-width="7" fill="none"/></g>'
             '<g id="steam" opacity=".6"><path d="M780,1180 q-12,-18 0,-34 q12,-16 0,-32" stroke="#ffffff" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M800,1186 q-10,-16 0,-30" stroke="#ffffff" stroke-width="7" fill="none" stroke-linecap="round"/></g></g>')
    ladles = ('<g><rect x="430" y="676" width="220" height="12" rx="6" fill="#a8693a"/>'
              '<path d="M470,688 L470,800" stroke="#b9c2cc" stroke-width="8" stroke-linecap="round"/><ellipse cx="470" cy="812" rx="20" ry="14" fill="url(#gCup)"/>'
              '<path d="M540,688 L540,790" stroke="#b9c2cc" stroke-width="8" stroke-linecap="round"/><rect x="526" y="788" width="28" height="30" rx="6" fill="url(#gCup)"/>'
              '<path d="M610,688 L610,800" stroke="#b9c2cc" stroke-width="8" stroke-linecap="round"/><circle cx="610" cy="816" r="18" fill="none" stroke="#b9c2cc" stroke-width="7"/></g>')
    counter = ('<rect x="0" y="1400" width="1080" height="34" fill="url(#gCounter)"/><rect x="0" y="1430" width="1080" height="80" fill="#4f9c8e"/>'
               '<rect x="0" y="1430" width="1080" height="10" fill="#3f8073" opacity=".6"/>'
               '<g transform="translate(150,1400)"><path d="M-70,-10 L70,-10 L56,-70 L-56,-70Z" fill="#c98a4a"/><path d="M-62,-30 L62,-30 M-58,-50 L58,-50" stroke="#a8693a" stroke-width="5"/>'
               '<circle cx="-24" cy="-78" r="26" fill="url(#gRoti)"/><circle cx="18" cy="-82" r="26" fill="url(#gRoti)"/></g>')
    return (f'<rect width="1080" height="1300" fill="url(#gWall)"/>{tiles}{win}{clock}{ladles}{shelf}{counter}'
            f'<rect x="0" y="1500" width="1080" height="420" fill="url(#gFloor)"/>{floor}'
            f'<rect x="0" y="1500" width="1080" height="14" fill="#c98a55" opacity=".5"/>')

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(36))
    sx, sy = SHOW
    glow = f'<g id="glow" transform="translate({sx},{sy})"><g id="glowS"><circle r="250" fill="url(#gGlow)"/></g></g>'
    outl = (f'<circle class="outl" id="oC" cx="{sx}" cy="{sy}" r="164" fill="none" stroke="#ff2f7a" stroke-width="12" stroke-linecap="round" stroke-dasharray="1030" transform="rotate(-90 {sx} {sy})"/>'
            f'<rect class="outl" id="oS" x="{sx-154}" y="{sy-154}" width="308" height="308" rx="8" fill="none" stroke="#1e63d6" stroke-width="12" stroke-linejoin="round" stroke-dasharray="1240"/>'
            f'<path class="outl" id="oT" d="M{sx},{sy-170} L{sx+178},{sy+124} L{sx-178},{sy+124}Z" fill="none" stroke="#2e9d3a" stroke-width="12" stroke-linejoin="round" stroke-dasharray="1000"/>')
    def badge(id_, x, y, n, col):
        return (f'<g transform="translate({x},{y})"><g class="cbadge" id="{id_}"><circle r="34" fill="#ffffff" stroke="{col}" stroke-width="7"/>'
                f'<text y="17" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="48" fill="{col}">{n}</text></g></g>')
    sq = [(sx-154, sy-154), (sx+154, sy-154), (sx+154, sy+154), (sx-154, sy+154)]
    tr = [(sx, sy-170), (sx+178, sy+124), (sx-178, sy+124)]
    bdg = "".join(badge(f"sb{k}", x, y, k+1, "#1e63d6") for k, (x, y) in enumerate(sq)) + "".join(badge(f"tb{k}", x, y, k+1, "#2e9d3a") for k, (x, y) in enumerate(tr))
    foods = (f'<g id="fb"><g id="fib" filter="url(#f3d)">{biscuit()}</g></g><g id="fs"><g id="fis"><g filter="url(#f3d)">{samosa()}</g></g></g>'
             f'<g id="fr"><g id="fir"><g id="fiq">{roti()}</g></g></g>')
    bonk = (f'<g id="bonk" transform="translate({HEAD[0]},{HEAD[1]-40})"><g id="bonkS">'
            + "".join(f'<path d="M0,-12 L4,-4 L12,-4 L6,2 L8,11 L0,6 L-8,11 L-6,2 L-12,-4 L-4,-4Z" fill="#ffd23f" stroke="#ff8a00" stroke-width="2" transform="translate({110*math.cos(a):.0f},{-60+40*math.sin(a):.0f}) scale(2.2)"/>' for a in (math.pi*.95, math.pi*1.25, math.pi*1.75, math.pi*2.05))
            + '</g></g>')
    mithu = f'<g filter="url(#f3d)"><g transform="translate(905,1250) scale(-.42,.42)">{MITHU}</g></g>'
    chars = (f'<g id="pgolu" transform="translate({GX},{GY}) scale({GS})"><g id="rgolu"><g id="gwrap" filter="url(#f3d)">{GOLU}</g></g></g>'
             f'<g transform="translate(150,{GY}) scale({KS})">{ka}</g><g transform="translate(930,{GY}) scale({KS})">{kb}</g>')
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}<clipPath id="clipRoti"><circle r="{ROTI_R-8}"/></clipPath></defs>
{kitchen()}
{mithu}
{chars}
{glow}
{foods}
{outl}
{bdg}
{bonk}
{conf}
</svg>'''
    css = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#fff3dc}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0;transform-origin:540px 1400px}
#punch{position:absolute;inset:0;transform-origin:50% 55%}
#world{position:absolute;inset:0}
#ovl{position:absolute;inset:0}
.word{position:absolute;left:120px;width:840px;top:380px;text-align:center;line-height:1.08;white-space:nowrap}
.word .hi{font-size:120px;font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(90,40,0,.18)}
.word .en{font-size:80px;font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(90,40,0,.18)}
.rlab{position:absolute;top:960px;width:260px;background:rgba(255,255,255,.82);border-radius:28px;padding:4px 0;text-align:center;line-height:1.02;white-space:nowrap}
.rlab .hi{font-size:60px;font-weight:800;-webkit-text-stroke:12px #fff;paint-order:stroke fill}
.rlab .en{font-size:44px;font-weight:800;-webkit-text-stroke:10px #fff;paint-order:stroke fill}
.badge{position:absolute;top:290px;left:150px;padding:12px 26px;border-radius:40px;background:rgba(255,255,255,.94);color:#e65100;font-size:38px;font-weight:800;box-shadow:0 6px 0 rgba(120,60,0,.15)}
"""
    fit = """
function fitWords(){ document.querySelectorAll('.word > div').forEach(function(el){
  if(!el.dataset.fs) el.dataset.fs = parseFloat(getComputedStyle(el).fontSize);
  var fs = +el.dataset.fs; el.style.fontSize = fs + 'px'; el.style.display='inline-block';
  while (el.offsetWidth > 680 && fs > 40) { fs -= 2; el.style.fontSize = fs + 'px'; }
  el.style.display='block'; }); }
fitWords(); if (document.fonts) document.fonts.ready.then(fitWords);"""
    js = "\n".join(J)
    return f'''<!doctype html><html lang="hi" data-resolution="portrait"><head><meta charset="UTF-8"/>
<script src="assets/gsap.min.js"></script><style>{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
  <audio id="song" class="clip" src="assets/song.mp3" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
  <div id="stage" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0"><div id="cam"><div id="punch">{svg}</div></div><div id="ovl">{overlays()}</div></div>
</div>
<script>
{fit}
const tl = gsap.timeline({{paused:true}});
{js}
tl.set({{}},{{}},{DUR});
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl; tl.seek(0);
</script></body></html>'''

open(f"{PROJ}/index.html", "w").write(html())
print("ok", len(J), "DUR", DUR)
