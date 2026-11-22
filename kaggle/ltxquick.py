# Kaggle GPU test: image-to-video with Wan 2.2 TI2V-5B (Apache-2.0) and LTX-Video (OpenRAIL-M). Outputs go to /kaggle/working.
import subprocess, sys, os, time, json, traceback, urllib.request
OUT = "/kaggle/working"; LOG = []
def log(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.append(s)
    open(f"{OUT}/log.txt", "w").write("\n".join(LOG))
try: log(subprocess.run(["nvidia-smi"], capture_output=True, text=True).stdout)
except Exception as e: log("nvidia-smi missing:", e)
import torch
log("cuda available:", torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else "")
if not torch.cuda.is_available(): log("NO GPU - stopping"); raise SystemExit
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-U", "diffusers", "transformers", "accelerate", "ftfy", "imageio", "imageio-ffmpeg", "sentencepiece"], check=False)
import torch
from diffusers.utils import export_to_video, load_image
RAW = "https://raw.githubusercontent.com/suhesnabasu/golu-dost/main/kaggle_req/in/"
imgs = {k: load_image(RAW + k + ".png") for k in ("arjun_comic", "arjun_ai")}
PROMPT = ("A frightened young Indian man sits on his bed at night holding a glowing phone, his eyes dart toward the door, "
          "he breathes heavily and his hands tremble, the ceiling fan turns slowly, cold blue light flickers on his face, "
          "graphic novel animation, subtle natural motion")
NEG = "static, frozen, blurry, distorted face, extra fingers, deformed hands, morphing, text, watermark"
dt = torch.float16
def run(name, fn):
    t = time.time()
    try:
        fn(); log(f"{name}: OK in {time.time()-t:.0f}s")
    except Exception:
        log(f"{name}: FAILED after {time.time()-t:.0f}s\n" + traceback.format_exc()[-2500:])
    torch.cuda.empty_cache()

def ltx():
    from diffusers import LTXImageToVideoPipeline
    pipe = LTXImageToVideoPipeline.from_pretrained("Lightricks/LTX-Video", torch_dtype=dt)
    pipe.enable_model_cpu_offload()
    for k, im in imgs.items():
        v = pipe(image=im, prompt=PROMPT, negative_prompt=NEG, width=480, height=832, num_frames=97,
                 num_inference_steps=30, generator=torch.Generator("cuda").manual_seed(7)).frames[0]
        export_to_video(v, f"{OUT}/ltx_{k}.mp4", fps=24)
    del pipe

def wan():
    from diffusers import AutoencoderKLWan, WanImageToVideoPipeline
    mid = "Wan-AI/Wan2.2-TI2V-5B-Diffusers"
    vae = AutoencoderKLWan.from_pretrained(mid, subfolder="vae", torch_dtype=torch.float32)
    pipe = WanImageToVideoPipeline.from_pretrained(mid, vae=vae, torch_dtype=dt)
    pipe.enable_model_cpu_offload()
    for k, im in imgs.items():
        v = pipe(image=im, prompt=PROMPT, negative_prompt=NEG, width=480, height=832, num_frames=49,
                 num_inference_steps=30, guidance_scale=5.0, generator=torch.Generator("cuda").manual_seed(7)).frames[0]
        export_to_video(v, f"{OUT}/wan_{k}.mp4", fps=24)
    del pipe

imgs = {"arjun_comic": imgs["arjun_comic"]}
run("LTX-Video", ltx)
log("DONE")
