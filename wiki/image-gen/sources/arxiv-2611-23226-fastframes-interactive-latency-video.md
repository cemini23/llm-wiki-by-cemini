---
title: "FastFrames: video generation at interactive latency (arXiv:2611.23226)"
type: source
related:
  - concepts/interactive-latency-autoregressive-video.md
  - concepts/streaming-video-generation-serving.md
  - concepts/one-step-autoregressive-video-distillation.md
  - concepts/budget-aware-diffusion-caching.md
  - entities/models/wan-2-2.md
  - concepts/cascaded-streaming-high-resolution-video.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FastFrames: Video Generation at Interactive Latency |
| Authors | Gene Chou (Apple, Cornell), Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan R. Richter, Vladlen Koltun (Apple) |
| Type | arXiv preprint, cs.CV |
| arXiv | 2611.23226v1, 17 Nov 2026 |
| Location | `research to be indexed/image-gen/arxiv-2611.23226-fastframes-video-generation-at-interactive-laten.pdf` |
| URL | https://arxiv.org/abs/2611.23226 |
| Project page | https://apple-aiml-research.github.io/ml-fastframes/ |
| Retrieved | 2026-11-22 |
| Pages | 19 |
| Read status | read |
| Domain fit | **On-topic.** Autoregressive video diffusion, inference latency, open-weight Wan 2.1 backbone. |

## Narrative

### The argument

Fast autoregressive video models report speed as frames per second. FPS hides the wait. A model that renders 30 frames as one batch in one second scores 30 FPS, but the user still waits one second for the first response. FastFrames measures **end-to-end per-frame latency**: the delay from a new input signal to the first RGB frame that shows its effect. It reports the reciprocal as **responses per second** (RPS).

The target is 50 ms per frame, or 20 RPS. Human-factors studies place the delay-detection threshold near 50 to 60 ms. The authors state that no prior model meets this target `[TENTATIVE]` — single paper, but the baseline table supports it.

### Diagnosis

The authors profile a 1.3B autoregressive model. Diffusion sampling takes only about 30% of wall time. The rest goes to operations treated as fixed details:

- VAE decoding takes 147 ms, or as long as 3.5 DiT passes.
- The KV-cache write needs one extra DiT pass on the clean latent, about 83 ms.
- DiT evaluation itself costs about 41.6 ms at the full 32,760-token cache.

The baseline pipeline needs 271.8 ms per frame. The authors keep the DiT and replace the "accessories".

### Three changes

**1. Pixel decoder instead of the VAE.** Three causal 3D ConvNeXt blocks read the low-resolution token grid (21×30×52). One linear layer turns each token into a 4×16×16 RGB patch. The head has 63.9M parameters against the VAE's 73.3M, and runs in 1 ms against 147 ms. Training uses five reconstruction terms against the frozen VAE output, then a relativistic adversarial loss with a frozen DINOv3 ViT-S/16 discriminator. The head is model-specific: it must be refit for each checkpoint.

**2. KV-refinement network.** The baselines run a full DiT pass on the clean latent to repair noisy cache entries. FastFrames replaces it with a small network: the frozen patch embedding, four trainable transformer blocks, and per-layer repair heads that predict residual corrections. It takes about 2 ms (1.3B) and 6 ms (14B), against 20× and 12× slower DiT refinement. Removing refinement without a replacement degrades quality.

**3. Systems work.** Persistent KV buffers, precomputed RoPE tables, fused QKV projection, segmented KV attention with a softmax merge (13% saving at five segments), and CUDA graphs. DiT evaluation drops from 41.6 to 16.4 ms for the 1.3B model. Context parallelism across 8× B200 takes it to 5.8 ms.

### Results

| Model | Params | Latency | RPS | VBench total |
|-------|--------|---------|-----|--------------|
| FastFrames-S, 1 GPU | 1.3B | 36 ms | 27.8 | 84.23 |
| FastFrames-S, 8 GPU | 1.3B | 14 ms | 71.4 | 84.23 |
| FastFrames-L, 8 GPU | 14.3B | 45 ms | 22.2 | 84.44 |
| FastFrames-L, 1 GPU | 14.3B | 158 ms | 6.33 | 84.44 |
| Causal Forcing++ (baseline) | 1.3B | 272 ms | 3.68 | 84.11 |
| Krea-Realtime (baseline) | 14.3B | 1,675 ms | 0.60 | 84.42 |

FastFrames-S matches the quality of a baseline that is 7.6× slower. FastFrames-L is about 10× faster than Krea-Realtime with similar VBench. The higher quality over the shared Causal Forcing++ weights comes from end-to-end adversarial training in pixel space.

### Transfer to control models

The method moves to off-the-shelf control models:

| Model | Official latency | FastFrames latency | Speedup |
|-------|------------------|--------------------|---------|
| LingBot 1.3B (camera) | 842 ms, 2 GPU | 52 ms, 8 GPU | 16× |
| RealWonder 1.3B (physics) | 1,141 ms, 1 GPU | 51 ms, 8 GPU | 22× |
| LingBot 14B (camera) | 1,373 ms, 8 GPU | 233 ms, 8 GPU | 5.9× |

These models stay slower than the T2V models. They need more sampling steps, more latent frames per step, and extra DiT work for conditioning.

### Workspace relevance

Interactive latency changes what a persona pipeline can do. At 36 ms per frame on one B200, camera and physics controls respond in real time. The paper claims code and weights on the project page `[NEEDS VERIFICATION 2026-11-22]`. Weights are stated, not yet confirmed by download.

Money point: the cheap wins are not new sampling methods. They are the VAE decoder and the KV-cache write. Any local autoregressive video stack can try the pixel-head and KV-repair replacements first.

## Snippets

> "Our 1.3B variant runs at 36 ms per frame, or 28 responses per second (RPS), on a single B200 GPU." [Source: arxiv-2611.23226 p.1]

> "Operations often treated as fixed implementation details, such as VAE decoding and KV cache updates, in fact account for over half of end-to-end inference latency." [Source: arxiv-2611.23226 p.1]

> "Our pixel decoder must be finetuned for each individual model." [Source: arxiv-2611.23226 p.6]

## Dead Ends

A single linear layer as the pixel decoder gives blurry but recognizable output. The authors had to add the ConvNeXt blocks to recover thin detail.

Finetuning the DiT with a low learning rate during adversarial training was unstable. They froze the DiT.
