# Ep 5 — Music & sound design plan (Stage 7)

## Score
- Original song from `music_gm.make_song()` (FluidR3 GM, MIT): **seed 13, prog_id 0** (I–V–vi–IV in C major), **120 bpm** (beat 0.5 s, bar 2 s) — new seed so the song is new (ep2 = 3, ep3 = 7, ep4 = 11).
- Instruments: strummed nylon guitar, xylophone melody (Golu's colour), glockenspiel sparkle arpeggios (chimes) on every new word card, acoustic bass, light kit (kick 1&3, clap 2&4, shaker).
  Kids' chorus lines are the "everyone" moments; Mithu's lines sit on the beat after Golu's.
- Structure aligned to scenes: hook (full groove from frame 1 — no soft intro, the hook needs energy) → intro chime → 4 vehicle verses (chime on each vehicle card) → recap chime → finale arpeggio + piano chord on "कल फिर मिलेंगे!" → loop.
- Character colours: Golu's lines ride on the xylophone melody; glockenspiel chimes mark the words; whoosh/pop effects for the vehicles (no synthesised tones).
- Signature "Golu theme": music_gm has no separate motif seed, so the opening motif can't be held constant across episodes yet. The finale glockenspiel arpeggio (C-E-G-C-E-G-C) is identical in every episode, and that serves as the recognisable sting. *Pipeline note for the owner: add a fixed-seed 2-bar motif option to music_gm.*

## Mix rules
Voices on top. Music ducks ~55% under any voice (envelope follower). SFX at 0.3–0.4, with each clip's peak placed one frame after its picture. Final loudnorm −14 LUFS, true peak −1 dBTP.

## Cue sheet (provisional — final seconds come from timing.json after Stage 8; see 08_voices.md for the real ones)
| t (s) | cue |
|---|---|
| 0.05 | pop (हॉन्क card) |
| 0.25 | VO a1 Golu "पों-पों!" |
| ~1.0 | whoosh (train's fastest frame) |
| ~1.5 | VO a2 Mithu "छुक-छुक! छुक-छुक!" + pop |
| intro | VO b1 Golu + pop + glock chime |
| V0..V3 in | whoosh-short / whoosh, rotated (vehicle arrives); the train's arrival is under the gate-down move |
| V g | pop + glock chime + VO Golu (Hindi word + sound) |
| V m | VO Mithu English ×2 |
| V k | VO kids (Hindi + English + sound) + sparkle |
| V out | whoosh / whoosh-short (vehicle leaves) |
| recap | VO g1 + pop + 4 click-soft (bubbles) + glock chime |
| h1, h2 | VO kids Hindi row, English row; chime at the end of h2 |
| s1 | VO Golu "शाबाश! Well done!" + pop |
| end | VO k1 + pop + chime + finale arpeggio; then k2 Mithu |

The exact SFX list is written by audio.py to `sfx_cues.json` and copied into 08_voices.md.
