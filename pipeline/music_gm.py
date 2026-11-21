"""Human-feel kids' music with real instrument samples (FluidR3 GM soundfont, MIT licence).
All melodies are generated here from chord tones with a seed, so every song is original (no existing tunes).

make_song(out_wav, dur, bpm=120, seed=1, chimes=[], finale=None, intro_soft=0.0)
"""
import random, subprocess, os
import pretty_midi

SF2 = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
# I - V - vi - IV style progressions in C major (bright, happy), as (root midi, chord tones)
PROGS = [
    [(48, [60, 64, 67]), (43, [59, 62, 67]), (45, [60, 64, 69]), (41, [60, 65, 69])],
    [(48, [60, 64, 67]), (41, [60, 65, 69]), (43, [59, 62, 67]), (48, [60, 64, 67])],
    [(45, [60, 64, 69]), (41, [60, 65, 69]), (48, [60, 64, 67]), (43, [59, 62, 67])],
]


def make_song(out_wav, dur, bpm=120, seed=1, chimes=(), finale=None, intro_soft=0.0, prog_id=None):
    rnd = random.Random(seed)
    beat = 60.0 / bpm
    bar = beat * 4
    prog = PROGS[prog_id if prog_id is not None else seed % len(PROGS)]
    pm = pretty_midi.PrettyMIDI(initial_tempo=bpm)
    uke = pretty_midi.Instrument(program=24, name="nylon guitar")      # strummed acoustic
    xylo = pretty_midi.Instrument(program=13, name="xylophone")        # melody
    bell = pretty_midi.Instrument(program=9, name="glockenspiel")      # sparkles
    bass = pretty_midi.Instrument(program=32, name="acoustic bass")
    piano = pretty_midi.Instrument(program=0, name="piano")             # soft pad-like comping
    drums = pretty_midi.Instrument(program=0, is_drum=True, name="kit")

    def h(t):  # humanise timing
        return max(0.0, t + rnd.uniform(-0.012, 0.012))

    def note(inst, pitch, t, length, vel):
        v = int(max(20, min(127, vel + rnd.randint(-10, 10))))
        inst.notes.append(pretty_midi.Note(velocity=v, pitch=pitch, start=h(t), end=h(t) + length))

    # one original 2-bar melodic motif from chord tones, varied each repeat
    motif = []
    for k in range(8):
        motif.append((k * beat * 0.5 + (beat * 0.5 if k % 4 == 3 else 0), rnd.choice([0, 1, 2, 2, 1])))
    t = 0.0; b = 0
    while t < dur - 0.5:
        root, tones = prog[b % 4]
        soft = t < intro_soft
        # bass: root on 1 and 3, fifth pickup
        note(bass, root, t, beat * 0.9, 85)
        note(bass, root + 7, t + beat * 2, beat * 0.9, 75)
        # strummed guitar: down-down-up-up-down rhythm, slight strum spread
        for off, vel in [(0, 70), (1, 60), (1.5, 50), (2.5, 52), (3, 62)]:
            st = t + off * beat
            for j, p in enumerate(tones):
                note(uke, p, st + j * 0.012, beat * 0.45, vel - (25 if soft else 0))
        note(piano, tones[0] + 12, t, bar * 0.95, 34)
        # drums (light, kids-pop): kick 1 & 3, clap 2 & 4, shaker eighths, tambourine on 4&
        if not soft:
            for q in range(4):
                if q in (0, 2): note(drums, 36, t + q * beat, 0.1, 80)
                if q in (1, 3): note(drums, 39, t + q * beat, 0.1, 70)
                note(drums, 70, t + q * beat, 0.05, 45); note(drums, 70, t + (q + .5) * beat, 0.05, 35)
            note(drums, 54, t + 3.5 * beat, 0.1, 50)
        # melody: motif over chord tones, every bar but varied
        if not soft:
            for (mo, deg) in motif[(b % 2) * 4:(b % 2) * 4 + 4]:
                p = tones[deg] + 12 + (12 if (b // 4) % 2 and deg == 0 else 0)
                note(xylo, p, t + mo - (b % 2) * beat * 2 if b % 2 else t + mo, beat * 0.4, 72)
        t += bar; b += 1
    for ct in chimes:  # sparkle arpeggio at moments (e.g. a new word appears)
        root = 84 + rnd.choice([0, 2, 4, 7])
        for j, iv in enumerate((0, 4, 7, 12)):
            note(bell, root + iv, ct + j * 0.06, 0.6, 85)
    if finale is not None:
        for j, p in enumerate((72, 76, 79, 84, 88, 91, 96)):
            note(bell, p, finale + j * 0.07, 1.0, 90)
        for j, p in enumerate((60, 64, 67, 72)):
            note(piano, p, finale, 1.6, 70)
    for inst in (uke, xylo, bell, bass, piano, drums):
        pm.instruments.append(inst)
    mid = out_wav.replace(".wav", ".mid")
    pm.write(mid)
    raw = out_wav.replace(".wav", "_raw.wav")
    subprocess.run(["fluidsynth", "-ni", "-g", "0.9", "-r", "44100", "-F", raw, SF2, mid], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # gentle room reverb + fade out, trimmed to duration
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af",
                    f"aecho=0.8:0.5:40|70:0.18|0.12,afade=t=out:st={dur-1.0}:d=1.0,atrim=0:{dur}",
                    "-ar", "44100", "-ac", "1", out_wav], check=True)
    os.remove(raw)
    return out_wav


if __name__ == "__main__":
    make_song("/tmp/test_song.wav", 22.0, 120, seed=3, chimes=[3.5, 7.5, 11.5, 15.5], finale=19.0, intro_soft=2.5)
    print("ok")
