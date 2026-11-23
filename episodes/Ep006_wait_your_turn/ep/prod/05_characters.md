# Ep 6 — Character & world sheet (Stage 5)

| character | design version | today | expressions / acting needed |
|---|---|---|---|
| Golu | soft-3D SVG Golu v2 (template GOLU, f3d), scarf knot at cy −212 (visible) | foreground row, scale .56; rides the slide last (mid-ground .39) | surprise (trunk up −30° on frame 1 + loop), looks (pupils), kind smile, happy closed eyes (praise, moral, landing), arm gesture to the slide, both arms up (moral), wave (bye), big landing squash |
| Bunny / बनी | **v2 Bunny** (Ep1 remake design: white-lilac glossy, long ears with pink insides, big eyes, buck tooth) — first speaking role in v2 | zooms (hook + 2 cut-ins), rides 4×, exits right (loop) | excited, giggly-dizzy (rotating stars over head), **sad** (new frown #b-sad + drooping ears), foot-tap waiting (new #b-foot), deep breath, happy closed eyes (praised), cheer (arms up) |
| Pari | v2 kid #kidA (pink polka-dot dress, pigtail buns + bows) | steps to the ladder, waits, rides first | **sad** (new frown .ksad + head dips), cheer, chorus lip-sync |
| Chintu | v2 kid #kidB (yellow T-shirt + orange zig-zag, blue shorts, green shoes) | steps up, waits, rides second | sad, cheer, chorus lip-sync |
| Mithu / मिठू | glossy v2 parrot (Ep4/5 source) | perched on the swing's top bar, mirrored to face the slide | talking bob + beak on every line (repeats twice) |

## New in this episode
- **Park playground set** (new): red-orange slide (chute #ff6b4a, blue rails #3b82f6, yellow platform/rungs #ffd23f), sandpit with wooden rim, pink swing frame with two swaying seats (blurred background), neem tree, far hills and trees with depth blur, flowers.
- **Bunny additions:** #b-sad frown, #b-foot (right foot for the tap), #b-stars (dizzy stars). **Kids addition:** .ksad frown for both kids.
- Character rig: every character sits in `#p<name>` (feet position + scale, tweened as an SVG transform attribute — NOT GSAP x/scale with svgOrigin, which drifted when the scale changed) and `#r<name>` (lean, bob, squash).
- Safety staging: one rider at a time, climbs holding the rails, sits and slides feet first into soft sand, steps out to the back of the line.
