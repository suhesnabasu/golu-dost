# Ep 8 — Stage 4 Script Review: गुस्सा आया! / Feeling Angry

## Verdict
**APPROVE WITH FIXES.** Strong structure: action in frame 1, crash at 2.6 s, clear arc (pride, crash, anger, stop, 3 breaths, words, forgive, rebuild), a real loop, "कल फिर मिलेंगे" ending, no subscribe/like/share, all characters original. Mithu's repeat gag, Bunny's "मेरी बारी?" callback and the Pari/Chintu chorus all match the bible. Devanagari is mostly correct (आख़िरी, साँस, सूँघो, बनाएँ, मिलेंगे). "टावर" is fine: Indian kids say it every day, and "मीनार" would sound bookish.
Six MUST fixes: the "anger is OK, throwing is not" line is missing; the throw pose needs a safety fix; a1 is too long for its slot; two lines would sound unnatural or break in TTS; the lang code is wrong.

## Fixes

1. **MUST — a1 too long for its slot.** "आख़िरी ब्लॉक… हो गया!" with the pause runs ~1.9 s, but a2 starts at 1.6 s. "हो गया" also spoils the crash.
   Replace with: `a1 | 0.2 | golu | hi | आख़िरी ब्लॉक!` (~0.9 s, matches the on-screen card and the loop frame).
2. **MUST — b1: "हम्फ़" will break in TTS** (likely read as "hamf"). It is also not a Hindi child sound, and the line never says what happened.
   Replace with: `b1 | 4.6 | golu | hi | मेरा टावर गिर गया! उफ़्फ़!`
3. **MUST — c1 Hindi is clipped and unnatural.** "ग़लती से गिरा" has no subject, so it sounds like a caption, not a child talking. Also use the nukta, to match आख़िरी/फ़.
   Replace with: `c1 | 9.2 | bunny | hi | सॉरी गोलू! ग़लती से गिर गया!`
4. **MUST — c1 action (safety).** "Golu has lifted a block to throw" while Bunny is apologising reads as aiming at Bunny, which is close to hitting.
   Action text: `Golu holds a block up high in his trunk, angry face, NOT aimed at anyone (Bunny is off to the side); he freezes on "रुको!"`
5. **MUST — the core lesson "anger is OK, throwing is not" is never said** (brief requires it). Insert it after e2 and shift the following lines:
   `e2b | 27.3 | golu | hi | गुस्सा आना ठीक है… फेंकना नहीं! | calm, puts block gently on rug | गुस्सा ठीक है, फेंकना नहीं / Angry is OK. No throwing!`
   `e2c | 29.3 | kids | en-us | Angry is OK. No throwing!`
   Then e3 → 31.0, e4 → 32.4, rebuild montage 33.8–35.8 (3–4 block pops on the beat). f1 onward stays as written, so the length stays ~45 s.
6. **MUST — lang code.** The runbook LINES format needs `"en-us"`, not `"en"`. Change b3, c3, d3, e2, f2, g2 (and the new e2c) to `en-us`.
7. **NICE — f1 is long** (~2.8–3 s, over the ~2.5 s target). Split it into two Golu lines for clearer TTS:
   `f1a | 36.0 | golu | hi | गुस्सा आए तो…` / `f1b | 37.0 | golu | hi | रुको, साँस लो, बोलो!` (one card pops per word); f2 at 39.0.
8. **NICE — e1 more natural for a child:** `मुझे गुस्सा आया!` (the "था" is adult-ish and unneeded). On-screen: `मुझे गुस्सा आया! / I felt angry!`
9. **NICE — d2 blow sound.** "फ़ूऊ" may be read oddly by TTS. Use the natural Hindi blow sound: `मोमबत्ती बुझाओ… फूँ!`
10. **NICE — talk to the child** (runbook: Golu talks to the viewer and pauses). Use breath 3 to invite the viewer:
    `d4 | 21.0 | mithu | hi | तुम भी! तुम भी!` with on-screen `तुम भी! / You too!`, then the silent breath with badge 3.
11. **NICE — d3 is borderline long** (~2.6 s). Option: `Smell… and blow!` with the cards still showing the full phrases.
12. **NICE — block-hat safety.** Make it a soft foam block that lands gently. Mithu is unhurt and grins under it (add a `[giggles]` tag to a3), so the crash stays funny, not painful.
13. **NICE — Hindi-first on screen for "Sorry".** The c1 card `सॉरी! / Sorry!` is the same word twice. Use `माफ़ करना! / Sorry!` (keep the spoken "सॉरी", which is natural).
14. **NICE — teaser.** g1 could tease tomorrow: `शाबाश! कल फिर मिलेंगे!` is fine; optionally Mithu ends on `Tomorrow? Tomorrow!` (question form, per loop rule).
15. **NICE (metadata stage, not script) — title is ~78 chars**, over the 60 limit. Suggest: `गुस्सा आया 😠 Feeling Angry | Golu #shorts`.

## Checks passed
Age fit 2–8 ✓ · nothing scary (cute anger, candle as pictogram) ✓ · surprise < 3 s ✓ · beat every 2–3 s ✓ · loop to frame 1 ✓ ·
Mithu repeats twice in every line ✓ · Bunny fast + learning patience (apology, slow-mo carry) ✓ · Pari/Chintu only via kids chorus ✓ ·
only TTS roles golu/bunny/mithu/kids ✓ · गुस्सा/Angry ≥3× ✓ · no CTA words ✓ · copyright clean ✓.
