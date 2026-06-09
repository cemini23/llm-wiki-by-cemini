---
title: "OLS alpha signal framework — intercept as edge after factor strip"
type: concept
tags: [concept, quant-finance, factor-models, signal-testing, k107]
keywords: [ols-alpha, intercept, information-coefficient, newey-west, out-of-sample, multiple-testing, rohonchain]
related:
  - sources/trading-posts-compilation-7-2026-06-09.md
  - concepts/time-series-arima-garch-framework.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/regime-conditioned-evaluation.md
  - sources/ssrn-5140015-time-series-quant-finance-2025.md
maturity: draft
created: 2026-06-09
updated: 2026-06-09
---

## Relations

- @sources/trading-posts-compilation-7-2026-06-09.md — K107 Post 15 (@RohOnChain)
- @concepts/time-series-arima-garch-framework.md — K55 time-series stack (ARIMA/GARCH layer)
- @concepts/monte-carlo-permutation-test-mcpt.md — K56 significance gauntlet
- @concepts/regime-conditioned-evaluation.md — IC stability across regimes

## Raw Concept

Pedagogical framework from @RohOnChain (K107) for turning factor beliefs into testable alpha via OLS — single-factor then multi-factor (strip market/size/value/momentum before claiming intercept).

## Narrative

**Pipeline:** factor → OLS returns regression (always intercept) → intercept = candidate alpha → multi-factor strip → p-value / t-stat / IC / OOS / Newey-West / Bonferroni.

**Discipline highlights:**

- High R² on return prediction = red flag (look-ahead or tautology)
- Real signals often R² ~ 0.01–0.02 yet profitable if persistent
- Alpha decays as crowding rises — research engine > single signal

**Cemini posture:** REFERENCE for equity signal backtest cadence and PM factor research hygiene — pair with `scripts/run_equity_signal_backtest.sh` quarterly ritual [TENTATIVE 2026-06-09].

## Snippets

> "Alpha is the intercept that survives after every known risk factor is removed." [Source: Posts.docx K107 Post 15, @RohOnChain]

> "The quant staring at a Sharpe of 0.03 and a p-value of 0.62 is not unlucky. He skipped the discipline." [Source: Posts.docx K107 Post 15]
