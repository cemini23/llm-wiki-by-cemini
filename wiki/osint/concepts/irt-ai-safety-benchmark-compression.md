---
title: "IRT compression for AI safety benchmarks"
type: concept
tags: [ai-safety, evaluation, irt, k225]
keywords: [item response theory, benchmark compression, safety eval]
related:
  - sources/arxiv-2608.05086-irt-ai-safety-2026-08-06.md
  - sources/arxiv-2608.04698-mllm-refusal-calibrated-grpo-2026-08-06.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- @sources/arxiv-2608.05086-irt-ai-safety-2026-08-06.md
- @sources/arxiv-2608.04698-mllm-refusal-calibrated-grpo-2026-08-06.md — refusal calibration (different lever)
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

arXiv 2608.05086 — apply **Item Response Theory** to select discriminative safety benchmark items; reduce eval cost without losing model ranking power.

## Narrative

Full safety suites are expensive for every harness change (Atto tool policies, GW fetch parsers, MCP canary audits K250). IRT treats each prompt/item as having difficulty + discrimination parameters — drop items that don't separate models.

**Cemini use:** Before multi-model agent eval campaigns, run **item analysis** on a calibration subset; freeze a compressed panel for regression gates. Pairs K242 deterministic verify (runtime) with **benchmark design** (offline). Not a substitute for execution-fidelity checks on irreversible writes (K239).

**Status:** `[TENTATIVE]` — single paper; pilot on internal canary suite before claiming cost savings.

## Snippets

> Do not use raw LLM over full safety CSV tables as primary analytics — use classical/IRT tooling; LLM for narrative. [Pairs K241]
