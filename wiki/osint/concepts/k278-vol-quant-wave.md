---
title: K278 Vol Quant Wave (Oct 2026)
type: concept
tags: [quant, options, volatility, k278]
keywords: [k278, barrier, american, rbsde, no-trade]
related:
  - concepts/k277-vol-quant-wave.md
  - sources/arxiv-2610.00340-barrier-option-2026-10-02.md
  - sources/arxiv-2610.01187-american-slsv-2026-10-02.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k277-vol-quant-wave.md
- @sources/arxiv-2610.00340-barrier-option-2026-10-02.md
- @sources/arxiv-2610.01187-american-slsv-2026-10-02.md

## Raw Concept

K278 cluster hub. Dual-ID **OSINT K278**. Prior @concepts/k277-vol-quant-wave.md.

## Narrative

Two papers. Both method notes. **No trade. No sizing change.** Zero clones.

| Source | Contribution | Posture |
|--------|--------------|---------|
| 2610.00340 barrier expansion | Leading short-dated up-and-out term is time-inhomogeneous Black-Scholes on the forward variance curve | Speed note |
| 2610.01187 American under SCLV | Reflected backward SDEs price and hedge American options with stochastic correlation | Speed note |

One number from each is worth keeping.

The barrier paper reports a mean absolute error of **0.01248** after the difference correction, against **0.09426** for plain Black-Scholes, validated on a CEV case with 21 strikes. Its correction is of order theta to the power H plus one half, where H is the relative-volatility order. That single exponent spans both rough and regular models, which is the tidy part.

The American paper reports about **35 seconds** for its gradient-boosting backward solver, against about **639 seconds** for a benchmark deep primal-dual training run. Its qualitative result: the effect of stochastic correlation grows when mean reversion is slow, and matters little when other parameters dominate.

Both authors are candid about gaps. The barrier paper states its bound is not available in the general rough case, so weak convergence alone does not justify the limit. The American paper states that the market prices of correlation and volatility risk have no unique specification.

**Cemini posture:** FILE. No clone. No sizing change. **0 product Integrate GO.**
