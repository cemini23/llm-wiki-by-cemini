---
title: "Optimal High-Frequency Market Making — Avellaneda-Stoikov + Inventory Control (Stanford GR5, 2018)"
type: source
tags: [source, market-making, hft, academic, k98]
keywords: [avellaneda-stoikov, gr5, stanford, inventory-risk, limit-order-book, spread-capture]
related:
  - concepts/avellaneda-stoikov-market-making-baseline.md
  - sources/stanford-ml-orderbook-mm-gr4-2017.md
  - concepts/order-book-pressure-ml-market-making.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - entities/data-sources/open-meteo.md
read_status: skimmed
maturity: draft
created: 2026-06-04
updated: 2026-06-07
---

## Relations

- @concepts/avellaneda-stoikov-market-making-baseline.md — canonical formulas + Cemini mapping
- @sources/stanford-ml-orderbook-mm-gr4-2017.md — sibling Stanford MM project (OBP ML overlay, K104)
- @concepts/order-book-pressure-ml-market-making.md — LOB directional skew synthesis
- @concepts/polymarket-market-making-architectures.md — MIT OSS PM MM refs build on same theoretical core

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Optimal High-Frequency Market Making |
| Authors | Takahiro Fushimi, Christian González Rojas, Molly Herman (Stanford) |
| Filename | gr5.pdf |
| Date | 2018-06-11 |
| Retrieved | 2026-06-04 |
| Location | `cemini-librarian:/opt/cemini-bulk/research/gr5.pdf` |
| read_status | skimmed |

## Narrative

Student implementation paper: **Avellaneda & Stoikov (2008)** optimal quoting integrated with a **proprietary inventory control** layer that dynamically scales order size to mitigate inventory risk. Trading simulator compares optimal vs baseline pricing on five representative equities; with inventory model, optimal quotes improve inventory management while staying profitable.

**Cemini relevance:** Theoretical baseline for `polymarket-lp-bot-phase0-spec` and logit-space MM notes on `@entities/data-sources/open-meteo.md` cross-links — use when calibrating spread skew vs inventory, not for PM 15-min latency bots directly.

## Snippets

> "integrates … Avellaneda and Stoikov (2008) … with a proprietary inventory control model that dynamically adjusts the order size to mitigate inventory risk"

[Source: gr5.pdf p.1, retrieved 2026-06-04]
