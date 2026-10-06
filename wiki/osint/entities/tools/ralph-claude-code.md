---
title: "frankbria/ralph-claude-code — continuous TDD outer loop for Claude Code"
type: entity
tags: [tool, agent-harness, ralph, claude-code, ccc, k283]
keywords: [ralph, ralph-claude-code, tdd-loop, autonomous-loop, claude-code, atto]
related:
  - sources/eval-github-repos-dev-tools-2026-10-06.md
  - concepts/k283-eval-wave.md
  - entities/tools/awesome-ralph.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-github-repos-dev-tools-2026-10-06.md — K283 eval (tier: Extract)
- @concepts/k283-eval-wave.md — K283 cluster hub
- @entities/tools/awesome-ralph.md — the Ralph technique family

## Raw Concept

- **Repo:** `github.com/frankbria/ralph-claude-code`
- **Tier (K283):** **Extract**
- **License:** NOT FOUND (docx)
- **Stack:** Bash, Python, Claude Code CLI harness
- **Docx metadata:** NOT FOUND

## Narrative

A harness wrapper for the **Ralph technique**: a continuous outer loop that feeds **test failures and linter output back to Claude Code** until all validation passes. It forces a coding agent into a self-correcting execution loop bounded by tests.

### Why it matters here

Accelerates resolver development for complex Italian genealogical document schemas at Atto. The wiki already tracks the Ralph family (@entities/tools/awesome-ralph.md); this is a concrete Claude Code implementation.

### Boundary

Unchecked autonomous loops can burn API tokens fast — **hard execution limits and cost caps are mandatory.** Must preserve Atto's ban on modifying `truth.ged`. Route: Atto + CCC.

## Snippets

> "The Ralph methodology forces coding agents into self-correcting execution loops bounded by unit tests and linters until a feature or bug fix is fully validated." [Source: eval-github-repos-dev-tools-2026-10-06.md]
