---
title: loop-engineering — autonomous agent loop patterns (cobusgreyling)
type: entity
tags: [entity, tool, agent-harness, ccc, k129]
keywords: [loop-engineering, cobusgreyling, MIT, loop-audit, loop-init, autonomous loops]
related:
  - sources/eval-url-cemini-research-2026-06-25.md
  - sources/substack-rss-addy-osmani-2026-08-14-practical-loop-engineering.md
  - concepts/practical-loop-engineering.md
  - concepts/code-as-agent-harness.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/active-project-research-routing.md
  - concepts/asd-ste100-writing-style.md
  - sources/x-article-antpalkin-self-improving-ai-trading-machine-2026-08-06.md
maturity: draft
created: 2026-06-25
updated: 2026-10-25
---

## Relations

- @sources/eval-url-cemini-research-2026-06-25.md — K129 Adopt row (URL 1)
- @sources/substack-rss-addy-osmani-2026-08-14-practical-loop-engineering.md — K239 methodology (Claude `/goal` `/loop`)
- @concepts/practical-loop-engineering.md — K239 concept; this page stays the cobusgreyling *repo*
- @concepts/wiki-tooling-evaluation.md — Phase-0 registry
- @concepts/code-as-agent-harness.md — loop taxonomy vs turn-by-turn prompting

## Raw Concept

Phase-0 prompted by K129 **Cemini URL Evaluation Research.docx** URL 1 — `cobusgreyling/loop-engineering`.

## Narrative

**loop-engineering** is an MIT-licensed collection of **practical patterns, starters, and CLI tools** for designing autonomous agent loops (loop-audit, loop-init, loop-cost). Shifts orchestration from isolated turn-by-turn prompting toward schedule-driven recursive loops with state memory, sub-agents, skills, plugins, and isolated worktrees.

**Phase-0 (2026-06-25):**

| Check | Result |
|-------|--------|
| License | **MIT** (`gh api` — SPDX MIT) |
| Hardcoded wiki layout | N/A — agent orchestration patterns, not wiki tool |
| Maturity | **1428★**, pushed 2026-06-25, 6 open issues |
| CCC-wiki fit | **Adopt** — canonical loop-engineering reference for Cursor/Claude Code meta-wiki |
| OSINT fit | Orchestrator-adjacent pipeline configs (secondary) |

**Posture:** **Adopt** for @ccc-wiki. Sync loop taxonomy into `.cursor/rules/` and `/loop` skill cross-references. Do not vendor into CeminiSuite prod trading stack.

## Snippets

> "Practical patterns, starters & CLI tools for loop engineering with AI coding agents." [Source: https://github.com/cobusgreyling/loop-engineering README (retrieved 2026-06-25)]

## Dead Ends

- Docx claimed 368★ — stale; `gh api` shows 1428★ at Phase-0 (eval doc lag, not license error).
