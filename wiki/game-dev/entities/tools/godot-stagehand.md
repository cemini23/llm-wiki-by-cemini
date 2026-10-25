---
title: godot-stagehand — Playwright-like Godot test driver
type: entity
tags: [entity, tool, godot, testing, automation, phase-0]
keywords: [godot-stagehand, playwright, mcp, ci, automation]
related:
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/tools/godot-ai-playtest.md
  - entities/tools/gamedevbench.md
  - sources/gamedevbench-phase-0-audit-2026-06-21.md
  - entities/tools/ziva-godot-agent.md
  - sources/ziva-godot-agent-phase-0-audit-2026-06-21.md
  - concepts/agent-harness-castle-project.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - sources/godot-stagehand-phase-0-audit-2026-06-13.md
  - sources/godot-stagehand-castle-sim-ci-eval-2026-06-13.md
  - entities/tools/airtest.md
  - entities/tools/godot-mcp-landscape.md
  - entities/tools/serpent-ai.md
  - sources/airtest-phase-0-audit-2026-06-13.md
  - sources/godot-ai-playtest-phase-0-audit-2026-06-13.md
  - concepts/godot-castle-sim-tool-gap-shelf.md
  - sources/godot-castle-sim-tool-gap-research-2026-06-17.md
  - entities/tools/gamelogicbench.md
  - entities/tools/hera-agent-godot.md
  - entities/tools/vrexplorer.md
  - sources/arxiv-2607.10174-vrexplorer-vr-testing-2026-07-14.md
  - sources/arxiv-2609.21562-gamelogicbench-runtime-logic-2026-09-24.md
  - sources/hera-agent-godot-phase-0-audit-2026-06-26.md
  - sources/notnull92-hera-agent-godot-devto-2026-06-25.md
  - sources/vrexplorer-phase-0-audit-2026-07-14.md
wire_status: policy_wired
wire_target: concepts/agent-harness-castle-project.md
maturity: validated
created: 2026-06-13
updated: 2026-10-25
---

## Relations

- @ccc-wiki/concepts/agent-completion-verification-gates.md
- @sources/godot-stagehand-phase-0-audit-2026-06-13.md

## Raw Concept

External **Go** MCP server + Godot WebSocket addon for automated gameplay/CI. Phase-0 complete 2026-06-13.

## Narrative

### Phase-0 audit (2026-06-13)

| Check | Result |
|-------|--------|
| License | MIT [CONFIRMED] |
| Maturity | Early (~7★) but active docs, Jun 2026 push |
| Model | MCP client ↔ Go server ↔ game addon (WS :26700) |
| Strength | External CI control, visual diff, perf asserts — **no arbitrary project file delete** |
| Risk | Open port in dev builds; disable addon in release exports |

### vs godot-ai-playtest

Prefer **stagehand** if MCP-native CI; **ai-playtest** if simple Python JSON-RPC suffices — pick one at W2.

| Verdict | **CONDITIONAL-GO** for W2 CI smoke on `castle-sim` |

## Snippets

Quickstart: github.com/mrf/godot-stagehand/docs/quickstart.md
