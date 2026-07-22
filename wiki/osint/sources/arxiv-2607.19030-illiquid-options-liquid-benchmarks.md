---
title: "arXiv 2607.19030 — Pricing options on illiquid assets via liquid benchmarks"
type: source
tags: [source, arxiv, options, energy, xsp, k182]
keywords: [2607.19030, Gasoil, Brent, crack-spread, local-volatility, Bachelier]
related:
  - concepts/xsp-lane-trading-framework.md
maturity: draft
read_status: read
created: 2026-07-22
updated: 2026-07-22
clusters: [k182-ingest]
---

## Relations

- @concepts/xsp-lane-trading-framework.md

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | 2607.19030 |
| **sha256** | `ed909e27c9293de7b50ec7e0dd0ba196ce00a7be41d51c7a028e8b823fdccea4` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.19030-pricing-options-on-illiquid-assets-using-liquid.pdf` |

## Narrative

Map liquid Brent IV → illiquid Gasoil IV via correlated Bachelier local-vol + crack-spread clusters — without using sparse Gasoil quotes as calibration inputs. **xsp steal:** when Mini-SPX/XSP liquidity thins, prefer liquid SPX/ES surface as benchmark mapper rather than forcing direct sparse-quote calibration. Context only — no energy book.
