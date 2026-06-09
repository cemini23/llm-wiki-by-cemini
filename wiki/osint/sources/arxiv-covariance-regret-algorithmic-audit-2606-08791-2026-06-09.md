---
title: "Evaluating AI Investment Strategies — Covariance Regret Audit (arXiv 2606.08791, Aldridge 2026)"
type: source
tags: [source, algorithmic-auditing, portfolio, regret, k107]
keywords: [covariance-regret, black-box-audit, dynamic-programming, hac-variance, momentum-strategies, welfare-audit]
related:
  - concepts/algorithmic-auditing-covariance-regret.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/brier-score-model-promotion-framework.md
  - sources/ssrn-knuteson-overnight-intraday-4619084-2026-06-07.md
maturity: draft
read_status: read
created: 2026-06-09
updated: 2026-06-09
clusters: [quant-finance, portfolio-strategy]
---

## Relations

- @concepts/algorithmic-auditing-covariance-regret.md — primary concept
- @concepts/regime-conditioned-evaluation.md — external audit without model access
- @concepts/monte-carlo-permutation-test-mcpt.md — sibling significance discipline (K56)
- @concepts/brier-score-model-promotion-framework.md — promotion gates

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Evaluating AI Investment Strategies |
| **Author** | Irene Aldridge |
| **arXiv** | 2606.08791 |
| **PDF** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-covariance-regret-algorithmic-audit-2606-08791-2026-06-09.pdf` |
| **Retrieved** | 2026-06-09 |
| **Read status** | read (abstract + TOC + §10 financial apps skim) |

## Narrative

Model-free **algorithmic auditing** from observable inputs/outputs only. Main result: under i.i.d. costs and mean-unbiased Markov policies, cumulative dynamic regret decomposes exactly into sum of per-period **cov(cost, decision)** — extends Aldridge (2026) single-period identity to multi-period SDP.

Delivers bias corrections for non-stationarity, discounted horizon, Bellman recursion for covariance regret, HAC-consistent trajectory estimator in O(T·nd) time. Financial apps: rolling-window rebalancing, mean-reverting execution costs.

**Cemini posture:** **REFERENCE** for prod strategy review — external audit metric when only fills/PnL traces available (shadow bots, third-party signal vendors). Complements MCPT + regime-conditioned eval; not a replacement for internal backtest oracles [TENTATIVE 2026-06-09].

## Snippets

> "The decomposition has direct implications for algorithmic auditing in strategic environments… a welfare-based audit metric without access to the agent's private type." [Source: arxiv-2606-08791-evaluating-ai-investment-strategies.pdf Abstract]

> "For rolling-window policies, the estimation-error bias is O(d/w)." [Source: arxiv-2606-08791-evaluating-ai-investment-strategies.pdf Abstract]
