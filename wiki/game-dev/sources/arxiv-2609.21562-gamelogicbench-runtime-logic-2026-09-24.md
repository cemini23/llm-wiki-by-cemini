---
title: GameLogicBench — tick-level runtime game logic for coding agents (2026-09-24)
type: source
tags: [source, arxiv, benchmark, harness, eval, steal-from]
keywords: [gamelogicbench, tick-level, assertions, coding-agents, runtime-rules]
related:
  - entities/tools/gamelogicbench.md
  - entities/tools/gamedevbench.md
  - concepts/agent-harness-castle-project.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - entities/tools/godot-stagehand.md
  - sources/inbox-arxiv-reject-batch-2026-09-24.md
  - sources/gamedevbench-phase-0-audit-2026-06-21.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.21562
maturity: validated
created: 2026-09-24
updated: 2026-09-24
---

## Raw Concept

**arXiv:2609.21562** — GameLogicBench evaluates coding agents on **runtime game logic** with **tick-level state assertions** across varied scenarios. Prior benches replay fixed cases, score videos, or use LLM judges; a game can end in a valid terminal state after mid-run rule violations. Repo: [NJU-LINK/GameLogicBench](https://github.com/NJU-LINK/GameLogicBench).

## Narrative

### Problem [CONFIRMED]

| Gap | castle-sim W2 implication |
|-----|---------------------------|
| End-state-only tests | Popularity/crime could look fine at frame N while rules broke at tick t |
| LLM-as-judge | Non-reproducible — conflicts with playtest + GdUnit gates |
| Fixed replay only | Kingmaker scenarios need parameterized seeds |

### Steal for castle-sim harness [CONFIRMED]

- **Tick-level invariants** during headless run — not only final scene tree
- **Deterministic verdicts** — same pattern as CraftBench-UE + GameDevBench ground truth
- Contrast @entities/tools/godot-stagehand.md L0 smoke (screenshot/state snapshot) — upgrade path to **assertion hooks** in `*_3d_test`

### Phase-0 (2026-09-24)

| Check | Result |
|-------|--------|
| LICENSE file | **Missing** — `gh api` license null; no LICENSE in repo root |
| Verdict | **STEAL-FROM (paper + docs)** — **NO-GO clone** until SPDX appears |

### Phase-1

**policy_wired** — tick-level assertion pattern cited in @concepts/agent-harness-castle-project.md (W2 verify lane).

## Snippets

```
Key claim: check game rules throughout execution across varied evaluator-selected scenarios with exactly reproducible verdicts
```

## Dead Ends

- Cloning GameLogicBench into castle-sim without LICENSE
- Replacing operator playtest with LLM judge for “fun” gate
