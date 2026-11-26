"""Golu & Dost Ep 9 — गोलू की गाड़ियाँ #2: गाड़ियों की आवाज़ | Vehicle Sounds #2 (soft-3D glossy, railway-crossing set from Ep5).
usage: python3 gen_episode.py <project dir>   (needs timing.json next to this file and <proj>/assets/lips.json)"""
import json, math, sys, os
PROJ = sys.argv[1]; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from props import PROP_DEFS, boom_gate, signal, milestone, fence, rails, road, puffs, aeroplane, ambulance, digger, auto_rickshaw
T = json.load(open(f"{HERE}/timing.json")); DUR = T["DUR"]; D = T["D"]; V = T["V"]; CUE = dict((k, v) for k, v in T["CUES"])
lips = json.load(open(f"{PROJ}/assets/lips.json"))

# ---- v2 cast from the series template (GOLU, KIDS, gradients, f3d) and Mithu from Ep4
tsrc = open("/home/claude/golu_pipeline/gen_episode_template.py").read()
ns = {"math": math}
exec(tsrc[tsrc.index("COLS = ["):tsrc.index("def overlays():")], ns)
rg, GOLU, KIDS, cloud = ns["rg"], ns["GOLU"], ns["KIDS"], ns["cloud"]
F3D = tsrc[tsrc.index('<filter id="f3d"'):tsrc.index('</filter>') + len('</filter>')]
MITHU = open(f"{HERE}/mithu_src.txt").read()
FLAP = '<path d="M-12,-238 l-34,58 l52,-30z" fill="#ff9a5c"/><circle cx="0" cy="-236" r="13" fill="#ffd24a"/>'
assert FLAP in GOLU
GOLU = GOLU.replace(FLAP, FLAP + '<g transform="translate(-52,-220)"><ellipse cx="-17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(-18 -17 0)"/><ellipse cx="17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(18 17 0)"/><circle r="12" fill="#ffd24a" stroke="#e09400" stroke-width="3"/><circle cx="-4" cy="-4" r="4" fill="#fff6c0"/></g>')
HAT = ('<g id="m-hat" opacity="0"><g transform="translate(18,-262)"><path d="M-70,10 Q-64,-46 -10,-56 Q8,-72 30,-52 Q70,-40 72,10 Q0,26 -70,10Z" fill="url(#gSand)"/>'
       '<circle cx="-30" cy="-14" r="6" fill="#a8702e" opacity=".5"/><circle cx="22" cy="-26" r="5" fill="#a8702e" opacity=".5"/><ellipse cx="-20" cy="-40" rx="22" ry="7" fill="#fff" opacity=".45"/></g></g>')
MITHU = MITHU.replace('<g id="m-beak">', HAT + '<g id="m-beak">', 1)
assert 'id="m-hat"' in MITHU
BUNNY = open(f"{HERE}/bunny_v2.svg.txt").read()
defs = ns["defs"] + PROP_DEFS + F3D + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    '<linearGradient id="gSky5" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5ec8ff"/><stop offset=".7" stop-color="#a8e4ff"/><stop offset="1" stop-color="#d8f4ff"/></linearGradient>',
    rg("gBun", [(0, "#ffffff"), (.6, "#f1ecff"), (1, "#c7b8ef")], "38%", "30%", "75%"),
    rg("gBunIn", [(0, "#ffd3e2"), (1, "#f59ab9")], "45%", "40%", "70%"),
    '<filter id="fblur" x="-10%" y="-30%" width="120%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>',
])

# ---- on-screen words (Hindi big, English below, optional sound line)
WORDS = [  # id, hindi, english, sound line, hi colour, en colour
    ("wHonk", "पों-पों!", "Honk honk!", None, "#e06a00", "#1565c0"),
    ("wZoom", "ज़ूम!", "Zoom!", None, "#1565c0", "#d81b3a"),
    ("wIntro", "चलो, नई गाड़ियाँ सीखें!", "Let's learn new vehicles!", None, "#6a1fc2", "#c2185b"),
    ("wV0", "हवाई जहाज़", "Aeroplane", "ज़ूम · Zoom", "#1565c0", "#d81b3a"),
    ("wV1", "एम्बुलेंस", "Ambulance", "वी-वू · Wee-woo", "#d81b3a", "#1565c0"),
    ("wV2", "खुदाई मशीन", "Digger", "घर्र-घर्र · Rumble rumble", "#b85400", "#1565c0"),
    ("wHat", "मेरी टोपी!", "My hat!", None, "#17702c", "#b85400"),
    ("wV3", "ऑटो रिक्शा", "Auto rickshaw", "पट-पट · Putt-putt", "#17702c", "#1565c0"),
    ("wTurn", "मेरी बारी?", "My turn?", None, "#c2185b", "#6a1fc2"),
    ("wG", "चलो फिर से!", "Let's do it again!", None, "#c2185b", "#1565c0"),
    ("wJ", "कल फिर मिलेंगे!", "See you tomorrow!", None, "#6a1fc2", "#1565c0"),
]

def overlays():
    w = ""
    for i, hi, en, snd, hc, ec in WORDS:
        s = f'<div class="snd">{snd}</div>' if snd else ""
        w += f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div><div class="en" style="color:{ec}">{en}</div>{s}</div>'
    return w + '<div class="badge">गोलू की गाड़ियाँ #2 · Golu\'s Vehicles #2</div>'

J = []
def tl(s): J.append(s)
def word_in(i, t):
    tl(f'tl.fromTo("#{i}",{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.35,ease:"back.out(1.6)",immediateRender:false}},{t:.2f});')
    tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.05,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t:.2f});')
def word_out(i, t): tl(f'tl.to("#{i}",{{opacity:0,scale:.5,duration:.2,ease:"power2.in"}},{t:.2f});')
def pulse(sel, t): tl(f'tl.to("{sel}",{{scale:1.15,duration:.15,yoyo:true,repeat:1}},{t:.2f});')
def happy(t0, t1):
    tl(f'tl.set("#g-eyes",{{opacity:0}},{t0:.2f}); tl.set("#g-happy",{{opacity:1}},{t0:.2f}); tl.set("#g-eyes",{{opacity:1}},{t1:.2f}); tl.set("#g-happy",{{opacity:0}},{t1:.2f});')
def jump(t, n=1, h=-50):
    # anticipation squash -> hop -> land squash (character acting)
    tl(f'tl.to("#gwrap",{{scaleY:.94,scaleX:1.04,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1}},{t:.2f});')
    tl(f'tl.to("#gwrap",{{y:{h},duration:.22,ease:"power2.out",yoyo:true,repeat:{2*n-1}}},{t+.1:.2f});')
def look(x, t): tl(f'tl.to(".pup",{{x:{x},duration:.2,ease:"power2.out"}},{t:.2f});')
def trunk(rot, t, d=.25, ease="back.out(2)"): tl(f'tl.to("#g-trunk",{{rotation:{rot},duration:{d},ease:"{ease}"}},{t:.2f});')
def honk(t, n=2):  # trunk pumps like a horn
    trunk(-62, t, .18); tl(f'tl.to("#g-trunk",{{rotation:-48,duration:.12,yoyo:true,repeat:{2*n-1},ease:"sine.inOut"}},{t+.18:.2f});'); trunk(0, t + .18 + .24 * n, .3, "power2.inOut")
def mithu_talk(t, dur):
    n = max(1, int(round(dur / 0.5)))
    tl(f'tl.to("#m-head",{{rotation:-10,svgOrigin:"18 -140",duration:.25,yoyo:true,repeat:{2*n-1},ease:"sine.inOut"}},{t:.2f});')
    tl(f'tl.to("#m-jaw",{{y:8,duration:.125,yoyo:true,repeat:{4*n-1}}},{t:.2f});')
    tl(f'tl.to("#m-all",{{y:-24,duration:.25,yoyo:true,repeat:{2*n-1},ease:"power2.out"}},{t:.2f});')
def kids_talk(t, dur):
    for k, d in (("A", 0), ("B", .05)):
        n = int(dur / .11)
        tl(f'tl.set("#kid{k} .ksmile",{{opacity:0}},{t+d:.2f});')
        for j in range(n):
            big = j % 2 == 0
            tl(f'tl.set("#kid{k} .kmouth",{{opacity:{1 if big else 0}}},{t+d+j*.11:.2f}); tl.set("#kid{k} .ksmall",{{opacity:{0 if big else 1}}},{t+d+j*.11:.2f});')
        tl(f'tl.set("#kid{k} .kmouth",{{opacity:0}},{t+d+n*.11:.2f}); tl.set("#kid{k} .ksmall",{{opacity:0}},{t+d+n*.11:.2f}); tl.set("#kid{k} .ksmile",{{opacity:1}},{t+d+n*.11:.2f});')
def kids_cheer(t, hold=1.0):
    for k, d in (("A", 0), ("B", .07)):
        tl(f'tl.to("#k{k}-armL",{{rotation:80,duration:.18,ease:"back.out(2)"}},{t+d:.2f}); tl.to("#k{k}-armR",{{rotation:-80,duration:.18,ease:"back.out(2)"}},{t+d+.05:.2f});')
        tl(f'tl.to("#k{k}-armL",{{rotation:0,duration:.3,ease:"power2.inOut"}},{t+d+hold:.2f}); tl.to("#k{k}-armR",{{rotation:0,duration:.3,ease:"power2.inOut"}},{t+d+hold+.06:.2f});')
def kids_wave(t):
    for k, arm, d in (("A", "armR", 0), ("B", "armL", .1)):
        s = -1 if arm == "armR" else 1
        tl(f'tl.to("#k{k}-{arm}",{{rotation:{-110*s},duration:.2,ease:"back.out(2)"}},{t+d:.2f}); tl.to("#k{k}-{arm}",{{rotation:{-80*s},duration:.15,yoyo:true,repeat:3}},{t+d+.2:.2f}); tl.to("#k{k}-{arm}",{{rotation:0,duration:.25}},{t+d+.8:.2f});')
def gate(rot, t, d=.5): tl(f'tl.to("#garm",{{rotation:{rot},svgOrigin:"0 0",duration:{d},ease:"power2.inOut"}},{t:.2f});')
def signal_blink(t0, t1):
    t = t0
    while t < t1 - .01:
        tl(f'tl.set("#sigR",{{opacity:1}},{t:.2f}); tl.set("#sigGlow",{{opacity:1}},{t:.2f}); tl.set("#sigR",{{opacity:.25}},{t+.25:.2f}); tl.set("#sigGlow",{{opacity:0}},{t+.25:.2f});')
        t += .5
    tl(f'tl.set("#sigR",{{opacity:.25}},{t1:.2f}); tl.set("#sigGlow",{{opacity:0}},{t1:.2f}); tl.set("#sigG",{{opacity:1}},{t1:.2f});')
def spin(cls, t0, t1, turns_per_s=2.5):
    tl(f'tl.fromTo(".{cls}",{{rotation:0}},{{rotation:{360*turns_per_s*(t1-t0):.0f},svgOrigin:"0 0",duration:{t1-t0:.2f},ease:"none",immediateRender:false}},{t0:.2f});')
def squash(sel, t):
    tl(f'tl.fromTo("{sel}",{{scaleX:1,scaleY:1}},{{scaleX:1.05,scaleY:.95,svgOrigin:"0 0",duration:.12,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t:.2f});')
def puff(prefix, n, t, dx=-50, dy=-130):
    for i in range(n):
        tt = t + i * .18
        tl(f'tl.fromTo("#{prefix}{i}",{{opacity:.95,scale:.3,x:0,y:0}},{{opacity:0,scale:1.5,x:{dx - i*8},y:{dy - i*10},svgOrigin:"0 0",duration:.9,ease:"power1.out",immediateRender:false}},{tt:.2f});')

ROAD_Y = 1272; RAIL_Y = 1048
BX, BY, BSC = 215, 1440, .45          # Bunny on the fence top rail (children's side, road empty while she is there)
STOP = [None, 520, 480, 520]          # road stop x for ambulance / digger / auto
def bunny_talk_set(): pass
def b_hop(t, h=60, d=.16):
    tl(f'tl.fromTo("#bhop",{{y:0}},{{y:{-h},duration:{d},yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t:.2f});')
def beacon(r, b, glow, t0, t1):
    t = t0
    while t < t1:
        tl(f'tl.set("{r}",{{opacity:1}},{t:.2f}); tl.set("{b}",{{opacity:.35}},{t:.2f}); tl.set("{glow}",{{opacity:.8}},{t:.2f}); tl.set("{r}",{{opacity:.35}},{t+.25:.2f}); tl.set("{b}",{{opacity:1}},{t+.25:.2f}); tl.set("{glow}",{{opacity:0}},{t+.25:.2f});')
        t += .5
    tl(f'tl.set("{glow}",{{opacity:0}},{t1:.2f});')
def prop_spin(t0, t1):
    n = int((t1 - t0) / .06)
    tl(f'tl.fromTo(".prop",{{scaleY:1}},{{scaleY:.15,svgOrigin:"0 0",duration:.03,yoyo:true,repeat:{2*n-1},ease:"none",immediateRender:false}},{t0:.2f});')

def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set(".bub",{opacity:0});')
    tl('gsap.set("#g-trunk",{svgOrigin:"0 -352",rotation:-52}); gsap.set("#g-ear",{svgOrigin:"-90 -380"}); gsap.set("#g-ear2",{svgOrigin:"90 -380"});')
    tl('gsap.set("#kA-armL",{svgOrigin:"-62 -230"}); gsap.set("#kA-armR",{svgOrigin:"62 -230"}); gsap.set("#kB-armL",{svgOrigin:"-60 -232"}); gsap.set("#kB-armR",{svgOrigin:"60 -232"});')
    tl('gsap.set("#garm",{svgOrigin:"0 0",rotation:-80}); gsap.set("#sigG",{opacity:1}); gsap.set("#sigR",{opacity:.25}); gsap.set("#sigGlow",{opacity:0});')
    tl('gsap.set("#plane",{x:-520,y:860}); gsap.set("#amb",{x:-560}); gsap.set("#dig",{x:-700}); gsap.set("#auto",{x:-560}); gsap.set("#clump",{x:770,y:1075,opacity:0});')
    tl('gsap.set("#rbunny",{x:-2300}); gsap.set("#darm",{svgOrigin:"60 -230",rotation:0});')
    nb = int(DUR / BEAT)
    tl(f'tl.to("#g-body",{{scaleY:.955,scaleX:1.022,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-head",{{y:9,rotation:2,svgOrigin:"0 -240",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#kA",{{y:-12,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.1);')
    tl(f'tl.to("#kB",{{y:-10,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.33);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.2);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.45);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to(".flw",{{rotation:8,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut",stagger:.1}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    for i, d in enumerate([90, -70, 60]):
        tl(f'tl.fromTo("#cl{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    for k in range(int(DUR / 3)):
        t = 2.2 + k * 3.0
        if t > DUR - 1.5: break
        tl(f'tl.to("#g-ear",{{rotation:-8,duration:.15,yoyo:true,repeat:1}},{t:.2f}); tl.to("#g-ear2",{{rotation:8,duration:.15,yoyo:true,repeat:1}},{t+.12:.2f});')

    # ===== HOOK: Golu honks, a plane zooms LOW over the crossing, gust, Mithu spins
    tl('tl.set("#wHonk",{opacity:1,scale:.85},0); tl.to("#wHonk",{scale:1,duration:.3,ease:"back.out(3)"},0.02);'); honk(0.25, 2)
    t0 = T["plane0"]
    tl(f'tl.fromTo("#plane",{{x:-520,y:980,rotation:-6}},{{x:1700,y:820,rotation:-10,duration:.9,ease:"power1.in",immediateRender:false}},{t0});')
    prop_spin(t0, t0 + 1.0)
    tl(f'tl.set("#speed",{{opacity:1}},{t0+.2}); tl.fromTo("#speed",{{x:-200}},{{x:300,duration:.6,ease:"none",immediateRender:false}},{t0+.2}); tl.set("#speed",{{opacity:0}},{t0+.8});')
    tl(f'tl.to("#g-ear",{{rotation:-24,duration:.12,ease:"power2.out"}},{t0+.35}); tl.to("#g-ear",{{rotation:-14,duration:.07,yoyo:true,repeat:7}},{t0+.47}); tl.to("#g-ear",{{rotation:0,duration:.35,ease:"back.out(2)"}},{t0+1.05});')
    tl(f'tl.to("#g-ear2",{{rotation:26,duration:.12,ease:"power2.out"}},{t0+.4}); tl.to("#g-ear2",{{rotation:16,duration:.07,yoyo:true,repeat:7}},{t0+.52}); tl.to("#g-ear2",{{rotation:0,duration:.35,ease:"back.out(2)"}},{t0+1.1});')
    tl(f'tl.to("#gwrap",{{x:24,rotation:3,svgOrigin:"0 0",duration:.15,ease:"power2.out"}},{t0+.35}); tl.to("#gwrap",{{x:0,rotation:0,duration:.4,ease:"elastic.out(1,.5)"}},{t0+1.0});')
    happy(t0 + .35, t0 + 1.05)
    tl(f'tl.to("#m-all",{{rotation:-360,svgOrigin:"0 -100",duration:.6,ease:"power2.out"}},{t0+.4}); tl.set("#m-all",{{rotation:0}},{t0+1.01});')
    word_out("wHonk", t0 + .9)
    a2 = CUE["a2"]
    word_in("wZoom", a2 - .05); mithu_talk(a2, D["a2"])
    tl(f'tl.to("#mithu",{{rotation:8,svgOrigin:"0 -80",duration:.2,yoyo:true,repeat:3,ease:"sine.inOut"}},{a2:.2f});')
    word_out("wZoom", V[0]["g"] - .25)
    kids_cheer(T["intro"], .6)

    # ===== VEHICLES
    names = ["plane", "amb", "dig", "auto"]
    for k, v in enumerate(V):
        sel = "#" + names[k]
        tin, tg, tm, tk, tout = v["in"], v["g"], v["m"], v["k"], v["out"]
        if k == 0:   # the plane loops back and floats across the sky, bobbing, then climbs away
            tl(f'tl.fromTo("#plane",{{x:-520,y:900,rotation:-4}},{{x:560,y:860,rotation:0,duration:1.0,ease:"power2.out",immediateRender:false}},{tin:.2f});')
            n = max(1, int((tout - tin - 1.0) / .5))
            tl(f'tl.to("#plane",{{y:836,duration:.5,yoyo:true,repeat:{n-1},ease:"sine.inOut"}},{tin+1.0:.2f});')
            tl(f'tl.to("#plane",{{x:1750,y:700,rotation:-10,duration:.9,ease:"power2.in"}},{tout:.2f});')
            prop_spin(tin, tout + 1.0)
        else:
            stop = STOP[k]
            tl(f'tl.fromTo("{sel}",{{x:-560}},{{x:{stop},duration:.75,ease:"power3.out",immediateRender:false}},{tin:.2f});')
            squash(f"{sel} .vbody", tin + .72)
            tl(f'tl.to("{sel}",{{x:1650,duration:.6,ease:"power3.in"}},{tout:.2f});')
            if k != 2:
                spin(["", "wA", "", "wU"][k], tin, tin + .75, 2.5); spin(["", "wA", "", "wU"][k], tout, tout + .6, 2.5)
            if k == 1:
                beacon(".abR", ".abB", "#aglow", tin, tout + .7)
            if k == 2:   # rumble + the arm digs on "घर्र घर्र"
                tl(f'tl.to("#dig .vbody",{{y:-5,duration:.06,yoyo:true,repeat:{int((tout-tin)/.12)*2-1}}},{tin:.2f});')
                tl(f'tl.to("#darm",{{rotation:14,svgOrigin:"60 -230",duration:.3,ease:"power2.inOut",yoyo:true,repeat:1}},{tg+.25:.2f});')
                tl(f'tl.set("#dsand",{{opacity:1}},{tg+.55:.2f});')
                # fling: arm lifts, a soft sand puff arcs onto Mithu's head = hat
                fl, ld = v["fling"], v["land"]
                tl(f'tl.to("#darm",{{rotation:-22,svgOrigin:"60 -230",duration:.22,ease:"back.out(2)"}},{fl:.2f}); tl.to("#darm",{{rotation:0,svgOrigin:"60 -230",duration:.4}},{fl+.6:.2f});')
                tl(f'tl.set("#dsand",{{opacity:0}},{fl+.18:.2f}); tl.set("#clump",{{opacity:1}},{fl+.18:.2f});')
                tl(f'tl.fromTo("#clump",{{x:770,y:1075,rotation:0}},{{x:840,y:960,rotation:-30,duration:.22,ease:"power2.out",immediateRender:false}},{fl+.18:.2f});')
                tl(f'tl.to("#clump",{{x:882,y:1150,rotation:-50,duration:.2,ease:"power2.in"}},{fl+.4:.2f});')
                tl(f'tl.set("#clump",{{opacity:0}},{ld:.2f}); tl.set("#m-hat",{{opacity:1}},{ld:.2f});')
                tl(f'tl.fromTo("#m-all",{{scaleY:1,scaleX:1}},{{scaleY:.86,scaleX:1.1,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1,immediateRender:false}},{ld:.2f});')
                word_out("wV2", ld - .25); word_in("wHat", v["hat"] - .05); mithu_talk(v["hat"], D["e4"])
                happy(ld, ld + 1.2); kids_cheer(ld + .05, .8)
                word_out("wHat", tout + .1)
            if k == 3:
                puff("apf", 3, tin + .1, -60, -40); puff("apf", 3, tout, -80, -40)
                tl(f'tl.to("#auto .vbody",{{y:-8,duration:.1,yoyo:true,repeat:3}},{tg+.4:.2f});')
                tl(f'tl.to("#auto .vbody",{{y:-8,duration:.1,yoyo:true,repeat:3}},{tk+.5:.2f});')
        look(-14, tin + (.3 if k else 0)); look(0, tin + 1.0); look(16, tout)
        if k == 0: look(0, tout + .5)
        if k == 0: tl(f'tl.to(".pup",{{y:-10,duration:.2}},{tin+.8:.2f}); tl.to(".pup",{{y:0,duration:.2}},{tout+.4:.2f});')
        word_in(f"wV{k}", tg); pulse(f"#wV{k} .en", tm); pulse(f"#wV{k} .snd", tk)
        happy(tg, tg + .9); jump(tm, 1, -40)
        if k == 1:   # siren: trunk wiggles like a siren
            tl(f'tl.to("#g-trunk",{{rotation:-40,duration:.12,yoyo:true,repeat:5,ease:"sine.inOut"}},{tg+.4:.2f});')
            trunk(0, tg + 1.2, .3, "elastic.out(1,.5)")
        elif k == 2:
            tl(f'tl.to("#gwrap",{{x:6,duration:.05,yoyo:true,repeat:11}},{tg+.5:.2f});')
        elif k == 0:  # trunk points up at the plane
            trunk(-70, tg, .3); trunk(-45, tg + .5, .2); trunk(0, tm + .4, .3, "power2.inOut")
        else:
            honk(tg + .3, 2)
        mithu_talk(tm, D[["c2", "d2", "e2", "f2"][k]])
        kids_cheer(tk, max(.8, D[["c3", "d3", "e3", "f3"][k]] - .3)); kids_talk(tk, D[["c3", "d3", "e3", "f3"][k]])
        kids_wave(tout)
        if k != 2: word_out(f"wV{k}", tout + .1)

    # ===== BUNNY zooms in along the fence top (too fast!), skids, then waits politely
    bn = T["bun"]
    tl(f'tl.fromTo("#rbunny",{{x:-2300}},{{x:0,duration:.45,ease:"power3.out",immediateRender:false}},{bn:.2f});')
    tl(f'tl.set("#bspeed",{{opacity:1}},{bn:.2f}); tl.fromTo("#bspeed",{{x:-300}},{{x:0,duration:.45,ease:"power3.out",immediateRender:false}},{bn:.2f}); tl.set("#bspeed",{{opacity:0}},{bn+.5:.2f});')
    tl(f'tl.fromTo("#rbunny",{{rotation:0}},{{rotation:14,svgOrigin:"0 0",duration:.15,ease:"power2.out",immediateRender:false}},{bn+.3:.2f}); tl.to("#rbunny",{{rotation:0,svgOrigin:"0 0",duration:.4,ease:"back.out(3)"}},{bn+.45:.2f});')
    tl(f'tl.to("#b-earL",{{rotation:-20,svgOrigin:"-40 -300",duration:.15}},{bn+.35:.2f}); tl.to("#b-earL",{{rotation:0,svgOrigin:"-40 -300",duration:.5,ease:"elastic.out(1,.4)"}},{bn+.5:.2f});')
    tl(f'tl.to("#b-earR",{{rotation:-16,svgOrigin:"44 -300",duration:.15}},{bn+.4:.2f}); tl.to("#b-earR",{{rotation:0,svgOrigin:"44 -300",duration:.5,ease:"elastic.out(1,.4)"}},{bn+.57:.2f});')
    look(-14, bn); look(0, bn + .6)
    word_in("wTurn", CUE["g0"] - .05)
    # paws folded while she waits
    tl(f'tl.to("#b-armL",{{rotation:-30,svgOrigin:"-60 -148",duration:.25}},{T["wait"]-.1:.2f}); tl.to("#b-armR",{{rotation:30,svgOrigin:"60 -148",duration:.25}},{T["wait"]-.05:.2f});')
    tl(f'tl.to("#b-armL",{{rotation:0,svgOrigin:"-60 -148",duration:.25}},{T["recap"]+.3:.2f}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -148",duration:.25}},{T["recap"]+.35:.2f});')
    word_out("wTurn", T["recap"] - .15)

    # ===== RECAP
    rc = T["recap"]
    word_in("wG", rc); jump(rc + .2); happy(rc + .2, rc + 1.2); b_hop(rc + .2, 26)
    tl(f'tl.to("#g-trunk",{{rotation:-30,duration:.25}},{rc:.2f}); tl.to("#g-trunk",{{rotation:0,duration:.3}},{rc+.9:.2f});')
    word_out("wG", T["end"] - .25)
    for k in range(4):
        tl(f'tl.fromTo("#bub{k}",{{opacity:0,y:60}},{{opacity:1,y:0,duration:.4,ease:"back.out(2.5)",immediateRender:false}},{rc + .3 + k*.12:.2f});')
    for key, pair in (("h1", (0, 1)), ("h2", (2, 3))):
        t0 = T[key]; step = D[key] / 2.2
        for j, k in enumerate(pair):
            tl(f'tl.fromTo("#bub{k}",{{y:0}},{{y:-28,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t0 + j*step:.2f});')
            b_hop(t0 + j * step, 24)
        kids_talk(t0, D[key])
    kids_cheer(T["h2"] + D["h2"] - .4, .6); bunny_cheer(T["h2"] + D["h2"] - .4, .6)
    lastb = T["end"] - .2
    for k in range(4):
        tl(f'tl.to("#bub{k}",{{opacity:0,y:40,duration:.25}},{lastb + k*.05:.2f});')

    # ===== END
    en = T["end"]
    word_in("wJ", en); pulse("#wJ .en", T["k2"]); happy(en + .1, en + 1.2)
    tl(f'tl.to("#g-trunk",{{rotation:-35,duration:.25,ease:"back.out(2)"}},{en:.2f}); tl.to("#g-trunk",{{rotation:-15,duration:.25,yoyo:true,repeat:5}},{en+.25:.2f}); tl.to("#g-trunk",{{rotation:0,duration:.25}},{en+1.75:.2f});')
    mithu_talk(T["k2"], D["k2"]); kids_wave(en + .3); kids_wave(T["k2"] + .4); jump(T["k2"], 1, -40)
    tl(f'tl.to("#rbunny",{{x:-2100,duration:.45,ease:"power3.in"}},{en+.6:.2f});')
    tl(f'tl.set(".conf",{{opacity:1}},{en:.2f});')
    for k in range(36):
        x = (k * 97) % 1080
        tl(f'tl.fromTo("#cf{k}",{{x:{x},y:-80,rotation:0}},{{y:{1500 + (k*53) % 400},x:{x + ((k*37) % 160) - 80},rotation:{360 + k*20},duration:{2.0 + (k % 5)*.15:.2f},ease:"power1.in",immediateRender:false}},{en + (k % 8)*.05:.2f});')
    tl(f'tl.set(".conf",{{opacity:0}},{min(en + 2.9, DUR - .9):.2f});')
    word_out("wJ", DUR - .85)
    lp = DUR - .8
    tl(f'tl.to("#m-hat",{{opacity:0,y:-30,duration:.3}},{lp:.2f});')
    trunk(-52, lp + .1, .35, "power2.out"); look(0, lp)
    tl(f'tl.fromTo("#wHonk",{{opacity:0,scale:.5}},{{opacity:1,scale:.85,duration:.3,ease:"power2.out",immediateRender:false}},{DUR-.35:.2f});')
    bt = 2.6
    while bt < DUR - 1:
        tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{bt:.2f});')
        tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{bt+1.1:.2f});')
        tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{bt+.6:.2f});')
        tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{bt+1.6:.2f});')
        bt += 3.4
    def lipsync(levels, mouth, rest, origin, scales):
        L = list(levels)
        for i in range(1, len(L) - 1):
            if L[i] and not L[i-1] and not L[i+1]: L[i] = 0
        prev = 0
        for i, v in enumerate(L):
            if v == prev: continue
            t = round(i / lips["fps"], 3)
            if v == 0: tl(f'tl.set("{mouth}",{{opacity:0}},{t});tl.set("{rest}",{{opacity:1}},{t});')
            else: tl(f'tl.set("{mouth}",{{opacity:1,scaleY:{scales[v]},svgOrigin:"{origin}"}},{t});tl.set("{rest}",{{opacity:0}},{t});')
            prev = v
    lipsync(lips["golu"], "#g-mouth", "#g-smile", "-62 -314", [0, .5, .8, 1.1])
    lipsync(lips["bunny"], "#b-mouth", "#b-smile", "0 -204", [0, .55, .8, 1.05])
def bunny_cheer(t, hold=.8):
    tl(f'tl.to("#b-armL",{{rotation:120,svgOrigin:"-60 -148",duration:.18,ease:"back.out(2)"}},{t:.2f}); tl.to("#b-armR",{{rotation:-120,svgOrigin:"60 -148",duration:.18,ease:"back.out(2)"}},{t+.06:.2f});')
    tl(f'tl.to("#b-armL",{{rotation:0,svgOrigin:"-60 -148",duration:.3}},{t+hold:.2f}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -148",duration:.3}},{t+hold+.06:.2f});')
def bubbles():
    items = [(lambda: f'<g transform="translate(0,-60) scale(.36)">{aeroplane("px")}</g>', "हवाई जहाज़", "Aeroplane", "#1565c0"),
             (lambda: f'<g transform="scale(.33)">{ambulance("ax", "wX")}</g>', "एम्बुलेंस", "Ambulance", "#d81b3a"),
             (lambda: f'<g transform="translate(-30,0) scale(.3)">{digger("dx", "wX")}</g>', "खुदाई मशीन", "Digger", "#b85400"),
             (lambda: f'<g transform="scale(.38)">{auto_rickshaw("ux", "wX")}</g>', "ऑटो रिक्शा", "Auto rickshaw", "#17702c")]
    pos = [(300, 815), (740, 815), (300, 1075), (740, 1075)]
    s = ""
    pos = [(290, 770), (700, 770), (290, 1050), (700, 1050)]
    for k, ((fn, hi, en, c), (x, y)) in enumerate(zip(items, pos)):
        body = fn()
        for a in ("abeacon", "aglow", "darm", "dbucket", "dsand"): body = body.replace(f'id="{a}"', f'id="{a}x"')
        body = body.replace('class="prop"', 'class="propx"').replace('class="abR"', '').replace('class="abB"', '').replace('id="apf', 'id="apfx').replace('class="apf"', 'class="apfx"')
        s += (f'<g transform="translate({x},{y})"><g class="bub" id="bub{k}">'
              f'<circle r="100" fill="#ffffff" opacity=".95"/><circle r="100" fill="none" stroke="{c}" stroke-width="9"/>'
              f'<g transform="translate(0,40) scale(.72)">{body}</g>'
              f'<rect x="-128" y="84" width="256" height="86" rx="30" fill="#ffffff" stroke="{c}" stroke-width="5"/>'
              f'<text class="bh" x="0" y="124" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="40" fill="{c}">{hi}</text>'
              f'<text class="be" x="0" y="158" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="30" fill="#1565c0">{en}</text>'
              f'</g></g>')
    return s

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(36))
    sunrays = "".join(f'<path d="M0,-92 L12,-120 L-12,-120Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    flowers = "".join(ns["flower"](x, y, c, i) for i, (x, y, c) in enumerate([(40, 1560, "#ff6b9a"), (1040, 1560, "#a66bff"), (330, 1420, "#ffc51c"), (760, 1440, "#ff6b9a")]))
    trees = "".join(f'<g transform="translate({x},{y}) scale({s})"><rect x="-10" y="-20" width="20" height="60" rx="8" fill="#a8714a"/><circle cx="0" cy="-50" r="50" fill="#5cc44a"/><circle cx="-24" cy="-64" r="16" fill="#9be86a" opacity=".7"/></g>' for x, y, s in [(140, 975, .8), (420, 965, .6), (980, 975, .9)])
    bspeed = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="9" rx="4" fill="#ffffff" opacity=".85"/>' for x, y, w in [(-40, 1300, 160), (-80, 1350, 220), (-30, 1400, 140)])
    speed = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="10" rx="5" fill="#ffffff" opacity=".8"/>' for x, y, w in [(100, 860, 220), (420, 900, 300), (200, 960, 180), (600, 840, 240)])
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}</defs>
<rect width="1080" height="1100" fill="url(#gSky5)"/>
<g transform="translate(960,250) scale(.62)"><g id="sunface">{sunrays}</g><circle r="80" fill="url(#gSun)"/>
  <ellipse cx="-24" cy="-10" rx="7" ry="10" fill="#7a4a00"/><ellipse cx="24" cy="-10" rx="7" ry="10" fill="#7a4a00"/>
  <path d="M-26,16 q26,24 52,0" stroke="#7a4a00" stroke-width="6" fill="none" stroke-linecap="round"/></g>
{cloud("cl0", 170, 260, .7)}{cloud("cl1", 760, 760, .55)}{cloud("cl2", 380, 690, .45)}
<ellipse cx="200" cy="1000" rx="520" ry="150" fill="#b4ecac"/><ellipse cx="900" cy="1010" rx="560" ry="170" fill="#a6e49e"/>
<rect x="0" y="960" width="1080" height="80" fill="url(#gField)"/>
{trees}
{rails(RAIL_Y)}
<g transform="translate(70,{RAIL_Y-8})">{signal()}</g>
<g id="speed" opacity="0">{speed}</g>
<g transform="translate(150,1112)">{boom_gate().replace('width="330"', 'width="260"').replace('<circle cx="318"', '<circle cx="248"')}</g>
{road(1150, 1300)}
<g transform="translate(0,{ROAD_Y})" filter="url(#f3d)"><g id="amb">{ambulance("ambI", "wA")}</g></g>
<g transform="translate(0,{ROAD_Y})" filter="url(#f3d)"><g id="dig"><g transform="scale(.82)">{digger("digI", "wD")}</g></g></g>
<g transform="translate(0,{ROAD_Y})" filter="url(#f3d)"><g id="auto">{auto_rickshaw("autoI", "wU")}</g></g>
<rect x="0" y="1300" width="1080" height="620" fill="url(#gGrass)"/>
{fence(1290, 1345)}
{flowers}
<g transform="translate(895,1460)">{milestone()}</g>
<g id="bspeed" opacity="0">{bspeed}</g>
<g transform="translate({BX},{BY}) scale({BSC})"><g id="rbunny"><ellipse cx="0" cy="4" rx="90" ry="16" fill="#1a4a10" opacity=".25"/><g id="bhop" filter="url(#f3d)">{BUNNY}</g></g></g>
<g filter="url(#f3d)"><g transform="translate(895,1350) scale(-.72,.72)"><g id="mithu">{MITHU}</g></g></g>
{KIDS}
<g transform="translate(540,1850) scale(.98)" filter="url(#f3d)"><g id="gwrap">{GOLU}</g></g>
{bubbles()}
<g id="plane" filter="url(#f3d)"><g transform="scale(.62)">{aeroplane("planeI")}</g></g>
<g id="clump"><path d="M-30,6 Q-28,-22 0,-26 Q28,-22 30,6 Q0,14 -30,6Z" fill="url(#gSand)"/></g>
{conf}
</svg>'''
    css = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#8fdcff}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0;transform-origin:50% 60%}
#punch{position:absolute;inset:0;transform-origin:50% 40%}
#world{position:absolute;inset:0}
.word{position:absolute;left:100px;width:880px;top:420px;text-align:center;line-height:1.08;white-space:nowrap}
.word .hi{font-size:124px;font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(0,40,90,.18)}
.word .en{font-size:86px;font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(0,40,90,.18)}
.word .snd{font-size:56px;font-weight:800;color:#6a1fc2;-webkit-text-stroke:10px #fff;paint-order:stroke fill;margin-top:6px}
.badge{position:absolute;top:300px;left:130px;padding:12px 26px;border-radius:40px;background:rgba(255,255,255,.94);color:#d81b3a;font-size:38px;font-weight:800;box-shadow:0 6px 0 rgba(0,60,120,.15)}
"""
    fit = """
function fitWords(){ document.querySelectorAll('.word > div').forEach(function(el){
  if(!el.dataset.fs) el.dataset.fs = parseFloat(getComputedStyle(el).fontSize);
  var fs = +el.dataset.fs; el.style.fontSize = fs + 'px'; el.style.display='inline-block';
  while (el.offsetWidth > 860 && fs > 40) { fs -= 2; el.style.fontSize = fs + 'px'; }
  el.style.display='block'; }); }
fitWords(); if (document.fonts) document.fonts.ready.then(fitWords);"""
    js = "\n".join(J)
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
print("ok", len(J), "DUR", DUR)
