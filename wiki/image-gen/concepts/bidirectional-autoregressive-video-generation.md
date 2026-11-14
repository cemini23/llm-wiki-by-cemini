---
title: Bidirectional autoregressive video generation (UniTemp)
type: concept
tags: [concept, video-generation, autoregressive, bidirectional, distillation, editing]
keywords: [UniTemp, anchor latents, backward generation, inbetween, causal VAE, any-direction AR]
related:
  - sources/arxiv-2606-18702-unitemp-bidirectional-video-generation.md
  - entities/models/unitemp.md
  - concepts/autoregressive-video-foresight-training.md
  - concepts/one-step-autoregressive-video-distillation.md
  - concepts/long-video-rag-retrieval.md
  - concepts/seam-stitching-strategies.md
  - entities/models/wan-2-2.md
  - sources/video-generation-survey-2026.md
  - sources/arxiv-2611.17336-pixvid-pixel-space-video.md
  - concepts/framewise-pixel-space-video-generation.md
maturity: draft
created: 2026-06-19
updated: 2026-11-14
---

## Relations

@sources/arxiv-2606-18702-unitemp-bidirectional-video-generation.md @entities/models/unitemp.md @concepts/seam-stitching-strategies.md @entities/models/wan-2-2.md

## Raw Concept

Ingest 2026-06-19 from UniTemp (arXiv:2606.18702) — single AR student for forward/backward/inbetween video via anchor latents.

## Narrative

**Gap:** Forward-only AR (Self-Forcing, LongLive class) cannot extend backward or fill gaps between clips.

**Causal VAE trap:** Backward generation breaks at block boundaries because VAE latents expect past context that doesn't exist when rolling reverse.

**UniTemp pattern:**

```
Block N (backward)  →  co-denoise anchor latents proxying block N+1 past
Teacher distillation  →  one student, shared weights, RoPE temporal indices
Inference           →  KV cache + flexible past/future conditioning
```

**Persona workflows unlocked:** Prologue before existing clip, inbetween two persona shots, loopable B-roll, storyboard keyframe → connect.

**Related constraint (2026-11-14).** PixVid shows that temporal VAE compression sets a floor on interaction latency in any block-based AR model. A multi-frame latent means a control waits for the rest of its block. One-frame pixel tokens remove that wait. This does not change the backward/inbetween problem above, but it changes the block size an operator can choose. See @concepts/framewise-pixel-space-video-generation.md.

## Snippets

(See @sources/arxiv-2606-18702-unitemp-bidirectional-video-generation.md)

## Dead Ends

Requires official distillation release on operator's Wan checkpoint — not DIY without teacher weights.
