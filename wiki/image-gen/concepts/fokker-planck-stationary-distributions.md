---
title: Fokker-Planck stationary distributions and relaxation modes (math adjacent to diffusion sampling)
type: concept
tags: [concept, stochastic-processes, physics, heavy-tails, peripheral]
keywords: [Fokker-Planck, drift-diffusion, stationary distribution, Pearson type IV, Mpemba effect, relaxation mode, resistor chain, score field, peripheral]
related:
  - sources/arxiv-pearson-type-iv-drift-diffusion-2611.06749.md
  - sources/arxiv-mpemba-quantum-state-preparation-2611.08424.md
  - concepts/single-score-field-conditional-sampling.md
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

The question this page answers: what do the classical stationary-solution and relaxation-rate results say about the drift term that a diffusion model's sampler uses? Synthesized from arXiv:2611.06749 and arXiv:2611.08424.

**This page is peripheral by design.** It groups two mathematics papers so they are findable, and it states plainly that neither paper tests an image model.

## Narrative

**The shared object.** Both papers study a linear stochastic process, `dx = m(x) dt + sqrt(2 d(x)) dW`, and its Fokker-Planck equation. That equation has the same structure as the probability-flow ODE and the reverse SDE inside a score-based model: a drift term and a diffusion term, with the data distribution as the stationary state.

**Paper one — what stationary solutions look like.** With linear drift and quadratic diffusion, the stationary solution is Pearson type IV. Two shape parameters:

| Parameter | Controls |
|---|---|
| κ | tail weight |
| λ | asymmetry |

The paper gives closed forms for the CDF, a moment recurrence, skewness, kurtosis and the mode, plus necessary and sufficient conditions for the solution to exist. The physical reading is that tail weight comes from the curvature of the diffusion coefficient and asymmetry comes from its gradient. Asymmetric fluctuations can appear even with a symmetric restoring drift.

**Paper two — how fast relaxation happens, and how initial conditions change it.** The strong Mpemba effect shortens relaxation by choosing a starting state with zero overlap on the slowest decaying mode. In a disordered system the slow mode differs per sample, so a blind preparation normally keeps some overlap. The paper shows a blind preparation can still win in typical samples, and links the residual overlap to the electrical resistance profile of an equivalent resistor chain. The decay is L^(−1/2) in chain length only when the resistance variance is finite.

**The one honest link to diffusion sampling.** Both results concern a stationary state reached by relaxation, and how the starting point and the drift change the convergence rate. Sampler schedule design is the same problem in a different language. An image sampler that starts from a chosen noise level is choosing an initial condition; a schedule is choosing how long each mode is given to decay.

That is an analogy. No experiment in either paper involves a learned score, an image, or a video. Nothing here changes a ComfyUI workflow.

**Operator read.** REFERENCE, wiki-only, no distribution. Use it to keep the vocabulary straight — "drift", "stationary distribution", "relaxation mode" — and to avoid mistaking a physics result titled "drift-diffusion" for an image-generation paper.

## Snippets

[Source: arxiv-2611.06749 p.1 — "Heavy tails and asymmetry originate from distinct features of state-dependent diffusion: its local nonlinear curvature and gradient, respectively."]

[Source: arxiv-2611.08424 p.1 — "A finite mean resistance suffices for diffusion, but the residual overlap decays as L−1/2 with chain length L only when the resistance variance is finite."]
