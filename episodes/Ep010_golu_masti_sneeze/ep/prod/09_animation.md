# Ep 10 — Animation & build (Stage 9)
- gen_episode.py built from Ep9's composition helpers + Ep6's park set (winter recolour), template GOLU v2 (+ scarf bow-knot) / KIDS / f3d, Ep8-9 Mithu (+ leaf hat), v2 Bunny (+ leaf ears, #bspin wrapper).
- Character acting (types/character.md): anticipation in steps (head tilt back, trunk curl + twitch, squint) → fast snap (power3.in 0.08 s) → elastic settle; ears flare offset (left 0.05 s before right, different amounts); squash on every landing (Mithu hat, Bunny pile, hops); eyes look at the feather, at Mithu's hat, at Bunny; holds after each mishap; blinks offset per character.
- Lip-sync: Golu + Bunny mouths toggle pre-drawn shapes with svgOrigin (never CSS transform-origin).
- Bugs found in snapshots and fixed: Mithu rendered as a black silhouette (filter on a negatively-scaled group → moved filter to a parent group); Bunny drifted below the pile after her spin (rotation+svgOrigin offset on the same group as y → spin moved to its own #bspin group); elbow icon overlapped the English card → removed (the action shows it).
- hyperframes@0.9.72 check: 0 errors. Snapshots in prod/qa/.
