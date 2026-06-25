---
title: EMAgnet — parameter-space EMA magnet for self-play regularization
type: concept
tags: [concept, game-theory, self-play, poker, marl, k129]
keywords: [EMAgnet, EMA, uniform magnet, PPO self-play, exploitability, dominated strategies, Riot Games]
related:
  - sources/arxiv-emagnet-parameter-space-ema-2606.23995-2026-06-25.md
  - concepts/garip-running-average-self-play.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/active-project-research-routing.md
  - sources/arxiv-garip-self-play-2606.22688-2026-06-23.md
maturity: draft
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- @sources/arxiv-emagnet-parameter-space-ema-2606.23995-2026-06-25.md — primary source (arXiv 2606.23995)
- @concepts/garip-running-average-self-play.md — complementary magnet axis (parameter EMA vs running-average policy mixture)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — exploitability / strategic-mixing axis target

## Raw Concept

Prompted by arXiv **2606.23995** (K129). PPO self-play with **uniform entropy regularization** is strategically agnostic — it pulls equally toward dominated actions. EMAgnet regularizes toward an **EMA of policy parameters** instead.

## Narrative

**Magnet comparison (K127 GARIP cluster):**

| Method | Regularization target | Weakness |
|--------|----------------------|----------|
| Uniform entropy | Flat action distribution | Wastes capacity on dominated strategies |
| R-NaD snapshot | Periodic policy copy | Peak lag from stale snapshot |
| **GARIP** | Running-average policy | Mixture-space anchor (K127) |
| **EMAgnet** | **EMA of last-iterate parameters** | Adaptive, strategy-aware magnet |

EMAgnet outperforms uniform-magnet PPO on exploitability across standard IIG benchmarks and games with large dominated-strategy sets [TENTATIVE — single paper, arXiv 2606.23995].

**Poker steal (offline, regime-conditioned):**

- Fold **parameter-space EMA decay** into GARIP chart refinement (`--garip-alpha-decay`) — mixture-space analogue, not full HF PPO training
- Pair with K124 MAFP stance rounds + K125 trajectory verifier before Arena submit
- Target axis: **exploitability** / worst-case bb/100 vs adaptive lag

**Cemini posture:** **REFERENCE / steal-from** — pattern brief only; Riot Games industrial setting ≠ NLHE Arena without sim validation.

## Snippets

> "EMAgnet, which instead regularizes toward an exponential moving average (EMA) of the last-iterate policy's parameters, providing an adaptive regularization target that evolves with the agent's improving strategy." [Source: arXiv:2606.23995 abstract (retrieved 2026-06-25)]

> "Relative to PPO self-play with uniform-magnet regularization … EMAgnet achieves lower exploitability in the majority of tested environments." [Source: arXiv:2606.23995 abstract (retrieved 2026-06-25)]
