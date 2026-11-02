---
title: worktrunk — git worktree CLI for parallel agents
type: entity
tags: [tool, ccc, git, worktree, unverified]
keywords: [worktrunk, git worktree, parallel agents, max-sixty]
related:
  - @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md"
  - entities/tools/thinkrail.md
maturity: draft
created: 2026-10-25
updated: 2026-11-02
phase_0_verdict: EXTRACT — licence confirmed, not cloned
wire_status: none
wire_note: Licence confirmed MIT OR Apache-2.0 on 2026-11-02. Still not cloned; stars, commits, and issues unreported.
---

## Raw Concept

URL 9 of @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md. Tier **Context**.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/max-sixty/worktrunk |
| **License** | NOT FOUND |
| **Stars / commits / issues** | NOT FOUND |
| **Verdict** | CONTEXT — carry as an unverified stub |

A CLI for creating and removing git worktrees so several coding agents can work on separate branches without dirtying the main tree.

**Why it is not adopted:** `git worktree` already does this, and Claude Code and Cursor both isolate branches. The wrapper saves keystrokes, not risk.

`[NEEDS VERIFICATION 2026-11-02]` — **the licence is now confirmed** (MIT OR Apache-2.0, see below). Still unverified: star count, commit cadence, and open issues. The first report carried no telemetry at all for this row.

## Re-surface — v10.10 batch C (2026-11-02)

`@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md` URL 9 raises this from **Context** to **Extract** and closes the licence gap.

| Field | 2026-10-25 | 2026-11-02 |
|-------|-----------|-----------|
| Licence | NOT FOUND | **MIT OR Apache-2.0**, dual-licensed |
| Tier | Context | **Extract** |
| Stars / commits / issues | NOT FOUND | still unreported |

**What the new row adds beyond a wrapper.** The report describes specifics the first pass missed:

- `wt switch -c -x claude <branch>` — create a worktree and start an agent in it in one step.
- **Lifecycle hooks** — `post-create` and `pre-merge`. A pre-merge hook is the interesting one: it is a gate that runs on every branch before it lands.
- `/wt-diff` review panes.
- `wt list --full` agent-activity indicators.

**Revisiting the earlier verdict.** The 2026-10-25 reasoning was that `git worktree` already does this and the wrapper "saves keystrokes, not risk". That still holds for worktree creation. It does **not** hold for the hooks: a deterministic `pre-merge` gate is a control, not a convenience, and there is no built-in equivalent in `git worktree`.

So the honest position is narrower than either report: **creation is still a wrapper; hooks and per-worktree diff review are the parts that could matter.** Extract those ideas; whether to adopt the CLI is a separate, smaller question.

## Dead Ends

- Treating the report's Context rating as an evaluation. It is a placeholder, not a finding.
