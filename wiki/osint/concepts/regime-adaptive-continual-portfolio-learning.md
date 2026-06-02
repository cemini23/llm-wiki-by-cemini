---
title: Regime-adaptive continual learning for portfolio management
type: concept
tags: [concept, quant-finance, regime, continual-learning, k94]
keywords: [regime shift, continual learning, non-stationary markets, portfolio]
related:
  - sources/arxiv-regime-adaptive-portfolio-learning-2606-00143-2026-06-02.md
  - concepts/regime-conditioned-evaluation.md
  - sources/arxiv-portbench-llm-portfolio-2605-27887-2026-06-02.md
maturity: draft
created: 2026-06-02
updated: 2026-06-02
---

## Relations

- @concepts/regime-conditioned-evaluation.md — Conductor/backtest regime disclosure
- @sources/arxiv-regime-adaptive-portfolio-learning-2606-00143-2026-06-02.md

## Narrative

Markets are **non-stationary**; static PM policies trained on one regime degrade. Paper (2606.00143) proposes **regime-adaptive continual learning** for portfolio policies — update as regimes shift rather than one-shot fit.

**Cemini relevance:** motivates quarterly backtest cadence and explicit regime tags in evaluation — aligns with `@concepts/regime-conditioned-evaluation.md` (traffic-mix / regime disclosure for routing policies).
