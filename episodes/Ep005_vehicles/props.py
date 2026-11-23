"""Ep5 props (original, glossy soft-3D, no outlines). Every vehicle: origin = bottom-centre (wheels touch y=0), faces RIGHT."""
import math

def rg(id_, stops, cx="35%", cy="30%", r="75%"):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<radialGradient id="{id_}" cx="{cx}" cy="{cy}" r="{r}">{s}</radialGradient>'

def lg(id_, stops, y2=1):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="0" y2="{y2}">{s}</linearGradient>'

PROP_DEFS = "".join([
    rg("gRed", [(0, "#ffb0a8"), (.4, "#ff5a4f"), (1, "#c92a22")], "35%", "25%", "85%"),
    rg("gRedT", [(0, "#ffa39b"), (.45, "#ff3b3b"), (1, "#b81818")], "35%", "25%", "85%"),
    rg("gYel", [(0, "#fff0a8"), (.45, "#ffb81c"), (1, "#e08a00")], "35%", "25%", "85%"),
    rg("gBlueC", [(0, "#c6e8ff"), (.45, "#3fa9f5"), (1, "#1a6fc0")], "35%", "25%", "85%"),
    rg("gGrn", [(0, "#c8f5c0"), (.45, "#3fbf5a"), (1, "#1f8a36")], "35%", "25%", "85%"),
    rg("gTyre", [(0, "#5a5f70"), (.7, "#2f3340"), (1, "#1c1f28")], "40%", "35%", "70%"),
    rg("gHub", [(0, "#ffffff"), (1, "#c3c8d6")], "40%", "35%", "70%"),
    rg("gHubY", [(0, "#fff6b0"), (1, "#ffc21c")], "40%", "35%", "70%"),
    rg("gLamp", [(0, "#ffffff"), (.5, "#fff3a0"), (1, "#ffc93c")], "40%", "35%", "70%"),
    rg("gPuff", [(0, "#ffffff"), (.7, "#f4f8ff"), (1, "#d6e2f2")], "40%", "35%", "70%"),
    rg("gBeaconR", [(0, "#ffd0d0"), (.5, "#ff2a2a"), (1, "#b00000")], "40%", "35%", "70%"),
    rg("gBeaconB", [(0, "#d0e8ff"), (.5, "#2a8cff"), (1, "#0050b0")], "40%", "35%", "70%"),
    rg("gGlow", [(0, "rgba(255,240,150,.9)"), (1, "rgba(255,240,150,0)")], "50%", "50%", "50%"),
    rg("gGlowR", [(0, "rgba(255,80,80,.8)"), (1, "rgba(255,80,80,0)")], "50%", "50%", "50%"),
    lg("gWin", [(0, "#e8f7ff"), (1, "#8fd0ff")]),
    lg("gRoad", [(0, "#8a8fa3"), (.25, "#6b6f80"), (1, "#5a5e6e")]),
    lg("gVerge", [(0, "#f0d39a"), (1, "#d9b070")]),
    lg("gWoodF", [(0, "#f0b878"), (1, "#c07a40")]),
    lg("gStone", [(0, "#ffffff"), (1, "#dcdfe8")]),
    lg("gGrass", [(0, "#8be064"), (1, "#4fb83a")]),
    lg("gField", [(0, "#c8f08a"), (1, "#8fd65a")]),
])

def shine(x, y, rx, ry, rot=-20, op=.55):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#fff" opacity="{op}" transform="rotate({rot} {x} {y})"/>'

def wheel(cls, x, y, r, hub="gHub"):
    spokes = "".join(f'<rect x="{-r*0.08:.1f}" y="{-r*0.55:.1f}" width="{r*0.16:.1f}" height="{r*1.1:.1f}" rx="{r*0.08:.1f}" fill="#9aa1b4" transform="rotate({a})"/>' for a in (0, 60, 120))
    return (f'<g transform="translate({x},{y})"><circle r="{r}" fill="url(#gTyre)"/>'
            f'<g class="{cls}">{spokes}</g><circle r="{r*0.42:.1f}" fill="url(#{hub})"/>'
            f'<circle cx="{-r*0.3:.1f}" cy="{-r*0.35:.1f}" r="{r*0.14:.1f}" fill="#fff" opacity=".45"/></g>')

def window(x, y, w, h, r=14):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="url(#gWin)"/>'
            f'<path d="M{x+w*0.25:.0f},{y+4} L{x+w*0.45:.0f},{y+4} L{x+w*0.2:.0f},{y+h-4} L{x+4},{y+h-4} L{x+4},{y+h*0.7:.0f}Z" fill="#fff" opacity=".6"/>')

def shadow(w, op=.22):
    return f'<ellipse cx="0" cy="4" rx="{w}" ry="16" fill="#1a2a10" opacity="{op}"/>'

def puffs(prefix, x, y, n=4):
    return "".join(f'<circle class="{prefix}" id="{prefix}{i}" cx="{x}" cy="{y}" r="{22+i*6}" fill="url(#gPuff)" opacity="0"/>' for i in range(n))

def train_engine(wc="wT"):
    return (f'<g>'
            f'<rect x="-215" y="-78" width="430" height="44" rx="16" fill="#ffc93c"/>'
            f'<rect x="-60" y="-178" width="240" height="112" rx="52" fill="url(#gRed)"/>'
            f'<circle cx="178" cy="-122" r="54" fill="#d93a30"/><circle cx="178" cy="-122" r="36" fill="#ff7a6e"/>'
            f'<circle cx="196" cy="-120" r="16" fill="url(#gLamp)"/>'
            f'<rect x="-50" y="-188" width="20" height="124" rx="10" fill="#ffc93c"/><rect x="40" y="-188" width="20" height="124" rx="10" fill="#ffc93c"/>'
            f'<path d="M108,-176 h48 l10,-58 h-68z" fill="#3a3f4f"/><rect x="92" y="-248" width="80" height="22" rx="11" fill="#ffc93c"/>'
            f'<rect x="-205" y="-262" width="160" height="196" rx="26" fill="url(#gRed)"/>'
            f'<rect x="-222" y="-288" width="196" height="36" rx="18" fill="#ffc93c"/>'
            f'{window(-186, -236, 110, 76)}'
            f'{shine(10, -150, 70, 16, -6, .45)}{shine(-150, -250, 40, 8, 0, .5)}'
            f'<path d="M212,-34 l38,0 l-20,-40z" fill="#ffc93c"/>'
            f'{wheel(wc, -150, -46, 46)}{wheel(wc, -46, -46, 46)}{wheel(wc, 80, -32, 32)}{wheel(wc, 150, -32, 32)}'
            f'<rect x="-170" y="-52" width="150" height="12" rx="6" fill="#ffd96a"/>'
            f'</g>')

def coach(wc="wT", body="gBlueC", trim="#ffc93c"):
    wins = "".join(window(-150 + i * 78, -214, 60, 60, 12) for i in range(4))
    return (f'<g><rect x="-180" y="-250" width="360" height="200" rx="34" fill="url(#{body})"/>'
            f'<rect x="-190" y="-268" width="380" height="30" rx="15" fill="{trim}"/>'
            f'<rect x="-180" y="-130" width="360" height="22" fill="{trim}" opacity=".9"/>{wins}'
            f'{shine(-80, -238, 70, 10, 0, .45)}'
            f'<rect x="-200" y="-74" width="20" height="12" rx="4" fill="#3a3f4f"/>'
            f'{wheel(wc, -110, -40, 38)}{wheel(wc, 110, -40, 38)}</g>')

def train(id_, wc):
    return (f'<g id="{id_}">{shadow(900, .16)}'
            f'<g transform="translate(-820,0)">{coach(wc, "gYel", "#ff7a1c")}</g>'
            f'<g transform="translate(-420,0)">{coach(wc)}</g>'
            f'{train_engine(wc)}</g>')

def bus(id_, wc="wB"):
    wins = "".join(window(-230 + i * 88, -258, 70, 74, 14) for i in range(4))
    return (f'<g id="{id_}">{shadow(270)}<g class="vbody">'
            f'<rect x="-262" y="-300" width="524" height="252" rx="46" fill="url(#gYel)"/>'
            f'<rect x="-262" y="-150" width="524" height="30" fill="#ff7a1c"/>'
            f'{wins}'
            f'<rect x="130" y="-258" width="70" height="196" rx="14" fill="#ffd56a"/>{window(138, -250, 54, 84, 12)}'
            f'<path d="M212,-258 h28 q20,0 20,22 v104 h-48z" fill="url(#gWin)"/>'
            f'<circle cx="244" cy="-86" r="16" fill="url(#gLamp)"/>'
            f'<rect x="-270" y="-72" width="540" height="24" rx="12" fill="#e08a00"/>'
            f'{shine(-140, -284, 100, 12, 0, .5)}</g>'
            f'{wheel(wc, -160, -46, 48)}{wheel(wc, 160, -46, 48)}</g>')

def tractor(id_, wc="wR"):
    return (f'<g id="{id_}">{shadow(220)}<g class="vbody">'
            f'<rect x="-30" y="-178" width="210" height="96" rx="40" fill="url(#gGrn)"/>'
            f'<rect x="150" y="-160" width="32" height="64" rx="10" fill="#2c7a3a"/>'
            f'<path d="M168,-150 h10 M168,-134 h10 M168,-118 h10" stroke="#a8e6a0" stroke-width="5" stroke-linecap="round"/>'
            f'<rect x="96" y="-262" width="18" height="90" rx="9" fill="#3a3f4f"/>'
            f'<rect x="-190" y="-200" width="180" height="120" rx="30" fill="url(#gGrn)"/>'
            f'<rect x="-178" y="-318" width="12" height="130" rx="6" fill="#2c7a3a"/><rect x="-36" y="-318" width="12" height="130" rx="6" fill="#2c7a3a"/>'
            f'<rect x="-200" y="-336" width="200" height="30" rx="15" fill="#ffd23f"/>'
            f'<rect x="-120" y="-238" width="44" height="44" rx="12" fill="#ffd23f"/>'
            f'{shine(40, -164, 60, 12, -4, .5)}</g>'
            f'{wheel(wc, -100, -96, 96, "gHubY")}{wheel(wc, 130, -52, 52, "gHubY")}'
            f'{puffs("smk", 105, -280, 4)}</g>')

def firetruck(id_, wc="wF"):
    rungs = "".join(f'<rect x="{-226 + i*40}" y="-262" width="8" height="34" rx="4" fill="#ffffff"/>' for i in range(9))
    return (f'<g id="{id_}">{shadow(275)}<g class="vbody">'
            f'<rect x="-262" y="-220" width="390" height="172" rx="30" fill="url(#gRedT)"/>'
            f'<rect x="110" y="-270" width="156" height="222" rx="40" fill="url(#gRedT)"/>'
            f'{window(150, -246, 92, 78, 16)}'
            f'<rect x="-262" y="-130" width="528" height="22" fill="#ffffff" opacity=".95"/>'
            f'<rect x="-240" y="-268" width="340" height="10" rx="5" fill="#ffffff"/><rect x="-240" y="-232" width="340" height="10" rx="5" fill="#ffffff"/>{rungs}'
            f'<circle cx="-120" cy="-170" r="30" fill="#c41414"/><circle cx="-120" cy="-170" r="18" fill="#ffd84a"/>'
            f'<rect x="-220" y="-200" width="60" height="50" rx="10" fill="#ff6b6b"/>'
            f'<circle cx="250" cy="-84" r="16" fill="url(#gLamp)"/>'
            f'<rect x="-270" y="-72" width="540" height="24" rx="12" fill="#c41414"/>'
            f'<g id="beacon"><rect x="160" y="-298" width="60" height="30" rx="14" fill="#3a3f4f"/>'
            f'<circle class="bcR" cx="176" cy="-290" r="16" fill="url(#gBeaconR)"/><circle class="bcB" cx="204" cy="-290" r="16" fill="url(#gBeaconB)"/>'
            f'<circle id="bglow" cx="190" cy="-292" r="70" fill="url(#gGlowR)" opacity="0"/></g>'
            f'{shine(-100, -206, 110, 10, 0, .45)}</g>'
            f'{wheel(wc, -170, -46, 48)}{wheel(wc, -50, -46, 48)}{wheel(wc, 170, -46, 48)}</g>')

def boom_gate():
    # post at (0,0) bottom; arm pivot at (0,-120); arm points right when down (rotation 0), up = -80
    stripes = "".join(f'<rect x="{30 + i*60}" y="-12" width="30" height="24" fill="#ffffff"/>' for i in range(5))
    return (f'<g id="gate">{shadow(40, .2)}<rect x="-18" y="-140" width="36" height="140" rx="12" fill="#3a3f4f"/>'
            f'<g transform="translate(0,-110)"><g id="garm"><rect x="0" y="-12" width="330" height="24" rx="12" fill="#ff4d4d"/>{stripes}'
            f'<circle cx="318" cy="0" r="9" fill="#fff3a0"/></g>'
            f'<circle cx="0" cy="0" r="22" fill="#ff4d4d"/><circle cx="0" cy="0" r="8" fill="#fff"/></g></g>')

def signal():
    return (f'<g id="signal">{shadow(30, .2)}<rect x="-9" y="-250" width="18" height="250" rx="9" fill="#3a3f4f"/>'
            f'<rect x="-34" y="-300" width="68" height="70" rx="22" fill="#2a2e3a"/>'
            f'<circle cx="-14" cy="-265" r="12" fill="#5a1a1a"/><circle id="sigR" cx="-14" cy="-265" r="12" fill="#ff3b3b"/>'
            f'<circle cx="14" cy="-265" r="12" fill="#1a4a2a"/><circle id="sigG" cx="14" cy="-265" r="12" fill="#3bdc6b" opacity="0"/>'
            f'<circle id="sigGlow" cx="-14" cy="-265" r="40" fill="url(#gGlowR)"/>'
            f'<path d="M-40,-200 l80,40 M40,-200 l-80,40" stroke="#ffffff" stroke-width="12" stroke-linecap="round"/>'
            f'<path d="M-40,-200 l80,40 M40,-200 l-80,40" stroke="#ff4d4d" stroke-width="12" stroke-linecap="round" stroke-dasharray="14 14"/></g>')

def milestone():
    return (f'<g id="mstone">{shadow(60, .2)}<path d="M-52,0 V-60 Q-52,-112 0,-112 Q52,-112 52,-60 V0Z" fill="url(#gStone)"/>'
            f'<path d="M-52,-60 Q-52,-112 0,-112 Q52,-112 52,-60Z" fill="#ffc21c"/>'
            f'<rect x="-30" y="-46" width="60" height="8" rx="4" fill="#c3c8d6"/><rect x="-22" y="-28" width="44" height="8" rx="4" fill="#c3c8d6"/></g>')

def fence(y0=1290, y1=1345):
    s = ""
    for x in range(30, 1080, 130):
        s += f'<rect x="{x-14}" y="{y0-18}" width="28" height="{y1-y0+30}" rx="10" fill="url(#gWoodF)"/>'
    s += f'<rect x="0" y="{y0+4}" width="1080" height="16" rx="8" fill="url(#gWoodF)"/><rect x="0" y="{y0+32}" width="1080" height="14" rx="7" fill="url(#gWoodF)"/>'
    return s

def rails(y=1048):
    sl = "".join(f'<rect x="{x}" y="{y-6}" width="34" height="22" rx="4" fill="#a8714a"/>' for x in range(-20, 1100, 70))
    return (f'<rect x="0" y="{y-18}" width="1080" height="44" fill="#c9b08a"/>{sl}'
            f'<rect x="0" y="{y-10}" width="1080" height="10" rx="4" fill="#9aa3b5"/><rect x="0" y="{y-10}" width="1080" height="3" fill="#e6ebf5"/>')

def road(y0=1150, y1=1300):
    dashes = "".join(f'<rect x="{x}" y="{(y0+y1)//2+18}" width="70" height="10" rx="5" fill="#fff6d6"/>' for x in range(20, 1080, 140))
    return (f'<rect x="0" y="{y0-36}" width="1080" height="40" fill="url(#gVerge)"/>'
            f'<rect x="0" y="{y0}" width="1080" height="{y1-y0}" fill="url(#gRoad)"/>{dashes}')

if __name__ == "__main__":
    # standalone prop sheet for Stage 5 check
    import sys
    sys.path.insert(0, "/home/claude/ep5work")
    items = [(train_engine(), 300, 380), (coach(), 760, 380), (bus("b"), 300, 760), (tractor("t"), 780, 760),
             (firetruck("f"), 300, 1140), (boom_gate(), 620, 1100), (signal(), 900, 1140), (milestone(), 940, 1400)]
    body = "".join(f'<g transform="translate({x},{y})" filter="url(#f3d)">{s}</g>' for s, x, y in items)
    F3D = open("/home/claude/ep5work/f3d.txt").read()
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1500" width="1080" height="1500"><defs>{PROP_DEFS}{F3D}</defs><rect width="1080" height="1500" fill="#bfe9ff"/>{rails(1440)}{body}</svg>'
    open("/home/claude/ep5work/propsheet.svg", "w").write(svg)
    print("ok")
