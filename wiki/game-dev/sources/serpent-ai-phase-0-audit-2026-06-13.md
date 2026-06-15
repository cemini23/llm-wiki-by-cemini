---
title: SerpentAI Phase-0 audit — 2026-06-13
type: source
tags: [source, phase-0, automation, audit]
keywords: [serpentai, visual, pixel, automation]
related:
  - entities/tools/serpent-ai.md
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
read_status: read
source_type: operator-audit
source_url: https://github.com/SerpentAI/SerpentAI
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Raw Concept

Phase-0 audit of **SerpentAI/SerpentAI** — MIT visual game-agent framework (historical).

## Narrative

### Method

Clone @ `2020.2.1` tag area (last commit 2020-05-22) to `/tmp/phase0-audit/SerpentAI`. Inventory `serpent/`, `pyproject.toml`, README revival note.

### Checks

| Gate | Result |
|------|--------|
| License | **MIT** [CONFIRMED — LICENSE.md] |
| Maturity | ~7k★ historical; **last commit May 2020**; revival announced but not sustained (gh push 2022-11) |
| Stack | Python 3.8+, Poetry; CUDA/ML optional paths (luminoth, etc.) |
| Architecture | Plugin-based game environments + agents; window capture controllers (Linux/Win32) |
| Security | CEF browser in dashboard submodule; no obvious remote shell in core audit — **heavy optional deps** |
| castle-sim fit | **NO-GO** install — dormant; godot-stagehand preferred for W2 |

### Steal value

| Extract | Skip |
|---------|------|
| Game environment plugin interface (`serpent/game.py`) | Full ML training stack |
| Frame capture → action loop pattern | CEF dashboard, vendor bundles |
| Comparison baseline vs Airtest/stagehand | CUDA-required training paths |

### Verdict

**STEAL-FROM / NO-GO install** — architecture reference only; route visual automation to @entities/tools/godot-stagehand.md or @entities/tools/airtest.md (CCC).

## Snippets

Revival README (May 2020): Python 3.8+, fewer deps — not delivered in mainline at audit clone.
