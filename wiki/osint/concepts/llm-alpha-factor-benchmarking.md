---
title: LLM alpha-factor benchmarking (vs direct trading agents)
type: concept
tags: [concept, quant-finance, llm, benchmarking]
keywords: [alphaforgebench, factor generation, reproducibility, llm trading]
related:
  - sources/arxiv-alphaforgebench-2602-18481-2026-06-01.md
  - concepts/llm-agent-systems.md
  - concepts/high-signal-paper-patterns.md
  - concepts/high-signal-paper-patterns.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @sources/arxiv-alphaforgebench-2602-18481-2026-06-01.md — K92 ingest

## Raw Concept

Prompted by K92 ingest of AlphaForgeBench (2602.18481): how to evaluate LLMs on trading tasks without conflating **reasoning** with **stochastic execution**.

## Narrative

**Problem:** Benchmarks that score LLMs on discrete trade actions inherit pathological variance (non-reproducible policies, action flipping) from stateless autoregressive decoding and continuous→discrete portfolio mappings.

**Pattern:** Evaluate LLMs as **quant researchers** — emit factors / strategy code, run deterministic backtests. AlphaForgeBench is the reference design.

**Cemini rule of thumb:** LLM → hypothesis and code; execution engine → orders. Aligns with @concepts/llm-agent-systems.md and prod boundary in CLAUDE.md.

## Snippets

- AlphaForgeBench: LLM generates executable alpha factors; evaluation reproducible. [Source: arxiv-2602.18481, Abstract]
