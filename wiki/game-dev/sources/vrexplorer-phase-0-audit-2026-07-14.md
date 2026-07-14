---
title: VRExplorer Phase-0 audit — 2026-07-14
type: source
tags: [source, phase-0, unity, vr, playtest, audit]
keywords: [vrexplorer, phase-0, license, unity-package]
related:
  - entities/tools/vrexplorer.md
  - sources/arxiv-2607.10174-vrexplorer-vr-testing-2026-07-14.md
  - sources/inbox-arxiv-reject-batch-2026-07-14.md
  - entities/tools/godot-ai-playtest.md
  - entities/tools/godot-stagehand.md
  - concepts/ai-game-dev-tool-stack-2026.md
read_status: read
source_type: operator-audit
source_url: https://github.com/TsingPig/VRExplorer
maturity: validated
created: 2026-07-14
updated: 2026-07-14
---

## Raw Concept

Phase-0 audit of **TsingPig/VRExplorer** — Unity VR model-based scene exploration / testing agent (ASE 2025 companion repo).

## Narrative

### Method

Shallow clone `main` (2026-05-19 tip) to `/tmp/vrexplorer-audit` on 2026-07-14. GitHub API + README install path checked.

### Checks

| Gate | Result |
|------|--------|
| License | **None declared** (GitHub `license: null`) [CONFIRMED] |
| Size | ~272 MB shallow clone (under 500 MB cap) — **not adopted** (license + engine) |
| Maturity | ~11★, 0 forks; ASE 2025 paper DOI `10.1109/ASE63991.2025.00047` |
| Stack | Unity C# project + UPM package URL `https://github.com/TsingPig/VRExplorer_Release.git` |
| Scope | VR scene exploration (NavMesh + EAT + PFSM) — not Godot, not 2D/3D RTS |
| Failure modes | Requires Navigation Static bake + per-scene EAT interface impl; XR plugin surface |

### vs W2 automation stack

| | VRExplorer | godot-stagehand / ai-playtest |
|---|------------|-------------------------------|
| Engine | Unity VR | Godot 4 |
| License | Undeclared | MIT |
| Control | In-scene agent + NavMesh | WebSocket/MCP or TCP JSON-RPC |
| Fit for castle-sim | None | Primary W2 path |

### Verdict

**NO-GO (adopt)** / **STEAL-FROM (patterns only)** — no local clone under `game-projects/` or castle-sim; keep EAT/PFSM exploration ideas on the playtest research shelf. Prefer Stagehand L1 for `game_3d.tscn` smoke.

## Dead Ends

- Local adopt under 500 MB rule — size OK, but license + Unity VR block adoption
- Dual-stack CI (Unity VRExplorer + Godot Stagehand) for castle-sim
