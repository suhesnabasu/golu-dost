# Ep 8 — Stage 8 Voices

- **Fish Audio S2.1 Pro (primary, used for ALL lines):** job `tts_job_Ep008_feeling_angry.json` (24 script lines → 30 takes; kids = 2-take chorus)
  uploaded to the public Drive drop-box folder 169NTC-6EJ1SZB0RFdy9pq6hVLXl4ICR3 (Drive id 1HxoYZX5NXPf2ZKwNT7VE3lcr9Pa5nnc2) at 11:25 UTC;
  the GitHub poller finished it within ~2 min (done.txt: all `ok`, no failed lines). Wavs fetched read-only from the `tts` branch with buffer_post.fetch_tts.
- Fixed per-role voices from voices_fish.py (golu/mithu = "Girl kid", bunny = "indian girl", kids = both, chorus) — same voices as the Fish remakes, so characters stay consistent. No Kokoro fallback needed.
- fish_prep.py → trimmed + levelled (−16 LUFS) lines. Then a tightening pass: internal pauses capped at 0.18 s and atempo 1.06 (1.12 for lines > 2 s) so the story fits ≤ 55 s.
  Line e2 (Mithu "Angry! Angry!") was cut for length — "गुस्सा/Angry" is still said 3× (b2, b3, e1) and once more in e2b/e2c.
- Listen-check by numbers: every line 0.86–3.36 s, none silent. Cue sheet re-timed from the real durations (timing.py) → **DUR 53.0 s**, no overlaps (≥ 0.12 s gaps).

| id | role | Fish raw s | final s | cue s |
|---|---|---|---|---|
| a1 | golu | 1.39 | 1.32 | 0.15 |
| a2 | bunny | 0.91 | 0.86 | 1.62 |
| a3 | mithu | 1.83 | 1.49 | 3.38 |
| b1 | golu | 3.65 | 2.62 | 5.12 |
| b2 | mithu | 2.29 | 1.66 | 7.89 |
| b3 | kids | 1.64 | 1.55 | 9.7 |
| c1 | bunny | 1.89 | 1.76 | 11.7 |
| c2 | kids | 2.25 | 2.01 | 13.66 |
| c3 | kids | 1.48 | 1.3 | 15.82 |
| d1 | golu | 1.59 | 1.5 | 17.77 |
| d2 | golu | 2.41 | 1.98 | 19.57 |
| d3 | kids | 3.76 | 3.36 | 22.0 |
| d4 | mithu | 1.69 | 1.23 | 25.71 |
| e1 | golu | 1.49 | 1.41 | 29.44 |
| e2b | golu | 3.53 | 2.82 | 31.15 |
| e2c | kids | 3.38 | 2.97 | 34.12 |
| e3 | golu | 1.61 | 1.52 | 37.39 |
| e4 | bunny | 1.4 | 1.3 | 39.06 |
| f1a | golu | 1.52 | 1.44 | 41.01 |
| f1b | golu | 2.5 | 2.14 | 42.6 |
| f2 | kids | 2.96 | 2.4 | 44.89 |
| g1 | golu | 2.77 | 2.48 | 47.54 |
| g2 | mithu | 2.29 | 1.87 | 50.17 |
