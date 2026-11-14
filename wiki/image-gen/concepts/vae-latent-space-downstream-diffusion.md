---
title: VAE latent space design for downstream diffusion
type: concept
tags: [concept, vae, latent-diffusion, training, codec]
keywords: [VAE design, reconstruction vs generative quality, latent smoothness, factorized latent, downstream diffusion]
related:
  - sources/arxiv-2606-22959-vae-latent-sign-pose-diffusion.md
  - sources/video-generation-survey-2026.md
  - entities/models/ltx-2.md
  - entities/models/wan-2-2.md
  - sources/arxiv-2606-22959-vae-latent-sign-pose-diffusion.md
  - entities/models/videorae.md
  - sources/arxiv-2607-14088-videorae-vfm-representation-autoencoder.md
  - sources/arxiv-2608-13556-v-rae.md
  - sweeps/2026-07-16-daily.md
  - sources/arxiv-2610-10524-grace-latent-compression.md
  - sources/arxiv-2611.17336-pixvid-pixel-space-video.md
  - concepts/framewise-pixel-space-video-generation.md
maturity: draft
created: 2026-06-24
updated: 2026-11-14
---

## Relations

@sources/arxiv-2606-22959-vae-latent-sign-pose-diffusion.md @entities/models/ltx-2.md @entities/models/wan-2-2.md @entities/models/videorae.md @sources/arxiv-2607-14088-videorae-vfm-representation-autoencoder.md @sources/arxiv-2608-13556-v-rae.md @sources/arxiv-2610-10524-grace-latent-compression.md

## Raw Concept

Ingest 2026-06-24 from Fauré et al. (arXiv:2606.22959) — sign-language pose VAE study with transferable latent-diffusion lesson.

## Narrative

**Core lesson:** VAE selection by **reconstruction metrics alone** mis-ranks codecs for **downstream latent diffusion**. Latent-space structure (smoothness, factorization, region-weighted losses) can dominate generative quality.

### Design axes (from SignPoseVAE study)

| Axis | Tradeoff |
|------|----------|
| Shared vs factorized latent distribution | Factorization can hurt hand-detail generation despite good recon |
| Multi-objective reconstruction weights | Position vs velocity terms shift latent geometry |
| β-VAE KL weight | Regularization vs expressivity for diffusion training |

### Image/video gen parallel

Same pattern noted in image latent diffusion literature — SD/VAE and video tokenizers (LTX, Wan VAE) should be evaluated on **DiT sample quality**, not PSNR/SSIM alone. **VideoRAE** (arXiv:2607.14088) makes the same point empirically: V-JEPA 2 teacher beats VideoMAEv2 on generation gFVD despite weaker PSNR; claimed LTX-VAE drop-in at 2B T2V. → @entities/models/videorae.md

**V-RAE** (arXiv:2608.13556, folded into the same entity) hardens the thesis with a dedicated diagnostic: introduces **tFVD** (temporal-coherence FVD) that correlates more reliably with downstream generation quality than reconstruction metrics — and shows Wan-2.2-VAE-comparable-or-better future-video prediction from frozen-VFM latents. → @sources/arxiv-2608-13556-v-rae.md

### The limit of the design axis: remove the VAE (2026-11-14)

Every page above assumes the VAE is fixed and asks how to design it better. PixVid (arXiv:2611.17336) argues the opposite for one case. Compress video in space and time and three things break: resolution scaling, per-frame control alignment, and control latency.

The lift is cheap. Fit a linear pixel-to-latent map offline, fuse it into the pretrained patch embedding, calibrate the timestep, and fine-tune in pixel space with a convolutional detailer head. Wan2.1-14B converges in about 4,000 B200 GPU-hours.

**The revised lesson for this page:** evaluate a codec on downstream quality, but also ask whether temporal compression is needed at all. If the product needs per-frame conditions or sub-frame latency, the VAE is the wrong interface. See @concepts/framewise-pixel-space-video-generation.md.

### Build-track note

Peripheral source domain (sign language). Do not adopt SignPoseVAE repo for persona work — see Phase-0 NO-GO in `briefs/2026-06-24_phase-0-car-signposevae.md`.

## Snippets

> "Optimizing solely for reconstruction error does not necessarily yield the most suitable latent representations for generative modeling."

## Dead Ends

Skeletal sign-pose modality — not portable to RGB persona latents without re-derivation.
