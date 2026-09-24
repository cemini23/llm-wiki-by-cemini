---
title: GameLogicBench — runtime game-logic agent benchmark
type: entity
tags: [entity, tool, benchmark, harness, phase-0, steal-from]
keywords: [gamelogicbench, tick-level, assertions, nju-link]
related:
  - sources/arxiv-2609.21562-gamelogicbench-runtime-logic-2026-09-24.md
  - entities/tools/gamedevbench.md
  - concepts/agent-harness-castle-project.md
  - entities/tools/godot-stagehand.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-09-24
updated: 2026-09-24
wire_status: policy_wired
wire_target: concepts/agent-harness-castle-project.md
---

## Relations

- Paper: [arXiv:2609.21562](https://arxiv.org/abs/2609.21562)
- GitHub: [NJU-LINK/GameLogicBench](https://github.com/NJU-LINK/GameLogicBench)

## Raw Concept

Benchmark for coding agents on **runtime game logic** with tick-level assertions and reproducible verdicts — complements GameDevBench (Godot task completion) and stagehand smoke (visual/state snapshot).

## Narrative

### Phase-0 verdict (2026-09-24)

| Check | Result |
|-------|--------|
| SPDX / LICENSE | **None** in repo root |
| Verdict | **STEAL-FROM** — extract harness ideas only; **NO-GO clone** |

### castle-sim mapping

| GameLogicBench idea | W2 action |
|---------------------|-----------|
| Mid-run rule checks | Extend GdUnit / headless tests beyond end-state |
| Scenario sampling | Parameterize kingmaker/economy test seeds |
| No LLM judge | Keep operator + deterministic asserts |

## Dead Ends

- Pinning NJU-LINK repo without license file
- Conflating with GameDevBench or GameEngineBench
