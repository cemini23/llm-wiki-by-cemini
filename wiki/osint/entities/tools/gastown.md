---
title: gastown — Git-backed multi-agent orchestration (gastownhall)
type: entity
tags: [entity, tool, ccc, tipdrop, agent-harness, k146]
keywords: [gastown, Beads, Git worktrees, Mayor, Deacon, Polecat, MIT]
related:
  - sources/eval-multi-wiki-github-mcp-2026-07-05.md
  - concepts/coding-agent-substrate-steerability.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @sources/eval-multi-wiki-github-mcp-2026-07-05.md — K146 Adopt row
- @concepts/coding-agent-substrate-steerability.md — file-backed state vs context death

## Raw Concept

K146 Phase-0 on [gastownhall/gastown](https://github.com/gastownhall/gastown).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `gastownhall/gastown` |
| **License** | **MIT** (`gh api` 2026-07-05) |
| **Stars / pushed** | ~16k★; pushed 2026-07-02 |
| **Verdict** | **Adopt** — CCC orchestration reference; TipDrop Module 1 handoff |
| **Pattern** | Event-sourced **Beads** ledger + Git worktrees; Mayor/Deacon/Polecat watchdog hierarchy for persistent agent swarms |

Replaces ad-hoc Windows handoff files for TipDrop agent continuity. Not prod-scp — kit-local adoption.

Brief: `../projects/tipdrop-workspace-kit/briefs/2026-07-05_k146-gastown-agent-handoff-adopt.md`

## Snippets

> "Anchoring agent state, procedural workflows, and asynchronous communication to Git worktrees and an event-sourced ledger named Beads." [Source: eval-multi-wiki-github-mcp-2026-07-05.md]
