---
title: "DISCO — diffusion-free score matching for exact conditional sampling (arXiv:2611.09758)"
type: source
tags: [source, arxiv, score-matching, diffusion, conditional-sampling, mcmc, theory]
keywords: [DISCO, diffusion-free score matching, single score field, exact conditional sampling, tempered SMC, Metropolis correction, energy-based model, Fisher divergence]
related:
  - concepts/single-score-field-conditional-sampling.md
  - concepts/tuned-diffusion-sampling-oys.md
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Diffusion-free Score Matching for Exact Conditional Sampling |
| Author | Thomas Wedenig, Robert Peharz (TU Graz, Graz Center for Machine Learning) |
| Type | arXiv:2611.09758, 26 pages |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.09758-diffusion-free-score-matching-for-exact-conditio.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.09758-diffusion-free-score-matching-for-exact-conditio.pdf` |
| Read status | read (abstract, method, claims) |

## Narrative

A theoretical paper that asks a fair question: does a generative model need a whole family of noise-indexed score fields?

**The observation.** A diffusion model learns one score field per noise level. Sampling from a marginal is easy. Sampling from an arbitrary conditional is not, because conditioning information exists only for clean data, not for the high noise levels the sampler needs.

**The proposal.** Learn one score field of the slightly perturbed data distribution, not a time-indexed family. The training objective looks like a diffusion loss and keeps diffusion's support-broadening benefit. The model then conditions by fixing the observed variables in the joint score. That gives the exact conditional score, which standard MCMC can sample.

**Claimed result.** On toy Gaussian mixtures, DISCO matches the model's true conditional where three diffusion heuristics — gradient guidance, the replacement heuristic and the twisted diffusion sampler — deviate substantially. On images, sample quality is close to diffusion models. Across repeated resampling, its conditionals drift the least of the tested samplers.

**The exactness qualifier.** The paper is careful here, and the qualifier matters:

| Setting | Parameterisation | Exactness |
|---|---|---|
| Low dimension | energy-based, Metropolis-corrected MCMC | asymptotically exact |
| Images | unconstrained score | exact only at the population optimum |

**Why it matters here.** Almost every practical task in this wiki is conditional generation: keep this face, change this shirt, hold this layout. Today that is done with heuristics. A single joint score field makes the conditional principled rather than a knob. That is a direction, not a tool an operator can use this week.

**Operator read.** No checkpoint, no ComfyUI node, no measurable speed claim against production models. The images experiment uses an unconstrained score, so it is not exact either. Treat this as REFERENCE: useful language for why conditional guidance drifts, and a research path if the wiki ever adopts a sampler at this level.

## Snippets

> "DISCO is competitive with state-of-the-art diffusion models in terms of sample quality. More importantly, DISCO yields a more faithful representation of the underlying data distribution and—crucially—enables accurate sampling from arbitrary conditionals." [Source: arxiv-2611.09758 p.1]

> "Here, 'exact' refers to the target: samples are asymptotically exact draws from the conditional of the learned model." [Source: arxiv-2611.09758 p.2]

## Dead Ends

- **Treating DISCO as a drop-in sampler.** The exactness proof covers the low-dimensional energy parameterisation. The image case is exact only at the population optimum.
