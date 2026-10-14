---
title: godot-stagehand Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, godot, testing, audit]
keywords: [godot-stagehand, playwright, mcp, automation]
related:
  - entities/tools/godot-stagehand.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - entities/tools/godot-mcp-landscape.md
read_status: read
source_type: operator-audit
source_url: https://github.com/mrf/godot-stagehand
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Raw Concept

Phase-0 audit of **mrf/godot-stagehand** — external Godot automation via WebSocket addon + Go MCP server.

## Narrative

### Method

Clone @ main (2026-06-03) to `/tmp/phase0-audit/godot-stagehand`.

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED] |
| Maturity | Early (~7★) but documented quickstart, Go Report Card, active Jun 2026 |
| Architecture | Godot addon (WS :26700) + Go MCP bridge |
| Capabilities | click, input, screenshots, visual diff, perf assert, record/replay |
| vs in-engine GUT | **External** control — fits CI + agent loops |
| Failure modes | Addon opens port on running game — disable in release builds; screenshot flakiness on headless |

### castle-sim fit

Pair with @ccc-wiki verification gates after M1 — smoke menu → pathfinding spike scene without full Godot MCP editor write access.

### Verdict

**CONDITIONAL-GO** — evaluate at W2 for CI smoke tests on `castle-sim`; lower risk than editor MCP (targets running game, not arbitrary file writes).

## Snippets

Tools include `godot_launch`, `godot_click`, `godot_screenshot_diff`, `godot_assert_performance`.
