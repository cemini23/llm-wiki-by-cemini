---
title: "pandas-ta-classic — Technical Analysis Indicator Library"
type: entity
tags: [tool, trading, technical-analysis, python, pandas, indicators]
keywords: [pandas-ta, technical indicators, OHLCV, candlestick patterns, Polars bridge, quantitative finance]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 2)

## Raw Concept

Community-maintained fork of the pandas-ta technical analysis library. Provides 200+ calculated indicators and 62 candlestick patterns as Pandas DataFrame extensions. Evaluated in the Trading & Wiki Stacks brief and recommended for **Adopt**.

- **Repo**: `github.com/xgboosted/pandas-ta-classic`
- **License**: To verify (community fork — need to confirm)
- **Stack**: Python, Pandas-native

## Narrative

Pandas TA Classic extends Pandas DataFrames with technical indicator calculations consuming OHLCV time-series data. The library functions as both an indicator factory and a mathematical reference dictionary for algorithmic trading strategies.

### Integration vectors

- **Cemini prod (Adopt)**: Extend `agents/orchestrator.py` calculation nodes. Requires Pandas↔Polars bridging — the Cemini stack uses Polars for memory efficiency; this library requires Pandas DataFrames. Serialization overhead must be profiled.
- **Workflow (Adopt)**: Use native Python implementations as ground-truth reference for esoteric indicator construction, cross-referencing against LLM-generated code to prevent hallucinations.

### Risks

- **Pandas↔Polars bridge latency**: Continuous DataFrame casting in a 24/7 trading loop may introduce unacceptable latency at sub-millisecond timescales
- **Community fork viability**: Must verify commit velocity and contributor count vs predecessor projects

### Open questions

- Exact latency penalty and memory allocation spikes from continuous Polars↔Pandas casting in sustained 24/7 ingestion loop `[NEEDS VERIFICATION 2026-05-10]`
- Current GitHub star count and primary contributor velocity `[NEEDS VERIFICATION 2026-05-10]`

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 2]
