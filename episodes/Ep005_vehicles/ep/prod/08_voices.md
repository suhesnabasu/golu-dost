# Ep 5 — Voices (Stage 8)

- **Fish Audio (primary):** job `tts_job_Ep005_vehicles.json` (27 takes incl. kids _a/_b, model s2.1-pro-free, fixed per-role voices from voices_fish.py) uploaded to the public folder at 08:42 UTC (Drive id 1JhkX5Ek1aeD5qzQG_PQz97wKURUsyvqZ). This scheduled run has no GitHub write access (the `add_repo` tool is absent, and gh/API dispatch returned 403 'GitHub access to this repository is not enabled for this session'), so the workflow could not be dispatched. The scheduled `tts.yml` cron had not produced `jobs/Ep005_vehicles/` on the `tts` branch after 2 h of polling (last tts commit 07:03 UTC).
- **Fallback used (RUNBOOK):** Kokoro `voices2.make()` voices (golu = hf_beta/af_bella, mithu = hf_beta/af_nova, kids = 3-voice chorus). Code-mixed kids lines are split into Hindi and English chunks (`kokoro_mixed.py`), all lines are levelled to −16 dB RMS, and kids' lines are sped up ×1.12. Checked by numbers: every line is 0.7–2.7 s, none silent, peaks ≤0.95.
- If the Fish voices land later, re-run: fish_prep.py → timing.py → audio.py → gen_episode.py → render. Everything is re-timed from info.json automatically.

## Final cue sheet (real durations)
| id | role | start s | dur s | TTS text |
|---|---|---|---|---|
| a1 | golu | 0.25 | 0.72 | पों पों! |
| a2 | mithu | 1.5 | 1.14 | छुक छुक! छुक छुक! |
| b1 | golu | 3.0 | 1.39 | चलो, गाड़ियाँ सीखें! |
| c1 | golu | 5.35 | 1.46 | रेलगाड़ी! छुक छुक! |
| c2 | mithu | 7.0 | 1.18 | Train! Train! |
| c3 | kids | 8.5 | 2.4 | रेलगाड़ी! Train! Choo choo! |
| d1 | golu | 13.15 | 1.02 | बस! पों पों! |
| d2 | mithu | 14.5 | 1.01 | Bus! Bus! |
| d3 | kids | 15.75 | 1.98 | बस! Bus! Beep beep! |
| e1 | golu | 18.95 | 1.8 | ट्रैक्टर! घर्रर्र घर्रर्र! |
| e2 | mithu | 21.0 | 1.32 | Tractor! Tractor! |
| e3 | kids | 22.5 | 2.38 | ट्रैक्टर! Tractor! Vroom vroom! |
| f1 | golu | 25.95 | 1.2 | दमकल! वीं वूँ! |
| f2 | mithu | 27.5 | 1.56 | Fire truck! Fire truck! |
| f3 | kids | 29.25 | 2.35 | दमकल! Fire truck! Wee woo! |
| g1 | golu | 32.5 | 2.06 | चलो फिर से! Let's do it again! |
| h1 | kids | 34.75 | 2.27 | रेलगाड़ी, बस, ट्रैक्टर, दमकल! |
| h2 | kids | 37.25 | 1.99 | Train, bus, tractor, fire truck! |
| s1 | golu | 39.5 | 1.55 | शाबाश! Well done! |
| k1 | golu | 41.25 | 1.97 | कल नई गाड़ी! कल फिर मिलेंगे! |
| k2 | mithu | 43.5 | 1.67 | See you tomorrow! Tomorrow! |

Total duration: 46.25 s. Vehicle beats: [{"in": 4.75, "g": 5.35, "m": 7.0, "k": 8.5, "out": 11.25}, {"in": 12.55, "g": 13.15, "m": 14.5, "k": 15.75, "out": 18.0}, {"in": 18.35, "g": 18.950000000000003, "m": 21.0, "k": 22.5, "out": 25.0}, {"in": 25.35, "g": 25.950000000000003, "m": 27.5, "k": 29.25, "out": 31.75}]

## SFX (bundled HyperFrames library, Pixabay licence)
| sfx | picture time s | vol |
|---|---|---|
| whoosh | 1.0 | 0.4 |
| pop | 0.05 | 0.3 |
| pop | 1.45 | 0.3 |
| pop | 3.0 | 0.3 |
| pop | 5.35 | 0.3 |
| pop | 13.15 | 0.3 |
| pop | 18.95 | 0.3 |
| pop | 25.95 | 0.3 |
| pop | 32.5 | 0.3 |
| pop | 41.25 | 0.3 |
| pop | 39.5 | 0.3 |
| whoosh | 11.6 | 0.3 |
| sparkle | 8.5 | 0.3 |
| whoosh-short | 12.8 | 0.3 |
| whoosh-short | 18.35 | 0.3 |
| sparkle | 15.75 | 0.3 |
| whoosh | 18.6 | 0.3 |
| whoosh | 25.35 | 0.3 |
| sparkle | 22.5 | 0.3 |
| whoosh-short | 25.6 | 0.3 |
| whoosh-short | 32.1 | 0.3 |
| sparkle | 29.25 | 0.3 |
| click-soft | 32.8 | 0.3 |
| click-soft | 32.92 | 0.3 |
| click-soft | 33.04 | 0.3 |
| click-soft | 33.16 | 0.3 |
| chime | 39.04 | 0.3 |
| chime | 41.25 | 0.35 |

Mix: music ducks 55% under voices, SFX 0.3–0.4, delivery loudnorm −14 LUFS; the 720p publish copy is measured at −14.0 LUFS.