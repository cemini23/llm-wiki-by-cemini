---
title: "An ODE-based sampler for discrete diffusion models"
type: source
tags: [source, arxiv, diffusion, sampling, discrete-diffusion, theory]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | An ODE-Based Sampler for Discrete Diffusion Models |
| Authors | Samson Gourevitch, Yazid Janati, Eric Moulines, Eric P. Xing, Alain Durmus, Giacomo Zanella |
| Affiliations | CMAP École polytechnique; Institute of Foundation Models; MBZUAI; EPITA; Bocconi |
| arXiv | 2610.40618 |
| Pages | 76 |
| File | `arxiv-2610.40618-an-ode-based-sampler-for-discrete-diffusion-mode.pdf` |
| Retrieved | 2026-11-01 |
| Read status | skimmed (abstract and first page) |

## Narrative

Continuous diffusion models have a deterministic counterpart: the probability flow ODE. It reproduces the model's marginals and underpins fast sampling and consistency distillation.

The paper asks whether a discrete diffusion model has an equivalent. It answers yes, and names the construction **exponential residual flows (ERFs)**.

The mechanism: augment the discrete state with a continuous residual variable, one per token and position. The residuals evolve deterministically under piecewise-defined ODEs. Each ODE's vector field reads the current discrete state and the forward and backward rate matrices of the prescribed diffusion model. The discrete state changes only when a residual reaches zero. The paper proves the construction preserves the original marginals.

The authors give a practical discretisation and specialise it to **masked** and **uniform** diffusion. They state that the deterministic trajectories support consistency distillation.

**Why this matters for image and video generation.** Masked diffusion is the family used by several text and image generators. A deterministic sampler makes a seed reproducible and makes distillation cheaper. That is a direct lever on inference cost and on repeatability, which are the two things a local generation pipeline cares about most.

**Caveat.** Only the abstract and first page were read. The paper is 76 pages. The proof, the discretisation error bounds, and any quality numbers are unread here. Do not cite an FID or speed number from this page.

## Snippets

> "The marginals of a continuous diffusion model can be reproduced by a deterministic ordinary differential equation (ODE), known as the probability flow ODE, which provides a foundation for accelerated sampling and consistency distillation." [Source: arxiv-2610.40618 p.1]

> "These residuals evolve deterministically according to piecewise-defined ODEs whose vector fields depend on the current discrete state and the forward and backward rate matrices of the prescribed diffusion model. The discrete state changes whenever a residual reaches zero." [Source: arxiv-2610.40618 p.1]

> "We derive a practical discretization of our sampler and specialize it to masked and uniform diffusion." [Source: arxiv-2610.40618 p.1]

## Dead Ends

- **Citing quality or speed numbers.** The abstract gives none, and only two pages were read. Read the experiments before any such claim.
