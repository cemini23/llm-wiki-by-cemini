---
title: CodeHack — code-based skill library for language agents
type: entity
tags: [entity, tool, harness, agents, skills, phase-0]
keywords: [codehack, nethack, skill-library, primitives, mit]
related:
  - sources/arxiv-2609.31076-abstraction-ladder-code-skills-2026-09-30.md
  - concepts/agent-harness-castle-project.md
  - entities/tools/gamedevbench.md
  - sources/inbox-arxiv-reject-batch-2026-09-30.md
maturity: validated
created: 2026-09-30
updated: 2026-09-30
wire_status: policy_wired
wire_target: concepts/agent-harness-castle-project.md
---

## Relations

- Paper: [arXiv:2609.31076](https://arxiv.org/abs/2609.31076)
- GitHub: [BartekCupial/codehack](https://github.com/BartekCupial/codehack)
- Baselines: [BartekCupial/codehack-baselines](https://github.com/BartekCupial/codehack-baselines)
- Project page: [bartekcupial.github.io/abstraction-ladder](https://bartekcupial.github.io/abstraction-ladder/)

## Raw Concept

A library of code-based skills with natural-language descriptions, released with the abstraction-ladder paper. Agents invoke named skills instead of selecting every primitive action. The study measures the effect on progression, inference cost, and learning in NetHack.

## Narrative

### Phase-0 verdict (2026-09-30)

| Check | Result |
|-------|--------|
| SPDX / LICENSE | **MIT** (`LICENSE` at repo root) |
| Maturity | Research release, 2★ — early |
| Verdict | **CONDITIONAL-GO** — clone permitted; **STEAL-FROM** the design pattern |

### Measured effect (from the paper)

| Metric | Result |
|--------|--------|
| Game progression | ~3x versus primitives |
| Inference cost per episode | −86% |
| RL dungeon-level gain | 7.2x larger over the same budget |
| Skills + primitives | keeps most of the benefit, preserves fallback |

### castle-sim mapping

The transferable rule for @concepts/agent-harness-castle-project.md: give agents named high-level operations (build wall segment, place granary, run smoke scene) instead of raw editor calls, and keep primitive fallback. The NetHack environment itself is not portable to Godot.

## Dead Ends

- Vendoring NetHack-specific skills into a Godot project.
- Skills-only agents with no primitive fallback.
