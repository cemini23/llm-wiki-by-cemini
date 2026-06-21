---
title: GameDevBench — Phase-0 audit — 2026-06-21
type: source
tags: [source, phase-0, benchmark, godot, harness, audit]
keywords: [gamedevbench, waynchi, godot, benchmark, icml]
related:
  - entities/tools/gamedevbench.md
  - entities/tools/godot-stagehand.md
  - entities/tools/hi-godot-ai.md
  - meta/cross-wiki-routing.md
  - concepts/agent-harness-castle-project.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - entities/tools/godot-stagehand.md
  - entities/tools/hi-godot-ai.md
  - entities/projects/castle-sim.md
  - entities/engines/godot-4.md
  - entities/tools/godot-mcp-landscape.md
  - sources/inbox-arxiv-reject-batch-2026-06-21.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: operator-audit
source_url: https://github.com/waynchi/gamedevbench
maturity: validated
created: 2026-06-21
updated: 2026-06-21
---

## Raw Concept

Phase-0 audit of **waynchi/gamedevbench** — ICML 2026 benchmark: 333 Godot 4.x tutorial tasks testing LM agents on gameplay, 2D/3D graphics, UI. Paper arXiv:2602.11103.

## Narrative

### Checks

| Gate | Result |
|------|--------|
| License | **Apache-2.0** [CONFIRMED — GitHub API + README badge] |
| Maturity | ~78★; active Jun 2026; CMU + Princeton |
| Scope | External agent (Claude Code, Codex, Gemini CLI, OpenHands) + Godot test harness |
| Task mix | Gameplay 19.8%, 2D gfx 33.3%, 3D gfx 26.7%, UI 20.1% |
| Difficulty | Avg 4.7 files, 114 LOC, 3.2 filetypes per solution; best agent ~54% pass |
| Multimodal | Image/video feedback loops improve agent scores materially |
| castle-sim fit | **STEAL-FROM (eval methodology)** — W2+ regression adjunct, not runtime dependency |

### Steal value

| Extract | Skip |
|---------|------|
| Godot-native test assertions per task | Running full 333-task suite in hobby CI |
| Category pass-rate baselines (2D gfx hardest) | Treating benchmark tasks as castle-sim stories |
| Video feedback pattern for art-heavy stories | Mandatory gate before every merge |

### Verdict

**STEAL-FROM (benchmark)** — operator brief: gitignored `briefs/research/gamedevbench-harness-eval.md`

Cross-ref: @entities/tools/godot-stagehand.md for castle-sim-specific smoke; GameDevBench for generic Godot agent capability baselines.

## Dead Ends

- Replacing story-004 stagehand smoke with full GameDevBench — scope explosion
- Expecting castle-sim isometric RTS tasks in upstream suite — tutorial-derived mini-games only
