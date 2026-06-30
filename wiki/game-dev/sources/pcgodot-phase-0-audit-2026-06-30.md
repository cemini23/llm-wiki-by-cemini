---
title: PCGODOT (GF-PCGODOT) — Phase-0 audit — 2026-06-30
type: source
tags: [source, phase-0, godot, pcg, audit]
keywords: [pcgodot, framedworld, flow-nodes, pcg, gdextension]
related:
  - entities/tools/pcgodot.md
  - concepts/agentic-pcg-level-design.md
  - concepts/godot-castle-sim-tool-gap-shelf.md
  - concepts/scope-tiers.md
  - entities/projects/castle-sim.md
  - sources/inbox-arxiv-reject-batch-2026-06-30.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: operator-audit
source_url: https://github.com/Framedworld/PCGODOT
maturity: validated
created: 2026-06-30
updated: 2026-06-30
---

## Raw Concept

Phase-0 audit of **Framedworld/PCGODOT** — Unreal PCG-style node-graph procedural content for Godot 4.4+. Fork/expansion of godot_flow; 120+ nodes, GDExtension spatial accel, editor-docked graph.

## Narrative

### Checks

| Gate | Result |
|------|--------|
| License | **Apache-2.0** [CONFIRMED — GitHub API] |
| Maturity | ~69★; active push 2026-06-24; 34 demo scenes |
| Godot version | **4.4+** [CONFIRMED] — compatible with castle-sim 4.5.2 pin |
| Scope | Scatter, splines, dungeons, runtime `FlowGraphNode3D.execute()` |
| castle-sim fit | **CONDITIONAL-GO (Tier 2+ PCG)** — v0 fixed 20×20 map; defer until core loop + lord AI stable |

### Steal value

| Extract | Skip |
|---------|------|
| UE PCG parity docs for operator PCG literacy | Mandatory for SH2 clone (hand-authored maps) |
| Spline fence / scatter patterns for props/terrain dressing Tier 2.5 | Procedural dungeon replacing Kingmaker scenarios |
| `docs/PARITY_ROADMAP.md` honest gap list before adoption | PCG before fun loop validated |

### Verdict

**CONDITIONAL-GO (Tier 2+ PCG shelf)** — operator brief: gitignored `briefs/research/pcgodot-tier2-pcg-watch.md`.

Cross-ref: @concepts/agentic-pcg-level-design.md (LLM tool-using PCG is separate lane); @concepts/godot-castle-sim-tool-gap-shelf.md.

## Dead Ends

- PCGODOT for v0 vertical slice — scope fence @concepts/vertical-slice-v0.md
- Replacing Kenney GridMap art path with full PCG pipeline prematurely
