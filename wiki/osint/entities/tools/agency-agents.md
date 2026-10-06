---
title: "msitarzewski/agency-agents — Claude Code / Cursor persona library"
type: entity
tags: [tool, agent-persona, claude-code, cursor, ccc, k283]
keywords: [agency-agents, personas, agent-roles, claude-code, cursor, k283]
related:
  - sources/eval-github-repos-dev-tools-2026-10-06.md
  - concepts/k283-eval-wave.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-github-repos-dev-tools-2026-10-06.md — K283 eval (tier: Extract)
- @concepts/k283-eval-wave.md — K283 cluster hub
- @concepts/wiki-tooling-evaluation.md — tooling eval context

## Raw Concept

- **Repo:** `github.com/msitarzewski/agency-agents`
- **Tier (K283):** **Extract**
- **License (docx claim):** MIT — unverified
- **Stack:** Markdown, Shell, YAML frontmatter, Claude Code / Cursor prompt templates
- **Docx metadata:** 156.3k★ / Oct 2026 — **suspiciously high; NOT independently verified**

## Narrative

A library of **140+ specialised domain agent personas** — role constraints, explicit boundaries, and success criteria — for Claude Code and Cursor. Cited examples: Database Architect, Codebase Onboarding, QA Reality Checker.

### Why it matters here

Reusable persona prompts that reduce architectural drift in long builds. Route: CCC wiki; Atto engineering briefs.

### Boundary

**Injected personas must not override active-project invariants** — Atto's ban on automated merge into `truth.ged`; GuruWatcher's alert-only design. The 156.3k star figure is a claim to verify before treating the repo as a canonical reference. **Extract the persona pattern; do not vendor the library.**

## Snippets

> "The repository contains extensive persona definitions that establish explicit boundaries, rules, and deliverable standards for coding assistants." [Source: eval-github-repos-dev-tools-2026-10-06.md]
