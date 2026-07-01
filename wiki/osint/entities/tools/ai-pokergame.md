---
title: AI_pokergame — Flask/Socket.IO Texas Hold'em with tiered AI
type: entity
tags: [entity, tool, poker, k138]
keywords: [AI_pokergame, PENEEEEE732, Texas Holdem, pot odds, range analysis, MIT, poker-arena]
related:
  - sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md
  - sources/eval-poker-github-repos-2026-06-26.md
  - concepts/takeover-auction-diligence-solvers.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - entities/tools/pokerkit.md
maturity: draft
created: 2026-07-01
updated: 2026-07-01
---

## Relations

- @sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md — K138 Steal-from row
- @entities/tools/pokerkit.md — canonical Arena poker engine (Adopt K130)

## Raw Concept

K138 eval of [PENEEEEE732/AI_pokergame](https://github.com/PENEEEEE732/AI_pokergame) — thread-safe Hold'em server with Easy/Medium/Hard AI tiers.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `PENEEEEE732/AI_pokergame` |
| **License** | **MIT** (`gh api` 2026-07-01; docx had NOT FOUND) |
| **Stars / pushed** | ~0★; pushed 2026-07-01 |
| **Stack** | Python, Flask, Socket.IO |
| **Verdict** | **Steal-from** — opponent modeling heuristics only |
| **Steal** | Hard-tier pot-odds vs implied-odds, semi-bluff vectors, range-read functions |

**Not Arena core:** extract **read-only** heuristic patterns into sandbox villain models or chart opponents — no drop-in `decide()` merge without audit.

**K138 eval (2026-07-01):** P0 inventory shipped (`config/villain_ai_pokergame_hard.yaml`, `examples/ai_pokergame_villain.py`). Local HU 800h seed 42: gin hu004 **+67.9 bb/100** vs ai_pokergame_hard vs **+39.2** vs `tight` — Hard tier is **weaker** than existing gate bots; **not wired to gate or live bundle** (would inflate scores, not improve Arena TS).

Docx notes possible rename/fork to `EMMA019/AI_pokergame` `[NEEDS VERIFICATION 2026-07-01]`.

Brief: `agents/devfun-poker-arena/briefs/2026-07-01_k138-ai-pokergame-opponent-steal.md`

## Snippets

> "Hard difficulty bot executes advanced range analysis and position-aware betting heuristics." [Source: GitHub Repository Evaluation Plan.docx URL 9 (retrieved 2026-07-01)]
