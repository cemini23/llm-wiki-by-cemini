---
title: draftfast — DFS lineup optimizer (BenBrostoff)
type: entity
tags: [entity, tool, dfs, nfl, k138]
keywords: [draftfast, BenBrostoff, FanDuel, DraftKings, lineup optimization, Python, CeminiDFS]
related:
  - sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md
  - sources/tool-eval-metaplan-81url-2026-06-24.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/espn-api.md
maturity: draft
created: 2026-07-01
updated: 2026-07-01
---

## Relations

- @sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md — K138 row (docx Adopt → downgraded)
- @sources/tool-eval-metaplan-81url-2026-06-24.md — prior Reference-only (CeminiDFS duplicate note)

## Raw Concept

K138 Phase-0 on [BenBrostoff/draftfast](https://github.com/BenBrostoff/draftfast) — Python 3.12+ knapsack lineup engine for DK/FD multi-sport slates.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `BenBrostoff/draftfast` |
| **License** | **NOT FOUND** on gh (no LICENSE file; docx NOT FOUND) |
| **Stars / pushed** | ~296★; pushed 2026-02-05 |
| **Stack** | Python 3.12+ |
| **Verdict** | **CONDITIONAL-GO** — adopt optimizer **after** license audit or clean-room reimplementation |
| **Steal** | RuleSet objects (DK/FD positional caps), `OptimizerSettings` stacking, CSV salary ingest |

**Overlap:** K128 Metaplan listed draftfast as CeminiDFS duplicate Reference-only; K138 reopens as optimizer gap-fill with **license blocker**.

Brief: `../projects/CeminiDFS/briefs/2026-07-01_k138-draftfast-optimizer-conditional.md`

## Snippets

> "No LICENSE file on GitHub — CONDITIONAL-GO not Adopt." [Source: K138 Phase-0 gh api 2026-07-01]
