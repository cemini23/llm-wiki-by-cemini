---
title: "shadcn/improve — audit with the best model, execute with a cheap one (MIT)"
type: entity
tags: [tool, agents, skills, audit, cost, worktree, mit]
keywords: [shadcn improve, audit, vet, prioritize, plan, disposable worktree, merge gate]
related:
  - "@osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-11.md"
  - entities/tools/autoharness.md
maturity: draft
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-repository-revenue-2026-11-11.md, URL 3, **Integrate** tier. Routed to Atto, Collectibles, and game-time.

The question this page answers: **how do you spend a frontier model's tokens on judgement and not on typing?**

## Narrative

### What it is

An MIT-licensed agent skill from shadcn. The tagline is the whole design: **"Use your most capable model to audit your codebase and write plans for cheaper models to execute."**

### The phases — five, not six

| Phase | What happens |
|-------|--------------|
| **Recon** | Map the stack, conventions, build commands, existing design docs. |
| **Audit** | Parallel subagents over **nine categories** — correctness, security, performance and others. Each finding cites `file:line`. |
| **Vet** | Re-check every cited location and **remove false positives**. |
| **Prioritize** | Rank by impact relative to effort, weighted by confidence. |
| **Plan** | One self-contained spec per chosen finding, with an index, ordering, and dependencies. |

The report says six phases. The README enumerates five; `execute` is a separate feature, not a phase. Minor, but it changes what the skill does on its own — five phases produce plans, the sixth is a different mode.

**The Vet phase is the one worth copying.** An audit that emits findings without re-checking them produces a list where some fraction are wrong, and a model executing that list will fix things that are not broken. Re-checking every cited location is cheap and it is the step most audit tools omit.

### The safety property

> **"Executors edit only in disposable worktrees, and merging is always yours."**

The skill itself writes **only to `plans/`** and performs read-only analysis otherwise. The executor runs in an isolated git worktree, and **a human merges**.

That is the same separation that makes `worktrunk` useful and the same gate Atto already applies to `truth.ged`. A tool that proposes into a disposable space and leaves the merge to a person cannot silently change the repo.

### Why it fits here

This workspace already runs a version of this manually — the design log freezes a plan, an agent implements, results are appended. `improve` is that loop as an installable procedure with a parallel audit and a false-positive pass.

The cost argument is the practical one: a frontier model reading the whole codebase once and writing five plans is cheaper than the same model editing five times.

### Status

Integrate. Review the plans before an executor runs; the merge gate is the safety, not the audit.

## Snippets

> "Use your most capable model to audit your codebase and write plans for cheaper models to execute." [fetched 2026-11-11]

> "Executors edit only in disposable worktrees, and merging is always yours." [fetched 2026-11-11]

> Licence: "MIT © shadcn." [fetched 2026-11-11]

## Dead Ends

- **Expecting six phases from the skill alone.** Execute is a separate feature.
- **Skipping the Vet pass.** Without it the plan inherits the audit's false positives.
