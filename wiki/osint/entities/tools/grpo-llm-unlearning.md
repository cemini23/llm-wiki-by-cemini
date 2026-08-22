---
title: "grpo-llm-unlearning — Apache-2.0 Extract/REFERENCE (K245)"
type: entity
tags: [tool, unlearning, grpo, extract, k245]
keywords: [GRPO, RWKU, Balbastre, Apache-2.0]
related:
  - sources/arxiv-2608.17804-grpo-unlearning.md
  - concepts/harness-optimization-bench.md
maturity: draft
created: 2026-08-22
updated: 2026-08-22
wire_status: wont_wire
wire_note: "Phase-0 Extract/REFERENCE. 0 stars. Do not train unlearning in prod. Do not swap /route."
---

## Relations

- @sources/arxiv-2608.17804-grpo-unlearning.md — paper + four-reward diagnostic
- @concepts/harness-optimization-bench.md — reward/benchmark disagreement is a harness-eval problem

## Raw Concept

OSINT K245 Phase-0. Paper companion for 2608.17804. https://github.com/rubenbalbastre/grpo-llm-unlearning

## Narrative

| Field | Value |
|-------|--------|
| License | **Apache-2.0** [CONFIRMED `gh api` 2026-08-22] |
| Stars | 0 |
| Pushed | 2026-08-18 |
| Local clone | none this wave |
| Verdict | **Extract / REFERENCE** — **0 Integrate GO** |
| wire_status | `wont_wire` |

Code and W&B/HF artifacts for a controlled LoRA-GRPO unlearning study (Qwen2.5-Instruct, RWKU, four reward specs). Useful as a **negative example**: RWKU forget scores can look “successful” while the behavioral endpoint is refusal collapse or classifier hacking.

Do not adopt as a Cemini unlearning trainer. Do not copy reward prompts into prod. CCC may cite the diagnostic pattern (held-out audit required). Phase-1 leftover: none to wire in `.cursor/skills`.

## Snippets

> license.spdx_id = Apache-2.0 [Source: `gh api repos/rubenbalbastre/grpo-llm-unlearning` 2026-08-22]
