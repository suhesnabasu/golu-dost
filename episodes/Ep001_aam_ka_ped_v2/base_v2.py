# Loads the house drawing kit (defs, GOLU v2, KIDS, cloud, flower, f3d filter) from gen_episode_template.py
import re, math
TPL = "/home/claude/golu_pipeline/golu_pipeline/gen_episode_template.py"
def load():
    src = open(TPL).read()
    head = src[src.index("COLS = ["):src.index("def overlays")]
    ns = {"math": math}
    exec(head, ns)
    html_src = src[src.index("def html"):]
    f3d = re.search(r'(<filter id="f3d".*?</filter>)', html_src, re.S).group(1)
    ns["F3D"] = f3d
    return ns
FONT_CSS = """
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-latin-800-normal.woff2) format("woff2");font-weight:800}
@font-face{font-family:Baloo2;src:url(assets/fonts/baloo-2-devanagari-800-normal.woff2) format("woff2");font-weight:800;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
"""
def lip_events(levels, fps, mouth_sel, smile_sel, scale_origin, skip=()):
    """golu-style lip sync (opacity toggle + scaleY with svgOrigin). skip = [(t0,t1)] windows where the mouth is busy."""
    out = []; prev = 0
    def busy(t): return any(a - 1e-6 <= t < b for a, b in skip)
    for i, v in enumerate(levels):
        t = round(i / fps, 3)
        if busy(t): prev = -1; continue
        if v == prev: continue
        if v == 0: out.append(f'tl.set("{mouth_sel}",{{opacity:0}},{t});tl.set("{smile_sel}",{{opacity:1}},{t});')
        else: out.append(f'tl.set("{mouth_sel}",{{opacity:1,scaleY:{[0,.5,.8,1.1][v]},svgOrigin:"{scale_origin}"}},{t});tl.set("{smile_sel}",{{opacity:0}},{t});')
        prev = v
    return out
def kid_lip_events(levels, fps, kid, lag=0):
    out = []; prev = 0
    for i, v in enumerate(levels):
        if v == prev: continue
        t = round((i + lag) / fps, 3); k = f"#{kid}"
        big, small, smile = (1, 0, 0) if v >= 2 else ((0, 1, 0) if v == 1 else (0, 0, 1))
        out.append(f'tl.set("{k} .kmouth",{{opacity:{big}}},{t});tl.set("{k} .ksmall",{{opacity:{small}}},{t});tl.set("{k} .ksmile",{{opacity:{smile}}},{t});')
        prev = v
    return out
def segments(levels, fps, gap=0.35):
    """talking segments [(t0,t1)] from a level list"""
    segs = []; on = None; last = None
    for i, v in enumerate(levels):
        t = i / fps
        if v:
            if on is None: on = t
            last = t
        elif on is not None and t - last > gap:
            segs.append((on, last + 1 / fps)); on = None
    if on is not None: segs.append((on, last + 1 / fps))
    return segs
