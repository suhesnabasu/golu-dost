"""Golu & Dost Ep 12 — गोलू की कविता #1: एक मोटा हाथी | One Elephant Went Out to Play (traditional rhyme, own melody;
soft-3D glossy, winter park from Ep10 + NEW spider-web trampoline, friendly spider, paper elephant-ear headbands).
usage: python3 gen_episode.py <project dir>   (needs timing.json next to this file and <proj>/assets/lips.json)"""
import json, math, sys, os
PROJ = sys.argv[1]; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f"{HERE}/timing.json")); DUR = T["DUR"]; D = T["D"]; CUE = dict((k, v) for k, v in T["CUES"])
lips = json.load(open(f"{PROJ}/assets/lips.json"))
def f(v): return f"{v:.3f}"
def E(l): return CUE[l] + D[l]

# ---- v2 cast from the series template (GOLU, KIDS, f3d), glossy Mithu (Ep8-11)
tsrc = open("/home/claude/golu_pipeline/gen_episode_template.py").read()
ns = {"math": math}
exec(tsrc[tsrc.index("COLS = ["):tsrc.index("def overlays():")], ns)
rg, GOLU, KIDS, cloud = ns["rg"], ns["GOLU"], ns["KIDS"], ns["cloud"]
F3D = tsrc[tsrc.index('<filter id="f3d"'):tsrc.index('</filter>') + len('</filter>')]
FLAP = '<path d="M-12,-238 l-34,58 l52,-30z" fill="#ff9a5c"/><circle cx="0" cy="-236" r="13" fill="#ffd24a"/>'
assert FLAP in GOLU      # scarf bow-knot left of the collar (continuity fix 23 Nov)
GOLU = GOLU.replace(FLAP, FLAP + '<g transform="translate(-52,-220)"><ellipse cx="-17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(-18 -17 0)"/><ellipse cx="17" cy="0" rx="17" ry="12" fill="#ffc51c" transform="rotate(18 17 0)"/><circle r="12" fill="#ffd24a" stroke="#e09400" stroke-width="3"/><circle cx="-4" cy="-4" r="4" fill="#fff6c0"/></g>')

# ---- NEW: paper elephant-ear headbands for Pari (#kidA) and Chintu (#kidB) — pretend play, they become elephants 2 and 3
def ears(dx):
    return (f'<g class="pears"><g transform="translate({-dx},-322) rotate(-14)"><ellipse rx="64" ry="80" fill="url(#gPEar)"/><ellipse cx="-10" cy="4" rx="38" ry="52" fill="url(#gPEarIn)"/>'
            f'<path d="M-40,-60 q-14,40 0,96" stroke="#ffffff" stroke-width="6" fill="none" opacity=".45" stroke-linecap="round"/></g>'
            f'<g transform="translate({dx},-322) rotate(14)"><ellipse rx="64" ry="80" fill="url(#gPEar)"/><ellipse cx="10" cy="4" rx="38" ry="52" fill="url(#gPEarIn)"/>'
            f'<path d="M40,-60 q14,40 0,96" stroke="#ffffff" stroke-width="6" fill="none" opacity=".45" stroke-linecap="round"/></g></g>')
BAND = '<path d="M-98,-386 Q0,-486 98,-386" stroke="#6f8fe0" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M-80,-410 Q0,-478 80,-410" stroke="#c9d8ff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".8"/>'
ia, ib = KIDS.index('<g id="kA-head">'), KIDS.index('<g id="kB-head">')
A, B = KIDS[:ib], KIDS[ib:]
A = A.replace('<g id="kA-head">', '<g id="kA-head">' + ears(108), 1)
A = A.replace('<g class="kpup">', BAND + '<g class="kpup">', 1)
B = B.replace('<g id="kB-head">', '<g id="kB-head">' + ears(104), 1)
B = B.replace('<g class="kpup">', BAND + '<g class="kpup">', 1)
KIDS = A + B
# kids stand ON the web strand (web top strand y at their x): Pari x170 y1788, Chintu x930 y1780
KIDS = KIDS.replace('translate(150,1880) scale(.78)', 'translate(140,1779) scale(.76)').replace('translate(930,1880) scale(.78)', 'translate(945,1775) scale(.76)')
assert 'translate(140,1779)' in KIDS and 'translate(945,1775)' in KIDS and KIDS.count('class="pears"') == 2
KA_OPEN = '<g id="kidA" '; KB_OPEN = '<g id="kidB" '
KIDS = KIDS.replace(KA_OPEN, '<g id="enterA">' + KA_OPEN, 1).replace(KB_OPEN, '</g><g id="enterB">' + KB_OPEN, 1) + '</g>'

# Mithu with a WEB-PUFF hat (his 5th hat: block Ep8, sand Ep9, leaf Ep10, sock Ep11, web Ep12)
HAT = ('<g id="m-hat" opacity="0"><g transform="translate(18,-268)">'
       '<circle cx="-34" cy="0" r="30" fill="url(#gPuff)"/><circle cx="6" cy="-16" r="36" fill="url(#gPuff)"/><circle cx="44" cy="2" r="28" fill="url(#gPuff)"/>'
       '<path d="M-60,4 Q0,-60 70,6 M-40,-24 L52,-10 M-20,-44 L30,10 M20,-46 L-24,8" stroke="#b9d6ff" stroke-width="3" fill="none" opacity=".9"/>'
       '<ellipse cx="-6" cy="-34" rx="20" ry="7" fill="#fff" opacity=".9"/></g></g>')
MITHU = open(f"{HERE}/mithu_src.txt").read()
import re
MITHU = re.sub(r'<g id="m-hat".*?</g></g>', '', MITHU, count=1, flags=re.S) if 'id="m-hat"' in MITHU else MITHU
MITHU = MITHU.replace('<g id="m-beak">', HAT + '<g id="m-beak">', 1)
assert MITHU.count('id="m-hat"') == 1

def lg(id_, stops):
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="1">' + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops) + '</linearGradient>'
defs = ns["defs"] + F3D + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    rg("gCanopy", [(0, "#c9e86a"), (.6, "#7fbf3a"), (1, "#4f8a2e")], "40%", "30%", "75%"),
    rg("gPuff", [(0, "#ffffff"), (1, "#e3efff")], "40%", "35%", "70%"),
    rg("gPEar", [(0, "#d3e0ff"), (.55, "#a6c0f7"), (1, "#6688dd")], "38%", "30%", "75%"),
    rg("gPEarIn", [(0, "#ffd3e2"), (1, "#f59ab9")], "45%", "40%", "70%"),
    rg("gSpider", [(0, "#d9b3ff"), (.55, "#9a5ce6"), (1, "#5f2aa8")], "36%", "28%", "75%"),
    lg("gSky10", [(0, "#8fd0f5"), (.65, "#c4e7fa"), (1, "#eef8ff")]),
    lg("gGrass10", [(0, "#a8dc78"), (1, "#5ca842")]),
    '<filter id="fblur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>',
    '<filter id="fblur2" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.6"/></filter>',
    '<filter id="fglow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>',
])

WORDS = [  # id, hindi, english, hi colour, en colour
    ("wTitle", "एक मोटा हाथी", "One Elephant", "#6a1fc2", "#1565c0"),
    ("wWeb", "मकड़ी का जाला", "Spider's web", "#8a2be2", "#1565c0"),
    ("wFun", "इतना मज़ा!", "Such fun!", "#d81b3a", "#1565c0"),
    ("wCome", "आ जा!", "Come!", "#17702c", "#b85400"),
    ("wTwo", "दो हाथी", "Two elephants", "#c2185b", "#1565c0"),
    ("wWeb2", "मकड़ी का जाला", "Spider's web", "#8a2be2", "#1565c0"),
    ("wFun2", "इतना मज़ा!", "Such fun!", "#d81b3a", "#1565c0"),
    ("wCome2", "आ जा!", "Come!", "#17702c", "#b85400"),
    ("wThree", "तीन हाथी", "Three elephants", "#e65100", "#1565c0"),
    ("wJump", "एक, दो, तीन — कूदो!", "One, two, three — Jump!", "#6a1fc2", "#1565c0"),
    ("wBoing", "बोइंग!", "BOING!", "#d81b3a", "#1565c0"),
    ("wHat", "मेरी टोपी!", "My hat! My hat!", "#17702c", "#b85400"),
    ("wWell", "शाबाश!", "Well done!", "#e65100", "#1565c0"),
    ("wCount", "एक, दो, तीन!", "One, two, three!", "#6a1fc2", "#c2185b"),
    ("wFour", "चौथा हाथी… तुम?", "Number four — you!", "#c2185b", "#1565c0"),
    ("wBye", "कल फिर मिलेंगे!", "See you tomorrow!", "#17702c", "#1565c0"),
]
NB = [("nb1", "1", "एक", "One", 430, 1030, "#6a1fc2"), ("nb2", "2", "दो", "Two", 30, 1150, "#c2185b"), ("nb3", "3", "तीन", "Three", 835, 1150, "#e65100")]
def overlays():
    w = ""
    for i, hi, en, hc, ec in WORDS:
        w += f'<div class="word" id="{i}"><div class="hi" style="color:{hc}">{hi}</div><div class="en" style="color:{ec}">{en}</div></div>'
    for i, n, hi, en, x, y, c in NB:
        w += f'<div class="nb" id="{i}" style="left:{x}px;top:{y}px"><div class="nbn" style="background:{c}">{n}</div><div class="nbw" style="color:{c}">{hi} · {en}</div></div>'
    return w + '<div class="badge">गोलू की कविता #1 · Golu\'s Rhymes #1 🎵</div>'

J = []
def tl(s): J.append(s)
def word_in(i, t, big=False):
    tl(f'tl.fromTo("#{i}",{{opacity:0,scale:.3}},{{opacity:1,scale:{1.08 if big else 1},duration:.32,ease:"back.out(1.8)",immediateRender:false}},{f(t)});')
    tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.04,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def word_out(i, t): tl(f'tl.to("#{i}",{{opacity:0,scale:.5,duration:.18,ease:"power2.in"}},{f(t)});')
def nb_in(i, t): tl(f'tl.fromTo("#{i}",{{opacity:0,scale:.2,y:30}},{{opacity:1,scale:1,y:0,duration:.4,ease:"back.out(2.2)",immediateRender:false}},{f(t)});')
def nb_out(i, t): tl(f'tl.to("#{i}",{{opacity:0,scale:.4,duration:.16,ease:"power2.in"}},{f(t)});')
def nb_flash(i, t): tl(f'tl.fromTo("#{i}",{{scale:1}},{{scale:1.3,duration:.14,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{f(t)});')
def happy(t0, t1):
    tl(f'tl.set("#g-eyes",{{opacity:0}},{f(t0)}); tl.set("#g-happy",{{opacity:1}},{f(t0)}); tl.set("#g-eyes",{{opacity:1}},{f(t1)}); tl.set("#g-happy",{{opacity:0}},{f(t1)});')
def look(x, t, y=0): tl(f'tl.to(".pup",{{x:{x},y:{y},duration:.2,ease:"power2.out"}},{f(t)});')
def trunk(rot, t, d=.25, ease="back.out(2)"): tl(f'tl.to("#g-trunk",{{rotation:{rot},svgOrigin:"0 -352",duration:{d},ease:"{ease}"}},{f(t)});')
def beckon(t, n=2):
    for k in range(n):
        trunk(-38, t + k * .5, .2); trunk(8, t + k * .5 + .25, .2, "power2.inOut")
    trunk(0, t + n * .5, .25, "power2.out")
def web_dip(t, amt=.08, hold=.12):
    tl(f'tl.to("#webs",{{scaleY:{1+amt:.3f},svgOrigin:"540 1660",duration:{hold},ease:"power2.out",overwrite:"auto"}},{f(t)}); tl.to("#webs",{{scaleY:1,svgOrigin:"540 1660",duration:.8,ease:"elastic.out(1,.3)",overwrite:"auto"}},{f(t+hold)});')
def bounce(who, t, h=60, amt=.08, sq=.9):
    """land/push on the web at t: squash + web dips, then spring up h px and land back at t+.8"""
    sel = {"g": "#gwrap", "a": "#kA", "b": "#kB"}[who]
    dip = {"g": 180, "a": 90, "b": 90}[who] * amt
    tl(f'tl.to("{sel}",{{y:{dip:.0f},scaleY:{sq},scaleX:{2-sq:.2f},svgOrigin:"0 0",duration:.12,ease:"power2.out"}},{f(t)});')
    tl(f'tl.to("{sel}",{{y:{-h},scaleY:1.04,scaleX:.97,svgOrigin:"0 0",duration:.34,ease:"power2.out"}},{f(t+.12)});')
    tl(f'tl.to("{sel}",{{y:0,scaleY:1,scaleX:1,svgOrigin:"0 0",duration:.3,ease:"power2.in"}},{f(t+.46)});')
    web_dip(t, amt)
def mithu_talk(t, dur):
    n = max(1, int(round(dur / 0.5)))
    tl(f'tl.to("#m-head",{{rotation:-10,svgOrigin:"18 -140",duration:.25,yoyo:true,repeat:{2*n-1},ease:"sine.inOut"}},{f(t)});')
    tl(f'tl.to("#m-jaw",{{y:8,duration:.125,yoyo:true,repeat:{4*n-1}}},{f(t)});')
    tl(f'tl.to("#m-all",{{y:-20,duration:.25,yoyo:true,repeat:{2*n-1},ease:"power2.out"}},{f(t)});')
def kids_talk(t, dur, who=("A", "B")):
    for k, d in (("A", 0), ("B", .05)):
        if k not in who: continue
        n = int(dur / .11)
        tl(f'tl.set("#kid{k} .ksmile",{{opacity:0}},{f(t+d)});')
        for j in range(n):
            big = j % 2 == 0
            tl(f'tl.set("#kid{k} .kmouth",{{opacity:{1 if big else 0}}},{f(t+d+j*.11)}); tl.set("#kid{k} .ksmall",{{opacity:{0 if big else 1}}},{f(t+d+j*.11)});')
        tl(f'tl.set("#kid{k} .kmouth",{{opacity:0}},{f(t+d+n*.11)}); tl.set("#kid{k} .ksmall",{{opacity:0}},{f(t+d+n*.11)}); tl.set("#kid{k} .ksmile",{{opacity:1}},{f(t+d+n*.11)});')
def kids_cheer(t, hold=1.0, who=("A", "B"), amt=80):
    for k, d in (("A", 0), ("B", .07)):
        if k not in who: continue
        tl(f'tl.to("#k{k}-armL",{{rotation:{amt},duration:.18,ease:"back.out(2)"}},{f(t+d)}); tl.to("#k{k}-armR",{{rotation:{-amt},duration:.18,ease:"back.out(2)"}},{f(t+d+.05)});')
        tl(f'tl.to("#k{k}-armL",{{rotation:0,duration:.3,ease:"power2.inOut"}},{f(t+d+hold)}); tl.to("#k{k}-armR",{{rotation:0,duration:.3,ease:"power2.inOut"}},{f(t+d+hold+.06)});')
def kid_point(k, t, hold, side):   # one arm points toward the camera/centre
    arm, rot = (f"#k{k}-armR", -60) if side > 0 else (f"#k{k}-armL", 60)
    tl(f'tl.to("{arm}",{{rotation:{rot},duration:.2,ease:"back.out(2)"}},{f(t)}); tl.to("{arm}",{{rotation:0,duration:.3,ease:"power2.inOut"}},{f(t+hold)});')
def run_in(k, t, frm):
    tl(f'tl.fromTo("#enter{k}",{{x:{frm}}},{{x:0,duration:.6,ease:"power2.out",immediateRender:false}},{f(t)});')
    for j in range(3):
        tl(f'tl.to("#k{k}",{{y:-46,duration:.1,ease:"power2.out",yoyo:true,repeat:1}},{f(t+j*.2)});')
    tl(f'tl.fromTo("#k{k}-head",{{rotation:{6 if frm < 0 else -6}}},{{rotation:0,svgOrigin:"0 -250",duration:.5,ease:"elastic.out(1,.4)",immediateRender:false}},{f(t+.55)});')
def hop_out(k, t, to):
    tl(f'tl.to("#k{k}",{{y:-60,duration:.15,ease:"power2.out",yoyo:true,repeat:1}},{f(t)}); tl.to("#enter{k}",{{x:{to},duration:.55,ease:"power2.in"}},{f(t+.05)});')

SP = (300, 1010)    # spider on its thread (screen)
PUFF_TO = (949, 818)  # Mithu's head (swing top bar) — hat lands here

def build():
    tl('gsap.set(".word",{opacity:0,scale:.3}); gsap.set("#wTitle",{opacity:1,scale:1.08}); gsap.set(".nb",{opacity:0});')
    tl('gsap.set("#kA-armL",{svgOrigin:"-62 -230"}); gsap.set("#kA-armR",{svgOrigin:"62 -230"}); gsap.set("#kB-armL",{svgOrigin:"-60 -232"}); gsap.set("#kB-armR",{svgOrigin:"60 -232"});')
    tl('gsap.set("#g-ear",{svgOrigin:"-90 -380"}); gsap.set("#g-ear2",{svgOrigin:"90 -380"});')
    tl(f'gsap.set("#enterA",{{x:-520}}); gsap.set("#enterB",{{x:520}}); gsap.set("#gwrap",{{y:-70}}); gsap.set("#wpuff",{{opacity:0,x:540,y:1700}});')
    nb = int(DUR / BEAT)
    tl(f'tl.to("#g-body",{{scaleY:.965,scaleX:1.015,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.2);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},0.45);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to(".flw",{{rotation:8,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut",stagger:.1}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    tl(f'tl.to("#spsway",{{rotation:6,svgOrigin:"{SP[0]} 0",duration:1.0,yoyo:true,repeat:{int(DUR)-1},ease:"sine.inOut"}},0);')
    for i, d in enumerate([70, -60, 50]):
        tl(f'tl.fromTo("#cl{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    for k in range(10):   # slow falling leaves in the background (winter park)
        x = 80 + (k * 97) % 920; t0 = (k * 2.9) % (DUR - 4)
        tl(f'tl.fromTo("#bl{k}",{{x:{x},y:820,rotation:0,opacity:.9}},{{x:{x + (40 if k%2 else -40)},y:1150,rotation:{200 if k%2 else -200},duration:3.6,ease:"sine.inOut",immediateRender:false}},{f(t0)}); tl.set("#bl{k}",{{opacity:0}},{f(t0+3.6)});')

    # ===== HOOK: Golu drops onto the web — BOING (frame 1 = Golu in the air + title card)
    l0 = T["land0"]
    tl(f'tl.to("#gwrap",{{y:0,duration:{l0},ease:"power2.in"}},0);')
    tl(f'tl.to("#gwrap",{{y:16,scaleY:.9,scaleX:1.08,svgOrigin:"0 0",duration:.1,ease:"power2.out"}},{f(l0)}); tl.to("#gwrap",{{y:0,scaleY:1,scaleX:1,svgOrigin:"0 0",duration:.45,ease:"elastic.out(1,.4)"}},{f(l0+.1)});')
    web_dip(l0, .1)
    nb_in("nb1", CUE["a1"] + .1)
    # verse 1: sway (झूम), bounce/swing, fun, call
    a1, a1e = CUE["a1"], E("a1")
    tl(f'tl.to("#gwrap",{{rotation:-6,svgOrigin:"0 0",duration:.45,ease:"sine.inOut"}},{f(a1+.1)});')
    k = 0; t = a1 + .55
    while t < a1e + .3:
        tl(f'tl.to("#gwrap",{{rotation:{6 if k%2==0 else -6},svgOrigin:"0 0",duration:.5,ease:"sine.inOut"}},{f(t)});'); k += 1; t += .5
    tl(f'tl.to("#gwrap",{{rotation:0,svgOrigin:"0 0",duration:.3,ease:"sine.out"}},{f(t)});')
    tl(f'tl.to("#g-ear",{{rotation:-10,duration:.25,yoyo:true,repeat:3}},{f(a1+.2)}); tl.to("#g-ear2",{{rotation:12,duration:.25,yoyo:true,repeat:3}},{f(a1+.35)});')
    mithu_talk(CUE["m0"], D["m0"]); nb_flash("nb1", CUE["m0"] + .05); nb_flash("nb1", CUE["m0"] + D["m0"] * .55)
    word_out("wTitle", CUE["a2"] - .2); word_in("wWeb", CUE["a2"])
    sw = T["swing"]
    for j in range(3):
        bounce("g", sw + .2 + j * .85, 50 + 10 * j)
    tl(f'tl.to("#spdrop",{{y:60,duration:.5,ease:"sine.inOut",yoyo:true,repeat:1}},{f(sw+.2)}); tl.to("#sp-legR",{{rotation:-40,svgOrigin:"18 0",duration:.18,yoyo:true,repeat:5}},{f(sw+.3)});')
    look(-16, sw, -12); look(0, E("a2"))
    word_out("wWeb", CUE["a3"] - .2); word_in("wFun", CUE["a3"])
    happy(CUE["a3"] + .05, E("a3") + .1)
    tl(f'tl.to("#g-trunk",{{rotation:-26,svgOrigin:"0 -352",duration:.16,yoyo:true,repeat:5,ease:"sine.inOut"}},{f(CUE["a3"]+.1)});')
    bounce("g", CUE["a3"] + .3, 40, .06)
    word_out("wFun", CUE["a4"] - .2)
    c1 = T["call1"]
    look(-22, c1, 0)
    tl(f'tl.to("#gwrap",{{rotation:-5,svgOrigin:"0 0",duration:.3,ease:"power2.out"}},{f(c1)}); tl.to("#gwrap",{{rotation:0,svgOrigin:"0 0",duration:.4,ease:"power2.inOut"}},{f(E("a4")+.2)});')
    beckon(c1 + D["a4"] * .45, 2)
    word_in("wCome", CUE["a4"] + D["a4"] * .3)
    # Pari runs in with paper ears — elephant #2
    word_out("wCome", T["pari"] + .25)
    run_in("A", T["pari"], -520); web_dip(T["pland"], .05)
    nb_in("nb2", T["pland"]); word_in("wTwo", CUE["b1"])
    kids_talk(CUE["b1"], D["b1"], ("A",)); kids_cheer(CUE["b1"] + .1, .8, ("A",))
    happy(T["pland"], T["pland"] + .8); look(-12, T["pland"]); look(0, E("b1"))
    # verse 2 (English): bounce in turns
    e1 = T["e1"]
    kids_talk(e1, E("e2") - e1, ("A",))
    for j in range(4):
        bounce("g" if j % 2 == 0 else "a", e1 + .1 + j * .55 * 1.0, 46 if j % 2 == 0 else 54)
    word_out("wTwo", CUE["e2"] - .15); word_in("wWeb2", CUE["e2"])
    kid_point("A", CUE["e2"] + .1, 1.1, -1)
    tl(f'tl.to("#sp-legR",{{rotation:-40,svgOrigin:"18 0",duration:.18,yoyo:true,repeat:5}},{f(CUE["e2"]+.2)}); tl.to("#spdrop",{{y:40,duration:.4,ease:"sine.inOut",yoyo:true,repeat:1}},{f(CUE["e2"]+.1)});')
    look(-18, CUE["e2"] + .1, -14); look(0, E("e2"))
    word_out("wWeb2", CUE["e3"] - .15); word_in("wFun2", CUE["e3"])
    kids_talk(CUE["e3"], E("e4") - CUE["e3"], ("A",))
    happy(CUE["e3"] + .05, E("e3") + .2); kids_cheer(CUE["e3"] + .1, .9, ("A",))
    bounce("a", CUE["e3"] + .15, 44); bounce("g", CUE["e3"] + .7, 40, .06)
    tl(f'tl.to("#g-trunk",{{rotation:-30,svgOrigin:"0 -352",duration:.15,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(CUE["e3"]+.1)});')
    word_out("wFun2", CUE["e4"] - .15)
    c2 = T["call2"]
    look(22, c2, 0)
    tl(f'tl.to("#gwrap",{{rotation:5,svgOrigin:"0 0",duration:.3,ease:"power2.out"}},{f(c2)}); tl.to("#gwrap",{{rotation:0,svgOrigin:"0 0",duration:.4,ease:"power2.inOut"}},{f(E("e4")+.2)});')
    beckon(c2 + D["e4"] * .4, 2); kid_point("A", c2 + .3, 1.2, 1)
    word_in("wCome2", E("e4") - .55)
    # Chintu runs in — elephant #3
    word_out("wCome2", T["chintu"] + .25)
    run_in("B", T["chintu"], 520); web_dip(T["cland"], .05)
    nb_in("nb3", T["cland"]); word_in("wThree", CUE["c1"])
    kids_talk(CUE["c1"], D["c1"], ("B",)); kids_cheer(CUE["c1"] + .1, .8, ("B",))
    happy(T["cland"], T["cland"] + .8); look(14, T["cland"]); look(0, E("c1"))
    # count + crouch + the BIG BOING
    word_out("wThree", CUE["c2"] - .15); word_in("wJump", CUE["c2"], True)
    cn = T["count"]
    for j, i in enumerate(("nb1", "nb2", "nb3")):
        nb_flash(i, cn + D["c2"] * (.05 + .22 * j))
    bo = T["boing"]
    for i in ("nb1", "nb2", "nb3"): nb_out(i, bo - .35)
    for sel, d in (("#gwrap", 0), ("#kA", .04), ("#kB", .08)):   # anticipation crouch
        tl(f'tl.to("{sel}",{{y:30,scaleY:.86,scaleX:1.1,svgOrigin:"0 0",duration:.3,ease:"power2.out"}},{f(bo-.35+d)});')
    tl(f'tl.to("#webs",{{scaleY:1.2,svgOrigin:"540 1660",duration:.3,ease:"power2.out"}},{f(bo-.35)});')
    word_out("wJump", bo - .1); word_in("wBoing", bo, True)
    tl(f'tl.to("#webs",{{scaleY:.82,svgOrigin:"540 1660",duration:.12,ease:"power3.in"}},{f(bo-.05)}); tl.to("#webs",{{scaleY:1,svgOrigin:"540 1660",duration:1.2,ease:"elastic.out(1,.25)"}},{f(bo+.07)});')
    for sel, h, d in (("#gwrap", 150, 0), ("#kA", 150, .05), ("#kB", 140, .1)):
        tl(f'tl.to("{sel}",{{y:{-h},scaleY:1.08,scaleX:.94,svgOrigin:"0 0",duration:.42,ease:"power2.out"}},{f(bo-.05+d)});')
        tl(f'tl.to("{sel}",{{y:0,scaleY:1,scaleX:1,svgOrigin:"0 0",duration:.36,ease:"power2.in"}},{f(bo+.37+d)});')
        tl(f'tl.to("{sel}",{{scaleY:.93,scaleX:1.05,svgOrigin:"0 0",duration:.08,yoyo:true,repeat:1}},{f(bo+.73+d)});')
    web_dip(bo + .75, .06)
    happy(bo, bo + 1.2); kids_cheer(bo, 1.0)
    tl(f'tl.to("#g-ear",{{rotation:-24,duration:.12,yoyo:true,repeat:3}},{f(bo)}); tl.to("#g-ear2",{{rotation:26,duration:.12,yoyo:true,repeat:3}},{f(bo+.06)});')
    tl(f'tl.fromTo("#cam",{{y:0}},{{y:-8,duration:.05,yoyo:true,repeat:5,ease:"none",immediateRender:false}},{f(bo+.78)}); tl.set("#cam",{{y:0}},{f(bo+1.1)});')
    tl(f'tl.to("#spdrop",{{y:-90,duration:.3,ease:"power2.out",yoyo:true,repeat:1}},{f(bo)});')
    # a fluffy web puff flies up… and lands on Mithu = hat #5
    h = T["hat"]
    tl(f'tl.set("#wpuff",{{opacity:1,x:540,y:1700,scale:.6}},{f(bo)}); tl.to("#wpuff",{{x:800,y:760,scale:1,rotation:120,duration:.8,ease:"power2.out"}},{f(bo)});')
    tl(f'tl.to("#wpuff",{{x:{PUFF_TO[0]},y:{PUFF_TO[1]-10},rotation:200,duration:{h-bo-.8:.2f},ease:"sine.in"}},{f(bo+.8)}); tl.set("#wpuff",{{opacity:0}},{f(h)}); tl.set("#m-hat",{{opacity:1}},{f(h)});')
    tl(f'tl.fromTo("#m-all",{{scaleY:1,scaleX:1}},{{scaleY:.86,scaleX:1.1,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:1,immediateRender:false}},{f(h)});')
    look(18, bo + .9, -22); look(0, E("m1"))
    word_out("wBoing", h - .4); word_in("wHat", h - .15)
    mithu_talk(CUE["m1"], D["m1"])
    tl(f'tl.to("#mithu",{{rotation:-8,svgOrigin:"0 -80",duration:.25,yoyo:true,repeat:3,ease:"sine.inOut"}},{f(h+.2)});')
    happy(h + .2, E("m1")); kids_cheer(h + .25, 1.0)
    # शाबाश + recap 1-2-3
    word_out("wHat", CUE["s1"] - .15); word_in("wWell", CUE["s1"])
    happy(CUE["s1"], E("s1")); tl(f'tl.to("#g-trunk",{{rotation:-34,svgOrigin:"0 -352",duration:.2,yoyo:true,repeat:1}},{f(CUE["s1"]+.1)});')
    bounce("g", CUE["s1"] + .2, 40, .05)
    word_out("wWell", CUE["d1"] - .15); word_in("wCount", CUE["d1"])
    rc = T["recap"]
    for j, (i, who) in enumerate((("nb1", "g"), ("nb2", "a"), ("nb3", "b"))):
        tj = rc + D["d1"] * (.02 + .3 * j)
        nb_in(i, tj); bounce(who, tj, 36, .05)
    kids_talk(rc, D["d1"])
    # tease: elephant number four… YOU?
    word_out("wCount", CUE["g1"] - .15); word_in("wFour", CUE["g1"])
    for i in ("nb1", "nb2", "nb3"): nb_out(i, CUE["g1"] - .1)
    fo = T["four"]
    look(0, fo, 10); trunk(24, fo + D["g1"] * .5, .3)
    tl(f'tl.fromTo("#cam",{{scale:1}},{{scale:1.06,duration:.5,ease:"power2.out",immediateRender:false}},{f(fo+D["g1"]*.5)}); tl.to("#cam",{{scale:1,duration:.5,ease:"power2.inOut"}},{f(E("g2")+.1)});')
    trunk(0, E("g2"), .3, "power2.inOut")
    kids_talk(CUE["g2"], D["g2"]); kid_point("A", CUE["g2"] + .05, D["g2"], 1); kid_point("B", CUE["g2"] + .1, D["g2"], -1)
    word_out("wFour", CUE["g3"] - .15); word_in("wBye", CUE["g3"])
    happy(CUE["g3"] + .1, E("g3") + .2)
    tl(f'tl.to("#g-armR",{{rotation:-50,svgOrigin:"128 -226",duration:.2,yoyo:true,repeat:3}},{f(CUE["g3"]+.1)});')
    kids_cheer(CUE["g3"] + .05, .6)
    ex = T["exit"]
    hop_out("A", ex, -560); hop_out("B", ex + .15, 560)
    mithu_talk(CUE["g4"], D["g4"])
    word_out("wBye", DUR - 1.0)
    tl(f'tl.to("#m-hat",{{y:-200,x:120,rotation:40,opacity:0,svgOrigin:"18 -268",duration:.8,ease:"power1.in"}},{f(DUR-1.2)});')
    # LOOP: Golu alone bounces up — back to frame 1 (in the air, title card)
    look(0, DUR - 1.6, 0)
    bounce("g", DUR - 1.4, 44, .06)
    tl(f'tl.to("#gwrap",{{y:-70,duration:.36,ease:"power2.out"}},{f(DUR-.38)});')
    tl(f'tl.fromTo("#wTitle",{{opacity:0,scale:.5}},{{opacity:1,scale:1.08,duration:.3,ease:"power2.out",immediateRender:false}},{f(DUR-.35)});')
    # blinks every ~3.4 s, offset per character
    bt = 1.6
    while bt < DUR - 1:
        tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{f(bt+1.1)});')
        tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{f(bt+.6)});')
        tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{f(bt+1.6)});')
        tl(f'tl.to("#sp-eyes",{{scaleY:.1,svgOrigin:"0 -6",duration:.06,yoyo:true,repeat:1}},{f(bt+2.3)});')
        bt += 3.4
    for bt in (E("a2") + .4, E("c1") + .6, E("g2") + .3):
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

LEAFC = ["#ffb020", "#ff7a2a", "#e85a1a", "#ffd34a", "#c9a227"]
def leaf(id_, c, s=1, cls="lf"):
    return f'<g class="{cls}" id="{id_}"><g transform="scale({s})"><path d="M-22,0 Q0,-24 22,0 Q0,24 -22,0Z" fill="{c}"/><path d="M-18,0 L20,0" stroke="#8a4a10" stroke-width="3" opacity=".6"/></g></g>'

def park():
    sunrays = "".join(f'<path d="M0,-92 L12,-120 L-12,-120Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    flowers = "".join(ns["flower"](x, y, c, i) for i, (x, y, c) in enumerate([(380, 1440, "#ffc51c"), (700, 1450, "#ff6b9a"), (60, 1500, "#a66bff"), (1020, 1520, "#ff6b9a")]))
    trees = "".join(f'<g transform="translate({x},{y}) scale({s})" filter="url(#fblur)"><rect x="-10" y="-20" width="20" height="60" rx="8" fill="#a8714a"/><circle cx="0" cy="-50" r="50" fill="{c}"/><circle cx="-24" cy="-64" r="16" fill="#ffe08a" opacity=".6"/></g>'
                    for x, y, s, c in [(70, 1080, .9, "#e8a43a"), (420, 1070, .7, "#8cc84a"), (760, 1075, .8, "#f0b24a"), (1010, 1085, .75, "#d9873a")])
    neem = ('<g transform="translate(560,1160)" filter="url(#fblur2)" opacity=".95"><path d="M-22,0 q8,-120 0,-220 l44,0 q-8,100 0,220z" fill="#9a6a40"/>'
            '<circle cx="0" cy="-300" r="130" fill="url(#gCanopy)"/><circle cx="-110" cy="-240" r="80" fill="url(#gCanopy)"/><circle cx="110" cy="-235" r="84" fill="url(#gCanopy)"/>'
            '<circle cx="-40" cy="-350" r="40" fill="#f6f08a" opacity=".5"/><circle cx="60" cy="-210" r="18" fill="#ffb020" opacity=".8"/><circle cx="-90" cy="-200" r="14" fill="#ff7a2a" opacity=".8"/></g>')
    swing = ('<g filter="url(#fblur2)" opacity=".92"><path d="M870,985 L840,1235 M870,985 L905,1235 M1050,985 L1020,1235 M1050,985 L1075,1235" stroke="#e85d9a" stroke-width="14" stroke-linecap="round"/>'
             '<rect x="852" y="972" width="216" height="22" rx="11" fill="#ff7ab0"/>'
             '<g><path d="M893,994 L893,1150 M917,994 L917,1150" stroke="#9aa6b8" stroke-width="4"/><rect x="882" y="1146" width="46" height="12" rx="5" fill="#ffd23f"/></g>'
             '<g><path d="M998,994 L998,1140 M1022,994 L1022,1140" stroke="#9aa6b8" stroke-width="4"/><rect x="987" y="1136" width="46" height="12" rx="5" fill="#3fb6ff"/></g></g>')
    ground = "".join(f'<g transform="translate({x},{y}) rotate({r})">{leaf("gl"+str(i), LEAFC[i%5], .9, "gl")}</g>' for i, (x, y, r) in enumerate(
        [(120, 1480, 20), (330, 1560, -30), (470, 1470, 60), (650, 1520, -10), (780, 1560, 40), (1000, 1480, -50)]))
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

def qpt(t, c):   # point on Q bezier from (-80,1660) ctrl (540,c) to (1160,1660)
    x = -80 + 1240 * t; y = 1660 * (1 - t) ** 2 + 2 * c * t * (1 - t) + 1660 * t * t
    return x, y
def web():
    """NEW prop: a friendly spider web strung low across the park like a trampoline-hammock (top strand = where everyone stands)"""
    ctr = [2056, 2150, 2250, 2350]
    s = '<ellipse cx="540" cy="1905" rx="560" ry="28" fill="#2e6a20" opacity=".18"/>'
    for i, c in enumerate(ctr):
        d = f"M-80,1660 Q540,{c} 1160,1660"
        s += f'<path d="{d}" stroke="#7fa8e0" stroke-width="{13-2*i}" fill="none" opacity=".45"/><path d="{d}" stroke="#ffffff" stroke-width="{8-1.5*i:.1f}" fill="none" opacity=".95"/>'
    for t in [k / 14 for k in range(1, 14)]:   # cross threads fan downward like web spokes
        x0, y0 = qpt(t, ctr[0]); x3, y3 = qpt(.5 + (t - .5) * 1.15, ctr[-1])
        s += f'<path d="M{x0:.0f},{y0:.0f} L{x3:.0f},{y3:.0f}" stroke="#ffffff" stroke-width="4" opacity=".8"/>'
    for k, (t, c) in enumerate([(.3, ctr[0]), (.62, ctr[1]), (.48, ctr[2])]):   # dew sparkles
        x, y = qpt(t, c)
        s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#e8f6ff"/><circle cx="{x-2:.0f}" cy="{y-2:.0f}" r="3" fill="#ffffff"/>'
    sheen = '<g id="web-sheen" opacity=".55"><path d="M-300,1660 l120,0 l-60,300 l-120,0z" fill="#ffffff" filter="url(#fglow)"/></g>'
    clip = '<clipPath id="webclip" clipPathUnits="userSpaceOnUse"><path d="M-80,1650 Q540,2046 1160,1650 L1160,1700 Q540,2366 -80,1700Z"/></clipPath>'
    return f'<defs>{clip}</defs><g id="webs">{s}</g>'

def spider():
    """NEW friendly spider (मकड़ी): tiny, round, purple, big glossy eyes, smile, 6 short stubby legs; dangles on a thread"""
    x, y = SP
    legs = ""
    for i, (a, l) in enumerate([(-30, 30), (0, 34), (30, 30)]):
        legs += f'<path d="M-24,{-2+i*10} q-{l},{-10+i*6} -{l+8},{10+i*8}" stroke="#5f2aa8" stroke-width="8" fill="none" stroke-linecap="round"/>'
        if i != 0:
            legs += f'<path d="M24,{-2+i*10} q{l},{-10+i*6} {l+8},{10+i*8}" stroke="#5f2aa8" stroke-width="8" fill="none" stroke-linecap="round"/>'
    wave = '<g id="sp-legR"><path d="M24,-2 q30,-10 38,-36" stroke="#5f2aa8" stroke-width="8" fill="none" stroke-linecap="round"/><circle cx="62" cy="-38" r="6" fill="#5f2aa8"/></g>'
    body = (f'<ellipse cx="0" cy="8" rx="34" ry="30" fill="url(#gSpider)"/><circle cx="0" cy="-22" r="26" fill="url(#gSpider)"/>'
            f'<g id="sp-eyes"><ellipse cx="-10" cy="-26" rx="9" ry="11" fill="#fff"/><ellipse cx="10" cy="-26" rx="9" ry="11" fill="#fff"/>'
            f'<circle cx="-8" cy="-24" r="5" fill="#2a1a2e"/><circle cx="12" cy="-24" r="5" fill="#2a1a2e"/><circle cx="-6" cy="-27" r="2" fill="#fff"/><circle cx="14" cy="-27" r="2" fill="#fff"/></g>'
            f'<ellipse cx="-18" cy="-12" rx="6" ry="4" fill="#ff8fd0" opacity=".8"/><ellipse cx="18" cy="-12" rx="6" ry="4" fill="#ff8fd0" opacity=".8"/>'
            f'<path d="M-8,-10 q8,8 16,0" stroke="#3a1060" stroke-width="3" fill="none" stroke-linecap="round"/>'
            f'<ellipse cx="-12" cy="-2" rx="10" ry="5" fill="#fff" opacity=".35"/>')
    return (f'<g id="spsway"><g id="spdrop"><path d="M{x},0 L{x},{y-48}" stroke="#ffffff" stroke-width="3" opacity=".9"/>'
            f'<g transform="translate({x},{y})" filter="url(#f3d)">{legs}{wave}{body}</g></g></g>')

def html():
    build()
    bls = "".join(leaf(f"bl{k}", LEAFC[k % 5], .7, "bl") for k in range(10))
    puff = ('<g id="wpuff"><circle cx="-30" cy="0" r="26" fill="url(#gPuff)"/><circle cx="4" cy="-14" r="32" fill="url(#gPuff)"/><circle cx="36" cy="2" r="24" fill="url(#gPuff)"/>'
            '<path d="M-52,4 Q0,-50 60,6 M-34,-20 L46,-8" stroke="#b9d6ff" stroke-width="3" fill="none"/></g>')
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}</defs>
{park()}
<g id="bls">{bls}</g>
{spider()}
<g filter="url(#f3d)"><g transform="translate(960,975) scale(-.6,.6)"><g id="mithu">{MITHU}</g></g></g>
{web()}
{KIDS}
<g transform="translate(540,1850) scale(.98)" filter="url(#f3d)"><g id="gwrap">{GOLU}</g></g>
{puff}
</svg>'''
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
.badge{position:absolute;top:300px;left:130px;padding:12px 26px;border-radius:40px;background:rgba(255,255,255,.94);color:#6a1fc2;font-size:38px;font-weight:800;box-shadow:0 6px 0 rgba(0,60,120,.15)}
.nb{position:absolute;width:220px;text-align:center;transform-origin:50% 100%}
.nb .nbn{width:110px;height:110px;margin:0 auto;border-radius:50%;color:#fff;font-size:72px;line-height:1;display:flex;align-items:center;justify-content:center;padding-top:8px;font-weight:800;border:8px solid #fff;box-shadow:0 8px 0 rgba(0,40,90,.18)}
.nb .nbw{display:inline-block;margin-top:6px;padding:2px 16px;border-radius:30px;background:rgba(255,255,255,.95);font-size:36px;font-weight:800;white-space:nowrap}
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
