import json, subprocess, numpy as np, soundfile as sf
SR = 44100
def voice_track(plan, LD, roles, DUR, fps=30):
    N = int(SR * DUR); voice = np.zeros(N); env = {}
    nf = int(DUR * fps) + 2; hop = SR // fps
    end = -1
    for lid, t0, _tempo, _nd in plan:
        a, _ = sf.read(f"{LD}/{lid}.wav")
        assert t0 >= end + 0.1 - 1e-6, (lid, t0, end); end = t0 + len(a) / SR
        s = int(t0 * SR); voice[s:s + len(a)] += a[:max(0, N - s)]
        r = roles[lid]; e = env.setdefault(r, np.zeros(nf))
        for k in range(len(a) // hop):
            fi = int(round(t0 * fps)) + k
            if fi < nf: e[fi] = np.sqrt(np.mean(a[k * hop:(k + 1) * hop] ** 2))
    assert end <= DUR, end
    lips = {"fps": fps}
    for r in ("golu", "kids", "mithu", "bunny", "nar"):
        e = env.get(r)
        if e is None or not (e > 0).any(): lips[r] = [0] * nf; continue
        m = np.percentile(e[e > 0], 85); e = np.clip(e / m, 0, 1); e = np.convolve(e, [.25, .5, .25], "same")
        lips[r] = np.where(e < 0.18, 0, np.where(e < 0.45, 1, np.where(e < 0.75, 2, 3))).astype(int).tolist()
    return voice, lips, end
def lib_sfx(N, items, d="/home/claude/golu_pipeline/assets/sfx"):
    fx = np.zeros(N)
    for name, t, v in items:
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f"{d}/{name}.mp3", "-ac", "1", "-ar", str(SR), "/tmp/_sfx.wav"], check=True)
        a = sf.read("/tmp/_sfx.wav")[0]; s0 = int(t * SR); seg = a[:max(0, N - s0)] * v; fx[s0:s0 + len(seg)] += seg
    return fx
def final_mix(mus, voice, out_mp3, duck=0.62, vgain=1.3):
    venv = np.convolve(np.abs(voice), np.ones(2205) / 2205, "same")
    mix = mus * (1 - duck * np.clip(venv / 0.02, 0, 1)) + voice * vgain
    mix = mix / np.abs(mix).max() * 0.93
    sf.write("/tmp/_mix.wav", mix.astype(np.float32), SR)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", "/tmp/_mix.wav", "-af", "loudnorm=I=-14:TP=-1", "-ar", "44100", "-b:a", "192k", out_mp3], check=True)
    # voice-vs-music check: RMS of voice part vs ducked music during speech
    m = venv > 0.01
    v_rms = np.sqrt(np.mean((voice[m] * vgain) ** 2)); mu = (mus * (1 - duck * np.clip(venv / 0.02, 0, 1)))[m]
    return round(20 * np.log10(v_rms / (np.sqrt(np.mean(mu ** 2)) + 1e-9)), 1)
