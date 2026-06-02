---
title: "PortBench — LLM portfolio management benchmark (2605.27887)"
type: source
tags: [source, arxiv, quant-finance, benchmarking, llm, k94]
keywords: [portbench, portfolio management, correlation-aware, llm benchmark]
related:
  - sources/arxiv-alphaforgebench-2602-18481-2026-06-01.md
  - concepts/llm-alpha-factor-benchmarking.md
  - concepts/llm-portfolio-management-benchmarking.md
  - concepts/regime-adaptive-continual-portfolio-learning.md
  - sources/arxiv-regime-adaptive-portfolio-learning-2606-00143-2026-06-02.md
maturity: draft
read_status: read
created: 2026-06-02
updated: 2026-06-02
clusters: [quant-finance, ml-methods]
---

## Relations

- @concepts/llm-portfolio-management-benchmarking.md — synthesis
- @sources/arxiv-alphaforgebench-2602-18481-2026-06-01.md — complementary LLM×finance eval lane

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management |
| **Author** | Zhao, Chen, Su (HKUST-GZ et al.) |
| **arXiv ID** | 2605.27887 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2605.27887-portbench-a-correlation-aware-full-pipeline-benc.pdf` |
| **Retrieved** | 2026-06-02 |
| **Read status** | read (abstract) |

## Narrative

K94 digest. Argues PM benchmarks ignore **correlation structure**, **full pipeline** (signals → constraints → rebalance), and **investor risk tolerance** — gaps vs Markowitz-style PM.

**Cemini relevance:** evaluation primitive for any LLM-assisted portfolio research layer; not a trading-stack adopt. Large PDF (~24MB) — deep-read optional.

## Snippets

> "Portfolio management … remains poorly benchmarked. Existing benchmarks exhibit two main gaps: they ignore correlation …" [Source: arxiv-2605.27887…pdf, Abstract]
