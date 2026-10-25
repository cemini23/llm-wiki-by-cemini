---
title: serena — LSP semantic code retrieval for agents (oraios)
type: entity
tags: [entity, tool, ccc, agent-harness, k146]
keywords: [serena, LSP, find_symbol, AST, semantic grep, MIT]
related:
  - sources/eval-github-repo-mcp-plan-2026-07-05.md
  - concepts/coding-agent-substrate-steerability.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/ripgrep.md
maturity: draft
created: 2026-07-05
updated: 2026-10-25
---

## Relations

- @sources/eval-github-repo-mcp-plan-2026-07-05.md — K146 Steal-from
- @concepts/coding-agent-substrate-steerability.md — bounded retrieval complement

## Raw Concept

K146 Phase-0 on [oraios/serena](https://github.com/oraios/serena).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `oraios/serena` |
| **License** | **MIT** |
| **Stars / pushed** | ~26k★; pushed 2026-07-03 |
| **Verdict** | **Steal-from** — CCC harness; no install brief |
| **Pattern** | LSP-backed `find_symbol` / `get_symbols_overview` vs naive text grep |

Extract prompt patterns for federation agent refactors; pair with substrate constraints from `@concepts/coding-agent-substrate-steerability.md`.

## Snippets

> "Grants agents abstract syntax tree (AST) level semantic code retrieval tools." [Source: eval-github-repo-mcp-plan-2026-07-05.md]
