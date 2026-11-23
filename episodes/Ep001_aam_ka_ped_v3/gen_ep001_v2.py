"""Golu & Dost Ep 1 (v2 remake) — गोलू हाथी और आम का पेड़ | 1 से 5 तक गिनती.
Same script/audio/timing as the original; visuals rebuilt in the soft-3D house style (Golu v2, v2 Bunny, glossy Mithu)."""
import json, math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import base_v2
PROJ = sys.argv[1]; DUR = 44.5; BEAT = 60 / 112
LIPS = json.load(open(sys.argv[2]))
ns = base_v2.load(); rg = ns["rg"]; GOLU = ns["GOLU"]
GS = 0.9; GX, GY = 610, 1830
STEP0, STEP = 8.6, 2.85   # v3: counting starts later so the Fish intro lines fit
defs = ns["defs"] + "".join([
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    rg("gMango", [(0, "#fff3a0"), (.45, "#ffc21f"), (1, "#f07a12")], "35%", "30%", "80%"),
    rg("gCanopy", [(0, "#9cf26a"), (.6, "#3fbf3a"), (1, "#1f8a2e")], "40%", "30%", "75%"),
    rg("gCanopy2", [(0, "#7fe05a"), (1, "#23902e")], "40%", "30%", "75%"),
    rg("gBark", [(0, "#c98a55"), (1, "#7a4a26")], "30%", "40%", "90%"),
    rg("gBasket", [(0, "#f6c98a"), (1, "#b9782f")], "40%", "25%", "90%"),
    rg("gBun", [(0, "#ffffff"), (.6, "#f1ecff"), (1, "#c7b8ef")], "38%", "30%", "75%"),
    rg("gBunIn", [(0, "#ffd3e2"), (1, "#f59ab9")], "45%", "40%", "70%"),
    rg("gMoon", [(0, "#fffbe0"), (1, "#ffe066")], "40%", "35%", "70%"),
    rg("gMedal", [(0, "#fff6b0"), (.6, "#ffd23a"), (1, "#e09400")], "35%", "30%", "75%"),
    '<linearGradient id="gNight" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#151a52"/><stop offset=".6" stop-color="#3a3590"/><stop offset="1" stop-color="#6a4fa8"/></linearGradient>',
    '<linearGradient id="gSign" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2a868"/><stop offset="1" stop-color="#b87a3c"/></linearGradient>',
])
def mango(id_, x=0, y=0, s=1, op=1, extra=""):
    return (f'<g id="{id_}" transform="translate({x},{y}) scale({s})" opacity="{op}" {extra}>'
            '<ellipse cx="0" cy="0" rx="30" ry="36" fill="url(#gMango)" transform="rotate(-18)"/>'
            '<ellipse cx="-10" cy="-14" rx="8" ry="12" fill="#ffffff" opacity=".5" transform="rotate(-18)"/>'
            '<path d="M6,-34 q4,-10 2,-16" stroke="#6a4a20" stroke-width="5" fill="none" stroke-linecap="round"/>'
            '<path d="M8,-46 q24,-14 40,2 q-22,12 -40,-2z" fill="#3fbf3a"/></g>')

# ---- Golu v2 extras: sleepy eyes, bump stars, held mango, medal
SLEEP = '''<g id="g-sleep" opacity="0">
      <path d="M-104,-396 q36,26 72,0" stroke="#3a2a55" stroke-width="12" fill="none" stroke-linecap="round"/>
      <path d="M32,-396 q36,26 72,0" stroke="#3a2a55" stroke-width="12" fill="none" stroke-linecap="round"/></g>'''
happy_end = GOLU.index('</g>', GOLU.index('id="g-happy"')) + 4
GOLU = GOLU[:happy_end] + "\n    " + SLEEP + GOLU[happy_end:]
BUMP = '''<g id="g-bump" opacity="0"><ellipse cx="40" cy="-548" rx="34" ry="20" fill="#8fa9ee"/>
      <path id="bst0" d="M-60,-600 l7,18 18,7 -18,7 -7,18 -7,-18 -18,-7 18,-7Z" fill="#ffd93a"/>
      <path id="bst1" d="M110,-610 l6,15 15,6 -15,6 -6,15 -6,-15 -15,-6 15,-6Z" fill="#ffffff"/>
      <path id="bst2" d="M30,-650 l6,15 15,6 -15,6 -6,15 -6,-15 -15,-6 15,-6Z" fill="#ffd93a"/></g>'''
GOLU = GOLU[:GOLU.rindex('</g>')] + BUMP + mango("g-mango", 92, -236, 1.0, 0) + '''
  <g id="g-medal" opacity="0"><path d="M-24,-250 L-10,-196 M24,-250 L10,-196" stroke="#ff5fa2" stroke-width="12"/>
    <circle cx="0" cy="-180" r="30" fill="url(#gMedal)"/><path d="M0,-198 l6,12 13,2 -9,9 2,13 -12,-6 -12,6 2,-13 -9,-9 13,-2Z" fill="#fff6b0"/></g>
</g>'''

BUNNY = '''
<g id="bunny"><g id="b-all">
  <ellipse cx="0" cy="6" rx="110" ry="20" fill="url(#gShadow)"/>
  <ellipse cx="-38" cy="-8" rx="36" ry="17" fill="url(#gBun)"/><ellipse cx="38" cy="-8" rx="36" ry="17" fill="url(#gBun)"/>
  <ellipse cx="-38" cy="-6" rx="14" ry="7" fill="#ffc2d6"/><ellipse cx="38" cy="-6" rx="14" ry="7" fill="#ffc2d6"/>
  <ellipse cx="0" cy="-92" rx="74" ry="86" fill="url(#gBun)"/>
  <ellipse cx="0" cy="-76" rx="44" ry="54" fill="#ffffff" opacity=".85"/>
  <circle cx="72" cy="-40" r="20" fill="#ffffff"/>
  <g id="b-armL"><ellipse cx="-66" cy="-112" rx="20" ry="40" fill="url(#gBun)" transform="rotate(24 -66 -112)"/></g>
  <g id="b-armR"><ellipse cx="66" cy="-112" rx="20" ry="40" fill="url(#gBun)" transform="rotate(-24 66 -112)"/></g>
  ''' + mango("b-mango", 0, -110, 1.0, 0) + '''
  <g id="b-head">
    <g id="b-earL"><ellipse cx="-44" cy="-380" rx="32" ry="100" fill="url(#gBun)" transform="rotate(-12 -44 -380)"/>
      <ellipse cx="-44" cy="-376" rx="16" ry="74" fill="url(#gBunIn)" transform="rotate(-12 -44 -376)"/></g>
    <g id="b-earR"><ellipse cx="48" cy="-380" rx="32" ry="100" fill="url(#gBun)" transform="rotate(14 48 -380)"/>
      <ellipse cx="48" cy="-376" rx="16" ry="74" fill="url(#gBunIn)" transform="rotate(14 48 -376)"/></g>
    <ellipse cx="0" cy="-238" rx="104" ry="92" fill="url(#gBun)"/>
    <ellipse cx="-34" cy="-290" rx="40" ry="20" fill="#ffffff" opacity=".6"/>
    <g id="b-eyes">
      <ellipse cx="-38" cy="-250" rx="27" ry="32" fill="url(#gEye)"/><ellipse cx="38" cy="-250" rx="27" ry="32" fill="url(#gEye)"/>
      <ellipse class="bpup" cx="-33" cy="-244" rx="19" ry="23" fill="url(#gPupil)"/><ellipse class="bpup" cx="33" cy="-244" rx="19" ry="23" fill="url(#gPupil)"/>
      <circle cx="-26" cy="-254" r="7" fill="#fff"/><circle cx="40" cy="-254" r="7" fill="#fff"/>
      <path d="M-62,-276 l-10,-10 M62,-276 l10,-10" stroke="#3a2a55" stroke-width="5" stroke-linecap="round"/></g>
    <g id="b-happy" opacity="0"><path d="M-62,-248 q24,-28 48,0 M14,-248 q24,-28 48,0" stroke="#3a2a55" stroke-width="9" fill="none" stroke-linecap="round"/></g>
    <ellipse cx="-70" cy="-208" rx="22" ry="13" fill="url(#gCheek)"/><ellipse cx="70" cy="-208" rx="22" ry="13" fill="url(#gCheek)"/>
    <path d="M-10,-214 q10,-6 20,0 q-10,12 -20,0z" fill="#ff7fa6"/>
    <path id="b-smile" d="M-22,-196 q11,12 22,0 q11,12 22,0" stroke="#7a2140" stroke-width="5" fill="none" stroke-linecap="round"/>
    <rect x="-9" y="-196" width="18" height="14" rx="3" fill="#ffffff" stroke="#e6e0f0" stroke-width="2"/>
    <g id="b-mouth" opacity="0"><ellipse cx="0" cy="-186" rx="16" ry="17" fill="#7a1838"/><ellipse cx="0" cy="-176" rx="9" ry="6" fill="#ff8fa8"/>
      <rect x="-9" y="-204" width="18" height="13" rx="3" fill="#ffffff"/></g>
  </g>
</g></g>'''

MITHU = '''
<g id="mithu"><g id="m-all">
  <path d="M-16,-60 L-58,80 L-30,86 L4,-50Z" fill="#2f8cff"/><path d="M-4,-56 L-30,92 L-8,94 L14,-48Z" fill="#14943a"/>
  <ellipse cx="0" cy="-92" rx="60" ry="80" fill="url(#gMBody)"/>
  <ellipse cx="16" cy="-70" rx="34" ry="50" fill="#d9ff8f" opacity=".75"/>
  <g id="m-wing"><ellipse cx="-24" cy="-92" rx="34" ry="58" fill="url(#gMWing)" transform="rotate(-12 -24 -92)"/>
    <path d="M-40,-80 q10,26 2,48 M-26,-84 q10,28 2,52" stroke="#127a2c" stroke-width="4" fill="none" stroke-linecap="round" opacity=".6"/></g>
  <path d="M-22,-150 Q18,-124 60,-154" stroke="#ff4f6d" stroke-width="9" fill="none" stroke-linecap="round"/>
  ''' + mango("m-mango", 40, -40, .8, 0) + '''
  <g id="m-head">
    <path d="M-6,-224 q-6,-36 18,-40 q-2,22 6,30Z" fill="#2fcf5a"/><path d="M12,-228 q8,-34 30,-30 q-12,16 -12,32Z" fill="#4fd65a"/>
    <circle cx="18" cy="-182" r="54" fill="url(#gMHead)"/>
    <ellipse cx="0" cy="-206" rx="24" ry="14" fill="#ffffff" opacity=".35"/>
    <ellipse cx="34" cy="-194" rx="17" ry="19" fill="url(#gEye)"/>
    <ellipse class="mpup" cx="39" cy="-191" rx="10" ry="12" fill="url(#gPupil)"/><circle cx="43" cy="-196" r="4" fill="#fff"/>
    <ellipse cx="22" cy="-158" rx="14" ry="9" fill="url(#gCheek)"/>
    <g id="m-beak"><path d="M58,-196 Q104,-190 92,-150 Q80,-162 56,-164Z" fill="url(#gBeak)"/><path d="M60,-196 Q84,-194 90,-178" stroke="#ffd0c0" stroke-width="4" fill="none" opacity=".7"/></g>
    <path id="m-jaw" d="M58,-166 Q78,-160 84,-150 Q66,-146 56,-156Z" fill="#c3132a"/>
  </g>
  <path d="M-14,-12 q-4,14 -16,14 M-14,-12 q2,14 8,16 M14,-12 q-4,14 -14,16 M14,-12 q4,14 14,14" stroke="#ff9a3c" stroke-width="7" fill="none" stroke-linecap="round"/>
</g></g>'''

TREE_MANGOS = [(150, 860), (330, 760), (420, 930), (250, 1010), (90, 1000)]   # the 5 counted mangoes
EXTRA_MANGOS = [(230, 820), (360, 1040), (60, 900), (470, 830), (300, 900)]
BASKET = [(255, 1712), (300, 1716), (345, 1712), (278, 1688), (322, 1688)]
BX, BY = 300, 1790
BONK_FROM = (520, 760)
BUN_X, BUN_Y, BUN_S = 950, 1840, .78
MIT_X, MIT_Y, MIT_S = 96, 1640, .9

CARDS = [  # id, hindi, english, colour hi, colour en, sizes
    ("cT", "गोलू हाथी और आम का पेड़", "Golu & the Mango Tree", "#c2185b", "#1565c0", 90, 66),
    ("cC", "चलो आम गिनें!", "Let's count mangoes!", "#b35400", "#0a7d33", 120, 76),
    ("cW", "वाह! पाँच आम!", "Wow! Five mangoes!", "#c2185b", "#b35400", 126, 80),
    ("cF", "गोलू के दोस्त आए!", "Golu's friends are here!", "#1565c0", "#c2185b", 112, 70),
    ("cQ", "गोलू क्या करेगा?", "What will Golu do?", "#6a1fc2", "#0a7d33", 120, 78),
    ("cG", "ये लो दोस्तों!", "Here you go, friends!", "#b35400", "#1565c0", 124, 76),
    ("cD", "धन्यवाद!", "Thank you!", "#c2185b", "#0a7d33", 150, 92),
    ("cM", "मिलकर बाँटो, खुश रहो!", "Sharing is caring!", "#c2185b", "#1565c0", 108, 84),
    ("cS", "बाँटने से सब खुश!", "Sharing makes everyone happy!", "#ffe066", "#ffffff", 120, 64),
    ("cB", "कल फिर मिलेंगे!", "See you tomorrow!", "#ffe066", "#ffffff", 124, 78),
]
NUMS = [("एक", "One"), ("दो", "Two"), ("तीन", "Three"), ("चार", "Four"), ("पाँच", "Five")]
NUMCOL = ["#ff3b4e", "#ff9a3c", "#2f8cff", "#2fcf5a", "#a66bff"]
def overlays():
    w = "".join(f'<div class="word" id="{i}"><div class="hi" style="color:{hc};font-size:{hs}px">{hi}</div>'
                f'<div class="en" style="color:{ec};font-size:{es}px">{en}</div></div>' for i, hi, en, hc, ec, hs, es in CARDS)
    w += "".join(f'<div class="word num" id="n{i}"><div class="big" style="color:{NUMCOL[i]}">{i+1}</div>'
                 f'<div class="hi" style="color:{NUMCOL[i]};font-size:110px">{hi} आम</div><div class="en" style="color:#1565c0;font-size:74px">{en} mango{"" if i == 0 else "es"}</div></div>'
                 for i, (hi, en) in enumerate(NUMS))
    w += '<div class="bub" id="bubB">मुझे भी आम! <span>Me too!</span></div><div class="bub" id="bubM">मुझे भी! मुझे भी!<span>Me too! Me too!</span></div>'
    w += '<div class="boom" id="thak">ठक!<span>BONK!</span></div><div class="zzz" id="zzz">Z<small>z</small><small>z</small></div>'
    return w + '<div class="badge">1 से 5 तक गिनती · Count 1–5 ✨</div>'

J = []
def tl(s): J.append(s)
def card_in(i, t):
    tl(f'tl.to("#{i}",{{opacity:1,scale:1,duration:.35,ease:"back.out(3)"}},{t});')
    tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.05,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t});')
def card_out(i, t): tl(f'tl.to("#{i}",{{opacity:0,scale:.5,duration:.25}},{t});')
def eyes(state, t):  # 'open' | 'happy' | 'sleep'
    for k in ("open", "happy", "sleep"):
        sel = {"open": "#g-eyes", "happy": "#g-happy", "sleep": "#g-sleep"}[k]
        tl(f'tl.set("{sel}",{{opacity:{1 if k == state else 0}}},{t});')
def happy(t0, t1): eyes("happy", t0); eyes("open", t1)
def jump(t, n=1, h=-80):
    tl(f'tl.to("#gjump",{{y:{h},duration:.25,ease:"power2.out",yoyo:true,repeat:{2*n-1}}},{t});')
    tl(f'tl.fromTo("#g-body",{{scaleY:1}},{{scaleY:.9,scaleX:1.06,svgOrigin:"0 0",duration:.08,yoyo:true,repeat:1,immediateRender:false}},{t + .5*n - .02:.2f});')
def fly(sel, x0, y0, x1, y1, t, d, peak):
    tl(f'tl.set("{sel}",{{opacity:1}},{t:.2f}); tl.fromTo("{sel}",{{x:{x0}}},{{x:{x1},duration:{d},ease:"none",immediateRender:false}},{t:.2f});')
    tl(f'tl.fromTo("{sel}",{{y:{y0}}},{{y:{peak},duration:{d/2},ease:"power2.out",immediateRender:false}},{t:.2f}); tl.to("{sel}",{{y:{y1},duration:{d/2},ease:"power2.in"}},{t+d/2:.2f});')
    tl(f'tl.fromTo("{sel}",{{rotation:0}},{{rotation:360,duration:{d},ease:"none",immediateRender:false}},{t:.2f});')

def build():
    tl('gsap.set(".word,.bub,.boom",{opacity:0,scale:.3}); gsap.set(".fm",{opacity:0}); gsap.set("#bunny",{x:420}); gsap.set("#mithu",{x:-300,y:-700});')
    tl('tl.set("#g-trunk",{svgOrigin:"0 -352"},0); tl.set("#g-ear",{svgOrigin:"-90 -380"},0); tl.set("#g-ear2",{svgOrigin:"90 -380"},0);')
    tl('tl.set("#g-armR",{svgOrigin:"110 -215"},0); tl.set("#b-earL",{svgOrigin:"-40 -300"},0); tl.set("#b-earR",{svgOrigin:"40 -300"},0);')
    nb = int(DUR / BEAT)
    # 0 - 1.45: Golu dozes, Zzz; a mango drops and bonks his head
    eyes("sleep", 0)
    tl('tl.to("#g-head",{y:8,rotation:-3,svgOrigin:"0 -240",duration:.7,yoyo:true,repeat:1,ease:"sine.inOut"},0);')
    tl('tl.set("#zzz",{opacity:1},0); tl.fromTo("#zzz",{y:0,x:0},{y:-60,x:30,duration:1.4,ease:"none",immediateRender:false},0); tl.set("#zzz",{opacity:0},1.45);')
    tl(f'tl.set("#fbonk",{{opacity:1,x:{BONK_FROM[0]},y:{BONK_FROM[1]}}},0.9); tl.to("#fbonk",{{x:{GX+30},y:{GY-560*GS:.0f},rotation:200,duration:.55,ease:"power2.in"}},0.9);')
    tl(f'tl.to("#fbonk",{{x:{GX+340},y:{GY-700*GS:.0f},rotation:420,duration:.35,ease:"power2.out"}},1.45); tl.to("#fbonk",{{x:1180,y:1700,duration:.45,ease:"power2.in"}},1.8);')
    tl('tl.fromTo("#g-body",{scaleY:1},{scaleY:.86,scaleX:1.08,svgOrigin:"0 0",duration:.08,yoyo:true,repeat:1,immediateRender:false},1.45);')
    tl('tl.fromTo("#g-head",{y:0},{y:26,duration:.08,yoyo:true,repeat:1,immediateRender:false},1.45);')
    eyes("open", 1.5)
    tl('tl.fromTo(".pup",{scale:1},{scale:.72,transformOrigin:"50% 50%",duration:.12,yoyo:true,repeat:1,repeatDelay:.7,immediateRender:false},1.5);')
    tl('tl.set("#g-bump",{opacity:1},1.45); tl.set("#g-bump",{opacity:0},3.3);')
    for k in range(3):
        tl(f'tl.fromTo("#bst{k}",{{rotation:0}},{{rotation:360,svgOrigin:"{[-60,110,30][k]} {[-584,-596,-636][k]}",duration:.9,repeat:1,ease:"none",immediateRender:false}},{1.45+k*.1:.2f});')
    tl('tl.to("#thak",{opacity:1,scale:1,duration:.2,ease:"back.out(3)"},1.45); tl.to("#thak",{opacity:0,scale:.6,duration:.2},2.9);')
    tl('tl.fromTo("#punch",{scale:1,x:0},{scale:1.07,x:-10,duration:.08,yoyo:true,repeat:3,immediateRender:false},1.45);')
    # beat dance from 1.7 (head leads, ears follow, never in unison)
    T0 = 1.7; n = int((DUR - T0) / BEAT)
    tl(f'tl.to("#g-body",{{scaleY:.96,scaleX:1.02,svgOrigin:"0 0",duration:{BEAT/2:.3f},yoyo:true,repeat:{n*2-1},ease:"sine.inOut"}},{T0});')
    tl(f'tl.to("#g-head",{{y:9,rotation:1.5,svgOrigin:"0 -240",duration:{BEAT/2:.3f},yoyo:true,repeat:{n*2-1},ease:"sine.inOut"}},{T0});')
    tl(f'tl.to("#g-ear",{{rotation:-8,duration:{BEAT/2:.3f},yoyo:true,repeat:{n*2-1},ease:"sine.inOut"}},{T0+.06});')
    tl(f'tl.to("#g-ear2",{{rotation:6,duration:{BEAT/2:.3f},yoyo:true,repeat:{n*2-1},ease:"sine.inOut"}},{T0+.12});')
    tl(f'tl.to(".flw",{{rotation:8,duration:{BEAT:.3f},yoyo:true,repeat:{nb-1},ease:"sine.inOut",stagger:.1}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    for i, d in enumerate([110, -90, 70]):
        tl(f'tl.fromTo("#cl{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    tl(f'tl.to("#cam",{{scale:1.025,duration:{BEAT*4:.3f},yoyo:true,repeat:{int(DUR/(BEAT*4))-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#canopy",{{rotation:1.2,svgOrigin:"250 1150",duration:{BEAT*2:.3f},yoyo:true,repeat:{int(DUR/(BEAT*2))-1},ease:"sine.inOut"}},0);')
    # intro: hello + title, trunk wave
    tl('tl.to("#g-trunk",{rotation:-26,duration:.3,ease:"back.out(2)"},4.4); tl.to("#g-trunk",{rotation:-12,duration:.22,yoyo:true,repeat:5},4.70); tl.to("#g-trunk",{rotation:0,duration:.3},6.10);')
    happy(4.4, 5.30)
    card_in("cT", 4.30); card_out("cT", 6.81); card_in("cC", 6.96); card_out("cC", 8.45)
    jump(6.96, 1, -60)
    # counting 1..5: Golu swings his trunk at the tree, a mango drops into the basket, number card pops
    for i in range(5):
        s0 = STEP0 + i * STEP
        mx, my = TREE_MANGOS[i]; bx, by = BASKET[i]
        tl(f'tl.to("#g-trunk",{{rotation:-30,duration:.15,ease:"power2.out",yoyo:true,repeat:1}},{s0-.1:.2f});')
        tl(f'tl.fromTo("#canopy",{{x:0}},{{x:10,duration:.06,yoyo:true,repeat:3,immediateRender:false}},{s0:.2f});')
        tl(f'tl.set("#tm{i}",{{opacity:0}},{s0+.12:.2f});')
        tl(f'tl.set("#fm{i}",{{opacity:1,x:{mx},y:{my},rotation:0}},{s0+.12:.2f});')
        tl(f'tl.to("#fm{i}",{{x:{bx},y:{by},rotation:300,duration:.58,ease:"power2.in"}},{s0+.12:.2f});')
        tl(f'tl.fromTo("#basket",{{scaleY:1}},{{scaleY:.9,scaleX:1.05,svgOrigin:"{BX} {BY+40}",duration:.08,yoyo:true,repeat:1,immediateRender:false}},{s0+.7:.2f});')
        tl(f'tl.fromTo("#fm{i}",{{scale:1.3}},{{scale:1,duration:.2,ease:"back.out(3)",immediateRender:false}},{s0+.7:.2f});')
        card_in(f"n{i}", s0 + .7)
        tl(f'tl.to("#n{i} .big",{{scale:1.18,duration:.15,yoyo:true,repeat:1}},{s0+.8:.2f});')
        card_out(f"n{i}", min(s0 + STEP - .3, 21.7))
        happy(s0 + .78, s0 + 1.7); jump(s0 + .78, 1, -70)
    # wow, five
    card_in("cW", 22.0); card_out("cW", 23.45); happy(22.0, 23.2); jump(22.0, 2)
    tl('tl.to(".fm",{y:"-=14",duration:.2,yoyo:true,repeat:3,stagger:.06},22.0);')
    # friends arrive
    card_in("cF", 23.6); card_out("cF", 25.5)
    tl(f'tl.fromTo("#bunny",{{x:420}},{{x:0,duration:.7,ease:"power2.out",immediateRender:false}},23.7);')
    tl('tl.fromTo("#b-all",{y:0},{y:-70,duration:.12,yoyo:true,repeat:5,ease:"power2.out",immediateRender:false},23.7);')
    tl('tl.fromTo("#mithu",{x:-300,y:-700},{x:0,y:0,duration:.9,ease:"power2.out",immediateRender:false},24.0);')
    tl('tl.to("#m-wing",{rotation:-30,svgOrigin:"-24 -140",duration:.08,yoyo:true,repeat:11},24.0);')
    tl('tl.to(".pup",{x:14,duration:.2},23.7); tl.to(".pup",{x:-10,duration:.25},24.3); tl.to(".pup",{x:0,duration:.25},25.4);')
    # idle life for friends after arrival (offset from Golu)
    m = int((DUR - 25.0) / BEAT)
    tl(f'tl.to("#b-all",{{y:-10,duration:{BEAT/2:.3f},yoyo:true,repeat:{m*2-1},ease:"sine.inOut"}},25.0);')
    tl(f'tl.to("#b-earL",{{rotation:-8,duration:{BEAT:.3f},yoyo:true,repeat:{m-1},ease:"sine.inOut"}},25.05);')
    tl(f'tl.to("#b-earR",{{rotation:10,duration:{BEAT:.3f},yoyo:true,repeat:{m-1},ease:"sine.inOut"}},25.2);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT:.3f},yoyo:true,repeat:{m-1},ease:"sine.inOut"}},25.0);')
    # "me too!"
    tl('tl.to("#bubB",{opacity:1,scale:1,duration:.3,ease:"back.out(2.5)"},25.7); tl.to("#bubB",{opacity:0,scale:.5,duration:.25},27.8);')
    tl('tl.to("#b-armR",{rotation:-60,svgOrigin:"60 -140",duration:.2,yoyo:true,repeat:3},25.8);')
    tl('tl.to("#bubM",{opacity:1,scale:1,duration:.3,ease:"back.out(2.5)"},27.95); tl.to("#bubM",{opacity:0,scale:.5,duration:.25},29.2);')
    tl('tl.to("#m-all",{y:-30,duration:.22,yoyo:true,repeat:5,ease:"power2.out"},27.95);')
    # what will Golu do?  (thinking: eyes look up, trunk curls)
    card_in("cQ", 29.61); card_out("cQ", 31.05)
    tl('tl.to(".pup",{y:-14,x:-8,duration:.3},29.4); tl.to("#g-trunk",{rotation:-18,duration:.4,ease:"sine.inOut"},29.5); tl.to(".pup",{y:0,x:0,duration:.25},30.9); tl.to("#g-trunk",{rotation:0,duration:.3},30.9);')
    # sharing: one for Bunny, one for Mithu, one for Golu
    card_in("cG", 31.2); card_out("cG", 34.2)
    bx, by = BUN_X, BUN_Y - 110 * BUN_S; mx2, my2 = MIT_X + 40 * MIT_S, MIT_Y - 40 * MIT_S
    tl('tl.to("#g-trunk",{rotation:-34,duration:.18,ease:"power2.out",yoyo:true,repeat:5},31.55);')
    for k, (sel, tx, ty, t, dst) in enumerate([("#fm4", bx, by, 31.7, "#b-mango"), ("#fm3", mx2, my2, 32.5, "#m-mango"), ("#fm2", GX + 92 * GS, GY - 236 * GS, 33.3, "#g-mango")]):
        x0, y0 = BASKET[4 - k]
        fly(sel, x0, y0, round(tx), round(ty), t, .55, 1200)
        tl(f'tl.set("{sel}",{{opacity:0}},{t+.55:.2f}); tl.set("{dst}",{{opacity:1}},{t+.55:.2f});')
        tl(f'tl.fromTo("{dst}",{{scale:{.6 if k != 1 else .5}}},{{scale:{1 if k != 1 else .8},duration:.25,ease:"back.out(3)",immediateRender:false}},{t+.55:.2f});')
    tl('tl.set("#b-happy",{opacity:1},32.25); tl.set("#b-eyes",{opacity:0},32.25); tl.set("#b-happy",{opacity:0},33.4); tl.set("#b-eyes",{opacity:1},33.4);')
    tl('tl.to("#b-all",{y:-60,duration:.2,yoyo:true,repeat:1,ease:"power2.out"},32.25); tl.to("#m-all",{y:-40,duration:.2,yoyo:true,repeat:1},33.05);')
    happy(33.85, 34.8)
    # thank you
    card_in("cD", 34.45); card_out("cD", 37.35)
    tl('tl.to("#b-head",{rotation:-8,svgOrigin:"0 -150",duration:.25,yoyo:true,repeat:3},34.65);')
    tl('tl.to("#m-head",{rotation:-10,svgOrigin:"18 -140",duration:.25,yoyo:true,repeat:3},35.75);')
    # medal + moral + confetti
    tl('tl.set("#g-medal",{opacity:1},36.7); tl.fromTo("#g-medal",{scale:.2},{scale:1,transformOrigin:"50% 50%",duration:.4,ease:"back.out(2.5)",immediateRender:false},36.7);')
    card_in("cM", 37.45); card_out("cM", 39.18); happy(36.7, 38.5); jump(36.75, 2, -70)
    tl('tl.set(".conf",{opacity:1},36.8);')
    for k in range(36):
        x = (k * 97) % 1080
        tl(f'tl.fromTo("#cf{k}",{{x:{x},y:-80,rotation:0}},{{y:{1500 + (k*53) % 400},x:{x + ((k*37) % 160) - 80},rotation:{360 + k*20},duration:{2.0 + (k % 5)*.15:.2f},ease:"power1.in",immediateRender:false}},{36.8 + (k % 8)*.05:.2f});')
    tl('tl.set(".conf",{opacity:0},39.3);')
    # night: lullaby, stars, bye
    tl('tl.to("#night",{opacity:1,duration:1.4,ease:"sine.inOut"},38.6); tl.to("#sunwrap",{y:500,opacity:0,duration:1.2,ease:"sine.in"},38.6);')
    tl('tl.fromTo("#moon",{opacity:0,y:60},{opacity:1,y:0,duration:1.2,ease:"sine.out",immediateRender:false},39.0);')
    for k in range(14):
        tl(f'tl.fromTo("#st{k}",{{opacity:0}},{{opacity:1,duration:.4,yoyo:true,repeat:{3 + k % 3},repeatDelay:.3}},{39.2 + k*.12:.2f});')
    tl('tl.to("#dim",{opacity:.28,duration:1.4},38.6);')
    card_in("cS", 39.15); card_out("cS", 41.2)
    card_in("cB", 41.4); card_out("cB", 44.3)
    tl('tl.to("#g-armR",{rotation:-80,duration:.25,ease:"back.out(2)"},41.4); tl.to("#g-armR",{rotation:-55,duration:.22,yoyo:true,repeat:7,ease:"sine.inOut"},41.65); tl.to("#g-armR",{rotation:0,duration:.3},43.6);')
    tl('tl.to("#b-armR",{rotation:-70,svgOrigin:"60 -140",duration:.2,yoyo:true,repeat:7},41.6);')
    happy(43.2, 44.5)
    # blinks
    for t in [6.4, 9.9, 13.3, 16.9, 20.3, 25.2, 28.6, 31.0, 35.2, 40.4]:
        tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
    for t in [26.4, 29.7, 33.9, 37.6, 40.9]:
        tl(f'tl.to(".bpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
        tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+.7:.2f});')
    # lip-sync (svgOrigin keeps mouths on the faces)
    J.extend(base_v2.lip_events(LIPS["golu"], LIPS["fps"], "#g-mouth", "#g-smile", "-62 -314", skip=[(0, 1.45)]))
    J.extend(base_v2.lip_events(LIPS["bunny"], LIPS["fps"], "#b-mouth", "#b-smile", "0 -204"))
    prev = 0
    for i, v in enumerate(LIPS["mithu"]):
        if v == prev: continue
        tl(f'tl.set("#m-jaw",{{y:{[0,4,8,12][v]}}},{round(i/LIPS["fps"],3)});'); prev = v

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(36))
    flowers = "".join(ns["flower"](x, y, c, i) for i, (x, y, c) in enumerate([(450, 1800, "#ff6b9a"), (60, 1860, "#ffc51c"), (790, 1880, "#a66bff"), (1040, 1700, "#ff6b6b"), (870, 1720, "#ffc51c"), (990, 1890, "#ff9a3c")]))
    sunrays = "".join(f'<path d="M0,-90 L12,-118 L-12,-118Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    stars = "".join(f'<path id="st{k}" d="M{x},{y} l6,14 14,6 -14,6 -6,14 -6,-14 -14,-6 14,-6Z" fill="#fff6a8" opacity="0"/>'
                    for k, (x, y) in enumerate([(120, 160), (300, 90), (480, 200), (640, 120), (760, 300), (980, 120), (200, 420), (560, 420), (880, 480), (60, 600), (420, 640), (700, 620), (1000, 700), (300, 760)]))
    tree_m = "".join(mango(f"tm{i}", x, y) for i, (x, y) in enumerate(TREE_MANGOS)) + "".join(mango(f"tx{i}", x, y) for i, (x, y) in enumerate(EXTRA_MANGOS))
    fall_m = "".join(mango(f"fm{i}", 0, 0, 1, 0, 'class="fm"') for i in range(5))
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}{ns["F3D"]}</defs>
<rect width="1080" height="1920" fill="url(#gSky)"/>
<g opacity=".3">{"".join(f'<path d="M-60,1440 A600,600 0 0 1 1140,1440" stroke="{c}" stroke-width="30" fill="none" transform="translate(0,{i*30})"/>' for i, c in enumerate(["#ff3b4e","#ff9a3c","#ffc51c","#2fcf5a","#2f8cff","#a66bff"]))}</g>
<g id="sunwrap"><g transform="translate(930,150)"><g id="sunface">{sunrays}</g><circle r="80" fill="url(#gSun)"/>
  <ellipse cx="-24" cy="-10" rx="7" ry="10" fill="#7a4a00"/><ellipse cx="24" cy="-10" rx="7" ry="10" fill="#7a4a00"/>
  <path d="M-26,18 q26,24 52,0" stroke="#7a4a00" stroke-width="6" fill="none" stroke-linecap="round"/></g></g>
{ns["cloud"]("cl0", 640, 700, .8)}{ns["cloud"]("cl1", 960, 640, .7)}{ns["cloud"]("cl2", 140, 260, .6)}
<g id="night" opacity="0"><rect width="1080" height="1920" fill="url(#gNight)"/>{stars}</g>
<g id="moon" opacity="0" transform="translate(900,260)"><circle r="78" fill="url(#gMoon)"/><circle cx="34" cy="-22" r="70" fill="#1d2160"/></g>
<ellipse cx="160" cy="1560" rx="720" ry="300" fill="url(#gHillA)"/><ellipse cx="980" cy="1580" rx="680" ry="320" fill="url(#gHillB)"/>
<g transform="translate(900,1395) scale(.62)" opacity=".95"><rect x="-90" y="-110" width="180" height="120" rx="14" fill="#ffe2b8"/>
  <path d="M-120,-100 L0,-200 L120,-100Z" fill="#ff7a5c"/><rect x="-26" y="-70" width="52" height="80" rx="20" fill="#b9783f"/>
  <rect x="44" y="-80" width="34" height="34" rx="6" fill="#8fdcff"/></g>
<rect x="0" y="1700" width="1080" height="220" fill="#4fbf3a"/>
<g id="tree"><path d="M200,1770 C215,1500 205,1300 230,1120 L290,1120 C300,1300 300,1500 320,1770Z" fill="url(#gBark)"/>
  <path d="M235,1250 C200,1220 170,1180 150,1130 M280,1220 C320,1190 360,1160 380,1110" stroke="#8a5a30" stroke-width="22" fill="none" stroke-linecap="round"/>
  <ellipse cx="260" cy="1772" rx="100" ry="16" fill="url(#gShadow)"/>
  <g id="canopy"><ellipse cx="260" cy="900" rx="300" ry="240" fill="url(#gCanopy2)"/>
    <circle cx="120" cy="960" r="150" fill="url(#gCanopy)"/><circle cx="400" cy="950" r="150" fill="url(#gCanopy)"/>
    <circle cx="260" cy="780" r="180" fill="url(#gCanopy)"/><circle cx="250" cy="1020" r="140" fill="url(#gCanopy2)"/>
    <ellipse cx="190" cy="700" rx="80" ry="40" fill="#ffffff" opacity=".2"/>{tree_m}</g></g>
<g transform="translate(600,1890)"><rect x="-150" y="-40" width="300" height="60" rx="14" fill="url(#gSign)"/>
  <text x="0" y="6" text-anchor="middle" font-family="Baloo2" font-weight="800" font-size="40" fill="#5a3410">गोलू और दोस्त</text></g>
{flowers}
<g transform="translate({MIT_X},{MIT_Y+8})"><rect x="-14" y="0" width="28" height="140" rx="8" fill="url(#gSign)"/><rect x="-40" y="-6" width="80" height="18" rx="8" fill="url(#gSign)"/></g>
<g id="basket"><path d="M{BX-110},{BY-90} L{BX+110},{BY-90} L{BX+90},{BY+30} Q{BX},{BY+50} {BX-90},{BY+30}Z" fill="url(#gBasket)"/>
  <path d="M{BX-100},{BY-50} H{BX+100} M{BX-96},{BY-12} H{BX+96}" stroke="#9a5f22" stroke-width="7" opacity=".6"/>
  <ellipse cx="{BX}" cy="{BY+40}" rx="120" ry="16" fill="url(#gShadow)"/></g>
{fall_m}
<g transform="translate({MIT_X},{MIT_Y}) scale({MIT_S})" filter="url(#f3d)">{MITHU}</g>
<g transform="translate({BUN_X},{BUN_Y}) scale({BUN_S})" filter="url(#f3d)">{BUNNY}</g>
<g transform="translate({GX},{GY}) scale({GS})" filter="url(#f3d)"><g id="gjump"><g id="gwrap">{GOLU}</g></g></g>
<path d="M{BX-104},{BY-80} L{BX+104},{BY-80} L{BX+92},{BY+30} Q{BX},{BY+50} {BX-92},{BY+30}Z" fill="url(#gBasket)" opacity="0"/>
{mango("fbonk", 0, 0, 1, 0)}
<rect id="dim" width="1080" height="1920" fill="#1b1f5e" opacity="0"/>
{conf}
</svg>'''
    css = base_v2.FONT_CSS + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#8fdcff}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0;transform-origin:50% 60%}
#punch{position:absolute;inset:0;transform-origin:50% 55%}
#world{position:absolute;inset:0}
.word{position:absolute;left:40px;right:40px;top:300px;text-align:center;line-height:1.05}
.word .hi{font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(0,40,90,.18)}
.word .en{font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(0,40,90,.18)}
#cS .hi,#cS .en,#cB .hi,#cB .en{-webkit-text-stroke:14px #2a2370}
.word.num{top:220px}
.word .big{font-size:230px;font-weight:800;line-height:.95;-webkit-text-stroke:18px #fff;paint-order:stroke fill;text-shadow:0 12px 0 rgba(0,40,90,.18)}
.badge{position:absolute;top:120px;left:40px;padding:14px 28px;border-radius:40px;background:rgba(255,255,255,.92);color:#d81b72;font-size:40px;font-weight:800;box-shadow:0 6px 0 rgba(0,60,120,.15)}
.bub{position:absolute;padding:18px 30px;border-radius:44px;background:#fff;color:#c2185b;font-size:54px;font-weight:800;line-height:1.05;text-align:center;box-shadow:0 8px 0 rgba(0,60,120,.15)}
.bub span{display:block;color:#1565c0;font-size:40px}
#bubB{right:30px;top:1020px} #bubM{left:30px;top:1080px}
.boom{position:absolute;left:560px;top:960px;font-size:120px;font-weight:800;color:#ff3b4e;-webkit-text-stroke:14px #fff;paint-order:stroke fill;line-height:1;text-align:center;transform:rotate(-8deg)}
.boom span{display:block;font-size:64px;color:#ff9a3c}
.zzz{position:absolute;left:770px;top:1150px;font-size:90px;font-weight:800;color:#5a78cf;-webkit-text-stroke:10px #fff;paint-order:stroke fill;opacity:0}
.zzz small{font-size:60px;margin-left:6px}
"""
    js = "\n".join(J)
    return f'''<!doctype html><html lang="hi" data-resolution="portrait"><head><meta charset="UTF-8"/>
<script src="assets/gsap.min.js"></script><style>{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
  <audio id="song" class="clip" src="assets/song.mp3" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
  <div id="stage" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0"><div id="cam"><div id="punch">{svg}{overlays()}</div></div></div>
</div>
<script>
const tl = gsap.timeline({{paused:true}});
{js}
tl.set({{}},{{}},{DUR});
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl; tl.seek(0);
</script></body></html>'''

open(f"{PROJ}/index.html", "w").write(html())
print("ok", len(J))
