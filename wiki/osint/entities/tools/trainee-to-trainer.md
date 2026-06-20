---
title: Trainee-to-Trainer (LARK-AI-Lab)
type: entity
tags: [entity, tool, rl, llm-agents, k124]
keywords: [Trainee-to-Trainer, MAPF, environment engineer, LARK, GRPO]
related:
  - sources/arxiv-trainee-to-trainer-2606.17682-2026-06-20.md
  - concepts/llm-environment-engineer-rl-curriculum.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @sources/arxiv-trainee-to-trainer-2606.17682-2026-06-20.md — arXiv source
- @concepts/llm-environment-engineer-rl-curriculum.md — pattern synthesis

## Raw Concept

Phase-0 audit entity for **Trainee-to-Trainer** (arXiv 2606.17682). LLM-designed RL environment configuration loop with MAPF-FrozenLake testbed.

## Narrative

| Signal | Value (2026-06-20) |
|--------|---------------------|
| Repo | https://github.com/LARK-AI-Lab/Trainee-to-Trainer |
| License | **NOASSERTION** (gh api) — not Adopt |
| Stars / pushed | 19 / 2026-06-15 |
| Weights | HuggingFace `LARK-Lab/Trainee2Trainer/` |

**Verdict:** **CONDITIONAL-GO** — steal environment-engineer loop; revisit when SPDX license file lands. Failure mode checked: hardcoded MAPF domain (expected — pattern steal only, no install).

## Snippets

> Phase-0: `bash scripts/adopt_k124_phase0.sh`

## Dead Ends

- Do not clone into CeminiSuite — wrong domain (grid MAPF vs trading/poker).
