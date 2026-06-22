---
title: castle-sim — Pathfinding & Multi-Criteria Route Steals
type: concept
tags: [concept, game-dev, pathfinding, castle-sim, multi-criteria, k126]
keywords: [AHP, genetic-algorithm, A-star, siege-ai, godot-navigation, route-diversity, castle-sim]
related:
  - sources/arxiv-continuum-robots-resilience-2606.20495-2026-06-22.md
  - sources/links-6-22-tool-eval.md
  - concepts/active-project-research-routing.md
  - entities/tools/mattpocock-skills.md
maturity: draft
created: 2026-06-22
updated: 2026-06-22
---

## Relations

- @sources/arxiv-continuum-robots-resilience-2606.20495-2026-06-22.md — K126 REFERENCE source for AHP + GA vs A* tradeoffs
- @sources/links-6-22-tool-eval.md — co-primary K126 ingest batch

## Raw Concept

What prompted this page: K126 arXiv 2606.20495 (continuum robot path planning) is off-domain for OSINT trading but maps cleanly to **castle-sim** siege unit routing — multi-criteria path quality beyond shortest-path.

## Narrative

Castle-sim Godot vertical slice needs siege AI that picks **diverse, resilient approach routes**, not identical shortest paths every replay. arXiv 2606.20495 demonstrates wrapping path planners with **Analytical Hierarchy Process (AHP)** scoring across weighted criteria — transferable pattern even though the paper's domain is soft robotics.

### Stealable pattern (regime-conditioned)

| Criterion (paper) | castle-sim analog |
|-------------------|-------------------|
| Distance | Grid path cost / navigation mesh length |
| Motor damage | Unit stamina / siege engine wear (future mechanic) |
| Mechanical damage | Exposure to tower fire along route |
| Accuracy | Arrival precision at breach point |

**Planner choice heuristic from paper:**

- **Small maps, single choke** → A* acceptable (fast, deterministic)
- **Multi-path siege maps** → GA or weighted A* with AHP reranking for route diversity (reduces predictable defender positioning)

### Implementation sketch (P0 brief scope)

1. Godot `NavigationAgent3D` returns top-k paths or waypoint sets
2. Score each with weighted sum (start weights: distance 0.4, exposure 0.3, diversity 0.2, arrival 0.1)
3. Pick argmax; tie-break with seed for replay determinism in tests
4. Playtest parity: log chosen route family per seed in Stagehand smoke

### Out of scope

- Continuum robot kinematics simulation
- Production trading / poker routing

## Snippets

> "GA performance time does not depend on environment cardinality; generates more diverse paths than A*." [Source: arxiv-2606.20495 — paraphrased for game routing]
