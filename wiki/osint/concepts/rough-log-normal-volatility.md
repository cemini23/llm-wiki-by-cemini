---
title: Rough log-normal stochastic volatility with quadratic drift
type: concept
maturity: draft
related:
  - sources/arxiv-rough-log-normal-stochastic-volatility-quadratic-drift-2611.32791.md
  - concepts/local-stochastic-volatility-calibration.md
  - concepts/stochastic-calculus-foundations.md
updated: 2026-11-25
---

## Raw Concept

Question this page answers: can a rough volatility model be both realistic and arbitrage-free under positive spot-volatility correlation?

From Sepp and Rakhmonov, "Rough log-normal stochastic volatility with quadratic drift" (arXiv 2611.32791, 2026-11-24).

## Narrative

**The tension.** Equity-index log-volatility behaves like a fractional Brownian motion with a Hurst exponent near 0.1. Rough models fit the smile well. But the standard rough Bergomi model cannot combine positive spot-volatility correlation with a true-martingale price under the usual pricing measure. Positive correlation is common in Bitcoin options. A model that breaks the martingale property is not usable for pricing.

**The fix.** Add a quadratic drift term to a log-normal volatility model and extend it to a fractional Volterra equation. The drift `(κ1 + κ2σ)(θ − σ)` gives a damping response that grows with volatility. At large volatility the leading term is `−κ2σ²`, which is stronger damping than the linear model.

**Three results.**
- The volatility equation has a unique global non-negative solution with finite moments.
- Under linear drift there is an exact second-moment threshold `γ = ϑ² ∫ G(u)² du`. Below it the second moment is bounded; above it the second moment grows exponentially.
- The price is a true martingale when `κ2 >= β`, where `β` is the volatility beta. For finite exponential mixtures that condition is also necessary. [Source: arxiv-2611.32791-rough-log-normal-stochastic-volatility-with-quad.pdf p.1]

**Calibration evidence.** Fitted to Bitcoin and Ether smiles at `H = 0.30` and `H = 0.50`, with a 97-factor approximation. The rough fit is better for Bitcoin, 9.4% lower RMS error, and worse for Ether, 13.3% higher. Both fits land at `κ2 − β = 0.01`. So the method is not a free win; it depends on the underlying.

**Microstructure story.** Appendix C maps the model to order flow: signed volatility impacts arrive at a rate proportional to variance, generating multiplicative noise, and a small state-dependent bias in the trade sign generates the quadratic drift. The authors present this as an interpretation, not an estimate.

**Read.** Use this page as the reference for a rough-volatility model that stays arbitrage-free. The calibration numbers are the checkable part. The Bitcoin result is the useful data point for crypto options.

[OPEN QUESTION 2026-11-25] Necessity of the martingale condition for the singular fractional kernel remains open. Strict positivity of the fractional volatility is a conjecture.
