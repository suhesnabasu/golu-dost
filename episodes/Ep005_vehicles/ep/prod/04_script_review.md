# Ep 5 — Script Review (Stage 4) · गाड़ियाँ / Vehicles

Overall: the script fits ages 2–8 well, the vehicle words रेलगाड़ी / बस / ट्रैक्टर / दमकल are correct and natural, and the hook, loop, ending line, Mithu gag and the no brands / no "subscribe" rules are all followed. Fixes below.

1. **MUST — Each Hindi vehicle word is said only 2× (Golu + recap). The rule is 3×.** The English words are said 4×. Also, the RUNBOOK says "then everyone says both together", but the kids' lines are English only. Fix: change c3/d3/e3/f3 to Hindi + English + sound, e.g. kids "रेलगाड़ी! Train! Choo-choo!", "बस! Bus! Beep beep!", "ट्रैक्टर! Tractor! Vroom vroom!", "दमकल! Fire truck! Wee-woo!" (each about 2–2.3 s). These lines mix two languages, so give them lang "hi" (Fish S2 handles the switch) or split each into a hi cue and an en-us cue 0.15 s apart.
2. **MUST — Safety staging. Nobody should be near the track or the road.** In the brief, Pari and Chintu stand "behind the fence", which puts them on the road/track side. Golu is "at the crossing" while a train "whooshes past behind him". Fix: all five characters stay on the viewer's side of the low fence, with the road and track behind it. The boom gate is already DOWN and the signal red on frame 1 (this also matches the loop). The train passes on the far track, and only its gust reaches Golu's ears. Nobody steps toward the road when the gate goes up for the bus.
3. **MUST — "नी-नो / Nee-naw" is a British siren sound.** It is not natural Hindi, and it sounds odd in an en-us voice. Fix: use "वीं-वूँ! / Wee-woo!". f1 becomes "दमकल! वीं-वूँ!", which is shorter and fits its 1.5 s window.
4. **MUST — Make the TTS text different from the on-screen text for the onomatopoeia** (keep the correct hyphenated spelling on screen):
   - "घर्र-घर्र" can come out as "ghar ghar" (= house house). TTS: "घर्रर्र घर्रर्र".
   - "छुक-छुक" → TTS "छुक छुक" (use a space, not a hyphen, so there is no pause or stray schwa).
   - "पों-पों" → TTS "पों पों". If the test take sounds wrong, use "पोम पोम".
   - "वीं-वूँ" → TTS "वीं वूँ". English sounds: "Choo choo", "Wee woo", "Beep beep", "Vroom vroom" (no hyphens).
5. **MUST — The timing windows are too tight for TTS.** k1 "कल नई गाड़ी! कल फिर मिलेंगे!" takes about 2.4 s but has only 1.6 s before k2. h1 (kids' chorus, about 2.5 s) has only 2.1 s. Set the CUES from the real durations: start ≥ previous end + 0.15 s. Let the episode run to about 35 s; trim the recap pauses rather than the words.
6. **MUST — The same Hindi sound is glossed two ways.** The hook shows "पों-पों! / Honk honk!" and the bus line glosses पों-पों as "Beep beep". Use one gloss: make the hook card "पों-पों! / Beep beep!", or have the kids say "Honk honk!" for the bus.
7. **NICE — On-screen b1 "गाड़ियाँ सीखो! / Learn Vehicles!" does not match the spoken "चलो, गाड़ियाँ सीखें!".** Use "चलो, गाड़ियाँ सीखें! / Let's learn vehicles!". If time allows, add Mithu "Let's learn! Let's learn!" so the catchphrase is also bilingual in audio.
8. **NICE — Show each sound word on its card under the name** (e.g. "छुक-छुक · Choo-choo"). Sounds are half the lesson but are spoken only once or twice each.
9. **NICE — The brief's "pride" beat and Golu's catchphrase are missing.** After h2, add Golu "शाबाश! Well done!" (about 1.2 s), with a happy closed-eye take. Optionally have g1 talk to the child: "अब तुम बोलो! Your turn!"
10. **NICE — "Vroom vroom" is a car/race sound.** For a tractor, "Brum brum" / "Putt-putt" is closer to घर्र-घर्र. Vroom is acceptable if kept.
11. **NICE — Call it a "red cartoon train", not a "toy train".** A toy at a real crossing confuses the scale, and the same train later stops as a real one. Keep the siren SFX soft (≤0.3) so the fire truck stays cheerful and not alarming.
12. **NICE — Golu's clumsy side appears only in the hook.** A small extra gag, e.g. his trunk tangling during the siren wiggle on f1, would keep his established character.
13. **NICE — Title (about 44 chars, OK).** For search, consider "गाड़ियाँ 🚂 Vehicle Sounds for Kids | Golu #shorts" (about 50 chars, still ≤60).

## Applied changes
- 1 MUST applied: kids' lines c3/d3/e3/f3 now say Hindi + English + sound ("रेलगाड़ी! Train! Choo choo!" …), lang "hi" (code-mixed) → every Hindi word ≥3× (Golu, kids, recap).
- 2 MUST applied: all five characters stand on the viewer's side of the low fence (fence is between them and the road/rails); boom gate DOWN + signal red on frame 1 and on the loop; gate goes up only for road vehicles, nobody moves toward the road.
- 3 MUST applied: fire truck sound is now "वीं-वूँ! / Wee-woo!".
- 4 MUST applied: TTS text differs from screen text for sound words (छुक छुक, पों पों, घर्रर्र घर्रर्र, वीं वूँ; English without hyphens). Screen keeps hyphenated spellings.
- 5 MUST applied: all cues are set from the real Fish durations (start ≥ previous end + 0.15 s, snapped to the beat); target ~35–38 s allowed.
- 6 MUST applied: पों-पों is glossed "Beep beep!" everywhere (hook card too).
- 7 NICE applied: b1 card = "चलो, गाड़ियाँ सीखें! / Let's learn vehicles!".
- 8 NICE applied: each vehicle card shows a third small line with the sound word (Hindi · English).
- 9 NICE applied: added s1 Golu "शाबाश! Well done!" after the recap (catchphrase / pride beat).
- 10 NICE skipped: kept "Vroom vroom" (familiar to toddlers; Hindi घर्र-घर्र carries the tractor sound).
- 11 NICE applied: cartoon-scale train; no siren SFX (voices carry the sound), SFX ≤0.35.
- 12 NICE applied (visual): Golu's trunk curls into a loop/tangle during the "वीं-वूँ" siren wiggle, then springs back.
- 13 NICE applied: title "गाड़ियाँ 🚂 Vehicle Sounds for Kids | Golu #shorts".
