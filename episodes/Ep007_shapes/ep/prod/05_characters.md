# Ep 7 — Character & world sheet (Stage 5)

| character | design version | position / scale | today | expressions & acting needed |
|---|---|---|---|---|
| Golu | soft-3D SVG v2 (`GOLU`, gen_episode_template.py) + f3d; orange scarf with visible yellow knot | centre, feet (540,1840), scale .62 | roti lands on his head as a hat (hook), then hops off | surprised (eyes up), happy closed eyes on every right answer, trunk curl (−60/−80°) when excited, arm up on "चलो, आकार सीखें!", both arms up on recap, wave on bye; lip-sync via #g-mouth opacity toggle + svgOrigin "-62 -314" |
| Pari (#kidA) | template KIDS v2, f3d | left, feet (150,1840), scale .5 | counts the samosa corners (points with right arm) | talk (kmouth/ksmall toggle), cheer (arms, offset), point |
| Chintu (#kidB) | template KIDS v2, f3d | right, feet (930,1840), scale .5 | counts the biscuit corners (bible: loves to count) | talk, cheer, point |
| Mithu | glossy v2 parrot (cast/mithu_src.txt from Ep4–6), f3d, mirrored to face the food | on the kitchen shelf (905,1250), scale .42 | all English repeats, twice | head bob + beak jaw + body bounce per line, wing idle |

## New props (designed for this episode, same glossy soft-gradient language, no outlines, no brands/logos)
- **Roti** — round, r=150, golden radial gradient `gRoti`, seeded brown spots clipped to the disc, soft highlight. Spins + flips (scaleY) via nested attr-transform groups (#fir rotate, #fiq scale). No f3d (the lighting filter turned the scaled disc black in a test frame — fixed by dropping it; the gradient gives the volume).
- **Biscuit** — a TRUE square (280×280, rx 22), `gBisc` gradient, dashed inner rim, 3×3 dot holes, no name/emboss (script review fix #2). f3d.
- **Samosa** — side-on flat triangle with rounded corners, `gSamo`, crimp dots on the base, highlight streak. f3d. Wobble via attr rotate around its base.
- **Shape outlines** — glowing traced outlines (pink circle / blue square / green triangle, stroke 12, dash-offset draw) + white corner count badges (same style as Ep6's line-up badges).
- **Kitchen set (NEW)** — cream wall, window with winter-morning sky, low sun and drifting mist, pink curtains; hanging steel ladles; wall clock with moving hand; wooden shelf with plain jars + steaming steel cup; mint tiled backsplash + teal counter with a roti basket; checked terracotta floor. No stove or fire on screen.

Snapshot check (draft): all characters on-model, no overlaps, scarf knot visible, text inside title-safe area.
