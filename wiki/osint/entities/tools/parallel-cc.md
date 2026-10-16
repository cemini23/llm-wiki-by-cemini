---
title: parallel-cc — git-worktree isolation for concurrent Claude Code sessions
type: entity
tags: [tools, claude-code, git, k292]
keywords: [parallel-cc, git-worktree, concurrency, claude-code, session-isolation]
related:
  - sources/eval-url-multi-wiki-repository-2026-10-16.md
maturity: draft
created: 2026-10-16
updated: 2026-10-16
wire_status: extract_only
---

## Relations

- @sources/eval-url-multi-wiki-repository-2026-10-16.md

## Raw Concept

**What prompted this page:** K292 tool eval (2026-10-16). Phase-0 licence read via `gh api`; shallow-cloned to `.local/adopts/k292/` as REFERENCE. **No install. 0 Integrate GO.**

## Narrative

**Git-worktree isolation for concurrent Claude Code sessions** — the problem of two agent sessions editing one checkout.

**Licence:** **MIT** — `[CONFIRMED]` by `gh api` on 2026-10-16 (the docx agreed).

**Docx tier: Extract.** Cloned; 2,340 KB after the 2026-10-16 prune — the smallest clone in the batch.

**Why it is worth reading here specifically:** this workspace already runs concurrent sessions against one repository, and the app itself creates worktrees for Code sessions. The interesting question is whether `parallel-cc` solves anything the app's own worktrees do not — **that comparison is the whole evaluation**, and it has not been made.
