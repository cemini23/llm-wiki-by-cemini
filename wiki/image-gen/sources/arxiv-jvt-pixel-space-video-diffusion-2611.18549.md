---
title: "JVT: Just Video Transformer Makes Pixel-Space Video Diffusion Simple (2611.18549)"
type: source
maturity: draft
related:
  - concepts/pixel-space-video-diffusion.md
  - sources/arxiv-rediverse-diversity-collapse-2611.18550.md
updated: 2026-11-16
read_status: read
---
## Raw Concept

- **Title:** JVT: Just Video Transformer Makes Pixel-Space Video Diffusion Simple
- **Authors:** Jianjun Zhou, Hua Geng, Haoyu Guo (Zhejiang University, Shanghai AI Laboratory)
- **Type:** arXiv preprint, cs.CV
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.18549-jvt-just-video-transformer-makes-pixel-space-vid.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18549
- **Read status:** full — 23 pages extracted 2026-11-16

## Narrative

Pixel-space video diffusion has usually needed help: a pretrained autoencoder, auxiliary detailers, cascaded stages, or U-Net skips. JVT drops all of them and uses a plain large-patch DiT-style transformer.

The engineering contribution is a systematic ablation of three choices — video patch embedding, register tokens, and adaptive layer normalisation — to find a quality/cost balance. The resulting model is competitive with latent-diffusion baselines in both class-conditioned and unconditional settings.

The more interesting property is structural: because generation happens in pixel space, aligned modalities can be produced jointly. The demo is camera-conditioned RGB-disparity generation, which improves camera following over RGB-only baselines and yields explicit scene geometry without a separate reconstruction model at inference.

[Source: arxiv-2611.18549-jvt-just-video-transformer-makes-pixel-space-vid.pdf]

## Snippets

> "without a pretrained autoencoder, auxiliary detailers, cascaded stages, or U-Net-style skip connections."

## Dead Ends

- **Full-read note (2026-11-16):** Camera-conditioned generators follow rotations reliably but reproduce translations less accurately. FVD is computed at 2048 samples while several baselines use 10000, so cross-paper FVD is not directly comparable. [Source: arxiv-jvt-pixel-space-video-diffusion-2611.18549.md full text, 23pp]
