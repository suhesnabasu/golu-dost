"""Golu & Dost Ep 13 — गोलू की पहेली #2: बताओ कौन? | Guess the Animal (soft-3D glossy, Golu's sunny meadow + NEW bush,
NEW glossy cat / cow / duck peeking from the bush, Mithu's 6th hat = a yellow duck feather).
usage: python3 gen_episode.py <project dir>   (needs timing.json next to this file and <proj>/assets/lips.json)"""
import json, math, sys, os
PROJ = sys.argv[1]; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json")); DUR = T["DUR"]; D = T["D"]
CUE = dict((k, v) for k, v in T["CUES"])
lips = json.load(open(f"{PROJ}/assets/lips.json"))
END = lambda lid: CUE[lid] + D[lid]
def f(v): return f"{v:.3f}"

# ---- v2 cast from the series template + glossy Mithu + v2 Bunny
tsrc = open("/home/claude/golu_pipeline/gen_episode_template.py").read()
ns = {"math": math}
exec(tsrc[tsrc.index("COLS = ["):tsrc.index("def overlays():")], ns)
rg, GOLU, cloud, flower = ns["rg"], ns["GOLU"], ns["cloud"], ns["flower"]
FLAP = '<path d="M-12,-238 l-34,58 l52,-30z" fill="#ff9a5c"/><circle cx="0" cy="-236" r="13" fill="#ffd24a"/>'
assert FLAP in GOLU
GOLU = GOLU.replace(FLAP, FLAP + '<g transform="translate(-52,-220)"><ellipse cx="-17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(-18 -17 0)"/><ellipse cx="17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(18 17 0)"/><circle r="12" fill="#ffd24a" stroke="#e09400" stroke-width="3"/><circle cx="-4" cy="-4" r="4" fill="#fff6c0"/></g>')
F3D = tsrc[tsrc.index('<filter id="f3d"'):tsrc.index('</filter>') + len('</filter>')]
MITHU = open(f"{HERE}/mithu_src.txt").read()
# Mithu's 6th hat: a fluffy yellow duck feather (block, sand, leaf, sock, web puff, feather)
HAT = ('<g id="m-hat" opacity="0"><g transform="translate(14,-262) rotate(-24)">'
       '<path d="M0,0 C-30,-40 -26,-104 6,-132 C34,-100 34,-40 0,0Z" fill="url(#gFeather)"/>'
       '<path d="M2,-4 Q4,-60 6,-126" stroke="#e0a000" stroke-width="4" fill="none" stroke-linecap="round"/>'
       '<ellipse cx="-8" cy="-86" rx="7" ry="22" fill="#fffbe0" opacity=".7"/></g></g>')
MITHU = MITHU.replace('<g id="m-beak">', HAT + '<g id="m-beak">', 1)
assert MITHU.count('id="m-hat"') == 1
BUNNY = open(f"{HERE}/bunny_v2.svg.txt").read()

def lg(id_, stops, x2=0, y2=1):
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="{x2}" y2="{y2}">' + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops) + '</linearGradient>'
defs = ns["defs"] + F3D + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    rg("gBun", [(0, "#ffffff"), (.6, "#f1ecff"), (1, "#c7b8ef")], "38%", "30%", "75%"),
    rg("gBunIn", [(0, "#ffd3e2"), (1, "#f59ab9")], "45%", "40%", "70%"),
    rg("gFeather", [(0, "#fff6b0"), (.6, "#ffd84d"), (1, "#f0a800")], "40%", "30%", "80%"),
    rg("gBush", [(0, "#9ee28a"), (.55, "#4fa35b"), (1, "#2f7a3c")], "40%", "30%", "75%"),
    rg("gBush2", [(0, "#8ad47a"), (.6, "#3f9450"), (1, "#276a34")], "40%", "30%", "75%"),
    rg("gCat", [(0, "#ffd6a0"), (.55, "#f6a54c"), (1, "#d27a22")], "38%", "30%", "75%"),
    rg("gCatIn", [(0, "#ffd3e2"), (1, "#f59ab9")], "45%", "40%", "70%"),
    rg("gCow", [(0, "#ffffff"), (.6, "#fff4e0"), (1, "#e6d2b0")], "38%", "30%", "75%"),
    rg("gMuz", [(0, "#ffd9e4"), (1, "#f2a0b8")], "40%", "30%", "75%"),
    rg("gHorn", [(0, "#fffbe6"), (1, "#e8cf8a")], "35%", "30%", "75%"),
    rg("gDuck", [(0, "#fff8c0"), (.55, "#ffd84d"), (1, "#f0b000")], "38%", "30%", "75%"),
    rg("gDBeak", [(0, "#ffc08a"), (.6, "#ff8a3d"), (1, "#e0601a")], "38%", "30%", "75%"),
    rg("gMango", [(0, "#ffe27a"), (.6, "#ffb020"), (1, "#f07a00")], "38%", "30%", "75%"),
    rg("gCanopy", [(0, "#a8e67a"), (.6, "#4fae4a"), (1, "#2f7a34")], "40%", "30%", "75%"),
    lg("gTrunkT", [(0, "#b07a4a"), (1, "#7a4a24")], 1, 0),
    lg("gFence", [(0, "#f6d6a6"), (1, "#d6a66a")]),
])

def eyes(x, y, r=17):
    return "".join(f'<g class="apup"><ellipse cx="{sx*x}" cy="{y}" rx="{r}" ry="{r*1.25:.1f}" fill="#2a1d3a"/><circle cx="{sx*x+r*.35:.1f}" cy="{y-r*.45:.1f}" r="{r*.38:.1f}" fill="#fff"/><circle cx="{sx*x-r*.3:.1f}" cy="{y+r*.35:.1f}" r="{r*.16:.1f}" fill="#fff"/></g>' for sx in (-1, 1))
def blush(x, y): return f'<ellipse cx="{-x}" cy="{y}" rx="20" ry="12" fill="#ff9eb1" opacity=".75"/><ellipse cx="{x}" cy="{y}" rx="20" ry="12" fill="#ff9eb1" opacity=".75"/>'
# NEW animals (head centred at 0,0; ~r110), glossy, no outlines, front-facing
CAT = ('<g id="cat">'
       '<path d="M-96,-40 L-84,-150 L-20,-92Z" fill="url(#gCat)"/><path d="M-82,-58 L-76,-124 L-40,-90Z" fill="url(#gCatIn)"/>'
       '<path d="M96,-40 L84,-150 L20,-92Z" fill="url(#gCat)"/><path d="M82,-58 L76,-124 L40,-90Z" fill="url(#gCatIn)"/>'
       '<ellipse cx="0" cy="0" rx="118" ry="104" fill="url(#gCat)"/>'
       '<path d="M-30,-98 q10,22 0,40 M0,-104 q8,24 0,44 M30,-98 q-10,22 0,40" stroke="#d27a22" stroke-width="9" fill="none" stroke-linecap="round" opacity=".7"/>'
       '<ellipse cx="0" cy="40" rx="62" ry="44" fill="#fff3e4"/>' + eyes(44, -8, 18) + blush(70, 30) +
       '<path d="M-12,20 L12,20 L0,34Z" fill="#ff7a9a"/><path d="M0,34 q-10,16 -22,6 M0,34 q10,16 22,6" stroke="#7a2140" stroke-width="5" fill="none" stroke-linecap="round"/>'
       '<g id="whisk" stroke="#5a3a20" stroke-width="4" stroke-linecap="round"><path d="M-46,30 L-150,14 M-46,40 L-152,44 M-46,50 L-144,72"/><path d="M46,30 L150,14 M46,40 L152,44 M46,50 L144,72"/></g>'
       '<ellipse cx="-50" cy="-62" rx="30" ry="12" fill="#fff" opacity=".35"/>'
       '<g id="catpaws"><ellipse cx="-60" cy="112" rx="34" ry="24" fill="url(#gCat)"/><ellipse cx="60" cy="112" rx="34" ry="24" fill="url(#gCat)"/></g></g>')
COW = ('<g id="cow">'
       '<path d="M-60,-84 C-96,-110 -110,-150 -92,-172 C-80,-140 -60,-122 -30,-100Z" fill="url(#gHorn)"/>'
       '<path d="M60,-84 C96,-110 110,-150 92,-172 C80,-140 60,-122 30,-100Z" fill="url(#gHorn)"/>'
       '<ellipse cx="-128" cy="-44" rx="52" ry="24" fill="url(#gCow)" transform="rotate(-20 -128 -44)"/><ellipse cx="-130" cy="-44" rx="30" ry="12" fill="#f5b0c4" transform="rotate(-20 -130 -44)"/>'
       '<ellipse cx="128" cy="-44" rx="52" ry="24" fill="url(#gCow)" transform="rotate(20 128 -44)"/><ellipse cx="130" cy="-44" rx="30" ry="12" fill="#f5b0c4" transform="rotate(20 130 -44)"/>'
       '<ellipse cx="0" cy="0" rx="104" ry="112" fill="url(#gCow)"/>'
       '<path d="M30,-96 C70,-100 92,-60 76,-30 C56,-20 34,-44 30,-96Z" fill="#6b4f3f"/><ellipse cx="-62" cy="-30" rx="22" ry="16" fill="#6b4f3f"/>'
       + eyes(40, -28, 17) + blush(72, 14) +
       '<ellipse cx="0" cy="56" rx="82" ry="52" fill="url(#gMuz)"/><ellipse cx="-30" cy="52" rx="11" ry="15" fill="#b05470"/><ellipse cx="30" cy="52" rx="11" ry="15" fill="#b05470"/>'
       '<path d="M-24,84 q24,14 48,0" stroke="#7a2140" stroke-width="5" fill="none" stroke-linecap="round"/>'
       '<ellipse cx="-44" cy="-70" rx="26" ry="10" fill="#fff" opacity=".6"/></g>')
DUCK = ('<g id="duck">'
        '<path d="M-6,-92 q-14,-40 6,-56 q4,26 10,52Z" fill="url(#gDuck)"/><path d="M8,-94 q10,-36 30,-40 q-12,22 -14,44Z" fill="url(#gDuck)"/>'
        '<ellipse cx="0" cy="0" rx="100" ry="96" fill="url(#gDuck)"/>' + eyes(38, -20, 16) + blush(66, 26) +
        '<ellipse cx="0" cy="34" rx="58" ry="22" fill="url(#gDBeak)"/><ellipse cx="0" cy="48" rx="46" ry="14" fill="#e0601a"/>'
        '<ellipse cx="-18" cy="26" rx="18" ry="6" fill="#fff" opacity=".45"/><ellipse cx="-40" cy="-56" rx="24" ry="10" fill="#fff" opacity=".5"/>'
        '<g id="duckwings"><ellipse cx="-104" cy="70" rx="22" ry="40" fill="url(#gDuck)" transform="rotate(30 -104 70)"/><ellipse cx="104" cy="70" rx="22" ry="40" fill="url(#gDuck)" transform="rotate(-30 104 70)"/></g></g>')

# ---- layout
GX, GY, GS = 410, 1830, .74          # Golu left-centre
BX, BY = 810, 1560                   # bush centre (animals rise above its top ≈1365)
AH = 1830                            # animal hidden y (behind bush)
PEEK = {"cat": 1305, "cow": 1440, "duck": 1292}
UP = 1268                            # revealed head y
BUN = (112, 1826); BS = .5; BUN_OFF = (-160, 1826)
MI = (236, 1196); MS = .55           # Mithu on the mango-tree branch

WORDS = [  # id, hindi, english, hi colour, en colour
    ("wMeow", "म्याऊँ!", "Meow!", "#e65100", "#1565c0"),
    ("wGuess", "बताओ कौन?", "Guess who?", "#6a1fc2", "#1565c0"),
    ("wCat", "बिल्ली", "Cat", "#e65100", "#1565c0"),
    ("wMoo", "मूँ!", "Moo!", "#6b4f3f", "#1565c0"),
    ("wCow", "गाय", "Cow", "#8a4b2a", "#1565c0"),
    ("wQuack", "क्वैक!", "Quack!", "#e0a000", "#1565c0"),
    ("wDuck", "बत्तख", "Duck", "#d88a00", "#1565c0"),
    ("wWell", "शाबाश, बनी!", "Well done, Bunny!", "#d81b60", "#2e7d32"),
    ("wBye", "कल फिर मिलेंगे!", "See you tomorrow!", "#d81b60", "#1565c0"),
]
RECAP = [("rc1", "बिल्ली", "Cat", "#e65100"), ("rc2", "गाय", "Cow", "#8a4b2a"), ("rc3", "बत्तख", "Duck", "#d88a00")]

def overlays():
    w = ""
    for i, hi, en, hc, ec in WORDS:
        w += f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div><div class="en" style="color:{ec}">{en}</div></div>'
    w += '<div class="moral" id="wRecap">' + "".join(f'<div class="mw" id="{i}"><div class="hi" style="color:{c}">{hi}</div><div class="en" style="color:#1565c0">{en}</div></div>' for i, hi, en, c in RECAP) + '</div>'
    w += '<div class="xmark" id="xm">✗</div>'
    return w + '<div class="badge">गोलू की पहेली #2 · Golu\'s Riddles</div>'

J = []
def tl(s): J.append(s)
def word_in(i, t, punch=True):
    tl(f'tl.fromTo("#{i}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.32,ease:"back.out(2.6)",immediateRender:false}},{f(t)});')
    if punch: tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.045,duration:.14,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def word_out(i, t): tl(f'tl.to("#{i}",{{opacity:0,scale:.6,duration:.18,ease:"power2.in"}},{f(t)});')
def card(i, t0, t1, punch=True): word_in(i, t0, punch); word_out(i, t1 - .18)
def happy(t0, t1):
    tl(f'tl.set("#g-eyes",{{opacity:0}},{f(t0)}); tl.set("#g-happy",{{opacity:1}},{f(t0)}); tl.set("#g-eyes",{{opacity:1}},{f(t1)}); tl.set("#g-happy",{{opacity:0}},{f(t1)});')
def look(x, t, y=0): tl(f'tl.to("#gwrap .pup",{{x:{x},y:{y},duration:.2,ease:"power2.out"}},{f(t)});')
def trunk(rot, t, d=.25, ease="back.out(2)"): tl(f'tl.to("#g-trunk",{{rotation:{rot},svgOrigin:"0 -352",duration:{d},ease:"{ease}"}},{f(t)});')
def g_hop(t, h=60): tl(f'tl.fromTo("#rgolu",{{y:0}},{{y:{-h},duration:.22,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def golu_arm(side, rot, t, hold, d=.22):
    o = "-138 -170" if side == "L" else "138 -170"
    tl(f'tl.to("#g-arm{side}",{{rotation:{rot},svgOrigin:"{o}",duration:{d},ease:"back.out(2)"}},{f(t)}); tl.to("#g-arm{side}",{{rotation:0,svgOrigin:"{o}",duration:.3,ease:"power2.inOut"}},{f(t+hold)});')
def mithu_talk(t, dur):
    n = max(1, int(round(dur / 0.5)))
    tl(f'tl.to("#m-head",{{rotation:-10,svgOrigin:"18 -140",duration:.25,yoyo:true,repeat:{2*n-1},ease:"sine.inOut"}},{f(t)});')
    tl(f'tl.to("#m-jaw",{{y:8,duration:.125,yoyo:true,repeat:{4*n-1}}},{f(t)});')
    tl(f'tl.to("#m-all",{{y:-24,duration:.25,yoyo:true,repeat:{2*n-1},ease:"power2.out"}},{f(t)});')
def m_wing(t, n=3): tl(f'tl.to("#m-wing",{{rotation:-30,svgOrigin:"-10 -130",duration:.12,yoyo:true,repeat:{2*n-1}}},{f(t)});')
def b_hop(t, h=46, d=.18): tl(f'tl.fromTo("#rbunny",{{y:0}},{{y:{-h},duration:{d},yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def bush_shake(t, n=6, a=4):
    tl(f'tl.fromTo("#bush",{{rotation:0}},{{rotation:{a},svgOrigin:"{BX} {BY+200}",duration:.06,yoyo:true,repeat:{n-1},ease:"sine.inOut",immediateRender:false}},{f(t)});')
    tl(f'tl.set("#bush",{{rotation:0,svgOrigin:"{BX} {BY+200}"}},{f(t + n*.06 + .01)});')
    tl(f'tl.fromTo("#leaves",{{opacity:1,y:0}},{{opacity:0,y:-90,duration:.6,ease:"power2.out",immediateRender:false}},{f(t)});')
def a_move(k, t, y0, y1, d=.3, ease="back.out(1.8)"):
    tl(f'tl.fromTo("#a{k}",{{y:{y0 - AH}}},{{y:{y1 - AH},duration:{d},ease:"{ease}",immediateRender:false}},{f(t)});')
def a_wiggle(k, t, n=4):
    tl(f'tl.fromTo("#a{k} > g",{{rotation:0}},{{rotation:6,svgOrigin:"0 60",duration:.12,yoyo:true,repeat:{n-1},ease:"sine.inOut",immediateRender:false}},{f(t)});')

def build():
    tl('tl.set(".word",{opacity:0,scale:.3},0); tl.set(".mw",{opacity:0,scale:.3},0); tl.set("#wRecap",{opacity:1},0); tl.set("#xm",{opacity:0},0);')
    tl('tl.set("#g-trunk",{svgOrigin:"0 -352"},0); tl.set("#g-ear",{svgOrigin:"-90 -380"},0); tl.set("#g-ear2",{svgOrigin:"90 -380"},0);')
    nb = int(DUR / BEAT)
    # idle life (finite repeats so the timeline stays seekable)
    tl(f'tl.to("#g-body",{{scaleY:.96,scaleX:1.02,svgOrigin:"0 0",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-head",{{y:8,rotation:2,svgOrigin:"0 -240",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0.1);')
    tl(f'tl.to("#g-ear",{{rotation:-7,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0.16);')
    tl(f'tl.to("#g-ear2",{{rotation:6,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0.3);')
    tl(f'tl.to(".flw",{{rotation:8,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut",stagger:.1}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    for i, d in enumerate([90, -70, 60]): tl(f'tl.fromTo("#cl{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    tl(f'tl.to("#mbob",{{y:-10,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0.2);')
    tl(f'tl.to(".mango",{{rotation:5,svgOrigin:"0 -20",duration:{BEAT*2},yoyo:true,repeat:{nb//2-1},ease:"sine.inOut"}},0);')
    # Golu's resting look = at the bush (frame 1 == last frame for the loop)
    tl('tl.set("#gwrap .pup",{x:9,y:-2},0);')
    # ---------- HOOK: bush shakes, meow
    bush_shake(0.0, 8, 5)
    card("wMeow", 0.08, T["q1"] - 0.05, punch=False)
    a_move("cat", 0.0, AH, AH, .01)
    tl(f'tl.fromTo("#punch",{{scale:1.06}},{{scale:1,duration:.6,ease:"power2.out",immediateRender:false}},0);')
    look(-2, T["q1"] - .1, 2); trunk(-18, T["q1"])
    card("wGuess", T["q1"], T["b1"] + .4)
    trunk(0, T["q1"] + .9)
    # Bunny zooms in TOO FAST from the left (running gag) and guesses "शेर!"
    tl(f'tl.fromTo("#pbunny",{{attr:{{transform:"translate({BUN_OFF[0]},{BUN_OFF[1]}) scale({BS})"}}}},{{attr:{{transform:"translate({BUN[0]+40},{BUN[1]}) scale({BS})"}},duration:.18,ease:"power3.out",immediateRender:false}},{f(T["bun_in"])});')
    tl(f'tl.to("#pbunny",{{attr:{{transform:"translate({BUN[0]},{BUN[1]}) scale({BS})"}},duration:.25,ease:"back.out(3)"}},{f(T["bun_in"]+.18)});')
    tl(f'tl.fromTo("#speedb",{{opacity:.9}},{{opacity:0,duration:.35,immediateRender:false}},{f(T["bun_in"])});')
    b_hop(T["b1"], 50)
    look(-10, T["b1"], 3)
    # wrong → red ✗ + boing, bunny sad for a beat
    tl(f'tl.fromTo("#xm",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.22,ease:"back.out(3)",immediateRender:false}},{f(T["x1"])}); tl.to("#xm",{{opacity:0,duration:.2}},{f(T["x1"]+.9)});')
    tl(f'tl.set("#b-smile",{{opacity:0}},{f(T["x1"])}); tl.set("#b-sad",{{opacity:1}},{f(T["x1"])}); tl.set("#b-sad",{{opacity:0}},{f(T["x1"]+1.0)}); tl.set("#b-smile",{{opacity:1}},{f(T["x1"]+1.0)});')
    # ---------- RIDDLE 1: cat
    look(9, T["c1"], -2); trunk(24, T["c1"]); trunk(0, END("c1") + .3)
    a_move("cat", T["peek1"], AH, PEEK["cat"]); a_wiggle("cat", T["peek1"] + .35, 4)
    tl(f'tl.fromTo("#whisk",{{scaleY:1}},{{scaleY:1.25,svgOrigin:"0 40",duration:.15,yoyo:true,repeat:5,immediateRender:false}},{f(T["peek1"]+.4)});')
    tl(f'tl.fromTo("#think",{{opacity:0,scale:.4}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)",immediateRender:false}},{f(END("c1")+.1)}); tl.to("#think",{{opacity:0,duration:.2}},{f(T["r1"]-.15)});')
    a_move("cat", T["r1"] - .05, PEEK["cat"], UP, .35)
    card("wCat", T["r1"], T["hide1"])
    happy(T["r1"], T["r1"] + 1.1); g_hop(T["r1"], 50); golu_arm("R", -70, T["r1"], .9)
    mithu_talk(CUE["m1"], D["m1"]); m_wing(CUE["m1"])
    tl(f'tl.to("#wCat .en",{{scale:1.18,duration:.15,yoyo:true,repeat:1}},{f(CUE["m1"])});')
    a_move("cat", T["hide1"], UP, AH, .35, "power2.in")
    # ---------- RIDDLE 2: cow
    bush_shake(T["s2"] - .1, 8, 5); look(9, T["s2"] - .1, -2)
    card("wMoo", T["s2"], T["b2"])
    b_hop(T["b2"], 50)
    tl(f'tl.fromTo("#xm",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.22,ease:"back.out(3)",immediateRender:false}},{f(T["x2"])}); tl.to("#xm",{{opacity:0,duration:.2}},{f(T["x2"]+.9)});')
    tl(f'tl.set("#b-smile",{{opacity:0}},{f(T["x2"])}); tl.set("#b-sad",{{opacity:1}},{f(T["x2"])}); tl.set("#b-sad",{{opacity:0}},{f(T["x2"]+.9)}); tl.set("#b-smile",{{opacity:1}},{f(T["x2"]+.9)});')
    # "हाथी तो मैं हूँ!" — Golu laughs, points at himself
    happy(T["c2"], END("c2")); trunk(-30, T["c2"]); trunk(0, END("c2")); look(0, T["c2"], 4)
    tl(f'tl.fromTo("#rgolu",{{rotation:0}},{{rotation:3,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:5,immediateRender:false}},{f(T["c2"])});')
    look(9, T["c3"], -3); trunk(24, T["c3"]); trunk(0, END("c3") + .3)
    a_move("cow", T["peek2"], AH, PEEK["cow"]); a_wiggle("cow", T["peek2"] + .35, 4)
    tl(f'tl.fromTo("#think",{{opacity:0,scale:.4}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)",immediateRender:false}},{f(END("c3")+.1)}); tl.to("#think",{{opacity:0,duration:.2}},{f(T["r2"]-.15)});')
    a_move("cow", T["r2"] - .05, PEEK["cow"], UP + 10, .35)
    card("wCow", T["r2"], T["hide2"])
    happy(T["r2"], T["r2"] + 1.1); g_hop(T["r2"], 50); golu_arm("R", -70, T["r2"], .9)
    mithu_talk(CUE["m2"], D["m2"]); m_wing(CUE["m2"])
    tl(f'tl.to("#wCow .en",{{scale:1.18,duration:.15,yoyo:true,repeat:1}},{f(CUE["m2"])});')
    a_move("cow", T["hide2"], UP + 10, AH, .35, "power2.in")
    # ---------- RIDDLE 3: duck — Bunny remembers to wait (Ep6 callback) and gets it RIGHT
    bush_shake(T["s3"] - .1, 8, 5); look(9, T["s3"] - .1, -2)
    card("wQuack", T["s3"], T["b3a"] + .2)
    # Bunny starts to zoom, stops herself, raises a paw: "मेरी बारी?"
    tl(f'tl.to("#pbunny",{{attr:{{transform:"translate({BUN[0]+30},{BUN[1]}) scale({BS})"}},duration:.12,ease:"power2.out"}},{f(T["b3a"]-.25)}); tl.to("#pbunny",{{attr:{{transform:"translate({BUN[0]},{BUN[1]}) scale({BS})"}},duration:.25,ease:"back.out(2)"}},{f(T["b3a"]-.1)});')
    tl(f'tl.to("#b-armR",{{rotation:-120,svgOrigin:"60 -146",duration:.22,ease:"back.out(2)"}},{f(T["b3a"])}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -146",duration:.3}},{f(T["b3b"]+.6)});')
    tl(f'tl.to("#rbunny",{{rotation:-8,svgOrigin:"0 -100",duration:.25,yoyo:true,repeat:1}},{f(T["b3a"])});')
    look(-10, T["b3a"], 3); look(9, T["c4"], -2); trunk(-14, T["c4"]); trunk(0, END("c4") + .3)
    a_move("duck", T["peek3"], AH, PEEK["duck"]); a_wiggle("duck", T["peek3"] + .35, 4)
    tl(f'tl.fromTo("#think",{{opacity:0,scale:.4}},{{opacity:1,scale:1,duration:.25,ease:"back.out(2)",immediateRender:false}},{f(END("c4")+.1)}); tl.to("#think",{{opacity:0,duration:.2}},{f(T["b3b"]-.15)});')
    a_move("duck", T["b3b"] - .05, PEEK["duck"], UP, .35)
    b_hop(T["b3b"], 70); b_hop(T["b3b"] + .45, 50)
    tl(f'tl.set("#b-eyes",{{opacity:0}},{f(T["b3b"])}); tl.set("#b-happy",{{opacity:1}},{f(T["b3b"])}); tl.set("#b-eyes",{{opacity:1}},{f(END("r3"))}); tl.set("#b-happy",{{opacity:0}},{f(END("r3"))});')
    tl(f'tl.fromTo("#b-stars",{{opacity:0,scale:.3}},{{opacity:1,scale:1,svgOrigin:"0 -200",duration:.3,ease:"back.out(2)",immediateRender:false}},{f(T["b3b"])}); tl.to("#b-stars",{{opacity:0,duration:.3}},{f(END("r3"))});')
    card("wDuck", T["b3b"], T["r3"] + .9)
    card("wWell", T["r3"] + .9, T["hide3"], punch=False)
    happy(T["r3"], END("r3")); g_hop(T["r3"], 50); golu_arm("L", 70, T["r3"], 1.0); look(-10, T["r3"] + .6, 3)
    # Mithu's 6th hat: a duck feather floats onto his head
    tl(f'tl.fromTo("#flyfeather",{{opacity:1,x:0,y:0,rotation:0}},{{x:{MI[0]-BX+10},y:{MI[1]-140-UP+20},rotation:-200,duration:.5,ease:"power1.inOut",immediateRender:false}},{f(T["feather"])}); tl.set("#flyfeather",{{opacity:0}},{f(T["feather"]+.5)});')
    tl(f'tl.set("#m-hat",{{opacity:1}},{f(T["feather"]+.5)});')
    mithu_talk(CUE["m3"], D["m3"]); m_wing(CUE["m3"])
    a_move("duck", T["hide3"], UP, AH, .35, "power2.in")
    # ---------- RECAP: cat, cow, duck pop up one by one with the 3 pills
    for j, (k, rc) in enumerate((("cat", "rc1"), ("cow", "rc2"), ("duck", "rc3"))):
        t = T["k2"] + D["k2"] * (.1 + .3 * j) - .05
        a_move(k, t, AH, UP, .28)
        if j < 2: a_move(k, t + D["k2"] * .3, UP, AH, .2, "power2.in")
        tl(f'tl.fromTo("#{rc}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.28,ease:"back.out(2.6)",immediateRender:false}},{f(t)});')
    happy(T["k2"], END("k2") + .2); g_hop(T["k2"] + .1, 40)
    tl(f'tl.to(".mw",{{opacity:0,scale:.6,duration:.2}},{f(T["g2"]-.1)});')
    a_move("duck", T["g2"] - .1, UP, AH, .3, "power2.in")
    # ---------- BYE + loop back to the shaking bush
    card("wBye", T["g2"], DUR - .45, punch=False)
    tl(f'tl.to("#g-trunk",{{rotation:-26,svgOrigin:"0 -352",duration:.2,yoyo:true,repeat:5,ease:"sine.inOut"}},{f(T["g2"])});')
    look(0, T["g2"], 4)
    tl(f'tl.set("#m-hat",{{opacity:0}},{f(DUR-.3)});')
    look(9, DUR - .6, -2)
    tl(f'tl.set("#gwrap .pup",{{x:9,y:-2}},{f(DUR-.35)}); tl.set("#g-trunk",{{rotation:0}},{f(DUR-.35)});')
    bush_shake(DUR - .5, 8, 5)
    tl(f'tl.to("#pbunny",{{attr:{{transform:"translate({BUN_OFF[0]},{BUN_OFF[1]}) scale({BS})"}},duration:.2,ease:"power3.in"}},{f(DUR-.75)});')
    tl(f'tl.fromTo("#speedb",{{opacity:.9}},{{opacity:0,duration:.3,immediateRender:false}},{f(DUR-.7)});')
    tl(f'tl.to("#punch",{{scale:1.06,duration:.45,ease:"power2.in"}},{f(DUR-.5)});')
    # everyone together on the chorus lines (Golu, Bunny, Mithu all "say" them)
    for lid in ("a1", "a2", "a3", "k2"):
        mithu_talk(CUE[lid], D[lid]); b_hop(CUE[lid], 30, .2)
    # blinks
    t = 1.7
    while t < DUR - 1:
        tl(f'tl.to("#gwrap .pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{f(t)});')
        tl(f'tl.to(".apup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{f(t+.9)});')
        t += 3.1
    # lip-sync (pre-drawn mouths toggled by opacity, scale only with svgOrigin)
    def lipsync(levels, mouth, rest, origin, scales):
        Lv = list(levels)
        for i in range(1, len(Lv) - 1):
            if Lv[i] and not Lv[i-1] and not Lv[i+1]: Lv[i] = 0
        prev = 0
        for i, v in enumerate(Lv):
            t = round(i / lips["fps"], 3)
            if v == prev: continue
            if v == 0: tl(f'tl.set("{mouth}",{{opacity:0}},{t});tl.set("{rest}",{{opacity:1}},{t});')
            else: tl(f'tl.set("{mouth}",{{opacity:1,scaleY:{scales[v]},svgOrigin:"{origin}"}},{t});tl.set("{rest}",{{opacity:0}},{t});')
            prev = v
    g = [max(a, b) for a, b in zip(lips["golu"], lips["kids"])]
    bl = [max(a, b) for a, b in zip(lips["bunny"], lips["kids"])]
    lipsync(g, "#g-mouth", "#g-smile", "-62 -314", [0, .5, .8, 1.1])
    lipsync(bl, "#b-mouth", "#b-smile", "0 -204", [0, .55, .8, 1.05])

def bush():
    clumps = [(-150, 40, 110), (150, 40, 110), (-80, -60, 120), (80, -60, 120), (0, -110, 110), (0, 40, 150), (-190, 120, 80), (190, 120, 80)]
    s = "".join(f'<circle cx="{BX+x}" cy="{BY+y}" r="{r}" fill="url(#{"gBush" if i % 2 else "gBush2"})"/>' for i, (x, y, r) in enumerate(clumps))
    s += "".join(f'<ellipse cx="{BX+x}" cy="{BY+y}" rx="26" ry="10" fill="#d8ffc0" opacity=".45" transform="rotate(-20 {BX+x} {BY+y})"/>' for x, y in [(-110, -110), (40, -170), (120, -90), (-180, 0)])
    s += "".join(f'<circle cx="{BX+x}" cy="{BY+y}" r="12" fill="#ff7fb0"/><circle cx="{BX+x}" cy="{BY+y}" r="5" fill="#ffd24a"/>' for x, y in [(-60, -40), (110, 10), (-150, 90), (30, 80), (170, -20)])
    leaves = "".join(f'<ellipse cx="{BX+x}" cy="{BY-170+y}" rx="16" ry="8" fill="#6fcf5a" transform="rotate({r} {BX+x} {BY-170+y})"/>' for x, y, r in [(-120, 0, 30), (-40, -30, -20), (60, -20, 40), (140, 10, -30)])
    return f'<g id="bush" filter="url(#f3d)">{s}</g><g id="leaves" opacity="0">{leaves}</g>'

def tree():
    mangos = "".join(f'<g transform="translate({x},{y})"><g class="mango"><ellipse cx="0" cy="0" rx="20" ry="26" fill="url(#gMango)"/><path d="M0,-24 q6,-10 14,-8" stroke="#2f7a34" stroke-width="4" fill="none"/></g></g>' for x, y in [(80, 960), (300, 900), (180, 1060), (360, 1040)])
    return ('<g id="tree">'
            '<path d="M180,1640 C190,1400 170,1250 200,1120 L270,1120 C290,1260 280,1420 300,1640Z" fill="url(#gTrunkT)"/>'
            '<path d="M240,1200 C300,1170 330,1180 360,1190" stroke="#8a5a30" stroke-width="22" fill="none" stroke-linecap="round"/>'
            '<g filter="url(#f3d)"><circle cx="110" cy="960" r="150" fill="url(#gCanopy)"/><circle cx="300" cy="900" r="160" fill="url(#gCanopy)"/>'
            '<circle cx="220" cy="1040" r="150" fill="url(#gCanopy)"/><circle cx="400" cy="1010" r="110" fill="url(#gCanopy)"/><circle cx="30" cy="1060" r="110" fill="url(#gCanopy)"/></g>'
            + mangos + '</g>')

def fence():
    posts = "".join(f'<rect x="{x}" y="1560" width="34" height="140" rx="10" fill="url(#gFence)"/><circle cx="{x+17}" cy="1562" r="17" fill="#f6d6a6"/>' for x in range(-10, 1100, 110))
    return f'<g id="fence" opacity=".95"><rect x="0" y="1590" width="1080" height="20" rx="8" fill="#e8c08a"/><rect x="0" y="1648" width="1080" height="20" rx="8" fill="#e8c08a"/>{posts}</g>'

def html():
    build()
    flowers = "".join(flower(x, y, c, i) for i, (x, y, c) in enumerate([(60, 1880, "#ff6b9a"), (300, 1900, "#ffc51c"), (640, 1890, "#a66bff"), (1010, 1880, "#ff6b6b"), (560, 1790, "#ffc51c"), (960, 1770, "#ff9a3c"), (160, 2000, "#a66bff"), (420, 2040, "#ff6b9a"), (760, 2010, "#ffc51c"), (980, 2050, "#ff6b6b")]))
    sunrays = "".join(f'<path d="M0,-118 L14,-150 L-14,-150Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    animals = "".join(f'<g transform="translate({BX},{AH})"><g id="a{k}"><g filter="url(#f3d)">{art}</g></g></g>' for k, art in (("cat", CAT), ("cow", COW), ("duck", DUCK)))
    flyf = (f'<g transform="translate({BX},{UP-60})"><g id="flyfeather" opacity="0"><path d="M0,0 C-30,-40 -26,-104 6,-132 C34,-100 34,-40 0,0Z" fill="url(#gFeather)" transform="scale(.5)"/></g></g>')
    mithu = f'<g filter="url(#f3d)"><g transform="translate({MI[0]},{MI[1]}) scale({MS})"><g id="mbob">{MITHU}</g></g></g>'
    speedb = '<g id="speedb" opacity="0">' + "".join(f'<path d="M{-10+i*14},{1700+i*36} l-120,0" stroke="#ffffff" stroke-width="10" stroke-linecap="round"/>' for i in range(4)) + '</g>'
    think = (f'<g transform="translate({GX+150},{GY-640})"><g id="think" opacity="0"><circle cx="-60" cy="70" r="12" fill="#fff"/><circle cx="-34" cy="40" r="18" fill="#fff"/>'
             f'<ellipse cx="20" cy="-20" rx="70" ry="54" fill="#fff"/><text x="20" y="4" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="76" fill="#6a1fc2">?</text></g></g>')
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}<clipPath id="clipAn"><rect x="0" y="0" width="1080" height="1712"/></clipPath></defs>
<rect width="1080" height="1920" fill="url(#gSky)"/>
<g opacity=".3">{"".join(f'<path d="M-60,1500 A600,600 0 0 1 1140,1500" stroke="{c}" stroke-width="30" fill="none" transform="translate(0,{i*30}) scale(1,{1-i*0.02})"/>' for i, c in enumerate(["#ff3b4e","#ff9a3c","#ffc51c","#2fcf5a","#2f8cff","#a66bff"]))}</g>
<g transform="translate(880,230)"><g id="sunface">{sunrays}</g><circle r="105" fill="url(#gSun)"/>
  <ellipse cx="-30" cy="-12" rx="9" ry="13" fill="#7a4a00"/><ellipse cx="30" cy="-12" rx="9" ry="13" fill="#7a4a00"/>
  <path d="M-34,22 q34,30 68,0" stroke="#7a4a00" stroke-width="7" fill="none" stroke-linecap="round"/></g>
{cloud("cl0", 150, 640, 1.0)}{cloud("cl1", 700, 700, .8)}{cloud("cl2", 480, 200, .6)}
<g transform="translate(0,-170)">
<g filter="url(#fblurH)"><ellipse cx="200" cy="1600" rx="720" ry="300" fill="url(#gHillA)"/><ellipse cx="960" cy="1620" rx="680" ry="320" fill="url(#gHillB)"/></g>
{tree()}
{fence()}
<rect x="0" y="1720" width="1080" height="400" fill="#4fbf3a"/>
<ellipse cx="{BX}" cy="1782" rx="260" ry="26" fill="#2f7a34" opacity=".35"/>
<g clip-path="url(#clipAn)">{animals}</g>
{bush()}
{flyf}
{flowers}
{mithu}
<g id="pgolu" transform="translate({GX},{GY}) scale({GS})"><g id="rgolu"><g id="gwrap" filter="url(#f3d)">{GOLU}</g></g></g>
{speedb}
<g id="pbunny" transform="translate({BUN_OFF[0]},{BUN_OFF[1]}) scale({BS})"><g id="rbunny"><g filter="url(#f3d)">{BUNNY}</g></g></g>
{think}
</g>
</svg>'''
    svg = svg.replace("<defs>", '<defs><filter id="fblurH" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="3"/></filter>', 1)
    css = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#8fdcff}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0}
#punch{position:absolute;inset:0;transform-origin:60% 70%}
#world{position:absolute;inset:0}
#ovl{position:absolute;inset:0}
.word{position:absolute;left:60px;width:860px;top:400px;text-align:center;line-height:1.08;white-space:nowrap}
.word .hi{font-size:132px;font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(20,20,60,.22)}
.word .en{font-size:86px;font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(20,20,60,.22)}
.moral{position:absolute;left:40px;width:880px;top:430px;display:flex;justify-content:center;gap:18px}
.mw{background:rgba(255,255,255,.94);border-radius:34px;padding:8px 22px;text-align:center;line-height:1.05;white-space:nowrap;box-shadow:0 8px 0 rgba(20,20,60,.2)}
.mw .hi{font-size:80px;font-weight:800}
.mw .en{font-size:52px;font-weight:800}
.word,.mw,.xmark{opacity:0}
.xmark{position:absolute;left:60px;top:1330px;font-size:150px;font-weight:800;color:#ff3b4e;-webkit-text-stroke:10px #fff;paint-order:stroke fill;line-height:1}
.badge{position:absolute;top:290px;left:150px;padding:12px 26px;border-radius:40px;background:rgba(255,255,255,.94);color:#6a1fc2;font-size:38px;font-weight:800;box-shadow:0 6px 0 rgba(20,20,60,.2)}
"""
    fit = """
function fitWords(){ document.querySelectorAll('.word > div').forEach(function(el){
  if(!el.dataset.fs) el.dataset.fs = parseFloat(getComputedStyle(el).fontSize);
  var fs = +el.dataset.fs; el.style.fontSize = fs + 'px'; el.style.display='inline-block';
  while (el.offsetWidth > 760 && fs > 40) { fs -= 2; el.style.fontSize = fs + 'px'; }
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
