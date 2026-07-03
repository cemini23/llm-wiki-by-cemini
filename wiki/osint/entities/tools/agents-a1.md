---
title: Agents-A1 — InternScience long-horizon agent model
type: entity
tags: [entity, tool, llm, osint, k141]
keywords: [Agents-A1, InternScience, qwen3.5 MoE, long-horizon, Apache-2.0]
related:
  - sources/eval-huggingface-models-v2-2026-07-03.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/eval-huggingface-models-v2-2026-07-03.md — K141 Adopt row

## Raw Concept

K141 eval of [InternScience/Agents-A1](https://huggingface.co/InternScience/Agents-A1) — trajectory-scaling agent model (45K-token execution traces).

## Narrative

| Field | Value |
|-------|-------|
| **HF** | `InternScience/Agents-A1` |
| **License** | **Apache-2.0** (docx; linked gh repo) |
| **Stars** | ~219★ on gh org repo |
| **Verdict** | **Adopt** — OSINT deep-research / multi-constraint gather reference |
| **Steal** | Long-horizon verify trajectories; external KB + code interpreter pairing |

Wiki-only — no prod brief unless user reopens deep-research lane.

## Snippets

> "Natively generating execution and verification trajectories up to 45K tokens." [Source: Hugging Face Model Evaluation 2.docx URL 10 (retrieved 2026-07-03)]
