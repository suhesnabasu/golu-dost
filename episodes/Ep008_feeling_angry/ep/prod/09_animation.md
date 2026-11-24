# Ep 8 — Stage 9 Animation & build
- Built with gen_episode.py (from the Ep7 template code: v2 GOLU/KIDS + f3d, glossy Mithu, v2 Bunny from Ep6) → ep/index.html (HyperFrames 0.9.72, 1080×1920, 30 fps, DUR 53.0 s), audio by audio.py (song.mp3 = Fish voices + music_gm seed 23/prog 0 + bundled SFX, −14 LUFS).
- Acting: shock → squash → angry take (ears out, brows, frown, red flush, steam, stomp); hold/freeze on "रुको!"; three breaths (gwrap swells, trunk up/forward, red + steam step down); happy closed eyes on calm/rebuild; offset idle (body/head/kids/Mithu/Bunny never in unison), blinks every 3.3 s offset per character.
- Camera: slow push in the hook, punch-in on the crash, close on Golu for the anger take, breathing push/pull, beat punches in the rebuild.
- Lip-sync: Golu + Bunny from the real voice envelopes (pre-drawn mouths, svgOrigin scale); kids/Mithu talk cycles from line durations.
- Checks: `hyperframes check` 0 errors; snapshots at every shot change (qa/contact-sheet-*.jpg) → QA fixes → re-snapshot → render.
