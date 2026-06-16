---
title: Stronghold2AnalyseHub Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, stronghold-2, modding, audit]
keywords: [stronghold-2, d3d9, minhook, overlay, research]
related:
  - entities/tools/stronghold2-analyse-hub.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - sources/github-stronghold-2-scan-2026-06-13.md
read_status: read
source_type: operator-audit
source_url: https://github.com/crycodebaby/Stronghold2AnalyseHub
maturity: validated
created: 2026-06-13
updated: 2026-06-16
---

## Raw Concept

Phase-0 audit of **crycodebaby/Stronghold2AnalyseHub** — MIT injectable DX9 research overlay for retail Stronghold 2.

## Narrative

### Method

Clone to `/tmp/phase0-audit/Stronghold2AnalyseHub` (2026-02 active). Read README, `src/` hook layout, MinHook + ImGui integration, logging path.

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED — LICENSE] |
| Maturity | Active through 2026-02; small star count; author roadmap mentions pathfinding viz |
| Stack | C++17, MinHook, ImGui, Win32 DLL inject |
| Security | Local-only overlay; no network in core audit — **requires PROCESS inject on retail EXE** |
| castle-sim fit | **NO-GO merge** — Windows retail companion only |

### Steal value

| Extract | Skip |
|---------|------|
| D3D9 EndScene hook + WndProc routing pattern | Shipping DLL in Godot repo |
| Frame-synced debug overlay UX | Long-term replacement for Godot `@tool` panels |
| Structured log beside EXE for playtest notes | Mac/CrossOver inject (unreliable) |

### Verdict

**STEAL-FROM (patterns only)** — operator research overlay while playing retail SH2. Godot equivalent: sim tick HUD + `@tool` debug panel in `castle-sim`.

Install sketch: gitignored `briefs/sh2-analyse-hub-install.md`.

## Snippets

Unload: `END` key — clean DLL detach per README.
