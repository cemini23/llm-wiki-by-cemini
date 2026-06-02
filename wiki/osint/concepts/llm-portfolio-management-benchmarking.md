---
title: LLM portfolio management benchmarking (PortBench lane)
type: concept
tags: [concept, quant-finance, benchmarking, llm, k94]
keywords: [portbench, portfolio management, correlation-aware, full-pipeline benchmark]
related:
  - sources/arxiv-portbench-llm-portfolio-2605-27887-2026-06-02.md
  - sources/arxiv-alphaforgebench-2602-18481-2026-06-01.md
  - concepts/llm-alpha-factor-benchmarking.md
maturity: draft
created: 2026-06-02
updated: 2026-06-02
---

## Relations

- @sources/arxiv-portbench-llm-portfolio-2605-27887-2026-06-02.md
- @concepts/llm-alpha-factor-benchmarking.md — factor codegen vs full PM pipeline

## Narrative

**PortBench** (2605.27887) argues LLM finance benchmarks under-specify **portfolio management**: they skip correlation-aware multi-asset construction, investor risk constraints, and end-to-end pipeline fidelity.

**Cemini posture:** use PM benchmarks to evaluate research agents and factor pipelines — not to bless direct LLM order placement. Pairs with AlphaForgeBench (alpha factors) and regime-adaptive PM learning (2606.00143).
