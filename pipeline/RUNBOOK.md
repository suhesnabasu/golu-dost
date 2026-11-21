# Golu & Dost — daily episode runbook

You are producing ONE new episode of the Hindi kids' cartoon "गोलू और दोस्त" (Golu & Dost) and
scheduling it on YouTube. The channel owner is inactive: never wait for approval, never ask questions.
Work end to end, then send one short push/summary.

## Fixed facts
- YouTube channel id: UCWdDaTHUR3AWbXVsMNJ9PQA (posted through Metricool brand blogId **8255605**, timezone Asia/Calcutta)
- Google Drive folder for videos: **17JNsxv9QPuPqefnkkjfqd_BgCI6FDpjo** ("Golu & Dost Videos")
- State file in Drive: `golu_state.json` (same folder; several copies exist — always use the NEWEST by createdTime, never the trashed ones) — read it first, save a new copy last
- **Two Shorts a day, two slots:** the MORNING task posts at **11:00 IST** on `next_post_date_11`; the EVENING task posts at
  **18:00 IST** on `next_post_date_18`. Your task prompt says which slot you are. Each run prepares the NEXT day's Short for its slot.
  The two daily Shorts must be different TYPES (e.g. morning = learning/habit, evening = story/riddle/rhyme). Every Sunday also post a compilation if the plan says so (optional; skip if short on time).
- Language: **BILINGUAL Hindi + English in every video (one channel, one video).**
  - Dialogue is simple Hindi, and every key word or lesson is said in BOTH languages, Hindi first:
    "एक — One!", "लाल — Red!", "सेब — Apple!", "धन्यवाद — Thank you!". Golu says the Hindi word, Mithu repeats it in English
    (he repeats everything anyway — that is his running gag), then everyone says both together.
  - Story lines can be Hindi; the lesson/moral line at the end is said in Hindi then English ("मिलकर बाँटो — Sharing is caring!").
  - On-screen text shows BOTH: big Devanagari line + English line under it (e.g. number card "1 / एक / One").
    Use Baloo2 (has both scripts); English lines a little smaller.
  - English lines use the Kokoro English voice (`lang="en-us"`, voices af_heart / af_bella pitched like the Hindi cast);
    `voices2.py` LINES take (id, role, lang, text) with lang "hi" or "en-us".
  - Title format: "<Hindi title> | <English title> | Learn in Hindi & English #shorts" (≤100 chars),
    description: 2 Hindi lines + 2 English lines, hashtags in both (#HindiKahani #KidsLearning #HindiEnglish #Shorts).
- Audience: kids 2–8. Always `madeForKids: true`. No copyrighted characters, brands, real people, scary or violent content.
- Cast: Golu (baby elephant, curious, clumsy, kind), Bunny/बनी (fast, impatient), Mithu Tota/मिठू (parrot, repeats things twice).
- World: mango tree, hut, fence, wooden nameplate "गोलू और दोस्त", sky that can go day→night.

## Setup (each run starts in a fresh workspace)
1. Download `golu_pipeline.tar.gz` from the Drive folder (Google Drive connector `download_file_content`), extract to `/home/claude/golu_pipeline`.
2. `cd /home/claude/golu_pipeline && pip install --break-system-packages -q kokoro-onnx soundfile numpy pillow pretty_midi mido`
   and `apt-get update -qq && apt-get install -y -qq fluidsynth fluid-soundfont-gm` (real instrument samples, MIT licence).
   Set `export KOKORO_DIR=/home/claude/golu_pipeline`.
3. Voice model (GitHub is reachable):
   `curl -sSL -o kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx`
   `curl -sSL -o voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin`
4. HyperFrames project: `npx --yes hyperframes@0.9.72 init ep --example blank --resolution portrait --non-interactive --skip-skills`,
   then copy `assets/*` into `ep/assets/`. (The CDN is blocked; the composition loads `assets/gsap.min.js` locally.)
   Chrome is at /usr/bin/google-chrome, FFmpeg is installed.

## Playlist upkeep (do this first, takes 1 minute)
Every Golu video must be in the public playlist **PLFws_tdOs3iI** ("गोलू और दोस्त — सारी कहानियाँ | All Golu Stories"),
so viewers keep watching one episode after another. With Zapier YouTube `youtube_make_api_get_request`, list the channel's uploads
(playlistItems, playlistId UUWdDaTHUR3AWbXVsMNJ9PQA, maxResults 50) and the playlist's items (playlistId PLFws_tdOs3iI);
add every Golu & Dost video (published 21 Nov 2026 or later) that is missing, with Zapier `add_video_to_playlist`
(or a POST to /youtube/v3/playlistItems). Ignore the channel's older personal videos from before 21 Nov 2026.

## VISUAL + AUDIO STYLE (since 21 Nov 2026 — bright, glossy, music-driven)
- Look: bright saturated sky-blue/green world, smiling sun, rainbow, dancing flowers; glossy soft-3D characters drawn with
  radial gradients and highlights, NO thick outlines, big shiny eyes; giant bubbly bilingual words (Baloo2, white stroke).
  `gen_episode_template.py` ("गोलू के रंग #1 / Golu's Colours") is the reference: reuse its gradients, GOLU group, sky,
  hills, flowers, balloon, badge, word cards, confetti, beat-synced dance and lip-sync code; build new props in the same style.
  (`old_storybook_template_reference.py` is the old paper style — do not use it for new episodes.)
- Everything moves on the beat (120 bpm, beat = 0.5 s): character bounce/sway, flowers, camera pulse; each new word/object
  lands ON a beat with a camera punch-in and a sparkle sound.
- Music: `music_gm.make_song()` = original melody, real instrument samples (strummed guitar, xylophone, glockenspiel,
  acoustic bass, light real drum kit), humanised timing. Use a different `seed` (and prog_id) every episode so every song is new.
- Voices: `voices2.make(LINES, outdir)` with roles golu/bunny/mithu/nar and **kids** (a 3-voice children's chorus — use it for
  every English repeat and every "everyone together" line so it feels like real kids singing along).
- Mix: copy `audio_template.py` (cues, lip-sync for golu lines, music ducking under voices, loudnorm -14 LUFS).
- Kokoro voices can talk/chant on the beat but cannot truly sing: write lyrics as short rhythmic chants that land on beats.

## COPYRIGHT RULES (never break)
- Only original characters (Golu, Bunny, Mithu and new ones you invent). Never draw or name characters, logos or brands from
  other shows (no Cocomelon/JJ, Peppa, Disney, Chhota Bheem, Motu Patlu, etc.), never imitate their designs.
- Only original music from `music_gm` — never recreate a known song, nursery-rhyme recording or jingle melody. Traditional
  public-domain rhyme lyrics are allowed only with a new original melody, but prefer fully original lyrics.
- Assets in use are licensed for commercial use: FluidR3 soundfont (MIT), Kokoro TTS (Apache-2.0), Baloo 2 and Kalam fonts
  (SIL OFL), GSAP (free licence), HyperFrames (open source). Do not add any downloaded image, clip, sound or music.
- `isAiGeneratedContent: false` is correct for these cartoons (YouTube's disclosure is for realistic synthetic people/events).

## Make the episode
1. **MONETIZATION FIRST — topic priority.** The channel's main goal is monetization (1,000 subs + 10M Shorts views or 4,000 watch hours).
   About 70% of episodes come from the evergreen, high-search, rewatchable topics parents search for every day.
   Rewatching drives views and subscribers. Rotate within this list:
   - colours (रंग / Colours), counting 1–10 and 1–20 (गिनती / Numbers), Hindi letters अ-आ-इ and English ABC, shapes (आकार)
   - animal sounds (जानवरों की आवाज़ें), vehicles (fire truck, JCB, train, bus, tractor, aeroplane), fruits and vegetables
   - body parts, opposites (बड़ा-छोटा / big-small), days of the week, weather
   - habit songs: brushing teeth, bath time, washing hands, eating food, sleeping on time, "no-no" (manners)
   The other 30% are stories, feelings, riddles and festival specials, for variety and for the inauthentic-content rule.
   Every learning episode ends with a quick recap ("चलो फिर से! Let's do it again!") so kids rewatch, and the best performers
   get numbered sequels ("रंग भाग 2 / Colours Part 2"). Titles lead with the searched word in both languages
   (e.g. "रंग सीखो | Learn Colours with Golu …").
1b. **ALGORITHM RULES (Shorts ranking signals — apply to EVERY episode):**
   - The Shorts feed tests each new Short on a small audience, then shows it to more people only if they don't swipe away,
     watch to the end and rewatch. Optimise for those three things above everything else.
   - **Frame 1 = action, not a title.** The first frame already shows Golu's face plus something bright happening, with
     big words on screen within 0.5 s. No intro, no slow pan, no logo.
   - **Length:** learning/habit Shorts 25–35 s, stories 40–55 s. Shorter means more viewers finish and replay.
   - **Seamless loop:** the last 0.5 s returns to the same pose and background as the first frame, so the replay feels
     continuous and counts as a rewatch. End on a question or a teaser line ("कल? Tomorrow!"), never a slow fade to black.
   - **A new beat every 2–3 s** (pop, zoom, sound effect, new object) and the ठक!/comic surprise inside the first 3 s.
   - **Series branding:** every Short belongs to a named, numbered series shown as a small badge in the top corner
     (e.g. "गोलू के रंग #3 / Golu's Colours #3", "गोलू की गिनती #2", "अच्छी आदतें #4"). Repeat series kids already watched.
   - **Title** ≤ 60 characters: searched word first, both languages, then #shorts, e.g. "रंग सीखो 🎨 Learn Colours | Golu #shorts".
   - Never write "subscribe", "like" or "share" in kids' videos or titles (YouTube treats that as low-quality, pushy kids'
     content). Instead Golu says "कल फिर मिलेंगे! See you tomorrow!" to build the return habit.
   - Same posting times every day (11:00 and 18:00 IST) so returning viewers find new episodes.
2. **Pick the idea — VARIETY IS THE RULE. Optimise for subscribers:** strongest hook in the first 1 second, a series format kids want more of ("भाग 2" / Part 2 of the best performers), end with Golu asking kids to come back tomorrow. Check `history` for which earlier types got the most views (Monday report data) and do more of those. Kids must see their own lives in the channel, so never make two
   episodes of the same type or setting in a row, and never repeat a topic in `history`. Rotate across these TYPES:
   - **कहानी (story with a lesson):** sharing, honesty, saying sorry, waiting your turn, helping, not being afraid of the dark
   - **सीखो (learning):** गिनती, रंग, आकार, जानवर और उनकी आवाज़ें, फल-सब्ज़ियाँ, वर्णमाला अ-आ-इ, हफ़्ते के दिन, मौसम, शरीर के अंग
   - **अच्छी आदतें (daily habits):** brushing teeth, bath time, washing hands, eating vegetables, bedtime, tidying toys, drinking water
   - **गाना (chant-rhyme):** an original rhythmic rhyme with actions (clap, jump), simple repeated chorus
   - **पहेली (riddle/quiz):** "बताओ कौन?" guess the animal/fruit/vehicle from clues, with a pause to answer
   - **सुरक्षा (safety):** crossing the road, not touching the stove, holding hands in a crowd, staying near parents
   - **भावनाएँ (feelings):** feeling angry, sad, scared, jealous of a new baby, and what helps
   - **खोज (explore):** vehicles, space and the moon, rain and rainbows, plants growing, a trip to the zoo/market/beach
   - **त्योहार (festival special)** on its date: 24 Dec Christmas, 31 Dec/1 Jan New Year, 13 Jan Lohri, 14 Jan Makar Sankranti (पतंग), 26 Jan Republic Day (तिरंगे के रंग)
   Also vary the SETTING so it isn't always the mango tree: Golu's home (kitchen, bathroom, bedroom), school/आंगनवाड़ी,
   park, market, rain, night sky, a train ride, a birthday party. Kids relate to places they know. Build new sets with
   the same storybook style (wobbly outlines, paper texture, warm colours). Keep the core cast (Golu, Bunny, Mithu) and
   add recurring family/friends over time (Golu's Mummy, a baby sibling, a school teacher, a new friend around 20 Jan).
   Record the type and setting in `history` so the next run can rotate.
2. **Write a 45–55 s bilingual script** with ~12–16 short lines (characters: golu, bunny, mithu, nar). Follow the retention rules:
   comic surprise in the first 3 s, something changes every 3–5 s, Golu talks to the child and pauses,
   every taught word said 3 times, a feeling before the lesson, a running gag, end with "कल फिर मिलेंगे!" teasing tomorrow.
3. **Voices:** with `voices2.make(LINES, '/home/claude/golu_pipeline/lines')` (see STYLE).
4. **Soundtrack + lip-sync:** copy `audio_template.py`, set `DUR` and the `CUES` list (line id, start second) to today's timing so lines
   never overlap (start ≥ previous end + 0.15 s), adjust SFX times to today's beats, run `python3 audio.py ep/assets` (your copy of audio_template.py),
   then convert `soundtrack.wav` to mp3 (`ffmpeg -i soundtrack.wav -b:a 192k soundtrack.mp3`, delete the wav).
5. **Composition:** copy `gen_episode_template.py` (glossy style, Episode 2 "रंग सीखो") as the starting point. Keep the
   drawing helpers, characters, world, CSS, paper/vignette look and lip-sync code. Rewrite `build_timeline()`,
   the overlays and props for today's story; add new props as SVG with the same wobbly-outline helpers (`blob`, `wpoly`, `P`).
   All on-screen text bilingual (Devanagari + English). Run `python3 gen.py /path/to/ep`.
6. **Check:** `npx --yes hyperframes@0.9.72 check` must show 0 errors (fix `gsap_relative_value_second_writer` by using absolute values).
   Then `npx --yes hyperframes@0.9.72 snapshot --at <5–7 key seconds>` and LOOK at the contact sheet: no overlapping
   characters, no text cut off, speech bubbles not covering faces, Hindi renders (not boxes).
7. **Render:** `npx --yes hyperframes@0.9.72 render -q delivery -o renders/epNN.mp4` (~4 min).
8. **Make the upload copy under 3 MB** (Drive connector limit ~3.1 MB per call):
   two-pass x264 at 720x1280, `-vf scale=720:1280:flags=lanczos -b:v 800k` for ≤25 s (≈ 2400k/seconds·25 for longer; stay < 3 MB),
   audio `-c:a aac -b:a 96k -movflags +faststart`. Check size < 3,000,000 bytes.

## Publish
1. Upload the 720p file to the Drive folder with `create_file` (base64Content = file reference
   `sha256:<sha256>:<absolute path>`, contentMimeType video/mp4, disableConversionToGoogleType true).
2. `share_file` that one file with permissionId `anyoneWithLink`, role `reader`.
   ALSO upload the same 720p file (same file reference) into the PUBLIC episodes folder **169NTC-6EJ1SZB0RFdy9pq6hVLXl4ICR3**
   ("Golu Episodes (public)") named `Ep<NNN>_<short_english_slug>.mp4` (3-digit episode number, e.g. `Ep007_colours_part2.mp4`).
   A weekly GitHub workflow builds the long compilation video from this folder, so the name format matters.
   ALSO save the episode's source to the same public folder as `src_Ep<NNN>_<slug>.tar.gz` (a folder containing your
   gen_episode.py, audio.py, the LINES/script text, index.html and the song's .mid). A daily GitHub workflow copies these
   into the owner's repo suhesnabasu/golu-dost (episodes/…) and the videos into its "episodes" release.
   The name MUST start with `src_` (the compilation builder only reads files starting with `Ep`).
3. Metricool `createScheduledPost`: blogId 8255605, date = **your slot's time (11:00 or 18:00 +05:30) on your slot's `next_post_date_XX`**
   (if that date is already past, use today at your slot time; if that has also passed, tomorrow). Never put two
   episodes in the same slot on the same day, `providers:[{network:"youtube"}]`,
   media = the Drive view link, text = bilingual description (2 Hindi lines + 2 English lines + "रोज़ नई कहानी — A new story every day!" + 5–7 hashtags in both languages incl. #Shorts),
   `youtubeData: {title: "<searched word in Hindi + emoji> <English> | Golu #shorts" (≤60 chars, see ALGORITHM RULES), type:"short",
   privacy:"public", tags:[…], category:"EDUCATION", madeForKids:true, isAiGeneratedContent:false}`.
3b. **Instagram Reel (same video, same time).** A second Metricool `createScheduledPost` with the same media link and date,
   `providers:[{network:"instagram"}]`, `instagramData: {type:"REEL", showReelOnFeed:true, isAiGenerated:true}`
   (Meta requires the AI label for AI voices) and `videoCoverMilliseconds` = a moment where the big bilingual word is on
   screen (bright cover in the grid). Instagram page: @____golu__dost. Audience = PARENTS (13+ app). Reach rules:
   - Caption line 1 = searchable phrase parents type, e.g. "Learn colours for kids in Hindi & English 🎈" (Instagram search
     reads captions), then what the child learns in Hindi, then "Play it for your little one…" and a share prompt for
     parents: "Know a parent of a toddler? Send this to them 📩" (sends/shares are the strongest reach signal).
   - "New Golu cartoon every day — full episodes on YouTube (link in bio)".
   - Only **3–5 niche hashtags** (Instagram penalises hashtag stuffing), e.g. #LearnColours #HindiForKids #ToddlerLearning
     #KidsCartoon #GoluAndDost — pick the topic-specific ones each time.
   - The video must have no watermark/logo from other apps (Instagram demotes recycled content). Ours is original — keep it so.
   - Also post the same video as an Instagram **STORY** 5 minutes after the Reel (`instagramData: {type:"STORY",
     isAiGenerated:true}`, no text) so existing followers see it.
   - Trial Reels need 1,000+ followers; once the page passes 1,000, test 2 different hooks a week as TRIAL_REEL.
   No "subscribe" pressure aimed at kids. If Instagram fails, still keep the YouTube post and mention it in the summary.
3c. **Facebook Reel (same video, same time).** A third Metricool `createScheduledPost`, `providers:[{network:"facebook"}]`,
   `facebookData: {type:"REEL"}`, same parent-facing caption as Instagram (5 hashtags) but ending with
   "👉 YouTube: https://www.youtube.com/@youtubesbasu" (a clickable link works on Facebook). Facebook Page id 1413701528499553.
   Links everywhere: YouTube https://www.youtube.com/@youtubesbasu · Instagram https://www.instagram.com/____golu__dost ·
   Facebook https://www.facebook.com/1413701528499553
4. Update `golu_state.json` (append to history: episode number, post date, title, pillar, topic, Drive file id, Metricool post id; increment `next_episode`; set YOUR slot's `next_post_date_XX` to the day after the date you just used; leave the other slot's date unchanged). Read the newest state file again right before saving, so you don't overwrite the other task's update. Drive cannot overwrite file contents, so: `create_file` a NEW `golu_state.json` in the folder (textContent, contentMimeType application/json, disableConversionToGoogleType true), check it was created. NEVER trash or delete any file in the owner's Drive; old copies simply stay.
5. Send a 1–2 line summary (episode title + post time) as a push notification if available.

## Sundays (morning task only): post the weekly long video
GitHub repo **suhesnabasu/golu-dost** builds a 1080p landscape compilation every Sunday at 03:00 IST from the last
14 episodes in the public folder and publishes it as a GitHub Release (tag `comp-YYYY-Www`).
With the GitHub connector, call `get_latest_release` (owner suhesnabasu, repo golu-dost). If its tag is not yet in
`golu_state.json.compilations`, schedule it in Metricool: media = the release asset's `browser_download_url`,
`youtubeData.type: "video"` (NOT short), madeForKids true, category EDUCATION, date = today 19:30 IST (or tomorrow 09:00 if past),
title like "गोलू और दोस्त की कहानियाँ | Golu & Dost Stories Compilation | Learn in Hindi & English (15 min)",
bilingual description listing the episode titles. Record the tag in `compilations` in the state file.
If the release is missing (workflow not set up yet or fewer than 4 episodes), skip silently.
Long videos are the watch-hour engine (4,000 hours route), so never skip one when available.

## Mondays
Also pull last week's numbers (Metricool analytics or the YouTube API via Zapier `youtube_make_api_get_request`)
and send a short report: subscribers, views, best and worst video, and 3 changes for next week. Apply those changes.

## Never
- Never repeat a story, re-upload, or post near-duplicates (YouTube won't pay channels it sees as inauthentic, repetitive content).
- Never use copyrighted characters, songs or brands.
- Never post anything not marked Made for Kids.
