# Ep 7 — Script Review (Stage 4) · आकार सीखो / Learn Shapes

**Verdict:** APPROVE WITH FIXES. The script is age-right, accurate and on-format. The hook, recap, loop and bilingual counts are solid.
Fix the three mixed-script chorus lines (TTS/lang tags) and lock the biscuit art to a true, unbranded square before voicing.

## Checks passed
- Lesson words: गोल / चौकोर / तिकोना are correct, everyday Hindi a preschooler hears at home (better than formal वृत्त/वर्ग/त्रिकोण). Roti = circle and square biscuit = square are fair examples. Samosa = triangle works if it is shown side-on (see 5).
- Spelling: all Devanagari is correct (उड़ी has the nukta, मिलेंगे, बिस्कुट, समोसा, शाबाश, सीखें). Phrasing is short and natural.
- Bilingual counts: each Hindi word is said 4 times and each English word 4 times. Hindi always comes first, Mithu gives English twice and the chorus says both. The f2/f3 recap is correctly split by language.
- Retention: the ठक! roti-hat lands inside 3 s and the longest gap between beats is about 2 s. Every line fits in about 2.1 s or less, and the total is about 34 s (within 25–35). The last frame loops to the first (roti on trunk tip). There is no subscribe/like/share.
- Voice: Mithu repeats everything twice. Golu's catchphrases are used ("चलो, आकार सीखें!" as a variant of "चलो, सीखें!", "शाबाश!", "कल फिर मिलेंगे!"), and Chintu counts.
- Safety/copyright: no stove or fire, the jars are plain, and food is handled harmlessly.

## Fixes
1. **MUST — split the mixed-script chorus lines (TTS).** c3, d4 and e4 are tagged `hi` but contain English. A Hindi-tagged voice will mangle "Circle/Square/Triangle" (for example "सर्किल" with Hindi prosody). Replace each with two rows:
   - c3a | 9.6 | kids | hi | `गोल!`   · c3b | 10.3 | kids | en-us | `Circle!`
   - d4a | 16.4 | kids | hi | `चौकोर!` · d4b | 17.1 | kids | en-us | `Square!`
   - e4a | 23.0 | kids | hi | `तिकोना!` · e4b | 23.7 | kids | en-us | `Triangle!`
   Keep the on-screen text as it is. Each pair still ends before the next line starts.
2. **MUST — the biscuit must be a true square** (4 equal sides, equal corner badges) and plain, with no embossed name, logo or pattern that looks like a brand. Many real Indian biscuits are rectangles, and sequel #2 teaches आयत/rectangle, so a stretched biscuit would teach the wrong shape. Add to d1's action: "plain square biscuit, equal sides, no text/embossing".
3. **MUST — confirm the `kids` role is in the voices_fish.py ROLE map.** Runbook step 2 lists only golu/bunny/mithu/nar. If `kids` is missing, map it to the same chorus voice used in Ep5/Ep6. Do not invent a new voice, because the bible says never to change a character's voice.
4. **NICE — let Chintu lead the count** (bible: he loves to count). d2 → speaker `chintu` (if that role exists): `एक, दो, तीन, चार!`, with the kids echoing only the last word if there is time. Otherwise leave it as kids.
5. **NICE — show the samosa side-on** so its silhouette is a clean flat triangle and the dotted outline sits on that face. A ¾-view samosa reads as a cone/pyramid and confuses 3-year-olds. Add to e1's action: "samosa shown flat side-on, clean triangle silhouette".
6. **NICE — give Pari one line** so she is not silent (her trait is asking "क्यों?"). Add b1b | 4.3 | pari | hi | `रोटी टोपी? क्यों?` (giggle), or simply have her lead e2's count. Only do this if timing allows; otherwise skip it.
7. **NICE — end on a sequel teaser** (runbook: end on a teaser line). g1 → `शाबाश! कल — तारा!` + on-screen "कल फिर मिलेंगे! / See you tomorrow! ⭐". Keep "कल फिर मिलेंगे" on screen. If the spoken catchphrase must stay, keep g1 as written and put the ⭐ teaser on screen only.
8. **NICE — TTS pacing:** Fish may pause long at "।" in c1/d1/e1. If the voice comes out over about 2.3 s, use a comma instead: `रोटी गोल है, गोल!`, `बिस्कुट चौकोर है, चौकोर!`, `समोसा तिकोना है, तिकोना!`.
9. **NICE — a2 on-screen "Bonk! A hat!"**: the English for what Mithu says (टोपी) is just "Hat!". Use `ठक! टोपी! / Bonk! Hat! Hat!` to mirror Mithu's double.
