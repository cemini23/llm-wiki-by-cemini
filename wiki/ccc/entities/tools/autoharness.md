---
title: "autoharness — learns skills from your own sessions (MIT, never touches yours)"
type: entity
tags: [tool, skills, self-learning, claude-code, local, mit]
keywords: [autoharness, skill distillation, reflect every n, claude skills archive, python]
related:
  - "@osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-11.md"
  - entities/tools/shadcn-improve.md
maturity: draft
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-11.md, URL 17, **Integrate** tier. Routed to Atto, Collectibles, and game-time.

The question this page answers: **can an agent turn its own repeated work into a skill without being told to?**

## Narrative

### What it does

A Claude Code plugin, **Python 3.11+, no third-party dependencies**, **MIT**.

It counts main-session tool calls and triggers a **non-blocking background reflection at turn end** every N calls (`AUTOHARNESS_REFLECT_EVERY_N`, default 50). The reflection distils recurring workflows into skills. On demand: `/learn`.

It also **merges** skills covering the same scenario, **updates** existing ones when it learns an improvement, and **archives** ones that stop being useful.

### Phase-0 correction: where it writes

The report says skills land in `.claude/autoharness/`. Actual layout:

| Path | Contents |
|------|----------|
| `.claude/skills/` | Learned skills, project-scoped |
| `~/.claude/skills/` | Learned skills, global and not repo-specific |
| `.claude/skills/.archive/<name>/` | Archived skills |
| **`.claude/autoharness/`** | **State only** — not skills |

Overridable with `AUTOHARNESS_PROJECT_DIR`, `AUTOHARNESS_GLOBAL_ROOT`, `AUTOHARNESS_STATE_HOME`.

### The property that makes it safe here

> **It only manages skills it created itself, and leaves your own skills alone.**

This workspace has hand-written skills — `route`, `no-mistakes`, `security-audit`, and the project-local ones. An auto-learning layer that rewrote them would be unusable. One that confines itself to its own namespace is just a background process that writes files.

**Verify that boundary before trusting it.** "Leaves your skills alone" is a claim in a README, and a merge heuristic is exactly the kind of code that can get it wrong.

### The idea worth taking even if the plugin is not

**Reflect every N tool calls, not every session.** A per-session reflection only sees one task. A reflection every 50 calls sees the shape of the work — which tools recur, which steps repeat — and that is what a skill is made of.

The non-blocking part matters too. A reflection that pauses the session costs more than the skill it produces.

### Status

Integrate. Verify the namespace boundary on a scratch repo first.

## Snippets

> It distils lessons "after enough tool calls (default: every 50), or on demand with `/learn`." [fetched 2026-11-11]

> "It only manages skills it created itself and leaves your own skills alone." [fetched 2026-11-11]

> Licence: MIT. [fetched 2026-11-11]

## Dead Ends

- **Assuming everything lands in `.claude/autoharness/`.** That is state; skills go to `.claude/skills/`.
- **Trusting the namespace claim without checking.** A merge heuristic is where it would fail.
