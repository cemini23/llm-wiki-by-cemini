---
title: Starlog — CCGS 49-agent studio deep dive (2026)
type: source
tags: [source, ccgs, claude-code, review]
keywords: [ccgs, starlog, agents, skills, hierarchy]
related:
  - concepts/ccgs-workflow-extraction.md
  - entities/tools/claude-code-game-studios.md
read_status: read
source_type: blog
source_url: https://starlog.is/articles/developer-tools/donchitos-claude-code-game-studios
maturity: tentative
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

Third-party analysis of CCGS: three-tier hierarchy (Directors → Leads → Specialists), model economics, skill enforcement patterns.

## Narrative

### Architecture claims [TENTATIVE — secondary source]

- Agents = markdown + YAML (model, escalation, tools)
- Opus for directors, Sonnet specialists, Haiku narrow tasks
- Skills can **block** implementation without design doc (example Python gate)
- Path-scoped rules per folder (e.g. GDScript standards)
- Git hooks for pre-commit validation

### Verdict from article

- **Use if:** Claude Code committed, 6+ month project, want AI-enforced structure
- **Skip if:** Cursor/Copilot, game jams, existing human team, vendor lock-in concern

### castle-sim note

Starlog says Claude Code **only** — our harness uses **Cursor**. Treat enforcement examples as **patterns to manualize** in briefs/ROADMAP gates.

## Snippets

Cross-check agent names against @sources/ccgs-workflow-catalog-2026.md (authoritative list from repo API).
