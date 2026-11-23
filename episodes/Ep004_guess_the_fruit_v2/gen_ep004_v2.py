"""Golu & Dost Ep 4 (v2 remake) — पहेली #1: बताओ कौन सा फल? | Guess the Fruit.
Same script/song/timing structure as the original; soft-3D Golu v2 + Pari & Chintu + glossy Mithu; Fish Audio voices."""
import json, math, sys, os
PROJ = sys.argv[1]; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json")); DUR = T["DUR"]; D = T["D"]; R = T["R"]
LIPS = json.load(open(sys.argv[2]))
sys.path.insert(0, HERE); import base_v2
ns = base_v2.load(); rg = ns["rg"]; GOLU = ns["GOLU"]; KIDS = ns["KIDS"]; cloud = ns["cloud"]
MITHU = open(f"{HERE}/mithu_src.txt").read()
GS = 0.9; GX, GY = 540, 1880
KIDS = KIDS.replace('translate(150,1880) scale(.78)', 'translate(128,1895) scale(.74)').replace('translate(930,1880) scale(.78)', 'translate(952,1895) scale(.74)')
BUMP = (-34, -468)

defs = ns["defs"] + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    rg("gApple", [(0, "#ffb3b3"), (.35, "#ff3b4e"), (1, "#b0102a")], "35%", "30%", "75%"),
    rg("gBan", [(0, "#fff6b0"), (.5, "#ffd21c"), (1, "#e0a100")], "40%", "30%", "80%"),
    rg("gMelon", [(0, "#8fef7a"), (.5, "#2fb34a"), (1, "#136b2a")], "35%", "30%", "75%"),
    rg("gFlesh", [(0, "#ff9aa5"), (.6, "#ff3b5c"), (1, "#e0213f")], "50%", "10%", "90%"),
    rg("gOrange", [(0, "#ffe0a0"), (.45, "#ff9a1c"), (1, "#e06a00")], "35%", "30%", "75%"),
    rg("gBox", [(0, "#e3b8ff"), (.5, "#a35cff"), (1, "#6a1fc2")], "35%", "25%", "85%"),
    rg("gLid", [(0, "#f0d2ff"), (.5, "#b67aff"), (1, "#7a2fd0")], "35%", "25%", "85%"),
    rg("gSpark", [(0, "#ffffff"), (.5, "#fff6a8"), (1, "rgba(255,246,168,0)")], "50%", "50%", "50%"),
    '<linearGradient id="gWood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8a868"/><stop offset="1" stop-color="#b86c34"/></linearGradient>',
    '<linearGradient id="gWoodTop" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd09a"/><stop offset="1" stop-color="#e09a5a"/></linearGradient>',
    '<linearGradient id="gCrate" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffc98a"/><stop offset="1" stop-color="#d98a46"/></linearGradient>',
    '<linearGradient id="gGround" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe2a8"/><stop offset="1" stop-color="#f4bf72"/></linearGradient>',
])

# ---------- props (all original, glossy, no outlines) ----------
def apple(id_):
    return (f'<g id="{id_}"><path d="M0,-80 C55,-125 140,-85 132,5 C126,95 62,140 0,118 C-62,140 -126,95 -132,5 C-140,-85 -55,-125 0,-80Z" fill="url(#gApple)"/>'
            '<path d="M-4,-82 C-6,-110 4,-130 18,-148" stroke="#7a4a1c" stroke-width="13" fill="none" stroke-linecap="round"/>'
            '<path d="M16,-120 C40,-160 92,-150 104,-128 C78,-104 38,-104 16,-120Z" fill="#3fcf4a"/>'
            '<ellipse cx="-62" cy="-36" rx="24" ry="44" fill="#ffffff" opacity=".5" transform="rotate(-25 -62 -36)"/>'
            '<ellipse cx="-78" cy="30" rx="8" ry="12" fill="#ffffff" opacity=".4"/></g>')

def banana(id_):
    return (f'<g id="{id_}"><g transform="rotate(-12)"><path d="M-150,-60 C-120,90 90,120 158,-30 C165,-48 146,-60 134,-44 C76,52 -70,48 -116,-74 C-124,-92 -152,-82 -150,-60Z" fill="url(#gBan)"/>'
            '<path d="M-124,-40 C-90,50 60,80 120,-10" stroke="#fff8c8" stroke-width="10" fill="none" stroke-linecap="round" opacity=".7"/>'
            '<path d="M-150,-60 C-154,-80 -146,-96 -134,-98 L-116,-74 C-124,-92 -142,-84 -150,-60Z" fill="#8a5a1c"/>'
            '<circle cx="152" cy="-40" r="9" fill="#6a4214"/></g></g>')

def melon(id_):
    stripes = "".join(f'<path d="M{x},-100 C{x*1.35:.0f},-40 {x*1.35:.0f},40 {x},100" stroke="#0f5a22" stroke-width="16" fill="none" opacity=".55"/>' for x in (-80, -30, 20, 70))
    seeds = "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="8" fill="#2a1a1a" transform="rotate({x/3:.0f} {x} {y})"/>' for x, y in [(-50, 22), (-20, 40), (14, 42), (46, 24), (-4, 18), (28, 14), (-34, 8)])
    return (f'<g id="{id_}"><g transform="translate(-40,-20)"><ellipse rx="135" ry="108" fill="url(#gMelon)"/>{stripes}'
            '<ellipse cx="-56" cy="-50" rx="40" ry="22" fill="#ffffff" opacity=".35" transform="rotate(-20 -56 -50)"/></g>'
            '<g transform="translate(70,70) rotate(-10)"><path d="M-100,-10 A100,100 0 0 0 100,-10 Z" fill="#1f8a34"/>'
            '<path d="M-88,-10 A88,88 0 0 0 88,-10 Z" fill="#e9ffd8"/><path d="M-78,-10 A78,78 0 0 0 78,-10 Z" fill="url(#gFlesh)"/>'
            f'{seeds}<rect x="-104" y="-16" width="208" height="10" rx="5" fill="#ff7b8c"/></g></g>')

def orange(id_):
    return (f'<g id="{id_}"><circle r="40" fill="url(#gOrange)"/><circle cx="-14" cy="-14" r="10" fill="#fff" opacity=".5"/>'
            '<path d="M0,-38 C10,-56 30,-56 36,-48 C24,-36 10,-36 0,-38Z" fill="#3fcf4a"/></g>')

FRUITS = [("apple", apple), ("banana", banana), ("melon", melon)]

BOX = '''<g id="box"><g id="box-in">
  <ellipse cx="0" cy="150" rx="170" ry="24" fill="rgba(60,30,90,.25)"/>
  <rect x="-150" y="-110" width="300" height="250" rx="34" fill="url(#gBox)"/>
  <rect x="-24" y="-110" width="48" height="250" fill="#ffd21c"/>
  <ellipse cx="-80" cy="-60" rx="40" ry="22" fill="#ffffff" opacity=".3"/>
  <circle cx="0" cy="22" r="82" fill="#ffffff" opacity=".95"/>
  <text id="qm" x="0" y="64" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="130" fill="#a35cff">?</text>
  <text id="n3" x="0" y="64" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="130" fill="#ff3b4e" opacity="0">3</text>
  <text id="n2" x="0" y="64" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="130" fill="#ff9a1c" opacity="0">2</text>
  <text id="n1" x="0" y="64" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="130" fill="#2fcf5a" opacity="0">1</text>
  <g id="lid"><rect x="-168" y="-150" width="336" height="58" rx="22" fill="url(#gLid)"/>
    <rect x="-24" y="-150" width="48" height="58" fill="#ffe45c"/>
    <path d="M0,-150 C-40,-210 -100,-190 -70,-152Z M0,-150 C40,-210 100,-190 70,-152Z" fill="#ffd21c"/>
    <ellipse cx="-100" cy="-134" rx="40" ry="10" fill="#ffffff" opacity=".35"/></g>
</g></g>'''

def crate(x, y, fruit_svg):
    return (f'<g transform="translate({x},{y})">{fruit_svg}'
            '<rect x="-120" y="-20" width="240" height="90" rx="14" fill="url(#gCrate)"/>'
            '<path d="M-110,10 H110 M-110,40 H110" stroke="#b86c34" stroke-width="6" opacity=".6"/></g>')

def pile_apples():
    return "".join(f'<g transform="translate({x},{y}) scale(.3)">{apple("pa%d" % i)}</g>' for i, (x, y) in enumerate([(-70, -20), (0, -24), (70, -20), (-35, -60), (35, -60)]))
def pile_bananas():
    return "".join(f'<g transform="translate({x},{y}) scale(.36) rotate({r})">{banana("pb%d" % i)}</g>' for i, (x, y, r) in enumerate([(-40, -30, -10), (30, -34, 8), (-5, -62, 0)]))
def pile_oranges():
    return "".join(f'<g transform="translate({x},{y}) scale(.95)">{orange("po%d" % i)}</g>' for i, (x, y) in enumerate([(-75, -22), (0, -26), (75, -22), (-38, -66), (38, -66)]))

def awning():
    s = ""
    w = 1080 / 9
    for i in range(9):
        c = "#ff3b4e" if i % 2 == 0 else "#ffffff"
        x = i * w
        s += f'<path d="M{x:.0f},120 H{x+w:.0f} V250 Q{x+w/2:.0f},310 {x:.0f},250Z" fill="{c}"/>'
    s += '<rect x="0" y="100" width="1080" height="34" rx="10" fill="#c3132a"/>'
    return s

# ---------- overlays ----------
WORDS = [  # id, hindi, english, hi colour, en colour
    ("wBonk", "ठक! उफ़!", "Bonk! Oops!", "#e06a00", "#1565c0"),
    ("wIntro", "पहेली का समय!", "Riddle time!", "#6a1fc2", "#c2185b"),
    ("wC0", "मैं लाल हूँ, गोल हूँ!", "Red and round!", "#d81b3a", "#1565c0"),
    ("wC1", "मैं पीला हूँ, लंबा हूँ!", "Yellow and long!", "#b35400", "#1565c0"),
    ("wC2", "बाहर हरा, अंदर लाल!", "Green outside, red inside!", "#0a7d33", "#d81b3a"),
    ("wQ0", "बताओ, मैं कौन?", "Who am I?", "#6a1fc2", "#c2185b"),
    ("wQ1", "बताओ, मैं कौन?", "Who am I?", "#6a1fc2", "#c2185b"),
    ("wQ2", "बताओ, मैं कौन?", "Who am I?", "#6a1fc2", "#c2185b"),
    ("wA0", "सेब!", "Apple!", "#d81b3a", "#1565c0"),
    ("wA1", "केला!", "Banana!", "#c98a00", "#1565c0"),
    ("wA2", "तरबूज़!", "Watermelon!", "#0a7d33", "#d81b3a"),
    ("wG", "चलो फिर से!", "Let's do it again!", "#c2185b", "#1565c0"),
    ("wJ", "कल नई पहेली!", "See you tomorrow!", "#6a1fc2", "#1565c0"),
]

def overlays():
    w = "".join(f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div>'
                f'<div class="en" style="color:{ec}">{en}</div></div>' for i, hi, en, hc, ec in WORDS)
    return w + '<div class="badge">गोलू की पहेली #1 · Golu\'s Riddles</div>'

J = []
def tl(s): J.append(s)
def word_in(i, t):
    tl(f'tl.fromTo("#{i}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.35,ease:"back.out(3)",immediateRender:false}},{t});')
    tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.06,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t});')
def word_out(i, t): tl(f'tl.to("#{i}",{{opacity:0,scale:.5,duration:.25}},{t});')
def pulse(sel, t): tl(f'tl.to("{sel}",{{scale:1.15,duration:.15,yoyo:true,repeat:1}},{t});')
def happy(t0, t1):
    tl(f'tl.set("#g-eyes",{{opacity:0}},{t0}); tl.set("#g-happy",{{opacity:1}},{t0}); tl.set("#g-eyes",{{opacity:1}},{t1}); tl.set("#g-happy",{{opacity:0}},{t1});')
def jump(t, n=1, h=-70):
    tl(f'tl.to("#gjump",{{y:{h},duration:.25,ease:"power2.out",yoyo:true,repeat:{2*n-1}}},{t});')
    tl(f'tl.fromTo("#g-body",{{scaleY:1}},{{scaleY:.9,scaleX:1.06,svgOrigin:"0 0",duration:.08,yoyo:true,repeat:1,immediateRender:false}},{t + .5*n - .02:.2f});')
def kids_cheer(t, hold=1.0):
    for k, d in (("A", 0), ("B", .07)):
        tl(f'tl.to("#k{k}-armL",{{rotation:80,duration:.18,ease:"back.out(2)"}},{t+d:.2f}); tl.to("#k{k}-armR",{{rotation:-80,duration:.18,ease:"back.out(2)"}},{t+d+.05:.2f});')
        tl(f'tl.to("#k{k}-armL",{{rotation:0,duration:.3,ease:"power2.inOut"}},{t+d+hold:.2f}); tl.to("#k{k}-armR",{{rotation:0,duration:.3,ease:"power2.inOut"}},{t+d+hold+.06:.2f});')
def mithu_talk(t, dur):
    n = max(1, int(round(dur / 0.5)))
    tl(f'tl.to("#m-head",{{rotation:-10,svgOrigin:"18 -140",duration:.25,yoyo:true,repeat:{2*n-1},ease:"sine.inOut"}},{t});')
    tl(f'tl.to("#m-jaw",{{y:8,duration:.125,yoyo:true,repeat:{4*n-1}}},{t});')
    tl(f'tl.to("#m-all",{{y:-30,duration:.25,yoyo:true,repeat:{2*n-1},ease:"power2.out"}},{t});')
def wave(t, n=2):
    # arm wave (right arm, shoulder pivot) + a little trunk curl that follows a beat later
    tl(f'tl.to("#g-armR",{{rotation:-80,duration:.25,ease:"back.out(2)"}},{t}); tl.to("#g-armR",{{rotation:-55,duration:.25,yoyo:true,repeat:{2*n-1},ease:"sine.inOut"}},{t+.25}); tl.to("#g-armR",{{rotation:0,duration:.3}},{t+.25+.5*n});')
    tl(f'tl.to("#g-trunk",{{rotation:-14,duration:.2,yoyo:true,repeat:1,ease:"sine.inOut"}},{t+.12:.2f});')

CEN = (540, 930)                    # box / reveal centre
SLOTS = [(890, 830), (890, 950), (890, 1070)]
ROW = [(220, 960), (540, 960), (860, 960)]
OR_HOME = (300, 1305)               # orange resting by Mithu's feet
def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set(".fr",{opacity:0,scale:.2});')
    tl('tl.set("#g-trunk",{svgOrigin:"0 -352"},0); tl.set("#g-ear",{svgOrigin:"-90 -380"},0); tl.set("#g-ear2",{svgOrigin:"90 -380"},0); tl.set("#g-armR",{svgOrigin:"110 -215"},0); tl.set("#g-armL",{svgOrigin:"-110 -215"},0);')
    tl('tl.set("#kA-armL",{svgOrigin:"-62 -230"},0); tl.set("#kA-armR",{svgOrigin:"62 -230"},0); tl.set("#kB-armL",{svgOrigin:"-60 -232"},0); tl.set("#kB-armR",{svgOrigin:"60 -232"},0);')
    nb = int(DUR / BEAT)
    # beat dance — head leads, ears follow with offsets (never in unison)
    tl(f'tl.to("#g-body",{{scaleY:.96,scaleX:1.02,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-head",{{y:10,rotation:1.5,svgOrigin:"0 -240",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-ear",{{rotation:-8,duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0.06);')
    tl(f'tl.to("#g-ear2",{{rotation:6,duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0.12);')
    tl(f'tl.to("#kA",{{y:-12,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.25);')
    tl(f'tl.to("#kB",{{y:-10,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.5);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.3);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.55);')
    tl(f'tl.to("#cam",{{scale:1.025,duration:{BEAT*4},yoyo:true,repeat:{int(DUR/2)-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to(".flw",{{rotation:8,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut",stagger:.1}},0);')
    tl(f'tl.to("#flag",{{skewY:6,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    for i, d in enumerate([110, -90, 70]):
        tl(f'tl.fromTo("#cl{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    # idle box wobble (the mystery box is on screen at frame 1 and at the loop end)
    tl('tl.fromTo("#box-in",{rotation:-3},{rotation:3,svgOrigin:"0 140",duration:.5,yoyo:true,repeat:7,ease:"sine.inOut",immediateRender:false},0);')
    # ---- 0-3 s surprise: Mithu kicks the orange, it bonks Golu's head and lands in the crate
    ox, oy = OR_HOME
    tl(f'gsap.set("#orng",{{x:{ox},y:{oy}}});')
    tl('tl.to("#mithu",{x:30,duration:.1,yoyo:true,repeat:1},0);')
    hx, hy = GX + BUMP[0]*GS, GY + (BUMP[1]-30)*GS
    tl(f'tl.to("#orng",{{x:{hx:.0f},duration:.22,ease:"none"}},0); tl.to("#orng",{{y:{hy:.0f},duration:.22,ease:"power1.out"}},0);')
    tl('tl.to("#orng",{x:900,duration:.7,ease:"none"},.22); tl.to("#orng",{y:1040,duration:.32,ease:"power2.out"},.22); tl.to("#orng",{y:1250,duration:.38,ease:"power2.in"},.54);')
    tl('tl.to("#orng",{rotation:540,duration:.92,ease:"none"},0);')
    tl(f'tl.set("#bump",{{opacity:1}},.22); tl.fromTo("#bump",{{scale:.3}},{{scale:1.2,svgOrigin:"{BUMP[0]} {BUMP[1]}",duration:.25,ease:"back.out(3)",immediateRender:false}},.22); tl.to("#bump",{{opacity:0,duration:.3}},2.4);')
    tl(f'tl.set("#stars",{{opacity:1}},.25); tl.to("#stars",{{rotation:360,svgOrigin:"{BUMP[0]} {BUMP[1]-50}",duration:1,repeat:1,ease:"none"}},.25); tl.set("#stars",{{opacity:0}},2.3);')
    tl('tl.to("#gwrap",{x:-18,duration:.06,yoyo:true,repeat:5},.22);')
    happy(.22, 1.4)
    word_in("wBonk", 0.08)
    mithu_talk(1.5, D["a2"]); pulse("#wBonk .en", 1.5)
    word_out("wBonk", 2.75)
    tl('tl.to("#kA",{rotation:-4,svgOrigin:"0 0",duration:.2,yoyo:true,repeat:3},1.6); tl.to("#kB",{rotation:4,svgOrigin:"0 0",duration:.2,yoyo:true,repeat:3},1.7);')
    kids_cheer(T["b2"], .9)
    # ---- intro
    word_in("wIntro", T["intro"]); pulse("#wIntro .en", T["b2"]); jump(T["b2"], 1); happy(T["b2"], T["b2"] + 1.0); wave(T["intro"], 2)
    word_out("wIntro", R[0]["t0"] - .3)
    tl(f'tl.fromTo("#box-in",{{rotation:-3}},{{rotation:3,svgOrigin:"0 140",duration:.5,yoyo:true,repeat:{int((R[0]["cd"]-4.0)/.5)*1-1},ease:"sine.inOut",immediateRender:false}},4.0);')
    # ---- three riddles
    for k, r in enumerate(R):
        name = FRUITS[k][0]
        word_in(f"wC{k}", r["t0"]); pulse(f"#wC{k} .en", r["en"])
        mithu_talk(r["en"], D[["c2", "e2", "g2"][k]])
        word_out(f"wC{k}", r["q"] - .25)
        word_in(f"wQ{k}", r["q"])
        # countdown 3-2-1 on the box (box shakes harder each beat)
        tl(f'tl.set("#qm",{{opacity:0}},{r["cd"]});')
        for j, n in enumerate(["n3", "n2", "n1"]):
            t = r["cd"] + j * .5
            tl(f'tl.set("#{n}",{{opacity:1}},{t}); tl.fromTo("#{n}",{{scale:1.6}},{{scale:1,svgOrigin:"0 30",duration:.2,ease:"back.out(3)",immediateRender:false}},{t}); tl.set("#{n}",{{opacity:0}},{t+.5});')
            tl(f'tl.fromTo("#box-in",{{rotation:{-4-3*j}}},{{rotation:{4+3*j},svgOrigin:"0 140",duration:.1,yoyo:true,repeat:3,immediateRender:false}},{t});')
        word_out(f"wQ{k}", r["rev"] - .2)
        # reveal: lid flies off, fruit pops up big, box drops away
        rv = r["rev"]
        tl(f'tl.to("#lid",{{y:-260,x:120,rotation:40,svgOrigin:"0 -120",opacity:0,duration:.45,ease:"power2.out"}},{rv});')
        tl(f'tl.to("#box",{{y:260,opacity:0,duration:.4,ease:"power2.in"}},{rv+.1});')
        tl(f'tl.set("#f{k}",{{opacity:1,x:{CEN[0]},y:{CEN[1]+60},scale:.2,rotation:-30}},{rv});')
        tl(f'tl.to("#f{k}",{{y:{CEN[1]-20},scale:1.05,rotation:0,duration:.45,ease:"back.out(2.2)"}},{rv});')
        tl(f'tl.to("#f{k}",{{rotation:6,duration:.25,yoyo:true,repeat:5,ease:"sine.inOut"}},{rv+.5});')
        tl(f'tl.fromTo("#rays",{{opacity:0}},{{opacity:1,duration:.25,immediateRender:false}},{rv}); tl.to("#rays",{{opacity:0,duration:.4}},{rv+1.4});')
        word_in(f"wA{k}", rv + .05); pulse(f"#wA{k} .en", r["en2"])
        happy(rv + .1, r["en2"] + 1.0); jump(r["en2"], 1); wave(rv + .1, 1)
        tl(f'tl.to("#mithu",{{y:-50,duration:.2,yoyo:true,repeat:3,ease:"power2.out"}},{r["en2"]});')
        kids_cheer(r["en2"], 1.0)
        # fruit flies to its little slot, box comes back for the next riddle
        sx, sy = SLOTS[k]
        tl(f'tl.to("#f{k}",{{x:{sx},y:{sy},scale:.3,rotation:0,duration:.5,ease:"power2.inOut"}},{r["end"]-.6});')
        word_out(f"wA{k}", r["end"] - .5)
        if k < 2:
            tl(f'tl.set("#lid",{{y:0,x:0,rotation:0,opacity:1}},{r["end"]-.5}); tl.set("#qm",{{opacity:1}},{r["end"]-.5});')
            tl(f'tl.fromTo("#box",{{y:-500,opacity:1}},{{y:0,duration:.45,ease:"bounce.out",immediateRender:false}},{r["end"]-.5});')
    # ---- recap: fruits fly into a big row and bounce on each name
    rc = T["recap"]
    word_in("wG", rc); pulse("#wG .en", T["i2"]); happy(T["i2"], T["i2"] + 1.0); jump(T["i2"], 1)
    word_out("wG", T["j1"] - .3)
    for k in range(3):
        x, y = ROW[k]
        tl(f'tl.to("#f{k}",{{x:{x},y:{y},scale:.78,duration:.5,ease:"back.out(1.6)"}},{rc + .3 + k*.15:.2f});')
        tl(f'tl.fromTo("#f{k}",{{scale:.78}},{{scale:1.0,duration:.18,yoyo:true,repeat:1,immediateRender:false}},{T["j1"] + k*.55:.2f});')
        tl(f'tl.to("#f{k}",{{y:{y-70},duration:.18,yoyo:true,repeat:1,ease:"power2.out"}},{T["j2"] + k*.62:.2f});')
    tl(f'tl.set("#lbl",{{opacity:1}},{T["j1"]});')
    for k in range(3):
        tl(f'tl.fromTo("#lb{k}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,transformOrigin:"50% 50%",duration:.3,ease:"back.out(3)",immediateRender:false}},{T["j1"] + k*.55:.2f});')
        tl(f'tl.fromTo("#le{k}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,transformOrigin:"50% 50%",duration:.3,ease:"back.out(3)",immediateRender:false}},{T["j2"] + k*.62:.2f});')
    happy(T["j2"], T["j2"] + 1.6); jump(T["j2"], 2); kids_cheer(T["i2"], .9); kids_cheer(T["j1"], 1.2); kids_cheer(T["j2"], 1.4)
    tl(f'tl.to("#lbl",{{opacity:0,duration:.3}},{T["end"]-.4});')
    # ---- see you tomorrow + confetti
    en = T["end"]
    for k in range(3):
        sx, sy = SLOTS[k]
        tl(f'tl.to("#f{k}",{{x:{sx},y:{sy},scale:.3,duration:.5,ease:"power2.inOut"}},{en - .4:.2f});')
    word_in("wJ", en); pulse("#wJ .en", T["k2"])
    mithu_talk(T["k2"], D["k2"]); happy(T["k2"], T["k2"] + 1.2); jump(T["k2"], 2); wave(en, 2)
    tl(f'tl.set(".conf",{{opacity:1}},{en});')
    for k in range(36):
        x = (k * 97) % 1080
        tl(f'tl.fromTo("#cf{k}",{{x:{x},y:-80,rotation:0}},{{y:{1500 + (k*53) % 400},x:{x + ((k*37) % 160) - 80},rotation:{360 + k*20},duration:{2.0 + (k % 5)*.15:.2f},ease:"power1.in",immediateRender:false}},{en + (k % 8)*.05:.2f});')
    tl(f'tl.set(".conf",{{opacity:0}},{en + 2.9:.2f});')
    word_out("wJ", DUR - 0.9)
    # ---- loop back to the first frame: box with "?" returns, fruits leave, orange back by Mithu
    lb = DUR - 0.8
    for k in range(3):
        tl(f'tl.to("#f{k}",{{opacity:0,scale:.1,duration:.3}},{lb + k*.05:.2f});')
    tl(f'tl.set("#lid",{{y:0,x:0,rotation:0,opacity:1}},{lb}); tl.set("#qm",{{opacity:1}},{lb});')
    tl(f'tl.fromTo("#box",{{y:-500,opacity:1}},{{y:0,duration:.45,ease:"bounce.out",immediateRender:false}},{lb});')
    tl(f'tl.fromTo("#orng",{{x:{ox},y:{oy-300},rotation:0}},{{y:{oy},duration:.4,ease:"bounce.out",immediateRender:false}},{lb});')
    for t in [2.6, 8.7, 14.2, 18.4, 25.6, 28.6, 36.2, 42.4, 47.4]:
        if t < DUR: tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
    for t in [1.0, 5.5, 12.4, 20.4, 27.2, 33.6, 40.0]:
        tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
    for t in [3.1, 6.9, 10.2, 14.1, 18.2, 21.9, 26.3, 30.0, 34.6, 38.2, 44.8]:
        if t < DUR - .3:
            tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
            tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+.9:.2f});')
    # lip-sync (svgOrigin keeps the mouth on the face)
    J.extend(base_v2.lip_events(LIPS["golu"], LIPS["fps"], "#g-mouth", "#g-smile", "-62 -314"))
    J.extend(base_v2.kid_lip_events(LIPS["kids"], LIPS["fps"], "kidA"))
    J.extend(base_v2.kid_lip_events(LIPS["kids"], LIPS["fps"], "kidB", lag=2))

GOLU_X = f'''
    <g id="bump" opacity="0"><ellipse cx="{BUMP[0]}" cy="{BUMP[1]}" rx="30" ry="22" fill="#ff9aa5"/><ellipse cx="{BUMP[0]-8}" cy="{BUMP[1]-8}" rx="10" ry="6" fill="#fff" opacity=".6"/></g>
    <g id="stars" opacity="0">''' + "".join(
    f'<path d="M{BUMP[0]+90*math.cos(a):.0f},{BUMP[1]-50+28*math.sin(a):.0f} l6,14 14,6 -14,6 -6,14 -6,-14 -14,-6 14,-6Z" fill="#ffd21c"/>'
    for a in [k * 2 * math.pi / 4 for k in range(4)]) + '</g>'
hp_end = GOLU.rindex('</g>', 0, GOLU.rindex('</g>'))   # inside g-head
GOLU = GOLU[:hp_end] + GOLU_X + GOLU[hp_end:]

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(36))
    sunrays = "".join(f'<path d="M0,-92 L12,-120 L-12,-120Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    rays = "".join(f'<path d="M0,0 L{300*math.cos(a-0.12):.0f},{300*math.sin(a-0.12):.0f} L{300*math.cos(a+0.12):.0f},{300*math.sin(a+0.12):.0f}Z" fill="#fff6a8" opacity=".55"/>' for a in [k * 2 * math.pi / 12 for k in range(12)])
    fruits = "".join(f'<g class="fr" id="f{k}">{fn("fx%d" % k)}</g>' for k, (_, fn) in enumerate(FRUITS))
    labels = ""
    for k, (hi, en, c) in enumerate([("सेब", "Apple", "#d81b3a"), ("केला", "Banana", "#c98a00"), ("तरबूज़", "Watermelon", "#0a7d33")]):
        x = ROW[k][0]
        labels += (f'<text id="lb{k}" x="{x}" y="{ROW[k][1]-175}" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="76" fill="{c}" stroke="#fff" stroke-width="12" paint-order="stroke" opacity="0">{hi}</text>'
                   f'<text id="le{k}" x="{x}" y="{ROW[k][1]+180}" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="{50 if k == 2 else 58}" fill="#1565c0" stroke="#fff" stroke-width="10" paint-order="stroke" opacity="0">{en}</text>')
    flowers = "".join(ns["flower"](x, y, c, i) for i, (x, y, c) in enumerate([(40, 1890, "#ff6b9a"), (1040, 1880, "#a66bff"), (990, 1905, "#ffc51c")]))
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}{ns["F3D"]}</defs>
<rect width="1080" height="1720" fill="url(#gSky)"/>
<g transform="translate(985,365) scale(.6)"><g id="sunface">{sunrays}</g><circle r="80" fill="url(#gSun)"/>
  <ellipse cx="-24" cy="-10" rx="7" ry="10" fill="#7a4a00"/><ellipse cx="24" cy="-10" rx="7" ry="10" fill="#7a4a00"/>
  <path d="M-26,16 q26,24 52,0" stroke="#7a4a00" stroke-width="6" fill="none" stroke-linecap="round"/></g>
{cloud("cl0", 170, 760, .8)}{cloud("cl1", 880, 700, .7)}{cloud("cl2", 600, 1120, .55)}
<ellipse cx="160" cy="1400" rx="520" ry="200" fill="url(#gHillA)"/><ellipse cx="980" cy="1420" rx="520" ry="220" fill="url(#gHillB)"/>
<rect x="30" y="120" width="26" height="1260" rx="12" fill="#c97a3c"/><rect x="1024" y="120" width="26" height="1260" rx="12" fill="#c97a3c"/>
{awning()}
<g id="flag" transform="translate(1037,120)"><path d="M0,0 V-90" stroke="#8a5a1c" stroke-width="6"/><path d="M0,-90 L-60,-72 L0,-54Z" fill="#ffd21c"/></g>
<rect x="0" y="1720" width="1080" height="200" fill="url(#gGround)"/>
{flowers}
{crate(930, 1300, pile_oranges())}
<rect x="0" y="1360" width="1080" height="380" fill="url(#gWood)"/>
<rect x="-10" y="1340" width="1100" height="34" rx="14" fill="url(#gWoodTop)"/>
<path d="M0,1480 H1080 M0,1600 H1080" stroke="#a65e2a" stroke-width="6" opacity=".45"/>
<g transform="translate(190,1345)" filter="url(#f3d)">{MITHU}</g>
<g id="orng">{orange("orx")}</g>
<g transform="translate({CEN[0]},{CEN[1]-20})"><g id="rays" opacity="0">{rays}</g></g>
<g transform="translate({CEN[0]},{CEN[1]})">{BOX}</g>
{KIDS}
<g transform="translate({GX},{GY}) scale({GS})" filter="url(#f3d)"><g id="gjump"><g id="gwrap">{GOLU}</g></g></g>
{fruits}
<g id="lbl" opacity="0">{labels}</g>
{conf}
</svg>'''
    css = base_v2.FONT_CSS + """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#8fdcff}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0;transform-origin:50% 60%}
#punch{position:absolute;inset:0;transform-origin:50% 55%}
#world{position:absolute;inset:0}
.word{position:absolute;left:60px;width:870px;top:430px;text-align:center;line-height:1.08;white-space:nowrap}
.word .hi{font-size:124px;font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(0,40,90,.18)}
.word .en{font-size:86px;font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(0,40,90,.18)}
.badge{position:absolute;top:330px;left:70px;padding:12px 26px;border-radius:40px;background:rgba(255,255,255,.94);color:#6a1fc2;font-size:38px;font-weight:800;box-shadow:0 6px 0 rgba(0,60,120,.15)}
"""
    js = "\n".join(J)
    fit = """
function fitWords(){ document.querySelectorAll('.word > div').forEach(function(el){
  if(!el.dataset.fs) el.dataset.fs = parseFloat(getComputedStyle(el).fontSize);
  var fs = +el.dataset.fs; el.style.fontSize = fs + 'px'; el.style.display='inline-block';
  while (el.offsetWidth > 860 && fs > 40) { fs -= 2; el.style.fontSize = fs + 'px'; }
  el.style.display='block'; }); }
fitWords(); if (document.fonts) document.fonts.ready.then(fitWords);"""
    return f'''<!doctype html><html lang="hi" data-resolution="portrait"><head><meta charset="UTF-8"/>
<script src="assets/gsap.min.js"></script><style>{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
  <audio id="song" class="clip" src="assets/song.mp3" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
  <div id="stage" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0"><div id="cam"><div id="punch">{svg}{overlays()}</div></div></div>
</div>
<script>
{fit}
const tl = gsap.timeline({{paused:true}});
{js}
tl.set({{}},{{}},{DUR});
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl; tl.seek(0);
</script></body></html>'''

open(f"{PROJ}/index.html", "w").write(html())
print("ok", len(J))
