---
title: "arXiv 2608.04698 — RC-GRPO / GREC refusal calibration for MLLMs"
type: source
tags: [arxiv, alignment, mllm, rl, k225]
keywords: [RC-GRPO, GREC, refusal, GRPO, multimodal]
related:
  - concepts/irt-ai-safety-benchmark-compression.md
  - concepts/wiki-tooling-evaluation.md
  - sources/arxiv-2608.05086-irt-ai-safety-2026-08-06.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
read_status: skimmed
---

## Relations

- @concepts/irt-ai-safety-benchmark-compression.md — complementary safety-eval framing
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Teaching MLLMs to Say No: Generalized Referring Expression Comprehension (GREC) |
| arXiv | 2608.04698 |
| sha256 | `2e8549d016a851c1f61751ac2b0932e0bcc154c6b35001d2313c3169cfc3558d` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.04698-teaching-mllms-to-say-no-generalized-referring-e.pdf` |
| retrieved | 2026-08-06 |
| read_status | skimmed |

## Narrative

Proposes **GREC** — a refusal-aware task formulation for multimodal LLMs — and **RC-GRPO** (Refusal-Calibrated Group Relative Policy Optimization) to train models to decline invalid or unsafe referring expressions instead of hallucinating targets.

**Cemini posture:** `[TENTATIVE]` policy pattern only — no runtime wire. Relevant when evaluating vision+tool agents (Atto doc QA, GW screenshot parsers): prefer calibrated refusal over confident wrong answers. Pairs with safety-bench compression work (@concepts/irt-ai-safety-benchmark-compression.md) but different mechanism (RL refusal vs IRT item selection).

**Phase-0:** REFERENCE paper — no clone.

## Snippets

> RC-GRPO calibrates refusal behavior during GRPO-style RL on generalized referring expression tasks. [Source: arxiv-2608.04698-teaching-mllms-to-say-no-generalized-referring-e.pdf — skim]
