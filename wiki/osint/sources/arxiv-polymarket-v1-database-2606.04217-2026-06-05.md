---
title: Polymarket-v1 database — research dataset (arXiv 2606.04217, REFERENCE)
type: source
tags: [source, arxiv, polymarket, microstructure, cross-wiki-route]
keywords: [2606.04217, polymarket, database, vpin, aggressor-direction]
related:
  - concepts/polymarket-microstructure-findings.md
maturity: validated
read_status: read
created: 2026-06-05
updated: 2026-06-05
---

## Relations

- @gambling-wiki/sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md — gambling-wiki primary (K100)
- @gambling-wiki/concepts/polymarket-v1-research-database.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Polymarket-v1 Database |
| **Authors** | Boka Qin; Rui Yang (Time Seventeen) |
| **arXiv** | 2606.04217 |
| **Dataset** | https://huggingface.co/datasets/TimeSeventeen/Polymarket-v1 |
| **Span** | 2022-11-21 → 2026-04-28 (CTF Exchange v1 lifecycle) |
| **Scale** | 1.20B trades · 1.30M markets · ~$61B nominal volume |
| **Read status** | read — abstract + intro + benchmark findings (OSINT cross-wiki) |

## Narrative

**Cross-wiki:** full ingest on `@gambling-wiki`. OSINT keeps **measurement-layer** takeaways for Cemini research vs **live Gamma/CLOB** execution paths.

**Defining property:** **ground-truth aggressor side** from on-chain settlement — existing PM archives infer direction heuristically (~coin-flip accuracy).

**Three findings relevant to OSINT PM stack:**

1. **Tick rule / bulk volume classifiers** ≈ 50% aggregate accuracy — errors follow a **price-level gradient** (PM positive direction autocorrelation + concentrated MM violate mean-reversion assumptions).
2. **Downstream metrics break** — inferred VPIN diverges from true VPIN; OFI biased → TCA conclusions unreliable.
3. **True microstructure predicts calibration** — true VPIN ↑ Brier scores; Gibbs spread ↓ Brier (niche high-spread markets attract informed specialists). Classified proxies **attenuate** both relationships.

**Cemini:** use dataset for **offline** microstructure research / backtests; prod bots must not assume tick-rule labels on live CLOB. Arctic/librarian ingest of HF dataset is **out of scope** until storage brief `[NEEDS VERIFICATION 2026-06-05]`.

## Snippets

> "Its defining feature is all ground-truth aggressor direction derived from the blockchain settlement layer."

> "The tick rule and bulk volume classification achieve near-random aggregate accuracy (49.83% and 50.51%)."

> — [Source: arxiv-2606.04217-polymarket-v1-database.pdf p.1, retrieved 2026-06-05]
