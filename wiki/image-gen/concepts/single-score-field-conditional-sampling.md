---
title: Single score field for exact conditional sampling (DISCO)
type: concept
tags: [concept, score-matching, diffusion, conditional-sampling, theory]
keywords: [DISCO, single score field, exact conditional, tempered SMC, Metropolis-Hastings, energy-based model, guidance bias, diffusion-free]
related:
  - sources/arxiv-disco-diffusion-free-score-matching-2611.09758.md
  - concepts/tuned-diffusion-sampling-oys.md
  - concepts/constrained-braided-diffusion-sampling.md
  - concepts/fokker-planck-stationary-distributions.md
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

The question this page answers: why are conditional samples from a diffusion model biased, and what would fix it in principle? Synthesized from arXiv:2611.09758 (DISCO).

## Narrative

**The structural problem.** A diffusion model learns a family of score fields, one per noise level. Conditioning information exists only for clean data. So any method that conditions a diffusion sampler must inject that information at noise levels where it was never defined. The result is a heuristic, not a conditional draw.

**What the heuristics do.** Three common approaches were compared on a two-dimensional Gaussian mixture:

| Method | Behaviour on the true conditional |
|---|---|
| Gradient guidance | substantial deviation |
| Replacement heuristic | substantial deviation |
| Twisted diffusion sampler (particle based) | substantial deviation |

The authors' point is that the deviation is not a tuning failure. It comes from conditioning a process that has no conditional defined at high noise.

**The alternative.** Learn one score field of the slightly perturbed data distribution. Training keeps diffusion's support-broadening benefit — the score is learned away from the data manifold — without a time index. Conditioning then means: fix the observed variables in the joint score. That yields the exact conditional score, and standard MCMC draws from it.

**Two parameterisations, two exactness claims.** This distinction is the honest core of the paper.

| Case | Model | Sampler | Exactness |
|---|---|---|---|
| Low dimension | energy function, `p = exp(-E)/Z` | Metropolis-corrected MCMC (HMC) | asymptotically exact |
| Images | unconstrained score network | tempered SMC | exact only at the population optimum |

An energy parameterisation defines a real density and allows Metropolis correction. A directly modelled score need not be conservative — it may correspond to no density at all. That is secondary for pure generation, and essential for inference.

**Why it matters here.** Nearly every practical task in this wiki is a conditional generation: keep this face, change this shirt, hold this layout. All of those use guidance heuristics whose bias is now documented on a toy problem. A single joint score field would make the conditional principled. That is a research direction, not a tool.

**Relation to schedule tuning.** `@concepts/tuned-diffusion-sampling-oys.md` asks which timesteps to evaluate. This page asks whether there should be timesteps at all. The two are orthogonal: better schedules improve a family of fields, and a single field removes the family.

**Operator read.** REFERENCE. No checkpoint, no node, no speed claim against a production model. Use the vocabulary — "conditioning a family of fields is a heuristic" — when a guidance result looks unstable.

## Snippets

[Source: arxiv-2611.09758 p.2 — "Here, 'exact' refers to the target: samples are asymptotically exact draws from the conditional of the learned model."]
