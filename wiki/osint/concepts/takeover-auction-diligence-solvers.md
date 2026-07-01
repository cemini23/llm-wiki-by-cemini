---
title: Takeover auction diligence and solver selection (K138)
type: concept
tags: [concept, game-theory, auctions, poker, cfr, ppo, k138, reference-only]
keywords: [due diligence, deal games, OpenSpiel, PPO, PPG, CFR, exploitability, imperfect information, M&A auction]
related:
  - sources/arxiv-takeover-auction-diligence-2606.29457-2026-07-01.md
  - concepts/nash-equilibrium-solver-selection.md
  - concepts/projected-exploitability-descent.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
maturity: draft
created: 2026-07-01
updated: 2026-07-01
---

## Relations

- @sources/arxiv-takeover-auction-diligence-2606.29457-2026-07-01.md — Naboulsi (2606.29457)
- @concepts/nash-equilibrium-solver-selection.md — K136 Nash-polytope / solver-family cluster

## Raw Concept

What prompted this page: K138 arXiv **2606.29457** links **economic diligence depth** (private signals purchased pre-auction) to **computational intractability** (same signal count blows up strategy space) and benchmarks **exact vs policy-gradient** solvers on deal-auction games.

## Narrative

### Two questions, one lever

Each diligence unit = one private signal → exponential strategy growth. Economically optimal diligence is **modest**; exact solvers fail at **much larger** signal counts than profit-maximizing diligence — questions meet on one axis at different points.

### Solver hierarchy (enumerable games)

| Rank | Family | Note |
|------|--------|------|
| 1 | CFR, MMD, PSRO | Lowest exploitability + fastest wall-clock when tabular |
| 2 | PPO, PPG | Best **learning** solvers; do not beat exact tabular methods |
| 3 | Deep CFR, NFSP | Weaker at equal episode budget |

**Scaling:** PPO per-target wall-clock ~flat vs CFR steep — interest is **post-enumeration** only; largest tabular instance PPO misses exploitability target.

### Intractable regime

Multi-signal auction: PPO/PPG + calibrated LBR → exploitability estimate below naive bidder (**lower bound**). Honest reporting — not Nash certificate.

### Cemini / poker relevance

- Reinforces K136 literacy: **do not substitute PPO self-play for CFR baselines** on toy games without exploitability measurement.
- Deal-game repo (`imperfect-information-deal-games`) = optional OpenSpiel spike env — not Arena NLHE.
- Diligence-cost curve = metaphor for **information-buying** in chart research (bounded private signals).

**Posture:** REFERENCE — brief steal → `agents/devfun-poker-arena/briefs/`.

## Snippets

> "The economically optimal amount of diligence is modest, while the game outruns exact solvers only at much larger signal counts." [Source: arxiv-2606.29457-1-introduction.pdf §1 (retrieved 2026-07-01)]
