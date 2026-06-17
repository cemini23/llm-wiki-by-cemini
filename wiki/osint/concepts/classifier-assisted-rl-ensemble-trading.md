---
title: Classifier-assisted RL ensemble trading — variance-threshold policy gating
type: concept
tags: [concept, reinforcement-learning, portfolio-management, ensemble, gating, k120]
keywords: [classifier-ensemble, variance-threshold, policy-gating, multi-agent-rl, trademaster, promotion-gate]
related:
  - sources/arxiv-ensemble-rl-classifier-models-2502-17518-2026-06-17.md
  - entities/tools/trademaster.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/stockbench.md
  - concepts/trading-model-failure-diagnostics.md
maturity: draft
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- @sources/arxiv-ensemble-rl-classifier-models-2502-17518-2026-06-17.md — K120 anchor source
- @entities/tools/trademaster.md — benchmark data dependency
- @concepts/regime-conditioned-evaluation.md — regime-split reporting for ensemble vs single policy
- @concepts/stockbench.md — multi-regime hot-swap gate pattern
- @concepts/trading-model-failure-diagnostics.md — promotion failure diagnostics

## Narrative

K120 paper (2502.17518) proposes using **supervised classifiers as a meta-policy** over multiple RL portfolio agents. Instead of averaging Q-values (which collapse diversity), the system:

1. Collects per-agent action confidence scores.
2. Computes variance across scores for each action.
3. Applies threshold **τ**: low variance → pick highest-confidence action; high variance on all actions → pick most conservative (lowest confidence).

**Why it matters for Cemini:** MAPPO / multi-policy equity sleeves already train several agents. This is a **cheap gating layer** between policies — no new RL training, only a rolling classifier with strict no-leakage calibration.

**Promotion discipline (steal-from):**

| Gate | Requirement |
|------|-------------|
| τ sensitivity | Report Sharpe/MDD across τ grid, not single best τ |
| Pair diversity | Ensemble only wins when base agents are both competent and disagree |
| Regime split | SSE50-style gains may not transfer to US watchlist |
| Leakage audit | Classifier fit window must end before traded block |

**Verdict:** **REFERENCE** pattern — laptop smoke via MIT reproduction repo; prod only after TradeMaster-equivalent backtest on Cemini equity panel with regime disclosure.

## Snippets

> "When all actions exhibit high variance, opt for a more conservative approach by choosing the action with the lowest confidence score." [Source: arxiv-2502.17518-ensemble-rl-through-classifier-models-enhancing.pdf §2]
