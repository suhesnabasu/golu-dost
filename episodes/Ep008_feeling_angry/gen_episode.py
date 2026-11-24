"""Golu & Dost Ep 8 — गोलू की कहानियाँ #2: गुस्सा आया | Feeling Angry (soft-3D glossy, Golu's playroom on a winter evening).
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
GOLU = GOLU.replace(CHEEKS, CHEEKS + ANGRY + FROWN)
F3D = tsrc[tsrc.index('<filter id="f3d"'):tsrc.index('</filter>') + len('</filter>')]
MITHU = open(f"{HERE}/mithu_src.txt").read()
HATW, HATH = 150, 92
MITHU = MITHU.replace('<g id="m-beak">', f'<g id="m-hat" opacity="0"><g transform="translate(18,-268) rotate(-8)"><rect x="{-HATW/2}" y="{-HATH/2}" width="{HATW}" height="{HATH}" rx="20" fill="#e2691f"/><rect x="{-HATW/2+6}" y="{-HATH/2+5}" width="{HATW-12}" height="{HATH-12}" rx="16" fill="url(#gBk4)"/><circle r="22" fill="#ffffff" opacity=".35"/><ellipse cx="-34" cy="-24" rx="28" ry="9" fill="#ffffff" opacity=".5"/></g></g><g id="m-beak">', 1)
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
    rg("gSteam", [(0, "#ffffff"), (.7, "#f4f7ff"), (1, "#d8e2f5")], "40%", "35%", "70%"),
    rg("gSunW", [(0, "#fff6d0"), (.5, "#ffc36a"), (1, "#ff9a4a")], "45%", "40%", "60%"),
    rg("gLamp", [(0, "#fff4c8"), (.5, "#ffe08a55"), (1, "#ffe08a00")], "50%", "50%", "50%"),
    rg("gBall", [(0, "#ffffff"), (.35, "#ff7fb0"), (1, "#c83a78")], "35%", "30%", "75%"),
    rg("gPetal", [(0, "#ffe0ee"), (1, "#ff7fb0")], "40%", "30%", "75%"),
    rg("gFlame", [(0, "#fffbe0"), (.5, "#ffd23f"), (1, "#ff8a00")], "50%", "65%", "60%"),
    lg("gWall", [(0, "#ffefdc"), (.7, "#ffe0c4"), (1, "#ffd2ae")]),
    lg("gWin", [(0, "#8fb8ff"), (.45, "#ffb0c8"), (.75, "#ffb36b"), (1, "#ffd08a")]),
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
GX, GY, GS = 470, 1840, .62            # Golu feet + scale
KS = .46                               # kids scale
PARI, CHINTU = (80, 1850), (212, 1856)
BUN_IN, BUN_OUT, BS = (880, 1840), (1260, 1840), .5
MI = (820, 1212); MS = .42             # Mithu on the shelf (flipped, faces left)
BW, BH = 120, 76
TP = [(735, 1798 - 76 * k) for k in range(5)]                                 # tower slots
FALL = [(640, 1868, -14), (730, 1878, 10), (800, 1860, 22), (598, 1830, 30)]  # where blocks 0-3 land
HOLD0 = (604, 1640, 0)                 # frame-1 block on Golu's palm (right arm held out)
HOLDUP = (470, 1735, 0)                # hugs it to his tummy with both arms (never aimed at anyone)
HATW_WORLD = (MI[0] - 18 * MS, MI[1] - 268 * MS)

WORDS = [  # id, hindi, english, hi colour, en colour
    ("wLast", "आख़िरी ब्लॉक!", "Last block!", "#d8621a", "#1565c0"),
    ("wCrash", "धड़ाम!", "CRASH!", "#d8322a", "#1565c0"),
    ("wAngry", "गुस्सा!", "Angry!", "#e53935", "#1565c0"),
    ("wSorry", "माफ़ करना!", "Sorry!", "#7b1fa2", "#1565c0"),
    ("wStop", "रुको! साँस लो!", "Stop! Breathe!", "#1e63d6", "#c2185b"),
    ("wFlower", "फूल सूँघो", "Smell the flower", "#d81b60", "#1565c0"),
    ("wCandle", "मोमबत्ती बुझाओ", "Blow the candle", "#e65100", "#1565c0"),
    ("wYou", "तुम भी!", "You too!", "#2e7d32", "#1565c0"),
    ("wFelt", "मुझे गुस्सा आया!", "I felt angry!", "#e53935", "#1565c0"),
    ("wOk", "गुस्सा ठीक है, फेंकना नहीं!", "Angry is OK. No throwing!", "#6a1fc2", "#c2185b"),
    ("wTog", "साथ में!", "Together!", "#2e7d32", "#1565c0"),
    ("wBye", "कल फिर मिलेंगे!", "See you tomorrow!", "#6a1fc2", "#1565c0"),
]
MORAL = [("mw0", "रुको", "Stop", "#1e63d6"), ("mw1", "साँस लो", "Breathe", "#d81b60"), ("mw2", "बोलो", "Say it", "#2e7d32")]
def overlays():
    w = ""
    for i, hi, en, hc, ec in WORDS:
        w += f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div><div class="en" style="color:{ec}">{en}</div></div>'
    w += '<div class="moral" id="wMoral">' + "".join(f'<div class="mw" id="{i}"><div class="hi" style="color:{c}">{hi}</div><div class="en" style="color:{c}">{en}</div></div>' for i, hi, en, c in MORAL) + '</div>'
    return w + '<div class="badge">गोलू की कहानियाँ #2 · Golu\'s Stories</div>'

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

def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set(".mw",{opacity:0,scale:.3}); gsap.set(".mw .en",{opacity:0}); gsap.set(".cbadge",{opacity:0}); gsap.set(".conf",{opacity:0}); gsap.set(".ico",{opacity:0}); gsap.set("#stars",{opacity:0}); gsap.set("#speed",{opacity:0}); gsap.set(".puff",{opacity:0});')
    tl('gsap.set("#g-trunk",{svgOrigin:"0 -352",rotation:-30}); gsap.set("#g-ear",{svgOrigin:"-90 -380"}); gsap.set("#g-ear2",{svgOrigin:"90 -380"});')
    tl('gsap.set("#kA-armL",{svgOrigin:"-62 -230"}); gsap.set("#kA-armR",{svgOrigin:"62 -230"}); gsap.set("#kB-armL",{svgOrigin:"-60 -232"}); gsap.set("#kB-armR",{svgOrigin:"60 -232"});')
    tl('gsap.set("#g-armR",{rotation:-90,svgOrigin:"128 -226"}); gsap.set(".pup",{x:10,y:-12});')
    tl(f'gsap.set("#cam",{{transformOrigin:"540px 1360px"}});')
    nb = int(DUR / BEAT)
    # idle life (offset, never in unison)
    tl(f'tl.to("#g-body",{{scaleY:.955,scaleX:1.022,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-head",{{y:9,rotation:2,svgOrigin:"0 -240",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#kA",{{y:-8,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.1);')
    tl(f'tl.to("#kB",{{y:-7,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.33);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.2);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.45);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#b-head",{{rotation:3,svgOrigin:"0 -150",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.15);')
    tl(f'tl.to("#lampglow",{{opacity:.75,duration:1.5,yoyo:true,repeat:{int(DUR/1.5)-1},ease:"sine.inOut"}},0);')
    tl(f'tl.fromTo("#sun",{{y:0}},{{y:26,duration:{DUR},ease:"none"}},0);')
    for k in range(int(DUR / 3)):
        t = 2.2 + k * 3.0
        if t > DUR - 1.5: break
        tl(f'tl.to("#g-ear",{{rotation:-8,duration:.15,yoyo:true,repeat:1}},{t:.2f}); tl.to("#g-ear2",{{rotation:8,duration:.15,yoyo:true,repeat:1}},{t+.12:.2f});')

    # ===== HOOK (frame 1 = Golu lifting the last block, card already on)
    for k in range(4): bset(k, *TP[k])
    bset(4, *HOLD0)
    tl('tl.set("#wLast",{opacity:1,scale:.85},0); tl.to("#wLast",{scale:1,duration:.3,ease:"back.out(3)"},0.02);')
    barc(4, 0.0, (735, 1420, -4, 1), (TP[4][0], TP[4][1], 0, 1), .32, .26)
    bsquash(4, T["place"], .12); golu_arm("R", 0, .45, d=.35); look(14, .2, -16)
    tl(f'tl.fromTo("#cam",{{scale:1}},{{scale:1.04,duration:{T["bin"]},ease:"power1.inOut",immediateRender:false}},0);')
    happy(T["place"] + .05, T["bin"] + .2); trunk(-60, T["place"], .2); trunk(-30, T["place"] + .6, .4, "power2.inOut")
    # Bunny zooms in from the right, asks "मेरी बारी?", skids on the rug
    bunpos(*BUN_OUT); bunmove(T["bin"], BUN_IN[0] - 40, BUN_IN[1], .35, "power3.out")
    tl(f'tl.set("#speed",{{opacity:1}},{f(T["bin"])}); tl.to("#speed",{{opacity:0,duration:.25}},{f(T["bin"]+.3)});')
    tl(f'tl.fromTo("#rbunny",{{rotation:0}},{{rotation:14,svgOrigin:"0 0",duration:.18,ease:"power2.out",immediateRender:false}},{f(T["skid"]-.1)}); tl.to("#rbunny",{{rotation:0,svgOrigin:"0 0",duration:.4,ease:"back.out(3)"}},{f(T["skid"]+.35)});')
    bunmove(T["skid"], BUN_IN[0], BUN_IN[1], .3, "power2.out")
    tl(f'tl.fromTo("#rug",{{scaleX:1}},{{scaleX:1.035,svgOrigin:"760 1830",duration:.12,yoyo:true,repeat:3,ease:"sine.inOut",immediateRender:false}},{f(T["skid"])});')
    look(16, T["bin"], -2); tl(f'tl.to("#b-eyes .bpup, .bpup",{{x:-6,duration:.2}},{f(T["skid"])});')
    # tower wobble -> CRASH
    c = T["crash"]
    for k in range(5):
        tl(f'tl.to("#bki{k}",{{rotation:{(-1)**k * (3 + k)},svgOrigin:"0 {BH/2}",duration:.12,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(T["skid"]+.2)});')
    word_out("wLast", c - .2); card("wCrash", c, T["take"] + .4)
    for k in range(4):
        x, y, r = FALL[k]; d = .42 + .05 * (3 - k)
        bmove(k, c + .06 * (3 - k), x, y, r, d=d, ease="power2.in"); bsquash(k, c + .06 * (3 - k) + d, .2)
    barc(4, c, (900, 980, 120, 1), (HATW_WORLD[0], HATW_WORLD[1], 352, .5), .4, .35)
    tl(f'tl.set("#bk4",{{opacity:0}},{f(T["hat"])}); tl.set("#m-hat",{{opacity:1}},{f(T["hat"])});')
    tl(f'tl.fromTo("#m-all",{{scaleY:1}},{{scaleY:.86,svgOrigin:"0 0",duration:.09,yoyo:true,repeat:1,immediateRender:false}},{f(T["hat"])});')
    tl(f'tl.set("#stars",{{opacity:1}},{f(T["hat"])}); tl.fromTo("#starsR",{{rotation:0}},{{rotation:200,svgOrigin:"{HATW_WORLD[0]:.0f} {HATW_WORLD[1]-10:.0f}",duration:1.0,ease:"none",immediateRender:false}},{f(T["hat"])}); tl.set("#stars",{{opacity:0}},{f(T["hat"]+1.0)});')
    cam(c, 1.12, -60, 40, .25, "power2.out"); cam(T["take"] - .3, 1.0, 0, 0, .3)
    mithu_talk(CUE["a3"], D["a3"]); look(18, c + .1, -18); look(22, T["hat"], -24)
    tl(f'tl.to(".mpup",{{y:-4,duration:.2}},{f(T["hat"]+.1)});')
    # ===== ANGER take: shock -> squash -> angry face + steam + stomp (close on Golu)
    tk = T["take"]
    look(0, tk, -14); tl(f'tl.to("#g-ear",{{rotation:-16,duration:.15,ease:"back.out(3)"}},{f(tk)}); tl.to("#g-ear2",{{rotation:16,duration:.17,ease:"back.out(3)"}},{f(tk+.04)});')
    cam(tk, 1.2, 40, -40, .45)
    g_squash(T["stomp"], .14); g_hop(T["stomp"] - .35, 18)
    tl(f'tl.to("#g-angry",{{opacity:1,duration:.35}},{f(T["angry"])}); tl.set("#g-brows",{{opacity:0}},{f(T["angry"])});')
    look(0, T["angry"], 4); trunk(-6, T["angry"], .25)
    tl(f'tl.to("#g-ear",{{rotation:0,duration:.3}},{f(T["angry"]+.4)}); tl.to("#g-ear2",{{rotation:0,duration:.3}},{f(T["angry"]+.45)});')
    for j, (pid, dx) in enumerate((("puffL", 0), ("puffR", .18))):
        t0 = T["angry"] + .1 + dx; n = int((T["out3"] - t0) / .9)
        tl(f'tl.fromTo("#{pid}",{{opacity:0,y:20,scale:.5}},{{opacity:.95,y:0,scale:1,transformOrigin:"50% 50%",duration:.3,ease:"back.out(2)",immediateRender:false}},{f(t0)});')
        tl(f'tl.to("#{pid} .pf",{{y:-26,duration:.45,yoyo:true,repeat:{max(1,2*n-1)},ease:"sine.inOut"}},{f(t0+.3)});')
    cam(END("b1") + .1, 1.0, 0, 0, .4)
    mithu_talk(CUE["b2"], D["b2"]); card("wAngry", CUE["b2"], END("b3") + .15)
    kids_talk(CUE["b3"], D["b3"]); kid_arm("A", -55, CUE["b3"], D["b3"]); kid_arm("B", -55, CUE["b3"] + .05, D["b3"])
    # holds a block UP (not aimed at anyone), Bunny says sorry -> kids: stop! -> freeze -> lowers it
    lf = T["lift"]; golu_arm("R", 38, lf, d=.3); golu_arm("L", -38, lf + .04, d=.3); bmove(3, lf, HOLDUP[0], HOLDUP[1] - 40, 0, d=.3, ease="power2.out"); bmove(3, lf + .3, *HOLDUP, d=.2, ease="power2.in")
    tl(f'tl.fromTo("#bki3",{{y:0}},{{y:-14,duration:.12,yoyo:true,repeat:5,ease:"sine.inOut",immediateRender:false}},{f(lf+.6)});')
    look(-6, lf, -16)
    bunny_sad(CUE["c1"] - .15, T["forgive"] + .4); card("wSorry", CUE["c1"], END("c1") + .1)
    tl(f'tl.to("#rbunny",{{y:10,duration:.3,ease:"power2.out"}},{f(CUE["c1"]-.1)}); tl.to("#rbunny",{{y:0,duration:.3}},{f(T["forgive"]+.4)});')
    card("wStop", CUE["c2"], END("c3") + .25)
    kids_talk(CUE["c2"], D["c2"]); kids_talk(CUE["c3"], D["c3"])
    kid_arm("A", -120, CUE["c2"], D["c2"] + D["c3"] + .3, wig=False); kid_arm("B", -120, CUE["c2"] + .06, D["c2"] + D["c3"] + .3, wig=False)
    fz = T["freeze"]; look(-16, fz, -6)
    tl(f'tl.fromTo("#rgolu",{{x:0}},{{x:-6,duration:.05,yoyo:true,repeat:3,immediateRender:false}},{f(fz)});')
    lw = T["lower"]; golu_arm("R", 0, lw, d=.4); golu_arm("L", 0, lw + .05, d=.4); bmove(3, lw, *FALL[3], d=.45, ease="power2.inOut")
    # ===== BREATHING x3: in = swell + trunk up + flower; out = trunk forward + candle goes out; red fades a step
    steps = [(T["in1"], T["out1"], END("d2"), .66), (T["in2"], T["out2"], END("d3"), .33), (T["in3"], T["out3"], T["out3"] + 1.0, 0)]
    for k, (ti, to_, te, lvl) in enumerate(steps):
        tl(f'tl.to("#gwrap",{{scaleX:1.035,scaleY:1.06,svgOrigin:"0 0",duration:{max(.6,to_-ti-.15):.2f},ease:"sine.inOut"}},{f(ti)});')
        tl(f'tl.to("#gwrap",{{scaleX:1,scaleY:1,svgOrigin:"0 0",duration:.8,ease:"sine.inOut"}},{f(to_)});')
        trunk(-95, ti, .6, "sine.inOut"); trunk(-20, to_, .5, "power2.out"); trunk(-30, to_ + .7, .4, "power2.inOut")
        look(0, ti, -26); look(0, to_, -10)
        tl(f'tl.fromTo("#icoF",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.3,ease:"back.out(2)",immediateRender:false}},{f(ti)}); tl.to("#icoF",{{opacity:0,duration:.2}},{f(to_-.05)});')
        tl(f'tl.fromTo("#icoC",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.3,ease:"back.out(2)",immediateRender:false}},{f(to_)}); tl.to("#icoC",{{opacity:0,duration:.2}},{f(te-.1)});')
        tl(f'tl.set("#flame",{{opacity:1,y:0}},{f(to_)}); tl.fromTo("#flame",{{x:0,opacity:1}},{{x:7,duration:.1,yoyo:true,repeat:3,immediateRender:false}},{f(to_+.15)}); tl.to("#flame",{{opacity:0,y:-12,duration:.2}},{f(to_+.45)}); tl.set("#flame",{{y:0}},{f(to_+.85)});')
        tl(f'tl.fromTo("#smoke",{{opacity:0,y:0}},{{opacity:.8,y:-40,duration:.6,immediateRender:false}},{f(to_+.8)}); tl.to("#smoke",{{opacity:0,duration:.2}},{f(to_+1.45)});')
        tl(f'tl.to("#g-angry",{{opacity:{lvl},duration:.6}},{f(to_+.2)});')
        tl(f'tl.to("#steam .pf",{{scale:{max(lvl,0.01)},transformOrigin:"50% 80%",opacity:{1 if lvl else 0},duration:.6}},{f(to_+.2)});')
        tl(f'tl.fromTo("#bb{k}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,transformOrigin:"50% 50%",duration:.25,ease:"back.out(2)",immediateRender:false}},{f(to_+.4)});')
        for kk, dl in (("A", 0), ("B", .1)):   # the kids breathe along
            tl(f'tl.to("#kid{kk}",{{scaleY:1.04,svgOrigin:"0 0",duration:.6,ease:"sine.inOut"}},{f(ti+dl)}); tl.to("#kid{kk}",{{scaleY:1,svgOrigin:"0 0",duration:.6,ease:"sine.inOut"}},{f(to_+dl)});')
        cam(ti, 1.05, 0, -20, .9, "sine.inOut"); cam(to_, 1.0, 0, 0, .9, "sine.inOut")
    card("wFlower", T["in1"], T["out1"]); card("wCandle", T["out1"], END("d2") + .2, False)
    card("wFlower", T["in2"], T["out2"], False); card("wCandle", T["out2"], END("d3") + .1, False)
    kids_talk(CUE["d3"], D["d3"])
    card("wYou", CUE["d4"], T["in3"] - .05); mithu_talk(CUE["d4"], D["d4"])
    tl(f'tl.to(".mpup",{{x:-6,y:4,duration:.2}},{f(CUE["d4"])});')
    tl(f'tl.fromTo("#g-trunk",{{scaleY:1}},{{scaleY:1.12,svgOrigin:"0 -352",duration:.08,yoyo:true,repeat:3,immediateRender:false}},{f(T["out3"]+1.15)});')   # tiny toot
    calm = T["calm"]
    tl(f'tl.set("#g-brows",{{opacity:1}},{f(T["out3"]+.4)}); tl.set("#g-frown",{{opacity:0}},{f(T["out3"]+.4)}); tl.set("#g-smile",{{opacity:1}},{f(T["out3"]+.4)});')
    tl(f'tl.to(".cbadge",{{opacity:0,duration:.25}},{f(calm+.2)});')
    happy(calm - .05, calm + .7); g_hop(calm, 16)
    # ===== WORDS: "मुझे गुस्सा आया!" (hand on chest), "गुस्सा आना ठीक है… फेंकना नहीं!"
    card("wFelt", T["felt"], T["ok"] - .05); golu_arm("L", 40, T["felt"], D["e1"])
    cam(T["felt"], 1.05, 10, 50, .5)
    card("wOk", T["ok"], END("e2c") + .15); cam(T["ok"], 1.0, 0, 0, .5)
    no = CUE["e2b"] + D["e2b"] * .62
    tl(f'tl.to("#g-head",{{x:12,duration:.12,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(no)});')
    kids_talk(CUE["e2c"], D["e2c"]); kids_cheer(CUE["e2c"] + .2, .9)
    # forgive -> Bunny perks up -> together
    look(18, T["forgive"], -4); golu_arm("R", -60, T["forgive"] + .1, 1.0)
    tl(f'tl.set("#b-eyes",{{opacity:0}},{f(T["tog"])}); tl.set("#b-happy",{{opacity:1}},{f(T["tog"])}); tl.set("#b-eyes",{{opacity:1}},{f(T["tog"]+.9)}); tl.set("#b-happy",{{opacity:0}},{f(T["tog"]+.9)});')
    b_hop(T["tog"] + .1, 46); bunny_cheer(T["tog"] + .1, .7)
    card("wTog", CUE["e4"], T["moral"])
    # ===== REBUILD: blocks fly back on the beat; Bunny's block in slow motion; Golu happy
    RB = T["RB"]
    for k in (0, 1, 3):
        barc(k, RB[k], (TP[k][0] - 40, TP[k][1] - 140, 0, 1), (TP[k][0], TP[k][1], 0, 1), .22, .23); bsquash(k, RB[k] + .45, .12)
        tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.03,duration:.12,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(RB[k]+.45)});')
        g_hop(RB[k] + .45, 14)
    b0 = RB[2]   # Bunny pushes block 2 along the rug to the tower in exaggerated slow motion, then it hops up
    bunmove(b0, FALL[2][0] + 78, 1840, .25, "power2.out")
    bunmove(b0 + .25, TP[0][0] + 140, 1840, 1.0, "sine.inOut")
    bmove(2, b0 + .25, TP[0][0] + 62 + 0, 1858, 0, d=1.0, ease="sine.inOut")
    tl(f'tl.to("#b-armL",{{rotation:60,svgOrigin:"-60 -148",duration:.25}},{f(b0)}); tl.to("#b-armR",{{rotation:-60,svgOrigin:"60 -148",duration:.25}},{f(b0+.05)});')
    tl(f'tl.to("#rbunny",{{rotation:-10,svgOrigin:"0 0",duration:.25}},{f(b0)}); tl.to("#rbunny",{{rotation:0,svgOrigin:"0 0",duration:.3}},{f(b0+1.3)});')
    tl(f'tl.to("#b-armL",{{rotation:0,svgOrigin:"-60 -148",duration:.3}},{f(b0+1.3)}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -148",duration:.3}},{f(b0+1.35)});')
    barc(2, b0 + 1.25, (TP[2][0] + 40, TP[2][1] - 110, 0, 1), (TP[2][0], TP[2][1], 0, 1), .14, .14)
    bsquash(2, b0 + 1.53, .12); bunmove(b0 + 1.6, BUN_IN[0], BUN_IN[1], .35)
    happy(RB[0] + .4, RB[3] + .8); look(16, RB[0], -14)
    # ===== MORAL (words pop one per beat), kids English, confetti
    tl(f'tl.set("#wMoral",{{opacity:1}},{f(T["moral"])});')
    tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.04,duration:.15,yoyo:true,repeat:1,immediateRender:false}},{f(T["moral"])});')
    for k, (i, *_r) in enumerate(MORAL):
        tk2 = T["m1"] + k * D["f1b"] / 3
        tl(f'tl.fromTo("#{i}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.3,ease:"back.out(2)",immediateRender:false}},{f(tk2)});')
        tl(f'tl.fromTo("#{i} .en",{{opacity:0}},{{opacity:1,duration:.2,immediateRender:false}},{f(T["f2"]+k*D["f2"]/3)});')
        tl(f'tl.fromTo("#{i} .en",{{scale:1}},{{scale:1.2,duration:.15,yoyo:true,repeat:1,immediateRender:false}},{f(T["f2"]+k*D["f2"]/3)});')
        golu_arm("L", 60 + 25 * k, tk2, .35)
    tl(f'tl.to(".mw",{{opacity:0,scale:.6,duration:.18}},{f(T["bye"]-.2)});')
    kids_talk(CUE["f2"], D["f2"]); kids_cheer(CUE["f2"], 1.2); bunny_cheer(CUE["f2"] + .1, 1.1)
    happy(CUE["f2"], END("f2") + .2); golu_arm("R", -110, CUE["f2"] + .06, 1.0)
    random.seed(8)
    for k in range(36):
        x0 = random.uniform(80, 1000); dly = random.uniform(0, .9); rot = random.uniform(-540, 540)
        tl(f'tl.fromTo("#cf{k}",{{x:{x0:.0f},y:700,rotation:0,opacity:1}},{{x:{x0 + random.uniform(-120,120):.0f},y:{random.uniform(1500,1900):.0f},rotation:{rot:.0f},duration:2.4,ease:"power1.in",immediateRender:false}},{f(CUE["f2"]+dly)}); tl.set("#cf{k}",{{opacity:0}},{f(CUE["f2"]+dly+2.4)});')
    # ===== BYE + LOOP
    by = T["bye"]
    word_in("wBye", by); word_out("wBye", DUR - .7); golu_arm("L", 100, by + .1, 1.4, wave=True); happy(by + .1, by + 1.2)
    mithu_talk(CUE["g2"], D["g2"]); kids_cheer(CUE["g2"], .8)
    lp = DUR - 1.0
    bunmove(lp, BUN_OUT[0], BUN_OUT[1], .3, "power3.in")
    tl(f'tl.set("#speed",{{opacity:1}},{f(lp+.05)}); tl.to("#speed",{{opacity:0,duration:.2}},{f(lp+.3)});')
    # the hat block hops off Mithu into Golu's raised hand = frame 1
    tl(f'tl.set("#m-hat",{{opacity:0}},{f(DUR-.75)}); tl.set("#bk4",{{opacity:1}},{f(DUR-.75)});')
    bset(4, HATW_WORLD[0], HATW_WORLD[1], 352, .5, t=DUR - .75)
    barc(4, DUR - .75, (800, 1380, 200, .8), HOLD0, .3, .38)
    tl(f'tl.set("#bk4",{{attr:{{transform:"{tfr(*HOLD0)}"}}}},{f(DUR-.05)});')
    golu_arm("R", -90, DUR - .55, d=.4); look(10, DUR - .5, -12)
    tl(f'tl.fromTo("#wLast",{{opacity:0,scale:.5}},{{opacity:1,scale:.85,duration:.3,ease:"power2.out",immediateRender:false}},{DUR-.35:.2f});')
    # ===== blinks (offset)
    t = 2.6
    while t < DUR - 1:
        tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t:.2f});')
        tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.1:.2f});')
        tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+.6:.2f});')
        tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.9:.2f});')
        tl(f'tl.to(".bpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.5:.2f});')
        t += 3.3
    # ===== lip-sync: toggle pre-drawn mouths, scale with svgOrigin (never CSS transform-origin)
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
    a0, a1 = T["angry"], T["out3"] + .4
    lipsync(lips["golu"], "#g-mouth", lambda t: "#g-frown" if a0 <= t < a1 else "#g-smile", "#g-smile, #g-frown", "-62 -314", [0, .5, .8, 1.1])
    s0, s1 = CUE["c1"] - .15, T["forgive"] + .4
    lipsync(lips["bunny"], "#b-mouth", lambda t: "#b-sad" if s0 <= t < s1 else "#b-smile", "#b-smile, #b-sad", "0 -204", [0, .55, .8, 1.05])

# ---------------- set: Golu's playroom, winter evening ----------------
def block(k):
    a, b, c = BK[k]
    emb = ('<circle r="17" fill="#ffffff" opacity=".35"/>' if k % 2 == 0 else
           '<path d="M0,-18 L5,-6 L18,-6 L8,2 L12,15 L0,7 L-12,15 L-8,2 L-18,-6 L-5,-6Z" fill="#ffffff" opacity=".4"/>')
    return (f'<rect x="{-BW/2}" y="{-BH/2}" width="{BW}" height="{BH}" rx="16" fill="{c}"/>'
            f'<rect x="{-BW/2+5}" y="{-BH/2+4}" width="{BW-10}" height="{BH-10}" rx="13" fill="url(#gBk{k})"/>'
            f'{emb}<ellipse cx="-28" cy="-22" rx="24" ry="7" fill="#ffffff" opacity=".55"/>')
def room():
    planks = "".join(f'<rect x="0" y="{y}" width="1080" height="4" fill="#c88a52" opacity=".45"/>' for y in range(1560, 1920, 70))
    seams = "".join(f'<rect x="{(i*263 + (y//70)*131) % 1080}" y="{y}" width="4" height="70" fill="#c88a52" opacity=".4"/>' for y in range(1500, 1920, 70) for i in range(4))
    win = ('<g transform="translate(0,150)"><rect x="60" y="720" width="330" height="380" rx="28" fill="url(#gWood)"/><rect x="78" y="738" width="294" height="344" rx="18" fill="url(#gWin)"/>'
           '<g clip-path="url(#clipWin)"><g id="sun"><circle cx="268" cy="1000" r="54" fill="url(#gSunW)"/><circle cx="268" cy="1000" r="84" fill="#ffd08a" opacity=".35"/></g>'
           '<g filter="url(#fblur)"><path d="M78,1060 L120,1010 L170,1040 L170,1082 L78,1082Z" fill="#b0708a" opacity=".7"/><path d="M200,1082 L200,1030 L250,990 L300,1030 L300,1082Z" fill="#a06a86" opacity=".7"/>'
           '<rect x="300" y="1040" width="80" height="42" fill="#b57a8f" opacity=".7"/></g>'
           '<circle cx="140" cy="800" r="4" fill="#ffffff" opacity=".9"/><circle cx="320" cy="780" r="3" fill="#ffffff" opacity=".8"/></g>'
           '<rect x="219" y="738" width="12" height="344" fill="url(#gWood)"/><rect x="78" y="902" width="294" height="12" fill="url(#gWood)"/>'
           '<path d="M52,712 Q130,820 100,1110 L44,1110 Z" fill="url(#gCurt)"/><path d="M398,712 Q320,820 350,1110 L406,1110 Z" fill="url(#gCurt)"/>'
           '<rect x="36" y="696" width="378" height="24" rx="12" fill="#7b5cd6"/><rect x="50" y="1098" width="350" height="22" rx="11" fill="url(#gWood)"/></g>')
    flags = "".join(f'<path d="M{x},676 l30,0 l-15,40z" fill="{c}"/>' for x, c in zip(range(470, 1080, 52), ["#ff5a4e", "#ffc51c", "#4a8fe0", "#47c46a", "#ff8fb3", "#ff8a3d"] * 3))
    bunting = f'<g transform="translate(0,150)"><path d="M455,672 Q760,700 1080,668" stroke="#a8693a" stroke-width="4" fill="none"/>{flags}</g>'
    lamp = ('<g transform="translate(0,150)"><circle id="lampglow" cx="560" cy="1000" r="150" fill="url(#gLamp)" opacity=".55"/>'
            '<rect x="553" y="880" width="14" height="70" fill="#a8693a"/><path d="M510,880 L610,880 L585,820 L535,820Z" fill="#ffd36a"/><path d="M518,872 L602,872" stroke="#ffe9a8" stroke-width="5"/></g>')
    shelf = ('<g><rect x="640" y="1212" width="300" height="22" rx="8" fill="url(#gWood)"/><path d="M670,1234 l18,34 M910,1234 l-18,34" stroke="#a8693a" stroke-width="10" stroke-linecap="round"/>'
             '<g transform="translate(700,1212)"><circle cy="-32" r="32" fill="url(#gBall)"/><path d="M-30,-40 q30,14 60,0" stroke="#ffffff" stroke-width="5" fill="none" opacity=".7"/></g>'
             '<g transform="translate(895,1212)"><rect x="-30" y="-46" width="60" height="46" rx="10" fill="#4a8fe0"/><ellipse cy="-46" rx="30" ry="9" fill="#e8f1ff"/><path d="M-30,-36 l60,26 M30,-36 l-60,26" stroke="#ffd23f" stroke-width="4"/></g></g>')
    car = ('<g transform="translate(990,1500)"><rect x="-60" y="-44" width="120" height="34" rx="14" fill="#ff5a4e"/><path d="M-34,-44 q8,-26 34,-26 q22,0 30,26z" fill="#ff8a7e"/>'
           '<rect x="-20" y="-64" width="30" height="18" rx="5" fill="#bfe3ff"/><circle cx="-34" cy="-8" r="13" fill="#3a2a55"/><circle cx="34" cy="-8" r="13" fill="#3a2a55"/></g>')
    rug = ('<g id="rug"><ellipse cx="560" cy="1838" rx="520" ry="86" fill="#3fa79b"/><ellipse cx="560" cy="1834" rx="490" ry="74" fill="#5fc4b8"/>'
           '<ellipse cx="560" cy="1834" rx="400" ry="56" fill="none" stroke="#9fe3da" stroke-width="8" stroke-dasharray="20 14"/></g>')
    return (f'<rect width="1080" height="1500" fill="url(#gWall)"/>'
            '<g opacity=".18">' + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="#ff9f6b"/>' for x in range(40, 1080, 110) for y in range(120, 1480, 110)) + '</g>'
            f'{win}{bunting}{lamp}{shelf}'
            '<rect x="0" y="1488" width="1080" height="22" fill="#f3c9a0"/>'
            f'<rect x="0" y="1508" width="1080" height="412" fill="url(#gFloor)"/>{planks}{seams}{car}{rug}')

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(36))
    def puff(id_, x, y):
        return (f'<g transform="translate({x:.0f},{y:.0f})"><g id="{id_}" class="puff"><g class="pf"><circle cx="0" cy="0" r="22" fill="url(#gSteam)"/><circle cx="20" cy="-14" r="17" fill="url(#gSteam)"/>'
                f'<circle cx="-18" cy="-12" r="15" fill="url(#gSteam)"/><circle cx="4" cy="-30" r="13" fill="url(#gSteam)"/></g></g></g>')
    steam = f'<g id="steam">{puff("puffL", GX - GS * 150, GY - GS * 560)}{puff("puffR", GX + GS * 150, GY - GS * 560)}</g>'
    petals = "".join(f'<ellipse cx="540" cy="{800-34}" rx="22" ry="34" fill="url(#gPetal)" transform="rotate({a} 540 800)"/>' for a in range(0, 360, 72))
    icoF = (f'<g id="icoF" class="ico"><circle cx="540" cy="800" r="118" fill="#ffffff" opacity=".88"/>'
            f'<path d="M540,840 q-6,50 10,80" stroke="#47c46a" stroke-width="10" fill="none" stroke-linecap="round"/><ellipse cx="572" cy="880" rx="22" ry="11" fill="#47c46a" transform="rotate(-30 572 880)"/>'
            f'{petals}<circle cx="540" cy="800" r="20" fill="#ffd23f"/></g>')
    icoC = ('<g id="icoC" class="ico"><circle cx="540" cy="800" r="118" fill="#ffffff" opacity=".88"/>'
            '<rect x="512" y="770" width="56" height="120" rx="12" fill="url(#gCandle)" stroke="#e6c48a" stroke-width="3"/><path d="M540,770 L540,752" stroke="#5a3a2a" stroke-width="4"/>'
            '<g id="flame"><path d="M540,700 q24,30 12,50 q-12,12 -24,0 q-12,-20 12,-50z" fill="url(#gFlame)"/></g>'
            '<g id="smoke" opacity="0"><path d="M540,748 q-14,-18 0,-34 q14,-16 0,-32" stroke="#c9ced8" stroke-width="7" fill="none" stroke-linecap="round"/></g></g>')
    def badge(id_, x, y, n, col):
        return (f'<g transform="translate({x},{y})"><g class="cbadge" id="{id_}"><circle r="40" fill="#ffffff" stroke="{col}" stroke-width="8"/>'
                f'<text y="19" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="56" fill="{col}">{n}</text></g></g>')
    bdg = "".join(badge(f"bb{k}", 420 + 120 * k, 1000, k + 1, ["#d81b60", "#e65100", "#2e7d32"][k]) for k in range(3))
    speed = ('<g id="speed">' + "".join(f'<path d="M{1000+i*18},{1620+i*60} l140,0" stroke="#ffffff" stroke-width="10" stroke-linecap="round" opacity=".85"/>' for i in range(4)) + '</g>')
    hx, hy = HATW_WORLD
    stars = (f'<g id="stars"><g id="starsR">' + "".join(f'<path d="M0,-12 L4,-4 L12,-4 L6,2 L8,11 L0,6 L-8,11 L-6,2 L-12,-4 L-4,-4Z" fill="#ffd23f" stroke="#ff8a00" stroke-width="2" transform="translate({hx+70*math.cos(a):.0f},{hy-10+26*math.sin(a):.0f}) scale(1.6)"/>' for a in (0, 2.1, 4.2)) + '</g></g>')
    blocks = "".join(f'<g id="bk{k}"><g id="bki{k}" filter="url(#f3d)">{block(k)}</g></g>' for k in range(5))
    mithu = f'<g id="pmithu" filter="url(#f3d)"><g transform="translate({MI[0]},{MI[1]}) scale(-{MS},{MS})">{MITHU}</g></g>'
    chars = (f'<g transform="translate({PARI[0]},{PARI[1]}) scale({KS})">{ka}</g><g transform="translate({CHINTU[0]},{CHINTU[1]}) scale({KS})">{kb}</g>'
             f'<g id="pgolu" transform="translate({GX},{GY}) scale({GS})"><g id="rgolu"><g id="gwrap" filter="url(#f3d)">{GOLU}</g></g></g>'
             f'<g id="pbunny" transform="translate({BUN_OUT[0]},{BUN_OUT[1]}) scale({BS})"><g id="rbunny"><g filter="url(#f3d)">{BUNNY}</g></g></g>')
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}<clipPath id="clipWin"><rect x="78" y="738" width="294" height="344" rx="18"/></clipPath></defs>
<rect x="0" y="1500" width="1080" height="420" fill="#d99a5f"/>
<g id="shiftall" transform="translate(0,-200)">
{room()}
{mithu}
{chars}
{speed}
{steam}
{blocks}
{stars}
<g transform="translate(0,270)">{icoF}{icoC}</g>
<g transform="translate(0,330)">{bdg}</g>
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
.word .hi{font-size:118px;font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(90,40,0,.18)}
.word .en{font-size:78px;font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(90,40,0,.18)}
.moral{position:absolute;left:30px;width:900px;top:400px;display:flex;justify-content:center;gap:16px;opacity:0}
.mw{background:rgba(255,255,255,.9);border-radius:34px;padding:8px 22px;text-align:center;line-height:1.05;white-space:nowrap;box-shadow:0 8px 0 rgba(120,60,0,.15)}
.mw .hi{font-size:80px;font-weight:800}
.mw .en{font-size:48px;font-weight:800}
.badge{position:absolute;top:290px;left:150px;padding:12px 26px;border-radius:40px;background:rgba(255,255,255,.94);color:#e65100;font-size:38px;font-weight:800;box-shadow:0 6px 0 rgba(120,60,0,.15)}
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
