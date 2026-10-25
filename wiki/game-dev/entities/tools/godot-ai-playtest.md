---
title: godot-ai-playtest — TCP control for Godot 4 automation
type: entity
tags: [entity, tool, godot, playtest, automation, phase-0]
keywords: [godot-ai-playtest, tcp, json-rpc, ci]
related:
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/tools/godot-stagehand.md
  - sources/godot-ai-playtest-phase-0-audit-2026-06-13.md
  - entities/tools/godot-mcp-landscape.md
  - entities/tools/binarytracking.md
  - entities/tools/gamedevbench.md
  - entities/tools/hera-agent-godot.md
  - entities/tools/vrexplorer.md
  - sources/arxiv-2607.10174-vrexplorer-vr-testing-2026-07-14.md
  - sources/arxiv-na-2026-binary-tracking-spatial-qa-2606.16902-2026-06-21.md
  - sources/vrexplorer-phase-0-audit-2026-07-14.md
maturity: validated
created: 2026-06-13
updated: 2026-10-25
---

## Relations

- @sources/godot-ai-playtest-phase-0-audit-2026-06-13.md

## Raw Concept

Godot 4 plugin exposing JSON-RPC over TCP (:9876) + PyPI Python client. Phase-0 complete 2026-06-13.

## Narrative

### Phase-0 audit (2026-06-13)

| Check | Result |
|-------|--------|
| License | MIT [CONFIRMED] |
| Maturity | Small community (~3★), PyPI v0.4.0 |
| Use | Integration tests, AI agents, CI screenshots — **not** unit tests |
| Complements | GUT/gdUnit4 for in-process unit tests |

| Verdict | **CONDITIONAL-GO** — WATCH; choose vs stagehand at W2, not both |

## Snippets

`pip install godot-ai-playtest`
