---
title: GameDevBench — Godot agent development benchmark
type: entity
tags: [entity, tool, godot, benchmark, harness, steal-from]
keywords: [gamedevbench, waynchi, icml, evaluation, godot]
related:
  - sources/gamedevbench-phase-0-audit-2026-06-21.md
  - concepts/agent-harness-castle-project.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/tools/godot-stagehand.md
  - entities/tools/godot-stagehand.md
  - entities/tools/hi-godot-ai.md
  - concepts/agent-harness-castle-project.md
  - entities/tools/godot-mcp-landscape.md
  - entities/engines/godot-4.md
  - sources/inbox-arxiv-reject-batch-2026-06-21.md
  - meta/cross-wiki-routing.md
  - entities/tools/godot-ai-playtest.md
  - entities/engines/godot-4.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-21
updated: 2026-06-21
---

## Relations

- Paper: [arXiv:2602.11103](https://arxiv.org/abs/2602.11103)
- Gitignored brief: `briefs/research/gamedevbench-harness-eval.md`

## Raw Concept

[waynchi/gamedevbench](https://github.com/waynchi/gamedevbench) — **333 Godot 4.x tasks** for evaluating LM coding agents on game dev (gameplay, 2D/3D graphics, UI). ICML 2026.

**License:** Apache-2.0

## Narrative

### Quickstart

```bash
git clone https://github.com/waynchi/gamedevbench.git
cd gamedevbench && bash unzip_tasks.sh
uv run python validate_tasks.py   # ground-truth sanity
uv run python gamedevbench/src/benchmark_runner.py --agent claude-code --model <MODEL> run --task-list tasks.yaml
```

Requires Godot 4.x on PATH (`GODOT_EXEC_PATH`).

### castle-sim mapping

| GameDevBench | castle-sim harness |
|--------------|-------------------|
| Per-task Godot tests | story acceptance + stagehand smoke |
| 2D gfx low pass rate | Validates `@image-gen-wiki` art pipeline risk |
| Video feedback loop | Optional for placeholder-art stories |
| External agent CLI | Same Codex/Claude executor as W2 |

### Phase-0 verdict

**STEAL-FROM (eval)** — @sources/gamedevbench-phase-0-audit-2026-06-21.md

## Dead Ends

- Shipping GameDevBench tasks inside castle-sim repo — keep eval fork separate
