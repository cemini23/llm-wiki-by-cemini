---
title: GARIP — running-average magnet for zero-sum self-play convergence
type: concept
tags: [concept, game-theory, self-play, poker, marl, k127]
keywords: [GARIP, running average, Polyak magnet, R-NaD, DeepNash, MMD, last-iterate convergence, exploitability]
related:
  - sources/arxiv-garip-self-play-2606.22688-2026-06-23.md
  - concepts/emagnet-parameter-space-ema-self-play.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - meta/sandbox-season-harvest-cadence.md
  - sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
  - concepts/active-project-research-routing.md
  - concepts/self-enforcing-transfer-equilibrium.md
  - sources/arxiv-emagnet-parameter-space-ema-2606.23995-2026-06-25.md
  - sources/arxiv-equilibrium-internal-transfers-seate-2606.20960-2026-06-25.md
maturity: draft
created: 2026-06-23
updated: 2026-10-25
---

## Relations

- @sources/arxiv-garip-self-play-2606.22688-2026-06-23.md — primary source (Savcı)
- @concepts/emagnet-parameter-space-ema-self-play.md — K129 parameter-space EMA magnet (orthogonal to mixture-space running average)
- @concepts/multi-agent-fictitious-play-llm.md — K124 fictitious-play cluster (orthogonal axis: stance vs gradient magnet)
- @meta/sandbox-season-harvest-cadence.md — post-10k harvest for offline GARIP/chart iteration

## Raw Concept

Prompted by arXiv **2606.22688** (K127). Last-iterate self-play in two-player zero-sum games **cycles** without reference regularization.

## Narrative

**Reference policy ablation grid:**

| Method | Magnet | Opponent |
|--------|--------|----------|
| MMD | Fixed | varies |
| R-NaD | Periodic snapshot | current |
| **GARIP** | **Running average (Polyak)** | **average opponent** |

**Mechanism insight:** convergence collapse tracks **peak lag** of the reference; running average minimizes peak lag among causal convex averages with fixed mean lag.

**Poker steal (offline, regime-conditioned):**

- Maintain **running-average villain action mixture** as chart anchor (vs periodic snapshot or fixed population prior)
- Pair with K124 MAFP stance rounds and K125 trajectory verifier before Arena submit
- Target axis: **exploitability** / worst-case bb/100 vs adaptive lag

No public code — pattern brief only.

## Snippets

> "Replacing the running average by a periodic snapshot recovers R-NaD; replacing it by a fixed distribution recovers MMD." [Source: arXiv:2606.22688 §intro (retrieved 2026-06-23)]
