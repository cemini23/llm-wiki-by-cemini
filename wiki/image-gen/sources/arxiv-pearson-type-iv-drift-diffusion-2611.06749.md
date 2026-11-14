---
title: "Pearson type IV as a drift-diffusion stationary distribution (arXiv:2611.06749)"
type: source
tags: [source, arxiv, stochastic-processes, heavy-tails, physics, peripheral]
keywords: [Pearson type IV, Fokker-Planck, drift-diffusion, linear-quadratic process, heavy tails, skewness, kurtosis, moment recurrence, peripheral]
related:
  - concepts/fokker-planck-stationary-distributions.md
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Drift-Diffusion Approach for Pearson Type IV Heavy-Tail Distributions |
| Author | Daniele Belardinelli, Simone Benella, Mirko Stumpo, Giuseppe Consolini |
| Type | arXiv:2611.06749, 9 pages |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.06749-a-drift-diffusion-approach-for-pearson-type-iv-h.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.06749-a-drift-diffusion-approach-for-pearson-type-iv-h.pdf` |
| Read status | read (abstract, derivation sketch) |

## Narrative

**Peripheral to image generation.** The "drift-diffusion" in the title is the Fokker-Planck sense, not the image-diffusion sense. This paper has no model, no sampler and no image experiment. It is logged to prevent a later keyword search from producing a false positive.

**What it proves.** Derive the Pearson type IV distribution as the stationary solution of a standardised Fokker-Planck equation with linear drift and quadratic diffusion. The authors establish necessary and sufficient conditions for that solution, and show that the linear-quadratic structure is sufficient but not necessary.

**Two shape parameters.**

| Parameter | Controls |
|---|---|
| κ | tail weight |
| λ | asymmetry |

Closed forms are given for the cumulative distribution function, a moment recurrence relation, skewness, kurtosis and the mode.

**The physical interpretation.** Heavy tails and asymmetry come from separate features of a state-dependent diffusion coefficient: its local nonlinear curvature and its gradient. In particular, asymmetric stationary fluctuations can appear even with a symmetric linear restoring drift.

**Context.** The stated application is space-plasma turbulence, where magnetic-field increment PDFs become increasingly non-Gaussian as the scale decreases.

**The one thin link to this wiki.** Score-based generative models learn a drift term, and the stationary distribution of the reverse process is the data distribution. Stationary-solution families are therefore the well-studied half of that problem. No transfer to a diffusion image model is demonstrated.

## Snippets

> "We derive the Pearson type IV distribution as the stationary solution of a standardized Fokker-Planck equation with linear drift and quadratic diffusion." [Source: arxiv-2611.06749 p.1]

> "Heavy tails and asymmetry originate from distinct features of state-dependent diffusion: its local nonlinear curvature and gradient, respectively." [Source: arxiv-2611.06749 p.1]
