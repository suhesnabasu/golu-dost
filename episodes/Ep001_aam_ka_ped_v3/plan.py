"""Fit Fish lines to an episode's original cue sheet: speed up to MAXT, else slide later."""
import json, subprocess, os, sys, numpy as np, soundfile as sf
MAXT = 1.25
def plan(cues, info, dur, prefix):
    out = []; prev_end = -1
    for k, (lid, t0) in enumerate(cues):
        d = info[prefix + lid]["dur"]
        nxt = cues[k + 1][1] if k + 1 < len(cues) else dur - 0.3
        start = max(t0, prev_end + 0.12)
        room = nxt - start - 0.12
        tempo = min(MAXT, max(1.0, d / room)) if room > 0 else MAXT
        nd = d / tempo
        out.append([lid, round(start, 2), round(tempo, 3), round(nd, 2)]); prev_end = start + nd
    return out, prev_end
def render(pl, src, dst, prefix):
    os.makedirs(dst, exist_ok=True); info = {}
    for lid, start, tempo, nd in pl:
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{src}/{prefix}{lid}.wav", "-af", f"atempo={tempo}", "-ar", "44100", "-ac", "1", f"{dst}/{lid}.wav"], check=True)
        info[lid] = round(len(sf.read(f"{dst}/{lid}.wav")[0]) / 44100, 2)
    return info
