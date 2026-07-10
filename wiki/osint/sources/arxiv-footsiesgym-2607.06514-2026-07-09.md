---
title: FootsiesGym — fighting-game benchmark for 2p zero-sum imperfect-info (2607.06514)
type: source
tags: [source, arxiv, poker, game-theory, imperfect-information, k151]
keywords: [FootsiesGym, fighting game, zero-sum, imperfect information, benchmark, exploitability, PFSP]
related:
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - sources/arxiv-lightweight-game-agent-2607.06854-2026-07-09.md
  - sources/arxiv-policy-representation-2607.01498-2026-07-07.md
maturity: validated
read_status: skimmed
created: 2026-07-09
updated: 2026-07-09
---

## Relations

- @concepts/poker-arena-multi-axis-cognitive-profile.md — Raeth M₁–M₉ steal target
- @sources/arxiv-lightweight-game-agent-2607.06854-2026-07-09.md — paired lightweight-agent ablations
- @concepts/devfun-researcher-track-readiness-2026-06.md — Researcher Round eval posture

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.06514](https://arxiv.org/abs/2607.06514) |
| **Code** | https://github.com/como-research/FootsiesGym |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.06514-footsiesgym-a-fighting-game-benchmark-for-two-pl.pdf` |

## Narrative

Two-player zero-sum **imperfect-information** fighting-game benchmark (not poker). Isolates cyclic non-transitive “neutral game” RPS while staying cheap to train. Shared eval primitives with HU poker: hidden state, commitment timing, approximate exploitability.

### Env API (steal literacy)

| Piece | Spec |
|-------|------|
| Actions | \|A\|=6 default; optional \|A\|=9 with special-charge toggles |
| Obs | 85-d (88 w/ charge): common + shared×2 + **privileged self** (dash, charge, prev action) not shown to opponent |
| Rewards | Zero-sum; ±w terminal; timeout 0 |
| Action delay | Select→execute lag; delay 0 collapses to pure react; higher forces prediction/commitment |
| API | PettingZoo + vectorized headless Unity/gRPC |

### Eval findings that transfer

1. **H2H skill ≠ exploitability** — EMAgnet beat PPO variants head-to-head yet was most exploited by approximate best-response. [CONFIRMED]
2. **PFSP / population curriculum** improves robustness vs single-checkpoint self-play.
3. **Reactive collapse** vs stationary opponents — win-rate alone misleads.

**Cemini steal (K151):** map API → Raeth axes in `agents/devfun-poker-arena/references/footsiesgym-raeth-axis-map.md`; add `exploitability_advisory` to `axis_summary.json` (advisory only). **Do not** install FootsiesGym or replace pokerkit.

## Snippets

> "A Fighting Game Benchmark for Two-Player Zero-Sum Imperfect-Information Games" [Source: arXiv:2607.06514 title]

> "Each agent additionally observes a small block of privileged self-features… These are not exposed in the opponent block, mirroring the information asymmetry present in human play." [Source: arXiv:2607.06514 §3 Observations]

> "EMAgnet has a positive return against both PPO variants, but is more consistently exploited." [Source: arXiv:2607.06514 §4 Approximate Exploitability]
