"""Style test: glossy, outline-free, beat-driven 'colours song' for Golu & Dost."""
import json, math, sys
PROJ = sys.argv[1]; DUR = 22.0; BEAT = 0.5
lips = json.load(open(f"{PROJ}/assets/lips.json"))
COLS = [("r", "लाल", "RED", "#ff3b4e", "#ff9aa5", "#c3132a"),
        ("y", "पीला", "YELLOW", "#ffc51c", "#fff09a", "#e09400"),
        ("b", "नीला", "BLUE", "#2f8cff", "#a7d2ff", "#1259c9"),
        ("g", "हरा", "GREEN", "#2fcf5a", "#a8f5b9", "#14943a")]

def rg(id_, stops, cx="35%", cy="30%", r="75%"):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<radialGradient id="{id_}" cx="{cx}" cy="{cy}" r="{r}">{s}</radialGradient>'

defs = "".join([
    '<linearGradient id="gSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2eaaff"/><stop offset=".55" stop-color="#8fdcff"/><stop offset="1" stop-color="#e6fbff"/></linearGradient>',
    rg("gSun", [(0, "#fff8c4"), (.6, "#ffd93a"), (1, "#ffb300")], "40%", "38%", "65%"),
    rg("gCloud", [(0, "#ffffff"), (.7, "#ffffff"), (1, "#dcefff")], "45%", "30%", "70%"),
    rg("gHillA", [(0, "#b6f27a"), (1, "#58c43a")], "40%", "20%", "80%"),
    rg("gHillB", [(0, "#9be86a"), (1, "#3fae2e")], "60%", "20%", "80%"),
    rg("gBody", [(0, "#dbe8ff"), (.45, "#9fbaf6"), (1, "#5d7fd8")]),
    rg("gHead", [(0, "#e4eeff"), (.5, "#a6c0f7"), (1, "#6688dd")], "38%", "30%", "75%"),
    rg("gLeg", [(0, "#b8cbf8"), (1, "#7393e0")], "40%", "30%", "80%"),
    rg("gTrunk", [(0, "#c5d6fb"), (1, "#86a5ec")], "40%", "30%", "80%"),
    rg("gSkin", [(0, "#ffe0c4"), (1, "#eab38a")], "40%", "35%", "75%"),
    rg("gSkinB", [(0, "#f2c7a1"), (1, "#c98a5f")], "40%", "35%", "75%"),
    rg("gDressA", [(0, "#ffa6d0"), (1, "#ff4f8b")], "40%", "25%", "90%"),
    rg("gShirtB", [(0, "#ffe66b"), (1, "#ffb81c")], "40%", "25%", "90%"),
    rg("gEar", [(0, "#b9cdfa"), (1, "#7393e0")], "45%", "40%", "70%"),
    rg("gEarIn", [(0, "#ffd3de"), (1, "#f59ab2")], "45%", "40%", "70%"),
    rg("gEye", [(0, "#ffffff"), (.85, "#f3f5ff"), (1, "#d7dcf2")], "40%", "35%", "70%"),
    rg("gPupil", [(0, "#5b3d6e"), (1, "#1d1230")], "40%", "35%", "70%"),
    rg("gCheek", [(0, "#ff8fae"), (1, "rgba(255,143,174,0)")], "50%", "50%", "50%"),
    rg("gShadow", [(0, "rgba(30,80,20,.35)"), (1, "rgba(30,80,20,0)")], "50%", "50%", "50%"),
] + [rg(f"gBal_{k}", [(0, lt), (.35, c), (1, dk)], "35%", "28%", "75%") for k, _, _, c, lt, dk in COLS])

def cloud(id_, x, y, s):
    return (f'<g id="{id_}" transform="translate({x},{y}) scale({s})">' +
            "".join(f'<ellipse cx="{dx}" cy="{dy}" rx="{r*1.2}" ry="{r}" fill="url(#gCloud)"/>' for dx, dy, r in
                    [(-70, 10, 48), (0, -16, 64), (72, 10, 50), (0, 22, 52)]) + '</g>')

def flower(x, y, c, i):
    pet = "".join(f'<circle cx="{14*math.cos(a):.1f}" cy="{14*math.sin(a):.1f}" r="11" fill="{c}"/>' for a in [k*2*math.pi/5 for k in range(5)])
    return (f'<g class="flw" id="flw{i}" transform="translate({x},{y})"><path d="M0,0 q4,-25 0,-48" stroke="#2f9a2c" stroke-width="6" fill="none"/>'
            f'<g transform="translate(0,-52)">{pet}<circle r="9" fill="#fff3a3"/></g></g>')

def balloon(i, k, c):
    return (f'<g id="bal{i}" class="bal"><path d="M0,150 C-14,200 14,240 0,300" stroke="#ffffff" stroke-opacity=".9" stroke-width="4" fill="none"/>'
            f'<ellipse cx="0" cy="0" rx="120" ry="140" fill="url(#gBal_{k})"/>'
            f'<path d="M-10,138 L10,138 L4,154 L-4,154Z" fill="{c}"/>'
            f'<ellipse cx="-42" cy="-60" rx="26" ry="40" fill="#ffffff" opacity=".55" transform="rotate(-25 -42 -60)"/>'
            f'<ellipse cx="-58" cy="-10" rx="8" ry="12" fill="#ffffff" opacity=".45"/></g>')

GOLU = '''
<g id="golu">
  <ellipse cx="0" cy="6" rx="190" ry="30" fill="url(#gShadow)"/>
  <g id="g-body">
    <path d="M118,-150 q50,-6 56,-52" stroke="#7d97df" stroke-width="13" fill="none" stroke-linecap="round"/>
    <circle cx="176" cy="-206" r="11" fill="#5f7fd6"/>
    <rect x="-112" y="-112" width="92" height="116" rx="40" fill="url(#gLeg)"/><rect x="20" y="-112" width="92" height="116" rx="40" fill="url(#gLeg)"/>
    <ellipse cx="-66" cy="-2" rx="40" ry="12" fill="#c9d6fb"/><ellipse cx="66" cy="-2" rx="40" ry="12" fill="#c9d6fb"/>
    <g fill="#f4f7ff"><ellipse cx="-88" cy="-14" rx="11" ry="8"/><ellipse cx="-66" cy="-11" rx="11" ry="8"/><ellipse cx="-44" cy="-14" rx="11" ry="8"/>
      <ellipse cx="44" cy="-14" rx="11" ry="8"/><ellipse cx="66" cy="-11" rx="11" ry="8"/><ellipse cx="88" cy="-14" rx="11" ry="8"/></g>
    <ellipse cx="0" cy="-160" rx="142" ry="122" fill="url(#gBody)"/>
    <ellipse cx="0" cy="-138" rx="88" ry="78" fill="#dfe8ff" opacity=".75"/>
    <ellipse cx="-40" cy="-205" rx="70" ry="34" fill="#ffffff" opacity=".22"/>
    <g id="g-armL"><ellipse cx="-138" cy="-170" rx="38" ry="62" fill="url(#gLeg)" transform="rotate(22 -138 -170)"/></g>
    <g id="g-armR"><ellipse cx="138" cy="-170" rx="38" ry="62" fill="url(#gLeg)" transform="rotate(-22 138 -170)"/></g>
    <path d="M-96,-262 q96,46 192,0 l-12,34 q-84,40 -168,0z" fill="#ff7a3c"/>
    <path d="M-10,-214 l-34,56 l50,-28z" fill="#ff9a5c"/><circle cx="0" cy="-212" r="15" fill="#ffd24a"/><circle cx="-4" cy="-217" r="5" fill="#fff6c0" opacity=".8"/>
  </g>
  <g id="g-head">
    <g id="g-ear"><ellipse cx="-168" cy="-392" rx="118" ry="132" fill="url(#gEar)" transform="rotate(-14 -168 -392)"/>
      <ellipse cx="-160" cy="-388" rx="80" ry="94" fill="url(#gEarIn)" transform="rotate(-14 -160 -388)"/></g>
    <g id="g-ear2"><ellipse cx="168" cy="-392" rx="118" ry="132" fill="url(#gEar)" transform="rotate(14 168 -392)"/>
      <ellipse cx="160" cy="-388" rx="80" ry="94" fill="url(#gEarIn)" transform="rotate(14 160 -388)"/></g>
    <ellipse cx="0" cy="-380" rx="168" ry="156" fill="url(#gHead)"/>
    <ellipse cx="-58" cy="-470" rx="70" ry="38" fill="#ffffff" opacity=".3"/>
    <path d="M-14,-532 q-6,-40 20,-44 q20,0 12,24" stroke="#6688dd" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path d="M12,-534 q10,-34 34,-26 q14,10 0,26" stroke="#6688dd" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path d="M-104,-460 q34,-22 64,-6" stroke="#5a78cf" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path d="M40,-466 q30,-16 64,6" stroke="#5a78cf" stroke-width="9" fill="none" stroke-linecap="round"/>
    <g id="g-eyes">
      <ellipse cx="-68" cy="-398" rx="46" ry="54" fill="url(#gEye)"/><ellipse cx="68" cy="-398" rx="46" ry="54" fill="url(#gEye)"/>
      <ellipse class="pup" cx="-60" cy="-388" rx="32" ry="38" fill="url(#gPupil)"/><ellipse class="pup" cx="60" cy="-388" rx="32" ry="38" fill="url(#gPupil)"/>
      <circle cx="-48" cy="-404" r="12" fill="#fff"/><circle cx="72" cy="-404" r="12" fill="#fff"/>
      <circle cx="-70" cy="-372" r="5.5" fill="#fff"/><circle cx="50" cy="-372" r="5.5" fill="#fff"/>
      <path d="M-108,-438 l-14,-14 M-96,-448 l-8,-17" stroke="#3a2a55" stroke-width="6" stroke-linecap="round"/>
      <path d="M108,-438 l14,-14 M96,-448 l8,-17" stroke="#3a2a55" stroke-width="6" stroke-linecap="round"/>
    </g>
    <g id="g-happy" opacity="0">
      <path d="M-104,-392 q36,-42 72,0" stroke="#3a2a55" stroke-width="12" fill="none" stroke-linecap="round"/>
      <path d="M32,-392 q36,-42 72,0" stroke="#3a2a55" stroke-width="12" fill="none" stroke-linecap="round"/>
    </g>
    <ellipse cx="-118" cy="-318" rx="36" ry="22" fill="url(#gCheek)"/><ellipse cx="118" cy="-318" rx="36" ry="22" fill="url(#gCheek)"/>
    <path id="g-smile" d="M-92,-296 q30,34 62,4" stroke="#7a2140" stroke-width="8" fill="#d23a5e" stroke-linecap="round"/>
    <g id="g-mouth" opacity="0">
      <ellipse cx="-62" cy="-284" rx="28" ry="30" fill="#7a1838"/><ellipse cx="-62" cy="-268" rx="17" ry="10" fill="#ff8fa8"/>
    </g>
    <g id="g-trunk">
      <path d="M0,-352 C2,-300 0,-262 26,-240 C48,-222 74,-232 72,-258" stroke="url(#gTrunk)" stroke-width="54" fill="none" stroke-linecap="round"/>
      <path d="M-10,-340 C-8,-300 -8,-270 12,-252" stroke="#e3ecff" stroke-width="12" fill="none" stroke-linecap="round" opacity=".7"/>
      <path d="M-18,-318 q18,8 36,0 M-14,-292 q18,8 34,0" stroke="#6f8edb" stroke-width="5" fill="none" stroke-linecap="round"/>
      <ellipse cx="70" cy="-268" rx="9" ry="6" fill="#5470c4"/>
    </g>
  </g>
</g>'''

KIDS = '''
<g id="kidA" transform="translate(150,1880) scale(.78)" filter="url(#f3d)"><g id="kA">
  <ellipse cx="0" cy="4" rx="110" ry="20" fill="url(#gShadow)"/>
  <rect x="-48" y="-92" width="30" height="88" rx="14" fill="#f0b98e"/><rect x="18" y="-92" width="30" height="88" rx="14" fill="#f0b98e"/>
  <ellipse cx="-34" cy="-4" rx="30" ry="14" fill="#ff4f8b"/><ellipse cx="34" cy="-4" rx="30" ry="14" fill="#ff4f8b"/>
  <path d="M-62,-250 q62,-22 124,0 l40,170 q-102,24 -204,0z" fill="url(#gDressA)"/>
  <circle cx="-30" cy="-160" r="9" fill="#fff" opacity=".8"/><circle cx="24" cy="-130" r="9" fill="#fff" opacity=".8"/><circle cx="-6" cy="-200" r="9" fill="#fff" opacity=".8"/>
  <g id="kA-armL"><path d="M-62,-230 q-56,30 -64,92" stroke="#f0b98e" stroke-width="26" fill="none" stroke-linecap="round"/></g>
  <g id="kA-armR"><path d="M62,-230 q56,30 64,92" stroke="#f0b98e" stroke-width="26" fill="none" stroke-linecap="round"/></g>
  <g id="kA-head">
    <circle cx="-108" cy="-372" r="40" fill="#3b2417"/><circle cx="108" cy="-372" r="40" fill="#3b2417"/>
    <g fill="#ff4f8b"><path d="M-112,-414 l-34,-20 l0,40z M-112,-414 l34,-20 l0,40z"/><path d="M112,-414 l-34,-20 l0,40z M112,-414 l34,-20 l0,40z"/></g><circle cx="-112" cy="-414" r="9" fill="#ff2f6e"/><circle cx="112" cy="-414" r="9" fill="#ff2f6e"/>
    <circle cx="0" cy="-350" r="100" fill="url(#gSkin)"/>
    <path d="M-102,-356 q-6,-112 102,-110 q108,-2 102,110 q-30,-64 -102,-58 q-58,-6 -102,58z" fill="#3b2417"/>
    <g class="kpup"><ellipse cx="-36" cy="-344" rx="15" ry="19" fill="#2a1a2e"/><ellipse cx="36" cy="-344" rx="15" ry="19" fill="#2a1a2e"/>
      <circle cx="-30" cy="-352" r="6" fill="#fff"/><circle cx="42" cy="-352" r="6" fill="#fff"/></g>
    <ellipse cx="-60" cy="-306" rx="20" ry="11" fill="#ff8fae" opacity=".7"/><ellipse cx="60" cy="-306" rx="20" ry="11" fill="#ff8fae" opacity=".7"/>
    <path class="ksmile" d="M-24,-300 q24,24 48,0" stroke="#8a2a3c" stroke-width="7" fill="none" stroke-linecap="round"/>
    <g class="kmouth" opacity="0"><ellipse cx="0" cy="-292" rx="20" ry="20" fill="#7a1838"/><ellipse cx="0" cy="-282" rx="12" ry="7" fill="#ff8fa8"/></g><g class="ksmall" opacity="0"><ellipse cx="0" cy="-296" rx="16" ry="9" fill="#7a1838"/></g>
  </g>
</g></g>
<g id="kidB" transform="translate(930,1880) scale(.78)" filter="url(#f3d)"><g id="kB">
  <ellipse cx="0" cy="4" rx="110" ry="20" fill="url(#gShadow)"/>
  <rect x="-50" y="-120" width="40" height="70" rx="12" fill="#2f6fe0"/><rect x="10" y="-120" width="40" height="70" rx="12" fill="#2f6fe0"/>
  <rect x="-44" y="-60" width="28" height="56" rx="12" fill="#c8875e"/><rect x="16" y="-60" width="28" height="56" rx="12" fill="#c8875e"/>
  <ellipse cx="-32" cy="-4" rx="30" ry="14" fill="#2fcf5a"/><ellipse cx="32" cy="-4" rx="30" ry="14" fill="#2fcf5a"/>
  <rect x="-70" y="-252" width="140" height="146" rx="40" fill="url(#gShirtB)"/>
  <path d="M-30,-196 l14,-26 l14,26 l14,-26 l14,26" stroke="#ff7a3c" stroke-width="8" fill="none" stroke-linejoin="round"/>
  <g id="kB-armL"><path d="M-60,-232 q-56,30 -62,92" stroke="#c8875e" stroke-width="26" fill="none" stroke-linecap="round"/></g>
  <g id="kB-armR"><path d="M60,-232 q56,30 62,92" stroke="#c8875e" stroke-width="26" fill="none" stroke-linecap="round"/></g>
  <g id="kB-head">
    <circle cx="0" cy="-350" r="100" fill="url(#gSkinB)"/>
    <path d="M-100,-360 q-4,-104 100,-106 q104,2 100,106 q-24,-46 -60,-50 l-10,24 l-12,-28 q-40,-2 -70,10 l-8,26z" fill="#1f1612"/>
    <g class="kpup"><ellipse cx="-36" cy="-340" rx="15" ry="19" fill="#2a1a2e"/><ellipse cx="36" cy="-340" rx="15" ry="19" fill="#2a1a2e"/>
      <circle cx="-30" cy="-348" r="6" fill="#fff"/><circle cx="42" cy="-348" r="6" fill="#fff"/></g>
    <ellipse cx="-62" cy="-302" rx="20" ry="11" fill="#ff8f7a" opacity=".55"/><ellipse cx="62" cy="-302" rx="20" ry="11" fill="#ff8f7a" opacity=".55"/>
    <path class="ksmile" d="M-26,-296 q26,26 52,0" stroke="#6a2020" stroke-width="7" fill="none" stroke-linecap="round"/>
    <g class="kmouth" opacity="0"><ellipse cx="0" cy="-288" rx="21" ry="21" fill="#6a1430"/><ellipse cx="0" cy="-278" rx="12" ry="7" fill="#ff8fa8"/></g><g class="ksmall" opacity="0"><ellipse cx="0" cy="-292" rx="17" ry="9" fill="#6a1430"/></g>
  </g>
</g></g>'''

def overlays():
    words = "".join(f'''<div class="word" id="w{i}"><div class="hi" style="color:{c}">{hi}</div><div class="en" style="color:{c}">{en}</div></div>'''
                    for i, (k, hi, en, c, lt, dk) in enumerate(COLS))
    return f'''{words}
  <div class="word" id="wIntro"><div class="hi" style="color:#ff5fa2;font-size:150px">रंग सीखो!</div><div class="en" style="color:#2f8cff;font-size:96px">Learn Colours!</div></div>
  <div class="word" id="wEnd"><div class="hi" style="color:#ff5fa2">शाबाश!</div><div class="en" style="color:#ffb300">Well done!</div></div>
  <div class="badge">गोलू के रंग #1 · Golu's Colours</div>'''

J = []
def tl(s): J.append(s)
def build():
    tl('tl.set(".word",{opacity:0,scale:.3},0); tl.set(".bal",{opacity:0},0);')
    tl('tl.set("#g-trunk",{svgOrigin:"0 -352"},0); tl.set("#g-ear",{svgOrigin:"-90 -380"},0); tl.set("#g-ear2",{svgOrigin:"90 -380"},0);')
    tl('tl.set("#gwrap",{y:600},0); tl.to("#gwrap",{y:0,duration:.5,ease:"back.out(1.8)"},0);')
    # dance: bounce on every beat (finite repeats so it stays seekable)
    nb = int(DUR / BEAT)
    tl(f'tl.to("#g-body",{{scaleY:.94,scaleX:1.03,svgOrigin:"0 0",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0.5);')
    tl(f'tl.to("#g-head",{{y:14,rotation:3,svgOrigin:"0 -240",duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0.5);')
    tl(f'tl.to("#g-ear",{{rotation:-9,duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0.56);')
    tl(f'tl.to("#g-ear2",{{rotation:7,duration:{BEAT/2},yoyo:true,repeat:{nb*2-1},ease:"sine.inOut"}},0.62);')
    tl(f'tl.to("#g-trunk",{{rotation:5,duration:{BEAT},yoyo:true,repeat:{nb-2},ease:"sine.inOut"}},2.7);')
    # kids: enter, dance offset from Golu (never in unison), cheer on every English chorus line
    tl('tl.from("#kA",{y:500,duration:.55,ease:"back.out(1.6)"},0.2); tl.from("#kB",{y:500,duration:.55,ease:"back.out(1.6)"},0.35);')
    tl('tl.set("#kA-armL",{svgOrigin:"-62 -230"},0); tl.set("#kA-armR",{svgOrigin:"62 -230"},0); tl.set("#kB-armL",{svgOrigin:"-60 -232"},0); tl.set("#kB-armR",{svgOrigin:"60 -232"},0);')
    tl(f'tl.to("#kA",{{y:-14,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},0.9);')
    tl(f'tl.to("#kB",{{y:-12,duration:{BEAT/2},yoyo:true,repeat:{nb*2-3},ease:"sine.inOut"}},1.15);')
    tl(f'tl.to("#kA-head",{{rotation:4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},1.0);')
    tl(f'tl.to("#kB-head",{{rotation:-4,svgOrigin:"0 -250",duration:{BEAT},yoyo:true,repeat:{nb-3},ease:"sine.inOut"}},1.25);')
    cheer = [3.0 + i * 4.0 + 1.6 for i in range(4)] + [19.9]
    for t in cheer:
        for k, d in (("A", 0), ("B", .06)):
            tl(f'tl.to("#k{k}-armL",{{rotation:80,duration:.18,ease:"back.out(2)"}},{t+d}); tl.to("#k{k}-armR",{{rotation:-80,duration:.18,ease:"back.out(2)"}},{t+d+.04});')
            tl(f'tl.to("#k{k}-armL",{{rotation:0,duration:.3,ease:"power2.inOut"}},{t+d+1.0}); tl.to("#k{k}-armR",{{rotation:0,duration:.3,ease:"power2.inOut"}},{t+d+1.05});')
            for j in range(8):
                big = j % 2 == 0
                tl(f'tl.set("#kid{k} .kmouth",{{opacity:{1 if big else 0}}},{t+d+j*.11:.2f}); tl.set("#kid{k} .ksmall",{{opacity:{0 if big else 1}}},{t+d+j*.11:.2f});')
            tl(f'tl.set("#kid{k} .ksmile",{{opacity:0}},{t+d});')
            tl(f'tl.set("#kid{k} .kmouth",{{opacity:0}},{t+d+.9}); tl.set("#kid{k} .ksmall",{{opacity:0}},{t+d+.9}); tl.set("#kid{k} .ksmile",{{opacity:1}},{t+d+.9});')
    tl(f'tl.to(".flw",{{rotation:8,duration:{BEAT},yoyo:true,repeat:{nb-1},ease:"sine.inOut",stagger:.1}},0);')
    tl(f'tl.to("#sunface",{{rotation:360,svgOrigin:"0 0",duration:{DUR},ease:"none"}},0);')
    for i, (cx, d) in enumerate([(160, 120), (900, -90), (560, 80)]):
        tl(f'tl.fromTo("#cl{i}",{{x:0}},{{x:{d},duration:{DUR},ease:"none"}},0);')
    tl(f'tl.to("#cam",{{scale:1.03,duration:{BEAT*4},yoyo:true,repeat:{int(DUR/2)-1},ease:"sine.inOut"}},0);')
    # intro wave + words
    tl('tl.to("#g-trunk",{rotation:-28,duration:.3,ease:"back.out(2)"},.4); tl.to("#g-trunk",{rotation:-14,duration:.25,yoyo:true,repeat:5},.7); tl.to("#g-trunk",{rotation:0,duration:.3},2.3);')
    tl('tl.to("#wIntro",{opacity:1,scale:1,duration:.4,ease:"back.out(2.5)"},.5); tl.to("#wIntro",{opacity:0,scale:.4,duration:.25},2.75);')
    slots = [(150, 640), (370, 600), (590, 640), (810, 600)]
    for i in range(4):
        T = 3.0 + i * 4.0
        tl(f'tl.set("#bal{i}",{{opacity:1,x:540,y:1500,scale:1}},{T});')
        tl(f'tl.to("#bal{i}",{{y:720,duration:.5,ease:"back.out(1.4)"}},{T});')
        tl(f'tl.to("#bal{i}",{{rotation:6,transformOrigin:"50% 100%",duration:{BEAT},yoyo:true,repeat:4,ease:"sine.inOut"}},{T+.5});')
        tl(f'tl.fromTo("#cam",{{scale:1}},{{scale:1.07,duration:.15,yoyo:true,repeat:1,ease:"power2.out"}},{T+.5});')
        tl(f'tl.to("#w{i}",{{opacity:1,scale:1,duration:.35,ease:"back.out(3)"}},{T+.5});')
        tl(f'tl.to("#w{i} .en",{{scale:1.15,duration:.15,yoyo:true,repeat:1}},{T+1.6});')
        tl(f'tl.set("#g-eyes",{{opacity:0}},{T+.5}); tl.set("#g-happy",{{opacity:1}},{T+.5}); tl.set("#g-eyes",{{opacity:1}},{T+1.4}); tl.set("#g-happy",{{opacity:0}},{T+1.4});')
        tl(f'tl.to("#gwrap",{{y:-90,duration:.25,ease:"power2.out",yoyo:true,repeat:1}},{T+.5});')
        tl(f'tl.to("#w{i}",{{opacity:0,scale:.5,duration:.25}},{T+3.4});')
        sx, sy = slots[i]
        tl(f'tl.to("#bal{i}",{{x:{sx},y:{sy},scale:.42,duration:.6,ease:"power2.inOut"}},{T+3.3});')
    # finale
    tl('tl.to(".bal",{y:"-=30",duration:.25,yoyo:true,repeat:9,stagger:.12,ease:"sine.inOut"},19.0);')
    tl('tl.to("#wEnd",{opacity:1,scale:1,duration:.4,ease:"back.out(2.5)"},19.0); tl.to("#wEnd",{opacity:0,scale:.4,duration:.3},21.4);')
    tl('tl.set("#g-eyes",{opacity:0},19.0); tl.set("#g-happy",{opacity:1},19.0); tl.set("#g-eyes",{opacity:1},21.3); tl.set("#g-happy",{opacity:0},21.3);')
    tl('tl.to("#gwrap",{y:-110,duration:.25,ease:"power2.out",yoyo:true,repeat:3},19.0);')
    tl('tl.set(".conf",{opacity:1},19.0);')
    for k in range(40):
        x = (k * 97) % 1080; c = ["#ff3b4e", "#ffc51c", "#2f8cff", "#2fcf5a", "#ff5fa2"][k % 5]
        tl(f'tl.fromTo("#cf{k}",{{x:{x},y:-80,rotation:0}},{{y:{1500 + (k*53) % 400},x:{x + ((k*37) % 160) - 80},rotation:{360 + k*20},duration:{2.2 + (k % 5)*.2},ease:"power1.in"}},{19.0 + (k % 8)*.05});')
    # blinks
    for t in [2.0, 5.8, 9.9, 13.7, 17.6]:
        tl(f'tl.to(".pup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t});')
        tl(f'tl.to("#kidA .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+1.3});')
        tl(f'tl.to("#kidB .kpup",{{scaleY:.1,transformOrigin:"50% 50%",duration:.06,yoyo:true,repeat:1}},{t+.7});')
    # lip sync
    prev = 0
    for i, v in enumerate(lips["golu"]):
        if v == prev: continue
        t = round(i / lips["fps"], 3)
        if v == 0: tl(f'tl.set("#g-mouth",{{opacity:0}},{t});tl.set("#g-smile",{{opacity:1}},{t});')
        else: tl(f'tl.set("#g-mouth",{{opacity:1,scaleY:{[0,.5,.8,1.1][v]},svgOrigin:"-62 -314"}},{t});tl.set("#g-smile",{{opacity:0}},{t});')
        prev = v

def html():
    build()
    conf = "".join(f'<rect class="conf" id="cf{k}" x="-9" y="-5" width="18" height="10" rx="3" fill="{["#ff3b4e","#ffc51c","#2f8cff","#2fcf5a","#ff5fa2"][k%5]}" opacity="0"/>' for k in range(40))
    flowers = "".join(flower(x, y, c, i) for i, (x, y, c) in enumerate([(70, 1700, "#ff6b9a"), (150, 1790, "#ffc51c"), (960, 1720, "#a66bff"), (1020, 1820, "#ff6b6b"), (880, 1860, "#ffc51c"), (240, 1880, "#ff9a3c")]))
    sunrays = "".join(f'<path d="M0,-118 L14,-150 L-14,-150Z" fill="#ffd93a" transform="rotate({a})"/>' for a in range(0, 360, 30))
    svg = f'''<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
<defs>{defs}<filter id="f3d" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB"><feGaussianBlur in="SourceAlpha" stdDeviation="12" result="b"/>
<feSpecularLighting in="b" surfaceScale="8" specularConstant=".8" specularExponent="24" lighting-color="#ffffff" result="s"><fePointLight x="-200" y="-800" z="700"/></feSpecularLighting>
<feComposite in="s" in2="SourceAlpha" operator="in" result="s2"/>
<feDiffuseLighting in="b" surfaceScale="8" diffuseConstant="1.08" lighting-color="#ffffff" result="d"><feDistantLight azimuth="235" elevation="50"/></feDiffuseLighting>
<feComposite in="SourceGraphic" in2="d" operator="arithmetic" k1="1.02" k2="0" k3="0" k4="0" result="lit"/>
<feComposite in="lit" in2="s2" operator="arithmetic" k1="0" k2="1" k3=".5" k4="0" result="o"/>
<feComposite in="o" in2="SourceAlpha" operator="in"/></filter></defs>
<rect width="1080" height="1920" fill="url(#gSky)"/>
<g opacity=".35">{"".join(f'<path d="M-60,1500 A600,600 0 0 1 1140,1500" stroke="{c}" stroke-width="34" fill="none" transform="translate(0,{i*34}) scale(1,{1-i*0.02})"/>' for i, c in enumerate(["#ff3b4e","#ff9a3c","#ffc51c","#2fcf5a","#2f8cff","#a66bff"]))}</g>
<g transform="translate(880,230)"><g id="sunface">{sunrays}</g><circle r="105" fill="url(#gSun)"/>
  <ellipse cx="-30" cy="-12" rx="9" ry="13" fill="#7a4a00"/><ellipse cx="30" cy="-12" rx="9" ry="13" fill="#7a4a00"/>
  <path d="M-34,22 q34,30 68,0" stroke="#7a4a00" stroke-width="7" fill="none" stroke-linecap="round"/>
  <ellipse cx="-56" cy="18" rx="16" ry="10" fill="#ff8f6b" opacity=".6"/><ellipse cx="56" cy="18" rx="16" ry="10" fill="#ff8f6b" opacity=".6"/></g>
{cloud("cl0", 160, 560, 1.1)}{cloud("cl1", 820, 520, .9)}{cloud("cl2", 520, 160, .7)}
<ellipse cx="200" cy="1640" rx="720" ry="300" fill="url(#gHillA)"/><ellipse cx="960" cy="1660" rx="680" ry="320" fill="url(#gHillB)"/>
<rect x="0" y="1760" width="1080" height="200" fill="#4fbf3a"/>
{flowers}
{"".join(balloon(i, k, c) for i, (k, hi, en, c, lt, dk) in enumerate(COLS))}
{KIDS}
<g transform="translate(540,1850) scale(.98)" filter="url(#f3d)"><g id="gwrap">{GOLU}</g></g>
{conf}
</svg>'''
    css = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#8fdcff}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif}
#cam{position:absolute;inset:0;transform-origin:50% 60%}
#world{position:absolute;inset:0}
.word{position:absolute;left:0;right:0;top:960px;text-align:center;line-height:1}
.word .hi{font-size:170px;font-weight:800;-webkit-text-stroke:16px #fff;paint-order:stroke fill;text-shadow:0 10px 0 rgba(0,40,90,.18)}
.word .en{font-size:120px;font-weight:800;-webkit-text-stroke:14px #fff;paint-order:stroke fill;margin-top:6px;text-shadow:0 8px 0 rgba(0,40,90,.18)}
#wIntro,#wEnd{top:930px}
.badge{position:absolute;top:56px;left:40px;padding:14px 28px;border-radius:40px;background:rgba(255,255,255,.92);color:#d81b72;font-size:44px;font-weight:800;box-shadow:0 6px 0 rgba(0,60,120,.15)}
"""
    js = "\n".join(J)
    return f'''<!doctype html><html lang="hi" data-resolution="portrait"><head><meta charset="UTF-8"/>
<script src="assets/gsap.min.js"></script><style>{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
  <audio id="song" class="clip" src="assets/song.mp3" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
  <div id="stage" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0"><div id="cam">{svg}{overlays()}</div></div>
</div>
<script>
const tl = gsap.timeline({{paused:true}});
{js}
tl.set({{}},{{}},{DUR});
window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl; tl.seek(0);
</script></body></html>'''

open(f"{PROJ}/index.html", "w").write(html())
print("ok", len(J))
