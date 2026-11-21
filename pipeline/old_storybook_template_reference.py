"""Generates the HyperFrames composition for Golu & Dost Ep.1 (storybook style)."""
import json, math, random, sys

PROJ = sys.argv[1]
DUR = 44.5
STEP0, STEP = 7.0, 3.2
INK = "#2b2233"
lips = json.load(open(f"{PROJ}/assets/lipsync.json"))

# ---------------------------------------------------------------- wobbly drawing helpers
def _smooth(pts, closed=True):
    n = len(pts)
    if closed:
        d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
        for i in range(n):
            p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
        return d + "Z"
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(n - 1):
        p0 = pts[max(i - 1, 0)]; p1 = pts[i]; p2 = pts[i + 1]; p3 = pts[min(i + 2, n - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d

def blob(cx, cy, rx, ry, seed=0, jit=0.035, n=14, rot=0):
    r = random.Random(seed)
    pts = []
    for i in range(n):
        a = rot + 2 * math.pi * i / n
        k = 1 + r.uniform(-jit, jit)
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    return _smooth(pts)

def wpoly(points, seed=0, jit=2.5, closed=True, sub=3):
    """hand-drawn polygon/polyline: subdivide edges and jitter"""
    r = random.Random(seed)
    pts = []
    m = len(points) if closed else len(points) - 1
    for i in range(m):
        a, b = points[i], points[(i + 1) % len(points)]
        for s in range(sub):
            t = s / sub
            pts.append((a[0] + (b[0] - a[0]) * t + r.uniform(-jit, jit), a[1] + (b[1] - a[1]) * t + r.uniform(-jit, jit)))
    if not closed: pts.append(points[-1])
    return _smooth(pts, closed)

def P(d, fill, sw=6, stroke=INK, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'

def rrect(x, y, w, h, seed=0, jit=2.0):
    return wpoly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], seed, jit)

# ---------------------------------------------------------------- props & characters
def mango_symbol():
    return f'''<symbol id="mango" viewBox="-50 -70 100 125" overflow="visible">
  {P(blob(0, 0, 36, 44, 11, 0.04), "#f2b134")}
  <path d="{blob(-12, -14, 10, 13, 2)}" fill="#fbdc8a"/>
  <path d="M0,-43 q4,-10 9,-14" stroke="#6b3d1e" stroke-width="6" fill="none" stroke-linecap="round"/>
  {P(blob(18, -55, 15, 7, 4, 0.06), "#6fae55", 4)}
  <ellipse cx="-11" cy="2" rx="5.5" ry="7" fill="{INK}"/><ellipse cx="11" cy="2" rx="5.5" ry="7" fill="{INK}"/>
  <circle cx="-9" cy="-1" r="2" fill="#fff"/><circle cx="13" cy="-1" r="2" fill="#fff"/>
  <path d="M-7,12 q7,7 14,0" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>
  <ellipse cx="-21" cy="11" rx="6" ry="3.5" fill="#f08a7e" opacity=".8"/><ellipse cx="21" cy="11" rx="6" ry="3.5" fill="#f08a7e" opacity=".8"/>
</symbol>'''

def flower_symbol():
    petals = "".join(P(blob(14 * math.cos(a), 14 * math.sin(a), 11, 11, k, 0.06, 8), "#f3a0b5", 3.5)
                     for k, a in enumerate([i * 2 * math.pi / 5 - math.pi / 2 for i in range(5)]))
    return f'''<symbol id="flower" viewBox="-40 -40 80 80" overflow="visible">{petals}
  {P(blob(0, 0, 9, 9, 9, 0.05, 8), "#f7d35c", 3.5)}</symbol>'''

def heart_symbol():
    return f'''<symbol id="heart" viewBox="-40 -40 80 80" overflow="visible">
  <path d="M0,28 C-40,0 -34,-30 -14,-30 C-4,-30 0,-20 0,-16 C0,-20 4,-30 14,-30 C34,-30 40,0 0,28Z" fill="#e8667a" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
  <ellipse cx="-14" cy="-16" rx="6" ry="4" fill="#f6a3ae"/></symbol>'''

def golu():
    body, dark, light = "#93acd8", "#7a93c6", "#b5c8ea"
    legs = "".join(P(rrect(x, -78, 58, 82, 20 + i, 2), dark, 6) +
                   f'<path d="M{x+8},-6 h42" stroke="#e8eefb" stroke-width="7" stroke-linecap="round"/>'
                   for i, x in enumerate([-128, -52, 34, 104]))
    curls = "".join(f'<path d="M{115+k*18},-352 q-12,-22 4,-30 q14,-4 10,12" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>' for k in range(3))
    flowers = "".join(f'<g class="hflower" id="hf{i}"><use href="#flower" x="{x-20}" y="{y-20}" width="40" height="40"/></g>'
                      for i, (x, y) in enumerate([(108, -350), (140, -362), (172, -352), (124, -380), (158, -382)]))
    return f'''
<g id="golu">
  <path d="M-150,-128 q-40,8 -46,52" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="{blob(-198,-72,10,14,5)}" fill="{INK}"/>
  {legs}
  {P(blob(0, -132, 158, 116, 1, 0.025, 18), body)}
  <path d="{blob(-12, -100, 100, 58, 3, 0.04)}" fill="{light}" opacity=".85"/>
  <path d="{blob(-60, -175, 40, 20, 6, 0.1)}" fill="#a9bfe6" opacity=".7"/>
  <g id="golu-sash" opacity="0">
    <path d="M-95,-235 C-20,-170 60,-110 120,-40 L95,-12 C30,-85 -45,-150 -122,-208Z" fill="#f3a3b8" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
    <text font-family="Baloo2" font-weight="800" font-size="30" fill="{INK}" data-layout-ignore="true" transform="translate(-98,-206) rotate(40)">मिलकर बाँटो!</text>
  </g>
  {P(blob(58, -252, 82, 98, 7, 0.04), "#8099cb")}
  <path d="{blob(58, -248, 54, 68, 8, 0.05)}" fill="#f3b4c3"/>
  <g id="golu-trunk">
    <path d="M222,-236 C276,-222 296,-160 274,-104" stroke="{INK}" stroke-width="58" fill="none" stroke-linecap="round"/>
    <path d="M222,-236 C276,-222 296,-160 274,-104" stroke="{body}" stroke-width="45" fill="none" stroke-linecap="round"/>
    <path d="M256,-114 q18,6 34,2" stroke="{dark}" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M262,-150 q16,4 30,0" stroke="{dark}" stroke-width="5" fill="none" stroke-linecap="round"/>
  </g>
  {P(blob(145, -258, 104, 98, 9, 0.03, 16), body)}
  {curls}
  <g id="golu-eyes-open">
    <g class="g-eye" id="g-eye-r">{P(blob(172,-280,24,28,12,0.04,10), "#fff", 5)}<ellipse cx="176" cy="-276" rx="14" ry="17" fill="{INK}"/><circle cx="181" cy="-283" r="5.5" fill="#fff"/><circle cx="171" cy="-268" r="2.5" fill="#fff"/></g>
    <g class="g-eye" id="g-eye-l">{P(blob(112,-284,20,24,13,0.04,10), "#fff", 5)}<ellipse cx="116" cy="-280" rx="12" ry="15" fill="{INK}"/><circle cx="120" cy="-286" r="4.5" fill="#fff"/></g>
  </g>
  <g id="golu-eyes-happy" opacity="0">
    <path d="M152,-276 q20,-26 40,0" stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path d="M96,-280 q16,-22 34,0" stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round"/>
  </g>
  <g id="golu-eyes-sleep" opacity="0">
    <path d="M152,-280 q20,18 40,0" stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M96,-284 q16,16 34,0" stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round"/>
  </g>
  <g id="golu-eyes-dizzy" opacity="0">
    <path d="M172,-280 m-18,0 a18,18 0 1,1 36,0 a12,12 0 1,1 -24,0 a6,6 0 1,1 12,0" stroke="{INK}" stroke-width="5" fill="none"/>
    <path d="M112,-284 m-15,0 a15,15 0 1,1 30,0 a10,10 0 1,1 -20,0 a5,5 0 1,1 10,0" stroke="{INK}" stroke-width="5" fill="none"/>
  </g>
  <g id="golu-brows" opacity="0">
    <path d="M150,-322 q20,-14 42,-4" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <path d="M96,-322 q14,-12 32,-2" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>
  </g>
  <path id="golu-sweat" opacity="0" d="M232,-320 q-14,22 0,30 q14,-8 0,-30Z" fill="#9fd3f0" stroke="{INK}" stroke-width="4"/>
  <ellipse id="golu-cheek-r" cx="196" cy="-232" rx="17" ry="10" fill="#f08a9a" opacity=".75"/>
  <ellipse cx="102" cy="-236" rx="14" ry="9" fill="#f08a9a" opacity=".75"/>
  <g id="golu-blush" opacity="0">
    <path d="M186,-238 l6,-8 M196,-238 l6,-8 M206,-238 l6,-8" stroke="#d9546b" stroke-width="3" stroke-linecap="round"/>
  </g>
  <path id="golu-smile" d="M138,-232 q22,22 46,0" stroke="{INK}" stroke-width="6" fill="#c9465f" stroke-linecap="round"/>
  <g id="golu-mouth" opacity="0" style="transform-box: fill-box; transform-origin: 50% 0%">
    <path d="{blob(161,-212,22,22,30,0.05,10)}" fill="#a8324c" stroke="{INK}" stroke-width="5"/>
    <ellipse cx="161" cy="-201" rx="12" ry="7" fill="#f08a9a"/>
  </g>
  {flowers}
</g>'''

def bunny():
    fur, inner = "#f6eee3", "#f3b4c3"
    return f'''
<g id="bunny">
  <g id="bunny-ear-l">{P(blob(-28,-270,22,70,40,0.05,12), fur)}<path d="{blob(-28,-266,10,48,41)}" fill="{inner}"/></g>
  <g id="bunny-ear-r">{P(blob(28,-270,22,70,42,0.05,12), fur)}<path d="{blob(28,-266,10,48,43)}" fill="{inner}"/></g>
  {P(blob(0,-78,70,78,44,0.03), fur)}
  <path d="{blob(0,-62,40,44,45)}" fill="#fffaf2"/>
  {P(blob(0,-186,62,56,46,0.03), fur)}
  <g id="bunny-eyes-open">
    <g class="b-eye">{P(blob(-22,-196,13,16,47,0.04,10), "#fff", 4)}<ellipse cx="-20" cy="-193" rx="8" ry="10" fill="{INK}"/><circle cx="-17" cy="-197" r="3" fill="#fff"/></g>
    <g class="b-eye">{P(blob(22,-196,13,16,48,0.04,10), "#fff", 4)}<ellipse cx="24" cy="-193" rx="8" ry="10" fill="{INK}"/><circle cx="27" cy="-197" r="3" fill="#fff"/></g>
  </g>
  <g id="bunny-eyes-happy" opacity="0">
    <path d="M-34,-192 q12,-16 24,0 M10,-192 q12,-16 24,0" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>
  </g>
  <g id="bunny-eyes-sleep" opacity="0">
    <path d="M-34,-194 q12,12 24,0 M10,-194 q12,12 24,0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>
  </g>
  <g id="bunny-brows" opacity="0"><path d="M-38,-214 l24,-10 M38,-214 l-24,-10" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></g>
  <ellipse cx="0" cy="-174" rx="8" ry="6" fill="#e5788f"/>
  <path id="bunny-smile" d="M-10,-162 q10,10 20,0" stroke="{INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/>
  <path id="bunny-frown" opacity="0" d="M-10,-156 q10,-9 20,0" stroke="{INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/>
  <g id="bunny-mouth" opacity="0" style="transform-box: fill-box; transform-origin: 50% 0%">
    <path d="{blob(0,-152,11,12,49,0.05,8)}" fill="#a8324c" stroke="{INK}" stroke-width="4"/></g>
  <ellipse cx="-40" cy="-170" rx="11" ry="7" fill="#f08a9a" opacity=".7"/><ellipse cx="40" cy="-170" rx="11" ry="7" fill="#f08a9a" opacity=".7"/>
  {P(blob(-36,-6,28,15,50), fur, 5)}{P(blob(36,-6,28,15,51), fur, 5)}
  <g id="bunny-mango" opacity="0"><use href="#mango" x="-80" y="-108" width="60" height="75"/><use href="#mango" x="22" y="-108" width="60" height="75"/></g>
</g>'''

def mithu():
    g, dg = "#68b960", "#4f9a4a"
    return f'''
<g id="mithu">
  <g id="mithu-tail">{P(wpoly([(-14,52),(-58,150),(-18,138),(12,62)],60,2), "#e2574c", 5)}{P(wpoly([(0,56),(-26,160),(10,150),(20,62)],61,2), "#f2b134", 5)}</g>
  {P(blob(0,0,58,78,62,0.03), g)}
  <path d="{blob(10,22,34,44,63)}" fill="#bfe5a9"/>
  <g id="mithu-wing">{P(blob(-48,0,32,58,64,0.05,12), dg)}<path d="M-60,-10 q12,20 6,40 M-46,-20 q12,24 6,46" stroke="#3e7d3b" stroke-width="4" fill="none" stroke-linecap="round"/></g>
  {P(blob(6,-88,52,48,65,0.03), g)}
  {P(wpoly([(-12,-130),(4,-170),(20,-128)],66,2), "#f2c94c", 4)}
  <g id="mithu-eyes-open">{P(blob(24,-98,14,16,67,0.04,10), "#fff", 4)}<ellipse cx="28" cy="-96" rx="8" ry="10" fill="{INK}"/><circle cx="31" cy="-100" r="3" fill="#fff"/></g>
  <g id="mithu-eyes-happy" opacity="0"><path d="M12,-96 q14,-16 28,0" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/></g>
  <g id="mithu-eyes-sleep" opacity="0"><path d="M12,-98 q14,12 28,0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/></g>
  <g id="mithu-brow" opacity="0"><path d="M8,-124 l30,10" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></g>
  <g id="mithu-beak-low">{P(wpoly([(48,-80),(80,-72),(48,-62)],68,1.5), "#e07a24", 4)}</g>
  {P(wpoly([(46,-104),(96,-82),(48,-76)],69,1.5), "#f39a3d", 4)}
  <ellipse cx="-12" cy="-80" rx="10" ry="6" fill="#f08a9a" opacity=".7"/>
  <g id="mithu-mango" opacity="0"><use href="#mango" x="-40" y="60" width="56" height="70"/></g>
</g>'''

def tree():
    trunk = P(wpoly([(-60, 0), (-44, -260), (-70, -420), (-20, -400), (0, -470), (28, -400), (80, -430), (46, -260), (62, 0)], 70, 3, sub=2), "#9a6640")
    bark = "".join(f'<path d="{wpoly([(-20+k*14,-40-k*60),(-14+k*14,-90-k*60)],71+k,3,False,2)}" stroke="#6e4426" stroke-width="5" fill="none" stroke-linecap="round"/>' for k in range(3))
    blobs = [(-170, -480, 150, 130), (150, -490, 150, 135), (0, -630, 190, 150), (-90, -390, 140, 110), (100, -395, 145, 110), (-10, -470, 160, 140)]
    outline = "".join(P(blob(x, y, rx, ry, 80 + i, 0.06, 16), "#5fa052") for i, (x, y, rx, ry) in enumerate(blobs))
    fill = "".join(f'<path d="{blob(x, y, rx - 5, ry - 5, 80 + i, 0.06, 16)}" fill="#5fa052"/>' for i, (x, y, rx, ry) in enumerate(blobs))
    hi = "".join(f'<path d="{blob(x, y, rx, ry, 90 + i, 0.1, 10)}" fill="#79b866" opacity=".9"/>' for i, (x, y, rx, ry) in enumerate([(-100, -610, 70, 40), (110, -580, 60, 34), (-200, -500, 44, 26), (40, -470, 50, 30)]))
    leaves = "".join(f'<path d="M{x},{y} q8,-10 16,0 q-8,10 -16,0Z" fill="#3f7d3a"/>' for x, y in [(-150, -420), (-40, -560), (60, -420), (170, -470), (-220, -470), (20, -680), (120, -640)])
    return f'<g id="tree">{trunk}{bark}{outline}{fill}{hi}{leaves}</g>'

def basket():
    weave = "".join(f'<path d="M-112,{-10+k*22} q112,10 224,0" stroke="#a8692e" stroke-width="4" fill="none"/>' for k in range(1, 4))
    return f'''<g id="basket">
  <g id="bm-wrap">{"".join(f'<g class="bmango" id="bm{i}" opacity="0"><use href="#mango" x="{x-30}" y="{y-38}" width="60" height="75"/></g>' for i,(x,y) in enumerate([(-62,-30),(0,-34),(62,-30),(-31,-74),(31,-74)]))}</g>
  {P(wpoly([(-120,-22),(120,-22),(104,74),(-104,74)],100,2.5), "#d39654")}{weave}
  {P(blob(0,-22,124,14,101,0.03), "#e6b06e", 5)}
</g>'''

def plaque():
    return f'''<g id="plaque">
  {P(rrect(-24, -60, 48, 130, 110), "#8a5a36")}
  {P(rrect(-300, -120, 600, 120, 111, 2.5), "#d8b25a")}
  <path d="{rrect(-286,-108,572,96,112,2)}" fill="none" stroke="#a9852f" stroke-width="4"/>
  <circle cx="-272" cy="-60" r="6" fill="#a9852f"/><circle cx="272" cy="-60" r="6" fill="#a9852f"/>
  <text x="0" y="-44" text-anchor="middle" font-family="Kalam" font-weight="700" font-size="60" fill="#4a2f1d">गोलू और दोस्त</text>
</g>'''

def scenery():
    hills = (P(blob(160, 1250, 520, 230, 120, 0.03, 18), "#a8cf7c") + P(blob(900, 1270, 520, 250, 121, 0.03, 18), "#94c26b"))
    hut = f'''<g id="hut" transform="translate(860,1040)">
      {P(rrect(-90,-10,180,150,130), "#e7c79a")}
      {P(wpoly([(-120,0),(0,-110),(120,0)],131,3), "#c86f4f")}
      {P(rrect(-30,50,60,90,132), "#8a5a36", 5)}
      {P(blob(55,40,20,20,133,0.04,10), "#fbe7a6", 5)}
    </g>'''
    ground = P(wpoly([(-40, 1390), (300, 1372), (700, 1392), (1120, 1376), (1120, 1960), (-40, 1960)], 140, 6, sub=4), "#86b95c")
    patch = "".join(f'<path d="{blob(x, y, rx, ry, 141 + i, 0.08, 12)}" fill="#97c76c" opacity=".8"/>' for i, (x, y, rx, ry) in enumerate([(200, 1500, 160, 30), (820, 1560, 200, 34), (480, 1880, 260, 40)]))
    grass = "".join(f'<path d="M{x},{y} l-6,-20 M{x},{y} l6,-22" stroke="#5e8f3e" stroke-width="5" stroke-linecap="round"/>' for x, y in
                    [(60, 1460), (330, 1450), (560, 1480), (900, 1470), (1010, 1520), (120, 1700), (980, 1760), (760, 1860), (40, 1860), (300, 1900)])
    fl = "".join(f'<g transform="translate({x},{y})"><path d="M0,0 v-46" stroke="#4f7f35" stroke-width="5"/><use href="#flower" x="-16" y="-62" width="32" height="32"/></g>'
                 for x, y in [(40, 1560), (90, 1590), (980, 1640), (1030, 1600), (950, 1880)])
    rock = P(blob(1000, 1460, 50, 30, 150, 0.06), "#b9b0a3") + f'<path d="{blob(985,1450,18,8,151)}" fill="#d2cabd"/>'
    fence = "".join(P(rrect(x, 1300, 18, 80, 160 + i, 1.5), "#c9a06b", 4) for i, x in enumerate(range(560, 760, 40))) + \
            f'<path d="{wpoly([(552,1320),(770,1316)],170,2,False)}" stroke="#c9a06b" stroke-width="10" fill="none" stroke-linecap="round"/>' + \
            f'<path d="{wpoly([(552,1350),(770,1346)],171,2,False)}" stroke="#c9a06b" stroke-width="10" fill="none" stroke-linecap="round"/>'
    return hills + hut + fence + ground + patch + grass + fl + rock

def sky():
    clouds = "".join(f'<g class="cloud" id="cloud{i}">{"".join(P(blob(x+dx, y+dy, r*1.25, r, 200+i*5+k, 0.05, 12), "#fffaf0", 5) for k,(dx,dy,r) in enumerate([(-60,10,42),(0,-14,56),(62,10,42)]))}'
                     f'{"".join(f"<path d=\"{blob(x+dx, y+dy, r*1.25-5, r-5, 200+i*5+k, 0.05, 12)}\" fill=\"#fffaf0\"/>" for k,(dx,dy,r) in enumerate([(-60,10,42),(0,-14,56),(62,10,42)]))}</g>'
                     for i, (x, y) in enumerate([(170, 880), (840, 760), (520, 1010)]))
    stars = "".join(f'<path class="star" d="M{x},{y-12} L{x+4},{y-4} L{x+12},{y} L{x+4},{y+4} L{x},{y+12} L{x-4},{y+4} L{x-12},{y} L{x-4},{y-4}Z" fill="#fff4c2"/>'
                    for x, y in [(90, 120), (260, 300), (420, 90), (640, 240), (900, 140), (1000, 380), (160, 560), (760, 480), (980, 640), (330, 720)])
    return f'''
  <rect width="1080" height="1500" fill="#a9dbe6"/>
  <rect id="sky-dawn" width="1080" height="1500" fill="url(#gDawn)"/>
  <rect id="sky-sunset" width="1080" height="1500" fill="url(#gSunset)" opacity="0"/>
  <rect id="sky-night" width="1080" height="1500" fill="url(#gNight)" opacity="0"/>
  <g id="stars" opacity="0">{stars}</g>
  <g id="sun">{P(blob(0,0,78,78,210,0.03,16), "#f6d36b")}<path d="{blob(-18,-22,26,20,211)}" fill="#fae39a"/></g>
  <g id="moon" opacity="0">{P(blob(0,0,62,62,212,0.03,16), "#fbf1c7")}<circle cx="-18" cy="-10" r="10" fill="#efe0a8"/><circle cx="16" cy="18" r="7" fill="#efe0a8"/></g>
  {clouds}'''

# ---------------------------------------------------------------- HTML overlay pieces
NUMS = [("1", "एक"), ("2", "दो"), ("3", "तीन"), ("4", "चार"), ("5", "पाँच")]
NOTE_COLORS = ["#fff3b8", "#ffd9e2", "#d8f0ff", "#e2f6cf", "#ffe2c4"]

def overlays():
    cards = "".join(f'''
  <div class="note numcard" id="card{i}" style="background:{NOTE_COLORS[i]}; transform: rotate({[-4,3,-2,4,-3][i]}deg)">
    <div class="tape"></div>
    <div class="num">{n}</div>
    <div class="words">{hi} आम</div>
  </div>''' for i, (n, hi) in enumerate(NUMS))
    counter = "".join(f'<div class="cslot"><svg viewBox="-50 -70 100 125" class="cm" id="cm{i}"><use href="#mango"/></svg></div>' for i in range(5))
    return f'''
  <div class="note title" id="titlecard"><div class="pin"></div><div class="pin r"></div>
    <div class="t1">गोलू हाथी</div><div class="t2">और आम का पेड़</div></div>
  <div class="counter" id="counter">{counter}</div>
  {cards}
  <div class="bubble" id="bub-wah">वाह! पाँच आम!</div>
  <div class="note small" id="kyakarega" style="background:#ffe2c4; transform: rotate(-3deg)"><div class="tape"></div>गोलू क्या करेगा?</div>
  <div class="note small" id="endcard" style="background:#d8f0ff; transform: rotate(2deg)"><div class="tape"></div>कल फिर मिलेंगे!<div class="sub">बाय बाय बच्चों!</div></div>
  <div class="zzz" id="zzz"><span>z</span><span>Z</span><span>Z</span></div>
  <div class="zzz" id="zzz2"><span>z</span><span>Z</span><span>Z</span></div>'''

# ---------------------------------------------------------------- timeline
J = []  # JS lines
def tl(s): J.append(s)

def lip_js():
    out = []
    fps = lips["fps"]
    for ch, arr in lips["levels"].items():
        if ch == "nar": continue
        prev = 0
        for i, v in enumerate(arr):
            if v == prev: continue
            t = round(i / fps, 3)
            if ch in ("golu", "bunny"):
                if v == 0:
                    out.append(f'tl.set("#{ch}-mouth",{{opacity:0}},{t});tl.set("#{ch}-smile",{{opacity:1}},{t});')
                else:
                    out.append(f'tl.set("#{ch}-mouth",{{opacity:1,scaleY:{[0,0.45,0.75,1.05][v]}}},{t});tl.set("#{ch}-smile",{{opacity:0}},{t});')
            else:
                out.append(f'tl.set("#mithu-beak-low",{{rotation:{[0,9,15,22][v]},svgOrigin:"48 -72"}},{t});')
            prev = v
    return "\n".join(out)

def expr(ch, name, t, allx):
    """show one expression group for a character at time t"""
    for e in allx:
        tl(f'tl.set("#{ch}-eyes-{e}",{{opacity:{1 if e == name else 0}}},{t});')

GX = ["open", "happy", "sleep", "dizzy"]
BX = ["open", "happy", "sleep"]
MX = ["open", "happy", "sleep"]

def build_timeline():
    # base states
    expr("golu", "sleep", 0, GX)
    tl('tl.set("#cam",{scale:1.2,transformOrigin:"60% 72%"},0);')
    tl('tl.set(".hflower",{scale:0,transformOrigin:"50% 50%"},0);')
    tl('tl.set("#bunny-pos",{x:-420},0); tl.set("#mithu-pos",{x:520,y:-700},0);')
    tl('tl.set(".numcard,#titlecard,#kyakarega,#endcard,#bub-wah",{opacity:0,scale:0.6},0);')
    tl('tl.set("#counter",{opacity:0,y:-40},0); tl.set(".cm",{opacity:0.25,scale:0.8},0);')
    tl('tl.set("#golu-trunk",{svgOrigin:"222 -236"},0); tl.set("#mithu-wing",{svgOrigin:"-48 -40"},0);')
    tl('tl.set("#bunny-ear-l",{svgOrigin:"-28 -220"},0); tl.set("#bunny-ear-r",{svgOrigin:"28 -220"},0);')
    tl('tl.set("#letter",{x:520,y:-760,rotation:-20,opacity:0},0);')
    tl('tl.set("#bonk",{x:0,y:-900},0); tl.set(".dstar",{opacity:0},0);')
    tl('tl.set("#sun",{x:300,y:330},0);')
    tl('tl.set("#nightveil,#fireflies",{opacity:0},0);')
    # ambient loops (seekable: finite repeats)
    tl('tl.to("#golu-body",{scaleY:1.025,svgOrigin:"0 0",duration:1.4,ease:"sine.inOut",yoyo:true,repeat:31},0);')
    for i in range(3):
        tl(f'tl.fromTo("#cloud{i}",{{x:0}},{{x:{[90,-70,60][i]},duration:{DUR},ease:"none"}},0);')
    tl('tl.to("#sun",{y:300,duration:6,ease:"sine.out"},0);')
    # Zzz while sleeping
    tl('tl.set("#zzz",{opacity:1},0); tl.fromTo("#zzz span",{y:20,opacity:0},{y:-60,opacity:1,duration:0.6,stagger:0.25,ease:"sine.out"},0.05);')
    tl('tl.to("#zzz",{opacity:0,duration:0.2},1.3);')

    # ---- bonk 1.45
    tl('tl.to("#bonk",{y:0,duration:0.5,ease:"power2.in"},0.95);')
    tl('tl.to("#bonk",{x:160,y:-160,rotation:200,duration:0.45,ease:"power1.out"},1.45);')
    tl('tl.to("#bonk",{x:300,y:140,rotation:360,duration:0.5,ease:"power2.in"},1.9);')
    tl('tl.to("#bonk",{x:-480,y:180,duration:0.01},2.4);')  # it lands in basket area (hidden behind)
    tl('tl.set("#bonk",{opacity:0},2.41);')
    tl('tl.set("#tuk",{opacity:1,scale:0.2},1.45); tl.to("#tuk",{scale:1,duration:0.25,ease:"back.out(3)"},1.45); tl.to("#tuk",{opacity:0,duration:0.3},2.6);')
    tl('tl.to("#golu-body",{y:12,duration:0.08,yoyo:true,repeat:1},1.45);')
    tl('tl.fromTo("#cam",{x:-14},{x:0,duration:0.4,ease:"elastic.out(1,0.3)"},1.45);')
    expr("golu", "dizzy", 1.46, GX)
    tl('tl.set(".dstar",{opacity:1},1.46); tl.to("#dstars",{rotation:720,svgOrigin:"150 -370",duration:1.6,ease:"none"},1.46); tl.set(".dstar",{opacity:0},3.1);')
    expr("golu", "open", 3.1, GX)
    tl('tl.to("#cam",{scale:1,x:0,duration:1.6,ease:"power2.inOut"},2.9);')
    # wave hello with trunk 3.4–5.3
    tl('tl.to("#golu-trunk",{rotation:-115,duration:0.35,ease:"back.out(2)"},3.35);')
    tl('tl.to("#golu-trunk",{rotation:-95,duration:0.22,yoyo:true,repeat:5,ease:"sine.inOut"},3.7);')
    tl('tl.to("#golu-trunk",{rotation:0,duration:0.4,ease:"power2.out"},5.1);')
    tl('tl.to("#titlecard",{opacity:1,scale:1,duration:0.45,ease:"back.out(2.2)"},3.5);')
    tl('tl.to("#titlecard",{opacity:0,y:-60,duration:0.35,ease:"power2.in"},6.7);')
    expr("golu", "happy", 5.5, GX); expr("golu", "open", 6.9, GX)
    tl('tl.to("#counter",{opacity:1,y:0,duration:0.4,ease:"back.out(2)"},6.8);')

    # ---- counting
    tree_spots = [(-150, -440), (-40, -600), (90, -520), (180, -420), (0, -380)]
    for i in range(5):
        s0 = STEP0 + i * STEP
        land = s0 + 0.7
        tl(f'tl.to("#tm{i}",{{rotation:8,duration:0.06,yoyo:true,repeat:3}},{s0});')
        tl(f'tl.to("#tm{i}",{{x:"+=" + {BASKET_DX[i]},y:"+=" + {BASKET_DY[i]},duration:0.6,ease:"power1.in"}},{s0+0.1});')
        tl(f'tl.set("#tm{i}",{{opacity:0}},{land}); tl.set("#bm{i}",{{opacity:1}},{land});')
        tl(f'tl.fromTo("#bm{i}",{{y:-30,scaleY:0.7}},{{y:0,scaleY:1,duration:0.4,ease:"bounce.out"}},{land});')
        tl(f'tl.to("#card{i}",{{opacity:1,scale:1,duration:0.4,ease:"back.out(2.4)"}},{land+0.02});')
        tl(f'tl.to("#card{i}",{{opacity:0,scale:0.7,y:-30,duration:0.3,ease:"power2.in"}},{s0+STEP-0.35});')
        tl(f'tl.to("#cm{i}",{{opacity:1,scale:1.15,duration:0.25,ease:"back.out(3)"}},{land}); tl.to("#cm{i}",{{scale:1,duration:0.2}},{land+0.25});')
        tl(f'tl.fromTo("#cam",{{scale:1}},{{scale:1.05,transformOrigin:"50% 55%",duration:0.18,ease:"power2.out",yoyo:true,repeat:1}},{land});')
        # golu hop
        tl(f'tl.to("#golu-hop",{{y:-70,duration:0.22,ease:"power2.out",yoyo:true,repeat:1}},{land+0.05});')
        expr("golu", "happy", land, GX); expr("golu", "open", land + 1.3, GX)
        # running gag: a flower drops onto Golu's head
        tl(f'tl.fromTo("#hf{i}",{{scale:0,y:-160,rotation:-90}},{{scale:1,y:0,rotation:0,duration:0.5,ease:"bounce.out"}},{land+0.75});')
    expr("golu", "happy", 21.9, GX)
    tl('tl.to("#bub-wah",{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"},21.95); tl.to("#bub-wah",{opacity:0,duration:0.25},23.3);')
    tl('tl.to("#counter",{opacity:0,y:-40,duration:0.3},23.3);')
    expr("golu", "open", 23.3, GX)

    # ---- friends arrive
    for k in range(5):
        tl(f'tl.to("#bunny-pos",{{x:{-420 + (k+1)*84},duration:0.32,ease:"none"}},{23.7 + k*0.32});')
        tl(f'tl.to("#bunny-hop",{{y:-55,duration:0.16,ease:"power2.out",yoyo:true,repeat:1}},{23.7 + k*0.32});')
    tl('tl.to("#bunny-ear-l",{rotation:-12,duration:0.3,yoyo:true,repeat:5,ease:"sine.inOut"},23.7); tl.to("#bunny-ear-r",{rotation:12,duration:0.3,yoyo:true,repeat:5,ease:"sine.inOut"},23.7);')
    tl('tl.to("#mithu-pos",{x:0,y:0,duration:1.4,ease:"power2.out"},24.6);')
    tl('tl.to("#mithu-wing",{rotation:-35,duration:0.09,yoyo:true,repeat:15,ease:"sine.inOut"},24.6); tl.set("#mithu-wing",{rotation:0},26.05);')
    # leaf letter (like the paper planes in the reference)
    tl('tl.set("#letter",{opacity:1},24.7); tl.to("#letter",{x:0,y:0,rotation:-8,duration:1.6,ease:"sine.inOut"},24.7);')
    tl('tl.to("#letter",{y:"+=14",duration:0.5,yoyo:true,repeat:3,ease:"sine.inOut"},26.3);')
    tl('tl.to("#letter",{opacity:0,y:"+=40",duration:0.3},28.5);')
    tl('tl.set("#bunny-frown",{opacity:1},25.6); tl.set("#bunny-smile",{opacity:0},25.6); tl.set("#bunny-brows",{opacity:1},25.6);')
    tl('tl.set("#mithu-brow",{opacity:1},27.8);')
    tl('tl.set("#golu-brows,#golu-sweat",{opacity:1},28.6); tl.fromTo("#golu-sweat",{y:0},{y:30,duration:1.2,ease:"power1.in"},28.6);')
    tl('tl.to("#cam",{scale:1.12,transformOrigin:"55% 72%",duration:2.4,ease:"sine.inOut"},28.0);')
    tl('tl.to("#kyakarega",{opacity:1,scale:1,duration:0.35,ease:"back.out(2)"},29.35); tl.to("#kyakarega",{opacity:0,duration:0.25},30.9);')
    tl('tl.set("#golu-brows,#golu-sweat",{opacity:0},31.0);')
    tl('tl.to("#cam",{scale:1,duration:0.8,ease:"power2.inOut"},30.6);')

    # ---- sharing
    expr("golu", "happy", 31.1, GX)
    tl('tl.to("#golu-trunk",{rotation:-70,duration:0.3,ease:"back.out(2)"},31.2);')
    tosses = [("#bm4", "#bunny-mango", 31.7, -470, -40), ("#bm3", "#bunny-mango", 32.5, -420, -40), ("#bm2", "#mithu-mango", 33.3, 470, -680)]
    for j, (src, dst, t0, dx, dy) in enumerate(tosses):
        tl(f'tl.to("{src}",{{x:{dx},rotation:360,duration:0.55,ease:"none"}},{t0});')
        tl(f'tl.to("{src}",{{y:{min(0,dy)-200},duration:0.27,ease:"power2.out"}},{t0});')
        tl(f'tl.to("{src}",{{y:{dy},duration:0.28,ease:"power2.in"}},{t0+0.27});')
        tl(f'tl.set("{src}",{{opacity:0}},{t0+0.56});')
    tl('tl.set("#bunny-mango",{opacity:1},32.27); tl.set("#mithu-mango",{opacity:1},33.86);')
    tl('tl.set("#bunny-frown,#bunny-brows",{opacity:0},32.3); tl.set("#bunny-smile",{opacity:1},32.3);')
    expr("bunny", "happy", 32.3, BX); expr("mithu", "happy", 33.9, MX)
    tl('tl.set("#mithu-brow",{opacity:0},33.9);')
    tl('tl.to("#golu-trunk",{rotation:0,duration:0.4},34.0);')
    tl('tl.to("#bunny-hop",{y:-60,duration:0.2,ease:"power2.out",yoyo:true,repeat:7},34.3);')
    tl('tl.to("#mithu-wing",{rotation:-35,duration:0.1,yoyo:true,repeat:13,ease:"sine.inOut"},35.5); tl.set("#mithu-wing",{rotation:0},36.9);')
    expr("bunny", "open", 35.9, BX)
    # sash lands on Golu (callback to the reference's "so cool" sash)
    tl('tl.set("#golu-sash",{opacity:1},36.75); tl.fromTo("#golu-sash",{y:-420,rotation:-20,svgOrigin:"0 -150"},{y:0,rotation:0,duration:0.6,ease:"bounce.out"},36.75);')
    tl('tl.set("#golu-blush",{opacity:1},37.3);')
    tl('tl.to("#cam",{scale:1.14,transformOrigin:"58% 74%",duration:0.6,ease:"power2.out"},36.8); tl.to("#cam",{scale:1,duration:0.9,ease:"power2.inOut"},38.4);')
    tl('tl.set(".fheart",{opacity:0},0);')
    for k in range(7):
        t0 = 37.0 + k * 0.18
        tl(f'tl.fromTo("#fh{k}",{{opacity:1,y:0,scale:0.4}},{{y:-420,scale:1,opacity:0,duration:1.6,ease:"sine.out"}},{t0});')

    # ---- evening -> night
    tl('tl.to("#sun",{y:1300,duration:2.0,ease:"sine.in"},38.6);')
    tl('tl.to("#sky-sunset",{opacity:1,duration:1.2},38.7); tl.to("#sky-night",{opacity:1,duration:1.6},39.8);')
    tl('tl.to("#stars",{opacity:1,duration:1.2},40.2); tl.set("#moon",{x:820,y:420},0); tl.to("#moon",{opacity:1,y:300,duration:2},40.2);')
    tl('tl.to("#nightveil",{opacity:0.42,duration:2.2},39.2); tl.to("#fireflies",{opacity:1,duration:1},40.6);')
    for k in range(8):
        tl(f'tl.to("#ff{k}",{{x:{[30,-40,25,-20,40,-35,20,-25][k]},y:{[-30,20,-40,25,-20,30,-35,15][k]},duration:{1.6+0.2*k},yoyo:true,repeat:2,ease:"sine.inOut"}},40.6);')
    tl('tl.to(".star",{opacity:0.5,duration:0.5,yoyo:true,repeat:5,stagger:0.15},40.6);')
    expr("golu", "open", 38.9, GX)
    tl('tl.to("#endcard",{opacity:1,scale:1,duration:0.45,ease:"back.out(2)"},41.4);')
    tl('tl.to("#golu-trunk",{rotation:-110,duration:0.3,ease:"back.out(2)"},41.4); tl.to("#golu-trunk",{rotation:-90,duration:0.2,yoyo:true,repeat:3},41.7); tl.to("#golu-trunk",{rotation:0,duration:0.4},42.6);')
    expr("golu", "sleep", 43.2, GX); expr("bunny", "sleep", 43.4, BX); expr("mithu", "sleep", 43.5, MX)
    tl('tl.set("#zzz2",{opacity:1},43.3); tl.fromTo("#zzz2 span",{y:20,opacity:0},{y:-60,opacity:1,duration:0.5,stagger:0.2,ease:"sine.out"},43.3);')
    tl('tl.to("#cam",{scale:1.08,transformOrigin:"55% 70%",duration:5,ease:"sine.inOut"},39.5);')
    tl('tl.to("#fadeout",{opacity:1,duration:0.6},43.9);')
    # blinks (only visible while eyes-open shows)
    for t in [3.9, 6.2, 9.6, 12.9, 16.1, 19.4, 24.4, 26.9, 30.2, 34.9, 40.1, 42.0]:
        tl(f'tl.to("#golu-eyes-open",{{scaleY:0.1,transformOrigin:"50% 50%",duration:0.06,yoyo:true,repeat:1}},{t});')
    for t in [24.9, 28.4, 36.3, 40.7]:
        tl(f'tl.to("#bunny-eyes-open",{{scaleY:0.1,transformOrigin:"50% 50%",duration:0.06,yoyo:true,repeat:1}},{t});')
        tl(f'tl.to("#mithu-eyes-open",{{scaleY:0.1,transformOrigin:"50% 50%",duration:0.06,yoyo:true,repeat:1}},{t+0.7});')

# mango positions on tree (absolute) and basket slots (absolute) -> deltas
TREE_X, TREE_Y = 270, 1560
TREE_SPOTS = [(-150, -440), (-40, -600), (90, -520), (180, -420), (0, -380)]
GOLU_X, GOLU_Y = 690, 1590
BASKET_X, BASKET_Y = 450, 1640
SLOTS = [(-62, -30), (0, -34), (62, -30), (-31, -74), (31, -74)]
BASKET_DX = [BASKET_X + SLOTS[i][0] - (TREE_X + TREE_SPOTS[i][0]) for i in range(5)]
BASKET_DY = [BASKET_Y + SLOTS[i][1] - (TREE_Y + TREE_SPOTS[i][1]) for i in range(5)]

def tree_mangoes():
    return "".join(f'<g id="tm{i}" style="transform-box:fill-box;transform-origin:50% 0%"><use href="#mango" x="{TREE_X+x-36}" y="{TREE_Y+y-45}" width="72" height="90"/></g>' for i, (x, y) in enumerate(TREE_SPOTS))

def world():
    dstars = "".join(f'<path class="dstar" d="{wpoly([(150+90*math.cos(a)+12*math.cos(a+k*1.2566*2), -370+30*math.sin(a)+12*math.sin(a+k*1.2566*2)) for k in range(5)], 300+j, 0.5, True, 1)}" fill="#f6d36b" stroke="{INK}" stroke-width="3"/>'
                     for j, a in enumerate([0, 1.57, 3.14, 4.71]))
    hearts = "".join(f'<g class="fheart" id="fh{k}"><use href="#heart" x="{x-34}" y="{1450-34}" width="68" height="68"/></g>' for k, x in enumerate([150, 300, 450, 600, 760, 900, 1000]))
    ffs = "".join(f'<circle id="ff{k}" cx="{x}" cy="{y}" r="9" fill="#fff3a0" filter="url(#glow)"/>' for k, (x, y) in enumerate([(120, 1250), (340, 1100), (560, 1300), (780, 1150), (960, 1280), (220, 1480), (880, 1450), (480, 1050)]))
    letter = f'''<g id="letter"><g transform="translate(560,1180)">
      {P(wpoly([(-110,-60),(110,-70),(118,60),(-104,66)],400,3), "#cfe8a6")}
      <path d="M-100,-62 L4,6 L112,-68" stroke="{INK}" stroke-width="4" fill="none"/>
      <text x="6" y="44" text-anchor="middle" font-family="Kalam" font-weight="700" font-size="36" fill="{INK}">मुझे भी आम?</text>
    </g></g>'''
    return f'''
<svg id="world" viewBox="0 0 1080 1920" width="1080" height="1920" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gDawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fd3e6"/><stop offset="1" stop-color="#fbe7c6"/></linearGradient>
    <linearGradient id="gSunset" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7d7fc1"/><stop offset=".6" stop-color="#f1a07a"/><stop offset="1" stop-color="#ffd59a"/></linearGradient>
    <linearGradient id="gNight" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f2554"/><stop offset="1" stop-color="#4a4a8a"/></linearGradient>
    <filter id="glow" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    {mango_symbol()}{flower_symbol()}{heart_symbol()}
  </defs>
  {sky()}
  {scenery()}
  <g transform="translate({TREE_X},{TREE_Y})">{tree()}</g>
  {tree_mangoes()}
  <g transform="translate(540,1880)">{plaque()}</g>
  <g transform="translate({BASKET_X},{BASKET_Y})">{basket()}</g>
  <g transform="translate({GOLU_X},{GOLU_Y}) scale(1.05)"><g id="golu-hop"><g id="golu-body">{golu()}</g></g>
    <g id="dstars">{dstars}</g></g>
  <g id="bunny-pos"><g transform="translate(170,1690) scale(1.05)"><g id="bunny-hop">{bunny()}</g></g></g>
  <g id="mithu-pos"><g transform="translate(880,860) scale(0.95)"><g id="mithu-bob">{mithu()}</g></g></g>
  <g id="bonk"><use href="#mango" x="{GOLU_X+130}" y="{GOLU_Y-450}" width="72" height="90"/></g>
  <text id="tuk" opacity="0" x="{GOLU_X+40}" y="{GOLU_Y-470}" font-family="Baloo2" font-weight="800" font-size="110" fill="#e8667a" stroke="{INK}" stroke-width="7" paint-order="stroke" style="transform-box:fill-box;transform-origin:50% 50%">ठक!</text>
  {letter}
  {hearts}
  <rect id="nightveil" x="-100" y="1380" width="1300" height="700" fill="#1f2554" style="mix-blend-mode:multiply"/>
  <g id="fireflies">{ffs}</g>
</svg>'''

CSS = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-700-normal.woff2) format("woff2");font-weight:700}
@font-face{font-family:Kalam;src:url(assets/fonts/kalam-latin-700-normal.woff2) format("woff2");font-weight:700}
@font-face{font-family:Kalam;src:url(assets/fonts/kalam-devanagari-700-normal.woff2) format("woff2");font-weight:700;unicode-range:U+0900-097F, U+1CD0-1CF9, U+200C-200D, U+20A8, U+20B9, U+25CC, U+A830-A839, U+A8E0-A8FF}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F, U+1CD0-1CF9, U+200C-200D, U+20A8, U+20B9, U+25CC, U+A830-A839, U+A8E0-A8FF}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-700-normal.woff2) format("woff2");font-weight:700;unicode-range:U+0900-097F, U+1CD0-1CF9, U+200C-200D, U+20A8, U+20B9, U+25CC, U+A830-A839, U+A8E0-A8FF}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden;background:#f6ecd8}
#root{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Baloo2,sans-serif;color:#2b2233}
#cam{position:absolute;inset:0;transform-origin:50% 60%}
#world{position:absolute;left:0;top:0}
.paper{position:absolute;inset:0;background:url(assets/paper.png);mix-blend-mode:multiply;opacity:.22;pointer-events:none}
.vignette{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 55%,transparent 55%,rgba(60,35,20,.28) 100%);pointer-events:none}
#fadeout{position:absolute;inset:0;background:#141633;opacity:0}
.note{position:absolute;left:50%;top:260px;margin-left:-380px;width:760px;padding:34px 30px 30px;background:#fff6dc;border:5px solid #2b2233;border-radius:14px 22px 18px 26px;box-shadow:8px 10px 0 rgba(43,34,51,.18);text-align:center}
.tape{position:absolute;left:50%;top:-24px;width:170px;height:46px;margin-left:-85px;background:rgba(240,220,160,.85);border:3px solid rgba(43,34,51,.35);transform:rotate(-3deg)}
.pin{position:absolute;top:14px;left:26px;width:28px;height:28px;border-radius:50%;background:#e8667a;border:4px solid #2b2233}
.pin.r{left:auto;right:26px;background:#68b960}
.title .t1{font-size:124px;font-weight:800;line-height:1;color:#e8667a;-webkit-text-stroke:5px #2b2233;paint-order:stroke fill}
.title .t2{font-family:Kalam;font-size:64px;font-weight:700;margin-top:6px}
.numcard{top:250px;width:520px;margin-left:-260px;padding:20px 20px 28px}
.numcard .num{font-size:300px;font-weight:800;line-height:.95;color:#f2b134;-webkit-text-stroke:9px #2b2233;paint-order:stroke fill}
.numcard .words{font-family:Baloo2;font-size:84px;font-weight:700;line-height:1.1}
.numcard .dot{color:#e8667a}
.counter{position:absolute;top:70px;left:50%;margin-left:-300px;width:600px;height:130px;display:flex;justify-content:space-around;align-items:center;background:#fff6dc;border:5px solid #2b2233;border-radius:20px 14px 24px 16px;transform:rotate(-1.5deg);box-shadow:6px 8px 0 rgba(43,34,51,.18)}
.cslot{width:96px;height:110px}.cm{width:96px;height:110px;overflow:visible}
.bubble{position:absolute;left:520px;top:880px;padding:22px 36px;background:#fff;border:5px solid #2b2233;border-radius:40px;font-size:58px;font-weight:800;white-space:nowrap}
.bubble:after{content:"";position:absolute;left:120px;bottom:-34px;border:18px solid transparent;border-top:24px solid #2b2233}
.note.small{top:330px;width:700px;margin-left:-350px;font-family:Kalam;font-size:76px;font-weight:700;padding:40px 20px 30px}
.note.small .sub{font-size:52px;color:#e8667a}
.zzz{position:absolute;left:880px;top:1150px;font-family:Kalam;font-weight:700;color:#2b2233;opacity:0}
.zzz span{display:inline-block;margin-right:6px}
.zzz span:nth-child(1){font-size:46px}.zzz span:nth-child(2){font-size:64px}.zzz span:nth-child(3){font-size:84px}
#zzz2{color:#fff4c2;left:860px;top:1100px}
"""

def html():
    build_timeline()
    js = "\n".join(J) + "\n" + lip_js()
    return f'''<!doctype html>
<html lang="en" data-resolution="portrait">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="assets/gsap.min.js"></script>
<style>{CSS}</style></head>
<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920">
  <audio id="soundtrack" class="clip" src="assets/soundtrack.mp3" data-start="0" data-duration="{DUR}" data-volume="1"></audio>
  <div id="stage" class="clip" data-start="0" data-duration="{DUR}" data-track-index="0">
    <div id="cam">{world()}
      {overlays()}
    </div>
    <div class="paper"></div><div class="vignette"></div><div id="fadeout"></div>
  </div>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{js}
tl.set({{}}, {{}}, {DUR});
window.__timelines = window.__timelines || {{}};
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body></html>'''

open(f"{PROJ}/index.html", "w").write(html())
print("written", len(J), "timeline lines")
