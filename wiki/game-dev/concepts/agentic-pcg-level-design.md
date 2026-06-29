---
title: Agentic PCG — LLM tool-using level design
type: concept
tags: [concept, pcg, llm, level-design, procedural, research]
keywords: [agentic-pcg, procedural, level-design, llm, tools]
related:
  - concepts/rts-pathfinding-approaches.md
  - concepts/scope-tiers.md
  - concepts/ai-assisted-game-dev-workflows.md
  - sources/agentic-pcg-jiang-2026.md
  - sources/exa-npc-pcg-ccgs-batch-2026-06-13.md
  - sources/unreal-engine-58-mcp-shelf-2026-06-24.md
maturity: validated
created: 2026-06-13
updated: 2026-06-29
---

## Relations

- @entities/projects/castle-sim.md — v0 map is fixed 20×20; PCG deferred

## Raw Concept

**Agentic PCG** — LLM agents edit levels via **tools** in a feedback loop (perceive → reason → plan → edit), not one-shot level generation. Research + selective hobby adoption for maps/dungeons, not castle-sim v0 walls.

## Narrative

### vs one-shot LLM generation [CONFIRMED — AgenticPCG]

| One-shot | Agentic loop |
|----------|--------------|
| "Generate entire level" | Iterative edits with metrics |
| No solvability guarantee | Environment evaluates path length, connectivity, sim play |
| Hard to constrain | Tool API: place_tile, generate_bsp, reroute corridor |

Domains demonstrated: Binary Maze, Lode Runner, Zelda, Sokoban, Super Mario Bros.

### Tool spectrum

- **Primitive:** place_tile, draw_line, patch
- **Classic PCG:** BSP, digger algorithms
- **Simulation feedback:** A* agent playthrough for SMB quality

### Natural language layer

Same framework accepts **metric targets** ("path length ~256") and **thematic instructions** (creative Mario levels) — language control on top of functional constraints.

### Godot / castle-sim relevance

| Use case | Tier | Fit |
|----------|------|-----|
| Fixed castle grid + player walls | v0 | **Manual** — dynamic walls break pre-gen maps |
| Skirmish map templates | Tier 2 | Agentic PCG for **starting terrain** only |
| Dungeon side mode | Tier 3+ | Full AgenticPCG pattern |
| Wall placement validation | v1 | Steal **metric feedback** idea (reachability tests like Lava Leap) |

### Related repos (Exa)

| Repo | Notes |
|------|-------|
| [JiangZehua/AgenticPCG](https://github.com/JiangZehua/AgenticPCG) | Reference implementation |
| [TaaroBravo/ai-powered-level-designer](https://github.com/TaaroBravo/ai-powered-level-designer) | — |
| [Edgar.Godot](https://github.com/RickyYCheng/Edgar.Godot) | Classic PCG library (non-LLM) |
| [alexishachemi/godot-procgen](https://github.com/alexishachemi/godot-procgen) | Godot procgen |

### Dev-time vs runtime PCG

- **Dev-time:** Agent assists **designer** in Cursor — generate map candidates → human picks → bake into game [aligns with @concepts/ai-assisted-game-dev-workflows.md]
- **Runtime:** Agent loop in shipped build — Tier 3+, needs perf + validation budget

### Hobby workflow (when needed)

1. Define metric targets (solvability, resource node count, siege approach lanes)
2. Expose edit tools as scripts/API
3. LLM iterates in dev session — human approves final map
4. Ship static `TileMapLayer` — no runtime agent

## Snippets

Borrow for pathfinding spike — **prove invariants**:

```gdscript
# After wall place: assert astar.get_point_path(keep, gate) not empty
# Same spirit as AgenticPCG connectivity checks
```

## Dead Ends

- Agentic PCG for **player-placed walls** in real-time — recomputation + solvability = Tier 3 research problem
- LLM generates Stronghold castle layout one-shot — fails defensibility/playability without tool loop
