---
title: TradeMaster — RL quantitative trading platform (NTU, Apache-2.0)
type: entity
tags: [entity, tool, rl-trading, backtest, steal-from, apache-2, k60]
keywords: [trademaster, ntu, reinforcement-learning, prudex-compass, algorithmic-trading, steal-from]
related:
  - sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md
  - sources/arxiv-fpilot-rl-trading-2605-12653.md
  - concepts/polymarket-bot-architecture.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
---

## Relations

- @sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md — K60 URL 4 Steal-from
- @sources/arxiv-fpilot-rl-trading-2605-12653.md — cites TradeMaster DJ30 benchmark

## Raw Concept

K60 v4 eval: academic RL trading platform with market simulator + PRUDEX-Compass evaluation benchmark. **Steal-from** specific algorithms/patterns — not a framework replacement for LangGraph/FastAPI stack.

## Narrative

- **Repo**: [github.com/TradeMaster-NTU/TradeMaster](https://github.com/TradeMaster-NTU/TradeMaster) (~2.7k★, Apache-2.0 verified 2026-05-23)
- **Scope**: End-to-end RL trading — 15+ algorithms, high-fidelity simulator, standardized benchmarks
- **License**: Apache-2.0 — compatible with IP-sale extraction of isolated algorithm code [CONFIRMED]

### Verdict: **Steal-from (CONDITIONAL-GO for snippets)**

Harvest: backtest harness ideas, feature-selection / hyperparameter patterns, PRUDEX-Compass metrics for RL agent eval on cemini-prod. **Do not** replace PostgreSQL/Timescale + LangGraph orchestrator with TradeMaster monolith.

### Prod touchpoints (when scoped)

- `agents/orchestrator.py` RL retrain windows — compare reward shaping vs TradeMaster baselines
- Benchmark tables for internal briefs (already referenced in FPilot paper ingest)

### Phase-0

Clone to `/tmp/trademaster-audit/` if implementing extracts; verify no GPL transitive deps in chosen submodule.

## Snippets

> "Steal-from — extract strategy backtesting patterns… without adopting the broader platform overhead." [Source: GitHub Repo Evaluation for Cemini.docx, URL 4, 2026-05-23]
