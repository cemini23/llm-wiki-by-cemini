---
title: "Monte Carlo repository evaluation — 12 rows (2026-10-03)"
type: source
tags: [source, k280, eval, simulation, dfs, overfitting]
keywords: [k280, monte-carlo, particle-filter, permutation-test, dfs]
related:
  - concepts/k280-dfs-wave.md
  - concepts/k280-ood-stub-wave.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: skimmed
---

## Relations

- @concepts/k280-dfs-wave.md
- @concepts/k280-ood-stub-wave.md

## Raw Concept

| File | `Revenue Opportunity Repository Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Revenue Opportunity Repository Evaluation.docx` |
| Archive | egress-fi 2026-10-03 |
| Retrieved | 2026-10-03 |
| Dual-ID | **OSINT K280** |
| sha256 | see the archive record |
| Batch theme | Probabilistic Monte Carlo frameworks, statistical validation, and offline historical-document HTR pipelines |

## Narrative

Twelve of the twenty rows are Monte Carlo or statistical. Most are Pass. **Two matter, and one of them is a DFS technique.**

### `neurotrader888/mcpt` — permutation tests for overfitting

Tier Extract. A harness for **Monte Carlo permutation tests**: shuffle returns and bar sequences, build a synthetic null distribution, and get a p-value for a strategy's performance.

Why this matters, and why it is broader than the XSP lane it was routed to. A backtest that beats its null by chance looks exactly like a backtest that works. Permutation testing is the cheap way to tell them apart. It applies to any strategy we test — XSP, parlay EV, and **DFS projection models**.

### `nchopin/particles` — particle filtering, and this one is CeminiDFS

Tier Extract. A sequential Monte Carlo and particle-filtering framework for state-space tracking and parameter learning.

The eval's own framing: **"Converts static pre-game fantasy projections into dynamic, state-space probability distributions that update continuously based on live drive results, snap counts, and game scripts."**

That is a real DFS technique for the late-swap window, and it is the answer to whether anything in this wave applies to CeminiDFS. It does. See @concepts/k280-dfs-wave.md.

### The Pass rows, and why

Nine rows are Pass. The pattern is worth recording, because it recurs:

| Row | Why Pass |
|-----|----------|
| MSM inverse-probability weights (R) | Epidemiology survival analysis. No copula or projection hook |
| Collision-avoidance system (C++) | Microcontroller sensors |
| `jmctf` | Signal processing |
| `vats98754/monte-carlo-experiments` | Teaching exercises |
| `int8/monte-carlo-tree-search` | Game-tree search, not estimation. Context only |
| `abdul92rehman/Probability-Simulation` | Introductory |

### Context and Watch rows

`openmc` (Context) is a serious Monte Carlo particle-transport code — a good architecture reference for large-scale MC, nothing more. `olafSmits/MonteCarloMethodsInFinance` (Context) is a teaching repo. `google-deepmind/mctx` (Watch) is a JAX-based MC tree-search library. `chi-feng/mcmc-demo` (Context) is an interactive MCMC visualiser.

### Boundary

Zero clones this wave for the MC rows. The permutation-test idea and the particle-filter idea are both implementable in our own code. Nothing is vendored.

**Cemini posture:** FILE. **0 product Integrate GO.**
