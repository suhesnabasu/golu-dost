# Kaggle (T4 x2 / 29 GB RAM): LTX-2.5 image-to-video WITH audio using the Unsloth GGUF distilled transformer
# (LTX-2.x Community License: free commercial use under $10M revenue). Text encoder loaded in 4-bit.
import subprocess, sys, os, time, json, traceback, glob
OUT = "/kaggle/working"; LOG = []
os.environ.setdefault("HF_HOME", "/tmp/hf")          # big files off /kaggle/working (20 GB cap)
def log(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.append(s)
    open(f"{OUT}/log.txt", "w").write("\n".join(LOG))
import torch
log("cuda:", torch.cuda.is_available(), [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())])
if not torch.cuda.is_available(): log("NO GPU"); raise SystemExit
t0 = time.time()
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "git+https://github.com/huggingface/diffusers",
                "-U", "transformers", "accelerate", "gguf", "bitsandbytes", "imageio", "imageio-ffmpeg", "av", "sentencepiece"], check=False)
log(f"pip done {time.time()-t0:.0f}s")
from huggingface_hub import hf_hub_download, list_repo_files
G = "unsloth/LTX-2.5-GGUF"
files = list_repo_files(G); log("gguf files:", [f for f in files if f.endswith(".gguf")])
pick = next((f for pat in ("distilled/LTX-2.5-distilled-UD-Q3_K_XL", "distilled/LTX-2.5-distilled-Q3_K_M", "UD-Q3_K_XL", "Q3_K_M")
             for f in files if pat in f and f.endswith(".gguf") and "distilled" in f), None) or \
       next((f for f in files if f.endswith(".gguf") and "distilled" in f and "Q3" in f), None)
log("pick:", pick)
gpath = hf_hub_download(G, pick); log(f"gguf downloaded {time.time()-t0:.0f}s", os.path.getsize(gpath) // 2**20, "MB")

from diffusers import ModularPipeline, GGUFQuantizationConfig
from diffusers.modular_pipelines import ComponentsManager
from diffusers.modular_pipelines.ltx2.guider import LTX2Guidance
from diffusers.pipelines.ltx2.utils import DEFAULT_NEGATIVE_PROMPT, DISTILLED_SIGMA_VALUES
from diffusers.utils import encode_video, load_image
import diffusers
MID = "Lightricks/LTX-2.5-Diffusers"
cm = ComponentsManager()
pipe = ModularPipeline.from_pretrained(MID, components_manager=cm)
log("expected components:", getattr(pipe, "component_names", None))
# transformer from GGUF (fp16 compute: T4 has no bf16)
tcls = None
for name in ("LTX2VideoTransformer3DModel", "LTX2Transformer3DModel", "LTX2VideoTransformerModel"):
    tcls = getattr(diffusers, name, None) or tcls
log("transformer class:", tcls)
tr = tcls.from_single_file(gpath, quantization_config=GGUFQuantizationConfig(compute_dtype=torch.float16),
                           config=MID, subfolder="transformer", torch_dtype=torch.float16)
log(f"transformer loaded {time.time()-t0:.0f}s")
# text encoder in 4-bit
from transformers import BitsAndBytesConfig, AutoModel
te = None
try:
    from transformers import AutoModelForCausalLM
    te_cls = json.load(open(hf_hub_download(MID, "text_encoder/config.json"))).get("architectures", ["?"])[0]
    log("text encoder arch:", te_cls)
    import transformers
    TE = getattr(transformers, te_cls, AutoModel)
    te = TE.from_pretrained(MID, subfolder="text_encoder", torch_dtype=torch.float16,
                            quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16), device_map={"": torch.cuda.device_count() - 1})
    log(f"text encoder 4-bit on GPU1 {time.time()-t0:.0f}s")
except Exception:
    log("TE 4bit failed\n" + traceback.format_exc()[-1500:])
names = [n for n in (getattr(pipe, "component_names", None) or []) if n not in ("transformer", "text_encoder", "prompt_enhancer", "processor")]
pipe.load_components(names=names, torch_dtype=torch.float16)
upd = {"transformer": tr}
if te is not None: upd["text_encoder"] = te
pipe.update_components(**upd, guider=LTX2Guidance(guidance_scale=1.0), audio_guider=LTX2Guidance(guidance_scale=1.0))
try:
    from diffusers.models.autoencoders.ltx2_diffusion_decoder import LTX2VideoVaeNeighborhoodNattenProcessor
    pipe.diffusion_decoder.set_attn_processor(LTX2VideoVaeNeighborhoodNattenProcessor())
except Exception as e: log("natten processor skipped:", e)
try: pipe.diffusion_decoder.enable_tiling()
except Exception as e: log("tiling skipped:", e)
cm.enable_auto_cpu_offload(memory_reserve_margin="6GB")
log(f"pipeline ready {time.time()-t0:.0f}s")
RAW = "https://raw.githubusercontent.com/suhesnabasu/golu-dost/main/kaggle_req/in/"
PROMPT = ("A frightened young Indian man sits on his bed at night holding a glowing phone. He slowly looks up toward the door, "
          "breathing heavily, his hands tremble. Rain patters on the window, a ceiling fan creaks. Cold blue light on his face. "
          "Graphic novel animation, subtle realistic motion. Sound: rain, fan creak, a soft knock on the door.")
for k in ("arjun_ai", "arjun_comic"):
    t = time.time()
    try:
        im = load_image(RAW + k + ".png")
        out = pipe(image=im, prompt=PROMPT, negative_prompt=DEFAULT_NEGATIVE_PROMPT, width=544, height=960, num_frames=97,
                   frame_rate=24.0, sigmas=DISTILLED_SIGMA_VALUES, generator=torch.Generator("cuda").manual_seed(7),
                   output_type="np", output=["videos", "audio"])
        encode_video(out["videos"][0], fps=24, output_path=f"{OUT}/ltx25_{k}.mp4", audio=out["audio"][0].float().cpu(),
                     audio_sample_rate=pipe.vocoder.config.output_sampling_rate)
        log(f"{k}: OK {time.time()-t:.0f}s")
    except Exception:
        log(f"{k}: FAILED {time.time()-t:.0f}s\n" + traceback.format_exc()[-2500:])
    torch.cuda.empty_cache()
log("DONE")
