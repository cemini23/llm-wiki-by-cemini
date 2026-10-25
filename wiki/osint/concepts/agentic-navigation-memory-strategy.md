---
title: Agentic navigation — task-conditioned memory strategy
type: concept
tags: [concept, navigation, llm-agents, game-dev, k124]
keywords: [RobotNav, observation budget, memory strategy, agentic planner, pathfinding]
related:
  - sources/arxiv-2607.29600-ham-vln-2026-08-03.md
  - sources/arxiv-qwen-robotnav-2606.18112-2026-06-20.md
  - sources/arxiv-rng-bench-non-markov-mllm-2606.19338-2026-06-21.md
  - concepts/non-markov-belief-state-benchmarks.md
  - concepts/llm-agent-systems.md
  - concepts/fara-computer-use-agent-training.md
maturity: draft
created: 2026-06-20
updated: 2026-10-25
---

## Relations

- @sources/arxiv-qwen-robotnav-2606.18112-2026-06-20.md — primary source
- @game-dev-wiki/concepts/godot-pathfinding-patterns.md — castle-sim pathfinding baseline

## Raw Concept

Prompted by arXiv **2606.18112** (K124). Navigation models should expose a **planner-controllable memory/observation interface** rather than baking in one temporal strategy (uniform subsample vs sliding window).

## Narrative

**Task families differ:**
- Instruction following → long-horizon landmark memory
- Target tracking → recency-only (stale history is noise)
- Object search → shifts mid-episode from global exploration to local approach

**Castle-sim mapping:**
| RobotNav mode | Castle-sim analog |
|---------------|-------------------|
| Long-horizon instruction | Peasant haul routes across full bailey (A* + flow-field) |
| Recency tracking | Siege unit pursuit / ram approach |
| Planner reconfig | External `NavigationService` mode flag set by lord AI or Stagehand harness |

**Posture:** **REFERENCE** — Qwen repo 404; steal interface design for `@game-dev-wiki` pathfinding stories, not model weights.

## Snippets

> "Different navigation tasks demand fundamentally different temporal context and memory strategies." [Source: arXiv:2606.18112 intro (retrieved 2026-06-20)]

## Dead Ends

- Vision-language navigation inputs ≠ Godot NavigationAgent3D — no direct weight transfer.
