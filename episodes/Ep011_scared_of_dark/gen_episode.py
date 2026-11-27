"""Golu & Dost Ep 11 — गोलू की कहानियाँ #3: अंधेरे से डर | Scared of the Dark (soft-3D glossy, Golu's playroom at night).
usage: python3 gen_episode.py <project dir>   (needs timing.json next to this file and <proj>/assets/lips.json)"""
import json, math, sys, os, random
PROJ = sys.argv[1]; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json")); DUR = T["DUR"]; D = T["D"]
CUE = dict((k, v) for k, v in T["CUES"])
lips = json.load(open(f"{PROJ}/assets/lips.json"))
END = lambda lid: CUE[lid] + D[lid]

# ---- v2 cast from the series template (GOLU, KIDS, gradients, f3d) + glossy Mithu + v2 Bunny (Ep6 cast files)
tsrc = open("/home/claude/golu_pipeline/gen_episode_template.py").read()
ns = {"math": math}
exec(tsrc[tsrc.index("COLS = ["):tsrc.index("def overlays():")], ns)
rg, GOLU, KIDS = ns["rg"], ns["GOLU"], ns["KIDS"]
# scarf knot fix (bible: yellow knot always visible, left of the collar)
FLAP = '<path d="M-12,-238 l-34,58 l52,-30z" fill="#ff9a5c"/><circle cx="0" cy="-236" r="13" fill="#ffd24a"/>'
assert FLAP in GOLU
GOLU = GOLU.replace(FLAP, FLAP + '<g transform="translate(-52,-220)"><ellipse cx="-17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(-18 -17 0)"/><ellipse cx="17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(18 17 0)"/><circle r="12" fill="#ffd24a" stroke="#e09400" stroke-width="3"/><circle cx="-4" cy="-4" r="4" fill="#fff6c0"/></g>')
# NEW for Ep8: angry face parts (soft red cheeks + flush, slanted brows, pouty frown); normal brows get an id
BROWS = '<path d="M-104,-460 q34,-22 64,-6" stroke="#5a78cf" stroke-width="9" fill="none" stroke-linecap="round"/>\n    <path d="M40,-466 q30,-16 64,6" stroke="#5a78cf" stroke-width="9" fill="none" stroke-linecap="round"/>'
assert BROWS in GOLU
GOLU = GOLU.replace(BROWS, f'<g id="g-brows">{BROWS}</g>')
CHEEKS = '<ellipse cx="-118" cy="-318" rx="36" ry="22" fill="url(#gCheek)"/><ellipse cx="118" cy="-318" rx="36" ry="22" fill="url(#gCheek)"/>'
assert CHEEKS in GOLU
ANGRY = ('<g id="g-angry" opacity="0"><ellipse cx="0" cy="-318" rx="160" ry="74" fill="#ff5a6a" opacity=".16"/>'
         '<ellipse cx="-118" cy="-318" rx="62" ry="40" fill="url(#gRed)"/><ellipse cx="118" cy="-318" rx="62" ry="40" fill="url(#gRed)"/>'
         '<path d="M-114,-478 L-42,-456" stroke="#3a2a55" stroke-width="13" stroke-linecap="round"/><path d="M42,-456 L114,-478" stroke="#3a2a55" stroke-width="13" stroke-linecap="round"/></g>')
FROWN = '<path id="g-frown" d="M-94,-280 q32,-28 64,0" stroke="#7a2140" stroke-width="10" fill="none" stroke-linecap="round" opacity="0"/>'
WORRY = ('<g id="g-worry" opacity="0"><path d="M-106,-454 L-44,-486" stroke="#5a78cf" stroke-width="10" stroke-linecap="round"/><path d="M44,-486 L106,-454" stroke="#5a78cf" stroke-width="10" stroke-linecap="round"/></g>')
GOLU = GOLU.replace(CHEEKS, CHEEKS + ANGRY + FROWN + WORRY)
F3D = tsrc[tsrc.index('<filter id="f3d"'):tsrc.index('</filter>') + len('</filter>')]
MITHU = open(f"{HERE}/mithu_src.txt").read()
MITHU = MITHU.replace('<g id="m-beak">', '<g id="m-hat" opacity="0"><g transform="translate(10,-262) rotate(-10)"><rect x="-74" y="-40" width="84" height="58" rx="20" fill="#e23b54"/><ellipse cx="28" cy="2" rx="62" ry="30" fill="#e23b54"/><rect x="-74" y="-40" width="22" height="58" rx="8" fill="#ffffff"/><rect x="-40" y="-40" width="16" height="58" fill="#ffffff" opacity=".9"/><ellipse cx="66" cy="4" rx="24" ry="22" fill="#ffd24a"/><ellipse cx="-10" cy="-26" rx="34" ry="8" fill="#ffffff" opacity=".45"/></g></g><g id="m-beak">', 1)
assert 'id="m-hat"' in MITHU
BUNNY = open(f"{HERE}/bunny_v2.svg.txt").read()
def lg(id_, stops, x2=0, y2=1):
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="{x2}" y2="{y2}">' + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops) + '</linearGradient>'
BK = [("#ff8a7e", "#ff5a4e", "#d8322a"), ("#ffe07a", "#ffc51c", "#e09a00"), ("#8fc0ff", "#4a8fe0", "#2a62b8"), ("#8fe8a0", "#47c46a", "#238a44"), ("#ffbf86", "#ff8a3d", "#d8621a")]
defs = ns["defs"] + F3D + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    rg("gBun", [(0, "#ffffff"), (.6, "#f1ecff"), (1, "#c7b8ef")], "38%", "30%", "75%"),
    rg("gBunIn", [(0, "#ffd3e2"), (1, "#f59ab9")], "45%", "40%", "70%"),
    rg("gRed", [(0, "#ff3b3b"), (.6, "#ff5a5acc"), (1, "#ff5a5a00")], "50%", "50%", "50%"),
    rg("gTed", [(0, "#f2c58e"), (.55, "#c98a4e"), (1, "#8f5a2c")], "38%", "30%", "75%"),
    rg("gTedIn", [(0, "#ffe6c8"), (1, "#f0c08c")], "45%", "40%", "70%"),
    rg("gNL", [(0, "#fff3b0"), (.35, "#ffd86a88"), (1, "#ffc04a00")], "50%", "50%", "50%"),
    rg("gStar", [(0, "#fffbe0"), (.5, "#ffd23f"), (1, "#f0a000")], "40%", "35%", "70%"),
    rg("gMoon", [(0, "#fffbe6"), (.7, "#fff0b0"), (1, "#f2d77a")], "40%", "35%", "70%"),
    lg("gBeam", [(0, "#fff3b0"), (1, "#ffe58a")], 1, 0),
    lg("gBox", [(0, "#5fc4b8"), (1, "#2f8f86")]),
    rg("gSteam", [(0, "#ffffff"), (.7, "#f4f7ff"), (1, "#d8e2f5")], "40%", "35%", "70%"),
    rg("gSunW", [(0, "#fff6d0"), (.5, "#ffc36a"), (1, "#ff9a4a")], "45%", "40%", "60%"),
    rg("gLamp", [(0, "#fff4c8"), (.5, "#ffe08a55"), (1, "#ffe08a00")], "50%", "50%", "50%"),
    rg("gBall", [(0, "#ffffff"), (.35, "#ff7fb0"), (1, "#c83a78")], "35%", "30%", "75%"),
    rg("gPetal", [(0, "#ffe0ee"), (1, "#ff7fb0")], "40%", "30%", "75%"),
    rg("gFlame", [(0, "#fffbe0"), (.5, "#ffd23f"), (1, "#ff8a00")], "50%", "65%", "60%"),
    lg("gWall", [(0, "#ffefdc"), (.7, "#ffe0c4"), (1, "#ffd2ae")]),
    lg("gWin", [(0, "#141a4a"), (.6, "#26326f"), (1, "#3a4a94")]),
    lg("gFloor", [(0, "#eebb85"), (1, "#d99a5f")]),
    lg("gWood", [(0, "#d99a5b"), (1, "#a8693a")]),
    lg("gCurt", [(0, "#cbbcff"), (1, "#9c86f0")]),
    lg("gCandle", [(0, "#fff8e6"), (1, "#f2dcb0")], 1, 0),
    '<filter id="fblur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>',
    '<filter id="fsoft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>',
] + [rg(f"gBk{k}", [(0, a), (.55, b), (1, c)], "35%", "28%", "80%") for k, (a, b, c) in enumerate(BK)])

ka, kb = KIDS[KIDS.index('<g id="kidA"'):KIDS.index('<g id="kidB"')], KIDS[KIDS.index('<g id="kidB"'):]
ka = ka.replace(' transform="translate(150,1880) scale(.78)"', '')
kb = kb.replace(' transform="translate(930,1880) scale(.78)"', '')
SOCK_SHAPE = '<g transform="translate(10,-262) rotate(-10)"><rect x="-74" y="-40" width="84" height="58" rx="20" fill="#e23b54"/><ellipse cx="28" cy="2" rx="62" ry="30" fill="#e23b54"/><rect x="-74" y="-40" width="22" height="58" rx="8" fill="#ffffff"/><rect x="-40" y="-40" width="16" height="58" fill="#ffffff" opacity=".9"/><ellipse cx="66" cy="4" rx="24" ry="22" fill="#ffd24a"/><ellipse cx="-10" cy="-26" rx="34" ry="8" fill="#ffffff" opacity=".45"/></g>'
# ---- Ep11 layout (all in the scene's shifted coords; scene group translate(0,-200))
TORCH = ('<g id="torch" opacity="0"><g transform="translate(122,-140) rotate(56)">'
         '<rect x="-46" y="-17" width="82" height="34" rx="12" fill="#2f6fd6"/><rect x="-40" y="-11" width="70" height="10" rx="5" fill="#8fc0ff" opacity=".7"/>'
         '<path d="M34,-24 L58,-30 L58,30 L34,24Z" fill="#ffc51c"/><ellipse cx="58" cy="0" rx="8" ry="30" fill="#fff6c0"/>'
         '<rect x="-12" y="-21" width="14" height="10" rx="4" fill="#ff5a4e"/></g></g>')
KBARM = '<g id="kB-armR"><path d="M60,-232 q56,30 62,92" stroke="#c8875e" stroke-width="26" fill="none" stroke-linecap="round"/>'
assert KBARM in kb
kb = kb.replace(KBARM, KBARM + TORCH)
GX, GY, GS = 470, 1840, .62
KS = .46
PARI, CHINTU = (80, 1850), (212, 1856)
BOX = (880, 1850)
BUN_HIDE, BUN_UP, BS = (880, 2010), (880, 1712), .5
MI = (712, 1212); MS = .42
HAT_WORLD = (MI[0] - 10 * MS, MI[1] - 262 * MS)
SHC = (890, 1075)                        # wall shadow centre
HAND = (276, 1714)                       # Chintu's torch hand (arm raised -100)
TED = (470, 1762)

WORDS = [
    ("wClick", "क्लिक!", "Click!", "#e65100", "#1565c0"),
    ("wShadow", "परछाईं?", "Shadow?", "#6a1fc2", "#1565c0"),
    ("wScared", "मुझे डर लग रहा है", "I'm scared", "#7b1fa2", "#1565c0"),
    ("wOk", "डरना ठीक है!", "It's okay to be scared!", "#1e63d6", "#c2185b"),
    ("wTorch", "टॉर्च!", "Torch!", "#e65100", "#1565c0"),
    ("wLight", "रोशनी!", "Light!", "#f39c00", "#1565c0"),
    ("wEars", "बनी के कान!", "Bunny's ears!", "#d81b60", "#1565c0"),
    ("wHat", "मेरी टोपी!", "My hat!", "#e23b54", "#1565c0"),
    ("wNL", "रात का लैंप", "Night light", "#f39c00", "#1565c0"),
    ("wTeddy", "टेडी को गले लगाओ", "Hug your teddy", "#a0522d", "#1565c0"),
    ("wBrave", "मैं बहादुर हूँ!", "I am brave!", "#2e7d32", "#1565c0"),
    ("wBye", "शुभ रात्रि! कल फिर मिलेंगे!", "Good night! See you tomorrow!", "#6a1fc2", "#1565c0"),
]
MORAL = [("mw0", "बताओ", "Tell someone", "#1e63d6"), ("mw1", "रोशनी करो", "Turn on a light", "#e65100")]
def overlays():
    w = ""
    for i, hi, en, hc, ec in WORDS:
        w += f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div><div class="en" style="color:{ec}">{en}</div></div>'
    w += '<div class="moral" id="wMoral">' + "".join(f'<div class="mw" id="{i}"><div class="hi" style="color:{c}">{hi}</div><div class="en" style="color:{c}">{en}</div></div>' for i, hi, en, c in MORAL) + '</div>'
    return w + '<div class="badge">गोलू की कहानियाँ #3 · Golu\'s Stories</div>'
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
def kid_arm(k, rot, t, hold, wig=True):
    arm = f"#k{k}-armR"
    tl(f'tl.to("{arm}",{{rotation:{rot},duration:.2,ease:"back.out(2)"}},{f(t)});')
    if wig: tl(f'tl.to("{arm}",{{rotation:{rot*0.88:.0f},duration:.15,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(t+.2)});')
    tl(f'tl.to("{arm}",{{rotation:0,duration:.3,ease:"power2.inOut"}},{f(t+hold)});')
def golu_arm(side, rot, t, hold=None, wave=False, d=.22):
    sel, o = ("#g-armR", "128 -226") if side == "R" else ("#g-armL", "-128 -226")
    tl(f'tl.to("{sel}",{{rotation:{rot},svgOrigin:"{o}",duration:{d},ease:"back.out(2)"}},{f(t)});')
    if wave: tl(f'tl.to("{sel}",{{rotation:{rot + (18 if rot < 0 else -18)},svgOrigin:"{o}",duration:.16,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(t+.22)});')
    if hold is not None: tl(f'tl.to("{sel}",{{rotation:0,svgOrigin:"{o}",duration:.3,ease:"power2.inOut"}},{f(t+hold)});')
def g_hop(t, h=26):
    tl(f'tl.fromTo("#rgolu",{{y:0}},{{y:{-h},duration:.16,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def g_squash(t, amt=.1):
    tl(f'tl.fromTo("#rgolu",{{scaleX:1,scaleY:1}},{{scaleX:{1+amt},scaleY:{1-amt},svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def bunny_cheer(t, hold=.8):
    tl(f'tl.to("#b-armL",{{rotation:120,svgOrigin:"-60 -148",duration:.18,ease:"back.out(2)"}},{f(t)}); tl.to("#b-armR",{{rotation:-120,svgOrigin:"60 -148",duration:.18,ease:"back.out(2)"}},{f(t+.06)});')
    tl(f'tl.to("#b-armL",{{rotation:0,svgOrigin:"-60 -148",duration:.3}},{f(t+hold)}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -148",duration:.3}},{f(t+hold+.06)});')
def b_hop(t, h=40, d=.18):
    tl(f'tl.fromTo("#rbunny",{{y:0}},{{y:{-h},duration:{d},yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')

# ---- transform helpers (attr transforms on wrappers; inner groups squash/spin)
def tfr(x, y, r=0, s=1.0): return f"translate({x:.1f},{y:.1f}) rotate({r:.1f}) scale({s:.3f})"
BKS = {}
def bset(k, x, y, r=0, s=1.0, t=None):
    BKS[k] = (x, y, r, s)
    if t is None: tl(f'gsap.set("#bk{k}",{{attr:{{transform:"{tfr(x, y, r, s)}"}}}});')
    else: tl(f'tl.set("#bk{k}",{{attr:{{transform:"{tfr(x, y, r, s)}"}}}},{f(t)});')
def bmove(k, t, x, y, r=None, s=None, d=.5, ease="power2.inOut"):
    x0, y0, r0, s0 = BKS[k]; r = r0 if r is None else r; s = s0 if s is None else s
    tl(f'tl.fromTo("#bk{k}",{{attr:{{transform:"{tfr(x0, y0, r0, s0)}"}}}},{{attr:{{transform:"{tfr(x, y, r, s)}"}},duration:{d},ease:"{ease}",immediateRender:false}},{f(t)});')
    BKS[k] = (x, y, r, s)
def barc(k, t, mid, end, d1, d2):
    bmove(k, t, *mid, d=d1, ease="power2.out"); bmove(k, t + d1, *end, d=d2, ease="power2.in")
def bsquash(k, t, amt=.18):
    tl(f'tl.fromTo("#bki{k}",{{scaleX:1,scaleY:1}},{{scaleX:{1+amt},scaleY:{1-amt},svgOrigin:"0 {BH/2}",duration:.08,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
BUN = {}
def bunpos(x, y, s=BS):
    BUN["p"] = (x, y, s); tl(f'gsap.set("#pbunny",{{attr:{{transform:"translate({x},{y}) scale({s})"}}}});')
def bunmove(t, x, y, d=.4, ease="power2.inOut"):
    x0, y0, s = BUN["p"]
    tl(f'tl.fromTo("#pbunny",{{attr:{{transform:"translate({x0},{y0}) scale({s})"}}}},{{attr:{{transform:"translate({x},{y}) scale({s})"}},duration:{d},ease:"{ease}",immediateRender:false}},{f(t)});')
    BUN["p"] = (x, y, s)
def bunny_sad(t0, t1):
    tl(f'tl.set("#b-smile",{{opacity:0}},{f(t0)}); tl.set("#b-sad",{{opacity:1}},{f(t0)}); tl.set("#b-smile",{{opacity:1}},{f(t1)}); tl.set("#b-sad",{{opacity:0}},{f(t1)});')
    tl(f'tl.to("#b-earL",{{rotation:-28,svgOrigin:"-40 -300",duration:.45,ease:"power2.out"}},{f(t0)}); tl.to("#b-earR",{{rotation:30,svgOrigin:"44 -300",duration:.5,ease:"power2.out"}},{f(t0+.08)});')
    tl(f'tl.to("#b-earL",{{rotation:0,svgOrigin:"-40 -300",duration:.35,ease:"back.out(2.5)"}},{f(t1)}); tl.to("#b-earR",{{rotation:0,svgOrigin:"44 -300",duration:.35,ease:"back.out(2.5)"}},{f(t1+.07)});')
def cam(t, s, x=0, y=0, d=.4, ease="power2.inOut"):
    tl(f'tl.to("#cam",{{scale:{s},x:{x},y:{y},duration:{d},ease:"{ease}"}},{f(t)});')

def golu_rest_pose():
    tl(f'gsap.set("#g-armR",{{rotation:38,svgOrigin:"128 -226"}}); gsap.set("#g-armL",{{rotation:-38,svgOrigin:"-128 -226"}});')
def dark(t, a, b, d=.25):
    tl(f'tl.to("#darkA",{{opacity:{a},duration:{d},ease:"power2.out"}},{f(t)}); tl.to("#darkB",{{opacity:{b},duration:{d},ease:"power2.out"}},{f(t)});')
def bunpos(x, y, s=BS):
    BUN["p"] = (x, y, s); tl(f'gsap.set("#pbunny",{{attr:{{transform:"translate({x},{y}) scale({s})"}}}});')

def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set(".mw",{opacity:0,scale:.3}); gsap.set(".mw .en",{opacity:0}); gsap.set(".cbadge",{opacity:0}); gsap.set(".conf",{opacity:0}); gsap.set("#stars",{opacity:0}); gsap.set("#speed",{opacity:0}); gsap.set("#speedv",{opacity:0}); gsap.set(".heart",{opacity:0});')
    tl('gsap.set("#darkA",{opacity:0}); gsap.set("#darkB",{opacity:0}); gsap.set("#shadow",{opacity:0}); gsap.set("#cone",{opacity:0}); gsap.set("#nlglow",{opacity:0}); gsap.set("#sockf",{opacity:0}); gsap.set("#lampglow",{opacity:.6});')
    tl('gsap.set("#g-trunk",{svgOrigin:"0 -352",rotation:-30}); gsap.set("#g-ear",{svgOrigin:"-90 -380"}); gsap.set("#g-ear2",{svgOrigin:"90 -380"});')
    tl('gsap.set("#kA-armL",{svgOrigin:"-62 -230"}); gsap.set("#kA-armR",{svgOrigin:"62 -230"}); gsap.set("#kB-armL",{svgOrigin:"-60 -232"}); gsap.set("#kB-armR",{svgOrigin:"60 -232"});')
    golu_rest_pose(); tl('gsap.set(".pup",{x:10,y:-16});')
    tl(f'gsap.set("#cam",{{transformOrigin:"540px 1360px"}});')
    tl('gsap.set("#mlean",{rotation:16,svgOrigin:"0 0"});')
    nb = int(DUR / BEAT)
    tl(f'tl.to("#g-body",{{scaleY:.955,scaleX:1.022,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-head",{{y:9,rotation:2,svgOrigin:"0 -240",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#kA",{{y:-8,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.1);')
    tl(f'tl.to("#kB",{{y:-7,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.33);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.2);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.45);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#b-head",{{rotation:3,svgOrigin:"0 -150",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.15);')
    tl(f'tl.to("#twinkle",{{opacity:.35,duration:.75,yoyo:true,repeat:{int(DUR/.75)-1},ease:"sine.inOut"}},0);')
    for k in range(int(DUR / 3)):
        t = 2.2 + k * 3.0
        if t > DUR - 1.5: break
        tl(f'tl.to("#g-ear",{{rotation:-8,duration:.15,yoyo:true,repeat:1}},{t:.2f}); tl.to("#g-ear2",{{rotation:8,duration:.15,yoyo:true,repeat:1}},{t+.12:.2f});')
    bunpos(*BUN_HIDE)
    # ===== HOOK: lamp on, Mithu leaning on the lamp string -> click -> dark -> big long-eared shadow
    ck = T["click"]
    tl('tl.set("#wClick",{opacity:1,scale:.85},0); tl.to("#wClick",{scale:1,duration:.3,ease:"back.out(3)"},0.02);')
    mithu_talk(CUE["a1"], D["a1"])
    tl(f'tl.fromTo("#bead",{{y:0}},{{y:22,duration:.08,yoyo:true,repeat:1,immediateRender:false}},{f(ck-.08)});')
    tl(f'tl.to("#mlean",{{rotation:0,svgOrigin:"0 0",duration:.35,ease:"back.out(2)"}},{f(ck+.1)});')
    tl(f'tl.to("#lampglow",{{opacity:0,duration:.12}},{f(ck)}); tl.to("#bulb",{{opacity:0,duration:.12}},{f(ck)});')
    dark(ck, .58, .3, .18)
    tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.05,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(ck)});')
    tl(f'tl.to("#shadow",{{opacity:.85,duration:.35}},{f(T["shadow"])});')
    wob_end = T["light"]
    n = int((wob_end - T["shadow"]) / .6)
    tl(f'tl.fromTo("#shadowi",{{rotation:-3,scaleX:1}},{{rotation:3,scaleX:1.05,svgOrigin:"0 180",duration:.6,yoyo:true,repeat:{max(1,n)},ease:"sine.inOut",immediateRender:false}},{f(T["shadow"])});')
    tl(f'tl.to("#shEarR",{{rotation:14,svgOrigin:"55 -150",duration:.45,yoyo:true,repeat:{max(1,int(n*1.3))},ease:"sine.inOut"}},{f(T["shadow"]+.2)});')
    word_out("wClick", T["gasp"] - .1)
    # gasp take: anticipation squash, ears out, eyes to the shadow, worried brows
    g = T["gasp"]
    g_squash(g - .1, .08); g_hop(g, 22)
    tl(f'tl.to("#g-ear",{{rotation:-18,duration:.15,ease:"back.out(3)"}},{f(g)}); tl.to("#g-ear2",{{rotation:18,duration:.17,ease:"back.out(3)"}},{f(g+.05)});')
    look(18, g, -26); tl(f'tl.to(".pup",{{scale:1.25,transformOrigin:"50% 50%",duration:.15}},{f(g)});')
    tl(f'tl.set("#g-brows",{{opacity:0}},{f(g)}); tl.set("#g-worry",{{opacity:1}},{f(g)});')
    trunk(-6, g, .2)
    cam(g, 1.08, -40, 60, .35, "power2.out")
    card("wShadow", CUE["a3"], END("a3") + .1); mithu_talk(CUE["a3"], D["a3"])
    tl(f'tl.to(".mpup",{{x:6,y:-4,duration:.2}},{f(CUE["a3"])});')
    # scared: ears droop, trembling, squeezes teddy
    s = T["scared"]
    cam(s - .2, 1.08, 30, -20, .45)
    tl(f'tl.to("#g-ear",{{rotation:14,duration:.4,ease:"power2.out"}},{f(s)}); tl.to("#g-ear2",{{rotation:-14,duration:.45,ease:"power2.out"}},{f(s+.06)});')
    nt = int((T["breath"] - s) / .1)
    tl(f'tl.fromTo("#rgolu",{{x:0}},{{x:-5,duration:.05,yoyo:true,repeat:{nt*2-1},ease:"none",immediateRender:false}},{f(s)});')
    tl(f'tl.fromTo("#tedi",{{scale:1}},{{scale:.9,svgOrigin:"0 40",duration:.2,yoyo:true,repeat:1,immediateRender:false}},{f(s+.1)});')
    card("wScared", s, END("b2") + .15)
    kids_talk(CUE["b2"], D["b2"])
    tl(f'tl.to("#kidA .kpup, #kidB .kpup",{{x:8,duration:.2}},{f(CUE["b2"])});')
    cam(END("b1") + .1, 1.0, 0, 0, .45)
    # friends: it's okay to be scared
    kids_talk(CUE["c1"], D["c1"]); kids_talk(CUE["c2"], D["c2"])
    kid_arm("A", -60, CUE["c1"], D["c1"] + .2); kid_arm("B", -60, CUE["c1"] + .06, D["c1"] + .1)
    card("wOk", CUE["c1"], END("c2") + .15)
    look(-16, CUE["c1"], -6)
    # one calming breath (callback to Ep8): swell + trunk up, then out
    b = T["breath"]
    tl(f'tl.to("#gwrap",{{scaleX:1.03,scaleY:1.055,svgOrigin:"0 0",duration:.5,ease:"sine.inOut"}},{f(b)}); tl.to("#gwrap",{{scaleX:1,scaleY:1,svgOrigin:"0 0",duration:.5,ease:"sine.inOut"}},{f(b+.5)});')
    trunk(-90, b, .45, "sine.inOut"); trunk(-30, b + .5, .4, "power2.out")
    tl(f'tl.to("#g-ear",{{rotation:0,duration:.4}},{f(b+.3)}); tl.to("#g-ear2",{{rotation:0,duration:.4}},{f(b+.36)});')
    tl(f'tl.to(".pup",{{scale:1,transformOrigin:"50% 50%",duration:.3}},{f(b+.4)});')
    # TORCH: Chintu raises the torch, Golu brightens
    tc = T["torch"]
    tl(f'tl.set("#g-worry",{{opacity:0}},{f(tc)}); tl.set("#g-brows",{{opacity:1}},{f(tc)});')
    kid_arm("B", -100, tc - .1, T["nl"] - tc + .2, wig=False)
    tl(f'tl.fromTo("#torch",{{opacity:0}},{{opacity:1,duration:.15,immediateRender:false}},{f(tc)});')
    card("wTorch", tc, END("c3") + .1); look(-18, tc, -14); happy(tc + .1, tc + .7); g_hop(tc + .1, 14)
    # COUNT 1-2-3 -> LIGHT (cone on the wall, the shadow melts), Bunny zooms up from behind the toy box
    for k in range(3):
        tk = T["count"] + k * D["d1"] * 0.2
        tl(f'tl.fromTo("#bb{k}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,transformOrigin:"50% 50%",duration:.25,ease:"back.out(2)",immediateRender:false}},{f(tk)});')
    kids_talk(CUE["d1"], D["d1"])
    L = T["light"]
    tl(f'tl.to(".cbadge",{{opacity:0,duration:.25}},{f(L+.3)});')
    tl(f'tl.fromTo("#cone",{{opacity:0}},{{opacity:.75,duration:.2,immediateRender:false}},{f(L)}); tl.fromTo("#cone",{{opacity:.75}},{{opacity:.6,duration:.08,yoyo:true,repeat:3,immediateRender:false}},{f(L+.2)});')
    tl(f'tl.to("#shadow",{{opacity:0,duration:.45}},{f(L+.1)})'); dark(L, .45, .24, .3)
    card("wLight", L, CUE["d2"] + .2); look(20, L, -24)
    P = T["pop"]
    tl(f'tl.fromTo("#pbunny",{{attr:{{transform:"translate({BUN_HIDE[0]},{BUN_HIDE[1]}) scale({BS})"}}}},{{attr:{{transform:"translate({BUN_UP[0]},{BUN_UP[1]-60}) scale({BS})"}},duration:.22,ease:"power3.out",immediateRender:false}},{f(P)});')
    tl(f'tl.fromTo("#pbunny",{{attr:{{transform:"translate({BUN_UP[0]},{BUN_UP[1]-60}) scale({BS})"}}}},{{attr:{{transform:"translate({BUN_UP[0]},{BUN_UP[1]}) scale({BS})"}},duration:.3,ease:"bounce.out",immediateRender:false}},{f(P+.22)});')
    BUN["p"] = (BUN_UP[0], BUN_UP[1], BS)
    tl(f'tl.set("#speedv",{{opacity:1}},{f(P)}); tl.to("#speedv",{{opacity:0,duration:.25}},{f(P+.25)});')
    tl(f'tl.to(".bpup",{{x:-8,duration:.2}},{f(P+.3)});')
    bunny_sad(CUE["d2"] - .1, END("d2") + .2)
    # giggle: it's only Bunny's ears!
    gg = T["giggle"]; happy(gg, END("d3") + .2); g_hop(gg + .1, 18); g_hop(gg + .5, 12)
    card("wEars", gg, END("d3") + .05)
    tl(f'tl.set("#b-eyes",{{opacity:0}},{f(gg+.3)}); tl.set("#b-happy",{{opacity:1}},{f(gg+.3)}); tl.set("#b-eyes",{{opacity:1}},{f(END("d3"))}); tl.set("#b-happy",{{opacity:0}},{f(END("d3"))});')
    tl(f'tl.to("#b-earL",{{rotation:-14,svgOrigin:"-40 -300",duration:.15,yoyo:true,repeat:3}},{f(gg+.3)}); tl.to("#b-earR",{{rotation:16,svgOrigin:"44 -300",duration:.15,yoyo:true,repeat:3}},{f(gg+.4)});')
    kids_cheer(gg + .2, .8, who=("A",))
    # sock lands on Mithu = his 4th hat
    sk = T["sock"]
    tl(f'tl.fromTo("#sockf",{{opacity:1,y:-520,rotation:-120}},{{opacity:1,y:0,rotation:0,svgOrigin:"10 -262",duration:.45,ease:"power2.in",immediateRender:false}},{f(sk)}); tl.set("#sockf",{{opacity:0}},{f(sk+.45)}); tl.set("#m-hat",{{opacity:1}},{f(sk+.45)});')
    tl(f'tl.fromTo("#m-all",{{scaleY:1}},{{scaleY:.86,svgOrigin:"0 0",duration:.09,yoyo:true,repeat:1,immediateRender:false}},{f(sk+.45)});')
    tl(f'tl.set("#stars",{{opacity:1}},{f(sk+.45)}); tl.fromTo("#starsR",{{rotation:0}},{{rotation:200,svgOrigin:"{HAT_WORLD[0]:.0f} {HAT_WORLD[1]-10:.0f}",duration:1.0,ease:"none",immediateRender:false}},{f(sk+.45)}); tl.set("#stars",{{opacity:0}},{f(sk+1.45)});')
    card("wHat", CUE["d4"], END("d4") + .1); mithu_talk(CUE["d4"], D["d4"]); look(14, sk + .4, -30)
    # NIGHT LIGHT: torch off, the star lamp glows warm
    nl = T["nl"]
    tl(f'tl.to("#cone",{{opacity:0,duration:.25}},{f(nl+.1)}); tl.to("#torch",{{opacity:0,duration:.2}},{f(nl+.25)});')
    tl(f'tl.fromTo("#nlglow",{{opacity:0,scale:.6}},{{opacity:.9,scale:1,svgOrigin:"{895} {1180}",duration:.45,ease:"back.out(1.6)",immediateRender:false}},{f(nl+.3)});')
    tl(f'tl.fromTo("#nlstar",{{scale:1}},{{scale:1.25,svgOrigin:"895 1180",duration:.18,yoyo:true,repeat:1,immediateRender:false}},{f(nl+.3)});')
    dark(nl + .3, .36, .1, .5); card("wNL", nl, END("e1") + .1); look(18, nl, -30)
    # TEDDY hug
    hg = T["hug"]
    tl(f'tl.fromTo("#tedi",{{scale:1}},{{scale:.86,svgOrigin:"0 40",duration:.22,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(hg+.2)});')
    g_squash(hg + .2, .08); happy(hg + .2, END("e2") + .1); look(0, hg, 10)
    for k in range(3):
        tl(f'tl.fromTo("#ht{k}",{{opacity:0,y:20,scale:.4}},{{opacity:1,y:-60,scale:1,transformOrigin:"50% 50%",duration:.6,ease:"power2.out",immediateRender:false}},{f(hg+.3+k*.18)}); tl.to("#ht{k}",{{opacity:0,duration:.25}},{f(hg+1.0+k*.18)});')
    card("wTeddy", hg, END("e2") + .1)
    # BRAVE
    bv = T["brave"]
    g_squash(bv - .05, .1); g_hop(bv + .05, 34); trunk(-95, bv + .05, .3); trunk(-30, END("e4") + .1, .4, "power2.inOut")
    tl(f'tl.to("#g-ear",{{rotation:-14,duration:.2,ease:"back.out(3)"}},{f(bv+.05)}); tl.to("#g-ear2",{{rotation:14,duration:.22,ease:"back.out(3)"}},{f(bv+.1)}); tl.to("#g-ear",{{rotation:0,duration:.3}},{f(END("e4"))}); tl.to("#g-ear2",{{rotation:0,duration:.3}},{f(END("e4")+.05)});')
    look(0, bv, -20); card("wBrave", bv, END("e4") + .15)
    tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.05,duration:.15,yoyo:true,repeat:1,immediateRender:false}},{f(bv+.05)});')
    kids_talk(CUE["e4"], D["e4"]); kids_cheer(CUE["e4"], 1.0); bunny_cheer(CUE["e4"] + .08, .9); b_hop(CUE["e4"] + .1, 30)
    # MORAL pills
    m = T["moral"]
    tl(f'tl.set("#wMoral",{{opacity:1}},{f(m)});')
    for k, (i, *_r) in enumerate(MORAL):
        tk = m + D["f1"] * (0.42 + 0.3 * k)
        tl(f'tl.fromTo("#{i}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)",immediateRender:false}},{f(tk)});')
        tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.03,duration:.12,yoyo:true,repeat:1,immediateRender:false}},{f(tk)});')
        te = T["f2"] + D["f2"] * (0.05 + 0.5 * k)
        tl(f'tl.fromTo("#{i} .en",{{opacity:0}},{{opacity:1,duration:.2,immediateRender:false}},{f(te)}); tl.fromTo("#{i} .en",{{scale:1}},{{scale:1.2,duration:.15,yoyo:true,repeat:1,immediateRender:false}},{f(te)});')
    tl(f'tl.to("#g-head",{{y:22,duration:.18,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(m+D["f1"]*.4)});')
    tl(f'tl.to(".mw",{{opacity:0,scale:.6,duration:.18}},{f(T["bye"]-.2)});')
    kids_talk(CUE["f2"], D["f2"]); kids_cheer(CUE["f2"], 1.2); happy(CUE["f2"], END("f2") + .2)
    random.seed(11)
    for k in range(30):
        x0 = random.uniform(80, 1000); dly = random.uniform(0, .9); rot = random.uniform(-540, 540)
        tl(f'tl.fromTo("#cf{k}",{{x:{x0:.0f},y:700,rotation:0,opacity:1}},{{x:{x0 + random.uniform(-120,120):.0f},y:{random.uniform(1500,1900):.0f},rotation:{rot:.0f},duration:2.4,ease:"power1.in",immediateRender:false}},{f(CUE["f2"]+dly)}); tl.set("#cf{k}",{{opacity:0}},{f(CUE["f2"]+dly+2.4)});')
    # BYE (trunk wave) + LOOP back to frame 1
    by = T["bye"]
    word_in("wBye", by); word_out("wBye", DUR - .75); happy(by + .1, by + 1.3)
    tl(f'tl.to("#g-trunk",{{rotation:-80,svgOrigin:"0 -352",duration:.25,yoyo:true,repeat:5,ease:"sine.inOut"}},{f(by+.15)}); tl.to("#g-trunk",{{rotation:-30,svgOrigin:"0 -352",duration:.3}},{f(by+1.7)});')
    mithu_talk(CUE["g2"], D["g2"]); kids_cheer(CUE["g2"], .8); bunny_cheer(CUE["g2"] + .1, .7)
    lp = DUR - 1.05
    bunmove(lp, BUN_HIDE[0], BUN_HIDE[1], .28, "power3.in")
    tl(f'tl.set("#speedv",{{opacity:1}},{f(lp+.05)}); tl.to("#speedv",{{opacity:0,duration:.2}},{f(lp+.3)});')
    tl(f'tl.to("#m-hat",{{opacity:0,y:30,duration:.25}},{f(DUR-.95)});')
    tl(f'tl.to("#mlean",{{rotation:16,svgOrigin:"0 0",duration:.35,ease:"power2.inOut"}},{f(DUR-.8)});')
    lo = DUR - .42
    tl(f'tl.to("#lampglow",{{opacity:.6,duration:.2}},{f(lo)}); tl.to("#bulb",{{opacity:1,duration:.2}},{f(lo)}); tl.to("#nlglow",{{opacity:0,duration:.3}},{f(lo)});')
    dark(lo, 0, 0, .3); look(10, DUR - .6, -16)
    tl(f'tl.fromTo("#wClick",{{opacity:0,scale:.5}},{{opacity:1,scale:.85,duration:.28,ease:"power2.out",immediateRender:false}},{DUR-.32:.2f});')
    # blinks (offset)
    t = 2.9
    while t < DUR - 1:
        if not (T["gasp"] - .2 < t < T["breath"]):
            tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t:.2f});')
        tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.1:.2f});')
        tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+.6:.2f});')
        tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.9:.2f});')
        tl(f'tl.to(".bpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.5:.2f});')
        t += 3.3
    def lipsync(levels, mouth, rest_of, rest_all, origin, scales):
        Lv = list(levels)
        for i in range(1, len(Lv) - 1):
            if Lv[i] and not Lv[i-1] and not Lv[i+1]: Lv[i] = 0
        prev = 0
        for i, v in enumerate(Lv):
            t = round(i / lips["fps"], 3)
            if v == prev: continue
            if v == 0: tl(f'tl.set("{mouth}",{{opacity:0}},{t});tl.set("{rest_of(t)}",{{opacity:1}},{t});')
            else: tl(f'tl.set("{mouth}",{{opacity:1,scaleY:{scales[v]},svgOrigin:"{origin}"}},{t});tl.set("{rest_all}",{{opacity:0}},{t});')
            prev = v
    a0, a1 = T["gasp"], T["torch"]
    tl(f'tl.set("#g-smile",{{opacity:0}},{f(a0)}); tl.set("#g-frown",{{opacity:1}},{f(a0)}); tl.set("#g-frown",{{opacity:0}},{f(a1)}); tl.set("#g-smile",{{opacity:1}},{f(a1)});')
    lipsync(lips["golu"], "#g-mouth", lambda t: "#g-frown" if a0 <= t < a1 else "#g-smile", "#g-smile, #g-frown", "-62 -314", [0, .5, .8, 1.1])
    s0, s1 = CUE["d2"] - .1, END("d2") + .2
    lipsync(lips["bunny"], "#b-mouth", lambda t: "#b-sad" if s0 <= t < s1 else "#b-smile", "#b-smile, #b-sad", "0 -204", [0, .55, .8, 1.05])
# ---------------- set: Golu's playroom at NIGHT (Ep8 set re-lit) ----------------
def room():
    planks = "".join(f'<rect x="0" y="{y}" width="1080" height="4" fill="#c88a52" opacity=".45"/>' for y in range(1560, 1920, 70))
    seams = "".join(f'<rect x="{(i*263 + (y//70)*131) % 1080}" y="{y}" width="4" height="70" fill="#c88a52" opacity=".4"/>' for y in range(1500, 1920, 70) for i in range(4))
    stars = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff"/>' for x, y, r in ((110, 780, 4), (170, 860, 3), (330, 770, 3), (130, 960, 3), (350, 900, 4), (200, 1010, 2)))
    win = ('<g transform="translate(0,150)"><rect x="60" y="720" width="330" height="380" rx="28" fill="url(#gWood)"/><rect x="78" y="738" width="294" height="344" rx="18" fill="url(#gWin)"/>'
           f'<g clip-path="url(#clipWin)"><g id="twinkle">{stars}</g><circle cx="290" cy="830" r="70" fill="#fff6c0" opacity=".18"/><circle cx="290" cy="830" r="44" fill="url(#gMoon)"/><circle cx="310" cy="818" r="38" fill="#26326f"/>'
           '<g filter="url(#fblur)"><path d="M78,1060 L120,1010 L170,1040 L170,1082 L78,1082Z" fill="#1a2050" opacity=".8"/><path d="M200,1082 L200,1030 L250,990 L300,1030 L300,1082Z" fill="#1a2050" opacity=".8"/></g></g>'
           '<rect x="219" y="738" width="12" height="344" fill="url(#gWood)"/><rect x="78" y="902" width="294" height="12" fill="url(#gWood)"/>'
           '<path d="M52,712 Q130,820 100,1110 L44,1110 Z" fill="url(#gCurt)"/><path d="M398,712 Q320,820 350,1110 L406,1110 Z" fill="url(#gCurt)"/>'
           '<rect x="36" y="696" width="378" height="24" rx="12" fill="#7b5cd6"/><rect x="50" y="1098" width="350" height="22" rx="11" fill="url(#gWood)"/></g>')
    flags = "".join(f'<path d="M{x},676 l30,0 l-15,40z" fill="{c}"/>' for x, c in zip(range(470, 1080, 52), ["#ff5a4e", "#ffc51c", "#4a8fe0", "#47c46a", "#ff8fb3", "#ff8a3d"] * 3))
    bunting = f'<g transform="translate(0,150)"><path d="M455,672 Q760,700 1080,668" stroke="#a8693a" stroke-width="4" fill="none"/>{flags}</g>'
    car = ('<g transform="translate(1010,1520)"><rect x="-60" y="-44" width="120" height="34" rx="14" fill="#ff5a4e"/><path d="M-34,-44 q8,-26 34,-26 q22,0 30,26z" fill="#ff8a7e"/>'
           '<rect x="-20" y="-64" width="30" height="18" rx="5" fill="#bfe3ff"/><circle cx="-34" cy="-8" r="13" fill="#3a2a55"/><circle cx="34" cy="-8" r="13" fill="#3a2a55"/></g>')
    rug = ('<g id="rug"><ellipse cx="560" cy="1838" rx="520" ry="86" fill="#3fa79b"/><ellipse cx="560" cy="1834" rx="490" ry="74" fill="#5fc4b8"/>'
           '<ellipse cx="560" cy="1834" rx="400" ry="56" fill="none" stroke="#9fe3da" stroke-width="8" stroke-dasharray="20 14"/></g>')
    return (f'<rect width="1080" height="1500" fill="url(#gWall)"/>'
            '<g opacity=".18">' + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="#ff9f6b"/>' for x in range(40, 1080, 110) for y in range(120, 1480, 110)) + '</g>'
            f'{win}{bunting}'
            '<rect x="0" y="1488" width="1080" height="22" fill="#f3c9a0"/>'
            f'<rect x="0" y="1508" width="1080" height="412" fill="url(#gFloor)"/>{planks}{seams}{car}{rug}')
def lamp():
    return ('<g transform="translate(0,150)"><circle id="lampglow" cx="560" cy="1000" r="170" fill="url(#gLamp)"/>'
            '<rect x="553" y="880" width="14" height="70" fill="#a8693a"/><path d="M510,880 L610,880 L585,820 L535,820Z" fill="#ffd36a"/>'
            '<ellipse id="bulb" cx="560" cy="884" rx="30" ry="9" fill="#fffbe0"/><path d="M518,872 L602,872" stroke="#ffe9a8" stroke-width="5"/></g>'
            '<g id="lstring"><path d="M600,1030 Q628,1060 640,1098" stroke="#8a5a30" stroke-width="4" fill="none"/><g id="bead"><circle cx="640" cy="1104" r="10" fill="#ff8a3d"/><circle cx="637" cy="1100" r="3" fill="#fff"/></g></g>')
def shadow():
    return (f'<g id="shadow" transform="translate({SHC[0]},{SHC[1]}) scale(.7)"><g id="shadowi" fill="#0d1033">'
            '<ellipse cx="0" cy="70" rx="120" ry="110"/><ellipse cx="0" cy="-80" rx="104" ry="92"/>'
            '<ellipse cx="-48" cy="-250" rx="34" ry="120" transform="rotate(-12 -48 -250)"/>'
            '<g id="shEarR"><ellipse cx="58" cy="-240" rx="34" ry="112" transform="rotate(18 58 -240)"/><ellipse cx="112" cy="-336" rx="30" ry="44" transform="rotate(60 112 -336)"/></g>'
            '<ellipse cx="-110" cy="40" rx="30" ry="46"/><ellipse cx="110" cy="40" rx="30" ry="46"/></g></g>')
def shelf():
    star = "M0,-46 L13,-16 L45,-14 L20,6 L28,38 L0,20 L-28,38 L-20,6 L-45,-14 L-13,-16Z"
    return ('<g><rect x="600" y="1212" width="380" height="22" rx="8" fill="url(#gWood)"/><path d="M630,1234 l18,34 M950,1234 l-18,34" stroke="#a8693a" stroke-width="10" stroke-linecap="round"/>'
            f'<g transform="translate(895,1162)"><rect x="-26" y="34" width="52" height="16" rx="6" fill="#7b5cd6"/><g id="nlstar"><path d="{star}" fill="url(#gStar)" stroke="#f0a000" stroke-width="3"/>'
            '<circle cx="-8" cy="-10" r="4" fill="#3a2a55"/><circle cx="8" cy="-10" r="4" fill="#3a2a55"/><path d="M-9,4 q9,8 18,0" stroke="#3a2a55" stroke-width="3" fill="none" stroke-linecap="round"/></g></g></g>')
def box():
    x, y = BOX
    return (f'<g transform="translate({x},{y})" filter="url(#f3d)"><rect x="-125" y="-176" width="250" height="176" rx="22" fill="#2f8f86"/>'
            '<rect x="-118" y="-168" width="236" height="160" rx="18" fill="url(#gBox)"/><rect x="-132" y="-190" width="264" height="34" rx="14" fill="#ff8a3d"/>'
            '<path d="M0,-118 L10,-96 L34,-94 L16,-78 L22,-54 L0,-67 L-22,-54 L-16,-78 L-34,-94 L-10,-96Z" fill="#ffd23f"/>'
            '<ellipse cx="-60" cy="-150" rx="40" ry="8" fill="#ffffff" opacity=".4"/></g>')
def teddy():
    return (f'<g transform="translate({TED[0]},{TED[1]}) scale(.72)"><g id="tedi" filter="url(#f3d)">'
            '<ellipse cx="-44" cy="10" rx="16" ry="26" fill="url(#gTed)" transform="rotate(30 -44 10)"/><ellipse cx="44" cy="10" rx="16" ry="26" fill="url(#gTed)" transform="rotate(-30 44 10)"/>'
            '<ellipse cx="0" cy="24" rx="46" ry="50" fill="url(#gTed)"/><ellipse cx="0" cy="30" rx="26" ry="28" fill="url(#gTedIn)"/>'
            '<circle cx="-30" cy="-84" r="17" fill="url(#gTed)"/><circle cx="30" cy="-84" r="17" fill="url(#gTed)"/><circle cx="-30" cy="-84" r="8" fill="#f0c08c"/><circle cx="30" cy="-84" r="8" fill="#f0c08c"/>'
            '<circle cx="0" cy="-50" r="42" fill="url(#gTed)"/><ellipse cx="0" cy="-36" rx="19" ry="14" fill="url(#gTedIn)"/><ellipse cx="0" cy="-42" rx="7" ry="5" fill="#4a2a14"/>'
            '<circle cx="-15" cy="-58" r="5" fill="#2a1a10"/><circle cx="15" cy="-58" r="5" fill="#2a1a10"/><circle cx="-13" cy="-60" r="1.8" fill="#fff"/><circle cx="17" cy="-60" r="1.8" fill="#fff"/>'
            '<path d="M-6,-32 q6,6 12,0" stroke="#4a2a14" stroke-width="3" fill="none" stroke-linecap="round"/>'
            '<path d="M0,-8 l-20,-10 l0,20z M0,-8 l20,-10 l0,20z" fill="#4a8fe0"/><circle cx="0" cy="-8" r="6" fill="#2a62b8"/></g></g>')
def cone():
    import math as _m
    dx, dy = SHC[0] - HAND[0], SHC[1] - HAND[1]; L = _m.hypot(dx, dy); nx, ny = -dy / L, dx / L
    p = lambda x, y, w: f"{x + nx*w:.0f},{y + ny*w:.0f}"
    return (f'<g id="cone" style="mix-blend-mode:screen"><path d="M{p(*HAND, 14)} L{p(*SHC, 165)} L{p(*SHC, -165)} L{p(*HAND, -14)}Z" fill="url(#gBeam)" opacity=".55"/>'
            f'<circle cx="{SHC[0]}" cy="{SHC[1]}" r="175" fill="url(#gNL)"/></g>')

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(30))
    def badge(id_, x, y, n, col):
        return (f'<g transform="translate({x},{y})"><g class="cbadge" id="{id_}"><circle r="40" fill="#ffffff" stroke="{col}" stroke-width="8"/>'
                f'<text y="19" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="56" fill="{col}">{n}</text></g></g>')
    bdg = "".join(badge(f"bb{k}", 420 + 120 * k, 1330, k + 1, ["#d81b60", "#e65100", "#2e7d32"][k]) for k in range(3))
    speedv = ('<g id="speedv">' + "".join(f'<path d="M{BOX[0]-60+i*40},{1660+(i%2)*30} l0,110" stroke="#ffffff" stroke-width="9" stroke-linecap="round" opacity=".85"/>' for i in range(4)) + '</g>')
    hx, hy = HAT_WORLD
    stars = (f'<g id="stars"><g id="starsR">' + "".join(f'<path d="M0,-12 L4,-4 L12,-4 L6,2 L8,11 L0,6 L-8,11 L-6,2 L-12,-4 L-4,-4Z" fill="#ffd23f" stroke="#ff8a00" stroke-width="2" transform="translate({hx+70*math.cos(a):.0f},{hy-10+26*math.sin(a):.0f}) scale(1.6)"/>' for a in (0, 2.1, 4.2)) + '</g></g>')
    sockshape = SOCK_SHAPE
    sockf = f'<g transform="translate({MI[0]},{MI[1]}) scale(-{MS},{MS})"><g id="sockf">{sockshape}</g></g>'
    hearts = "".join(f'<path id="ht{k}" class="heart" d="M0,10 C-30,-14 -18,-40 0,-24 C18,-40 30,-14 0,10Z" fill="#ff5f8f" transform="translate({560 + 60*k},{1600 - 30*(k%2)})"/>' for k in range(3))
    mithu = f'<g id="pmithu" filter="url(#f3d)"><g transform="translate({MI[0]},{MI[1]}) scale(-{MS},{MS})"><g id="mlean">{MITHU}</g></g></g>'
    chars = (f'<g transform="translate({PARI[0]},{PARI[1]}) scale({KS})">{ka}</g><g transform="translate({CHINTU[0]},{CHINTU[1]}) scale({KS})">{kb}</g>'
             f'<g id="pgolu" transform="translate({GX},{GY}) scale({GS})"><g id="rgolu"><g id="gwrap" filter="url(#f3d)">{GOLU}</g></g></g>'
             f'<g clip-path="url(#clipBun)"><g id="pbunny" transform="translate({BUN_HIDE[0]},{BUN_HIDE[1]}) scale({BS})"><g id="rbunny"><g filter="url(#f3d)">{BUNNY}</g></g></g></g>')
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}<clipPath id="clipBun"><rect x="0" y="0" width="1080" height="1846"/></clipPath><clipPath id="clipWin"><rect x="78" y="738" width="294" height="344" rx="18"/></clipPath></defs>
<rect x="0" y="1500" width="1080" height="420" fill="#d99a5f"/>
<g id="shiftall" transform="translate(0,-200)">
{room()}
<rect id="darkA" x="0" y="0" width="1080" height="2200" fill="#141a48"/>
{shadow()}
{lamp()}
{shelf()}
{mithu}
{sockf}
{chars}
{box()}
{teddy()}
{speedv}
{stars}
<rect id="darkB" x="0" y="0" width="1080" height="2200" fill="#141a48"/>
<circle id="nlglow" cx="895" cy="1180" r="330" fill="url(#gNL)" style="mix-blend-mode:screen"/>
{cone()}
{hearts}
{bdg}
</g>
{conf}
</svg>'''
    css = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#ffefdc}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0}
#punch{position:absolute;inset:0;transform-origin:50% 55%}
#world{position:absolute;inset:0}
#ovl{position:absolute;inset:0}
.word{position:absolute;left:60px;width:860px;top:380px;text-align:center;line-height:1.08;white-space:nowrap}
.word .hi{font-size:118px;font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(20,20,60,.25)}
.word .en{font-size:78px;font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(20,20,60,.25)}
.moral{position:absolute;left:30px;width:900px;top:400px;display:flex;justify-content:center;gap:20px;opacity:0}
.mw{background:rgba(255,255,255,.92);border-radius:34px;padding:8px 24px;text-align:center;line-height:1.05;white-space:nowrap;box-shadow:0 8px 0 rgba(20,20,60,.2)}
.mw .hi{font-size:84px;font-weight:800}
.mw .en{font-size:50px;font-weight:800}
.badge{position:absolute;top:290px;left:150px;padding:12px 26px;border-radius:40px;background:rgba(255,255,255,.94);color:#e65100;font-size:38px;font-weight:800;box-shadow:0 6px 0 rgba(20,20,60,.2)}
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
