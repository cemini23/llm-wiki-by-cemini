---
title: K280 DFS Wave (Oct 2026)
type: concept
tags: [dfs, gambling, k280]
keywords: [k280, particle-filter, late-swap, permutation-test, extract]
related:
  - concepts/k279-dfs-parlays-wave.md
  - sources/eval-monte-carlo-repos-2026-10-03.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k279-dfs-parlays-wave.md
- @sources/eval-monte-carlo-repos-2026-10-03.md

## Raw Concept

K280 DFS cluster hub. Dual-ID **OSINT K280**. Prior @concepts/k279-dfs-parlays-wave.md.

## Narrative

**Yes — this wave applies to CeminiDFS.** Two techniques, both from the Monte Carlo half of the eval.

### 1. Particle filtering for the late-swap window

Source: `nchopin/particles`, tier Extract.

The eval's own framing: it **"converts static pre-game fantasy projections into dynamic, state-space probability distributions that update continuously based on live drive results, snap counts, and game scripts."**

That is the late-swap gap. Today a projection is a number computed before the slate. During the games, that number is stale, and the late-swap decision is made against a stale prior. A particle filter is the standard tool for exactly this: maintain a set of weighted hypotheses about each player's state, update the weights as observations arrive (drives, snaps, targets, game script), and read the posterior distribution rather than a point estimate.

Concretely, the build:

| Piece | What it does |
|-------|--------------|
| State | Per-player latent usage rate and game state |
| Transition | How usage drifts as the game script changes |
| Observation | Live drive results, snap counts, targets, carries |
| Weights | Re-weight particles on each observation |
| Output | A posterior distribution per player, not a point projection |

The late-swap decision then compares posteriors instead of pre-game means.

**Honest caution.** This is the highest-complexity item either of the last two waves has produced. A particle filter has real failure modes: particle degeneracy, a misspecified transition model, and a likelihood that looks right but is subtly wrong. It is worth building only if the late-swap lane is actually where the margin sits.

### 2. Permutation tests for overfitting

Source: `neurotrader888/mcpt`, tier Extract.

Shuffle returns and bar sequences to build a synthetic null distribution, then score the strategy against it. A backtest that beats its null by chance looks exactly like a backtest that works, and permutation testing is the cheap way to tell them apart.

Routed by the eval to the XSP lane, but it applies to any strategy we test — including **DFS projection models and lineup constructions**. If a projection model's edge does not survive a permutation test, the edge was noise.

### What was rejected

The DFS-shaped rows in the K279 wave were noise, and that assessment stands. This wave is different: both items above are genuine techniques, not duplicate solvers.

No DFS optimizer repo appeared in this batch. Nothing is vendored.

### Boundary

**No auto-submit. No automated board scraping. A human types the ticket.** FILE only.

**Cemini posture:** FILE. **0 product Integrate GO.**
