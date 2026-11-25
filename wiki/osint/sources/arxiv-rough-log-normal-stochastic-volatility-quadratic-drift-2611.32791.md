---
title: "Rough log-normal stochastic volatility with quadratic drift"
type: source
related:
  - concepts/rough-log-normal-volatility.md
  - concepts/local-stochastic-volatility-calibration.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Rough log-normal stochastic volatility with quadratic drift: second-moment stability and the martingale property under positive correlation |
| Author | Artur Sepp (LGT Bank, Zurich), Parviz Rakhmonov (Marex, London) |
| Type | arXiv preprint, mathematical finance (q-fin.MF) |
| Location | `research to be indexed/osint/arxiv-2611.32791-rough-log-normal-stochastic-volatility-with-quad.pdf` |
| Retrieved | 2026-11-25 |
| arXiv | 2611.32791v1, 24 Nov 2026 |
| Pages | 34 |
| Read status | read |

## Narrative

### Problem

Rough volatility models fit equity-index implied volatility better than standard stochastic volatility, because log-volatility looks like a fractional Brownian motion with a Hurst exponent near 0.1. But a rough model must still produce a true martingale price. With positive spot-volatility correlation, the standard rough Bergomi model fails that condition. The paper extends a log-normal stochastic volatility model with quadratic drift to a fractional Volterra equation, and shows when the price stays a martingale.

### The model

Volatility follows a Volterra equation with a Riemann-Liouville fractional kernel `K(t) = t^(H-1/2) / Gamma(H+1/2)`, `H` in (0, 1/2]. The drift is quadratic in the volatility: `(κ1 + κ2σ)(θ − σ)`. That quadratic term is the stabiliser. It offsets the damping that positive correlation would otherwise remove. [Source: arxiv-2611.32791-rough-log-normal-stochastic-volatility-with-quad.pdf p.1]

### Theoretical results

The volatility equation has a unique global non-negative solution with finite moments. Under linear drift, the first two conditional moments are exact, and there is a threshold `γ = ϑ² ∫ G(u)² du` for a uniformly bounded second moment. Below the threshold the second moment is bounded; above it, the second moment grows exponentially at a rate the paper derives. [Source: arxiv-2611.32791-rough-log-normal-stochastic-volatility-with-quad.pdf p.7]

The martingale condition is clean. With positive quadratic damping, `κ2 >= β` is sufficient for the price to be a true martingale under the pricing measure. For finite exponential mixtures the condition is also necessary. For the singular fractional kernel, necessity stays open.

### Calibration

The model is fitted to Bitcoin and Ether option smiles at fixed roughness, with `H = 0.30` and `H = 0.50`. Six risk-neutral coefficients are estimated by least squares to premium midpoints, with the constraint `κ2 >= β`. A 97-factor Markovian approximation makes the fit practical.

The rough fit places 27 of 45 Bitcoin prices and 33 of 39 Ether prices inside the bid-ask bands. Its RMS error is 9.4% lower than the classical fit for Bitcoin and 13.3% higher for Ether. The Bitcoin fit lands at `κ2 − β = 0.01`. Implied volatilities range from 0.096 to 0.223. [Source: arxiv-2611.32791-rough-log-normal-stochastic-volatility-with-quad.pdf p.12]

### Microstructure reading

Appendix C gives an order-flow interpretation. Signed volatility impacts arrive at a rate proportional to variance, which generates multiplicative noise. A small state-dependent bias in the trade sign produces the quadratic drift. That is a modelling story, not an estimate. The authors say so.

The paper discloses use of generative AI to edit text and check arguments. The authors state they made the methodological decisions and verified the results. [Source: arxiv-2611.32791-rough-log-normal-stochastic-volatility-with-quad.pdf p.13]

### Why it matters here

This gives a rough-volatility model that is internally consistent: non-negative, moment-stable, and a true martingale under positive correlation. For crypto option work the Bitcoin calibration is the useful data point. The Ether fit is worse than the classical model, so the method is not a free win.

## Snippets

> "With positive quadratic damping the second moment is uniformly bounded for every admissible Hurst exponent and volatility of volatility." [Source: arxiv-2611.32791-rough-log-normal-stochastic-volatility-with-quad.pdf p.1]

> "The quadratic term keeps the price process a true martingale when returns and volatility are positively correlated, provided κ2 ≥ β." [Source: arxiv-2611.32791-rough-log-normal-stochastic-volatility-with-quad.pdf p.1]
