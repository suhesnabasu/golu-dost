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

## Golu's friend gangs (introduced by the owner, 24 Nov 2026 — recurring side characters)
Owner-made intro videos (look reference + reusable footage):
- https://raw.githubusercontent.com/suhesnabasu/golu-dost/media/media/Golu_Friends_Guess_Who.mp4 ("पहचानो कौन? Guess who!" — all five gangs)
- https://raw.githubusercontent.com/suhesnabasu/golu-dost/media/media/Golu_New_Friends_Laddoo_Tower.mp4 ("गोलू मस्ती #0 — लड्डू टावर / Laddoo Tower")
1. 🍡 लड्डू गैंग · The Laddoo Gang — round orange laddoos with faces; sweet, giggly, "masters of running away" (गोल-गोल, मीठे-मीठे… भागने में उस्ताद!). Hide in a steel dabba; love being stacked into a tower.
2. 💗 ब्लॉबू टोली · The Blobbu Gang — soft colourful jelly blobs (pink, purple, teal, orange) with simple dot/line eyes; bouncy, hide behind laundry/clouds ("बादल!"), play hide-and-seek.
3. 🏺 चाक वाले · The Clay Critters — little clay creatures (brown, beige, pink) with antennae; made on the potter's wheel, hide in matkas, spin ("गोल-गोल! Spin!").
4. 🌧️ बारिश वाले · The Rain Critters — tall soft blocks (yellow, pink, green) with antennae/ears and big smiles; love rain, splashing and paper boats ("छपाक! चलो नाव चलाएँ!").
5. 🏏 गली क्रिकेट टीम · The Gully Cricket Team — chunky round-top blobs (blue, orange, teal) with a bat; play behind the brick wall; catchphrase "बल्ला, गेंद… छक्का!" and a running joke "शर्मा जी!".
Use: one gang can guest in an episode (max one gang + Golu + Pari/Chintu/Mithu on screen, no overlaps), especially "पहचानो कौन?" guessing games, counting (count the laddoos!), colours (Blobbu colours) and rain/weather topics. Keep their look exactly as in the videos; never redesign them.

## Open continuity threads
(kept in golu_state.json → `continuity`)


## Golu look (current)
Soft-3D SVG Golu v2 (front-facing, orange scarf). The Lottie test was rejected by the owner.

## Props & sets added by Ep 9 (26 Nov 2026, गोलू की गाड़ियाँ #2)
- Railway crossing (Ep5 set) re-used with the gate UP and the signal green when no train comes.
- Vehicles in src_Ep009 props.py (glossy, no outlines, face RIGHT, enter L exit R): हवाई जहाज़ aeroplane (spinning propeller), एम्बुलेंस ambulance
  (white + red stripe, **heart-with-plus emblem — never the Red Cross emblem**, red/blue beacon), खुदाई मशीन digger (never "JCB"; arm pivots, sand bucket),
  ऑटो रिक्शा auto-rickshaw (yellow canopy, green body, 3 wheels). Ep5 props: train, bus, tractor, fire truck.
- Mithu's hat gag now has two hats (Ep8 toy block, Ep9 sand clump) — a running gag: things land on Mithu's head and he is proud ("मेरी टोपी!").
- Bunny stays OFF roads: on the crossing set she stands on the grass on the children's side (left, x≈215), arriving from the left.

## Props & sets added by Ep 10 (25 Nov 2026, Golu Masti #1 — गोलू की छींक / Golu's Big Sneeze)
- First "Golu Masti" (Wednesday silent slapstick) made by the pipeline: vocal sounds only (Fish: "आ… आ…", sneezes, giggles, "उह-ओह!", laughs), bilingual sound-word cards, music dips under each build-up.
- Winter park = Ep6 park recoloured (autumn trees, haze band, fallen leaves), slide + sandpit removed; leaf pile on the left (215,1440 — Bunny's spot), tree stump on the right (895,1462 — Mithu's perch). Source: src_Ep010 gen_episode.py park().
- Golu rig: #g-elbow = front copy of the right arm drawn AFTER the trunk inside g-head (pivot 128 -226) for covering a sneeze/cough with the elbow; hide #g-armR while it is up. Good-habit rule: always cover sneezes/coughs with the elbow or a tissue, never a scarf/hand.
- Mithu's 3rd hat: a leaf (#m-hat leaf version). Mithu's loose green feather (#feather) is a new prop/trigger.
- Bunny: spin her in a separate #bspin group (svgOrigin "0 -180"); never put rotation+svgOrigin on the same group as her y moves (it offsets her position). Leaf ears #b-leaf after landing in leaves.
- Filter rule: never put filter="url(#f3d)" on a group with a NEGATIVE scale (mirrored Mithu rendered as a black silhouette) — wrap: <g filter><g transform="scale(-…)">.
