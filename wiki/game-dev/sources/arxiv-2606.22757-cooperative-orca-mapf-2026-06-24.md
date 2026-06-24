---
title: Cooperative-ORCA* MAPF — continuous-space deadlock avoidance — 2026-06-24
type: source
tags: [source, arxiv, pathfinding, mapf, orca, rts]
keywords: [orca, mapf, multi-agent, local-avoidance, flowtime, rts]
related:
  - concepts/rts-pathfinding-approaches.md
  - concepts/flow-field-pathfinding.md
  - concepts/godot-pathfinding-patterns.md
  - entities/projects/castle-sim.md
  - sources/inbox-arxiv-reject-batch-2026-06-24.md
  - sources/vav-labs-godot-flow-fields-2026.md
  - sources/vav-labs-astargrid2d-gotchas-2026-06-22.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2606.22757
maturity: validated
created: 2026-06-24
updated: 2026-06-24
---

## Raw Concept

**arXiv:2606.22757** — C-ORCA* and C-ORCA*-MAPF extend ORCA* velocity-assignment MAPF with **proactive deadlock avoidance** using agents' full spatial trajectories and spatial dependencies. Beats prior ORCA*-MAPF on solve rate, runtime, and flowtime by avoiding post-hoc deadlock fallback overhead.

## Narrative

### Problem class [CONFIRMED]

**Multi-Agent Path Finding (MAPF):** collision-free paths for many agents from starts to goals in continuous space. ORCA* assigns per-timestep velocities in real time but is **myopic** — current decisions can cause future deadlocks. ORCA*-MAPF adds fallback when deadlocks detected, but flowtime suffers.

### C-ORCA* contribution [CONFIRMED]

| Aspect | ORCA*-MAPF (prior) | C-ORCA* family |
|--------|-------------------|----------------|
| Deadlock handling | Post-hoc fallback when detected | **Proactive** — trajectory + dependency aware |
| Flowtime | High overhead on corrections | Lower — fewer deadlock recoveries |
| Space | Continuous | Continuous (not grid-only) |

Paper domain: robotics teams (cs.RO). Digest surfaced under RTS flow-field query — relevant as **local avoidance layer**, not global path planner.

### castle-sim mapping [TENTATIVE — Tier 2+ shelf]

| Layer | v0 / Tier 1 | Tier 2 hybrid |
|-------|-------------|---------------|
| Global route | `AStarGrid2D` per job (@sources/vav-labs-astargrid2d-gotchas-2026-06-22.md) | Flow field for shared goals (@concepts/flow-field-pathfinding.md) |
| Local crowding | Pattern 7 service + optional `NavigationAgent2D` nudge | ORCA-class velocity steering when 30+ units share choke |
| Deadlock symptom | Units stack at gate / stockpile | Proactive trajectory deps vs reactive unstuck scripts |

**Verdict:** **STEAL-FROM (architecture reference)** — do not port C-ORCA* to GDScript in vertical slice. Evaluate simplified ORCA/RVO nudge (Godot `NavigationAgent2D.avoidance_enabled`) before custom continuous MAPF.

### Relationship to flow fields [CONFIRMED]

- **Flow field** — global direction field toward shared goal; O(1) per-agent lookup
- **ORCA / MAPF** — pairwise velocity constraints to prevent collisions along those directions
- RTS pattern: **global planner + local avoidance** — Emerson flow tiles + RVO/ORCA micro-steer

### Implementation gate

| Signal | Action |
|--------|--------|
| ≤20 peasants, unique job cells | Stay on A* only |
| Rally / breach with 30+ units in choke | Spike flow field + Godot avoidance |
| Persistent gate deadlocks in playtest | Read C-ORCA* for proactive deps; consider grid reservation (simpler) |

## Snippets

```
ORCA* myopia → deadlocks → post-hoc fallback → flowtime overhead
C-ORCA*: trajectory + spatial dependencies → proactive deadlock prevention
```

## Dead Ends

- Full continuous-space C-ORCA* port in Godot — no reference implementation in paper; hobby ROI low vs grid reservation + flow field
- Replacing `AStarGrid2D` with MAPF globally — overkill for castle-sim peasant count in v0–Tier 1
