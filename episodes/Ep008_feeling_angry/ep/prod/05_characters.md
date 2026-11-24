# Ep 8 — Stage 5 Character & world sheet

| Character | Design version | Today | Expressions / rig needed |
|---|---|---|---|
| **Golu** | v2 soft-3D SVG (template GOLU + visible yellow bow-knot left of collar, f3d) at (500,1840) scale .62 | orange scarf, holds a block in his trunk | proud happy (closed eyes), shock (pupils up, ears out), **ANGRY (new)**, breathing in/out, calm smile, laughing |
| **Bunny** | v2 (Ep6 cast file bunny_v2.svg.txt, f3d) at (985,1840) scale .5 | — | zoom-in with skid lean, sad ears + sad mouth (#b-sad), happy eyes, slow-motion carry, lip-sync on #b-mouth |
| **Pari** (#kidA) | v2 template KIDS, scale .46 at x 95 | pink polka-dot dress | worried, "stop" hand (arm up), cheer, talk mouths |
| **Chintu** (#kidB) | v2 template KIDS, scale .46 at x 245 | yellow zig-zag T-shirt | point, cheer, talk mouths |
| **Mithu** | glossy v2 parrot (cast/mithu_src.txt, f3d), on the toy shelf at (955,1205) scale .36, facing left | wears a soft foam block as a hat after the crash, grins | head bob talk, wing flap |

## NEW rig pieces for Golu (added to GOLU at build time, same soft style, no outlines)
- `#g-angry` (opacity 0 → 1 → fades in 3 steps): soft red cheek glow (radial gradient #ff5a5a→transparent, rx 58),
  a faint warm-red flush over the lower face (opacity .22), and two slanted brows (inner ends down) in #3a2a55.
- `#g-brows` = the normal brows (hidden while angry).
- `#g-frown` = a small pouty down-curve mouth (replaces #g-smile as the resting mouth while angry; lip-sync still toggles #g-mouth with svgOrigin).
- `#steam` (world layer): two cute white steam clouds above Golu's ears that puff and rise; shrink each breath.
Anger is cute, never scary: no teeth, no shouting face, no change of body colour.

## NEW props / set (built once in gen_episode.py, soft-gradient, f3d on hero blocks only)
- **Toy blocks ×5** (130×80, rx 16, glossy gradient + a soft emboss circle/star; red #ff5a4e, yellow #ffc51c, blue #4a8fe0, green #47c46a, orange #ff8a3d) — foam blocks, so the crash is harmless.
- **Playroom set:** peach wall gradient #ffe9d2→#ffd2b0, window with sunset gradient (#ffb36b→#ff8fa8→#8fb8ff top), low orange sun,
  blurred far roofs, curtains (lilac #b9a7ff), table lamp with warm glow, wall toy shelf (ball, drum, toy car — generic, no brands),
  wooden floor #e8b07a, round teal rug #5fc4b8 with a lighter ring.
- **Breath cards:** a pink flower pictogram (5 petals, #ff7fb0) and a candle pictogram (cream candle + small yellow flame that wobbles and goes out) — icons only.
- **Breath badges 1-2-3** (reuse Ep7 count-badge style).

## On-model checks (snapshot): Golu front-facing with knot visible, kids beside him not overlapping his ears, Bunny right of the tower, Mithu fully on the shelf, nobody under the word cards (cards live in y 300–620; characters below y 1080).
