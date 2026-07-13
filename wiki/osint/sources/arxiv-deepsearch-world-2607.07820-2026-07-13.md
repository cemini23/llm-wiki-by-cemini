---
title: DeepSearch-World — self-distillation for deep search agents (2607.07820)
type: source
tags: [source, arxiv, web-agents, self-distillation, k161]
keywords: [DeepSearch-World, DeepSearch-Evolve, BrowseComp, GAIA, HotpotQA, verifiable environment]
clusters: [k161-ingest, agent-harness]
related:
  - concepts/deepsearch-world-self-evolution.md
  - concepts/continual-harness-online-self-improvement.md
  - sources/arxiv-hierarchical-memory-ensemble-qsp-2607.07666-2026-07-13.md
maturity: validated
read_status: deep-read
created: 2026-07-13
updated: 2026-07-13
---

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.07820](https://arxiv.org/abs/2607.07820) |
| **sha256** | `8a160004267c01fe…` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.07820-2607-07820v1-deepsearch-world-self-distillation.pdf` |
| **Authors** | Geng et al. (HKUST / Tencent) |
| **Code/Data** | Promised release (env + 420K pool + 9B model) — **not yet on GitHub at ingest** |

## Relations

- @concepts/deepsearch-world-self-evolution.md — K161 concept
- @concepts/continual-harness-online-self-improvement.md — self-evolve without teacher distill

## Narrative

**DeepSearch-World** — deterministic, verifiable environment for deep-search web agents (reproducible search + page-reading tools). **420K** multi-hop QA tasks from entity-level random walks; supports progress verification, grounded reflection, failure recovery.

**DeepSearch-Evolve** — iterative self-distillation: trajectory generation → filtering → data mixing → fine-tuning. **No distillation from stronger teachers.** DeepSearch-World-9B: **31.2%** BrowseComp, **61.5%** GAIA, **93.4%** HotpotQA.

**Cemini steal:** poker sandbox + CCC research agents — verifiable env + trajectory filter/mix beats sparse RL or static SFT for long-horizon tool use. **Phase-0 Watch** until code/data land; no Adopt.

## Snippets

> "Without distillation from more capable models, DeepSearch-World-9B achieves … 31.2% on BrowseComp, 61.5% on GAIA, and 93.4% on HotpotQA" [Source: arXiv:2607.07820 abstract]
