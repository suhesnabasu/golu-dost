"""Golu & Dost Ep 10 — Golu Masti #1: गोलू की छींक | Golu's Big Sneeze (silent slapstick, soft-3D glossy, winter park set from Ep6).
usage: python3 gen_episode.py <project dir>   (needs timing.json next to this file and <proj>/assets/lips.json)"""
import json, math, sys, os
PROJ = sys.argv[1]; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json")); DUR = T["DUR"]; D = T["D"]; CUE = dict((k, v) for k, v in T["CUES"])
lips = json.load(open(f"{PROJ}/assets/lips.json"))
def f(v): return f"{v:.3f}"
def E(l): return CUE[l] + D[l]

# ---- v2 cast from the series template (GOLU, KIDS, f3d), glossy Mithu (Ep8/9), v2 Bunny (Ep6-9)
tsrc = open("/home/claude/golu_pipeline/gen_episode_template.py").read()
ns = {"math": math}
exec(tsrc[tsrc.index("COLS = ["):tsrc.index("def overlays():")], ns)
rg, GOLU, KIDS, cloud = ns["rg"], ns["GOLU"], ns["KIDS"], ns["cloud"]
F3D = tsrc[tsrc.index('<filter id="f3d"'):tsrc.index('</filter>') + len('</filter>')]
FLAP = '<path d="M-12,-238 l-34,58 l52,-30z" fill="#ff9a5c"/><circle cx="0" cy="-236" r="13" fill="#ffd24a"/>'
assert FLAP in GOLU      # scarf bow-knot left of the collar (continuity fix 23 Nov)
GOLU = GOLU.replace(FLAP, FLAP + '<g transform="translate(-52,-220)"><ellipse cx="-17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(-18 -17 0)"/><ellipse cx="17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(18 17 0)"/><circle r="12" fill="#ffd24a" stroke="#e09400" stroke-width="3"/><circle cx="-4" cy="-4" r="4" fill="#fff6c0"/></g>')
# elbow-cover arm: a copy of the right arm drawn IN FRONT of the trunk (inside g-head, after the trunk)
ELBOW = '<g id="g-elbow" opacity="0"><ellipse cx="138" cy="-170" rx="44" ry="68" fill="url(#gLeg)" stroke="#5f7fd0" stroke-width="5" transform="rotate(-22 138 -170)"/><ellipse cx="128" cy="-128" rx="16" ry="9" fill="#ffffff" opacity=".35"/></g>'
TR_END = '<ellipse cx="70" cy="-268" rx="9" ry="6" fill="#5470c4"/>\n    </g>'
assert TR_END in GOLU
GOLU = GOLU.replace(TR_END, TR_END + ELBOW)
# Mithu with a LEAF hat (his 3rd hat: block Ep8, sand Ep9, leaf Ep10)
HAT = ('<g id="m-hat" opacity="0"><g transform="translate(18,-262) rotate(-12)"><path d="M-74,6 Q-40,-70 0,-62 Q48,-70 76,4 Q0,30 -74,6Z" fill="url(#gLeafO)"/>'
       '<path d="M-60,4 Q0,-30 64,2" stroke="#b5430f" stroke-width="5" fill="none"/><path d="M60,2 q16,-6 22,-22" stroke="#8a5a2a" stroke-width="6" fill="none" stroke-linecap="round"/>'
       '<ellipse cx="-24" cy="-38" rx="20" ry="6" fill="#fff" opacity=".45"/></g></g>')
MITHU = open(f"{HERE}/cast/mithu_src.txt").read().replace('<g id="m-beak">', HAT + '<g id="m-beak">', 1)
assert 'id="m-hat"' in MITHU
BUNNY = open(f"{HERE}/cast/bunny_v2.svg.txt").read()
BLEAF = ('<g id="b-leaf" opacity="0"><g transform="translate(-50,-470) rotate(30)"><path d="M-30,0 Q0,-34 30,0 Q0,34 -30,0Z" fill="#ffb020"/><path d="M-26,0 L26,0" stroke="#c46a00" stroke-width="4"/></g>'
         '<g transform="translate(52,-440) rotate(-40)"><path d="M-26,0 Q0,-30 26,0 Q0,30 -26,0Z" fill="#ff6a2a"/><path d="M-22,0 L22,0" stroke="#a83a00" stroke-width="4"/></g></g>')
BUNNY = BUNNY.replace('<g id="b-eyes"', BLEAF + '<g id="b-eyes"', 1) if '<g id="b-eyes"' in BUNNY else BUNNY + BLEAF
def lg(id_, stops):
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1">' + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops) + '</linearGradient>'
defs = ns["defs"] + F3D + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    rg("gBun", [(0, "#ffffff"), (.6, "#f1ecff"), (1, "#c7b8ef")], "38%", "30%", "75%"),
    rg("gBunIn", [(0, "#ffd3e2"), (1, "#f59ab9")], "45%", "40%", "70%"),
    rg("gCanopy", [(0, "#c9e86a"), (.6, "#7fbf3a"), (1, "#4f8a2e")], "40%", "30%", "75%"),
    rg("gLeafO", [(0, "#ffd36a"), (.6, "#ff9a2a"), (1, "#e0601a")], "40%", "30%", "75%"),
    rg("gPile", [(0, "#ffd27a"), (.6, "#f0942e"), (1, "#c8611c")], "45%", "30%", "75%"),
    rg("gStump", [(0, "#d9a06a"), (.6, "#a86a3a"), (1, "#7a4824")], "40%", "30%", "75%"),
    rg("gPuff", [(0, "#ffffff"), (1, "#e6f2ff")], "40%", "35%", "70%"),
    lg("gSky10", [(0, "#8fd0f5"), (.65, "#c4e7fa"), (1, "#eef8ff")]),
    lg("gGrass10", [(0, "#a8dc78"), (1, "#5ca842")]),
    lg("gHaze", [(0, "#ffffff"), (1, "#ffffff")]),
    '<filter id="fblur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>',
    '<filter id="fblur2" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.6"/></filter>',
    '<clipPath id="pileclip" clipPathUnits="userSpaceOnUse"><rect x="-400" y="0" width="1200" height="1432"/></clipPath>',
])

WORDS = [  # id, hindi, english, hi colour, en colour
    ("wAah", "आ… आ…", "Ah… ah…", "#6a1fc2", "#1565c0"),
    ("wAchoo", "आ-छी!", "ACHOO!", "#d81b3a", "#1565c0"),
    ("wHat", "मेरी टोपी! मेरी टोपी!", "My hat! My hat!", "#17702c", "#b85400"),
    ("wAah2", "आ… आ… आ…", "Ah… ah… ah…", "#6a1fc2", "#1565c0"),
    ("wAchoo2", "आ-आ-छी!!", "ACHOO!!", "#d81b3a", "#1565c0"),
    ("wWhee", "वी-ई-ई!", "Wheee!", "#c2185b", "#6a1fc2"),
    ("wUhoh", "उह-ओह!", "Uh-oh!", "#b85400", "#1565c0"),
    ("wCover", "छींक आए तो ढको!", "Cover your sneeze!", "#17702c", "#1565c0"),
    ("wHaha", "हा हा हा!", "Ha ha ha!", "#d81b3a", "#6a1fc2"),
]
def overlays():
    w = ""
    for i, hi, en, hc, ec in WORDS:
        w += f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div><div class="en" style="color:{ec}">{en}</div></div>'
    return w + '<div class="badge">गोलू मस्ती #1 · Golu Masti #1 😂</div>'

J = []
def tl(s): J.append(s)
def word_in(i, t, big=False):
    tl(f'tl.fromTo("#{i}",{{opacity:0,scale:.3}},{{opacity:1,scale:{1.08 if big else 1},duration:.32,ease:"back.out(1.8)",immediateRender:false}},{f(t)});')
    tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.05,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def word_out(i, t): tl(f'tl.to("#{i}",{{opacity:0,scale:.5,duration:.18,ease:"power2.in"}},{f(t)});')
def happy(t0, t1):
    tl(f'tl.set("#g-eyes",{{opacity:0}},{f(t0)}); tl.set("#g-happy",{{opacity:1}},{f(t0)}); tl.set("#g-eyes",{{opacity:1}},{f(t1)}); tl.set("#g-happy",{{opacity:0}},{f(t1)});')
def jump(t, h=-40):
    tl(f'tl.to("#gwrap",{{scaleY:.94,scaleX:1.04,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1}},{f(t)});')
    tl(f'tl.to("#gwrap",{{y:{h},duration:.22,ease:"power2.out",yoyo:true,repeat:1}},{f(t+.1)});')
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
def kids_cheer(t, hold=1.0):
    for k, d in (("A", 0), ("B", .07)):
        tl(f'tl.to("#k{k}-armL",{{rotation:80,duration:.18,ease:"back.out(2)"}},{f(t+d)}); tl.to("#k{k}-armR",{{rotation:-80,duration:.18,ease:"back.out(2)"}},{f(t+d+.05)});')
        tl(f'tl.to("#k{k}-armL",{{rotation:0,duration:.3,ease:"power2.inOut"}},{f(t+d+hold)}); tl.to("#k{k}-armR",{{rotation:0,duration:.3,ease:"power2.inOut"}},{f(t+d+hold+.06)});')
def kids_lean(t, hold=.8):   # blown by the gust: lean AWAY from Golu, smiling, then spring back
    for k, r, d in (("A", -7, 0), ("B", 7, .06)):
        tl(f'tl.to("#k{k}",{{rotation:{r},svgOrigin:"0 0",duration:.14,ease:"power2.out"}},{f(t+d)}); tl.to("#k{k}",{{rotation:0,svgOrigin:"0 0",duration:.5,ease:"elastic.out(1,.45)"}},{f(t+d+hold)});')
def kids_duck(t, hold):
    for k, d in (("A", 0), ("B", .08)):
        tl(f'tl.to("#k{k}",{{y:36,scaleY:.94,svgOrigin:"0 0",duration:.18,ease:"power2.out"}},{f(t+d)}); tl.to("#k{k}",{{y:0,scaleY:1,svgOrigin:"0 0",duration:.35,ease:"back.out(2)"}},{f(t+d+hold)});')
        tl(f'tl.to("#k{k}-armL",{{rotation:150,duration:.2,ease:"back.out(2)"}},{f(t+d+.03)}); tl.to("#k{k}-armR",{{rotation:-150,duration:.2,ease:"back.out(2)"}},{f(t+d+.07)});')
        tl(f'tl.to("#k{k}-armL",{{rotation:0,duration:.3}},{f(t+d+hold)}); tl.to("#k{k}-armR",{{rotation:0,duration:.3}},{f(t+d+hold+.05)});')
def bunny_cheer(t, hold=.8):
    tl(f'tl.to("#b-armL",{{rotation:120,svgOrigin:"-60 -148",duration:.18,ease:"back.out(2)"}},{f(t)}); tl.to("#b-armR",{{rotation:-120,svgOrigin:"60 -148",duration:.18,ease:"back.out(2)"}},{f(t+.06)});')
    tl(f'tl.to("#b-armL",{{rotation:0,svgOrigin:"-60 -148",duration:.3}},{f(t+hold)}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -148",duration:.3}},{f(t+hold+.06)});')

TIP = (611, 1597)                           # Golu's trunk tip on screen
MW = (880, 1250)                            # Mithu's wing (feather source)
def feather_float(t0, t1, start=MW, end=TIP):
    """feather drifts in a zig-zag from start to Golu's trunk tip"""
    n = 4; dt = (t1 - t0) / n
    tl(f'tl.set("#feather",{{opacity:1,x:{start[0]},y:{start[1]},rotation:-30}},{f(t0)});')
    for i in range(1, n + 1):
        fx = start[0] + (end[0] - start[0]) * i / n + (0 if i == n else (40 if i % 2 else -40))
        fy = start[1] + (end[1] - start[1]) * i / n
        tl(f'tl.to("#feather",{{x:{fx:.0f},y:{fy:.0f},rotation:{(-30 if i % 2 else 30) if i < n else 0},duration:{dt:.3f},ease:"sine.inOut"}},{f(t0+(i-1)*dt)});')
def feather_blow(t):
    tl(f'tl.to("#feather",{{x:{TIP[0]+260},y:{TIP[1]-900},rotation:540,duration:.7,ease:"power2.out"}},{f(t)}); tl.set("#feather",{{opacity:0}},{f(t+.7)});')
def anticip(t0, t1, amt=1.0):
    """'आ… आ…' build-up: head tilts back in steps, trunk curls up and twitches, eyes squint"""
    steps = 3 if amt > 1 else 2; dt = (t1 - t0) / steps
    for i in range(steps):
        a = (i + 1) / steps * amt
        tl(f'tl.to("#g-head",{{rotation:{-5*a:.1f},y:{-14*a:.1f},svgOrigin:"0 -240",duration:{dt*.6:.2f},ease:"power2.out"}},{f(t0+i*dt)});')
        tl(f'tl.to("#g-trunk",{{rotation:{-22*a:.1f},svgOrigin:"0 -352",duration:{dt*.5:.2f},ease:"back.out(2)"}},{f(t0+i*dt)});')
        tl(f'tl.to("#g-trunk",{{rotation:{-22*a-6:.1f},svgOrigin:"0 -352",duration:.06,yoyo:true,repeat:3}},{f(t0+i*dt+dt*.5)});')
        tl(f'tl.to("#gwrap",{{scaleY:{1+.02*a:.3f},scaleX:{1-.01*a:.3f},svgOrigin:"0 0",duration:{dt*.6:.2f},ease:"power2.out"}},{f(t0+i*dt)});')
    tl(f'tl.set("#g-eyes",{{opacity:0}},{f(t0+dt*.5)}); tl.set("#g-happy",{{opacity:1}},{f(t0+dt*.5)});')
def sneeze(t, big=1.0):
    """the snap: head + trunk whip forward, body squash, ears flare (offset), camera shake, gust lines + leaves"""
    tl(f'tl.to("#g-head",{{rotation:{6*big:.1f},y:{8*big:.1f},svgOrigin:"0 -240",duration:.08,ease:"power3.in"}},{f(t-.04)}); tl.to("#g-head",{{rotation:0,y:0,svgOrigin:"0 -240",duration:.6,ease:"elastic.out(1,.45)"}},{f(t+.2)});')
    tl(f'tl.to("#g-trunk",{{rotation:{-70*big:.0f},svgOrigin:"0 -352",duration:.08,ease:"power3.in"}},{f(t-.04)}); tl.to("#g-trunk",{{rotation:0,svgOrigin:"0 -352",duration:.6,ease:"elastic.out(1,.4)"}},{f(t+.35)});')
    tl(f'tl.to("#gwrap",{{scaleY:{1-.08*big:.3f},scaleX:{1+.04*big:.3f},svgOrigin:"0 0",duration:.08}},{f(t-.04)}); tl.to("#gwrap",{{scaleY:1,scaleX:1,svgOrigin:"0 0",duration:.5,ease:"elastic.out(1,.4)"}},{f(t+.1)});')
    tl(f'tl.to("#g-ear",{{rotation:{-26*min(big,1.1):.0f},duration:.1}},{f(t)}); tl.to("#g-ear",{{rotation:{-14*big:.0f},duration:.07,yoyo:true,repeat:5}},{f(t+.1)}); tl.to("#g-ear",{{rotation:0,duration:.35,ease:"back.out(2)"}},{f(t+.55)});')
    tl(f'tl.to("#g-ear2",{{rotation:{28*min(big,1.1):.0f},duration:.1}},{f(t+.05)}); tl.to("#g-ear2",{{rotation:{16*big:.0f},duration:.07,yoyo:true,repeat:5}},{f(t+.15)}); tl.to("#g-ear2",{{rotation:0,duration:.35,ease:"back.out(2)"}},{f(t+.62)});')
    tl(f'tl.fromTo("#cam",{{x:0,y:0}},{{x:{10*big:.0f},y:{-6*big:.0f},duration:.05,yoyo:true,repeat:5,ease:"none",immediateRender:false}},{f(t)}); tl.set("#cam",{{x:0,y:0}},{f(t+.32)});')
    tl(f'tl.set("#g-eyes",{{opacity:1}},{f(t+.45)}); tl.set("#g-happy",{{opacity:0}},{f(t+.45)});')
    tl(f'tl.fromTo("#gust",{{opacity:1,scale:.2}},{{opacity:0,scale:{1.2*big:.2f},svgOrigin:"{TIP[0]} {TIP[1]-40}",duration:.7,ease:"power2.out",immediateRender:false}},{f(t)});')
    for k in range(14):
        a = math.radians(-160 + k * (140 / 13))    # fan upward: -160°..-20° (never down into faces)
        r = (420 + (k * 71) % 260) * big
        tl(f'tl.fromTo("#lf{k}",{{opacity:1,x:{TIP[0]},y:{TIP[1]-40},rotation:0,scale:.6}},{{opacity:0,x:{TIP[0]+r*math.cos(a):.0f},y:{TIP[1]-40+r*math.sin(a):.0f},rotation:{360+k*40},scale:1.1,duration:{1.0+(k%4)*.12:.2f},ease:"power2.out",immediateRender:false}},{f(t+(k%5)*.02)});')

def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set("#wAah",{opacity:1,scale:1}); gsap.set("#gust",{opacity:0});')
    tl('gsap.set("#kA-armL",{svgOrigin:"-62 -230"}); gsap.set("#kA-armR",{svgOrigin:"62 -230"}); gsap.set("#kB-armL",{svgOrigin:"-60 -232"}); gsap.set("#kB-armR",{svgOrigin:"60 -232"});')
    tl('gsap.set("#g-ear",{svgOrigin:"-90 -380"}); gsap.set("#g-ear2",{svgOrigin:"90 -380"}); gsap.set("#g-elbow",{svgOrigin:"128 -226"});')
    tl(f'gsap.set("#feather",{{x:{TIP[0]},y:{TIP[1]},rotation:0,opacity:1}}); gsap.set("#rbunny",{{x:-2300}}); gsap.set(".lf",{{opacity:0}}); gsap.set("#hleaf",{{opacity:0}});')
    nb = int(DUR / BEAT)
    tl(f'tl.to("#g-body",{{scaleY:.96,scaleX:1.018,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#kA",{{y:-10,duration:{BEAT/2},yoyo:true,repeat:5,ease:"sine.inOut"}},0.1);')
    tl(f'tl.to("#kB",{{y:-8,duration:{BEAT/2},yoyo:true,repeat:5,ease:"sine.inOut"}},0.33);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.2);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.45);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to(".flw",{{rotation:8,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut",stagger:.1}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    tl(f'tl.to("#seat0",{{x:8,duration:1.2,yoyo:true,repeat:{int(DUR/1.2)-1},ease:"sine.inOut"}},0);')
    for i, d in enumerate([70, -60, 50]):
        tl(f'tl.fromTo("#cl{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    for k in range(12):   # slow falling leaves in the background (winter)
        x = 80 + (k * 89) % 920; t0 = (k * 2.3) % (DUR - 4)
        tl(f'tl.fromTo("#bl{k}",{{x:{x},y:820,rotation:0,opacity:.9}},{{x:{x + (40 if k%2 else -40)},y:1150,rotation:{200 if k%2 else -200},duration:3.6,ease:"sine.inOut",immediateRender:false}},{f(t0)}); tl.set("#bl{k}",{{opacity:0}},{f(t0+3.6)});')

    # ===== HOOK + SNEEZE 1
    S1 = T["S1"]
    look(10, 0, 18)   # eyes on the feather on his trunk
    anticip(0.15, CUE["a2"] + .2, 1.0)
    tl(f'tl.to("#feather",{{rotation:14,duration:.18,yoyo:true,repeat:{int(S1/.36)*2-1},ease:"sine.inOut"}},0.05);')
    word_out("wAah", S1 - .18); word_in("wAchoo", S1, True)
    sneeze(S1, 1.0); feather_blow(S1); look(0, S1 + .5)
    kids_lean(S1 + .05, .7)
    tl(f'tl.to("#m-all",{{rotation:-360,svgOrigin:"0 -100",duration:.6,ease:"power2.out"}},{f(S1+.1)}); tl.set("#m-all",{{rotation:0}},{f(S1+.71)});')
    tl(f'tl.fromTo("#mstars",{{opacity:1,rotation:0}},{{rotation:360,svgOrigin:"0 0",duration:1.2,ease:"none",immediateRender:false}},{f(S1+.7)}); tl.set("#mstars",{{opacity:0}},{f(S1+1.9)});')
    word_out("wAchoo", T["hat"] - .3)
    # a leaf from the gust floats down onto Mithu = leaf hat
    h = T["hat"]
    tl(f'tl.set("#hleaf",{{opacity:1,x:760,y:880,rotation:-40}},{f(h-1.0)}); tl.to("#hleaf",{{x:850,y:1020,rotation:20,duration:.5,ease:"sine.inOut"}},{f(h-1.0)}); tl.to("#hleaf",{{x:{MW[0]+10},y:1150,rotation:-10,duration:.5,ease:"sine.in"}},{f(h-.5)}); tl.set("#hleaf",{{opacity:0}},{f(h)}); tl.set("#m-hat",{{opacity:1}},{f(h)});')
    tl(f'tl.fromTo("#m-all",{{scaleY:1,scaleX:1}},{{scaleY:.86,scaleX:1.1,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1,immediateRender:false}},{f(h)});')
    word_in("wHat", h + .05); mithu_talk(CUE["m1"], D["m1"]); happy(h + .1, h + 1.1)
    tl(f'tl.to("#mithu",{{rotation:-8,svgOrigin:"0 -80",duration:.25,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(h+.2)});')
    look(14, h - .6, -8); look(0, E("m1"))
    word_out("wHat", E("m1") - .1)

    # ===== BIGGER MISHAP: feather again, Bunny zooms in, MEGA sneeze
    tl(f'tl.to("#m-wing",{{rotation:-30,svgOrigin:"-24 -140",duration:.1,yoyo:true,repeat:3}},{f(T["f2"])});')
    feather_float(T["f2"], CUE["b1"] - .05)
    look(12, T["f2"] + .2, -6); look(10, CUE["b1"], 18)
    word_in("wAah2", CUE["b1"]); anticip(CUE["b1"], CUE["b2"] + .3, 1.6)
    bn = T["bun"]
    tl(f'tl.fromTo("#rbunny",{{x:-2300}},{{x:0,duration:.45,ease:"power3.out",immediateRender:false}},{f(bn)});')
    tl(f'tl.set("#bspeed",{{opacity:1}},{f(bn)}); tl.fromTo("#bspeed",{{x:-300}},{{x:0,duration:.45,ease:"power3.out",immediateRender:false}},{f(bn)}); tl.set("#bspeed",{{opacity:0}},{f(bn+.5)});')
    tl(f'tl.fromTo("#rbunny",{{rotation:0}},{{rotation:14,svgOrigin:"0 0",duration:.15,ease:"power2.out",immediateRender:false}},{f(bn+.3)}); tl.to("#rbunny",{{rotation:0,svgOrigin:"0 0",duration:.4,ease:"back.out(3)"}},{f(bn+.45)});')
    tl(f'tl.to("#b-earL",{{rotation:-20,svgOrigin:"-40 -300",duration:.15}},{f(bn+.35)}); tl.to("#b-earL",{{rotation:0,svgOrigin:"-40 -300",duration:.5,ease:"elastic.out(1,.4)"}},{f(bn+.5)});')
    tl(f'tl.to("#b-earR",{{rotation:-16,svgOrigin:"44 -300",duration:.15}},{f(bn+.4)}); tl.to("#b-earR",{{rotation:0,svgOrigin:"44 -300",duration:.5,ease:"elastic.out(1,.4)"}},{f(bn+.57)});')
    S2 = T["S2"]
    word_out("wAah2", S2 - .18); word_in("wAchoo2", S2, True)
    sneeze(S2, 1.5); feather_blow(S2); kids_lean(S2 + .05, 1.0)
    tl(f'tl.to("#m-all",{{rotation:-10,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:5}},{f(S2+.05)});')   # Mithu clings on
    # Bunny spins like a top, up and down into the soft leaf pile
    tl(f'tl.to("#bhop",{{y:-260,duration:.45,ease:"power2.out"}},{f(S2+.05)}); tl.to("#bhop",{{y:0,duration:.35,ease:"power2.in"}},{f(S2+.5)});')
    tl(f'tl.fromTo("#bspin",{{rotation:0}},{{rotation:-720,svgOrigin:"0 -180",duration:.8,ease:"none",immediateRender:false}},{f(S2+.05)});')
    tl(f'tl.to("#bsink",{{opacity:0,duration:.08}},{f(T["pile"]-.04)});')
    tl(f'tl.fromTo("#pile",{{scaleY:1,scaleX:1}},{{scaleY:.8,scaleX:1.12,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1,immediateRender:false}},{f(T["pile"])});')
    for k in range(8):
        a = math.radians(-150 + k * 17)
        tl(f'tl.fromTo("#pl{k}",{{opacity:1,x:0,y:-30,rotation:0}},{{opacity:0,x:{160*math.cos(a):.0f},y:{-30+200*math.sin(a):.0f},rotation:{300+k*30},duration:.9,ease:"power2.out",immediateRender:false}},{f(T["pile"]+k*.02)});')
    word_out("wAchoo2", T["S2"] + .6); word_in("wWhee", T["S2"] + .8)
    word_out("wWhee", T["pop"] - .1)
    tl(f'tl.set("#b-leaf",{{opacity:1}},{f(T["pop"])}); tl.set("#bsink",{{opacity:1}},{f(T["pop"])}); tl.fromTo("#bsink",{{y:120}},{{y:0,duration:.3,ease:"back.out(2.5)",immediateRender:false}},{f(T["pop"])});')
    tl(f'tl.set("#b-eyes",{{opacity:0}},{f(T["pop"]+.2)}); tl.set("#b-happy",{{opacity:1}},{f(T["pop"]+.2)}); tl.set("#b-eyes",{{opacity:1}},{f(T["pop"]+1.0)}); tl.set("#b-happy",{{opacity:0}},{f(T["pop"]+1.0)});')
    bunny_cheer(T["pop"] + .25, .5); happy(T["pop"] + .2, T["pop"] + .9)
    look(-14, S2 + .3, 0); look(0, T["pop"] + .8)

    # ===== TWIST: third tickle, everyone ducks… Golu sneezes into his ELBOW
    tl(f'tl.to("#m-wing",{{rotation:-30,svgOrigin:"-24 -140",duration:.1,yoyo:true,repeat:3}},{f(T["f3"]-.3)});')
    feather_float(T["f3"] - .2, CUE["c1"] - .05)
    word_in("wUhoh", CUE["k1"] - .05); kids_talk(CUE["k1"], D["k1"]); kids_duck(CUE["k1"] + .1, E("c2") - CUE["k1"] + .1)
    tl(f'tl.to("#b-armL",{{rotation:150,svgOrigin:"-60 -148",duration:.2}},{f(CUE["k1"]+.1)}); tl.to("#b-armR",{{rotation:-150,svgOrigin:"60 -148",duration:.2}},{f(CUE["k1"]+.15)});')
    tl(f'tl.to("#b-armL",{{rotation:0,svgOrigin:"-60 -148",duration:.3}},{f(E("c2")+.2)}); tl.to("#b-armR",{{rotation:0,svgOrigin:"60 -148",duration:.3}},{f(E("c2")+.25)});')
    tl(f'tl.to("#m-wing",{{rotation:-60,svgOrigin:"-24 -140",duration:.2}},{f(CUE["k1"]+.2)}); tl.to("#m-wing",{{rotation:0,svgOrigin:"-24 -140",duration:.3}},{f(E("c2")+.2)});')
    look(10, CUE["c1"], 18); anticip(CUE["c1"], T["tuck"] + .3, .8)
    word_out("wUhoh", T["tuck"] - .1)
    tk = T["tuck"]   # the right arm comes up IN FRONT of the trunk (elbow cover)
    tl(f'tl.set("#g-armR",{{opacity:0}},{f(tk)}); tl.set("#g-elbow",{{opacity:1,rotation:0}},{f(tk)}); tl.to("#g-elbow",{{rotation:118,svgOrigin:"128 -226",duration:.3,ease:"back.out(1.6)"}},{f(tk)});')
    trunk(26, tk + .05, .3)
    tl(f'tl.set("#feather",{{opacity:0}},{f(tk+.25)});')
    S3 = T["S3"]
    tl(f'tl.to("#gwrap",{{scaleY:.97,scaleX:1.02,svgOrigin:"0 0",duration:.07,yoyo:true,repeat:1}},{f(S3-.03)}); tl.to("#g-head",{{rotation:3,y:4,svgOrigin:"0 -240",duration:.07,yoyo:true,repeat:1}},{f(S3-.03)});')
    tl(f'tl.fromTo("#tpuff",{{opacity:.9,scale:.3}},{{opacity:0,scale:1,svgOrigin:"0 0",duration:.6,ease:"power2.out",immediateRender:false}},{f(S3)});')
    tl(f'tl.to("#g-head",{{rotation:0,y:0,svgOrigin:"0 -240",duration:.4,ease:"power2.out"}},{f(S3+.3)});')
    tl(f'tl.to("#g-elbow",{{rotation:0,svgOrigin:"128 -226",duration:.3,ease:"power2.inOut"}},{f(S3+.7)}); tl.set("#g-elbow",{{opacity:0}},{f(S3+1.0)}); tl.set("#g-armR",{{opacity:1}},{f(S3+1.0)});')
    trunk(0, S3 + .7, .35, "power2.inOut")
    tl(f'tl.set("#g-eyes",{{opacity:1}},{f(S3+.4)}); tl.set("#g-happy",{{opacity:0}},{f(S3+.4)});')
    word_in("wCover", S3 + .05); look(0, S3 + .5)
    word_out("wCover", CUE["k2"] - .22)

    # ===== LAUGH
    la = T["laugh"]
    happy(la, la + 1.6); jump(la + .1); jump(la + .9, -30)
    tl(f'tl.to("#g-trunk",{{rotation:-30,svgOrigin:"0 -352",duration:.15,yoyo:true,repeat:5,ease:"sine.inOut"}},{f(la)});')
    word_in("wHaha", CUE["k2"]); kids_cheer(CUE["k2"], 1.4); kids_talk(CUE["k2"], D["k2"]); bunny_cheer(CUE["k2"] + .1, 1.2)
    tl(f'tl.fromTo("#bhop",{{y:0}},{{y:-40,duration:.18,yoyo:true,repeat:3,ease:"power2.out",immediateRender:false}},{f(CUE["k2"]+.1)});')
    mithu_talk(CUE["m2"], D["m2"])
    tl(f'tl.set(".conf",{{opacity:1}},{f(la)});')
    for k in range(24):
        x = (k * 97) % 1080
        tl(f'tl.fromTo("#cf{k}",{{x:{x},y:-80,rotation:0}},{{y:{1300 + (k*53) % 300},x:{x + ((k*37) % 160) - 80},rotation:{360 + k*20},duration:{2.6 + (k % 5)*.2:.2f},ease:"sine.in",immediateRender:false}},{f(la + (k % 8)*.08)});')
    tl(f'tl.set(".conf",{{opacity:0}},{f(la+3.8)});')
    word_out("wHaha", E("m2") - .1)
    # extra beat: Mithu's leaf hat blows up and lands back on his head
    hf, hb = T["hatfly"], T["hatback"]
    tl(f'tl.to("#m-hat",{{y:-150,rotation:-25,svgOrigin:"18 -262",duration:.45,ease:"power2.out"}},{f(hf)}); tl.to("#m-hat",{{y:0,rotation:0,svgOrigin:"18 -262",duration:.5,ease:"bounce.out"}},{f(hf+.5)});')
    tl(f'tl.to("#m-head",{{rotation:-18,svgOrigin:"18 -140",duration:.3,yoyo:true,repeat:1}},{f(hf+.1)});')
    tl(f'tl.fromTo("#m-all",{{scaleY:1,scaleX:1}},{{scaleY:.88,scaleX:1.08,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1,immediateRender:false}},{f(hb-.05)});')
    happy(hb, hb + .6); look(14, hf, -10); look(0, hb + .3)

    # ===== LOOP: Bunny zooms off, the hat floats away, a feather floats down onto the trunk = frame 1
    lp = T["loop"]
    tl(f'tl.to("#rbunny",{{x:-2100,duration:.45,ease:"power3.in"}},{f(lp-.4)});')
    tl(f'tl.to("#m-hat",{{y:-260,x:160,rotation:40,opacity:0,svgOrigin:"18 -262",duration:.8,ease:"power1.in"}},{f(lp)});')
    tl(f'tl.to("#m-wing",{{rotation:-30,svgOrigin:"-24 -140",duration:.1,yoyo:true,repeat:3}},{f(lp)});')
    feather_float(lp, DUR - .4)
    look(10, DUR - 1.2, 18)
    tl(f'tl.to("#g-trunk",{{rotation:-8,svgOrigin:"0 -352",duration:.06,yoyo:true,repeat:3}},{f(DUR-.38)});')
    tl(f'tl.fromTo("#wAah",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.3,ease:"power2.out",immediateRender:false}},{f(DUR-.35)});')
    # blinks every ~3.4 s, offset per character (not while eyes are squinting)
    bt = 2.0
    while bt < DUR - 1:
        tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{f(bt+1.1)});')
        tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{f(bt+.6)});')
        tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{f(bt+1.6)});')
        bt += 3.4
    for bt in (T["laugh"] + 2.2, T["hatback"] + 1.0):
        tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{f(bt)});')
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

LEAFC = ["#ffb020", "#ff7a2a", "#e85a1a", "#ffd34a", "#c9a227"]
def leaf(id_, c, s=1, cls="lf"):
    return f'<g class="{cls}" id="{id_}"><g transform="scale({s})"><path d="M-22,0 Q0,-24 22,0 Q0,24 -22,0Z" fill="{c}"/><path d="M-18,0 L20,0" stroke="#8a4a10" stroke-width="3" opacity=".6"/></g></g>'

def park():
    sunrays = "".join(f'<path d="M0,-92 L12,-120 L-12,-120Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    flowers = "".join(ns["flower"](x, y, c, i) for i, (x, y, c) in enumerate([(40, 1600, "#ff6b9a"), (1040, 1610, "#a66bff"), (380, 1420, "#ffc51c"), (700, 1430, "#ff6b9a")]))
    trees = "".join(f'<g transform="translate({x},{y}) scale({s})" filter="url(#fblur)"><rect x="-10" y="-20" width="20" height="60" rx="8" fill="#a8714a"/><circle cx="0" cy="-50" r="50" fill="{c}"/><circle cx="-24" cy="-64" r="16" fill="#ffe08a" opacity=".6"/></g>'
                    for x, y, s, c in [(70, 1080, .9, "#e8a43a"), (420, 1070, .7, "#8cc84a"), (760, 1075, .8, "#f0b24a"), (1010, 1085, .75, "#d9873a")])
    neem = ('<g transform="translate(560,1160)" filter="url(#fblur2)" opacity=".95"><path d="M-22,0 q8,-120 0,-220 l44,0 q-8,100 0,220z" fill="#9a6a40"/>'
            '<circle cx="0" cy="-300" r="130" fill="url(#gCanopy)"/><circle cx="-110" cy="-240" r="80" fill="url(#gCanopy)"/><circle cx="110" cy="-235" r="84" fill="url(#gCanopy)"/>'
            '<circle cx="-40" cy="-350" r="40" fill="#f6f08a" opacity=".5"/><circle cx="60" cy="-210" r="18" fill="#ffb020" opacity=".8"/><circle cx="-90" cy="-200" r="14" fill="#ff7a2a" opacity=".8"/></g>')
    swing = ('<g filter="url(#fblur2)" opacity=".9"><path d="M870,985 L840,1235 M870,985 L905,1235 M1050,985 L1020,1235 M1050,985 L1075,1235" stroke="#e85d9a" stroke-width="14" stroke-linecap="round"/>'
             '<rect x="852" y="972" width="216" height="22" rx="11" fill="#ff7ab0"/>'
             '<g id="seat0"><path d="M893,994 L893,1150 M917,994 L917,1150" stroke="#9aa6b8" stroke-width="4"/><rect x="882" y="1146" width="46" height="12" rx="5" fill="#ffd23f"/></g>'
             '<g><path d="M998,994 L998,1140 M1022,994 L1022,1140" stroke="#9aa6b8" stroke-width="4"/><rect x="987" y="1136" width="46" height="12" rx="5" fill="#3fb6ff"/></g></g>')
    ground = "".join(f'<g transform="translate({x},{y}) rotate({r})">{leaf("gl"+str(i), LEAFC[i%5], .9, "gl")}</g>' for i, (x, y, r) in enumerate(
        [(120, 1520, 20), (330, 1600, -30), (470, 1500, 60), (650, 1540, -10), (780, 1590, 40), (1000, 1520, -50), (260, 1700, 10), (840, 1720, -20), (60, 1760, 30), (1030, 1780, 70)]))
    return (f'<rect width="1080" height="1180" fill="url(#gSky10)"/>'
            f'<g transform="translate(935,220) scale(.55)"><g id="sunface">{sunrays}</g><circle r="80" fill="url(#gSun)"/>'
            f'<ellipse cx="-24" cy="-10" rx="7" ry="10" fill="#7a4a00"/><ellipse cx="24" cy="-10" rx="7" ry="10" fill="#7a4a00"/>'
            f'<path d="M-26,16 q26,24 52,0" stroke="#7a4a00" stroke-width="6" fill="none" stroke-linecap="round"/></g>'
            f'{cloud("cl0", 160, 230, .65)}{cloud("cl1", 820, 790, .5)}{cloud("cl2", 420, 760, .42)}'
            f'<g filter="url(#fblur)"><ellipse cx="220" cy="1110" rx="560" ry="150" fill="#bfe8a8"/><ellipse cx="900" cy="1120" rx="580" ry="170" fill="#b2e09a"/></g>'
            f'{trees}<rect x="0" y="960" width="1080" height="240" fill="#ffffff" opacity=".28" filter="url(#fblur)"/>'
            f'<rect x="0" y="1150" width="1080" height="770" fill="url(#gGrass10)"/>'
            f'<path d="M0,1420 Q540,1380 1080,1430 L1080,1470 Q540,1420 0,1460Z" fill="#c6ef9e" opacity=".5"/>'
            f'{neem}{swing}{ground}{flowers}')

def html():
    build()
    conf = "".join(leaf(f"cf{k}", LEAFC[k % 5], 1.1, "conf") for k in range(24))
    lfs = "".join(leaf(f"lf{k}", LEAFC[k % 5], 1.2) for k in range(14))
    bls = "".join(leaf(f"bl{k}", LEAFC[k % 5], .7, "bl") for k in range(12))
    pls = "".join(leaf(f"pl{k}", LEAFC[k % 5], 1.0, "pl") for k in range(8))
    gust = "".join(f'<path d="M{TIP[0]+40*math.cos(math.radians(a)):.0f},{TIP[1]-40+40*math.sin(math.radians(a)):.0f} L{TIP[0]+330*math.cos(math.radians(a)):.0f},{TIP[1]-40+330*math.sin(math.radians(a)):.0f}" stroke="#ffffff" stroke-width="14" stroke-linecap="round" opacity=".85"/>' for a in range(-165, -10, 22))
    bspeed = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="9" rx="4" fill="#ffffff" opacity=".85"/>' for x, y, w in [(-40, 1330, 160), (-80, 1370, 220), (-30, 1410, 140)])
    feather = ('<g id="feather"><g transform="rotate(-20) scale(1.7)"><path d="M0,-34 Q16,-10 4,30 Q-14,-6 0,-34Z" fill="#4fd65a"/><path d="M0,-30 L2,34" stroke="#1f9c3a" stroke-width="3"/>'
               '<path d="M2,-10 l10,-6 M2,4 l11,-5 M1,-4 l-9,-6 M1,12 l-9,-5" stroke="#b8ff8a" stroke-width="2"/></g></g>')
    mstars = '<g transform="translate(895,1040)"><g id="mstars" opacity="0">' + "".join(f'<path transform="rotate({a}) translate(60,0)" d="M0,-14 L4,-4 14,-4 6,3 9,14 0,7 -9,14 -6,3 -14,-4 -4,-4Z" fill="#ffd93a" stroke="#e0a000" stroke-width="2"/>' for a in (0, 120, 240)) + '</g></g>'
    pile = ('<g transform="translate(215,1440)"><g id="pile"><ellipse cx="0" cy="6" rx="150" ry="22" fill="#5a3a10" opacity=".22"/>'
            '<path d="M-150,6 Q-140,-50 -80,-62 Q-30,-96 20,-70 Q80,-90 120,-48 Q156,-24 150,6 Q0,26 -150,6Z" fill="url(#gPile)"/>'
            + "".join(f'<g transform="translate({x},{y}) rotate({r})">{leaf("pp"+str(i), LEAFC[i%5], 1.0, "pp")}</g>' for i, (x, y, r) in enumerate([(-100, -30, 20), (-50, -60, -30), (10, -62, 50), (70, -44, -20), (110, -14, 30), (-20, -20, 70), (40, -12, -60)]))
            + '<ellipse cx="-40" cy="-60" rx="40" ry="8" fill="#fff" opacity=".35"/>' + "".join(f'<g id="pl{k}w">{""}</g>' for k in range(0)) + f'{pls}</g></g>')
    stump = ('<g transform="translate(895,1462)"><ellipse cx="0" cy="8" rx="110" ry="18" fill="#3a2a10" opacity=".25"/>'
             '<path d="M-78,6 L-70,-100 Q0,-118 70,-100 L78,6 Q0,22 -78,6Z" fill="url(#gStump)"/><ellipse cx="0" cy="-100" rx="70" ry="18" fill="#e8c28a"/>'
             '<ellipse cx="0" cy="-100" rx="44" ry="11" fill="none" stroke="#b98a52" stroke-width="4"/><ellipse cx="0" cy="-100" rx="20" ry="5" fill="none" stroke="#b98a52" stroke-width="3"/>'
             '<path d="M-40,-60 q8,30 0,56" stroke="#7a4824" stroke-width="5" fill="none" opacity=".5"/></g>')
    tpuff = f'<g transform="translate({TIP[0]+40},{TIP[1]-80})"><g id="tpuff" opacity="0"><circle r="30" fill="url(#gPuff)"/><circle cx="-26" cy="8" r="20" fill="url(#gPuff)"/><circle cx="24" cy="10" r="22" fill="url(#gPuff)"/></g></g>'
    elbowicon = ('<g transform="translate(540,1000)"><g id="elbowicon" opacity="0"><circle r="74" fill="#ffffff" stroke="#17702c" stroke-width="8"/>'
                 '<path d="M-44,30 Q-20,-36 34,-20" stroke="#ff9e6b" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M34,-20 q10,-4 14,6" stroke="#ff9e6b" stroke-width="24" stroke-linecap="round" fill="none"/>'
                 '<circle cx="-8" cy="-34" r="22" fill="#ffd2b0"/><path d="M-8,-12 l0,-4" stroke="#333" stroke-width="3"/>'
                 '<text x="48" y="52" font-family="Baloo2" font-weight="800" font-size="40" fill="#17702c">✓</text></g></g>')
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}</defs>
{park()}
<g id="bls">{bls}</g>
{stump}
<g filter="url(#f3d)"><g transform="translate(895,1350) scale(-.72,.72)"><g id="mithu">{MITHU}</g></g></g>
{mstars}
<g id="bspeed" opacity="0">{bspeed}</g>
<g><g transform="translate(215,1440) scale(.45)"><g id="rbunny"><g id="bsink"><g id="bhop" filter="url(#f3d)"><g id="bspin">{BUNNY}</g></g></g></g></g></g>
{pile}
{KIDS}
<g transform="translate(540,1850) scale(.98)" filter="url(#f3d)"><g id="gwrap">{GOLU}</g></g>
{tpuff}
<g id="gust">{gust}</g>
{lfs}
<g id="hleaf">{leaf("hl", "#ff9a2a", 1.6, "hl")}</g>
{feather}
{conf}
</svg>'''
    # Mithu must sit ON the stump: stump top y≈1362; Mithu's feet are at local y≈0 → 1350. Stump is drawn after him only below his feet.
    css = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#c4e7fa}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0;transform-origin:50% 60%}
#punch{position:absolute;inset:0;transform-origin:50% 40%}
#world{position:absolute;inset:0}
.word{position:absolute;left:100px;width:880px;top:420px;text-align:center;line-height:1.08;white-space:nowrap}
.word .hi{font-size:124px;font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(0,40,90,.18)}
.word .en{font-size:86px;font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(0,40,90,.18)}
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
