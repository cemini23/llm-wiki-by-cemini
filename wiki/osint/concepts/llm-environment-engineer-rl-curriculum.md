---
title: LLM environment engineer — RL curriculum loop
type: concept
tags: [concept, llm-agents, rl, curriculum, k124]
keywords: [environment engineer, Trainee-to-Trainer, MAPF, GRPO, failure-driven curriculum]
related:
  - sources/arxiv-trainee-to-trainer-2606.17682-2026-06-20.md
  - entities/tools/trainee-to-trainer.md
  - concepts/llm-agent-systems.md
  - concepts/continual-harness-online-self-improvement.md
  - entities/tools/spade.md
  - sources/arxiv-2608.19197-spade-2026-08-20.md
maturity: draft
created: 2026-06-20
updated: 2026-08-20
---

## Relations

- @sources/arxiv-trainee-to-trainer-2606.17682-2026-06-20.md — primary source
- @entities/tools/trainee-to-trainer.md — tool entity + Phase-0
- @concepts/continual-harness-online-self-improvement.md — online improvement sibling (harness vs env config)

## Raw Concept

Prompted by arXiv **2606.17682** (K124). Shifts self-improvement from **task/response space** to **environment configuration space**: the trained checkpoint redesigns the generator that produces next-round training instances.

## Narrative

**Loop:** train policy on `D_n` → validate → compose context (failures, history, guidelines) → checkpoint proposes `C_{n+1}` → generator emits `D_{n+1}`.

**Design insight:** failure breakdown + config history beats guideline-only context; preserve working dimensions when patching failures.

**Castle-sim steal:** HL analyst or Stagehand session reads playtest failure clusters (pathing stalls, siege AI leaks) and proposes next **regression scenario mix** (map size, wall density, raid timing) — analog to MAPF hole/wait ratios.

**Poker steal:** trajectory export identifies recurring leak buckets (SB defend, 3-bet fold frequency); environment engineer proposes next **regression_spots.py** weighting — offline, not runtime LLM.

**Posture:** **CONDITIONAL-GO** on repo (`NOASSERTION` license); pattern REFERENCE until SPDX verified.

## Snippets

> "Successful environment updates rely on failure evidence and preserve configurations that already work." [Source: arXiv:2606.17682 abstract (retrieved 2026-06-20)]

## Dead Ends

- Full MAPF-FrozenLake stack not portable to PokerKit — config schema differs entirely.
