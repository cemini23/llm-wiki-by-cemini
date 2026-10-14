---
title: GameEngineBench — UE5 agent-eval taxonomy (paper only) — 2026-08-15
type: source
tags: [source, arxiv, harness, eval, steal-from]
keywords: [gameenginebench, 2607.03525, harness, ue5, eval]
related:
  - entities/tools/gamedevbench.md
  - concepts/agent-harness-castle-project.md
  - concepts/tycho-arc-agi-active-abstraction-stub.md
  - entities/projects/castle-sim.md
  - sources/gamedevbench-phase-0-audit-2026-06-21.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2607.03525
maturity: validated
created: 2026-08-15
updated: 2026-08-15
---

## Relations

- @entities/tools/gamedevbench.md — **different bench** (Godot task zips, Apache-2.0). Do not conflate names.
- @concepts/agent-harness-castle-project.md — scoped story + `*_3d_test` shape
- Gitignored brief: `briefs/research/gameenginebench-harness-taxonomy-2026-07-19.md` (copied from castle-sim 2026-08-15)

## Raw Concept

**arXiv:2607.03525** — GameEngineBench: 110 UE5 C++ agent tasks over gameplay, multiplayer, AI/world orchestration, animation/movement, UI/session, loading, online services, persistence, serialization, XR, rendering plugins. Strongest config **55.5% pass@1**; **31** tasks unsolved by all configs. Upstream code **NOASSERTION** — **paper citation only; no clone / pin**.

castle-sim already mapped categories onto headless `*_3d_test` / Stagehand / memory-gap layers in the gitignored brief (2026-07-19). This page is the public wiki stub so the brief is not orphaned.

## Narrative

### Steal (harness shape, not UE5)

| Idea | castle-sim use |
|------|----------------|
| One scoped edit + compile/run behavioral test | One story brief → one `*_3d_test` / GdUnit assert |
| Unsolved-task backlog | Stories that fail W2 stay “hard” items |
| Category coverage | Tag tests gameplay / AI / movement / UI |

### Contrast vs GameDevBench

| | GameDevBench | GameEngineBench |
|-|--------------|-----------------|
| Runtime | Godot 4.x task zips | UE5 C++ |
| License | Apache-2.0 | NOASSERTION — no pin |
| Wiki entity | @entities/tools/gamedevbench.md | this source only |

**Verdict:** **STEAL-FROM (rubric)** — no Phase-0 clone.

## Dead Ends

- Vendoring UE5 GEB repos or XR/online-service task families
- Replacing `playtest_checklist.sh` / GdUnit with an external bench
- Treating this paper as GameDevBench
