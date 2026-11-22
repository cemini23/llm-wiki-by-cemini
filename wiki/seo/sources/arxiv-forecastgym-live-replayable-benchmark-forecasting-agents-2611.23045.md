---
title: "ForecastGym forecasting-agent benchmark — no SEO link, recorded for inventory"
type: source
related:
  - concepts/corpus-overflow-out-of-scope.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents |
| Authors | Yicheng Tao, Yuante Li (Carnegie Mellon University); Zipei Fan (Jilin University) |
| arXiv | 2611.23045 |
| Pages | 12 |
| File | `arxiv-2611.23045-forecastgym-a-live-controlled-and-replayable-ben.pdf` |
| Location | `research to be indexed/seo/arxiv-2611.23045-forecastgym-a-live-controlled-and-replayable-ben.pdf` |
| Retrieved | 2026-11-22 |
| Read status | read |

## Narrative

**No SEO link.** This paper studies forecasting agents on prediction markets. It has no connection to search engines, retrieval visibility, citation, or local ranking. The page exists for inventory honesty and links from @concepts/corpus-overflow-out-of-scope.md.

The authors build a benchmark for agents that forecast real-world events by searching the web. A forecast depends on both the evidence and the model, so the benchmark freezes the evidence. ForecastGym records what four commercial search APIs return for open prediction-market questions every two days. It replays this frozen evidence offline after outcomes are known.

The first release covers 150 questions, 614 evidence states, and 131k search results. Rerunning the same queries after settlement returns results that nearly state the outcome for up to 92% of the questions, even with date filters. On the frozen evidence, all tested LLMs trail the market in forecasting accuracy. Switching the search API changes a model's Brier score by up to 0.043, which is more than the spread across models. The authors conclude that the evidence a forecaster sees can matter as much as the model. The numbers are single-source claims.

## Snippets

> "The evidence a forecaster sees can matter as much as the model that reads it." [Source: `arxiv-2611.23045-forecastgym-a-live-controlled-and-replayable-ben.pdf` p.1 (arXiv 2611.23045), retrieved 2026-11-22]
