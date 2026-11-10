---
title: Long memory and the a = 1/2 phase transition — correlated Bernoulli selection
type: concept
related:
  - sources/arxiv-random-lcm-memory-2611.11301.md
  - concepts/market-memory-hurst-regime.md
  - concepts/genealogical-reinforcement-branching.md
updated: 2026-11-10
---

## Raw Concept

At what memory level does a system's description change class, and what does the proof shape look like? Prompted by arXiv 2611.11301.

## Narrative

### The process

A binary sequence `X_1, ..., X_n` with fixed marginal `θ` and a copying rule:

```
P(X_{j+1} = 1 | history) = θ + a ( average(X_1..X_j) - θ )
```

With probability `a` the new value copies a uniformly chosen earlier value. With probability `1 - a` it is drawn fresh. `a = 0` is independent sampling.

The copying rule builds a **genealogical forest**. Each component inherits the label of its root. That is the device that turns a temporal dependence into a clustering problem.

### The phase transition

The object is `T_n = log lcm(A_n)`, the logarithm of the least common multiple of the retained set.

| Range of `a` | Fluctuation scale | Limit |
|---|---|---|
| `0 ≤ a < 1/2` | `√n log n` | Gaussian, same variance as independent |
| `a = 1/2` | `√n log n` | Gaussian, larger variance |
| `1/2 < a < 1` | `n^a` | Non-Gaussian |

[Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.4]

The law of large numbers is unchanged at `T_n / n → c(θ)` in all three regimes. Only the fluctuation class changes.

### The boundary case

Under sparse retention (`θ_n ~ λ/n`), the retained count converges to a marked Poisson process. Marks are geometric conditional on the root time. Mixed over root times the mark law is **Yule–Simon** with parameter `1/a`. The variance is finite only for `a < 1/2`. [Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.5]

### The proof shape

1. Reduce to primes larger than `√n`, whose multiple sets are disjoint.
2. Expand the fluctuations exactly into a martingale of fresh decisions plus a memory-carrying drift.
3. Project the drift onto the retained count.
4. Control rare families with marked point-process convergence.

### Why it is here

The paper has no market content. Its value is a **worked example of a memory threshold**. Two lessons:

- **A regime shift can be a change of scaling class, not a change of mean.** A test that looks only at the mean cannot find it. The right test looks at how the variance scales with `n`.
- **A boundary parameter forces a simulated null.** The same issue appears in the branching paper and in any model where a parameter is inactive under the null. See @concepts/genealogical-reinforcement-branching.md.

This is a method reference only. Do not read `a` as a Hurst exponent, and do not fit this process to price data.

## Snippets

> "At fixed density, the logarithmic least common multiple exhibits a fluctuation phase transition at the memory parameter a = 1/2." [Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.1]

> "For a > 1/2, the scale changes from √n log n to n^a, and the non-Gaussian count process limit determines the leading fluctuation." [Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.5]

> "Thus Z has the Yule–Simon distribution with parameter 1/a." [Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.5]

## Dead Ends

- **Reading `a` as a Hurst exponent.** It is a copying probability in a specific generative model. It does not estimate H.
- **Looking for a mean shift.** The mean is unchanged across all three regimes.
- **Using the boundary variance for `a ≥ 1/2`.** The second moment is infinite there.
