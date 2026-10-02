---
title: "American options under stochastic local volatility and correlation (2610.01187)"
type: source
tags: [source, k278, quant, options, volatility]
keywords: [k278, rbsde, american-option, xgboost, FILE]
related:
  - concepts/k278-vol-quant-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-vol-quant-wave.md

## Raw Concept

| File | `arxiv-2610.01187-on-the-pricing-of-american-options-under-stochas.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.01187-on-the-pricing-of-american-options-under-stochas.pdf` |
| Archive | egress-fi 2026-10-02 |
| Retrieved | 2026-10-02 |
| Dual-ID | **OSINT K278** |
| sha256 | `5828bc3fe3b5dbb2c4ee43358b1c50b1be5c88fd138f51661e192bbaa745cad6` |
| arXiv | 2610.01187 |
| Author | L. Teng (University of Wuppertal) |

## Narrative

The paper extends stochastic local volatility models with a flexible stochastic correlation process, which the author calls SCLV.

Reflected backward stochastic differential equations give the pricing and hedging framework. The paper derives sensitivities to spot, local volatility, and correlation, and shows the framework also models how the option price evolves forward in time.

The numerical scheme is a gradient-boosting regression backward solver, using XGBoost. The author gives a convergence analysis that accounts for the reflection and obstacle error.

Reported timings: about **35 seconds** average run time, against about **639 seconds** for a benchmark deep primal-dual training run. Tests cover SABR plus stochastic correlation, and Heston stochastic local volatility plus stochastic correlation, for an American put.

One qualitative result is worth keeping: the effect of stochastic correlation grows when mean reversion is slow, and matters little when other parameters dominate.

The author admits two open points. Robust hedging needs work on ill-conditioned systems, and SCLV calibration needs faster numerical methods. The market prices of correlation and volatility risk have, in the author's words, no unique way to specify.

No code URL. No clone. Method note only. **No trade. No sizing change.**
