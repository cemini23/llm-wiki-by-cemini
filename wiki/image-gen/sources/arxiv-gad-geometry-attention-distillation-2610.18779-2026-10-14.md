---
title: "GAD — Geometry Attention Distillation for Consistent Video Generation"
type: source
tags: [arxiv, video-generation, attention, consistency]
keywords: [geometry attention distillation, cross-frame correspondence, video diffusion, temporal consistency, Wan2.2]
related:
  - concepts/k291-image-gen-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-image-gen-wave.md — K291 image-gen wave hub

## Raw Concept

Title: GAD — Geometry Attention Distillation for Consistent Video Generation
Authors: Junfeng Ni, Ziyu Zhu, Fan Jiang et al. (Tsinghua, AMAP Alibaba, BIGAI)
Type: arXiv preprint (2610.18779)
Location: `research to be indexed/image-gen/arxiv-2610.18779-gad-geometry-attention-distillation-for-consiste.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The diagnosis:** current video attention **cannot identify reliable cross-frame correspondences** — responses spread across multiple regions even after recognisable scene structure has emerged. Reliable associations are what let information exchange as structure forms.

**The fix:** **Geometry Attention Distillation** transfers correspondences from a **frozen geometry model's** attention into video attention. Because structure forms in **deeper layers at high noise and shallower layers at low noise**, distillation targets a student layer **chosen per noise timestep**.

| Measure | Effect |
|---|---|
| Cross-frame matching accuracy (Wan2.2 5B) | **≥ +30%** over baseline, long-range benchmarks |
| Backbones tested | three |
| Inference cost | **no additional modules** |

## Snippets

> "current video attention cannot identify reliable correspondences across frames, with responses dispersed across multiple regions even after recognizable scene structure has emerged." [Source: arxiv-2610.18779 p.1]

> "On Wan2.2 5B, GAD improves cross-frame matching accuracy by at least 30% over the Wan baseline on both long-range benchmarks." [Source: arxiv-2610.18779 p.1]

## Dead Ends

- Applying distillation at a fixed layer. The paper shows the effective layer moves with the noise timestep.
