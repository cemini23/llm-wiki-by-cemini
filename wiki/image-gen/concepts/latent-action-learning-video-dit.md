---
title: Latent action learning with one video DiT prior
type: concept
related:
  - sources/arxiv-2611-26617-one-prior-two-dynamics-latent-action.md
  - concepts/world-models-video-generation.md
  - concepts/camera-controlled-video-generation.md
  - entities/models/wan-2-2.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: can one pretrained video generator supply both the ability to infer a control action and the ability to render its effect?

From arXiv 2611.26617 (NUS Show Lab, Tencent, Stanford).

## Narrative

### The setup

Latent action learning extracts a control signal from unlabeled video. Two models do the work:

- **Inverse dynamics model (IDM):** z = IDM(x_t, x_t+1). It infers the action from a frame pair.
- **Forward dynamics model (FDM):** x̂_t+1 = FDM(x_t, z). It predicts the consequence.

Prior work puts a pretrained prior in one place at a time: from scratch, on frozen features, or as the FDM only. The idea here is **one prior, two dynamics**: initialise both models from the same pretrained video DiT.

### How the roles split

| Role | Adaptation |
|------|------------|
| IDM | Feed-forward transition encoder; learnable action queries; causal temporal attention; 32-dim bottleneck |
| FDM | Causal joint prediction of the future sequence, conditioned on z |

Both train end-to-end through the bottleneck. The bottleneck size is what forces z to keep only what explains the change.

### The high-noise trick

At partially noisy timesteps the noisy future leaks the target, so the FDM can predict without the action. Training at high noise (a mix of the base schedule and a [0.9, 1) band) forces the FDM to depend on z. Without this, the FDM learns to ignore the action.

### Results

- Few-shot linear probing: GR-1 robot EEF R² 0.277 against DreamDojo's 0.149. The encoder trains on human demonstrations only, with no robot adaptation.
- Zero-shot cross-context camera transfer: lowest camera-motion error and highest imaging quality in first and third person, against AdaWorld and Olaf-World.
- Cross-embodiment cycle reconstruction: beats DreamDojo on PSNR, SSIM, and LPIPS.

### Why this is here and not in a robotics wiki

Video DiT reuse is the image-gen link. The result says a video model trained to predict visual change already encodes both a transition encoder and a renderer. For a persona pipeline the implication is narrow but real: one video checkpoint can extract motion and synthesise it, instead of two models.

The paper also warns that action probing quality does not always predict downstream control quality. Validate the action space on the application, not on the probe.

## Snippets

> "One prior, two dynamics." [Source: arxiv-2611.26617 p.1]

> "Much of the prior needed for latent action learning therefore already exists inside a pretrained video generator." [Source: arxiv-2611.26617 p.2]
