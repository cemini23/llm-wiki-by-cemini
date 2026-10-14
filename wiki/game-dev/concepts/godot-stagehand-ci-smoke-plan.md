---
title: godot-stagehand CI smoke plan — castle-sim (W2 research)
type: concept
tags: [concept, testing, ci, godot, automation]
keywords: [godot-stagehand, ci, smoke-test, castle-sim, verification]
related:
  - entities/tools/godot-stagehand.md
  - entities/projects/castle-sim.md
  - concepts/vertical-slice-v0.md
  - concepts/agent-harness-castle-project.md
  - sources/godot-stagehand-phase-0-audit-2026-06-13.md
  - sources/godot-stagehand-castle-sim-ci-eval-2026-06-13.md
  - concepts/godot-castle-sim-tool-gap-shelf.md
maturity: validated
created: 2026-06-13
updated: 2026-06-17
---

## Relations

- @ccc-wiki/concepts/agent-completion-verification-gates.md

## Raw Concept

Research-only plan for **external** Godot smoke tests on `castle-sim` using godot-stagehand — implementation stays in game repo at W2; this page defines scope and pass criteria.

## Narrative

### Why stagehand (not editor MCP) for CI

| Concern | stagehand | hi-godot MCP |
|---------|-----------|--------------|
| Target | Running game WS :26700 | Editor + project files |
| CI headless | Launch export + assert | Harder; write tools risky |
| Agent loop | screenshot_diff, perf assert | scene mutate |

**M0:** manual playtest only. **W2:** add stagehand after M0 PROCEED.

### Proposed smoke ladder

| Level | Scene | Assert | When |
|-------|-------|--------|------|
| L0 | `pathfinding_spike.tscn` | Game boots, FPS > 55 × 30s | W2 day 1 |
| L1 | same | Place wall via UI click sequence; peasant reaches tree | After M0 pass |
| L2 | M1 main | Wood counter increments | Post-M1 |

Start **L0 only** — flakiness from screenshot diff on placeholder art.

### castle-sim wiring (game repo — not wiki)

1. Add stagehand addon to `castle-sim/addons/` (pin commit from Phase-0 audit)
2. Enable only in `debug`/`ci` export preset — **strip from release**
3. GitHub Action or local: `go run` MCP server + script calling `godot_launch`, `godot_assert_performance`
4. Bind localhost; firewall note in @cybersecurity-wiki MCP posture

### Pass/fail gates

Align with @concepts/vertical-slice-v0.md:

- **Smoke green** ≠ slice done — still requires operator playtest for fun/feel
- **Smoke red** blocks story merge in harness pilot

### Risks [CONFIRMED audit]

- Headless Mac export may differ from editor — test early
- WS port open — disable addon in shipping builds
- Pick **one** automation stack (stagehand **or** godot-ai-playtest)

| Verdict | **Research complete** — execute install in `castle-sim` at W2 kickoff |

## Snippets

```bash
# W2 spike (castle-sim repo) — illustrative
godot --path . res://scenes/spike/pathfinding_spike.tscn
# + stagehand MCP godot_assert_performance max_frame_ms=18
```

## Dead Ends

- Full Playwright-style UI suite before placeholder art stable — too flaky for hobby CI
