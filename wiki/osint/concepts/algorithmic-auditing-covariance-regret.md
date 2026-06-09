---
title: "Algorithmic auditing via covariance regret decomposition"
type: concept
tags: [concept, algorithmic-auditing, portfolio, evaluation, k107]
keywords: [covariance-regret, black-box-audit, trajectory-estimator, hac, welfare-metric, external-review]
related:
  - sources/arxiv-covariance-regret-algorithmic-audit-2606-08791-2026-06-09.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/brier-score-model-promotion-framework.md
  - concepts/trading-model-failure-diagnostics.md
maturity: draft
created: 2026-06-09
updated: 2026-06-09
---

## Relations

- @sources/arxiv-covariance-regret-algorithmic-audit-2606-08791-2026-06-09.md — K107 anchor (Aldridge 2026)
- @concepts/regime-conditioned-evaluation.md — regime disclosure for fair ATE/CATE comparisons
- @concepts/monte-carlo-permutation-test-mcpt.md — permutation significance for factor claims
- @concepts/trading-model-failure-diagnostics.md — internal zero-trade / shadow diagnostics

## Raw Concept

External audit of sequential decision systems (strategies, bots, platform mechanisms) using only observed cost vectors and action trajectories — no access to private state or model weights.

## Narrative

When i.i.d. cost shocks and mean-unbiased Markov policies hold, **cumulative regret equals summed cov(cost, action)** — turning black-box performance review into a tractable O(T·nd) statistic with HAC confidence bands.

**Cemini use cases:**

1. **Shadow bot promotion** — compare shadow fill stream vs baseline without opening strategy code to external reviewers [TENTATIVE]
2. **Vendor signal audit** — third-party PM/crypto signals: measure covariance regret vs naive benchmark before capital allocation
3. **Cross-check internal backtests** — if internal Sharpe high but covariance regret vs factor exposure large → investigate overfit or hidden leverage

**Not a substitute for:** MCPT, walk-forward splits, regime-conditioned tables, or EMS/RBAC gates.

## Snippets

> "Model-free audit tool for platform mechanisms, algorithmic portfolio strategies, and any sequential decision system subject to external performance review." [Source: arxiv-2606-08791 Abstract]
