# Ep 5 — Stage 1b Visual refs: soft-3D glossy look for "गाड़ियाँ / Vehicles" (railway-crossing village road)
These are broad style traits only (soft-3D, toy-like preschool CG family). They don't copy any show, character or vehicle design. All vehicles are generic and have no logos, brand names or real railway liveries.

## Style traits
1. **Palette (bright, saturated, warm-sunny):**
   - Sky: top #5ec8ff → horizon #c9f0ff. Sun #ffd84a with glow #fff3b0.
   - Fields/hills: near #7ed957 → #4fb83a, far hills #a8e6a0 (lighter + bluer for depth).
   - Road: warm asphalt #6b6f80 with a soft top-light #8a8fa3, centre dashes #fff6d6. Dirt verge #e8c48a.
   - Rails: steel #9aa3b5 rails on brown sleepers #a8714a. Boom gate stripes #ff4d4d / #ffffff, signal post #3a3f4f with light #ff3b3b / #3bdc6b.
   - Vehicles (hero props): Train engine #ff5a4f body + #ffc93c trim + #3fa9f5 windows · Bus #ffb81c + #ff7a1c stripe · Tractor #3fbf5a + #ffd23f wheels hubs · Fire truck #ff3b3b + #ffffff ladder + #ffd84a light. Tyres #2f3340 with hubcap #d9dde6.
   - Characters stay as in v2 (Golu #a6c0f7 → #6688dd, orange scarf, Mithu green parrot).
2. **Shading = soft-3D volume via radial gradients.** Every body gets a light-to-dark radial gradient (light at top-left, about 30% in), a soft darker belly or underside (about 15% darker), and one or two **specular highlights**: a white ellipse at 60–80% opacity at top-left plus a tiny dot. Rounded-rectangle vehicle bodies (rx ≥ 30) read as toys. Apply `filter="url(#f3d)"` to every hero vehicle and character, never to text.
3. **Outline policy:** **no thick black outlines.** Separate shapes by value and colour only. A darker same-hue edge at most (1–3 px, about 25% darker, low opacity). Windows have a soft inner shadow and a diagonal white glint stripe.
4. **Eyes:** characters keep huge glossy eyes with two shine dots and lashes. Vehicles stay **non-faced props** by default (safer for originality, and they don't compete with Golu). Headlights get a round glossy "shine" instead. Optional: tiny blush-like round lamps on the train front.
5. **Lighting:** a warm morning key light from top-left (sun), a cool sky-blue rim light on the right edges (#bfe8ff at 40%), and soft **contact shadows** (ellipse #000 at 18–25% opacity, blurred) under every wheel and character. A light bloom on the sun and on the fire-truck beacon when it flashes.
6. **Background detail level: LOW, in 3 depth layers.** Far: blurred hills (stdDeviation about 6) plus 2–3 puffy clouds. Mid: field strips, a few round trees, a small bus-stop shelter, the crossing gate. Near: the road and the rails, fully crisp. No clutter, no text signs except one bilingual board "रेलवे फाटक / Railway Crossing" in Baloo2. Leave the top 35% of the frame fairly clean for the big word cards.
7. **Camera framing for 9:16 (1080×1920):** the road runs horizontally at y≈1350–1550 so vehicles cross left→right through the middle third. Golu centred low (translate(540,1850) scale ≈ .9), Pari at x≈150 and Chintu at x≈930 (scale .78). Word cards at y≈350–650 (big Devanagari, English below). Each vehicle enters on a beat with a small camera punch-in (scale 1.00 → 1.06, 0.25 s) and a whip/whoosh. Slower, smoother moves than 2D. Speed lines are allowed as soft white streaks (not ink lines).
8. **Motion feel:** vehicles squash slightly on stopping (scaleX 1.04 / scaleY .96, then settle), wheels rotate, a body bounce of 4–6 px on the beat, and puffs of soft white steam and smoke circles (train/tractor) that pop and fade.

## Avoid
- Thick black outlines, flat vector fills with no gradient, gritty or realistic textures, dark night palette.
- Faces on vehicles that look like any existing vehicle-character show. Real brand logos (no "JCB", no railway or manufacturer marks), number plates with real formats.
- Dangerous behaviour: kids standing on the tracks, near a moving train, or crossing while the gate is down. Pari, Chintu and Golu stay behind the boom gate and wave from a safe distance (good safety modelling).
- Busy backgrounds behind word cards, text cut off at the 9:16 edges (keep a 60 px safe margin), and characters overlapping the cards.
- Scary sounds or visuals: the fire truck is cheerful, with no fire or emergency shown, just a "नी-नो" siren and flashing light.
