---
title: "Frontier Financial Judgement (arXiv 2607.20645)"
type: source
tags: [source, arxiv, equity, agents, news-flow, k193, xsp]
keywords: [Frontier Financial Judgement, valuation-relevant news, false-positive, equity analyst]
related:
  - concepts/frontier-financial-judgement.md
  - concepts/xsp-lane-trading-framework.md
  - sources/substack-rss-capital-flows-2026-07-24-sp500-selling.md
maturity: draft
read_status: read
created: 2026-07-24
updated: 2026-07-24
clusters: [k193-ingest]
---

## Relations

- @concepts/frontier-financial-judgement.md
- @concepts/xsp-lane-trading-framework.md
- @sources/substack-rss-capital-flows-2026-07-24-sp500-selling.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `arxiv-2607.20645-frontier-financial-judgement-can-agents-tell-wha.pdf` |
| **sha256** | `985d068078e8057d273760025985a8817ec61a143712345c7f1091255195f63d` |
| **arXiv** | [2607.20645](https://arxiv.org/abs/2607.20645) |
| **Authors** | Sonto / Joshua Harris |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.20645-frontier-financial-judgement-can-agents-tell-wha.pdf` |

## Narrative

Benchmark for whether agents can flag **valuation-relevant** equity news vs stale/immaterial/misleading flow (656 items; analyst-labeled + live news mix). Best agent matches all expert labels in only **52.4%** of cases. False-positive rates diverge hard (~1% GPT-5.6 Sol vs ~32% Claude Sonnet 4.6). Cost–accuracy Pareto continues to block reliable news-flow filtering for buy-side coverage.

**Steal for XSP / intel:** treat agent news filters as high-FP risk; require explicit FP/FN gates before any auto-trade or alert escalation; prefer low-FP models even at lower all-label accuracy.

## Snippets

> "The strongest agent we evaluate on Frontier Financial Judgement matches all expert labels in only 52.4% of cases."
