---
title: Pixel-space video diffusion without a latent bottleneck
type: concept
maturity: draft
related:
  - sources/arxiv-jvt-pixel-space-video-diffusion-2611.18549.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: does video diffusion still need a pretrained autoencoder and a U-Net?

From JVT (arXiv 2611.18549).

## Narrative

The default stack is latent diffusion: encode video into a learned latent, denoise there, decode. The cost is a fixed lossy bottleneck and a second model to train and ship.

JVT operates directly on high-dimensional pixels with a large-patch DiT-style transformer, without an autoencoder, auxiliary detailers, cascaded refinement, or U-Net skips. The paper's work is finding a patch-embedding and normalisation combination that makes this efficient enough to be competitive with latent baselines on class-conditioned and unconditional generation.

The structural payoff is joint modality generation. Because everything is in pixel space, camera-conditioned RGB and disparity can be produced together. That improves camera following over RGB-only baselines and yields explicit geometry at inference without a separate reconstruction stage.

Why it matters for a pipeline: removing the autoencoder removes a whole failure class (reconstruction artefacts) and a whole model from the dependency graph. The open cost is compute at high resolution, which the paper addresses by design rather than by scaling.

[TENTATIVE] One preprint's abstract. The ablations and the actual compute numbers were not read.

## Snippets

> "The pixel-space formulation of JVT also naturally supports joint generation of pixel-aligned modalities."
