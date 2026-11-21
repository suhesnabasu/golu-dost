import soundfile as sf, json, subprocess, os
from kokoro_onnx import Kokoro
k = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
# character -> (kokoro voice, pitch factor, speed)
CAST = {"golu": ("hf_beta", 1.18, 1.05), "bunny": ("hf_alpha", 1.32, 1.1),
        "mithu": ("hf_beta", 1.5, 1.2), "nar": ("hf_alpha", 1.05, 1.0)}
LINES = [
    ("l01", "golu", "नमस्ते बच्चों! मैं हूँ गोलू हाथी!"),
    ("l02", "golu", "आउच! अरे... ये तो आम है!"),
    ("l03", "golu", "चलो बच्चों, आम गिनते हैं!"),
    ("n1", "golu", "एक आम!"), ("n2", "golu", "दो आम!"), ("n3", "golu", "तीन आम!"),
    ("n4", "golu", "चार आम!"), ("n5", "golu", "पाँच आम!"),
    ("l04", "golu", "वाह! पाँच आम!"),
    ("l05", "nar", "अरे! गोलू के दोस्त आए!"),
    ("l06", "bunny", "गोलू, मुझे भी आम चाहिए!"),
    ("l07", "mithu", "मुझे भी! मुझे भी!"),
    ("l08", "nar", "गोलू क्या करेगा?"),
    ("l09", "golu", "ये लो दोस्तों! एक तुम्हारे लिए, और एक तुम्हारे लिए!"),
    ("l10", "bunny", "धन्यवाद गोलू!"),
    ("l11", "mithu", "धन्यवाद! धन्यवाद!"),
    ("l12", "nar", "मिलकर बाँटो, खुश रहो!"),
    ("l13", "golu", "बाँटने से सब खुश होते हैं!"),
    ("l14", "golu", "बाय बाय बच्चों! कल फिर मिलेंगे!"),
]
LDIR="lines_hi"
os.makedirs(LDIR, exist_ok=True)
info = {}
for lid, ch, txt in LINES:
    v, pf, sp = CAST[ch]
    s, sr = k.create(txt, voice=v, speed=sp, lang="hi")
    sf.write(f"{LDIR}/raw.wav", s, sr)
    # pitch up (cartoon) keeping tempo, normalise
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{LDIR}/raw.wav", "-af",
                    f"asetrate={sr}*{pf},aresample=44100,atempo={1/pf:.4f},atempo=1.0,loudnorm=I=-16:TP=-1.5,silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_threshold=-45dB:stop_duration=0.2",
                    "-ac", "1", "-ar", "44100", f"{LDIR}/{lid}.wav"], check=True)
    d, _ = sf.read(f"{LDIR}/{lid}.wav")
    info[lid] = {"char": ch, "dur": round(len(d) / 44100, 2)}
json.dump(info, open(f"{LDIR}/info.json", "w"), indent=1)
print(json.dumps(info))
