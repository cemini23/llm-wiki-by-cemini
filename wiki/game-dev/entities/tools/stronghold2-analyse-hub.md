---
title: Stronghold2AnalyseHub — DX9 research overlay (MIT)
type: entity
tags: [entity, tool, stronghold-2, modding, reverse-engineering]
keywords: [stronghold-2, d3d9, minhook, imgui, overlay]
related:
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - concepts/stronghold-2-architect-controls.md
  - concepts/operator-vision-sh2-personal-clone.md
  - sources/github-stronghold-2-scan-2026-06-13.md
  - sources/stronghold2-analyse-hub-phase-0-audit-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-16
---

## Relations

- @concepts/stronghold-2-github-ecosystem-shelf.md — catalog context

## Raw Concept

[`crycodebaby/Stronghold2AnalyseHub`](https://github.com/crycodebaby/Stronghold2AnalyseHub) — injectable **Win32 DLL** for **Stronghold 2 (DX9)** with MinHook, ImGui overlay, WndProc routing, structured logging. MIT. Active through **2026-02**.

## Narrative

### Hooks [CONFIRMED — README]

- `Direct3DCreate9` → `CreateDevice` → `EndScene` / `Reset`
- Game window **WndProc** for ImGui input
- `END` key — clean unload

### Intended roadmap (author)

Render-pass analysis, wireframe toggles, **pathfinding visualization**, AI timing — aligns with operator playtest + clone pathfinding validation.

### Value vs castle-sim

| Study | Godot equivalent |
|-------|------------------|
| In-game overlay UX | Godot `@tool` debug panel / `CanvasLayer` HUD |
| Frame-synced telemetry | Sim tick debug overlay in `castle-sim` |
| D3D9 hook lifecycle | N/A — document **retail-only** research path |

### Phase-0 verdict

**STEAL-FROM (patterns only)** — MIT hook + overlay architecture for **companion research** while playing retail. Not merged into Godot codebase.

### Install sketch [NEEDS VERIFICATION on Steam EXE build]

Build Win32 Release DLL → inject into `Stronghold2.exe` → read `Stronghold2AnalyseHub.log` beside EXE. Steps: `briefs/sh2-analyse-hub-install.md` (local).

## Dead Ends

- **Mac/CrossOver injection** — DLL path is Windows-native; CrossOver may block inject; use Windows VM or native bottle if needed
- Replacing Godot debug tools with this long-term
