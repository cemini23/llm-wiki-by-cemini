---
title: Regime-adaptive continual learning for portfolio management
type: concept
tags: [concept, quant-finance, regime, continual-learning, k94]
keywords: [regime shift, continual learning, non-stationary markets, portfolio]
related:
  - sources/arxiv-regime-adaptive-portfolio-learning-2606-00143-2026-06-02.md
  - concepts/regime-conditioned-evaluation.md
  - sources/arxiv-portbench-llm-portfolio-2605-27887-2026-06-02.md
  - sources/arxiv-bavar-bled-portfolio-regime-2606-09104-2026-06-09.md
  - concepts/heuristic-portfolio-optimization-hpo.md
maturity: draft
created: 2026-06-02
updated: 2026-06-17
---

## Relations

- @concepts/regime-conditioned-evaluation.md — Conductor/backtest regime disclosure
- @sources/arxiv-regime-adaptive-portfolio-learning-2606-00143-2026-06-02.md
- @concepts/heuristic-portfolio-optimization-hpo.md — K120 RLPO bridge: dynamic layer on static HPO prior

## Narrative

Markets are **non-stationary**; static PM policies trained on one regime degrade. Paper (2606.00143) proposes **regime-adaptive continual learning** for portfolio policies — update as regimes shift rather than one-shot fit.

**Cemini relevance:** motivates quarterly backtest cadence and explicit regime tags in evaluation — aligns with `@concepts/regime-conditioned-evaluation.md` (traffic-mix / regime disclosure for routing policies).
