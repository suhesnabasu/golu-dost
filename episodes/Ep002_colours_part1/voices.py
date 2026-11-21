"""Natural-sounding character voices + a kids' chorus (Kokoro TTS, Apache-2.0).
LINES: (id, role, lang, text). Roles: golu, bunny, mithu, nar, kids (= 3 child-like voices together).
Writes <outdir>/<id>.wav (44.1 kHz mono) and info.json with durations."""
import json, os, subprocess, sys
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

KDIR = os.environ.get("KOKORO_DIR", "/home/claude/tts")
k = Kokoro(f"{KDIR}/kokoro-v1.0.onnx", f"{KDIR}/voices-v1.0.bin")
# (voice for Hindi, voice for English, pitch factor, speed) — mild pitch only, so voices stay human
ROLE = {"golu": ("hf_beta", "af_bella", 1.08, 1.0), "bunny": ("hf_alpha", "af_sky", 1.14, 1.05),
        "mithu": ("hf_beta", "af_nova", 1.22, 1.1), "nar": ("hf_alpha", "af_heart", 1.0, 0.95)}
KIDS = [("hf_beta", "af_bella", 1.20, 0.000), ("hf_alpha", "af_sky", 1.26, 0.028), ("hf_alpha", "af_nova", 1.16, 0.051)]


def tts(text, voice, lang, pitch, speed, path):
    s, sr = k.create(text, voice=voice, speed=speed, lang=lang)
    sf.write(path + ".raw.wav", s, sr)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", path + ".raw.wav", "-af",
                    f"asetrate={sr}*{pitch},aresample=44100,atempo={1/pitch:.4f},"
                    "highpass=f=90,equalizer=f=3000:t=q:w=1:g=2,"
                    "silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_threshold=-45dB:stop_duration=0.15,"
                    "loudnorm=I=-16:TP=-1.5", "-ac", "1", "-ar", "44100", path], check=True)
    os.remove(path + ".raw.wav")
    return sf.read(path)[0]


def make(lines, outdir):
    os.makedirs(outdir, exist_ok=True)
    info = {}
    for lid, role, lang, text in lines:
        out = f"{outdir}/{lid}.wav"
        if role == "kids":
            parts = []
            for j, (vh, ve, p, off) in enumerate(KIDS):
                a = tts(text, vh if lang == "hi" else ve, lang, p, 1.0, f"{outdir}/_k{j}.wav")
                parts.append(np.concatenate([np.zeros(int(off * 44100)), a]))
            n = max(len(x) for x in parts)
            mix = sum(np.pad(x, (0, n - len(x))) for x in parts) / 2.2
            sf.write(out, mix, 44100)
            for j in range(len(KIDS)): os.remove(f"{outdir}/_k{j}.wav")
        else:
            vh, ve, p, sp = ROLE[role]
            tts(text, vh if lang == "hi" else ve, lang, p, sp, out)
        info[lid] = {"role": role, "dur": round(len(sf.read(out)[0]) / 44100, 2)}
    json.dump(info, open(f"{outdir}/info.json", "w"), indent=1)
    return info


if __name__ == "__main__":
    LINES = [("s0", "golu", "hi", "चलो, रंग सीखें!"), ("s0e", "golu", "en-us", "Let's learn colours!")]
    for c, hi, en in [("r", "लाल!", "Red!"), ("y", "पीला!", "Yellow!"), ("b", "नीला!", "Blue!"), ("g", "हरा!", "Green!")]:
        LINES += [(c, "golu", "hi", hi), (c + "e", "kids", "en-us", en)]
    LINES += [("end", "golu", "hi", "शाबाश!"), ("ende", "kids", "en-us", "Well done!")]
    print(make(LINES, sys.argv[1]))
