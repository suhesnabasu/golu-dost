# Ep 7 — Voices (Stage 8)

- **Fish Audio (primary):** job `tts_job_Ep007_shapes.json` (23 lines; fixed per-role voices from voices_fish.py — golu/mithu = "Girl kid", kids = 2-take chorus) uploaded to the public folder 169NTC-6EJ1SZB0RFdy9pq6hVLXl4ICR3 at 08:40 UTC (Drive id 1bV3HbxjW9SeaDAX38iMnigcPbhc_eb32).
  This scheduled run has **no push/Actions access to suhesnabasu/golu-dost** (git proxy 403: repo not in the session's authorized set), so the TTS workflow could not be dispatched. Polled the public `tts` branch for ~45 min: no new commit since 22 Nov 15:24 UTC — the 10-minute cron is not picking up jobs on its own.
- **Fallback used (RUNBOOK):** Kokoro `voices2.make()` via kokoro_mixed.py (same fallback voices as Ep5/Ep6, so the sound stays consistent). The Fish job stays in the folder: if the workflow runs later, `jobs/Ep007_shapes/` will hold the Fish takes for a remake (fish_prep.py → timing.py → audio.py → gen_episode.py → render).
- Listen-check by numbers: all 23 lines 0.76–1.78 s, none silent; cue sheet re-timed from the real durations (timing.py), DUR 35.25 s.

| id | role | dur s |
|---|---|---|
| a1 | golu | 1.12 |
| a2 | mithu | 0.83 |
| b1 | golu | 1.35 |
| b2 | mithu | 1.11 |
| c1 | golu | 1.35 |
| c2 | mithu | 1.26 |
| c3a | kids | 0.79 |
| c3b | kids | 0.78 |
| d1 | golu | 1.64 |
| d2 | kids | 1.43 |
| d3 | mithu | 1.13 |
| d4a | kids | 0.96 |
| d4b | kids | 0.76 |
| e1 | golu | 1.78 |
| e2 | kids | 1.16 |
| e3 | mithu | 1.43 |
| e4a | kids | 0.88 |
| e4b | kids | 1.07 |
| f1 | golu | 1.01 |
| f2 | kids | 1.7 |
| f3 | kids | 1.78 |
| g1 | golu | 1.62 |
| g2 | mithu | 1.67 |
