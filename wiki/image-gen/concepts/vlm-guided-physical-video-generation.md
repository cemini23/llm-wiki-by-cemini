---
title: VLM-guided physical video generation (training-free)
type: concept
tags: [concept, video-generation, physics, vlm, training-free, inference-time]
keywords: [CausalMotion, keyframe guidance, trajectory guidance, VLM chain-of-thought, latent soft mask, PhyGenBench, training-free physics]
related:
  - sources/arxiv-2606-14317-causalmotion-physical-reasoning-video.md
  - entities/models/causalmotion.md
  - concepts/video-generation-physical-executability.md
  - entities/models/ltx-2.md
  - concepts/world-models-video-generation.md
  - sources/arxiv-proprio-physics-video-2605-28230.md
  - sources/video-generation-survey-2026.md
  - sources/arxiv-2611.17324-k2v-generative-keyframing.md
  - concepts/training-free-keyframe-latent-conditioning.md
  - entities/models/wan-2-2.md
maturity: draft
created: 2026-06-17
updated: 2026-11-14
---

## Relations

@sources/arxiv-2606-14317-causalmotion-physical-reasoning-video.md @entities/models/causalmotion.md @concepts/video-generation-physical-executability.md @entities/models/ltx-2.md

## Raw Concept

Ingest 2026-06-17 from CausalMotion (arXiv:2606.14317) — explicit VLM physical reasoning as inference-time guidance for frozen video diffusion.

## Narrative

**Design pattern:** Don't retrain the video model for physics — **structure the denoising path** with interpretable intermediates.

```
Text prompt
  → VLM: causal key states + captions
  → T2I keyframes per state
  → Grounding + physical state vectors → trajectories
  → Time-align keyframes to trajectory
  → Soft-mask latent injection during video diffusion
```

**When to use:** Dynamics-heavy prompts (melting, deflation, pouring, collisions) where pure diffusion skips intermediate states.

**When to skip:** Persona talking-head / static-scene I2V — overhead of VLM+SAM2+multi-keyframe pipeline exceeds benefit.

**Cluster:** Complements simulator-based physics (@sources/arxiv-proprio-physics-video-2605-28230.md best-of-N) and executability benchmarks (@concepts/video-generation-physical-executability.md) — CausalMotion is **zero-training inference glue**.

### Second member: K2V (2026-11-14)

K2V (arXiv:2611.17324) uses the same principle with a different division of labour. A VLM planner predicts the physically important states as **keyframes**. An image edit model renders them. Wan2.2 interpolates, unmodified.

| | CausalMotion | K2V |
|---|---|---|
| Physical reasoning | VLM chain-of-thought | VLM planning agent with tools |
| Intermediate | Keyframes plus explicit trajectories | Keyframe stack plus expanded caption |
| Injection | Soft-mask latent injection | Keyframes written into the first-frame conditioning channel |
| Video model | LTX-Video | Wan2.2 I2V-A14B and TI2V-5B |
| Training | None | None |
| Key benchmark | PhyGenBench | Physics-IQ Verified 32.2 → 55.0; PhyGenBench 0.56 → 0.63 |

K2V reports roughly $0.47–0.59 per video, mostly planning cost. See @concepts/training-free-keyframe-latent-conditioning.md for the transport mechanism.

**Updated guidance.** This is now the best-evidenced training-free physics lever in the wiki. The cost per clip still rules it out for real-time persona work. Use it for batch clips where physical interaction is the subject.

## Snippets

(See @sources/arxiv-2606-14317-causalmotion-physical-reasoning-video.md)

## Dead Ends

Backbone-specific latent guidance implementation — porting from LTX-Video to Wan requires engineering, not paper recipe alone.
