---
title: PCGODOT — Unreal-style PCG node graph for Godot 4
type: entity
tags: [entity, tool, godot, pcg, phase-0]
keywords: [pcgodot, framedworld, flow-nodes, procedural]
related:
  - concepts/agentic-pcg-level-design.md
  - concepts/godot-castle-sim-tool-gap-shelf.md
  - concepts/scope-tiers.md
  - entities/projects/castle-sim.md
  - sources/pcgodot-phase-0-audit-2026-06-30.md
maturity: validated
created: 2026-06-30
updated: 2026-06-30
---

## Relations

- @sources/pcgodot-phase-0-audit-2026-06-30.md — audit trail
- @concepts/agentic-pcg-level-design.md — LLM agent PCG research (separate from this editor graph)

## Raw Concept

**Framedworld/PCGODOT** — Apache-2.0 Godot 4.4+ addon (GDExtension + editor plugin). Visual node graph for scatter, splines, density workflows, runtime graph execution.

## Narrative

### Phase-0 audit (2026-06-30)

| Check | Result |
|-------|--------|
| License | Apache-2.0 |
| Stars | ~69 (Jun 2026) |
| Verdict | **CONDITIONAL-GO** — Tier 2+ PCG only |

### When to use (castle-sim)

| Prefer PCGODOT | Skip |
|----------------|------|
| Procedural prop scatter / terrain dressing after M0 | v0 fixed map + architect walls |
| Learning UE PCG → Godot translation | Kingmaker scenario authoring (hand-built) |

Repo: https://github.com/Framedworld/PCGODOT — copy `demo/addons/flow_nodes_editor/` into project `addons/`.

## Dead Ends

- v0 vertical slice dependency on PCG graphs
