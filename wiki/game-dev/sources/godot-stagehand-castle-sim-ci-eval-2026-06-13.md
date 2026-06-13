---
title: godot-stagehand castle-sim CI evaluation — 2026-06-13
type: source
tags: [source, testing, ci, evaluation, castle-sim]
keywords: [godot-stagehand, ci, smoke, evaluation]
related:
  - concepts/godot-stagehand-ci-smoke-plan.md
  - entities/tools/godot-stagehand.md
  - entities/projects/castle-sim.md
read_status: read
source_type: operator-research
source_url: https://github.com/mrf/godot-stagehand
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Wiki-side evaluation of godot-stagehand for `castle-sim` regression — no install performed (M0 = manual playtest).

## Narrative

### Method

Phase-0 audit read + quickstart/docs review; mapped to @concepts/vertical-slice-v0.md acceptance tests.

### Fit matrix

| v0 criterion | stagehand capability | Automatable? |
|--------------|---------------------|--------------|
| 20×20 wall grid | `godot_click` UI | Partial — needs stable button coords |
| 5 peasants path | `godot_screenshot_diff` or custom metric | Hard early — use perf + boot first |
| 60 fps × 10 min | `godot_assert_performance` | **Yes** — best first CI hook |
| Wood increment | read UI/text via addon hooks | W2+ after HUD exists |

### Recommendation

1. **W2 kickoff:** L0 perf smoke only in `castle-sim` CI
2. **After M1:** add L1 scripted clicks if stagehand record/replay stable on Mac
3. Keep human playtest script as primary gate (@concepts/agent-harness-castle-project.md)

### vs godot-ai-playtest

Choose stagehand if MCP-native + visual diff matter; ai-playtest if minimal Python JSON-RPC preferred — **not both**.

## Snippets

Research artifact: @concepts/godot-stagehand-ci-smoke-plan.md
