---
title: Anytime-valid agent evaluation in imperfect-information games (AV-AIVAT)
type: concept
tags: [poker, eval, k226, gambling]
keywords: [AV-AIVAT, AIVAT, anytime-valid, TrueSkill]
related:
  - sources/arxiv-2608.06362-av-aivat-2026-08-07.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-08-07
updated: 2026-08-20
---

## Relations

- @sources/arxiv-2608.06362-av-aivat-2026-08-07.md
- @concepts/code-as-agent-harness.md

## Raw Concept

2608.06362: anytime-valid stopping + AIVAT variance reduction → ~74× cheaper agent comparison in II-games.

## Narrative

Fixed-budget agent-vs-agent matches either keep paying after the result is settled or stop too early; peeking an ordinary CI invalidates coverage. AV-AIVAT pairs **AIVAT** (action-informed, conditionally mean-zero corrections) with **confidence sequences** so an evaluation can stop when evidence suffices and still hand a third party a recheckable claim.

Paper numbers (HUNL, 15 LLM-agent configs, 71,439 paired hands): AIVAT cuts variance by a **median 54×**. At 95% / ±1 BB, raw outcomes need a **median 74×** as many hands as AIVAT-corrected outcomes to stop under the asymptotic CS. The exact Empirical-Bernstein CS is much less generous (**~1.37×**) because a declared payoff bound imposes a width floor — variance reduction does not automatically become earlier stopping. The online value model may use games `1:t−1` only; **game t must not score its own correction**. Naive peeking of a fixed-sample interval produced **61% false positives** under the null in their rolling-leaderboard sim; recomputing the CS at the reported stop overturned those claims.

**Poker Arena:** steal the *stopping + release protocol* (corrected prefix, rule, bound, CS settings) for sandbox LB / `decide()` A-B — not a mandatory clone. Do not use the current hand’s outcome to fit the correction. CCC: eval-budget discipline; anytime-valid > naive CI peeking.

[Source: arXiv:2608.06362 (abstract + §1, retrieved 2026-08-20)]
