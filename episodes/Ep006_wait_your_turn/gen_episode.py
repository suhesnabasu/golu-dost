"""Golu & Dost Ep 6 — गोलू की कहानियाँ #1: बारी-बारी | Wait Your Turn (soft-3D glossy, park playground set).
usage: python3 gen_episode.py <project dir>   (needs timing.json next to this file and <proj>/assets/lips.json)"""
import json, math, sys, os, random
PROJ = sys.argv[1]; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json")); DUR = T["DUR"]; D = T["D"]; R = T["R"]
CUE = dict((k, v) for k, v in T["CUES"])
lips = json.load(open(f"{PROJ}/assets/lips.json"))

# ---- v2 cast from the series template (GOLU, KIDS, gradients, f3d), Mithu (Ep4/5) and v2 Bunny (Ep1 remake)
tsrc = open("/home/claude/golu_pipeline/gen_episode_template.py").read()
ns = {"math": math}
exec(tsrc[tsrc.index("COLS = ["):tsrc.index("def overlays():")], ns)
rg, GOLU, KIDS, cloud = ns["rg"], ns["GOLU"], ns["KIDS"], ns["cloud"]
F3D = tsrc[tsrc.index('<filter id="f3d"'):tsrc.index('</filter>') + len('</filter>')]
MITHU = open(f"{HERE}/cast/mithu_src.txt").read()
BUNNY = open(f"{HERE}/cast/bunny_v2.svg.txt").read()
def lg(id_, stops, y2=1):
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="{y2}">' + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops) + '</linearGradient>'
defs = ns["defs"] + F3D + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    rg("gBun", [(0, "#ffffff"), (.6, "#f1ecff"), (1, "#c7b8ef")], "38%", "30%", "75%"),
    rg("gBunIn", [(0, "#ffd3e2"), (1, "#f59ab9")], "45%", "40%", "70%"),
    rg("gCanopy", [(0, "#9cf26a"), (.6, "#3fbf3a"), (1, "#1f8a2e")], "40%", "30%", "75%"),
    rg("gSand", [(0, "#fff0c2"), (.6, "#f6d88f"), (1, "#e2b964")], "45%", "35%", "70%"),
    lg("gSky6", [(0, "#62c6ff"), (.65, "#a9e3ff"), (1, "#e4f6ff")]),
    lg("gGrass6", [(0, "#97e46c"), (1, "#4fb83a")]),
    lg("gChute", [(0, "#ff8a5c"), (.5, "#ff6b4a"), (1, "#d9442a")]),
    lg("gPlat", [(0, "#ffe36a"), (1, "#f2b81f")]),
    '<linearGradient id="gRail" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7fb2ff"/><stop offset=".5" stop-color="#3b82f6"/><stop offset="1" stop-color="#1f5fd0"/></linearGradient>',
    '<filter id="fblur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>',
    '<filter id="fblur2" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.6"/></filter>',
])

# ---- kids: split, remove fixed placement, add a sad mouth (.ksad)
ka, kb = KIDS[KIDS.index('<g id="kidA"'):KIDS.index('<g id="kidB"')], KIDS[KIDS.index('<g id="kidB"'):]
ka = ka.replace(' transform="translate(150,1880) scale(.78)"', '')
kb = kb.replace(' transform="translate(930,1880) scale(.78)"', '')
ka = ka.replace('<g class="kmouth"', '<path class="ksad" d="M-22,-286 q22,-18 44,0" stroke="#8a2a3c" stroke-width="7" fill="none" stroke-linecap="round" opacity="0"/><g class="kmouth"', 1)
kb = kb.replace('<g class="kmouth"', '<path class="ksad" d="M-24,-282 q24,-18 48,0" stroke="#6a2020" stroke-width="7" fill="none" stroke-linecap="round" opacity="0"/><g class="kmouth"', 1)
CH = {"golu": f'<g id="gwrap" filter="url(#f3d)">{GOLU}</g>', "pari": ka, "chintu": kb, "bunny": f'<g filter="url(#f3d)">{BUNNY}</g>'}
FG = {"golu": .56, "pari": .55, "chintu": .55, "bunny": .55}       # foreground scales
HALF = {"golu": 160, "pari": 81, "chintu": 81, "bunny": 70}         # half widths at FG scale (px)
MID = .70                                                            # mid-ground (slide) scale factor
ROW_Y = 1840; LEFT = 73; GAP = 50
SEAT = 26; FOOT = (210, 1305); TOP = (232, 896); CH_A = (330, 922); CH_B = (700, 1240); SAND = (850, 1300)

def pack(order):
    xs, x = [], LEFT
    for c in order:
        x += HALF[c]; xs.append(x); x += HALF[c] + GAP
    return dict(zip(order, xs))

# ---- on-screen words (Hindi big, English below)
WORDS = [  # id, hindi, english, hi colour, en colour
    ("wWait", "रुको, बनी!", "Wait, Bunny!", "#d81b60", "#1565c0"),
    ("wPlop", "धप्प!", "PLOP!", "#a65500", "#1565c0"),
    ("wMe", "मैं पहले!", "Me first!", "#7b1fa2", "#1565c0"),
    ("wSad", "अरे, सब उदास!", "Oh no, everyone is sad!", "#3949ab", "#c2185b"),
    ("wAlone", "अकेले मज़ा नहीं!", "It's no fun alone!", "#3949ab", "#c2185b"),
    ("wTurns", "बारी-बारी!", "Take turns!", "#c43e00", "#1565c0"),
    ("wCount", "एक, दो, तीन, चार", "1, 2, 3, 4", "#2e7d32", "#1565c0"),
    ("wPari", "परी की बारी!", "Pari's turn!", "#d81b60", "#1565c0"),
    ("wChintu", "चिंटू की बारी!", "Chintu's turn!", "#c43e00", "#1565c0"),
    ("wHard", "रुकना मुश्किल!", "Waiting is hard!", "#6a1fc2", "#c2185b"),
    ("wGood", "शाबाश, बनी!", "Well done, Bunny!", "#ff4f8b", "#e08a00"),
    ("wBunny", "बनी की बारी!", "Bunny's turn!", "#7b1fa2", "#1565c0"),
    ("wGolu", "गोलू की बारी!", "Golu's turn!", "#1e63d6", "#d81b60"),
    ("wPlop2", "धप्प!", "PLOP!", "#a65500", "#1565c0"),
    ("wMoral", "बारी-बारी, सबकी बारी!", "Wait your turn,<br>everyone gets a turn!", "#c43e00", "#1565c0"),
    ("wTog", "साथ में मज़ा!", "Together is fun!", "#d81b60", "#1565c0"),
    ("wBye", "कल फिर मिलेंगे!", "See you tomorrow!", "#6a1fc2", "#1565c0"),
]
def overlays():
    w = ""
    for i, hi, en, hc, ec in WORDS:
        w += f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div><div class="en" style="color:{ec}">{en}</div></div>'
    return w + '<div class="badge">गोलू की कहानियाँ #1 · Golu\'s Stories</div>'

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
def look(x, t): tl(f'tl.to(".pup",{{x:{x},duration:.2,ease:"power2.out"}},{f(t)});')
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
def bunny_cheer(t, hold=.8):
    tl(f'tl.to("#b-armL",{{rotation:120,svgOrigin:"-60 -148",duration:.18,ease:"back.out(2)"}},{f(t)}); tl.to("#b-armR",{{rotation:-120,svgOrigin:"60 -148",duration:.18,ease:"back.out(2)"}},{f(t+.06)});')
    tl(f'tl.to("#b-armL",{{rotation:0,svgOrigin:"-60 -148",duration:.3}},{f(t+hold)}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -148",duration:.3}},{f(t+hold+.06)});')
def golu_arm(side, rot, t, hold, wave=False):
    sel, o = ("#g-armR", "128 -226") if side == "R" else ("#g-armL", "-128 -226")
    tl(f'tl.to("{sel}",{{rotation:{rot},svgOrigin:"{o}",duration:.22,ease:"back.out(2)"}},{f(t)});')
    if wave: tl(f'tl.to("{sel}",{{rotation:{rot + (18 if rot < 0 else -18)},svgOrigin:"{o}",duration:.16,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(t+.22)});')
    tl(f'tl.to("{sel}",{{rotation:0,svgOrigin:"{o}",duration:.3,ease:"power2.inOut"}},{f(t+hold)});')
def sad(who, t0, t1):
    if who == "bunny":
        tl(f'tl.set("#b-smile",{{opacity:0}},{f(t0)}); tl.set("#b-sad",{{opacity:1}},{f(t0)}); tl.set("#b-smile",{{opacity:1}},{f(t1)}); tl.set("#b-sad",{{opacity:0}},{f(t1)});')
        tl(f'tl.to("#b-earL",{{rotation:-28,svgOrigin:"-40 -300",duration:.45,ease:"power2.out"}},{f(t0)}); tl.to("#b-earR",{{rotation:30,svgOrigin:"44 -300",duration:.5,ease:"power2.out"}},{f(t0+.08)});')
        tl(f'tl.to("#b-earL",{{rotation:0,svgOrigin:"-40 -300",duration:.35,ease:"back.out(2.5)"}},{f(t1)}); tl.to("#b-earR",{{rotation:0,svgOrigin:"44 -300",duration:.35,ease:"back.out(2.5)"}},{f(t1+.07)});')
    else:
        k = "#kidA" if who == "pari" else "#kidB"
        tl(f'tl.set("{k} .ksmile",{{opacity:0}},{f(t0)}); tl.set("{k} .ksad",{{opacity:1}},{f(t0)}); tl.set("{k} .ksmile",{{opacity:1}},{f(t1)}); tl.set("{k} .ksad",{{opacity:0}},{f(t1)});')
        h = "#kA-head" if who == "pari" else "#kB-head"
        tl(f'tl.to("{h}",{{y:14,duration:.35,ease:"power2.out"}},{f(t0)}); tl.to("{h}",{{y:0,duration:.3,ease:"back.out(2)"}},{f(t1)});')

# ---- position scheduler: wrapper #p<who> = feet position + scale; #r<who> = lean / bob
S = {}; MEND = {}
def tf(x, y, s): return f"translate({x:.2f},{y:.2f}) scale({s:.4f})"
def setpos(who, x, y, s):
    S[who] = (x, y, s); tl(f'gsap.set("#p{who}",{{attr:{{transform:"{tf(x, y, s)}"}}}});')
def move(who, t, x, y, s=None, d=.6, ease="power2.inOut", bob=0):
    x0, y0, s0 = S[who]; s = s0 if s is None else s
    tl(f'tl.fromTo("#p{who}",{{attr:{{transform:"{tf(x0, y0, s0)}"}}}},{{attr:{{transform:"{tf(x, y, s)}"}},duration:{d},ease:"{ease}",immediateRender:false}},{f(t)});')
    if bob:
        n = max(1, int(round(d / .3)))
        tl(f'tl.fromTo("#r{who}",{{y:0}},{{y:{-bob},duration:{d/(2*n):.3f},yoyo:true,repeat:{2*n-1},ease:"sine.out",immediateRender:false}},{f(t)});')
    S[who] = (x, y, s); MEND[who] = max(MEND.get(who, 0), t + d)
def hop(who, t, h=30):
    tl(f'tl.fromTo("#r{who}",{{y:0}},{{y:{-h},duration:.14,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def squash(who, t, amt=.12):
    tl(f'tl.fromTo("#r{who}",{{scaleX:1,scaleY:1}},{{scaleX:{1+amt},scaleY:{1-amt},svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def sand_puff(t, big=False):
    k = 2.0 if big else 1.0
    tl(f'tl.set("#sandp",{{opacity:1}},{f(t)}); tl.set("#sandp",{{opacity:0}},{f(t+.75)});')
    for i in range(8):
        a = math.pi * (0.1 + 0.8 * i / 7); dx = -math.cos(a) * 120 * k; dy = -math.sin(a) * 70 * min(k, 1.2) - 20
        tl(f'tl.fromTo("#sp{i}",{{x:0,y:0,scale:.4,opacity:1}},{{x:{dx:.0f},y:{dy:.0f},scale:{1.3*k:.2f},opacity:0,svgOrigin:"0 0",duration:.7,ease:"power2.out",immediateRender:false}},{f(t)});')
def ride(who, t, fast=False):
    """approach the ladder -> climb (holding the rails) -> sit -> slide feet first -> land in the sand"""
    q = .5 if fast else 1.0; fg = FG[who]; m = fg * MID
    move(who, t, FOOT[0], FOOT[1], m, .4 * q if fast else .6, "power2.inOut", bob=0 if fast else 14)
    c0 = t + (.4 * q if fast else .6)
    for j in range(4):
        y0 = FOOT[1] + (TOP[1] - FOOT[1]) * j / 4; y1 = FOOT[1] + (TOP[1] - FOOT[1]) * (j + 1) / 4
        x1 = FOOT[0] + (TOP[0] - FOOT[0]) * (j + 1) / 4
        move(who, c0 + j * .25 * q, x1, y1, m, .22 * q, "power2.out")
    s0 = c0 + 1.0 * q          # on top: sit down (squash) and lean back a little
    tl(f'tl.fromTo("#r{who}",{{scaleX:1,scaleY:1}},{{scaleX:1.05,scaleY:.84,svgOrigin:"0 0",duration:.14,ease:"power2.out",immediateRender:false}},{f(s0)});')
    sl = s0 + .25 * q          # slide (seated, feet first)
    tl(f'tl.fromTo("#r{who}",{{rotation:0}},{{rotation:-12,svgOrigin:"0 0",duration:.15,ease:"power2.out",immediateRender:false}},{f(sl)});')
    move(who, sl, CH_A[0], CH_A[1] + SEAT, m, .12 * q, "power1.in")
    move(who, sl + .12 * q, CH_B[0], CH_B[1] + SEAT, m, .45 * q, "power1.in")
    move(who, sl + .57 * q, SAND[0], SAND[1], m, .28 * q, "power2.out")
    tl(f'tl.to("#r{who}",{{rotation:0,svgOrigin:"0 0",duration:.2,ease:"back.out(2)"}},{f(sl + .6 * q)});')
    land = sl + .85 * q
    tl(f'tl.fromTo("#r{who}",{{scaleX:1.05,scaleY:.84}},{{scaleX:1,scaleY:1,svgOrigin:"0 0",duration:.3,ease:"back.out(2.5)",immediateRender:false}},{f(land)});')
    return land

def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set(".cbadge",{opacity:0}); gsap.set("#sandp",{opacity:0}); gsap.set("#b-stars",{opacity:0}); gsap.set(".conf",{opacity:0});')
    tl('gsap.set("#g-trunk",{svgOrigin:"0 -352",rotation:-30}); gsap.set("#g-ear",{svgOrigin:"-90 -380"}); gsap.set("#g-ear2",{svgOrigin:"90 -380"});')
    tl('gsap.set("#kA-armL",{svgOrigin:"-62 -230"}); gsap.set("#kA-armR",{svgOrigin:"62 -230"}); gsap.set("#kB-armL",{svgOrigin:"-60 -232"}); gsap.set("#kB-armR",{svgOrigin:"60 -232"});')
    P4 = pack(["pari", "chintu", "bunny", "golu"])
    setpos("pari", P4["pari"], ROW_Y, FG["pari"]); setpos("chintu", P4["chintu"], ROW_Y, FG["chintu"])
    setpos("golu", P4["golu"], ROW_Y, FG["golu"]); setpos("bunny", 1250, 1250, FG["bunny"] * MID)
    nb = int(DUR / BEAT)
    # idle life on the beat (offset, never in unison)
    tl(f'tl.to("#g-body",{{scaleY:.955,scaleX:1.022,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-head",{{y:9,rotation:2,svgOrigin:"0 -240",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#kA",{{y:-8,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.1);')
    tl(f'tl.to("#kB",{{y:-7,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.33);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.2);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.45);')
    tl(f'tl.to("#b-head",{{rotation:3,svgOrigin:"0 -150",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.15);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to(".flw",{{rotation:8,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut",stagger:.1}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    tl(f'tl.to("#seat0",{{rotation:5,svgOrigin:"905 985",duration:1.2,yoyo:true,repeat:{int(DUR/1.2)-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#seat1",{{rotation:-4,svgOrigin:"1010 985",duration:1.4,yoyo:true,repeat:{int(DUR/1.4)-1},ease:"sine.inOut"}},0.3);')
    for i, d in enumerate([80, -60, 50]):
        tl(f'tl.fromTo("#cl{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    for k in range(int(DUR / 3)):
        t = 2.2 + k * 3.0
        if t > DUR - 1.5: break
        tl(f'tl.to("#g-ear",{{rotation:-8,duration:.15,yoyo:true,repeat:1}},{t:.2f}); tl.to("#g-ear2",{{rotation:8,duration:.15,yoyo:true,repeat:1}},{t+.12:.2f});')

    # ===== HOOK: Bunny zooms in, up and down the slide, PLOP into the sand (Mithu: धप्प! धप्प!)
    tl('tl.set("#wWait",{opacity:1,scale:.85},0); tl.to("#wWait",{scale:1,duration:.3,ease:"back.out(3)"},0.02);')
    look(-14, 0.05); hk = T["hook"]
    move("bunny", hk["in"], 700, 1290, None, .25, "power1.in")
    lnd = ride("bunny", hk["in"] + .25, fast=True)
    word_out("wWait", lnd - .3); word_in("wPlop", lnd); sand_puff(lnd)
    trunk(0, 1.0, .4, "power2.inOut"); look(10, lnd - .4)
    tl(f'tl.set("#b-stars",{{opacity:1}},{f(lnd+.05)}); tl.fromTo("#b-stars",{{rotation:0}},{{rotation:360,svgOrigin:"0 -470",duration:1.2,ease:"none",immediateRender:false}},{f(lnd+.05)}); tl.set("#b-stars",{{opacity:0}},{f(lnd+1.25)});')
    hop("bunny", lnd + 1.3, 26); bunny_cheer(lnd + 1.3, .5)
    mithu_talk(CUE["a3"], D["a3"]); word_out("wPlop", CUE["a3"] + D["a3"] + .2)
    kids_cheer(lnd + .1, .6)
    # ===== PROBLEM: Pari steps up -> Bunny zips in front (no touching); Chintu steps up -> again
    move("pari", T["pari_step"], 240, 1560, .48, .6, "power2.inOut", bob=12)
    c1 = T["cut1"]; word_in("wMe", c1["in"])
    move("bunny", c1["in"] - .05, 420, 1300, None, .25, "power2.in")
    ride("bunny", c1["in"] + .2, fast=True)
    tl(f'tl.to("#rpari",{{x:-14,duration:.15,ease:"power2.out",yoyo:true,repeat:1}},{f(c1["in"]+.1)});')
    sad("pari", c1["in"] + .45, T["turns"] + .3)
    move("chintu", T["chintu_step"], 440, 1600, .5, .6, "power2.inOut", bob=12)
    c2 = T["cut2"]
    move("bunny", c2["in"] - .05, 420, 1300, None, .25, "power2.in")
    ride("bunny", c2["in"] + .2, fast=True)
    mithu_talk(CUE["b2"], D["b2"]); word_out("wMe", c2["land"])
    tl(f'tl.to("#rchintu",{{x:-14,duration:.15,ease:"power2.out",yoyo:true,repeat:1}},{f(c2["in"]+.1)});')
    sad("chintu", c2["in"] + .45, T["turns"] + .3)
    for z in (c1, c2): sand_puff(z["land"])
    # ===== FEELING: Golu notices; Bunny is alone in the sand (camera eases in on her)
    card("wSad", T["sad"], T["lonely"] - .05); look(-22, T["sad"])
    tl(f'tl.to(".bpup",{{x:-10,duration:.25,ease:"power2.inOut"}},{f(T["sad"]+.4)}); tl.to(".bpup",{{x:10,duration:.3,ease:"power2.inOut"}},{f(T["sad"]+1.0)}); tl.to(".bpup",{{x:0,duration:.2}},{f(T["lonely"]-.3)});')
    sad("bunny", T["lonely"] - .3, T["turns"] + .45)
    card("wAlone", T["lonely"], T["turns"] - .05, punch=False)
    tl(f'tl.to("#cam",{{scale:1.22,duration:.9,ease:"power2.inOut"}},{f(T["lonely"]-.4)}); tl.to("#cam",{{scale:1,duration:.7,ease:"power2.inOut"}},{f(T["turns"]+.05)});')
    # ===== LEARN: बारी-बारी! everyone lines up (Pari, Chintu, Bunny, Golu)
    card("wTurns", T["turns"], T["count"] - .05); happy(T["turns"] + .1, T["turns"] + 1.0); look(0, T["turns"])
    golu_arm("L", 70, T["turns"] + .2, 1.1)
    lu = T["line_up"]
    move("pari", lu, P4["pari"], ROW_Y, FG["pari"], .7, "power2.inOut", bob=12)
    move("chintu", lu + .15, P4["chintu"], ROW_Y, FG["chintu"], .7, "power2.inOut", bob=12)
    move("bunny", lu + .3, P4["bunny"], 1420, FG["bunny"] * .8, .5, "power2.inOut", bob=16)
    move("bunny", lu + .8, P4["bunny"], ROW_Y, FG["bunny"], .5, "power2.inOut", bob=12)
    mithu_talk(CUE["c2"], D["c2"])
    ct = T["count"]; card("wCount", ct, R[0]["go"])
    for k, who in enumerate(["pari", "chintu", "bunny", "golu"]):
        hop(who, ct + .1 + k * .3, 34 if who != "golu" else 24)
        tl(f'tl.fromTo("#cb{k}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,transformOrigin:"50% 50%",duration:.25,ease:"back.out(2)",immediateRender:false}},{f(ct+.1+k*.3)});')
        tl(f'tl.to("#cb{k}",{{opacity:0,duration:.2}},{f(R[0]["go"]-.25)});')
    kids_talk(CUE["c3a"], D["c3a"]); kids_talk(CUE["c3b"], D["c3b"]); kids_cheer(CUE["c3b"] + .1, .7)
    # ===== TRY: four turns, one at a time
    L = ["pari", "chintu", "bunny", "golu"]
    cards = ["wPari", "wChintu", "wBunny", "wGolu"]
    nxt = [R[1]["go"], T["wait_hard"] - .05, R[3]["go"], T["plop2"] - .05]
    for k, r in enumerate(R):
        who = L[0]; rest = L[1:]
        card(cards[k], r["go"] + .1, nxt[k])
        land = ride(who, r["go"])
        pk = pack(rest)
        for j, c in enumerate(rest): move(c, max(r["go"] + .35 + j * .08, MEND.get(c, 0) + .02), pk[c], ROW_Y, FG[c], .6, "power2.inOut", bob=10)
        sand_puff(land, big=(who == "golu"))
        L = rest + [who]; pk = pack(L)
        move(who, r["back"], pk[who], 1420, FG[who] * .82, .45, "power2.inOut", bob=14)
        move(who, r["back"] + .45, pk[who], ROW_Y, FG[who], .5, "power2.inOut", bob=10)
        if who == "golu":
            trunk(-40, land, .2); trunk(0, land + .8, .4, "power2.inOut")
            happy(land + .05, land + 1.0)
            kids_cheer(land + .2, 1.0); bunny_cheer(land + .25, .9)
        elif who == "bunny":
            bunny_cheer(land + .05, .9); kids_cheer(land + .1, .9); golu_arm("R", -100, land + .1, .9)
        else:
            kids_cheer(land + .05, .8)
    # Bunny waits at the front: taps her foot, Mithu "रुको! रुको!", a deep breath and a smile; Golu praises her
    wh = T["wait_hard"]; card("wHard", wh, T["praise"] - .05, punch=False)
    tl(f'tl.fromTo("#b-foot",{{rotation:0}},{{rotation:-18,svgOrigin:"38 -4",duration:.15,yoyo:true,repeat:7,ease:"power2.out",immediateRender:false}},{f(wh+.1)});')
    mithu_talk(CUE["d3"], D["d3"])
    tl(f'tl.fromTo("#b-all",{{scaleX:1,scaleY:1}},{{scaleX:1.05,scaleY:1.07,svgOrigin:"0 0",duration:.45,yoyo:true,repeat:1,ease:"sine.inOut",immediateRender:false}},{f(T["breath"])});')
    card("wGood", T["praise"], R[2]["go"]); happy(T["praise"], T["praise"] + .9); kids_cheer(T["praise"] + .1, .6)
    tl(f'tl.set("#b-eyes",{{opacity:0}},{f(T["praise"]+.1)}); tl.set("#b-happy",{{opacity:1}},{f(T["praise"]+.1)}); tl.set("#b-eyes",{{opacity:1}},{f(T["praise"]+1.0)}); tl.set("#b-happy",{{opacity:0}},{f(T["praise"]+1.0)});')
    mithu_talk(CUE["d6"], D["d6"]); card("wPlop2", T["plop2"], T["moral"] - .05)
    # ===== PAYOFF: the moral, confetti
    mo = T["moral"]; card("wMoral", mo, T["together"] - .05); happy(mo + .05, mo + 1.4)
    golu_arm("L", 110, mo + .1, 1.2); golu_arm("R", -110, mo + .16, 1.2)
    kids_talk(CUE["e2a"], D["e2a"]); kids_talk(CUE["e2b"], D["e2b"]); kids_cheer(CUE["e2a"], 1.2); bunny_cheer(CUE["e2a"] + .1, 1.2)
    random.seed(6)
    for k in range(36):
        x0 = random.uniform(80, 1000); dly = random.uniform(0, .9); rot = random.uniform(-540, 540)
        tl(f'tl.fromTo("#cf{k}",{{x:{x0:.0f},y:760,rotation:0,opacity:1}},{{x:{x0 + random.uniform(-120,120):.0f},y:{random.uniform(1500,1900):.0f},rotation:{rot:.0f},duration:2.6,ease:"power1.in",immediateRender:false}},{f(mo+dly)}); tl.set("#cf{k}",{{opacity:0}},{f(mo+dly+2.6)});')
    card("wTog", T["together"], T["bye"] - .05); kids_cheer(T["together"] + .2, .7)
    # ===== LOOP: wave, Mithu "See you tomorrow!", Bunny zooms off right
    by = T["bye"]; word_in("wBye", by); word_out("wBye", DUR - .62); golu_arm("R", -100, by + .1, 1.4, wave=True); happy(by + 1.0, by + 1.8)
    mithu_talk(CUE["f2"], D["f2"])
    ex = T["exit"]
    move("bunny", ex, 700, 1420, FG["bunny"] * .8, .3, "power2.in", bob=14)
    move("bunny", ex + .3, 1250, 1250, FG["bunny"] * MID, .35, "power2.in")
    trunk(-30, DUR - .45, .3, "power2.out"); look(-14, DUR - .4)
    tl(f'tl.fromTo("#wWait",{{opacity:0,scale:.5}},{{opacity:1,scale:.85,duration:.3,ease:"power2.out",immediateRender:false}},{DUR-.35:.2f});')
    # ===== blinks (offset)
    for t in [2.6, 5.9, 9.4, 13.1, 16.8, 20.3, 24.6, 27.9, 31.7, 35.2, 38.4, 41.6, 44.2]:
        if t < DUR - 1:
            tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
            tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.1:.2f});')
            tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+.6:.2f});')
            tl(f'tl.to(".bpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.4:.2f});')
            tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.9:.2f});')
    # ===== lip-sync: toggle pre-drawn mouths, scale with svgOrigin (never CSS transform-origin)
    def lipsync(levels, mouth, rest_of, origin, scales):
        Lv = list(levels)
        for i in range(1, len(Lv) - 1):
            if Lv[i] and not Lv[i-1] and not Lv[i+1]: Lv[i] = 0
        prev = 0; prest = None
        for i, v in enumerate(Lv):
            t = round(i / lips["fps"], 3); rest = rest_of(t)
            if v == prev and rest == prest: continue
            if v == 0: tl(f'tl.set("{mouth}",{{opacity:0}},{t});tl.set("{rest}",{{opacity:1}},{t});')
            else: tl(f'tl.set("{mouth}",{{opacity:1,scaleY:{scales[v]},svgOrigin:"{origin}"}},{t});tl.set("{rest}",{{opacity:0}},{t});')
            prev, prest = v, rest
    lipsync(lips["golu"], "#g-mouth", lambda t: "#g-smile", "-62 -314", [0, .5, .8, 1.1])
    sad0, sad1 = T["lonely"] - .3, T["turns"] + .45
    lipsync(lips["bunny"], "#b-mouth", lambda t: "#b-sad" if sad0 <= t < sad1 else "#b-smile", "0 -204", [0, .55, .8, 1.05])

def park():
    sunrays = "".join(f'<path d="M0,-92 L12,-120 L-12,-120Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    flowers = "".join(ns["flower"](x, y, c, i) for i, (x, y, c) in enumerate([(40, 1600, "#ff6b9a"), (1040, 1610, "#a66bff"), (560, 1400, "#ffc51c"), (980, 1420, "#ff6b9a"), (300, 1430, "#a66bff")]))
    trees = "".join(f'<g transform="translate({x},{y}) scale({s})" filter="url(#fblur)"><rect x="-10" y="-20" width="20" height="60" rx="8" fill="#a8714a"/><circle cx="0" cy="-50" r="50" fill="#5cc44a"/><circle cx="-24" cy="-64" r="16" fill="#9be86a" opacity=".7"/></g>' for x, y, s in [(70, 1080, .9), (420, 1070, .7), (760, 1075, .8), (1010, 1085, .75)])
    neem = ('<g transform="translate(560,1160)" filter="url(#fblur2)" opacity=".95"><path d="M-22,0 q8,-120 0,-220 l44,0 q-8,100 0,220z" fill="#9a6a40"/>'
            '<circle cx="0" cy="-300" r="130" fill="url(#gCanopy)"/><circle cx="-110" cy="-240" r="80" fill="url(#gCanopy)"/><circle cx="110" cy="-235" r="84" fill="url(#gCanopy)"/>'
            '<circle cx="-40" cy="-350" r="40" fill="#b8f58a" opacity=".55"/></g>')
    swing = ('<g filter="url(#fblur2)" opacity=".9"><path d="M870,985 L840,1235 M870,985 L905,1235 M1050,985 L1020,1235 M1050,985 L1075,1235" stroke="#e85d9a" stroke-width="14" stroke-linecap="round"/>'
             '<rect x="852" y="972" width="216" height="22" rx="11" fill="#ff7ab0"/>'
             '<g id="seat0"><path d="M893,994 L893,1150 M917,994 L917,1150" stroke="#9aa6b8" stroke-width="4"/><rect x="882" y="1146" width="46" height="12" rx="5" fill="#ffd23f"/></g>'
             '<g id="seat1"><path d="M998,994 L998,1140 M1022,994 L1022,1140" stroke="#9aa6b8" stroke-width="4"/><rect x="987" y="1136" width="46" height="12" rx="5" fill="#3fb6ff"/></g></g>')
    sandpit = ('<ellipse cx="860" cy="1312" rx="214" ry="58" fill="#c98a55"/><ellipse cx="860" cy="1304" rx="200" ry="50" fill="url(#gSand)"/>'
               '<ellipse cx="800" cy="1292" rx="60" ry="10" fill="#fff6d8" opacity=".6"/><g fill="#e8c27a"><circle cx="940" cy="1318" r="6"/><circle cx="760" cy="1322" r="5"/><circle cx="990" cy="1300" r="4"/></g>')
    rungs = "".join(f'<rect x="{163 + (TOP[0]-FOOT[0])*(1 - (y-896)/409)*0:.0f}" y="{y}" width="96" height="12" rx="6" fill="#ffd23f"/>' for y in range(950, 1300, 70))
    slide = (f'<g id="slide">'
             f'<ellipse cx="230" cy="1312" rx="120" ry="18" fill="url(#gShadow)"/><ellipse cx="560" cy="1290" rx="300" ry="26" fill="url(#gShadow)"/>'
             f'<path d="M160,900 L160,1305 M304,900 L304,1305" stroke="url(#gRail)" stroke-width="18" stroke-linecap="round"/>'
             f'<path d="M152,1305 L158,858 M268,1305 L262,858" stroke="url(#gRail)" stroke-width="16" stroke-linecap="round"/>{rungs}'
             f'<path d="M158,858 q60,-40 104,0" stroke="url(#gRail)" stroke-width="12" fill="none" stroke-linecap="round"/>'
             f'<rect x="146" y="888" width="172" height="26" rx="10" fill="url(#gPlat)"/>'
             f'<path d="M300,904 C420,960 520,1090 640,1200 C690,1244 760,1268 846,1272" stroke="#c23a22" stroke-width="58" fill="none" stroke-linecap="round"/>'
             f'<path d="M300,898 C420,954 520,1084 640,1194 C690,1238 760,1262 846,1266" stroke="url(#gChute)" stroke-width="44" fill="none" stroke-linecap="round"/>'
             f'<path d="M310,884 C428,940 528,1070 648,1180 C698,1222 766,1244 846,1248" stroke="#ffb08a" stroke-width="9" fill="none" stroke-linecap="round" opacity=".9"/>'
             f'<path d="M560,1130 L560,1290 M700,1232 L700,1290" stroke="url(#gRail)" stroke-width="14" stroke-linecap="round"/></g>')
    return (f'<rect width="1080" height="1180" fill="url(#gSky6)"/>'
            f'<g transform="translate(935,220) scale(.55)"><g id="sunface">{sunrays}</g><circle r="80" fill="url(#gSun)"/>'
            f'<ellipse cx="-24" cy="-10" rx="7" ry="10" fill="#7a4a00"/><ellipse cx="24" cy="-10" rx="7" ry="10" fill="#7a4a00"/>'
            f'<path d="M-26,16 q26,24 52,0" stroke="#7a4a00" stroke-width="6" fill="none" stroke-linecap="round"/></g>'
            f'{cloud("cl0", 160, 230, .65)}{cloud("cl1", 820, 790, .5)}{cloud("cl2", 420, 760, .42)}'
            f'<g filter="url(#fblur)"><ellipse cx="220" cy="1110" rx="560" ry="150" fill="#b4ecac"/><ellipse cx="900" cy="1120" rx="580" ry="170" fill="#a6e49e"/></g>'
            f'{trees}<rect x="0" y="1150" width="1080" height="770" fill="url(#gGrass6)"/>'
            f'<path d="M0,1420 Q540,1380 1080,1430 L1080,1470 Q540,1420 0,1460Z" fill="#b6ef8e" opacity=".5"/>'
            f'{neem}{swing}{sandpit}{slide}{flowers}')

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(36))
    sandp = '<g id="sandp" transform="translate(850,1296)">' + "".join(f'<circle id="sp{i}" r="{14 + (i % 3) * 5}" fill="{["#f6d88f","#e2b964","#fff0c2"][i%3]}"/>' for i in range(8)) + '</g>'
    P4 = pack(["pari", "chintu", "bunny", "golu"]); tops = {"pari": 1540, "chintu": 1540, "bunny": 1530, "golu": 1470}
    cb = "".join(f'<g transform="translate({P4[w]},{tops[w]-28})"><g class="cbadge" id="cb{k}"><circle r="40" fill="#ffffff" stroke="{c}" stroke-width="8"/>'
                 f'<text y="20" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="56" fill="{c}">{k+1}</text></g></g>'
                 for k, (w, c) in enumerate(zip(["pari", "chintu", "bunny", "golu"], ["#d81b60", "#c43e00", "#7b1fa2", "#1e63d6"])))
    lip = ('<path d="M322,936 C440,992 540,1122 660,1232 C710,1276 770,1296 830,1300" stroke="url(#gChute)" stroke-width="30" fill="none" stroke-linecap="round"/>'
           '<path d="M322,926 C440,982 540,1112 660,1222 C710,1266 770,1286 830,1290" stroke="#ffb08a" stroke-width="6" fill="none" stroke-linecap="round" opacity=".85"/>')
    mithu = f'<g filter="url(#f3d)"><g transform="translate(990,974) scale(-.42,.42)">{MITHU}</g></g>'
    chars = "".join(f'<g id="p{w}"><g id="r{w}">{CH[w]}</g></g>' for w in ["golu", "pari", "chintu", "bunny"])
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}</defs>
{park()}
{mithu}
{chars}
{lip}
{sandp}
{cb}
{conf}
</svg>'''
    css = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#8fdcff}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0;transform-origin:850px 1300px}
#punch{position:absolute;inset:0;transform-origin:50% 60%}
#world{position:absolute;inset:0}
#ovl{position:absolute;inset:0}
.word{position:absolute;left:100px;width:780px;top:390px;text-align:center;line-height:1.08;white-space:nowrap}
.word .hi{font-size:120px;font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(0,40,90,.18)}
.word .en{font-size:80px;font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(0,40,90,.18)}
.badge{position:absolute;top:290px;left:130px;padding:12px 26px;border-radius:40px;background:rgba(255,255,255,.94);color:#e65100;font-size:38px;font-weight:800;box-shadow:0 6px 0 rgba(0,60,120,.15)}
"""
    fit = """
function fitWords(){ document.querySelectorAll('.word > div').forEach(function(el){
  if(!el.dataset.fs) el.dataset.fs = parseFloat(getComputedStyle(el).fontSize);
  var fs = +el.dataset.fs; el.style.fontSize = fs + 'px'; el.style.display='inline-block';
  while (el.offsetWidth > 740 && fs > 40) { fs -= 2; el.style.fontSize = fs + 'px'; }
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
