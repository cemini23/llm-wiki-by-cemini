---
title: OpenClaw-RL — async RL from agent interaction traces
type: entity
tags: [entity, tool, rl, openclaw, k137]
keywords: [OpenClaw-RL, Gen-Verse, reinforcement learning, on-policy distillation, binary RL, Apache-2.0]
related:
  - sources/eval-multi-wiki-openclaw-ecosystem-2026-06-30.md
  - entities/tools/openclaw.md
  - concepts/rl-marl-research.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-06-30
updated: 2026-06-30
---

## Relations

- @entities/tools/openclaw.md — OpenClaw gateway context; Tier C prod NO-GO unchanged
- @concepts/rl-marl-research.md — MARL corpus index

## Raw Concept

K137 Phase-0 on [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) — Apache-2.0 framework for **async RL** from real agent interaction signals (Hybrid RL: Binary RL + on-policy distillation).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `Gen-Verse/OpenClaw-RL` |
| **License** | **Apache-2.0** (`gh api` 2026-06-30) |
| **Stars / pushed** | ~5.5k★; pushed 2026-05-23 |
| **Stack** | Python, Ray, vLLM |
| **Verdict** | **Adopt** (wiki + optional laptop spike; **not** cemini-prod trading path without review) |
| **Steal** | Interaction-trace → policy gradient loop without manual annotation |

**Posture:** reference Adopt for PM bot **offline** tuning research — do not wire to cemini-prod Lane A without separate security review. SGLang/Ray topology compatibility `[NEEDS VERIFICATION 2026-06-30]`.

## Snippets

> "Fully asynchronous reinforcement learning … without relying on expensive manual annotation." [Source: eval docx URL 18, 2026-06-30; Apache-2.0 gh verified]
