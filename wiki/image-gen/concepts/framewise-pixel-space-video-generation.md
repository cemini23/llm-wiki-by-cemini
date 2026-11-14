---
title: Frame-wise pixel-space video generation — lift the latent model, drop the VAE
type: concept
tags: [concept, video-generation, pixel-space, vae-free, high-resolution, latency, editing]
keywords: [PixVid, detailer head, x-prediction, noise shift, Euler sampler, patch embedding init, per-frame tokens, control-to-screen latency]
related:
  - sources/arxiv-2611.17336-pixvid-pixel-space-video.md
  - concepts/vae-latent-space-downstream-diffusion.md
  - concepts/cascaded-streaming-high-resolution-video.md
  - concepts/streaming-video-generation-serving.md
  - concepts/bidirectional-autoregressive-video-generation.md
  - entities/models/wan-2-2.md
updated: 2026-11-14
---

## Raw Concept

**The question this page answers:** can a pretrained latent video model generate in pixel space without a from-scratch train, and what changes when it does?

Source: PixVid (arXiv:2611.17336, Roblox and academic co-authors), ingested 2026-11-14.

## Narrative

### The lift recipe

Keep the diffusion transformer. Remove the VAE on both sides.

| Stage | Latent model | Pixel model |
|-------|--------------|-------------|
| Input | VAE encoder | Linear patch embedding, initialized from a fitted pixel-to-latent map |
| Backbone | DiT | Same DiT, inherited weights |
| Output | Linear head plus VAE decoder | Causal convolutional **detailer head** predicting clean video |
| Token scope | Several frames per latent | Exactly one frame per token (`1 × p × p` patch) |

**Initialization is the trick that makes the lift cheap.** Fit a linear map `A` offline between pixel patches and their latents. Fuse `A` with the pretrained patch embedding. Add a timestep calibration scale `c` so the signal-to-noise ratio in pixel space matches what the DiT saw in latent space. The DiT then starts training from close to its pretrained distribution.

**Training.** End-to-end in pixel space, from the latent checkpoint. 1.3M clips, about 4,000 B200 GPU-hours, versus a from-scratch video train.

### Four design choices, each with a measured effect

| Choice | Why | Measured |
|--------|-----|----------|
| Convolutional detailer head | Kernels cross patch borders, so neighbouring tokens agree at seams | seams 118.6 → 13.3 |
| x-prediction, not v-prediction | v-prediction must reproduce full-rank per-pixel noise, which grows with patch size | pixel noise 62.25 → 0.78 |
| Larger noise shift | Pixel data is more redundant, so it keeps more signal at the same noise level | peak at s = 15 |
| Euler sampler, not UniPC | Higher-order samplers drain colour in a bf16 pixel state | chroma kept 91% → 101% |

The x-prediction result is the important general lesson. Under flow matching, a network that predicts velocity must model the noise in its input. A network that predicts clean data must not. The gap widens as patch size grows.

### What per-frame tokens buy

1. **Resolution without token growth.** Double the patch size and add one detailer up-block. Token grid is unchanged, so 960×1664 costs nearly the same as 480×832.
2. **Frame-aligned control.** Each condition is tokenized per frame, so a depth map aligns with the frame it belongs to. Fast motion no longer blurs or deforms.
3. **One-frame latency.** With one frame per block, a control applies at the next frame. A latent model with four-frame latents waits at least three frames. This is a structural barrier, not an optimization problem.

### Costs

- Pixel models process more tokens per second of video. PixVid needs 3.9× the token rate of Wan2.1 at 480×832.
- Short low-resolution clips therefore cost more than a latent baseline. The gap closes at higher resolution.
- Throughput drops after distillation (29.4 vs 72.0 fps) but stays above real time.

### Relationship to the rest of the wiki

This is the reverse of the usual direction of travel. Most wiki pages accept the VAE as fixed and work inside the latent. See @concepts/vae-latent-space-downstream-diffusion.md for latent-design work. PixVid argues the VAE is an interface that can be replaced when it blocks resolution, control alignment, or latency.

For the high-resolution goal by a different route, see @concepts/cascaded-streaming-high-resolution-video.md (super-resolution cascade). For the serving side of latency, see @concepts/streaming-video-generation-serving.md.

## Snippets

> "Since the high-level semantic content of a video changes little with resolution, higher resolution should mainly require finer rendering, not more tokens." [Source: arxiv-2611.17336 p.4]

> "Predicting v would instead require the network to model the full-rank per-pixel noise in x_sigma, a burden that increases with patch size." [Source: arxiv-2611.17336 p.3]
