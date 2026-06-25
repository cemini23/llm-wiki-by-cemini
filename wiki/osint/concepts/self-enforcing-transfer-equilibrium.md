---
title: Self-Enforcing Transfer Equilibrium (SETE / M-SETE)
type: concept
tags: [concept, game-theory, mechanism-design, poker, k129]
keywords: [SETE, M-SETE, internal transfers, Nash equilibrium, price of anarchy, polymatrix, MIT]
related:
  - sources/arxiv-equilibrium-internal-transfers-seate-2606.20960-2026-06-25.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/garip-running-average-self-play.md
  - concepts/active-project-research-routing.md
maturity: draft
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- @sources/arxiv-equilibrium-internal-transfers-seate-2606.20960-2026-06-25.md — primary source (arXiv 2606.20960)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — multi-player incentive alignment vs scalar chip EV
- @concepts/multi-agent-fictitious-play-llm.md — complementary equilibrium-learning cluster

## Raw Concept

Prompted by arXiv **2606.20960** (K129). Nash equilibria can be **arbitrarily inefficient** (high Price of Anarchy). SETE augments games with **budget-balanced peer-to-peer transfers** paid only if recipients follow prescribed strategies.

## Narrative

**Solution hierarchy:**

| Concept | Enforcement | Property |
|---------|-------------|----------|
| **SETE** | Self-enforcing transfers among players | Any social optimum sustainable in polymatrix games; NE in agent normal form |
| **M-SETE** | Mediator binds payment schedule + strategies | NE of augmented game itself; supports any social optimum in finite games |

Polynomial-time algorithms and decentralized learning dynamics compute product-form equilibria in polymatrix settings [TENTATIVE — theory paper, no poker sim].

**Poker steal (conceptual, not implemented):**

- Multi-way **side-payment metaphors** for coalition stability in 6-max training pools — e.g., chip-EV transfer schedules that align exploitative deviators with table-wide exploitability targets
- Contrasts with K124 MAFP (fictitious play without transfers) and K127 GARIP (gradient magnet)
- Arena Researcher Round has **no transfer mechanism** — steal is offline thought experiment for self-play pool design

**Cemini posture:** **REFERENCE** — game-theoretic primitive for poker-arena incentive design notes; no prod deploy.

## Snippets

> "We introduce Self-Enforcing Transfer Equilibrium (SETE), where players commit to nonnegative peer-to-peer transfers that are paid only if the recipient does not deviate from a prescribed strategy." [Source: arXiv:2606.20960 abstract (retrieved 2026-06-25)]

> "Internal transfers improve welfare and computation while preserving independent play on the equilibrium path." [Source: arXiv:2606.20960 abstract (retrieved 2026-06-25)]
