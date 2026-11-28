# Ep 12: Script Review (Stage 4, independent): एक मोटा हाथी / One Elephant Went Out to Play

**Verdict: APPROVE WITH FIXES.** The counting logic is correct: 1 calls 2, then 2 call 3, and एक-दो-तीन / One-two-three are counted in order. Every Devanagari line is spelled correctly (मकड़ी, जाले, झूम, मज़ा, दूजे, बुलाया, कूदो, टोपी, मिलेंगे). The Hindi wording is our own (it avoids "जाके फँसा" and "बुलाओ भाई"), and the English is the traditional text. The hook is good, the spider is friendly, the hat count is right (#5 after block, sand, leaf, sock) and the loop works. Fix the items below before the voice stage.

## MUST
1. **e3/e4 must be sung by the kids, not Golu alone.** The bilingual rule says the kids' chorus says the English. Change the speaker for e3 and e4 to `kids`. Golu can mouth along in the animation, but there is no separate Golu English take.
2. **e4 is too long for the beat.** It has about 11 syllables, which comes to about 2.8 s at 120 bpm. Replace it with:
   `e4 | 20.0 | kids | en-us | They called for another to come!`
   This is still the traditional sense, at 8 syllables (about 2 s). The on-screen text stays "आ जा! / Come!".
3. **Remove the false tease "कल चार हाथी?".** Tomorrow's morning rhyme will be a different rhyme (rhymes_done forbids a repeat within 30 days), so the line would break a promise to the viewer. g1 is also about 2.9 s, which is too long. Replace g1/g2 with:
   - `g1 | 33.4 | golu | hi | चौथा हाथी… तुम? | trunk points at the camera, happy eyes | चौथा हाथी… तुम? / Number four… you?`
   - `g1e | 35.0 | kids | en-us | Number four — you! | kids point at the camera, then hop off sideways | —`
   - `g2 | 36.3 | golu | hi | कल फिर मिलेंगे! | waves with his trunk | कल फिर मिलेंगे! / See you tomorrow!`
   - `g3 | 37.5 | mithu | en-us | Tomorrow! Tomorrow! | Mithu bobs | —`

   This keeps the 2.5 s limit, the teaser question, Mithu's double repeat and the loop at 38.5–40. It also turns the cumulative rhyme into an invitation to join in. The action cell "holds up…" was unfinished and is replaced above.
4. **On-screen text order: Devanagari always on top.** e1–e4 currently put English first. Change them to `दो हाथी / Two elephants`, `मकड़ी का जाला / Spider's web`, `इतना मज़ा! / Such fun!`, `आ जा! / Come!`.
5. **How to handle "मोटा".** Keep it, because it is the searched title phrase and the common folk opening. "मोटा हाथी" describes a big animal fondly; it isn't an insult. Set these guardrails:
   - **(a)** "मोटा" is spoken only once (a1). It appears on the title card at 0 s and at the loop, never in a recap, and is never applied to Pari or Chintu (they are "हाथी", "दो हाथी", "तीन हाथी").
   - **(b)** No weight jokes. The web never strains, creaks or nearly breaks because of Golu. In a2, change "web sags" to "web springs, BOING". The c2 payoff is about three friends jumping together, not about being heavy.
   - **(c)** Nobody laughs *at* anyone. Everyone laughs at Mithu's hat, and Mithu is proud of it.
   - **(d)** The description should not use "fat" in English. Use "big elephant" or "One Elephant".

## SHOULD
6. **a4 spelling.** Standard Hindi writes "आ जा" as two words. Use `दूजे हाथी को बुलाया — आ जा!` and on screen `आ जा! / Come!`. The TTS also reads it more naturally as two words.
7. **Kids' chorus voices.** If the two child chorus voices are Pari's and Chintu's Fish voices, b1 ("दो हाथी! Two!") is fine. But Chintu should not clearly be heard before he enters at c1. Either use the generic kids' chorus voices for b1, e1 and e2, or have Pari say b1 solo (`pari | hi | दो हाथी! Two!`).
8. **Beat gaps over 3 s.** Add a visual or SFX pop in these windows:
   - e3–e4 (17.8–20.0): Golu's trunk curls with excitement, which is his gag. Add a "boing" SFX.
   - e4–c1 (about 22–23 s): Chintu's paper ears flap in, with a whoosh.
   - g1–g2: a card pop on "तुम?".
9. **Melody check, to pass on to the music stage.** The music_gm tune must not follow the well-known Hindi school tune or the Sharon, Lois & Bram melody. Use an original contour and never use a reference track (COPYRIGHT RULES).

## NICE
10. **Spoken "One".** The English "One" is heard only once (d1); it is shown 3 times. Optionally, Mithu says "One! One!" at about 2.4 s, under the end of a1, if the mix allows. If not, change the script note to read "shown 3×, heard 2× in Hindi and 1× in English".
11. **Golu's catchphrase.** After the BOING, Golu could add `शाबाश! Well done!` before m1, but only if the timing holds. Otherwise skip it.
12. **Title length (for the publish stage, not the script).** The brief's title is about 90 characters. That meets the GROWTH limit of 90 or fewer but breaks the ALGORITHM limit of 60 or fewer. A fit: `एक मोटा हाथी 🐘 One Elephant | Hindi Rhymes #shorts`.
