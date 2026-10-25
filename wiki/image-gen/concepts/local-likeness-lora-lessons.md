---
title: Local likeness LoRA — end-to-end lessons (2026-10)
type: concept
tags: [lora, likeness, sdxl, draw-things, runpod, kohya, dataset, failure-modes, apple-silicon, tos]
keywords: [likeness LoRA, character LoRA, SDXL, Lustify V9, draw-things-cli, kohya sd-scripts, rank, text encoder, trigger token, bucket, RunPod, ToS, M4 Air, 16 GB]
related:
  - runbooks/mac-local-image-director.md
  - concepts/de-censoring-techniques.md
  - concepts/censorship-tier-taxonomy.md
  - concepts/lora-taxonomy.md
  - concepts/reference-plus-lora-stacking.md
  - concepts/persona-legal-landscape.md
  - entities/models/sdxl-fine-tunes.md
  - entities/models/pony-v6.md
  - entities/models/z-image-turbo.md
  - entities/hardware/gpu-guide.md
  - entities/training-tools/kohya-sd-scripts.md
  - runbooks/runpod-unified-gen-stack.md
maturity: draft
created: 2026-10-24
updated: 2026-10-24
---

## Raw Concept

Lessons from one complete attempt, 2026-10-24: train a photoreal likeness LoRA of the operator from 7 personal
photos, on a rented RunPod 4090, and generate locally on a 16 GB M4 MacBook Air with no external drive.

The pipeline was built end to end and produced usable photoreal output. **The likeness failed.** This page records
what worked, what failed, and what to change next time. Operating detail lives in
@runbooks/mac-local-image-director.md.

## Narrative

### What the attempt cost

| Item | Value |
|---|---|
| GPU | RTX 4090 24 GB, SECURE, EUR-IS-2 |
| Rate | $0.89/hr, about 1.5 hr |
| Total spend | **~$1.35** |
| Local disk after cleanup | 17 GB free |
| Training time | 14 min, 1000 steps, 1.17 it/s |
| Local generation | 90-110 s per 1024 px image on M4 Air |

The economics were never the problem. The likeness quality was.

### The decision that mattered most: where to run

Three constraints interact, and ignoring any one of them wastes the week:

1. **ToS.** RunPod's terms ban "pornography or graphic adult content" and cover stored content, not just
   published. Private testing does not exempt you. Vast.ai bans only "obscene" and leaves a narrower but
   undefined gap. A rented GPU is therefore the wrong place for explicit *output*.
2. **Hardware.** A 16 GB M4 Air runs SDXL fine and cannot run Wan video at all; video is CUDA-native.
3. **Training.** Training needs the pixels. No scheme lets a remote GPU learn from images it never receives.

That produces one workable split: **train and store nothing sensitive on the cloud; generate locally.** Photos of
a clothed person are not the content the ban targets, so a short-lived pod for training is defensible. Generated
explicit imagery on a rented disk is not.

### Dataset was the failure point

Six usable images, of which four were full body. In a 1024 px frame a face in a full-body shot is roughly
80x100 pixels. Two frames carried usable facial detail. The LoRA learned **body proportions and outfits** and
almost no identity.

The diagnostic that proves it: render the same prompt and seed from two different training checkpoints. If both
outputs show the same face, and that face is not the subject, the LoRA is not carrying identity — the base model
is deciding. That test takes two minutes and saves a retrain.

**Rule:** a likeness LoRA needs face-dominant frames. Eight to ten portraits where the face fills a good share of
the frame, plus four to six full body for build. Six casual photos cannot work regardless of settings.

### Training parameters that produced a body-accurate, face-poor LoRA

```
rank 16 / alpha 8, LR 5e-5 UNet-only, 1000 steps, 1024 with buckets 640-1536,
AdamW8bit, fp16, gradient_checkpointing, cache_latents, sdpa, seed 42
```

Result: 9.2 GB VRAM, 14 min on a 4090, loss 0.167 → 0.127. Stable, no OOM, no divergence.

**These settings are fine for what they produced.** They were wrong for identity because the dataset was wrong,
not because the numbers were. For the retrain, raise rank to 32, train the text encoder at 1e-5, and pin the
trigger with `--keep_tokens=1`.

### The trigger word is not cosmetic

`mysubject` tokenises into several subword pieces. Binding a multi-piece string to one face is harder than
binding a single rare token the tokenizer has never split. Use something like `zkxpersona`. This is a real lever,
not a stylistic choice.

### Three environment traps that cost hours

1. **`models import` accepts checkpoints only.** Handing it a LoRA returns `Error: tensorNotFound`. A LoRA is
   never imported — copy the file into the models directory and reference it in `--config-json` with
   `loras[].version` (`sdxlBase` for SDXL).
2. **sd-scripts silently ignores concept folders without a repeat prefix.** The folder must be `N_name`
   (`10_mysubject`), or the loader reports "no data found" while the images sit right there.
3. **transformers 5.x broke sd-scripts.** `CLIPTextModel` moved and the import fails. Pin
   `transformers>=4.44,<4.50`, and pin `torch==2.5.1 torchvision==0.20.1` together — a mismatched pair throws
   `operator torchvision::nms does not exist`.

The full failure table is in @runbooks/mac-local-image-director.md.

### The GUI was never required

Draw Things publishes unsigned direct builds, and a separate `draw-things-cli` with headless inference. No Apple
account, no App Store, no GUI clicking. The CLI takes `--model --prompt --steps --cfg --seed --output` and
generates in about 90 s for 1024 px on an M4 Air.

This matters beyond convenience: a headless CLI is what makes the pipeline agent-drivable and reproducible at all.

### Checkpoint choice has a trap

Lustify's newest version (v10) is built on **Krea 2**, not SDXL — 11.9 GB and incompatible with both kohya's
SDXL trainer and Draw Things. V9 ZENITH (version 3045803) is the current SDXL build. Always read `baseModel` from
the API rather than taking the latest release:

```bash
curl -s "https://civitai.com/api/v1/models?query=Lustify&types=Checkpoint&limit=5&nsfw=true" \
  -H "Authorization: Bearer $TOKEN"
```

The `nsfw=true` flag is required; without it the API returns an empty list and looks broken.

### Storage is the hidden constraint on a small laptop

A 16 GB Air with 22 GB free cannot hold the full stack. Real numbers from this run:

| Item | Size |
|---|---|
| Draw Things app | 483 MB |
| draw-things-cli | 276 MB |
| SDXL checkpoint (f16) | 4.8 GB |
| CLIP bigG + ViT-L + VAE | 1.7 GB |
| LoRA | 163 MB |
| Source photos | under 1 MB |

Freeing space, in order of safety: `uv cache clean` (6.0 GiB here), npm cache, pip/bun caches, browser caches.
One process holding a uv lock blocked 6 GB until it was stopped.

### What would have made this easier

- **Face-dominant dataset.** The single highest-leverage change, and it costs only the time to take photos.
- **Text-encoder training.** UNet-only is cheaper but binds the trigger weakly.
- **A rare single-token trigger.**
- **A reference-image adapter** (IP-Adapter FaceID) as a cross-check before training: it needs one photo and shows
  roughly what identity signal is recoverable from the set.

### Where the field is heading

The reason this was hard is not the model — it is that SDXL is the only architecture this laptop can *train*.
Better photoreal engines already exist locally (Z-Image Turbo runs in 4 GiB) but cannot carry a trained likeness
until their LoRA tooling matures. When that changes, the whole pipeline simplifies: one competent engine, one
small LoRA, no fine-tune archaeology.

## Snippets

> "When the LoRA contributes little, the base checkpoint dominates and both variants converge." — the diagnostic
> that distinguishes a broken LoRA from a wrong strength, 2026-10-24.

> "Training needs the pixels. No scheme lets a remote GPU learn from images it never receives."

## Dead Ends

- **Raising LoRA strength to fix a wrong face.** At 1.0 on two checkpoints the faces were identical and not the
  subject. Strength cannot supply identity the training set never taught.
- **Face-centric adapter only, when full-body accuracy is the goal.** IP-Adapter FaceID conditions the face region;
  body shape and build still drift. It is a cross-check, not a substitute for a LoRA.
- **Using `models import` for a LoRA.** Wrong tool; returns `tensorNotFound`.
- **Downloading "the newest" CivitAI checkpoint.** v10 was a different architecture entirely.
- **Judging a LoRA by loss.** Loss fell cleanly 0.167 → 0.127 while identity failed. Judge by renders.
