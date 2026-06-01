---
title: Memory OS (ClaudioDrews) — Hermes agent memory stack
type: entity
tags: [entity, tool, memory, hermes, defer-claude-code]
keywords: [memory-os, hermes, qdrant, redis, claudedrews, k92]
related:
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - "@ccc-wiki/entities/tools/claude-mem.md"
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — K92 CONDITIONAL-GO
- @ccc-wiki/entities/tools/claude-mem.md — Claude Code memory owner; do not stack duplicate SessionStart stacks

## Raw Concept

- **Repo**: `github.com/ClaudioDrews/memory-os`
- **Stack**: Hermes Agent + Docker (Qdrant, Redis, ARQ worker)

## Narrative

### Phase-0 audit (2026-06-01)

| Check | Result |
|-------|--------|
| License | **MIT** |
| Maturity | 57★ / push 2026-06-01 |
| Fit | **Hermes-only** — not Claude Code / Cursor |
| Collision | Overlaps claude-mem + stash episodic goals on laptop |

**Verdict: CONDITIONAL-GO (Hermes lane only)** — **not adopted** on Cemini Claude Code stack 2026-06-01. Revisit only if operator standardizes on Hermes for research agents.

## Snippets

> K92 eval Adopt tier — deferred for wrong runtime (Hermes vs Claude Code). [Source: @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]
