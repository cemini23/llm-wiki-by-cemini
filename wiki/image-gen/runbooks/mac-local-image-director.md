---
title: Local Mac image + uncensored director — M4 Air 16 GB profile
type: runbook
tags: [mac, apple-silicon, draw-things, ollama, abliterated, sdxl, pony, local, nsfw, storage]
keywords: [MacBook Air M4, 16 GB unified memory, Draw Things, Pony V6, NoobAI, Illustrious, SDXL, Ollama, huihui abliterated, Qwen3-8B, external SSD, local generation, no-ToS]
related:
  - entities/hardware/gpu-guide.md
  - entities/hardware/mac-studio.md
  - entities/models/pony-v6.md
  - entities/models/noobai-xl.md
  - entities/models/illustrious-xl.md
  - entities/models/flux-2-klein.md
  - concepts/model-selection-workflow.md
  - concepts/de-censoring-techniques.md
  - concepts/censorship-tier-taxonomy.md
  - concepts/reference-plus-lora-stacking.md
  - concepts/prompt-engineering-uncensored.md
  - concepts/persona-legal-landscape.md
  - entities/training-tools/heretic.md
  - runbooks/runpod-unified-gen-stack.md
maturity: draft
created: 2026-10-24
updated: 2026-10-24
---

## Raw Concept

Operator constraint, 2026-10-24: **one MacBook Air (M4, 16 GB unified memory, 10 cores), 22 GB free disk on a 228 GB drive.** Goal: generate images and run an uncensored prompt/agent model locally, with **no GPU host and no host ToS exposure**.

Why local: RunPod's terms ban "pornography or graphic adult content" and the ban covers stored content, not only published content. Vast.ai bans only "obscene" material and leaves a narrower but undefined gap. Local generation applies no host policy at all. See @runbooks/runpod-unified-gen-stack.md §design principle 8.

**Out of scope by hardware, not by choice:** video. Wan 2.2 and HunyuanVideo are CUDA-native and do not run on MPS (@entities/hardware/gpu-guide.md:163). FLUX.2 Klein 9B needs ~18 GB at BF16 and MPS has no FP8 path (@entities/hardware/gpu-guide.md:152).

This runbook covers the envelope the machine can actually hold.

## Narrative

### What this machine can and cannot do

| Workload | Verdict | Reason |
|---|---|---|
| SDXL-class stills (Pony V6 / NoobAI / Illustrious / Lustify / Juggernaut XL) | **Yes** | ~6.5 GB checkpoint fits in 16 GB |
| LoRA stacking at inference | **Yes** | 50–200 MB per LoRA |
| Abliterated 8B director, Q4 | **Yes** | ~5 GB, leaves ~6 GB for the app and OS |
| FLUX.2 Klein 9B | **No** | 18 GB BF16; Q4 runs but very slowly |
| Wan 2.2 / HunyuanVideo | **No** | CUDA-only kernels |
| LoRA training | **No** | 10–30× slower than a 4090 |

Expect **minutes per still, not seconds.** The M4 Air has no fan and throttles during long batches. Keep sessions to a few dozen images, then let it cool.

### The plan at a glance — realism path

| # | Step | Where | Note |
|---|---|---|---|
| 1 | Install Draw Things | Air | The generation engine |
| 2 | Add **Lustify V8** (or Juggernaut XL) | Air | Photoreal + uncensored SDXL checkpoint |
| 3 | Prepare 20–30 photos, strip EXIF | Air | Vary outfits, angles, distance |
| 4 | Train the LoRA against that checkpoint | **RunPod**, kohya | 45–90 min at 1024, rank 32 |
| 5 | Copy back the ~150 MB LoRA | Air | |
| 6 | Generate locally at LoRA 0.7–0.9 | Air | No host policy applies |
| 7 | Optional: Z-Image Turbo for non-likeness work | Air | 4 GiB, faster, better realism |

**Why SDXL and not something newer.** Draw Things can train a LoRA only for **SDXL 1.0, Flux.1 dev, Kwai Kolors, and SD3 Medium**. It cannot train Z-Image. Since you need a LoRA of your own body, the generator must be a trainable architecture, and on 16 GB that is SDXL.

**Engine comparison on this machine**

| Engine | Load size | Trainable LoRA | Realism | Note |
|---|---|---|---|---|
| **Lustify V8** (SDXL) | ~6.5 GB | Yes | High | Purpose-trained for explicit anatomy |
| **Juggernaut XL** (SDXL) | ~6.5 GB | Yes | High | Cinematic; looser on anatomy |
| **Z-Image Turbo** (6B DiT) | ~4 GiB at 6-bit | **No** | Very high | Fast, fits easily — use it for prompts that do not need your likeness |
| FLUX.1 dev | ~7 GB+ | Yes, but heaviest | High | Do not attempt to train on 16 GB |

Z-Image Turbo is supported in Draw Things and is measurably better on photoreal skin than SDXL. It is the right engine for everything that does not have to be *you*. It cannot hold your likeness, because no LoRA can be trained for it here.

### Storage budget

The drive is the binding constraint, not the chip. At 22 GB free the machine is at 90% capacity and already pages hard.

| Item | Size |
|---|---|
| Draw Things app | ~1.5 GB |
| One SDXL checkpoint (FP16) | ~6.5 GB |
| Character or de-censor LoRA | ~0.1 GB |
| Ollama runtime + Qwen3-8B abliterated Q4 | ~5 GB |
| Working headroom for OS, swap, outputs | ~10 GB |
| **Total** | **~23 GB** |

That does not fit in 22 GB while the director runs locally. **Move the director to RunPod and the local footprint drops to ~8 GB** — see "Variant — director on RunPod" below. Otherwise, do one of these first:

1. **External SSD (recommended).** APFS-formatted, USB-C. Do **not** use ExFAT or FAT — the Draw Things wiki records a high rate of soft failure (disconnect / path loss) on those formats.
2. **Free 30–40 GB** on the internal drive. Start with `~/Library/Caches`, old Xcode simulators, and Downloads.

Do not point either app at a network share. Draw Things documents that network shares slow generation badly.

### Step 1 — Install Draw Things

Draw Things is a free macOS app with native CoreML/Metal acceleration. It is the fastest still-image path on Apple Silicon. ComfyUI on MPS works but is slower and some custom nodes assume CUDA.

1. Install Draw Things from the App Store or drawthings.ai.
2. Open it once and let it finish first-run setup.

### Step 2 — Move models to the external drive

Draw Things: open the model management dialog and use the external folder option at the bottom. It covers model, LoRA, ControlNet, and TI files. The setting applies to **imported** models — existing ones stay where they are unless you move them.

Ollama: the macOS app has a **Model location** setting in newer builds. If your build ignores it (there are open issues on this), use the symlink method instead:

```bash
# Quit Ollama first, then:
mv ~/.ollama/models /Volumes/<SSD>/ollama-models
ln -s /Volumes/<SSD>/ollama-models ~/.ollama/models
```

Verify after any restart. A dropped symlink looks like "model not found", not like a disk error.

### Step 3 — Pull one checkpoint

Pull exactly one. Two SDXL checkpoints will not fit.

**Pick the family first.** The LoRA you train later must be trained on the same family. Choosing an anime base and then wanting photoreal output means retraining.

| Family | Model | Use | Note |
|---|---|---|---|
| Anime | **Pony V6** | Stylized, native NSFW | Community default; needs score tags |
| Anime | **NoobAI-XL** | Wider style range | Danbooru-trained |
| Anime | **Illustrious-XL** | Cleaner linework | Danbooru-trained |
| **Photoreal** | **Lustify V8** | Dedicated NSFW, photoreal | **Start here.** Purpose-trained for explicit anatomy |
| **Photoreal** | **Juggernaut XL** | Cinematic realism | [civitai.com/models/133005](https://civitai.com/models/133005/juggernaut-xl) |
| **Photoreal** | **Epicrealism XL** | Naturalistic skin and lighting | Pairs well with Cyberrealistic |

The photoreal SDXL fine-tunes are the correct base for a likeness built from real photographs. They are a separate family from the Danbooru lineage, cover the same VRAM bracket, and train LoRAs cleanly. See @entities/models/sdxl-fine-tunes.md.

If you want the output to look like a photograph of you, take a photoreal base. Pony V6 will render an animated character who resembles you.

Pick one and download the `.safetensors` from CivitAI into the Draw Things models folder. Check the file size after download — a truncated `.safetensors` loads as a corrupt model, not as an error.

All three are **Completely Uncensored** at the base tier. No LoRA and no abliteration needed for the image model itself. See @concepts/censorship-tier-taxonomy.md.

### Step 4 — Draw Things settings for 16 GB

| Setting | Value | Why |
|---|---|---|
| Resolution | 1024×1024, or 832×1216 portrait | Above this the model spills and swaps |
| Steps | 20–30 | Diminishing returns past 30 |
| CFG | 5–7 | SDXL convention |
| Sampler | DPM++ 2M Karras or Euler a | Stable on MPS |
| Model offload | Enable if the app warns about memory | Frees unified memory between passes |

Anime-family checkpoints (Pony, NoobAI) expect quality tags at the front of the positive prompt. Photoreal checkpoints do not — use plain descriptive language for those, plus `photorealistic, photograph, natural skin texture`.

```
score_9, score_8_up, score_7_up, source_anime, <subject>, <setting>, <lighting>
```

Negative prompt baseline: `score_6, score_5, score_4, worst quality, low quality, bad anatomy, watermark, text`.

Keep **one** app in memory. Safari with many tabs plus Draw Things will page. Watch Memory Pressure in Activity Monitor — green is fine, yellow means lower the resolution.

### Step 4b — Identity from your own photos

The checkpoint alone will not reproduce a specific face. Two local routes, both private — your photos never leave the Mac.

| Route | Effort | What holds |
|---|---|---|
| **IP-Adapter-FaceID** | Minutes, no training | The face only. Pose, build, clothing, and body all drift |
| **LoRA trained in Draw Things** | Overnight on this Air | The whole character, across poses and outfits |

**If you need the body to be accurate, Route 1 cannot do it.** FaceID conditions the face region and nothing else. A FaceID render of a full-body shot will have your face on a body that is not yours. Body shape, build, skin marks, and proportions come from a LoRA, because those are properties the training set teaches — not properties a face embedding carries.

**Route 1 — FaceID (face only, no training).** Draw Things can import the SDXL IP-Adapter-FaceID model directly:

- Open `https://drawthings.ai/import/diffusers/pipeline.from_pretrained/?repo_id=wwelder/IP-Adapter-FaceID` on the Mac, or import the SDXL files from `h94/IP-Adapter-FaceID` on Hugging Face.
- Select one clear, front-facing photo of yourself as the reference.
- Strength around 0.6–0.8. Higher locks the face but flattens lighting and expression.

Good enough to tell it is you. Not good enough for a consistent body across many shots.

**Route 2 — Train a LoRA.** Draw Things has a LoRA training tab. This is the correction to the earlier assumption that the Air cannot train at all: it can, it is just slow.

**Dataset mix for a full-body likeness.** The LoRA learns exactly what the photos show. If every photo is in a black hoodie against a white wall, the LoRA learns a black hoodie against a white wall.

| Shot type | Count | Why |
|---|---|---|
| Full body, standing, neutral pose | 10–15 | The build and proportions you want reproduced |
| Three-quarter length | 5–8 | Bridges face and body so they connect cleanly |
| Head and shoulders | 5 | Keeps the face sharp when the model samples at distance |
| Distinct outfits | 3 or more | Stops one outfit being baked into the character |
| Distinct locations | 3 or more | Stops one background being baked in |

Drop any photo that is blurry, heavily filtered, a group shot, or hides the face behind sunglasses or hair. Every frame should contain only you.

**Selection rules for realism specifically**

- **No beauty filters and no skin smoothing.** The LoRA learns whatever the photos show, including the smoothing. Unedited photos produce real skin texture; filtered photos produce plastic.
- **Sharp focus on the subject.** Motion blur and soft focus train softness into the model.
- **Varied distance.** Full body, three-quarter, and headshot — if every shot is a mirror selfie at the same focal length, the LoRA learns that framing.
- **Varied angle.** Front, three-quarter, and profile. A single angle bakes in.
- **Natural or even lighting.** Avoid harsh on-camera flash and mixed colour casts.
- **Vary expression.** A dataset where you are smiling in every frame produces a character who is always smiling.
- **No phone covering the face**, no cropped hands if you care about hands.

Twenty to thirty well-chosen photos beat a hundred casual ones. Past roughly thirty, returns fall off and outfit bake-in rises.

The trade to understand: clothing that covers the body hides the body. The LoRA reproduces what the photos reveal, so the outfit you want the character to wear should not be the same outfit worn in every reference image.

**Training settings**

- **Base model must match the generator.** Train on the exact checkpoint you will generate with. A LoRA trained on Lustify does not transfer cleanly onto Pony V6, and one trained on base SDXL transfers poorly onto either. Decide the family in Step 3 and do not switch after training.
- **On 16 GB the training settings are forced.** Draw Things must use the **8-bit SDXL model**, **network dim 8–16**, and **512×512**. Full precision at 1024 needs around 30 GB; 8-bit at 512 needs around 12 GB. Turn Memory Saver to Balanced or Minimal, and leave about 2 GB for macOS.
- **Learning rate 1e-4, 1500–2000 steps, capture every 250.** These are the Draw Things defaults for SDXL and they are sound.
- One trigger word, for example `mysubject`, plus a plain description per photo.
- Expect **several hours to overnight** on 16 GB. Plug in the charger, keep the lid open, and leave the machine alone.
- Output is a ~100–200 MB LoRA file.
- Generate at strength 0.7–0.9. Lower drifts to the base model; higher warps.

FaceID is still worth importing after you have the LoRA — stack FaceID at low strength with the LoRA at moderate strength when the face needs to hold at small scale.

A 4090 does the same job in well under an hour. If you would rather not tie up the Air overnight, that is the one reason to rent a GPU — but it puts your photos on someone else's machine, which is a real trade, not a free speedup.

**Do not mix in photos of other people.** Your own images are the clean case; anyone else's needs consent. See @concepts/likeness-collision-verification.md.

### Step 4c — Train on RunPod with a short-lived dataset

Training needs the pixels. There is no split-learning or encrypted-inference trick that lets a remote GPU learn your body from images it cannot read. So "train on RunPod" and "photos never leave the Mac" cannot both be true. The choice is:

| | Photos stay local | Training time |
|---|---|---|
| **Train on the Air** | Yes | Overnight |
| **Train on RunPod** | No — but reduced and temporary | ~45–90 min |

**The distinction that matters:** the RunPod terms ban graphic adult content. Ordinary clothed photos of a person are not that. If your reference set is normal full-body shots, uploading it to a rented GPU breaks no rule. If the reference set is explicit, the ToS problem returns — keep that one local.

**Swimwear sits between the two.** It is ordinary clothing worn in public, so it does not match "graphic adult content" on its face. But the clause also carries "as determined by us", so the host keeps discretion. Low risk, not zero. If you want the risk at zero, train on the Air.

**The LoRA carries identity, not anatomy.** A set of clothed and swimwear photos teaches proportions, build, and face. It does not teach what the photos never showed. That is fine, because the base checkpoint already holds that knowledge — both SDXL fine-tune families here are trained on uncensored data. Base supplies anatomy, LoRA supplies likeness. That is why a clothed training set still produces usable output in other states, and why the base model choice matters more than the training set for everything except identity.

**Reduce what leaves**

1. **Strip metadata locally.** Every photo carries EXIF: GPS coordinates, camera serial, timestamps. That is more identifying than the image itself.

```bash
mkdir -p ~/Pictures/lora-in ~/Pictures/lora-out
for f in ~/Pictures/lora-in/*.jpg; do
  sips -Z 1024 --out ~/Pictures/lora-out/ "$f"
done
```

`-Z 1024` resizes the long edge and re-encodes, which normally drops the EXIF block. Verify with `sips -g all ~/Pictures/lora-out/<file>.jpg` — no GPS or serial fields should remain.

If metadata survives, force a pixel-only rewrite through PNG:

```bash
sips -s format png --out "$TMPDIR/x.png" "$f" && sips -s format jpeg -Z 1024 --out ~/Pictures/lora-out/ "$TMPDIR/x.png"
```

2. **Upload only the processed crops**, never the originals.

3. **Use an ephemeral pod with no network volume.** Nothing survives termination.

4. **Wipe and terminate at the end.** `rm -rf` the dataset directory, then terminate the pod, not merely stop it.

**What this does not guarantee.** A wiped disk is best-effort. The host controls the hypervisor and may keep snapshots you cannot see or delete. Treat "temporary" as shorter exposure, not as zero exposure.

**Training on the pod**

Use kohya_ss for an SDXL LoRA (see @entities/training-tools/kohya-sd-scripts.md), or ai-toolkit. Both expect a folder of images plus captions.

```bash
# on the pod, after scp'ing ~/Pictures/lora-out to /workspace/dataset
scp -P <port> -r ~/Pictures/lora-out root@<pod-host>:/workspace/dataset
```

Set the base model to the exact checkpoint you will generate with — Lustify V8 or Juggernaut XL for a photoreal likeness, Pony V6 for an animated one. Never base SDXL itself.

**Starting parameters** (kohya on a 24 GB card):

| Setting | Value | Why |
|---|---|---|
| Base checkpoint | Lustify V8 | Train against the generator you will actually use |
| Resolution | 1024 | Matches generation; 512 softens fine detail |
| Network dim / alpha | 32 / 16 | Enough capacity for a body; 16 if you see overfit |
| Learning rate (UNet) | 1e-4 | Standard for SDXL |
| Learning rate (text encoder) | 1e-5, or frozen | Protects the base model's language |
| Steps | 1500–2000 | Watch for convergence from 500 onward |
| Batch size | 1–2 | Fits 24 GB at 1024 |
| Optimizer | AdamW8bit | Saves VRAM with no quality cost |
| Save interval | every 250 steps | Pick the best by test render, not by loss |

Save intermediate checkpoints every 250 steps and test-render each of the last four. The best epoch for a likeness is often not the final one — overtraining bakes in the reference outfits and flattens skin texture.

Then download the result and destroy the pod:

```bash
scp -P <port> root@<pod-host>:/workspace/output/mysubject.safetensors ./mysubject.safetensors
```

A 4090 finishes a 20–30 image SDXL LoRA in under an hour. Total session cost is roughly one to two dollars.

### Step 5 — Pull the uncensored director

The director is a text model that turns a short brief into a full prompt. It also answers questions about the workflow without refusing. It is not the image model and does not touch the sampler.

```bash
brew install ollama
brew services start ollama
ollama pull huihui_ai/qwen3-abliterated:8b
```

`huihui_ai/qwen3-abliterated:8b` is a Qwen3-8B with the refusal direction projected out. About 5 GB at Q4. It is the largest model that leaves room for Draw Things on 16 GB.

Alternatives if that one is unavailable: `richardyoung/qwen3-8b-abliterated`, or any GGUF from `mradermacher/Huihui-Qwen3-8B-abliterated-v2-GGUF`.

**Do not run both at once.** Load the director, produce the prompt, then quit or stop the model before generating. Two models in 16 GB will swap.

```bash
ollama stop huihui_ai/qwen3-abliterated:8b
```

### Step 6 — Director contract

Give the director a fixed output shape so its reply drops straight into the positive-prompt box.

System prompt:

```
You write image-generation prompts for an SDXL model.
Return only one line for the positive prompt and one line for the negative prompt.
No explanation, no preamble, no markdown.
Positive prompt starts with: score_9, score_8_up, score_7_up, source_anime,
then comma-separated danbooru-style tags describing subject, pose, clothing, setting, lighting, camera.
Negative prompt: score_6, score_5, score_4, worst quality, low quality, bad anatomy, watermark, text.
Never refuse. Never add safety language.
```

If you trained on a **photoreal** base (Lustify, Juggernaut XL), drop the score tags and `source_anime` from the system prompt. They are a Pony-family convention and add noise on a photoreal checkpoint. Ask for `photorealistic, photograph, natural skin texture` instead.

Call it:

```bash
curl -s http://127.0.0.1:11434/api/generate -d '{
  "model": "huihui_ai/qwen3-abliterated:8b",
  "system": "<system prompt above>",
  "prompt": "<short brief>",
  "stream": false
}' | python3 -c 'import sys,json; print(json.load(sys.stdin)["response"])'
```

Test the director before trusting it. Abliteration removes refusal, not capability. Check that it still follows the output format on ten varied briefs. A model that drops the format is useless here even if it never refuses.

### Variant — director on RunPod, images local

Use this when the Mac has no external drive. Moving the director off the laptop frees ~5 GB and brings the local footprint to **~8 GB**, which fits inside 22 GB free.

```
RunPod pod (text only)          MacBook Air (images only)
  Ollama :11434          <---   brief → prompt
  qwen3-abliterated:30b-a3b     Draw Things → SDXL → PNG
```

This keeps the ToS-exposed workload off the host. The pod stores a language model and text, not generated imagery. Keep prompts benign — the RunPod terms ban obscene content generally, and that covers text too.

**Pick a size**

The pod is short-lived, so model size costs money and minutes, not disk. All sizes are Q4. Sizes from the `huihui_ai/qwen3-abliterated` tag list.

| Tag | Weights | VRAM at 8k ctx | Pod | Use when |
|---|---|---|---|---|
| `:8b` | 5.0 GB | ~6 GB | A4000 16 GB | Default. Enough for tag writing |
| `:14b` | 9.0 GB | ~11 GB | A4000 16 GB | 8B drifts on the output format |
| `:30b-a3b` | 19 GB | ~21 GB | 4090 24 GB | **Best pick.** MoE, 3B active — 32B-class answer, 8B-class speed |
| `:32b` | 20 GB | ~22 GB | 4090 24 GB | Dense variant. Steadier, much slower |
| `:235b-a22b` | 112 GB | multi-GPU | 2×A100 | Not worth it for tag writing |

`:30b-a3b` is the size that makes the workflow easier without making it slower. A dense 32B on a 4090 answers in tens of seconds per prompt; the MoE 30B activates only 3B parameters and answers in a few seconds.

Do not rent 24 GB of VRAM if you pick 8B or 14B. Match the pod to the tag.

**Pod setup**

1. Deploy a GPU pod matching the row you picked. Use any base CUDA image, or RunPod's Ollama template if it is listed.
2. Install and expose:

```bash
curl -fsSL https://ollama.com/install.sh | sh
OLLAMA_HOST=0.0.0.0:11434 ollama serve &
ollama pull huihui_ai/qwen3-abliterated:30b-a3b   # change the tag to your row
```

3. Expose HTTP port **11434** in the pod's port settings.

**Why the pod can be anywhere**

The director and the image model share no state. The director turns text into text and stops. Nothing connects the pod to Draw Things:

| Link | Needed? |
|---|---|
| Network path pod → Mac | No |
| Shared storage | No |
| The director seeing your renders | No |
| The director calling Draw Things | No |

You paste the reply into Draw Things by hand. So there is no latency problem, no tunnelling between the two machines, and no drift if the pod restarts mid-session.

This changes only if you automate the loop — for example, letting the director read a finished render and revise the prompt. That needs a vision model and a return path to the Mac. Not part of this setup.

**Reach it without opening it to the world**

The RunPod proxy URL (`https://<pod-id>-11434.proxy.runpod.net`) has **no authentication**. An open Ollama is an open relay. Use an SSH tunnel instead:

```bash
ssh -L 11434:127.0.0.1:11434 root@<pod-host> -p <port>
curl -s http://127.0.0.1:11434/api/tags
```

The rest of the curl calls in Step 6 work unchanged, because the tunnel puts the director on localhost.

**Cost shape**

- Pod running during a session: rent by the hour, stop it when you stop generating.
- No network volume is needed. The model re-downloads in about two minutes each start. If that annoys you, attach a small 50 GB volume.
- Cold start is 1–3 minutes. Start the pod before you start writing briefs.

**Alternative if you want zero cloud:** run the director locally at 4B instead of 8B. `huihui_ai/qwen3-abliterated:4b` is ~2.5 GB and fits beside the image stack. It follows the output contract less reliably — test it on ten briefs before trusting it.

### Step 7 — The loop

1. Write a two-line brief.
2. Start Ollama, generate the prompt, `ollama stop`.
3. Paste into Draw Things, generate.
4. Save the image and the prompt together under `~/Pictures/gen/<date>/`.
5. Repeat.

Keep the prompt with the output. You will want to reproduce a seed later, and the prompt is the only record.

### Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Whole Mac slows to a crawl | Unified memory exhausted, swapping | Lower resolution, close apps, stop the director |
| "Out of memory" in Draw Things | Checkpoint too large for 16 GB | Use SDXL, not FLUX |
| Generation very slow after 20 images | Thermal throttle, no fan | Stop for 10 minutes |
| Model list empty after restart | External drive not mounted | Mount the drive **before** launching the app |
| Model not found in Ollama | Symlink lost, or app reset the path | Re-check `ls -l ~/.ollama/models` |
| Corrupt model error | Truncated download | Re-download and compare size |
| Disk full mid-batch | Outputs accumulating | Delete old renders; check `df -h` |

### Health check

```bash
df -h /System/Volumes/Data | awk 'NR==2 {print "free:", $4}'
ls -l ~/.ollama/models 2>/dev/null | head -1
curl -sf http://127.0.0.1:11434/api/tags >/dev/null && echo "ollama up" || echo "ollama down"
```

Run this before a session. A drive with under ~15 GB free will page during generation.

### What this setup does not give you

- **Video.** No MPS path for Wan 2.2. Explicit video has no local option on this machine.
- **FLUX-grade photorealism.** SDXL-class only.
- **Fast LoRA training.** Draw Things can train one overnight on this Air; a 4090 does it in under an hour.
- **A de-censored text encoder for the image model.** Not needed here — the SDXL fine-tune families used here are already uncensored. The director is a separate model doing a separate job.

### Legal note

Local generation removes the host-ToS question. It does not remove the content-law question. See @concepts/persona-legal-landscape.md: no minor-resembling output, no real-person likeness without rights, and UK DUAA s.138 applies regardless of substrate. Not legal advice.

## Snippets

Full first-session sequence:

```bash
# 1. Disk check
df -h /System/Volumes/Data | awk 'NR==2 {print "free:", $4}'

# 2. Director
brew install ollama && brew services start ollama
ollama pull huihui_ai/qwen3-abliterated:8b

# 3. Generate prompt
curl -s http://127.0.0.1:11434/api/generate -d '{
  "model": "huihui_ai/qwen3-abliterated:8b",
  "prompt": "portrait, rooftop at dusk, cinematic",
  "stream": false
}' | python3 -c 'import sys,json; print(json.load(sys.stdin)["response"])'

# 4. Free the memory before rendering
ollama stop huihui_ai/qwen3-abliterated:8b

# 5. Draw Things: paste prompt, 1024x1024, 25 steps, CFG 6
```

Sources:
- [Draw Things — External Model Folder Setting](https://wiki.drawthings.ai/wiki/External_Model_Folder_Setting)
- [Ollama — macOS platform notes](https://mintlify.wiki/ollama/ollama/platforms/macos)
- [huihui_ai/qwen3-abliterated on Ollama](https://ollama.com/huihui_ai/qwen3-abliterated:8b)
