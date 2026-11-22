"""Golu & Dost Ep 3 — अच्छी आदतें #1: दाँत साफ़ करो | Brush Your Teeth (glossy style, bathroom set)."""
import json, math, sys, os
PROJ = sys.argv[1]; DUR = 34.0; BEAT = 0.5
HERE = os.path.dirname(os.path.abspath(__file__))
lips = json.load(open(f"{PROJ}/assets/lips.json"))
COLS = []  # template balloons not used
ns = {"COLS": COLS, "math": math}
exec(open(f"{HERE}/base_snip.py").read(), ns)   # rg(), defs, cloud(), flower(), balloon(), GOLU from Ep2 template
rg = ns["rg"]; GOLU = ns["GOLU"]

defs = ns["defs"] + "".join([
    '<linearGradient id="gWall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fd8ff"/><stop offset=".6" stop-color="#b8ecff"/><stop offset="1" stop-color="#e4f9ff"/></linearGradient>',
    '<linearGradient id="gFloor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd0b0"/><stop offset="1" stop-color="#ffab85"/></linearGradient>',
    '<linearGradient id="gWinDay" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2eaaff"/><stop offset="1" stop-color="#bdf0ff"/></linearGradient>',
    '<linearGradient id="gWinNight" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b1f5e"/><stop offset="1" stop-color="#4a3f9a"/></linearGradient>',
    '<linearGradient id="gChrome" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#c9d6e6"/><stop offset="1" stop-color="#8ea3bd"/></linearGradient>',
    '<linearGradient id="gTowel" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff7fb0"/><stop offset=".5" stop-color="#ffa6c9"/><stop offset="1" stop-color="#ff6fa3"/></linearGradient>',
    rg("gMBody", [(0, "#b8ff8a"), (.5, "#4fd65a"), (1, "#1f9c3a")], "38%", "30%", "75%"),
    rg("gMHead", [(0, "#c9ff9c"), (.55, "#5ade62"), (1, "#25a540")], "38%", "30%", "75%"),
    rg("gMWing", [(0, "#5fe36a"), (1, "#178a33")], "40%", "30%", "80%"),
    rg("gBeak", [(0, "#ffb08a"), (.5, "#ff5a3c"), (1, "#d02a1a")], "35%", "30%", "75%"),
    rg("gBub", [(0, "rgba(255,255,255,.05)"), (.75, "rgba(255,255,255,.25)"), (1, "rgba(200,240,255,.85)")], "50%", "50%", "50%"),
    rg("gCup", [(0, "#fff3a3"), (.6, "#ffc51c"), (1, "#e09400")], "35%", "30%", "80%"),
    rg("gDrop", [(0, "#ffffff"), (.4, "#9fe0ff"), (1, "#2f8cff")], "35%", "30%", "75%"),
    rg("gMoon", [(0, "#fffbe0"), (1, "#ffe066")], "40%", "35%", "70%"),
])

# --- Golu edits: curled trunk holding a toothbrush, raised trunk for the rinse, toothy grin, foam, sparkles, paste blob
TRUNK2 = '''<g id="g-trunk2">
      <path d="M268,-300 C350,-290 385,-200 335,-165 C300,-140 268,-165 258,-195" stroke="#86a7ef" stroke-width="62" fill="none" stroke-linecap="round"/>
      <path d="M266,-312 C338,-300 366,-230 330,-190" stroke="#c4d6fb" stroke-width="16" fill="none" stroke-linecap="round" opacity=".7"/>
      <g id="g-paste" opacity="0"><path d="M325,-262 q20,-18 38,-4 q16,14 0,26 q-14,12 -30,2 q-18,-10 -8,-24Z" fill="#ffffff"/>
        <path d="M333,-252 q12,-10 22,-2 q8,8 -2,14" stroke="#5fd0ff" stroke-width="7" fill="none" stroke-linecap="round"/></g>
    </g>
    <g id="g-trunkup" opacity="0">
      <path d="M268,-300 C340,-320 385,-420 345,-525" stroke="#86a7ef" stroke-width="62" fill="none" stroke-linecap="round"/>
      <path d="M262,-312 C326,-330 360,-410 332,-500" stroke="#c4d6fb" stroke-width="16" fill="none" stroke-linecap="round" opacity=".7"/>
    </g>'''
old_trunk_start = GOLU.index('<g id="g-trunk">'); old_trunk_end = GOLU.index('</g>', GOLU.index('326,-170')) + 4
GOLU = GOLU[:old_trunk_start] + TRUNK2 + GOLU[old_trunk_end:]
EXTRA = '''
    <g id="g-teeth" opacity="0">
      <path d="M134,-300 Q182,-232 230,-300 Z" fill="#7a1838"/>
      <path d="M140,-300 L224,-300 L220,-284 Q182,-278 144,-284 Z" fill="#ffffff"/>
      <path d="M161,-300 v15 M182,-300 v18 M203,-300 v15" stroke="#e3e8f5" stroke-width="3"/>
      <ellipse cx="182" cy="-258" rx="22" ry="9" fill="#ff8fa8"/>
    </g>
    <g id="g-foam" opacity="0">
      <circle cx="140" cy="-290" r="13" fill="#fff"/><circle cx="124" cy="-272" r="9" fill="#fff"/><circle cx="226" cy="-268" r="12" fill="#fff"/>
      <circle cx="240" cy="-288" r="8" fill="#fff"/><circle cx="150" cy="-262" r="7" fill="#eaf8ff"/><circle cx="112" cy="-294" r="6" fill="#eaf8ff"/>
    </g>
    <g id="g-brush">
      <path d="M266,-186 L196,-270" stroke="#2f8cff" stroke-width="18" stroke-linecap="round"/>
      <path d="M262,-194 L204,-264" stroke="#a7d2ff" stroke-width="5" stroke-linecap="round"/>
      <g transform="translate(188,-282) rotate(50)">
        <rect x="-30" y="-10" width="60" height="20" rx="10" fill="#2f8cff"/>
        <rect x="-26" y="-30" width="52" height="22" rx="5" fill="#ffffff"/>
        <path d="M-18,-30 v20 M-6,-30 v20 M6,-30 v20 M18,-30 v20" stroke="#cfe6ff" stroke-width="3"/>
        <g id="g-brushpaste" opacity="0"><path d="M-24,-34 q12,-16 24,-4 q12,-14 24,2 q-4,8 -48,4Z" fill="#ffffff"/>
          <path d="M-14,-36 q8,-6 14,0 q8,-6 14,0" stroke="#5fd0ff" stroke-width="5" fill="none" stroke-linecap="round"/></g>
      </g>
      <circle cx="262" cy="-192" r="30" fill="#86a7ef"/><circle cx="252" cy="-202" r="10" fill="#c4d6fb" opacity=".7"/>
    </g>
    <g id="g-spk" opacity="0">
      <path id="spk0" d="M150,-330 l8,22 22,8 -22,8 -8,22 -8,-22 -22,-8 22,-8Z" fill="#fff6a8"/>
      <path id="spk1" d="M236,-322 l6,16 16,6 -16,6 -6,16 -6,-16 -16,-6 16,-6Z" fill="#ffffff"/>
      <path id="spk2" d="M196,-248 l5,13 13,5 -13,5 -5,13 -5,-13 -13,-5 13,-5Z" fill="#fff6a8"/>
    </g>'''
mouth_end = GOLU.index('</g>', GOLU.index('id="g-mouth"')) + 4
GOLU = GOLU[:mouth_end] + EXTRA + GOLU[mouth_end:]

MITHU = '''
<g id="mithu"><g id="m-all">
  <path d="M-16,-60 L-58,80 L-30,86 L4,-50Z" fill="#2f8cff"/><path d="M-4,-56 L-30,92 L-8,94 L14,-48Z" fill="#14943a"/>
  <ellipse cx="0" cy="-92" rx="60" ry="80" fill="url(#gMBody)"/>
  <ellipse cx="16" cy="-70" rx="34" ry="50" fill="#d9ff8f" opacity=".75"/>
  <g id="m-wing"><ellipse cx="-24" cy="-92" rx="34" ry="58" fill="url(#gMWing)" transform="rotate(-12 -24 -92)"/>
    <path d="M-40,-80 q10,26 2,48 M-26,-84 q10,28 2,52" stroke="#127a2c" stroke-width="4" fill="none" stroke-linecap="round" opacity=".6"/></g>
  <path d="M-22,-150 Q18,-124 60,-154" stroke="#ff4f6d" stroke-width="9" fill="none" stroke-linecap="round"/>
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

WORDS = [  # id, hindi, english, hi colour, en colour, hi px, en px
    ("wT", "दाँत साफ़ करो!", "Brush your teeth!", "#c2185b", "#1565c0", 128, 88),
    ("wC", "ऊपर-नीचे!", "Up and down!", "#1565c0", "#b35400", 140, 92),
    ("wD", "गोल-गोल!", "Round and round!", "#6a1fc2", "#0a7d33", 140, 86),
    ("wE", "कुल्ला!", "Rinse! Splash!", "#0d5fb8", "#c2185b", 150, 92),
    ("wF", "चमकते दाँत!", "Sparkly teeth!", "#b35400", "#c2185b", 136, 92),
    ("wG", "चलो फिर से!", "Let's do it again!", "#c2185b", "#1565c0", 136, 82),
    ("wI", "सुबह और रात", "Morning and night!", "#b35400", "#4a2fb8", 130, 82),
    ("wJ", "कल फिर मिलेंगे!", "See you tomorrow!", "#c2185b", "#1565c0", 120, 76),
]

def overlays():
    w = "".join(f'<div class="word" id="{i}"><div class="hi" style="color:{hc};font-size:{hs}px">{hi}</div>'
                f'<div class="en" style="color:{ec};font-size:{es}px">{en}</div></div>' for i, hi, en, hc, ec, hs, es in WORDS)
    return w + '<div class="badge">अच्छी आदतें #1 · Good Habits</div>'

J = []
def tl(s): J.append(s)

def word_in(i, t):
    tl(f'tl.to("#{i}",{{opacity:1,scale:1,duration:.35,ease:"back.out(3)"}},{t});')
    tl(f'tl.fromTo("#punch",{{scale:1}},{{scale:1.06,duration:.15,yoyo:true,repeat:1,ease:"power2.out",immediateRender:false}},{t});')
def word_out(i, t): tl(f'tl.to("#{i}",{{opacity:0,scale:.5,duration:.25}},{t});')
def pulse(sel, t): tl(f'tl.to("{sel}",{{scale:1.15,duration:.15,yoyo:true,repeat:1}},{t});')
def happy(t0, t1):
    tl(f'tl.set("#g-eyes",{{opacity:0}},{t0}); tl.set("#g-happy",{{opacity:1}},{t0}); tl.set("#g-eyes",{{opacity:1}},{t1}); tl.set("#g-happy",{{opacity:0}},{t1});')
def jump(t, n=1, h=-80):
    tl(f'tl.to("#gwrap",{{y:{h},duration:.25,ease:"power2.out",yoyo:true,repeat:{2*n-1}}},{t});')
REST = (40, 40)
def brush_window(t0, t1, mode):
    """mode 'ud' up-down, 'rr' round; brush to mouth, teeth + foam visible, back to rest at t1."""
    tl(f'tl.to("#g-trunk2,#g-brush",{{x:0,y:0,duration:.2,ease:"power2.out"}},{t0});')
    tl(f'tl.set("#g-smile",{{opacity:0}},{t0}); tl.set("#g-teeth",{{opacity:1}},{t0}); tl.set("#g-foam",{{opacity:1}},{t0+.2});')
    avail = t1 - t0 - .45; sw = .25 if avail >= 1 else .1; off = sw / 2 if mode == "rr" else 0
    n = max(1, int((avail - off) / sw))
    if mode == "ud":
        tl(f'tl.fromTo("#g-trunk2,#g-brush",{{y:-16}},{{y:16,duration:{sw},yoyo:true,repeat:{n-1},ease:"sine.inOut",immediateRender:false}},{t0+.2:.3f});')
    else:
        tl(f'tl.fromTo("#g-trunk2,#g-brush",{{x:-16}},{{x:16,duration:{sw},yoyo:true,repeat:{n-1},ease:"sine.inOut",immediateRender:false}},{t0+.2:.3f});')
        tl(f'tl.fromTo("#g-trunk2,#g-brush",{{y:-16}},{{y:16,duration:{sw},yoyo:true,repeat:{n-1},ease:"sine.inOut",immediateRender:false}},{t0+.2+off:.3f});')
    tl(f'tl.fromTo("#g-foam",{{scale:1}},{{scale:1.12,transformOrigin:"50% 50%",duration:{sw},yoyo:true,repeat:{n-1},immediateRender:false}},{t0+.2:.3f});')
    tl(f'tl.to("#g-trunk2,#g-brush",{{x:{REST[0]},y:{REST[1]},duration:.2,ease:"power2.inOut"}},{t1-.2});')
    tl(f'tl.set("#g-teeth",{{opacity:0}},{t1}); tl.set("#g-foam",{{opacity:0}},{t1}); tl.set("#g-smile",{{opacity:1}},{t1});')
def mithu_talk(t, n=2):
    tl(f'tl.to("#m-head",{{rotation:-10,svgOrigin:"18 -140",duration:.25,yoyo:true,repeat:{2*n-1},ease:"sine.inOut"}},{t});')
    tl(f'tl.to("#m-jaw",{{y:8,duration:.12,yoyo:true,repeat:{4*n-1}}},{t});')
    tl(f'tl.to("#m-all",{{y:-30,duration:.25,yoyo:true,repeat:{2*n-1},ease:"power2.out"}},{t});')
def trunk_up(t0, t1):
    tl(f'tl.set("#g-trunk2,#g-brush",{{opacity:0}},{t0}); tl.set("#g-trunkup",{{opacity:1}},{t0});')
    tl(f'tl.set("#g-trunk2,#g-brush",{{opacity:1}},{t1}); tl.set("#g-trunkup",{{opacity:0}},{t1});')

NDROP = 16; NDROP2 = 8
TIPX, TIPY = 430 + 345 * 1.2, 1840 - 525 * 1.2   # raised trunk tip on screen
def build():
    tl('gsap.set(".word",{opacity:0,scale:.3});')
    tl(f'gsap.set("#g-trunk2,#g-brush",{{x:{REST[0]},y:{REST[1]}}});')
    nb = int(DUR / BEAT)
    tl(f'tl.to("#g-body",{{scaleY:.95,scaleX:1.025,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-head",{{y:10,rotation:2,svgOrigin:"100 -250",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#g-ear",{{rotation:-10,svgOrigin:"60 -260",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#cam",{{scale:1.025,duration:{BEAT*4},yoyo:true,repeat:{int(DUR/2)-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    tl(f'tl.to("#m-wing",{{rotation:-6,svgOrigin:"-24 -140",duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut"}},0);')
    tl(f'tl.to("#towel",{{skewX:3,duration:{BEAT*2},yoyo:true,repeat:{int(DUR)-1},ease:"sine.inOut"}},0);')
    for k in range(10):  # soap bubbles drifting up (background)
        x = [90, 990, 300, 760, 40, 1040, 560, 880, 200, 680][k]; d = 6 + (k % 3) * 2
        t = 0
        while t < DUR - 0.01:
            dd = min(d, DUR - t)
            tl(f'tl.fromTo("#bub{k}",{{x:{x},y:{1720 - (k*90) % 300}}},{{x:{x + (40 if k%2 else -40)},y:{1720 - (k*90) % 300 - 900*dd/d:.0f},duration:{dd},ease:"none",immediateRender:false}},{t});')
            t += d
    # 0.0-3.0 surprise: Mithu stomps the tube, paste flies onto Golu's trunk
    tl('tl.to("#mithu",{x:110,y:-60,duration:.15,ease:"power2.out"},0); tl.to("#mithu",{y:0,duration:.12,ease:"power2.in"},.15);')
    tl('tl.to("#tube",{scaleY:.45,scaleX:1.25,transformOrigin:"50% 100%",duration:.08},.25);')
    tl('tl.set("#pfly",{opacity:1},.27); tl.fromTo("#pfly",{x:330,y:960},{x:851,duration:.3,ease:"none",immediateRender:false},.27);')
    tl('tl.fromTo("#pfly",{y:960},{y:1555,duration:.3,ease:"power1.in",immediateRender:false},.27); tl.set("#pfly",{opacity:0},.57);')
    tl('tl.set("#g-paste",{opacity:1},.57); tl.fromTo("#g-paste",{scale:.5},{scale:2,svgOrigin:"344 -246",duration:.25,ease:"back.out(3)",immediateRender:false},.57);')
    happy(.57, 1.3)
    word_in("wT", .2)
    tl('tl.to("#gwrap",{x:-20,duration:.06,yoyo:true,repeat:5},.57);')
    tl('tl.to("#tube",{scaleY:1,scaleX:1,duration:.3},1.2); tl.to("#mithu",{x:0,duration:.3,ease:"power2.inOut"},1.4);')
    mithu_talk(2.0, 2)
    # wipe paste onto the brush
    tl('tl.to("#g-paste",{opacity:0,duration:.15},3.0); tl.set("#g-brushpaste",{opacity:1},3.05);')
    tl('tl.fromTo("#g-brushpaste",{scale:.3},{scale:1,duration:.25,ease:"back.out(3)",transformOrigin:"50% 100%",immediateRender:false},3.05);')
    pulse("#wT .hi", 3.35); pulse("#wT .en", 4.95)
    happy(4.95, 6.0); jump(4.95, 1)
    word_out("wT", 6.3)
    # up-down
    word_in("wC", 6.5); pulse("#wC .en", 7.7)
    brush_window(7.5, 10.3, "ud"); happy(7.7, 8.9)
    word_out("wC", 10.3)
    # round and round
    word_in("wD", 10.5); pulse("#wD .en", 11.7)
    brush_window(11.5, 14.3, "rr"); happy(11.7, 13.1)
    word_out("wD", 14.3)
    # rinse: raised trunk sprays a fountain that splashes Mithu
    word_in("wE", 14.5); trunk_up(15.3, 18.0)
    tl('tl.set("#g-brushpaste",{opacity:0},15.3);')
    for k in range(NDROP):
        t = 15.45 + k * 0.05; tx = 150 + (k * 37) % 120; peak = 700 + (k * 29) % 120
        tl(f'tl.set("#dp{k}",{{opacity:1}},{t:.2f}); tl.fromTo("#dp{k}",{{x:{TIPX:.0f}}},{{x:{tx},duration:.8,ease:"none",immediateRender:false}},{t:.2f});')
        tl(f'tl.fromTo("#dp{k}",{{y:{TIPY:.0f}}},{{y:{peak},duration:.4,ease:"power2.out",immediateRender:false}},{t:.2f}); tl.to("#dp{k}",{{y:{820 + (k*13) % 120},duration:.4,ease:"power2.in"}},{t+.4:.2f}); tl.set("#dp{k}",{{opacity:0}},{t+.8:.2f});')
    tl('tl.set("#mwet",{opacity:1},16.2); tl.to("#mwet",{y:40,duration:.8,ease:"power1.in"},16.2); tl.set("#mwet",{opacity:0},17.6);')
    tl('tl.to("#mithu",{rotation:8,svgOrigin:"0 0",duration:.1,yoyo:true,repeat:9},16.25);')
    mithu_talk(16.0, 2); happy(16.0, 17.2)
    word_out("wE", 18.3)
    # sparkly teeth
    word_in("wF", 18.5); pulse("#wF .en", 19.85)
    tl('tl.set("#g-smile",{opacity:0},19.7); tl.set("#g-teeth",{opacity:1},19.7); tl.set("#g-spk",{opacity:1},19.7);')
    for k in range(3):
        tl(f'tl.fromTo("#spk{k}",{{scale:.2,rotation:0}},{{scale:1.2,rotation:90,transformOrigin:"50% 50%",duration:.25,yoyo:true,repeat:5,immediateRender:false}},{19.7 + k*0.12:.2f});')
    tl('tl.set("#g-teeth",{opacity:0},21.3); tl.set("#g-spk",{opacity:0},21.3); tl.set("#g-smile",{opacity:1},21.3);')
    happy(19.85, 21.1); jump(19.85, 2)
    word_out("wF", 21.35)
    # recap
    word_in("wG", 21.5); pulse("#wG .en", 22.8); happy(22.8, 24.0); jump(22.8, 1)
    tl('tl.set("#g-brushpaste",{opacity:1},23.0);')
    word_out("wG", 24.2)
    word_in("wC", 24.45); brush_window(24.45, 25.15, "ud"); word_out("wC", 25.0)
    word_in("wD", 25.15); brush_window(25.15, 25.85, "rr"); word_out("wD", 25.7)
    word_in("wE", 25.9); trunk_up(25.9, 26.75)
    for k in range(NDROP2):
        t = 25.95 + k * 0.05; tx = TIPX - 140 + k * 40
        tl(f'tl.set("#dq{k}",{{opacity:1}},{t:.2f}); tl.fromTo("#dq{k}",{{x:{TIPX:.0f}}},{{x:{tx:.0f},duration:.6,ease:"none",immediateRender:false}},{t:.2f});')
        tl(f'tl.fromTo("#dq{k}",{{y:{TIPY:.0f}}},{{y:{TIPY-260:.0f},duration:.3,ease:"power2.out",immediateRender:false}},{t:.2f}); tl.to("#dq{k}",{{y:{TIPY-60:.0f},duration:.3,ease:"power2.in"}},{t+.3:.2f}); tl.set("#dq{k}",{{opacity:0}},{t+.6:.2f});')
    word_out("wE", 26.6)
    # morning and night: the window goes day -> night -> day
    word_in("wI", 26.9); pulse("#wI .en", 28.7)
    tl('tl.to("#winNight",{opacity:1,duration:.4},27.9); tl.to("#winNight",{opacity:0,duration:.4},29.9);')
    brush_window(28.7, 30.2, "ud"); happy(28.7, 29.8)
    word_out("wI", 30.3)
    # see you tomorrow (loop back to the first pose for 33.5-34)
    word_in("wJ", 30.5); pulse("#wJ .en", 31.85)
    mithu_talk(31.85, 3); happy(31.85, 33.0); jump(31.85, 2)
    tl('tl.set(".conf",{opacity:1},30.5);')
    for k in range(36):
        x = (k * 97) % 1080; c = ["#ff3b4e", "#ffc51c", "#2f8cff", "#2fcf5a", "#ff5fa2"][k % 5]
        tl(f'tl.fromTo("#cf{k}",{{x:{x},y:-80,rotation:0}},{{y:{1500 + (k*53) % 400},x:{x + ((k*37) % 160) - 80},rotation:{360 + k*20},duration:{2.0 + (k % 5)*.15:.2f},ease:"power1.in",immediateRender:false}},{30.5 + (k % 8)*.05:.2f});')
    tl('tl.set(".conf",{opacity:0},33.4);')
    word_out("wJ", 33.3)
    tl('tl.set("#g-brushpaste",{opacity:0},33.4);')
    for t in [2.6, 9.2, 13.6, 17.6, 23.5, 27.6, 33.6]:
        tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
    for t in [1.0, 5.5, 12.4, 20.4, 27.2]:
        tl(f'tl.to(".mpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
    prev = 0
    for i, v in enumerate(lips["golu"]):
        if v == prev: continue
        t = round(i / lips["fps"], 3)
        if v == 0: tl(f'tl.set("#g-mouth",{{opacity:0}},{t});tl.set("#g-smile",{{opacity:1}},{t});')
        else: tl(f'tl.set("#g-mouth",{{opacity:1,scaleY:{[0,.5,.8,1.1][v]}}},{t});tl.set("#g-smile",{{opacity:0}},{t});')
        prev = v

def tiles():
    s = "".join(f'<path d="M{x},0 V1720" stroke="#ffffff" stroke-opacity=".35" stroke-width="4"/>' for x in range(0, 1081, 120))
    s += "".join(f'<path d="M0,{y} H1080" stroke="#ffffff" stroke-opacity=".35" stroke-width="4"/>' for y in range(0, 1721, 120))
    s += "".join(f'<path d="M{x},1720 L{540 + (x-540)*1.6:.0f},1920" stroke="#ffffff" stroke-opacity=".4" stroke-width="4"/>' for x in range(-120, 1201, 120))
    s += '<path d="M0,1800 H1080 M0,1870 H1080" stroke="#ffffff" stroke-opacity=".4" stroke-width="4"/>'
    return s

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(36))
    bubs = "".join(f'<circle id="bub{k}" r="{18 + (k*7)%22}" cx="0" cy="0" fill="url(#gBub)" stroke="#ffffff" stroke-opacity=".7" stroke-width="2"/>' for k in range(10))
    drops = "".join(f'<ellipse id="dp{k}" rx="13" ry="17" fill="url(#gDrop)" opacity="0"/>' for k in range(NDROP))
    drops += "".join(f'<ellipse id="dq{k}" rx="11" ry="14" fill="url(#gDrop)" opacity="0"/>' for k in range(NDROP2))
    sunrays = "".join(f'<path d="M0,-74 L10,-98 L-10,-98Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    stars = "".join(f'<path d="M{x},{y} l5,12 12,5 -12,5 -5,12 -5,-12 -12,-5 12,-5Z" fill="#fff6a8"/>' for x, y in [(760, 780), (960, 840), (820, 980), (980, 980)])
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}<clipPath id="winClip"><rect x="700" y="720" width="320" height="340" rx="30"/></clipPath></defs>
<rect width="1080" height="1720" fill="url(#gWall)"/>
{tiles()}
<rect x="0" y="1690" width="1080" height="34" fill="#ffffff" opacity=".7"/>
<rect x="0" y="1720" width="1080" height="200" fill="url(#gFloor)"/>
<g clip-path="url(#winClip)"><rect x="700" y="720" width="320" height="340" fill="url(#gWinDay)"/>
  <g transform="translate(900,840)"><g id="sunface">{sunrays}</g><circle r="66" fill="url(#gSun)"/>
    <ellipse cx="-20" cy="-8" rx="6" ry="9" fill="#7a4a00"/><ellipse cx="20" cy="-8" rx="6" ry="9" fill="#7a4a00"/>
    <path d="M-22,14 q22,20 44,0" stroke="#7a4a00" stroke-width="5" fill="none" stroke-linecap="round"/></g>
  {ns["cloud"]("wcl", 790, 980, .55)}
  <g id="winNight" opacity="0"><rect x="700" y="720" width="320" height="340" fill="url(#gWinNight)"/>
    <circle cx="880" cy="860" r="60" fill="url(#gMoon)"/><circle cx="905" cy="842" r="52" fill="#2a2a70"/>{stars}</g>
</g>
<rect x="700" y="720" width="320" height="340" rx="30" fill="none" stroke="#ffffff" stroke-width="22"/>
<path d="M860,720 V1060 M700,890 H1020" stroke="#ffffff" stroke-width="12"/>
<rect x="680" y="1052" width="360" height="26" rx="12" fill="#ffffff"/>
<g id="shelf" transform="translate(-775,270)"><rect x="810" y="1150" width="240" height="20" rx="8" fill="#ffffff"/>
  <path d="M842,1150 L850,1080 L900,1080 L908,1150Z" fill="url(#gCup)"/>
  <path d="M862,1082 L852,1020 M884,1082 L896,1024" stroke="#ff5fa2" stroke-width="10" stroke-linecap="round"/>
  <rect x="842" y="1010" width="22" height="16" rx="5" fill="#fff"/><rect x="886" y="1014" width="22" height="16" rx="5" fill="#fff"/>
  <rect x="940" y="1104" width="80" height="46" rx="20" fill="#ffd0e6"/><ellipse cx="966" cy="1116" rx="14" ry="6" fill="#ffffff" opacity=".7"/></g>
<g id="bubs">{bubs}</g>
<g id="rail"><rect x="50" y="1000" width="300" height="18" rx="9" fill="url(#gChrome)"/>
  <circle cx="50" cy="1009" r="16" fill="url(#gChrome)"/><circle cx="350" cy="1009" r="16" fill="url(#gChrome)"/>
  <g id="towel"><path d="M80,1012 H290 V1250 Q185,1272 80,1250Z" fill="url(#gTowel)"/>
    <path d="M80,1200 H290 M80,1218 H290" stroke="#ffffff" stroke-width="8" opacity=".85"/></g></g>
<g id="tube" transform="translate(330,1000)"><g><path d="M-44,-34 H30 L44,-26 V-8 L30,0 H-44 Z" fill="#ffffff"/>
  <rect x="-44" y="-34" width="30" height="34" fill="#5fd0ff"/><rect x="44" y="-24" width="12" height="14" rx="3" fill="#ff5fa2"/></g></g>
<g transform="translate(180,1000)">{MITHU}</g>
<ellipse id="mwet" cx="190" cy="830" rx="10" ry="14" fill="url(#gDrop)" opacity="0"/>
<g transform="translate(430,1840) scale(1.2)"><g id="gwrap">{GOLU}</g></g>
<ellipse id="pfly" rx="22" ry="16" fill="#ffffff" stroke="#5fd0ff" stroke-width="5" opacity="0"/>
{drops}
{conf}
</svg>'''
    css = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#b8ecff}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0;transform-origin:50% 60%}
#punch{position:absolute;inset:0;transform-origin:50% 55%}
#world{position:absolute;inset:0}
.word{position:absolute;left:70px;right:150px;top:420px;text-align:center;line-height:1.05;white-space:nowrap}
.word .hi{font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(0,40,90,.18)}
.word .en{font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:4px;text-shadow:0 8px 0 rgba(0,40,90,.18)}
.badge{position:absolute;top:318px;left:80px;padding:14px 28px;border-radius:40px;background:rgba(255,255,255,.92);color:#d81b72;font-size:38px;font-weight:800;box-shadow:0 6px 0 rgba(0,60,120,.15)}
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
