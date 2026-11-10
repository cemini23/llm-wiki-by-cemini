---
title: worktrunk — git worktree CLI for parallel agents
type: entity
tags: [tool, ccc, git, worktree, unverified]
keywords: [worktrunk, git worktree, parallel agents, max-sixty]
related:
  - @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md"
  - entities/tools/thinkrail.md
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md"
  - "@osint-wiki/sources/eval-multi-wiki-link-evaluation-2026-11-10.md"
  - entities/tools/dzhng-skills.md
maturity: draft
created: 2026-10-25
updated: 2026-11-10
phase_0_verdict: INTEGRATE — licence confirmed across four evaluations, not cloned
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

**Licence confirmed** MIT OR Apache-2.0, verified 2026-11-02 and 2026-11-04, unchanged across four evaluations. Star count, commit cadence, and open-issue count remain unreported by every pass — but four consistent verdicts make that less material than it was.

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

## Third sighting — 2026-11-04

`@osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-04.md` URL 1 rates it **Extract** again and adds two specifics neither earlier pass carried:

- **Deterministic per-branch port hashing.** Concurrent agents each get a stable dev-server port from the branch name, so two worktrees do not collide on localhost. That is a concrete fix for a real failure, and it is not something `git worktree` provides.
- It is framed as solving **index contention** across concurrent coding agents — the git index is shared across worktrees, so parallel agents writing the index interfere.

The licence is unchanged and matches what was verified on 2026-11-02: **MIT OR Apache-2.0**.

**Verdict is stable across three passes.** Three evaluations, three Extract ratings, no new concerns. That is the strongest signal in this batch — most recurring items move between tiers.

## Fourth sighting — 2026-11-10: Extract → Integrate

`@osint-wiki/sources/eval-multi-wiki-link-evaluation-2026-11-10.md` URL 5 raises it to **Integrate**. Licence unchanged: **MIT OR Apache-2.0**, verified 2026-11-02 and 2026-11-04.

Two specifics this pass adds to the earlier `pre-merge` hook and port-hashing findings:

- **`wt step` copy-ignored sharing** — targets and build caches (`target/`, `build`) are shared across worktrees, so a fresh worktree does not pay the cold-compile cost on its first build.
- **`hash_port` as a template filter** — the per-branch port is derived in the config rather than set by hand.

**Four evaluations, four consistent verdicts, and the licence has never moved.** That is the most stable item in the entire eval pipeline — everything else that recurs has re-tiered at least once.

The Integrate is reasonable on that record. The one condition from 2026-11-02 stands: the value is in worktree isolation, cache sharing, and the `pre-merge` gate, not the keystroke savings.

## Dead Ends

- Treating the report's Context rating as an evaluation. It is a placeholder, not a finding.
