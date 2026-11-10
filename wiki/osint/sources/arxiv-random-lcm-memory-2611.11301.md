---
title: "Random least common multiples with memory — a phase transition at a = 1/2"
type: source
related:
  - concepts/k296-feeds-wave.md
  - concepts/long-memory-phase-transition-correlated-bernoulli.md
  - concepts/market-memory-hurst-regime.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Phase Transitions for Random Least Common Multiples with Memory |
| Author | Shaochen Wang, Guangyu Yang, Wang Zhou |
| Type | arXiv preprint, math.PR |
| Location | `research to be indexed/osint/arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf` |
| Retrieved | 2026-11-10 |
| File | arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf (36 pages) |
| Read status | read |

## Narrative

The paper studies the least common multiple of a random subset of `{1, ..., n}`. The selection is not independent. Each indicator copies a uniformly chosen earlier indicator with probability `a`, and is sampled fresh with probability `1 - a`. Every indicator keeps marginal retention probability `θ`. So `θ` sets density and `a` sets memory.

The copying rule builds a **genealogical forest**. A copied decision joins its predecessor, and a fresh decision starts a new component. Each root carries a Bernoulli label, and every descendant inherits it. The selected set is the union of the components with label one.

### Main result

The law of large numbers does not change: `T_n / n → c(θ)`. The fluctuations do change, in three regimes.

| Range of `a` | Scale | Limit |
|---|---|---|
| `0 ≤ a < 1/2` | `√n log n` | Gaussian, same variance as the independent case |
| `a = 1/2` | `√n log n` | Gaussian, variance increased by `θqK²_{1/2,θ}` |
| `1/2 < a < 1` | `n^a` | Non-Gaussian, driven by the count process |

[Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.4]

The threshold `a = 1/2` is the phase transition. Below it, dependence is invisible at the leading arithmetic scale. Above it, the scale of the fluctuation changes from `√n log n` to `n^a`, and the variance becomes infinite in the boundary regime.

The proof splits the fluctuation into a martingale of fresh decisions and a memory-carrying drift. The reduction to primes larger than `√n` makes the divisibility indicators almost independent.

### The boundary cases

- **Sparse retention** (`θ_n ~ λ/n`): the retained count converges to a marked Poisson process with geometric marks. Mixed over the uniform root time, the mark is **Yule–Simon** with parameter `1/a`. The variance is finite only when `a < 1/2`. [Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.5]
- **Near-complete retention**: the logarithmic defect converges to a Poisson law. Memory does not change the limit.

### Why it matters here

This is pure probability, with no market content. Its value to the wiki is structural, not numerical.

The paper gives a clean example of a system where a **single memory parameter flips the scaling law** and where the flip is at a specific value, not a gradual drift. That is the same question a regime model asks: at what memory level does the description of the series change class. @concepts/market-memory-hurst-regime.md frames that question with a Hurst statistic. This paper shows how to prove the answer when the generative process is known.

It also gives a template for a **simulated null**. When a parameter is unidentifiable under the null, or sits on a boundary, the asymptotic distribution does not apply. You must simulate the null. The branching paper in the same wave does the same thing.

## Snippets

> "At fixed density, the logarithmic least common multiple exhibits a fluctuation phase transition at the memory parameter a = 1/2." [Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.1]

> "For a > 1/2, the scale changes from √n log n to n^a, and the non-Gaussian count process limit determines the leading fluctuation." [Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.5]

> "Thus Z has the Yule–Simon distribution with parameter 1/a." [Source: arxiv-2611.11301-phase-transitions-for-random-least-common-multip.pdf p.5]

## Dead Ends

- **Reading the result as a market model.** The retained integers have no economic meaning. The `a` parameter is not a Hurst exponent and does not estimate one.
- **Using the boundary variance formula for `a ≥ 1/2`.** The second moment is infinite there. A sample variance will not converge.
