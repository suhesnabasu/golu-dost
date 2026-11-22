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
  <ellipse cx="0" cy="8" rx="230" ry="34" fill="url(#gShadow)"/>
  <g id="g-body">
    <rect x="-150" y="-110" width="70" height="118" rx="34" fill="#7f9de6"/><rect x="-62" y="-110" width="70" height="118" rx="34" fill="#87a4ea"/>
    <rect x="30" y="-110" width="70" height="118" rx="34" fill="#87a4ea"/><rect x="112" y="-110" width="70" height="118" rx="34" fill="#7f9de6"/>
    <ellipse cx="-115" cy="2" rx="30" ry="9" fill="#eef3ff"/><ellipse cx="-27" cy="2" rx="30" ry="9" fill="#eef3ff"/><ellipse cx="65" cy="2" rx="30" ry="9" fill="#eef3ff"/><ellipse cx="147" cy="2" rx="30" ry="9" fill="#eef3ff"/>
    <path d="M-170,-170 q-60,10 -60,70" stroke="#7f9de6" stroke-width="14" fill="none" stroke-linecap="round"/>
    <ellipse cx="0" cy="-175" rx="190" ry="140" fill="url(#gBody)"/>
    <ellipse cx="-20" cy="-130" rx="110" ry="60" fill="#ffffff" opacity=".18"/>
  </g>
  <g id="g-head">
    <g id="g-ear"><ellipse cx="60" cy="-345" rx="110" ry="125" fill="url(#gEar)"/><ellipse cx="62" cy="-340" rx="74" ry="88" fill="url(#gEarIn)"/></g>
    <g id="g-trunk">
      <path d="M268,-300 C330,-290 360,-220 336,-150" stroke="#86a7ef" stroke-width="64" fill="none" stroke-linecap="round"/>
      <path d="M262,-310 C318,-300 344,-240 326,-170" stroke="#c4d6fb" stroke-width="18" fill="none" stroke-linecap="round" opacity=".7"/>
    </g>
    <circle cx="170" cy="-350" r="135" fill="url(#gHead)"/>
    <ellipse cx="120" cy="-420" rx="60" ry="36" fill="#ffffff" opacity=".28"/>
    <path d="M150,-482 q-10,-34 14,-40 q18,-2 14,18" stroke="#6688dd" stroke-width="9" fill="none" stroke-linecap="round"/>
    <path d="M178,-484 q2,-36 26,-34 q16,6 6,24" stroke="#6688dd" stroke-width="9" fill="none" stroke-linecap="round"/>
    <g id="g-eyes">
      <ellipse cx="210" cy="-375" rx="40" ry="48" fill="url(#gEye)"/><ellipse cx="128" cy="-380" rx="36" ry="44" fill="url(#gEye)"/>
      <ellipse class="pup" cx="218" cy="-368" rx="25" ry="30" fill="url(#gPupil)"/><ellipse class="pup" cx="136" cy="-372" rx="22" ry="27" fill="url(#gPupil)"/>
      <circle cx="228" cy="-382" r="10" fill="#fff"/><circle cx="144" cy="-386" r="9" fill="#fff"/>
      <circle cx="210" cy="-356" r="4.5" fill="#fff"/><circle cx="128" cy="-360" r="4" fill="#fff"/>
    </g>
    <g id="g-happy" opacity="0">
      <path d="M180,-372 q30,-34 60,0" stroke="#3a2a55" stroke-width="11" fill="none" stroke-linecap="round"/>
      <path d="M100,-378 q28,-30 56,0" stroke="#3a2a55" stroke-width="11" fill="none" stroke-linecap="round"/>
    </g>
    <ellipse cx="246" cy="-300" rx="34" ry="22" fill="url(#gCheek)"/><ellipse cx="100" cy="-306" rx="30" ry="20" fill="url(#gCheek)"/>
    <path id="g-smile" d="M150,-300 q30,30 64,0" stroke="#7a2140" stroke-width="9" fill="#d23a5e" stroke-linecap="round"/>
    <g id="g-mouth" opacity="0" style="transform-box:fill-box;transform-origin:50% 0%">
      <ellipse cx="182" cy="-280" rx="34" ry="34" fill="#7a1838"/><ellipse cx="182" cy="-262" rx="20" ry="11" fill="#ff8fa8"/>
    </g>
  </g>
</g>'''

