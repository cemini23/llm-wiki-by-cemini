---
title: Interactive latency for autoregressive video models
type: concept
related:
  - sources/arxiv-2611-23226-fastframes-interactive-latency-video.md
  - concepts/streaming-video-generation-serving.md
  - concepts/one-step-autoregressive-video-distillation.md
  - concepts/budget-aware-diffusion-caching.md
  - concepts/cascaded-streaming-high-resolution-video.md
  - entities/models/wan-2-2.md
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Question this page answers: what does it take for a video model to answer an input in real time, and which parts of the inference path cost the most?

From arXiv 2611.23226 (FastFrames, Apple).

## Narrative

### Latency is not FPS

Frames per second amortises generation over a batch. If a model renders 30 frames in one second, it scores 30 FPS, but the user still waits one second. Interactive use needs **input-to-response latency**: the time from a control signal to the first frame that shows its effect. The reciprocal is **responses per second** (RPS).

The human delay-detection threshold is about 50 to 60 ms. So the practical target is 50 ms per frame, or 20 RPS.

### Where the time goes

On a 1.3B autoregressive video model at 480p, diffusion sampling is only about 30% of the 271.8 ms frame time. The rest sits in operations usually treated as fixed:

| Stage | Cost | Share |
|-------|------|-------|
| VAE decode | 147 ms | over half |
| KV-cache write (one extra DiT pass) | about 83 ms | about one third |
| DiT evaluation | 41.6 ms | remainder |

Few-step distillation shortens diffusion sampling. It does not touch these two stages. That is why a model can be "fast" in FPS and still slow to respond.

### Three levers

**Replace the VAE decoder with a pixel readout.** The DiT already produces rich low-resolution features. Three causal 3D ConvNeXt blocks read the token grid, and one linear layer unpatchifies each token into an RGB patch. The head has about the same parameter count as the VAE but runs about 147× faster. It must be refit per checkpoint, because it is tied to one model's feature space.

**Replace the KV-refinement pass with a small network.** The baselines spend a full DiT pass on the clean latent to repair noisy cache entries. A frozen patch embedding plus four trainable blocks plus per-layer repair heads predicts the correction. This costs about 2 ms instead of about 40 ms.

**Systems work.** Persistent KV buffers, precomputed RoPE tables, fused QKV, segmented KV attention with a softmax merge, and CUDA graphs. Context parallelism across 8 GPUs gives the final cut.

### The cost ladder on Wan 2.1

| Configuration | Latency | Speedup |
|---------------|---------|---------|
| Baseline autoregressive, 1 GPU | 272 ms | 1× |
| Pixel head plus KV repair plus systems, 1 GPU | 36 ms | 7.6× |
| Same, 8 GPUs | 14 ms | 19× |
| 14B model, 8 GPUs | 45 ms | — |

Quality holds: VBench total is 84.23 for the 1.3B and 84.44 for the 14B, against 84.11 and 84.42 for the matching baselines.

### Rule for a local stack

Order the work by measured share, not by the headline method. In an autoregressive video pipeline, profile the VAE decode and the KV write before changing the sampler. If those two stages take over half the frame time, a better sampler buys little.

### Limits

- The pixel head is model-specific. Each checkpoint needs its own head and its own adversarial training run.
- The gains are measured on Blackwell (B200) hardware. Older cards will show different shares.
- The transfer to control models is partial. LingBot 1.3B reaches 52 ms on 8 GPUs, not 36 ms, because control models need more steps and more conditioning compute.

## Snippets

> "FPS alone does not establish whether a model can respond to user inputs in real time." [Source: arxiv-2611.23226 p.1]

> "A single VAE decoding step takes as long as 3.5 DiT passes." [Source: arxiv-2611.23226 p.2]
