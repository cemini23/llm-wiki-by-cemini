---
title: K279 DFS / Parlays Wave (Oct 2026)
type: concept
tags: [dfs, parlays, gambling, k279]
keywords: [k279, breakeven, pickem, property-testing, extract]
related:
  - concepts/k278-ood-stub-wave.md
  - sources/eval-multi-repo-revenue-2026-10-03.md
  - sources/eval-repo-opportunity-2026-10-03.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k278-ood-stub-wave.md
- @sources/eval-multi-repo-revenue-2026-10-03.md
- @sources/eval-repo-opportunity-2026-10-03.md

## Raw Concept

K279 cluster hub for the DFS and parlay workstreams. Dual-ID **OSINT K279**.

## Narrative

Two eval docs, 40 rows. Most are noise. **Two techniques are worth building.**

### 1. Pick'em breakeven table (CeminiParlays)

A fixed-multiplier card is not a price. It is a payout structure, so comparing it to a sharp two-way line needs the **breakeven hit rate** for that card's multiplier and flex rules — not a de-vigged probability.

The build: a table of breakeven probabilities by card size (2-pick through 6-pick), by flex variant, and by platform settlement rule. For a flat multiplier `m`, the breakeven probability is `1/m`; the work is enumerating the variants, not the arithmetic.

Open question flagged by the eval: the specific breakeven weights for flex slips versus standard power plays on one platform.

### 2. Property-based testing of the copula and de-vig maths (CeminiParlays)

State the invariant, let the library generate inputs, and let it shrink any failure to the smallest counterexample. Assertions worth writing:

| Target | Property |
|--------|----------|
| De-vig | De-vigged probabilities sum to exactly 1.0 |
| De-vig | Raising one leg's implied price cannot lower its de-vigged probability |
| Gaussian copula | Joint hit rate sits between the product of marginals and the minimum marginal |
| Student-t copula | As degrees of freedom grow, it converges toward the Gaussian case |
| Correlation matrix | Any generated matrix is positive semi-definite |

This is the highest-value item in either doc. The copula code is where a silent numerical bug converts straight into mispriced tickets, and hand-picked unit tests are exactly what miss it.

### What was rejected, and why it matters

Two repos were **Pass** for the same reason: a naive score-regression model cannot beat a market-implied closing line and has no correlation structure. That is a standing argument for keeping the parlay stack on de-vigged market lines rather than internal score models.

The DFS optimizer repos were **Context** — CeminiDFS already runs multi-lineup generation, correlation stacking, and late swap. A second linear-programming solver adds regression risk, not edge. One row named "DFS" meaning depth-first search; irrelevant.

### Boundary

Nothing here is vendored. The breakeven table is derivable arithmetic and the property tests would be written by us. **No automated board scraping. The operator types the displayed lines. No auto-submit. A human types the ticket.**

**Cemini posture:** FILE. Zero clones. **0 product Integrate GO.**
