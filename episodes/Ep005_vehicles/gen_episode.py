"""Golu & Dost Ep 5 — गोलू की गाड़ियाँ #1: गाड़ियाँ और उनकी आवाज़ें | Vehicle Sounds (soft-3D glossy, railway-crossing set).
usage: python3 gen_episode.py <project dir>   (needs timing.json next to this file and <proj>/assets/lips.json)"""
import json, math, sys, os
PROJ = sys.argv[1]; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from props import PROP_DEFS, train, bus, tractor, firetruck, boom_gate, signal, milestone, fence, rails, road, puffs, train_engine, coach
T = json.load(open(f"{HERE}/timing.json")); DUR = T["DUR"]; D = T["D"]; V = T["V"]
lips = json.load(open(f"{PROJ}/assets/lips.json"))

# ---- v2 cast from the series template (GOLU, KIDS, gradients, f3d) and Mithu from Ep4
tsrc = open("/home/claude/golu_pipeline/gen_episode_template.py").read()
ns = {"math": math}
exec(tsrc[tsrc.index("COLS = ["):tsrc.index("def overlays():")], ns)
rg, GOLU, KIDS, cloud = ns["rg"], ns["GOLU"], ns["KIDS"], ns["cloud"]
F3D = tsrc[tsrc.index('<filter id="f3d"'):tsrc.index('</filter>') + len('</filter>')]
MITHU = open(f"{HERE}/mithu_src.txt").read()
defs = ns["defs"] + PROP_DEFS + F3D + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    '<linearGradient id="gSky5" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5ec8ff"/><stop offset=".7" stop-color="#a8e4ff"/><stop offset="1" stop-color="#d8f4ff"/></linearGradient>',
    '<filter id="fblur" x="-10%" y="-30%" width="120%" height="160%"><feGaussianBlur stdDeviation="5"/></filter>',
])

# ---- on-screen words (Hindi big, English below, optional sound line)
WORDS = [  # id, hindi, english, sound line, hi colour, en colour
    ("wHonk", "पों-पों!", "Beep beep!", None, "#e06a00", "#1565c0"),
    ("wChuk", "छुक-छुक!", "Choo-choo!", None, "#d81b3a", "#1565c0"),
    ("wIntro", "चलो, गाड़ियाँ सीखें!", "Let's learn vehicles!", None, "#6a1fc2", "#c2185b"),
    ("wV0", "रेलगाड़ी", "Train", "छुक-छुक · Choo-choo", "#d81b3a", "#1565c0"),
    ("wV1", "बस", "Bus", "पों-पों · Beep beep", "#b85400", "#1565c0"),
    ("wV2", "ट्रैक्टर", "Tractor", "घर्र-घर्र · Vroom vroom", "#17702c", "#1565c0"),
    ("wV3", "दमकल", "Fire truck", "वीं-वूँ · Wee-woo", "#c41414", "#1565c0"),
    ("wG", "चलो फिर से!", "Let's do it again!", None, "#c2185b", "#1565c0"),
    ("wS", "शाबाश!", "Well done!", None, "#ff5fa2", "#e08a00"),
    ("wJ", "कल फिर मिलेंगे!", "See you tomorrow!", None, "#6a1fc2", "#1565c0"),
]

def overlays():
    w = ""
    for i, hi, en, snd, hc, ec in WORDS:
        s = f'<div class="snd">{snd}</div>' if snd else ""
        w += f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div><div class="en" style="color:{ec}">{en}</div>{s}</div>'
    return w + '<div class="badge">गोलू की गाड़ियाँ #1 · Golu\'s Vehicles</div>'

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
def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set(".bub",{opacity:0});')
    tl('gsap.set("#g-trunk",{svgOrigin:"0 -352",rotation:-52}); gsap.set("#g-ear",{svgOrigin:"-90 -380"}); gsap.set("#g-ear2",{svgOrigin:"90 -380"});')
    tl('gsap.set("#kA-armL",{svgOrigin:"-62 -230"}); gsap.set("#kA-armR",{svgOrigin:"62 -230"}); gsap.set("#kB-armL",{svgOrigin:"-60 -232"}); gsap.set("#kB-armR",{svgOrigin:"60 -232"});')
    tl('gsap.set("#garm",{svgOrigin:"0 0",rotation:0}); gsap.set("#sigG",{opacity:0});')
    tl(f'gsap.set("#train",{{x:-400}}); gsap.set("#bus",{{x:-500}}); gsap.set("#trac",{{x:-400}}); gsap.set("#fire",{{x:-500}});')
    vis = [(0.5, 1.6), (V[0]['in'] - .05, V[0]['out'] + 1.2)] 
    tl('gsap.set("#vw0,#vw1,#vw2,#vw3",{visibility:"hidden"});')
    for a, b in vis: tl(f'tl.set("#vw0",{{visibility:"visible"}},{a:.2f}); tl.set("#vw0",{{visibility:"hidden"}},{b:.2f});')
    for k in (1, 2, 3): tl(f'tl.set("#vw{k}",{{visibility:"visible"}},{V[k]["in"]-.05:.2f}); tl.set("#vw{k}",{{visibility:"hidden"}},{V[k]["out"]+.8:.2f});')
    nb = int(DUR / BEAT)
    # idle life on the beat: Golu breathes/bounces, ears offset, kids dance offset, flowers, clouds
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
    # ear flaps (idle, offset, never in unison)
    for k in range(int(DUR / 3)):
        t = 2.2 + k * 3.0
        if t > DUR - 1.5: break
        tl(f'tl.to("#g-ear",{{rotation:-8,duration:.15,yoyo:true,repeat:1}},{t:.2f}); tl.to("#g-ear2",{{rotation:8,duration:.15,yoyo:true,repeat:1}},{t+.12:.2f});')

    # ===== HOOK 0–3 s: Golu honks, the train whooshes past, gust, Mithu spins
    tl('tl.set("#wHonk",{opacity:1,scale:.85},0); tl.to("#wHonk",{scale:1,duration:.3,ease:"back.out(3)"},0.02);'); honk(0.25, 2)
    t0 = T["train0"]
    tl(f'tl.fromTo("#train",{{x:-300}},{{x:2300,duration:.95,ease:"power1.in",immediateRender:false}},{t0});')
    spin("wT", t0, t0 + .95, 4)
    puff("stm", 3, t0 + .1, -160, -60)
    tl(f'tl.set("#speed",{{opacity:1}},{t0+.2}); tl.fromTo("#speed",{{x:-200}},{{x:300,duration:.6,ease:"none",immediateRender:false}},{t0+.2}); tl.set("#speed",{{opacity:0}},{t0+.8});')
    # gust: ears blow back (flare + flutter, offset), Golu leans and squints, Mithu spins round
    tl(f'tl.to("#g-ear",{{rotation:-24,duration:.12,ease:"power2.out"}},{t0+.35}); tl.to("#g-ear",{{rotation:-14,duration:.07,yoyo:true,repeat:7}},{t0+.47}); tl.to("#g-ear",{{rotation:0,duration:.35,ease:"back.out(2)"}},{t0+1.05});')
    tl(f'tl.to("#g-ear2",{{rotation:26,duration:.12,ease:"power2.out"}},{t0+.4}); tl.to("#g-ear2",{{rotation:16,duration:.07,yoyo:true,repeat:7}},{t0+.52}); tl.to("#g-ear2",{{rotation:0,duration:.35,ease:"back.out(2)"}},{t0+1.1});')
    tl(f'tl.to("#gwrap",{{x:24,rotation:3,svgOrigin:"0 0",duration:.15,ease:"power2.out"}},{t0+.35}); tl.to("#gwrap",{{x:0,rotation:0,duration:.4,ease:"elastic.out(1,.5)"}},{t0+1.0});')
    happy(t0 + .35, t0 + 1.05)
    tl(f'tl.to("#m-all",{{rotation:-360,svgOrigin:"0 -100",duration:.6,ease:"power2.out"}},{t0+.4}); tl.set("#m-all",{{rotation:0}},{t0+1.01});')
    word_out("wHonk", t0 + .9)
    a2 = T["CUES"][1][1]
    word_in("wChuk", a2 - .05); mithu_talk(a2, D["a2"])
    tl(f'tl.to("#mithu",{{rotation:8,svgOrigin:"0 -80",duration:.2,yoyo:true,repeat:5,ease:"sine.inOut"}},{a2:.2f});')   # dizzy wobble
    gate(-80, a2 + .3, .6); signal_blink(0, a2 + .3)
    word_out("wChuk", T["intro"] - .25)
    # ===== INTRO
    it = T["intro"]
    word_in("wIntro", it); jump(it + .1); happy(it + .1, it + 1.1)
    tl(f'tl.to("#g-trunk",{{rotation:-30,duration:.25,ease:"back.out(2)"}},{it:.2f}); tl.to("#g-trunk",{{rotation:-12,duration:.2,yoyo:true,repeat:3}},{it+.25:.2f}); tl.to("#g-trunk",{{rotation:0,duration:.3}},{it+1.05:.2f});')
    kids_cheer(it + .2, .9)
    word_out("wIntro", V[0]["g"] - .3)

    # ===== VEHICLES
    names = ["train", "bus", "trac", "fire"]
    for k, v in enumerate(V):
        sel = "#" + names[k]; wc = ["wT", "wB", "wR", "wF"][k]
        tin, tg, tm, tk, tout = v["in"], v["g"], v["m"], v["k"], v["out"]
        if k == 0:  # gate comes down, signal blinks, train arrives slowly and stops
            gate(0, tin - .6, .5); tl(f'tl.set("#sigG",{{opacity:0}},{tin-.6:.2f});'); signal_blink(tin - .6, tout + .9)
            tl(f'tl.fromTo("#train",{{x:-300}},{{x:590,duration:1.0,ease:"power2.out",immediateRender:false}},{tin:.2f});')
            spin(wc, tin, tin + 1.0, 2)
            puff("stm", 3, tg - .1); puff("stm", 3, tk)
            tl(f'tl.to("#train",{{x:2400,duration:1.1,ease:"power2.in"}},{tout:.2f});'); spin(wc, tout, tout + 1.1, 3)
            gate(-80, tout + 1.0, .32)
        else:
            stop = 540 if k != 2 else 560
            tl(f'tl.fromTo("{sel}",{{x:-450}},{{x:{stop},duration:.75,ease:"power3.out",immediateRender:false}},{tin:.2f});')
            spin(wc, tin, tin + .75, 2.5); squash(f"{sel} .vbody", tin + .72)
            tl(f'tl.to("{sel}",{{x:1550,duration:.6,ease:"power3.in"}},{tout:.2f});'); spin(wc, tout, tout + .6, 2.5)
            if k == 1:   # bus horn: body bounces twice on "पों-पों"
                tl(f'tl.to("#bus .vbody",{{y:-10,duration:.1,yoyo:true,repeat:3}},{tg+.35:.2f});')
                tl(f'tl.to("#bus .vbody",{{y:-10,duration:.1,yoyo:true,repeat:3}},{tk+.9:.2f});')
            if k == 2:   # tractor rumbles + smoke rings
                tl(f'tl.to("#trac .vbody",{{y:-5,duration:.06,yoyo:true,repeat:{int((tout-tin)/.12)}}},{tin:.2f});')
                puff("smk", 4, tg + .2, -30, -150); puff("smk", 4, tk + .3, -30, -150)
            if k == 3:   # beacon flashes red/blue the whole time on screen
                t = tin
                while t < tout + .7:
                    tl(f'tl.set(".bcR",{{opacity:1}},{t:.2f}); tl.set(".bcB",{{opacity:.35}},{t:.2f}); tl.set("#bglow",{{opacity:.8}},{t:.2f}); tl.set(".bcR",{{opacity:.35}},{t+.25:.2f}); tl.set(".bcB",{{opacity:1}},{t+.25:.2f}); tl.set("#bglow",{{opacity:0}},{t+.25:.2f});')
                    t += .5
        look(-14, tin + (.3 if k else 0)); look(0, tin + 1.0); look(16, tout)
        if k == 3: look(0, tout + .3)
        word_in(f"wV{k}", tg); pulse(f"#wV{k} .en", tm); pulse(f"#wV{k} .snd", tk)
        happy(tg, tg + .9); jump(tm, 1, -40)
        if k == 3:   # siren: trunk wiggles and tangles, springs back
            tl(f'tl.to("#g-trunk",{{rotation:-40,duration:.12,yoyo:true,repeat:5,ease:"sine.inOut"}},{tg+.4:.2f});')
            tl(f'tl.to("#g-trunk",{{scaleY:.7,scaleX:1.2,svgOrigin:"0 -352",duration:.15,yoyo:true,repeat:1}},{tg+1.1:.2f});')
            trunk(0, tg + 1.45, .3, "elastic.out(1,.5)")
        elif k == 2:  # engine shake
            tl(f'tl.to("#gwrap",{{x:6,duration:.05,yoyo:true,repeat:11}},{tg+.5:.2f});')
        else:
            honk(tg + .3, 2)
        mithu_talk(tm, D[["c2", "d2", "e2", "f2"][k]])
        kids_cheer(tk, max(.8, D[["c3", "d3", "e3", "f3"][k]] - .3)); kids_talk(tk, D[["c3", "d3", "e3", "f3"][k]])
        kids_wave(tout)
        word_out(f"wV{k}", tout + .1)

    # ===== RECAP: four bubbles pop in, bounce on each name (Hindi row, then English row)
    rc = T["recap"]
    word_in("wG", rc); jump(rc + .2); happy(rc + .2, rc + 1.2)
    tl(f'tl.to("#g-trunk",{{rotation:-30,duration:.25}},{rc:.2f}); tl.to("#g-trunk",{{rotation:0,duration:.3}},{rc+.9:.2f});')
    word_out("wG", T["h1"] - .15)
    for k in range(4):
        tl(f'tl.fromTo("#bub{k}",{{opacity:0,y:60}},{{opacity:1,y:0,duration:.4,ease:"back.out(2.5)",immediateRender:false}},{rc + .3 + k*.12:.2f});')
    for row, (key, lid) in enumerate([("h1", "h1"), ("h2", "h2")]):
        t0 = T[key]; step = D[lid] / 4.2
        if row == 1:
            tl(f'tl.set(".bh",{{opacity:0}},{t0-.05:.2f}); tl.set(".be",{{opacity:1}},{t0-.05:.2f});')
        for k in range(4):
            tl(f'tl.fromTo("#bub{k}",{{y:0}},{{y:-28,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t0 + k*step:.2f});')
        kids_talk(t0, D[lid]); kids_cheer(t0 + D[lid] - .4, .6)
    sh = T.get("s1")
    if sh:
        word_in("wS", sh); happy(sh, sh + 1.2); jump(sh, 2)
        word_out("wS", T["end"] - .2)
    lastb = T["end"] - .2
    for k in range(4):
        tl(f'tl.to("#bub{k}",{{opacity:0,y:40,duration:.25}},{lastb + k*.05:.2f});')

    # ===== END: see you tomorrow + confetti, then loop pose
    en = T["end"]
    word_in("wJ", en); pulse("#wJ .en", T["k2"]); happy(en + .1, en + 1.2)
    tl(f'tl.to("#g-trunk",{{rotation:-35,duration:.25,ease:"back.out(2)"}},{en:.2f}); tl.to("#g-trunk",{{rotation:-15,duration:.25,yoyo:true,repeat:5}},{en+.25:.2f}); tl.to("#g-trunk",{{rotation:0,duration:.25}},{en+1.75:.2f});')
    mithu_talk(T["k2"], D["k2"]); kids_wave(en + .3); kids_wave(T["k2"] + .4); jump(T["k2"], 1, -40)
    tl(f'tl.set(".conf",{{opacity:1}},{en:.2f});')
    for k in range(36):
        x = (k * 97) % 1080
        tl(f'tl.fromTo("#cf{k}",{{x:{x},y:-80,rotation:0}},{{y:{1500 + (k*53) % 400},x:{x + ((k*37) % 160) - 80},rotation:{360 + k*20},duration:{2.0 + (k % 5)*.15:.2f},ease:"power1.in",immediateRender:false}},{en + (k % 8)*.05:.2f});')
    tl(f'tl.set(".conf",{{opacity:0}},{min(en + 2.9, DUR - .9):.2f});')
    word_out("wJ", DUR - .85)
    # loop: gate down, signal red, trunk up in the honk pose = frame 1
    lp = DUR - .8
    gate(0, lp, .45); tl(f'tl.set("#sigG",{{opacity:0}},{lp:.2f});'); signal_blink(lp, DUR)
    tl(f'tl.set("#sigR",{{opacity:1}},{DUR-.05:.2f}); tl.set("#sigGlow",{{opacity:1}},{DUR-.05:.2f}); tl.set("#sigG",{{opacity:0}},{DUR-.05:.2f});')
    trunk(-52, lp + .1, .35, "power2.out"); look(0, lp)

    tl(f'tl.fromTo("#wHonk",{{opacity:0,scale:.5}},{{opacity:1,scale:.85,duration:.3,ease:"power2.out",immediateRender:false}},{DUR-.35:.2f});')
    # blinks (Golu, kids, Mithu — offset)
    for t in [2.6, 5.9, 9.4, 13.1, 16.8, 20.3, 24.6, 27.9, 31.7, 35.2, 38.4]:
        if t < DUR - 1:
            tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
            tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.1:.2f});')
            tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+.6:.2f});')
            tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.6:.2f});')
    # lip-sync (Golu): toggle pre-drawn mouth, scale with svgOrigin (never CSS transform-origin)
    L = list(lips["golu"])
    for i in range(1, len(L) - 1):
        if L[i] and not L[i-1] and not L[i+1]: L[i] = 0
    prev = 0
    for i, v in enumerate(L):
        if v == prev: continue
        t = round(i / lips["fps"], 3)
        if v == 0: tl(f'tl.set("#g-mouth",{{opacity:0}},{t});tl.set("#g-smile",{{opacity:1}},{t});')
        else: tl(f'tl.set("#g-mouth",{{opacity:1,scaleY:{[0,.5,.8,1.1][v]},svgOrigin:"-62 -314"}},{t});tl.set("#g-smile",{{opacity:0}},{t});')
        prev = v

def bubbles():
    items = [(lambda: f'<g transform="translate(-20,0) scale(.36)">{train_engine("wX")}</g>', "रेलगाड़ी", "Train", "#e0302a"),
             (lambda: f'<g transform="scale(.33)">{bus("bx", "wX")}</g>', "बस", "Bus", "#b86200"),
             (lambda: f'<g transform="scale(.4)">{tractor("tx", "wX")}</g>', "ट्रैक्टर", "Tractor", "#1a7a30"),
             (lambda: f'<g transform="scale(.32)">{firetruck("fx", "wX")}</g>', "दमकल", "Fire truck", "#d01818")]
    pos = [(300, 815), (740, 815), (300, 1075), (740, 1075)]
    s = ""
    for k, ((fn, hi, en, c), (x, y)) in enumerate(zip(items, pos)):
        body = fn().replace('id="beacon"', 'id="beaconx"').replace('id="bglow"', 'id="bglowx"').replace('class="smk"', 'class="smkx"')
        body = body.replace('id="smk', 'id="smkx')
        s += (f'<g transform="translate({x},{y})"><g class="bub" id="bub{k}">'
              f'<circle r="125" fill="#ffffff" opacity=".93"/><circle r="125" fill="none" stroke="{c}" stroke-width="10"/>'
              f'<g transform="translate(0,34) scale(.9)">{body}</g>'
              f'<text class="bh" x="0" y="88" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="46" fill="{c}" stroke="#fff" stroke-width="8" paint-order="stroke">{hi}</text>'
              f'<text class="be" x="0" y="86" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="{34 if len(en) > 7 else 40}" fill="#1565c0" stroke="#fff" stroke-width="8" paint-order="stroke" opacity="0">{en}</text>'
              f'</g></g>')
    return s

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(36))
    sunrays = "".join(f'<path d="M0,-92 L12,-120 L-12,-120Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    flowers = "".join(ns["flower"](x, y, c, i) for i, (x, y, c) in enumerate([(40, 1560, "#ff6b9a"), (1040, 1560, "#a66bff"), (330, 1420, "#ffc51c"), (760, 1440, "#ff6b9a")]))
    trees = "".join(f'<g transform="translate({x},{y}) scale({s})"><rect x="-10" y="-20" width="20" height="60" rx="8" fill="#a8714a"/><circle cx="0" cy="-50" r="50" fill="#5cc44a"/><circle cx="-24" cy="-64" r="16" fill="#9be86a" opacity=".7"/></g>' for x, y, s in [(140, 975, .8), (420, 965, .6), (980, 975, .9)])
    trainsvg = train("train", "wT")
    trainsvg = trainsvg[:-4] + puffs("stm", 135, -262, 3) + '</g>'
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
<g id="vw0" transform="translate(0,{RAIL_Y})">{trainsvg}</g>
<g id="speed" opacity="0">{speed}</g>
<g transform="translate(150,1112)">{boom_gate().replace('width="330"', 'width="260"').replace('<circle cx="318"', '<circle cx="248"')}</g>
{road(1150, 1300)}
<g id="vw1" transform="translate(0,{ROAD_Y})" filter="url(#f3d)">{bus("bus", "wB")}</g>
<g id="vw2" transform="translate(0,{ROAD_Y})" filter="url(#f3d)">{tractor("trac", "wR")}</g>
<g id="vw3" transform="translate(0,{ROAD_Y})" filter="url(#f3d)">{firetruck("fire", "wF")}</g>
<rect x="0" y="1300" width="1080" height="620" fill="url(#gGrass)"/>
{fence(1290, 1345)}
{flowers}
<g transform="translate(895,1460)">{milestone()}</g>
<g filter="url(#f3d)"><g transform="translate(895,1350) scale(-.72,.72)"><g id="mithu">{MITHU}</g></g></g>
{KIDS}
<g transform="translate(540,1850) scale(.98)" filter="url(#f3d)"><g id="gwrap">{GOLU}</g></g>
{bubbles()}
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
