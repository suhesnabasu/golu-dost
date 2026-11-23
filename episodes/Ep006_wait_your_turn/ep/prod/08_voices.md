# Ep 6 — Voices (Stage 8)

- **Fish Audio (primary):** job `tts_job_Ep006_wait_your_turn.json` (fixed per-role voices from voices_fish.py; kids = 2 takes) uploaded to the public folder 169NTC-6EJ1SZB0RFdy9pq6hVLXl4ICR3 (Drive id 1PoGalMlLzy1wfzy58SeSRIOrOwQ8wIn3).
  This scheduled run has **no GitHub access to suhesnabasu/golu-dost** (gh API → 403 "GitHub access to this repository is not enabled for this session"; no add_repo tool), so the TTS workflow could not be dispatched. Read-only check via the GitHub connector: the `tts` branch's last commit is 22 Nov 07:03 UTC and `jobs/Ep005_vehicles` was never produced, so the cron is not picking up new jobs either.
- **Fallback used (RUNBOOK):** Kokoro `voices2.make()` (golu = hf_beta/af_bella, bunny = hf_alpha/af_sky, mithu = hf_beta/af_nova, kids = 3-voice chorus), with code-mixed lines split into Hindi / English chunks (`kokoro_mixed.py`) — the same fallback voices as Ep5, so Ep5 → Ep6 sound consistent.
- Listen-check by numbers: all 25 lines 0.85–2.24 s, none silent, every line loudnorm −16 LUFS before the mix.
- If Fish voices land later: fish_prep.py → timing.py → audio.py → gen_episode.py → render (everything re-times from info.json).

## Final cue sheet (real durations)
| id | role | start s | dur s | TTS text |
|---|---|---|---|---|
| a1 | golu | 0.20 | 1.06 | अरे! रुको, बनी! |
| a2 | bunny | 1.41 | 0.90 | मैं पहले! |
| a3 | mithu | 2.46 | 0.85 | धप्प! धप्प! |
| b1 | bunny | 3.86 | 1.02 | मैं फिर से! |
| b2 | mithu | 6.26 | 1.04 | फिर से! फिर से! |
| b3 | golu | 8.01 | 1.42 | अरे, सब उदास हो गए। |
| b4 | bunny | 9.63 | 1.82 | अकेले मज़ा नहीं आता। |
| c1 | golu | 11.75 | 1.60 | चलो, बारी-बारी खेलें! |
| c2 | mithu | 13.50 | 1.63 | Take turns! Take turns! |
| c3a | kids | 15.28 | 1.07 | बारी-बारी! |
| c3b | kids | 16.50 | 1.20 | Take turns! |
| d1 | kids | 19.10 | 1.63 | परी की बारी! वीईई! |
| d2 | kids | 22.25 | 1.77 | चिंटू की बारी! वीईई! |
| d3a | bunny | 24.22 | 1.52 | उफ़! रुकना मुश्किल है! |
| d3 | mithu | 25.89 | 0.86 | रुको! रुको! |
| d3b | golu | 26.90 | 1.06 | शाबाश, बनी! |
| d4 | bunny | 29.31 | 1.47 | मेरी बारी! वीईई! |
| d5 | golu | 31.21 | 1.15 | अब मेरी बारी! |
| d6 | mithu | 34.06 | 1.03 | Plop! Plop! |
| e1 | golu | 35.34 | 1.70 | बारी-बारी, सबकी बारी! |
| e2a | kids | 37.19 | 1.31 | Wait your turn! |
| e2b | kids | 38.65 | 1.63 | Everyone gets a turn! |
| e3 | golu | 40.48 | 2.24 | साथ में मज़ा! Together is fun! |
| f1 | golu | 42.92 | 1.62 | शाबाश! कल फिर मिलेंगे! |
| f2 | mithu | 44.69 | 1.67 | See you tomorrow! Tomorrow! |

Total duration: 47.0 s.
