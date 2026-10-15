---
title: "K291 — image-gen wave (2026-10-14)"
type: concept
tags: [wave, k291, ingest, hub]
keywords: [K291, latent interface, video consistency, deepfake detection, diffusion theory, TTS personalization]
related:
  - sources/arxiv-instantfusion-shared-latent-interface-2610.13944-2026-10-14.md
  - sources/arxiv-gad-geometry-attention-distillation-2610.18779-2026-10-14.md
  - sources/arxiv-physics-aware-deepfake-detection-2610.18485-2026-10-14.md
  - sources/arxiv-finite-sample-conditional-diffusion-2610.13851-2026-10-14.md
  - sources/arxiv-on-policy-one-shot-tts-personalization-2610.17838-2026-10-14.md
maturity: draft
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @sources/arxiv-instantfusion-shared-latent-interface-2610.13944-2026-10-14.md — one latent interface between heterogeneous generators
- @sources/arxiv-gad-geometry-attention-distillation-2610.18779-2026-10-14.md — cross-frame correspondence for video consistency
- @sources/arxiv-physics-aware-deepfake-detection-2610.18485-2026-10-14.md — distance–speech consistency as a physical cue
- @sources/arxiv-finite-sample-conditional-diffusion-2610.13851-2026-10-14.md — learning and discretisation error bounded together
- @sources/arxiv-on-policy-one-shot-tts-personalization-2610.17838-2026-10-14.md — on-policy supervision beats target diversity

## Raw Concept

The question this page answers: **what did the K291 image-gen inbox contain, and what is usable?**

## Narrative

**Five papers are in scope. Three were skipped as out of scope** (robotics VLA and world-model papers — WAVE-0, GreenWAM, GTP) despite being filed here.

### InstantFusion — heterogeneous generators share a latent organisation

The most practically interesting result. Independently trained diffusion/flow models show **similar latent spatial organisation**, and directly handing intermediate states between *unaligned* models still preserves coarse visual content. InstantFusion adds lightweight **Latent AutoEncoders** projecting each model's intermediate states into a **shared latent space**, constrained by two objectives: align states from the same image at matched noise levels, and synchronise local denoising velocities.

Once trained it allows denoising to **transition across frozen generators** without a mapping per model pair. Demonstrated on acceleration, multi-preference composition, cross-architecture on-policy distillation, and cross-model composition.

**Why it matters here:** model-to-model latent handoff, with no per-pair mapping, is the mechanism behind mixing generators in one pipeline.

### GAD — video attention cannot find correspondences; distil them

Current video attention **cannot identify reliable cross-frame correspondences**, with responses dispersed even after scene structure has emerged. GAD transfers correspondences from a **frozen geometry model's attention** into video attention. Because structure forms in deeper layers at high noise and shallower layers at low noise, distillation targets a student layer **selected per noise timestep**.

On Wan2.2 5B: **at least +30%** cross-frame matching accuracy on long-range benchmarks, with **no additional inference modules**.

### Physics-aware deepfake detection — a cue lip-sync cannot see

Most audio-visual detectors rely on **lip–speech synchronisation** and assume static frontal video, so they degrade when the speaker moves. This detector uses an acoustic constraint instead: in real recordings, **speech energy varies predictably with speaker-to-camera distance**; generation can break that coupling. Combining video distance estimates with distance-dependent acoustic measures is effective in dynamic scenarios and **complements** lip-sync detectors in an ensemble.

### Finite-sample guarantees for conditional diffusion

Aligns the score-training objective with the **sampling grid**, so **statistical estimation and numerical discretisation error are analysed together**. Under a smooth conditional density, it derives high-probability bounds on generated-distribution error and the required number of score evaluations: averaged conditional KL $\tilde O_p(n^{-2\beta/(d_x+d_y+2\beta)})$, and TV error $\tilde O_p(n^{-\beta/(d_x+d_y+2\beta)})$, matching existing conditional distribution-estimation rates up to log factors. Both full and early-stopped samplers covered.

### On-policy one-shot TTS personalization

Supervised fine-tuning on a single reference pair **degrades** autoregressive TTS — fixed, off-policy supervision produces blank or near-empty outputs. Diversifying data with zero-shot pseudo-pairs removes the failure but adds little similarity and raises WER, because targets stay fixed and teacher-forced. Two on-policy methods fix it: **GRPO** with a speaker-similarity reward, and **On-Policy Self-Distillation**. Gains stem from **on-policy supervision, not target diversity**.

### Boundary

No install, no wire, no image or print local wire.

## Snippets

> "independently trained generators exhibit similar latent spatial organization, while directly handing off intermediate states between unaligned models can still preserve coarse visual content." [Source: arxiv-2610.13944 p.1]

> "current video attention cannot identify reliable correspondences across frames, with responses dispersed across multiple regions even after recognizable scene structure has emerged." [Source: arxiv-2610.18779 p.1]

> "we propose a physics-aware detector for dynamic speaking videos that leverages an acoustic constraint: in real recordings, speech energy varies predictably with speaker-to-camera distance, whereas deepfake generation can break this coupling." [Source: arxiv-2610.18485 p.1]

## Dead Ends

- **Skipped as out of scope:** `2610.18568` WAVE-0, `2610.18774` GreenWAM, `2610.18677` GTP. Robotics VLA and world models, filed in image-gen but not generative-media work.
- Treating GAD's gain as free. It requires a frozen geometry model and per-timestep layer selection at training time.
