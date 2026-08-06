---
title: "arXiv 2608.05086 — Item Response Theory for AI safety benchmarks"
type: source
tags: [arxiv, ai-safety, evaluation, irt, k225]
keywords: [IRT, item response theory, safety benchmark, compression]
related:
  - concepts/irt-ai-safety-benchmark-compression.md
  - sources/arxiv-2608.04698-mllm-refusal-calibrated-grpo-2026-08-06.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
read_status: skimmed
---

## Relations

- @concepts/irt-ai-safety-benchmark-compression.md
- @sources/arxiv-2608.04698-mllm-refusal-calibrated-grpo-2026-08-06.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Item Response Theory for AI Safety |
| arXiv | 2608.05086 |
| sha256 | `163d67ff918b5b91607cb98b6f41f69e39d4d5342e60610c1e8727b6fea1ad3a` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.05086-item-response-theory-for-ai-safety.pdf` |
| retrieved | 2026-08-06 |
| read_status | skimmed |

## Narrative

Applies **Item Response Theory (IRT)** to AI safety evaluations: treat benchmark items as having difficulty/discrimination parameters; compress large safety suites to informative subsets; reduce redundant eval cost while preserving model ranking signal.

**Cemini steal:** Before running expensive multi-model safety sweeps on agent harness changes (Atto tool policies, GW fetch agents), use IRT-style item selection — pairs K242 deterministic verify but for **benchmark design**, not runtime.

**Phase-0:** REFERENCE — no install.

## Snippets

> IRT models which safety items actually discriminate model behavior versus adding noise. [Source: arxiv-2608.05086-item-response-theory-for-ai-safety.pdf — skim]
