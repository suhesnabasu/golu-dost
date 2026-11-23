# Ep 6 — Script review (Stage 4) · बारी-बारी / Wait Your Turn

Verdict: strong, kind story; fix the MUST items below, then go to Stage 5.

## Fixes
1. **MUST — hook timing overlaps.** a1 (~1.2 s), a2 (~1.4 s) and a3 cannot all fit in 0–3 s with the 0.15 s gap rule.
   a2 → `मैं पहले!` (once; Bunny is too fast to say it twice, and saying it twice is Mithu's gag). Set a1 0.2, a2 1.5, a3 2.7;
   put the sand-puff SFX "thud" at ~2.5 s so the comic surprise lands inside 3 s even if a3 slips a bit.
2. **MUST — slide safety in every slide action.** Add to a2, d1, d2, d4, d5: "climbs holding the rails, sits at the top,
   slides sitting, feet first, lands in soft sand, steps out of the landing spot before the next one goes". The hook must
   show it too (fast, but sitting + feet first). a3: "dizzy" → "giggly-dizzy, shakes it off and grins" (nobody hurt).
3. **MUST — no pushing.** b1/b2 action: "Bunny zips in front — no touching or pushing; Pari/Chintu step back, sad."
4. **MUST — Golu's slide must not look unsafe.** d5 "slide wobbles" → "slide goes 'boing' and holds steady; Golu slides
   sitting, feet first". The comedy is the big sand splash, not a shaky slide.
5. **MUST — praise Bunny for waiting (positive, not shaming).** Insert after d3:
   `d3b | 29.4 | golu | hi | शाबाश, बनी! | Bunny smiles, deep breath; Golu's happy closed eyes | शाबाश, बनी! / Well done, Bunny!`
   and move d4 to 30.6 (others +0.6 s or absorb in the 30–33.5 gap).
6. **MUST — on-screen text bilingual.** e2 card `Everyone gets a turn!` → `सबकी बारी! / Everyone gets a turn!`.
   e1 card → `बारी-बारी, सबकी बारी! / Wait your turn, everyone gets a turn!` (two lines if needed; Baloo2).
   c3 card `1 2 3 4` → `एक दो तीन चार / 1 2 3 4` (small, above the badges).
7. **MUST — split mixed-language lines for TTS** (Kokoro hi voice mangles English; Fish is fine either way, so splitting is safe):
   c3 → `c3a | kids | hi | बारी-बारी!` + `c3b | kids | en-us | Take turns!` (start c3b ≥ c3a end + 0.15 s).
   d1/d2/d4 "Wheee!" inside hi lines → write `वीईई!` (hi), or split it off as `en-us` `Wheee!`.
8. **MUST — keep b4 from feeling like exclusion.** b4 action: "Bunny lands, looks back: Pari & Chintu are still waiting
   at the ladder (not turning away), nobody is sliding with her; ears droop." So the lesson is "alone is no fun", never "they left you".
9. **NICE — e2 length.** "Wait your turn! Everyone gets a turn!" by a chorus is ~2.5–2.8 s. Split:
   `e2a | kids | en-us | Wait your turn!` (39.6) + `e2b | kids | en-us | Everyone gets a turn!` (~41.0); shift f1 to ~43.0.
10. **NICE — more natural Hindi.** b1 `फिर से मैं!` → `मैं फिर से!`; b3 `ओहो… सब उदास हैं।` → `अरे, सब उदास हो गए।`
    (the "…" can make TTS pause oddly; use a comma).
11. **NICE — let Bunny name the feeling.** Replace Mithu's d3 with two short lines if timing allows:
    `d3 | bunny | hi | उफ़! रुकना मुश्किल है!` (taps foot) then `d3m | mithu | hi | रुको! रुको!` — waiting is hard is validated, not scolded.
12. **NICE — "together is more fun" is in the brief but never said.** Add on the confetti: kids `साथ में मज़ा!` (hi) or a
    card `साथ में मज़ा! / Together is fun!` during e2.
13. **NICE — beat-sheet times don't match the dialogue** (FEELING 10–14 s, LEARN 14.5–21 s, TRY 21.5–37 s). Sync the table.
14. **NICE — show the series badge** `गोलू की कहानियाँ #1 / Golu's Stories #1` top corner from frame 1 (algorithm rule).
15. **NICE — on-screen cards for b1** `मैं पहले! / Me first!` adds a beat in the 3–10 s stretch.
16. **NICE — TTS spellings.** Keep `धप्प!` (reads well in Fish and Kokoro hi; fall back to `धप!` if Kokoro clips the
    double consonant). `Plop! Plop!` fine in en-us. Avoid `ऽ` (avagraha) and long letter runs ("Wheeeee") — TTS may spell them.

## What works
- Lesson is accurate and gentle: feeling first (sad friends, "अकेले मज़ा नहीं आता"), then Golu's inclusive "चलो, बारी-बारी खेलें!".
- Bunny is never scolded by Golu; she gets the happiest ride and the cheers — her arc is lonely → patient → joyful.
- Bilingual rule followed: Hindi first, Mithu/kids give the English; "बारी-बारी" ×3 and "Take turns/Wait your turn" ×3.
- Voices on model: Mithu doubles every line, Bunny fast, Golu kind; Pari & Chintu only in chorus.
- Golu goes last in the line-up — models patience without a lecture; his big plop is a safe, warm laugh.
- धप्प!/Plop! callback, strong 0–3 s hook, clean loop (Bunny zooms off right → zooms in again), ends on
  "शाबाश! कल फिर मिलेंगे!"; no subscribe/like/share; original cast/setting, no copyright issues. Length ~47 s fits 40–55 s.
