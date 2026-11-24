# गोलू और दोस्त — Golu & Dost · SERIES BIBLE (keep every episode consistent with this)

## Premise
A gentle, glossy preschool cartoon (ages 2–8) in Hindi + English. Every episode Golu and his friends discover or learn
one small thing — a word, a habit, a feeling — through play, music and a little comic mishap. Warm, safe, never scary.

## World
A sunny Indian village meadow: rolling green hills, a big mango tree, Golu's hut with a wooden nameplate "गोलू और दोस्त",
a fence, flowers, a smiling sun, puffy clouds and a faint rainbow. Other settings rotate (kitchen, park, school, bathroom,
market, garden, night sky with stars) but always in the same soft-gradient, rounded, glossy style and bright palette.

## Cast (design details: RUNBOOK "CHARACTER DESIGN SHEET (v2)")
- **Golu** — baby elephant, ~4 yrs. Curious, kind, a bit clumsy; gets excited and trumpets. Orange scarf with a yellow
  knot (always). Catchphrase: "चलो, सीखें! — Let's learn!" and "शाबाश! — Well done!". Gag: his trunk gets tangled/curls when he is excited.
- **Pari** — girl ~4 yrs, pigtail buns with pink bows, pink polka-dot dress. Cheerful, asks "क्यों? — Why?".
- **Chintu** — boy ~5 yrs, yellow T-shirt with orange zig-zag, blue shorts, green shoes. Energetic, loves to count and race.
- **Bunny / बनी** — fast, impatient bunny (to be redrawn in v2 style on first use).
- **Mithu / मिठू** — parrot who repeats everything twice ("Red! Red!") — his running gag; does the English repeats (v2 redraw on first use).
- Voices (Fish Audio, fixed per character): see voices_fish.py ROLE map. Never change a character's voice.

## House styles (chosen by the owner, 21 Nov 2026)
- **Daily learning episodes = "Soft 3D plush" (option B).** Characters keep the v2 designs and get the `f3d` lighting filter
  (soft volume, rim light, specular shine) exactly as gen_episode_template.py applies it to #gwrap / #kidA / #kidB.
  Add a soft contact shadow under every character, gentle depth (blurred far hills), slower camera moves than 2D.
  New characters/props that are "hero" objects also get filter="url(#f3d)". Never apply it to text.
- **"Golu Masti" = weekly silent slapstick (option G), every WEDNESDAY evening slot.** No spoken words at all:
  only giggles, gasps, "uh-oh!", trumpets, kids' laughter (Fish tags like "[giggles]") and lots of SFX (whoosh, pop, boing,
  impact-bass). Story = one physical gag in 25–35 s: setup → mishap → bigger mishap → twist → everyone laughs → loop.
  Bold outlines allowed for the gag moments, takes and double-takes, speed lines, "BONK!"-style impact stars (Hindi + English
  sound words: "धड़ाम! BONK!"). Title: "Golu Masti #N 😂 <Hindi> | <English> #shorts". Still Made for Kids, never mean or violent —
  nobody gets hurt, mishaps are silly (slipping on a banana peel, a ball bouncing back, a cake landing on a head).
- Style references are broad families only (Pixar/Illumination-like soft 3D; Oggy/Mr Bean-like silent comedy) —
  never copy any show's characters, designs, music or gags.

## Music identity
- Golu theme: a bright 2-bar motif (xylophone + glockenspiel, major key, 120 bpm) that opens and closes every episode,
  made with music_gm — keep the same seed for the motif so it is recognisable; the rest of the song changes per episode.
- Character colours: Golu = xylophone + round bass, Pari = glockenspiel, Chintu = woodblock/claps, Bunny = pizzicato strings,
  Mithu = whistle/flute.

## Rules
- Original characters, music and art only. No copyrighted shows, brands or real people.
- Always bilingual on screen (Devanagari big, English below). Kids' chorus says the English repeats.
- Every episode ends with a loop back to the first frame and/or "कल फिर मिलेंगे! — See you tomorrow!".

## Open continuity threads
(kept in golu_state.json → `continuity`)


## Golu look (current)
Soft-3D SVG Golu v2 (front-facing, orange scarf). The Lottie test was rejected by the owner.

## Added by Ep8 (23 Nov 2026, "गुस्सा आया / Feeling Angry")
- **Golu's playroom set** (Ep8 src gen_episode.py `room()`): peach wall, sunset window with lilac curtains, bunting, wall lamp, toy shelf (ball, drum), toy car, teal round rug, wooden floor. Reuse for home/bedtime/feelings episodes.
- **Golu angry rig** (Ep8): `#g-angry` (soft red cheeks + flush + slanted brows, fade in 3 steps), `#g-brows`, `#g-frown` (resting mouth while angry), steam puffs above the ears. Anger stays cute — never teeth, shouting faces or throwing.
- **Toy blocks** ×5 (red/yellow/blue/green/orange foam blocks) + Mithu's block-hat (`#m-hat` inside `#m-head`).
- **Calm-down tool (callback):** "रुको, साँस लो, बोलो — Stop, breathe, say it" with "फूल सूँघो, मोमबत्ती बुझाओ — Smell the flower, blow the candle". Golu can model it again whenever a character has a big feeling.
- **Layout rule (Shorts UI):** keep faces above y ≈ 1550 and out of the right 120 px (Ep8 shifts the whole scene up 200 px); text cards ≤ 760 px wide.
- Bunny's arc: Ep8 she says sorry at once and helps rebuild (slow-motion push gag).
