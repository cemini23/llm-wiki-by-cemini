---
title: AS and Cartea–Jaimungal forced uniqueness — inventory MM (arXiv 2606.01477)
type: source
tags: [source, arxiv, market-making, inventory-risk, avellaneda-stoikov, cartea-jaimungal]
keywords: [2606.01477, forced-uniqueness, entropic-certainty-equivalent, phi-gamma, inventory-penalty]
related:
  - concepts/avellaneda-stoikov-market-making-baseline.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/market-informedness-market-making.md
maturity: validated
read_status: deep-read
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @concepts/avellaneda-stoikov-market-making-baseline.md — ϕ–γ forcing updates production calibration cross-check
- @concepts/polymarket-lp-bot-phase0-spec.md — LP skew / inventory penalty parameter discipline
- @concepts/market-informedness-market-making.md — preference layer sits above informed-flow microstructure

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Avellaneda–Stoikov and Cartea–Jaimungal as One Framework: A Forced Uniqueness Theorem for Inventory Market Making |
| **Author** | Frank M.V. Feys |
| **arXiv** | 2606.01477 |
| **sha256** | `28fe4d3571911f2b2ba8b90ff0bd445c80117c6fd37f88316669ff234a911b75` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/2606.01477v1.pdf` |
| **Retrieved** | 2026-06-11 |
| **Read status** | deep-read — abstract, axioms, executive summary, corollaries |

## Narrative

Axiomatic preference theory for inventory market makers: five axioms (cash-additivity, normalization, concavity, strong dynamic consistency, law-invariance) **force** the entropic certainty-equivalent on liquidation-adjusted terminal wealth, parametrized by a single **γ**. The Avellaneda–Stoikov (AS) framework is the unique representative; Cartea–Jaimungal (CJ) is its **second-order Taylor expansion** in inventory magnitude with:

| Parameter | Forced relation | Interpretation |
|-----------|-----------------|----------------|
| Running penalty **ϕ** | **ϕ = γσ²/2** | Preference parameter disguised as market parameter |
| Terminal penalty **α** | **α = ½ L″(0)** | Genuine microstructure property of liquidation cost **L** |
| Cross-check | **γ = 2ϕ/σ²** | Desk consistency test when ϕ and γ calibrated independently |

**Cemini mapping:** PM LP quoters treating (ϕ, α, γ) as three free knobs are **over-parametrized**. Use γ (or ϕ) as single risk dial; treat α as venue-specific liquidation curvature from fill-handler telemetry, not a taste parameter. Clock-invariance of γ w.r.t. quadratic-variation clock is a derived property — stochastic-vol CJ extensions may violate it `[TENTATIVE — paper Proposition 37; not independently verified]`.

**Posture:** REFERENCE — steal the **ϕ–γ consistency cross-check** for conviction/LP config reviews; no code adoption.

## Snippets

> "The running-penalty coefficient ϕ and the risk-aversion parameter γ are not independent: ϕ = γσ²/2."

> — [Source: 2606.01477v1.pdf Abstract, retrieved 2026-06-11]

> "A practitioner calibrating (ϕ, α, γ) as three free parameters is therefore over-parametrizing on both sides of the preference–market boundary."

> — [Source: 2606.01477v1.pdf Executive summary, retrieved 2026-06-11]
