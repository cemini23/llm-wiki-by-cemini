---
title: K280 OOD Stub Wave (Oct 2026)
type: concept
tags: [ood, k280, eval]
keywords: [k280, monte-carlo, context-only, no-clone]
related:
  - concepts/k279-ood-stub-wave.md
  - sources/eval-monte-carlo-repos-2026-10-03.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k279-ood-stub-wave.md
- @sources/eval-monte-carlo-repos-2026-10-03.md

## Raw Concept

K280 cluster hub. Dual-ID **OSINT K280**. Prior @concepts/k279-ood-stub-wave.md.

## Narrative

The out-of-domain remainder of a 20-row eval. Nothing here drives a decision.

### The Pass rows share one shape

Nine of twenty rows were Pass, and most were Pass for the same reason: **a repo that implements a well-known method, with no domain hook.** Teaching exercises, an introductory probability simulator, an epidemiology R script, a microcontroller sensor project, a game-tree search library.

That is a useful filter to state plainly. A repository is worth a row only if it brings either a technique we do not have or a dataset we cannot build. "Implements Monte Carlo methods" is neither.

### The Context and Watch rows

| Repo | Tier | What it is |
|------|------|-----------|
| `openmc-dev/openmc` | Context | A serious Monte Carlo particle-transport code. Architecture reference for large-scale MC, nothing else |
| `olafSmits/MonteCarloMethodsInFinance` | Context | Teaching repo for MC in finance |
| `int8/monte-carlo-tree-search` | Context | Game-tree search, not estimation |
| `google-deepmind/mctx` | Watch | JAX-based Monte Carlo tree search |
| `chi-feng/mcmc-demo` | Context | Interactive MCMC visualiser |

None of these is a product install. `openmc` is the only one with real engineering weight, and it solves a physics problem we do not have.

### Boundary

Zero clones. Nothing vendored.

**Cemini posture:** FILE. **0 product Integrate GO.**
