---
title: "One Prior, Two Dynamics: latent action learning from a video DiT (arXiv:2611.26617)"
type: source
related:
  - concepts/latent-action-learning-video-dit.md
  - concepts/world-models-video-generation.md
  - concepts/camera-controlled-video-generation.md
  - entities/models/wan-2-2.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning |
| Authors | Yuxin Jiang (NUS Show Lab, A*STAR), Wenqiang Sun (Tencent), Jiaqi Li (Tencent), Yuchao Gu (NUS), Lvmin Zhang (Stanford), Ivor Tsang (A*STAR), Mike Zheng Shou (NUS) |
| Type | arXiv preprint, cs.CV |
| arXiv | 2611.26617v1, 19 Nov 2026 |
| Location | `research to be indexed/image-gen/arxiv-2611.26617-one-prior-two-dynamics-repurposing-video-diffusi.pdf` |
| URL | https://arxiv.org/abs/2611.26617 |
| Project page | https://showlab.github.io/o2laf |
| Retrieved | 2026-11-22 |
| Pages | 21 |
| Read status | read |
| Domain fit | **Adjacent.** Video diffusion is repurposed for robot and camera control, not image generation. One design lesson transfers. |

## Narrative

### The idea

Videos show how the world changes but not which actions caused the change. **Latent action learning** recovers that signal from visual transitions. It uses two models:

- An **inverse dynamics model** (IDM) that infers a latent action z from a frame pair.
- A **forward dynamics model** (FDM) that predicts the next frame from the current frame and z.

Prior work puts a pretrained prior in one place at a time: from scratch, on frozen visual features, or as the FDM only. O2LaF (One prior, two dynamics) initialises **both** models from the same pretrained video DiT.

### How

**IDM.** The video DiT becomes a feed-forward transition encoder. Learnable action queries extract one compact latent action (32 dimensions) per transition under causal temporal attention.

**FDM.** The DiT keeps its generative role. Causal joint prediction writes the future state sequence jointly, conditioned on the inferred latent actions, with temporal causality preserved.

**High-noise training.** At partially noisy timesteps the noisy future still leaks much of the target, so the FDM can predict without the action. The authors therefore train at high noise (a mix of the base schedule and a [0.9, 1) band). This forces the FDM to depend on z.

Both models train end-to-end through the 32-dimensional bottleneck.

### Results

Few-shot linear probing of frozen latent actions:

| Setting | Baseline | O2LaF |
|---------|----------|-------|
| GR-1 robot EEF R² (1–32 episodes) | DreamDojo 0.149 | 0.277 |
| MIND camera navigation, exact-match (1–50 videos) | AdaWorld, Olaf-World below | best across budgets |

The encoder trains only on human demonstrations, with no robot adaptation. This suggests the latent actions capture motion structure that transfers across embodiments.

Zero-shot cross-context transfer (VBench imaging quality and camera error):

| Setting | Metric | O2LaF | Olaf-World | AdaWorld |
|---------|--------|-------|------------|----------|
| 1st person | Translation NRMSE ↓ | 1.289 | 1.627 | 2.539 |
| 1st person | Rotation RPE ↓ | 0.786 | 1.300 | 2.055 |
| 3rd person | Translation NRMSE ↓ | 0.511 | 0.985 | 1.342 |

Cross-embodiment cycle reconstruction beats DreamDojo on PSNR, SSIM, and LPIPS for human and robot. Human self-reconstruction PSNR is 26.72 against 23.38.

Latent-action CFG improves motion fidelity. This contrasts with earlier findings that CFG is weak for predefined action controls. The authors attribute it to a continuous motion manifold.

### Workspace relevance

This paper is robotics. It does not produce persona images or video.

One lesson is useful. A pretrained video DiT holds both the ability to **infer** a change and the ability to **render** it. If that holds, the same checkpoint can serve as both an encoder and a generator. For a persona pipeline this points at reusing one video model for motion extraction and motion synthesis, instead of two models.

Wan2.2-TI2V-5B is the base checkpoint here. The action space is 32-dimensional and continuous. Action probing does not always predict downstream control quality; the authors state this explicitly.

## Snippets

> "We initialize both models from the same pretrained video DiT and adapt them to their distinct roles: a feed-forward transition encoder with learnable action queries for inverse dynamics, and a causal, action-conditioned video generator for forward dynamics." [Source: arxiv-2611.26617 p.1]

> "Interestingly, stronger action probing performance does not necessarily translate into better downstream generative control." [Source: arxiv-2611.26617 p.2]

## Dead Ends

An IDM learned from scratch, or on frozen features, does not exploit the video prior. Earlier FDMs also drift toward ignoring the latent action under the standard diffusion recipe. High-noise training is the fix reported here.
