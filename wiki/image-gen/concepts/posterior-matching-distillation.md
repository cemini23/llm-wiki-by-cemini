---
title: Posterior matching distillation (PMD)
type: concept
related:
  - sources/arxiv-2611-26629-posterior-matching-distillation.md
  - concepts/diversity-collapse-in-distilled-generators.md
  - concepts/adversarial-distribution-matching-distillation.md
  - concepts/one-step-autoregressive-video-distillation.md
  - concepts/score-gradient-matching-video-distillation.md
  - entities/models/flux-2-klein.md
  - entities/models/sdxl-fine-tunes.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: how do you distill a diffusion model to a few steps without losing the diversity of its outputs?

From arXiv 2611.26629 (Virginia Tech, NVIDIA).

## Narrative

### Why distillation loses diversity

Distribution-based distillation matches the student's output to the teacher's. Most methods use a reverse-KL objective. Reverse KL is mode-seeking: it keeps the dominant teacher modes and drops the rest. The result is mode collapse, or few distinct images per prompt.

A second gap: matching output marginals does not pin the conditional distribution at each noise level. A student can match the teacher's mixture of outputs while learning a different noisy-to-clean map.

### The PMD idea

Posterior Matching Distillation trains a **stochastic** student to recover the teacher's conditional posterior of clean images at each noise level.

The target is an **exponentially tilted posterior mean**. The enabling identity:

> Under Gaussian corruption, exponentially reweighting the posterior equals shifting the noisy input at the same noise level. (Tilt=Shift)

So each target mean is one frozen-teacher call at a shifted input. No Monte Carlo sampling of teacher trajectories is needed.

### The loss

1. Fix a noisy state z and a tilt direction.
2. Target = teacher(z + ρ·tilt, t).
3. Draw M student samples from the same z.
4. Weight them by softmax of tilt · x.
5. Minimise the squared distance between the weighted student mean and the target.

Matching tilted means over an open neighbourhood of directions uniquely identifies the full posterior, including multimodal structure and mode probabilities. Thus a family of **mean** constraints supervises the whole conditional distribution, with no auxiliary score network. Four student draws per state suffice.

Add a non-saturating logistic GAN loss, as DMD2 does. Train on 8× L40 for 2,000 updates. Stochasticity comes from doubling the first layer's input width.

### Any-step sampling

The student learns the posterior at every trained noise level. To use more steps, re-noise the prediction to the next level and evaluate again. One student serves 2, 4, or more steps with no retraining.

### Results at four steps (1024×1024)

| Model | Method | FID ↓ | Vendi ↑ (PartiPrompts) |
|-------|--------|-------|------------------------|
| SDXL | DMD2 | 19.20 | 2.5178 |
| SDXL | PMD | 19.14 | 4.4621 |
| FLUX.2 klein 4B | RTDMD | 31.57 | 1.8540 |
| FLUX.2 klein 4B | PMD | 24.12 | 3.3708 |

PMD has the best FID among four-step methods on both families, and a large diversity lead. On SDXL it gives up GenEval and HPSv3 to DMD2 and SDXL-Lightning. On FLUX.2 it gives up GenEval to RTDMD, which adds external reward supervision. The pattern: PMD buys diversity with a small quality cost.

### When to use it

PMD is a **training** recipe. A shipped checkpoint cannot be converted with it.

Two uses:

1. **Explain the loss.** A four-step distill that uses reverse KL should lose diversity by construction. PMD shows the loss is not necessary.
2. **Distill your own model.** If you distill your own persona fine-tune, PMD keeps more seeds distinct and covers several step budgets with one student.

Check first whether the pipeline needs diversity. For a fixed persona look, mode collapse can be acceptable. For a batch of candidate images from one prompt, diversity is the product.

## Snippets

> "This matching is often driven by reverse-KL objectives, whose mode-seeking bias favors dominant teacher modes at the expense of diversity across samples." [Source: arxiv-2611.26629 p.1]

> "We prove that, matching tilted means over an open neighborhood uniquely identifies the full posterior." [Source: arxiv-2611.26629 p.1]
