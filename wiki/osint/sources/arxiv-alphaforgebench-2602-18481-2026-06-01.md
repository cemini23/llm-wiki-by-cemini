---
title: "AlphaForgeBench — LLM alpha-factor benchmarking (2602.18481)"
type: source
tags: [source, arxiv, quant-finance, llm, benchmarking, k92]
keywords: [alphaforgebench, llm trading agents, alpha factors, reproducibility, kdd-2026]
related:
  - concepts/llm-alpha-factor-benchmarking.md
  - concepts/llm-agent-systems.md
  - concepts/high-signal-paper-patterns.md
  - sources/arxiv-signal-adaptive-execution-2605-24242-2026-06-01.md
  - concepts/llm-portfolio-management-benchmarking.md
  - sources/arxiv-llm-robust-portfolio-optimization-2605-27013-2026-06-02.md
  - sources/arxiv-portbench-llm-portfolio-2605-27887-2026-06-02.md
maturity: draft
read_status: read
created: 2026-06-01
updated: 2026-06-02
clusters: [quant-finance, ml-methods, agent-harness]
---

## Relations

- @concepts/llm-alpha-factor-benchmarking.md — synthesis hub
- @sources/arxiv-signal-adaptive-execution-2605-24242-2026-06-01.md — K92 microstructure pair (execution quoting)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AlphaForgeBench: Benchmarking End-to-End Trading Strategy Design with Large Language Models |
| **Author** | Zhang et al. (NTU, HKUST-GZ, PolyU) |
| **Type** | PDF (arXiv / KDD'26) |
| **arXiv ID** | 2602.18481 |
| **DOI** | 10.1145/3770855.3817500 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2602.18481-alphaforgebench-benchmarking-end-to-end-trading.pdf` |
| **Retrieved** | 2026-06-01 |
| **Read status** | read (abstract + introduction) |

## Narrative

K92 daily-digest fetch. The paper argues that **LLMs as direct sequential trading agents** are a bad evaluation target: run-to-run variance, action flipping, and stateless autoregression break reproducibility of online trading benchmarks.

**AlphaForgeBench** reframes the task: models produce **executable alpha factors** and compose factor strategies (quant-researcher role), decoupling reasoning from discrete action mapping. Evaluation becomes deterministic and closer to buy-side workflow.

**Cemini relevance:** supports Conductor/Cemini posture that LLMs belong in **research and factor codegen**, not unguarded live order emission. Complements @concepts/llm-agent-systems.md debate-termination and IP-sale “LLM as research layer” framing. Not a deployment adopt — a **benchmark primitive** for any future LLM-assisted alpha pipeline.

## Snippets

> "When deployed as direct trading agents, LLMs manifest extreme run-to-run variance … even under strictly deterministic decoding configurations." [Source: arxiv-2602.18481-alphaforgebench.pdf, Abstract]

> "AlphaForgeBench tasks LLMs with generating executable alpha factors … decoupling reasoning from execution mechanics." [Source: arxiv-2602.18481-alphaforgebench.pdf, Abstract]

## Dead Ends

- Using raw LLM portfolio actions as a prod trading signal without a deterministic execution layer — paper treats this as pathological.
