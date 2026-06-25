---
title: SCOPE — evolving symbolic world for open-ended planning
type: concept
tags: [concept, planning, embodied-ai, castle-sim, game-dev, k129]
keywords: [SCOPE, SESim, SASMem, symbolic world, VLM planner, open-ended environments]
related:
  - sources/arxiv-scope-symbolic-world-planning-2606.22488-2026-06-25.md
  - concepts/castle-sim-pathfinding-steals.md
  - concepts/active-project-research-routing.md
  - concepts/llm-environment-engineer-rl-curriculum.md
maturity: draft
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- @sources/arxiv-scope-symbolic-world-planning-2606.22488-2026-06-25.md — primary source (arXiv 2606.22488)
- @concepts/castle-sim-pathfinding-steals.md — sibling castle-sim planning steal cluster (K126 pathfinding)
- @concepts/active-project-research-routing.md — castle-sim co-primary brief target

## Raw Concept

Prompted by arXiv **2606.22488** (K129). VLM + classical planner pipelines fail in **open-ended** embodied environments because symbolic world models from perception are **incomplete**.

## Narrative

**SCOPE framework — two modules:**

| Module | Role |
|--------|------|
| **SESim** (Symbolic Execution Simulator) | Symbolic validation + real execution; feedback refines plans and **evolves** symbolic world |
| **SASMem** (Self-Adaptive Symbolic Memory) | Distills execution feedback into evolving symbolic knowledge for long-horizon planning |

Improves symbolic-world completeness, plan success under perturbations, and cross-task grounding [TENTATIVE — Zhejiang U. preprint].

**castle-sim steal (regime-conditioned):**

- Maintain **evolving Godot scene graph / affordance registry** from playtest feedback — not static navmesh-only planning
- SESim analogue: headless Godot symbolic step simulator validating siege plans before live playtest
- SASMem analogue: persist distilled map mutations (breach points, tower arcs) across vertical-slice iterations
- Complements K126 AHP multi-criteria route steals — SCOPE adds **world-model evolution**, not just path scoring

**Out of scope:** VLM perception stack for castle-sim (Godot-native sensing preferred).

## Snippets

> "SCOPE comprises two synergistic modules: a Symbolic Execution Simulator (SESim) … and a Self-Adaptive Symbolic Memory (SASMem)." [Source: arXiv:2606.22488 abstract (retrieved 2026-06-25)]

> "In open-ended environments, these symbolic representations obtained from perception are often incomplete, leading to suboptimal performance." [Source: arXiv:2606.22488 abstract (retrieved 2026-06-25)]
