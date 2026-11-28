"""Golu & Dost branding (owner's rule, 26 Nov 2026): every new video gets
  - the watermark (Golu + "गोलू और दोस्त / Golu & Dost ©", 80% opacity) top-right for the WHOLE video
  - a follow badge that pops up twice (at ~35% and ~70% of the video, 3.5 s each — never on the last 1 s so the loop stays clean)
Two outputs, both 720x1280 H.264 under ~3 MB (two-pass) unless --full:
  <out>_meta.mp4  -> Facebook + Instagram  (badge: "फ़ॉलो करें और रोज़ देखें / Follow for a new cartoon daily!")
  <out>_yt.mp4    -> YouTube (Made for Kids: NO "subscribe/follow" wording; badge "रोज़ नई कहानी / New cartoon daily @golu_dost1")
usage: python3 brand.py <in.mp4> <out_prefix> [--watermark-only] [--max-bytes 2990000] [--landscape]
  --watermark-only : compilation / long videos (watermark only, no badges)
  --landscape      : 16:9 input (watermark scaled to the width, top-right)
"""
import subprocess, sys, json, os
HERE = "/home/claude/golu_pipeline"; B = f"{HERE}/assets/brand"
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).strip())
def size(p):
    o=json.loads(subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","json",p]))["streams"][0]; return o["width"],o["height"]
def run(inp, out, badge, wm_only, max_bytes, landscape):
    D = dur(inp); W,H = size(inp)
    tw, th = (1280, 720) if landscape else (720, 1280)
    wm_w = int(tw * (0.30 if landscape else 0.43)); b_w = int(tw * 0.72)
    t1 = max(2.0, D*0.35); t2 = min(D*0.70, D-4.6)
    en = f"between(t,{t1:.2f},{t1+3.5:.2f})" + (f"+between(t,{t2:.2f},{t2+3.5:.2f})" if t2 > t1+5 else "")
    fc = (f"[0:v]scale={tw}:{th}:force_original_aspect_ratio=decrease,pad={tw}:{th}:(ow-iw)/2:(oh-ih)/2,setsar=1[v0];"
          f"[1:v]scale={wm_w}:-1[wm];[v0][wm]overlay=W-w-{int(tw*0.028)}:{int(th*(0.04 if landscape else 0.075))}:shortest=1[v1]")
    inputs = ["-i", inp, "-loop", "1", "-i", f"{B}/golu_watermark_80.png"]
    if not wm_only:
        inputs += ["-loop", "1", "-i", f"{B}/{badge}"]
        fc += f";[2:v]scale={b_w}:-1[bd];[v1][bd]overlay=24:{int(th*0.395)}:shortest=1:enable='{en}'[v]"
    else: fc += ";[v1]null[v]"
    kbps = max(300, int((max_bytes*8/D - 100_000)/1000 * 0.95)) if max_bytes else 2500
    common = inputs + ["-filter_complex", fc, "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-preset", "medium", "-b:v", f"{kbps}k", "-pix_fmt", "yuv420p"]
    subprocess.run(["ffmpeg","-y","-loglevel","error",*common,"-pass","1","-an","-f","mp4","/dev/null"],check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error",*common,"-pass","2","-c:a","aac","-b:a","96k","-movflags","+faststart",out],check=True)
    return out, os.path.getsize(out), kbps
if __name__ == "__main__":
    a = sys.argv[1:]; inp, pre = a[0], a[1]
    wm_only = "--watermark-only" in a; landscape = "--landscape" in a
    mb = int(a[a.index("--max-bytes")+1]) if "--max-bytes" in a else 2_990_000
    if "--full" in a: mb = 0
    for suf, badge in (("meta","golu_follow_meta.png"),("yt","golu_daily_youtube.png")):
        if wm_only and suf=="yt": continue
        o,s,k = run(inp, f"{pre}_{suf}.mp4", badge, wm_only, mb, landscape)
        print(o, s, f"{k}k", "OK" if (not mb or s < 3_000_000) else "TOO BIG")
