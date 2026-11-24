# Ep7 Visual References — "Soft-3D plush glossy preschool" (style traits only)

Sources consulted for general style vocabulary (no assets copied):
- https://icons8.com/illustrations/styles/3d-kindy · https://icons8.com/illustrations/styles/3d-playful (rounded "toy" 3D family)
- https://design.tutsplus.com/articles/the-elements-of-cute-character-design--vector-3533 (cute proportions: big head, big eyes, small features)
- https://la.disneyresearch.com/wp-content/uploads/Designing-Animated-Characters-for-Children-of-Different-Ages-Paper.pdf (younger kids prefer rounder, simpler, high-contrast characters)

## Style traits
1. **Palette (warm, high-key, saturated but soft):**
   - Sky top #7EC8F2 → horizon #DFF3FF · Sun #FFD54A (glow #FFF3B0)
   - Near grass #6CCB5F → shadow side #3FA34D · far hills #A8DDA0 (desaturated)
   - Golu body #9FB6D6 (light #C9DAF0, shade #6F88AD) · scarf #FF8A3D, knot #FFD23F
   - Pari pink #FF8FB8 · Chintu yellow #FFD447 / blue #4A8FE0 · Mithu green #47C46A + red beak #FF5A4E · Bunny #F4EEE8
   - Kitchen (Ep7): warm wall #FFE8C7, wood counter #D9A066 (shade #B07A45), tawa #4A4A55, roti #F2C27A with brown spots #C98A44, samosa #E8A548, biscuit #E9B96E
   - Ink/text dark #3A2A55 (never pure black).
2. **Soft radial-gradient shading:** every hero shape uses a radialGradient with highlight offset to top-left (cx≈35%, cy≈30%), light → base → shade at ~70–100%; plus the `f3d` filter (soft volume, rim light, specular) on characters and hero props only.
3. **No thick outlines:** forms are defined by colour and shading; at most a 1–2 px edge one shade darker than the fill. (Bold outlines only in Wednesday "Golu Masti" gag moments.)
4. **Big glossy eyes:** large dark iris (#2B2140) with 2 white speculars (big top-left, small bottom-right); eyes ~1/4 of face width; happy closed eyes = soft upward arcs.
5. **Blush & tiny features:** pink cheek ovals #FF9DB0 at ~45% opacity, Gaussian-blurred; small smile, small nose; rounded, chubby limbs, no sharp corners anywhere (rx/ry on all rects).
6. **Contact shadows:** blurred dark ellipse (#000 at 18–25% opacity, stdDeviation ~6) under every character and prop; shrinks/fades when a character jumps.
7. **Depth:** 3 layers — far hills/back wall blurred (stdDeviation 3–5) and lighter; mid set sharp; foreground props slightly larger. Slow, gentle camera push-ins (≤ 8% zoom over 3 s); warm ambient light, light from top-left.
8. **Gloss & plush feel:** small white specular ellipse (opacity 0.5–0.7) on round surfaces (heads, roti, balloons); subtle soft-fuzz noise texture at low opacity optional.
9. **Bilingual text:** Baloo 2 ExtraBold, Devanagari line big (≈ 1.0) with English below (≈ 0.65 size); fill bright (#FFFFFF or topic colour) with thick white/dark stroke (paint-order: stroke; 8–12 px white stroke on coloured fill, or dark #3A2A55 stroke on white fill) + soft drop shadow; pop-in with scale 0→1.15→1 bounce. Never apply f3d to text.
10. **9:16 framing (1080×1920):** keep faces and text in the middle 80% (safe area: top 220 px for series badge, bottom 320 px clear of Shorts UI); characters' eyes near upper third; series badge small in top-left corner; Golu's face + action visible in frame 1; last frame matches frame 1 for the loop.

## Shapes episode specifics
- Shape "reveal" = glowing outline (#FFFFFF, 6 px, soft glow) tracing around the food, then a flat bright shape icon floats up beside the word: Circle #FF5A4E, Square #4A8FE0, Triangle #47C46A (consistent colour per shape for future #2).
- Steam curls: white, 30% opacity, blurred, slow rise.

## Avoid
- Copying any show's characters, designs, logos, colour schemes, sets, music or catchphrases (e.g. no Peppa/Cocomelon/Bluey/Chhota Bheem lookalikes); style families only.
- Brand logos on props (no real biscuit/packaging brands), real people, text in the scene other than our own.
- Pure black, harsh hard shadows, sharp corners, scary faces, flames near characters (tawa shown off-heat or with a tiny safe glow only).
- Dense backgrounds or busy patterns that compete with the taught object; more than ~3 props in focus at once.
- Thin, small or unstroked text; text in the bottom Shorts UI area.
