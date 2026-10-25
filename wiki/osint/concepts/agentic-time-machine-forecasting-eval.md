---
title: Agentic Time Machine — offline forecasting eval with leakage control
type: concept
tags: [concept, prediction-markets, polymarket, forecasting, multi-agent, k127]
keywords: [Agentic Time Machine, FutureX, offline replay, answer leakage, planner-solver-aggregator, Polymarket eval]
related:
  - sources/arxiv-agentic-time-machine-2606.21013-2026-06-23.md
  - concepts/polymarket-bot-architecture.md
  - concepts/prediction-market-information-leakage-score.md
  - concepts/sports-prediction-consensus-agent.md
  - concepts/llm-agent-systems.md
  - concepts/active-project-research-routing.md
maturity: draft
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- @sources/arxiv-agentic-time-machine-2606.21013-2026-06-23.md — primary source (Chai et al., SJTU)
- @concepts/polymarket-bot-architecture.md — PM retail bot eval hook
- @concepts/prediction-market-information-leakage-score.md — leakage scoring sibling

## Raw Concept

Prompted by arXiv **2606.21013** (K127). Forecasting agents need **dynamic web access** but retrospective eval suffers **answer leakage** when post-resolution content appears in tool results.

## Narrative

**Three eval paradigms:**

| Paradigm | Feedback | Web | Leakage risk |
|----------|----------|-----|--------------|
| Live (FutureX) | Slow | Dynamic | Low (real uncertainty) |
| Frozen DB replay | Fast | Static | Medium (stale env) |
| **Agentic Time Machine** | Fast | Dynamic | Low (cutoff filter) |

**TM mechanism:** wrap web tools with **post-cutoff content filter** at a chosen historical timestamp — simulates open web at prediction time.

**Planner-solver-aggregator:** question → diverse analytical angles → parallel evidence → aggregate forecast. Steal for PM bot **offline signal validation** before live CLOB deployment.

**Cemini use:** build laptop-side replay harness on resolved PM markets; correlate offline Brier/log score with paper's live-proxy claim before trusting multi-agent decomposition in prod briefs `[OPEN QUESTION 2026-06-23]`.

## Snippets

> "TM uniquely combines a fast feedback loop with dynamic, open-ended web interactions." [Source: arXiv:2606.21013 Figure 2 caption (retrieved 2026-06-23)]
