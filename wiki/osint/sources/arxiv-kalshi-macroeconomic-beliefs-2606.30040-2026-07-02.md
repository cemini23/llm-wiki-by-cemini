---
title: "The Shape of Macroeconomic Beliefs — arXiv 2606.30040"
type: source
tags: [arxiv, kalshi, macro, inflation, expectations, k140, pdf]
keywords: [Kalshi, CPI, core CPI, belief distribution, tail risk, Reuters Poll, prediction markets, Angelini]
related:
  - concepts/kalshi-implied-macro-belief-distributions.md
  - entities/platforms/kalshi.md
  - concepts/prediction-markets-efficiency-wolfers-zitzewitz.md
  - concepts/pm-capital-lock-up-settlement-discount.md
  - sources/arxiv-settlement-manipulation-pm-2606.31675-2026-07-01.md
maturity: draft
read_status: read
created: 2026-07-02
updated: 2026-07-02
clusters: [prediction-markets, kalshi, macro]
---

## Relations

- @concepts/kalshi-implied-macro-belief-distributions.md — primary synthesis
- @entities/platforms/kalshi.md — Kalshi CPI threshold contract panel

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Shape of Macroeconomic Beliefs |
| **Author** | Giovanni Angelini (University of Bologna) |
| **arXiv** | 2606.30040v1 |
| **Type** | PDF |
| **sha256** | `e8cb8d6291e50a005c8a3b5773773bf66fdfd8788fd9bfccc8a4db74857a7d38` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.30040-the-shape-of-macroeconomic-beliefs.pdf` |
| **Retrieved** | 2026-07-02 |
| **Read status** | read (abstract + intro + main results) |

## Narrative

Recovers **full subjective distributions** (not just means) for short-run CPI releases from **Kalshi adjacent-threshold contracts** — converting prices to probability mass over inflation bins from 30 days to 1 hour pre-release.

### Key findings

1. **Kalshi-implied means** beat simple moving-average benchmarks for headline CPI (RMSE 0.169 vs 0.274–0.331 pp); competitive for core CPI.
2. **Null on center:** lagged Reuters surprises do **not** systematically shift Kalshi mean away from current Reuters consensus (coef −0.023, SE 0.107 with FE).
3. **Distributional signal:** large lagged surprises → **higher implied uncertainty** and **higher upper-tail mass** (e.g. +0.1 pp lagged surprise → +4.7 pp on Pr(inflation > 0.3%)) even controlling for consensus.
4. **Validation:** Kalshi upper-tail probabilities predict high-inflation realizations when mean stays near consensus.

**Cemini relevance:** pm-kalshi bot — ingest **threshold ladder prices** for CPI release events as tail-risk overlay beyond point Reuters/consensus feeds; not a replacement for prod macro models.

Sample: 282 CPI + 240 core CPI snapshots across 46/39 releases.

## Snippets

> "The market's distinctive signal is not a persistent shift in the conditional mean relative to professional forecasters." [Source: arxiv-2606.30040-the-shape-of-macroeconomic-beliefs.pdf §1 (retrieved 2026-07-02)]

> "A 0.1 percentage point positive lagged surprise raises the probability of monthly inflation above 0.3 percent by about 4.7 percentage points." [Source: arxiv-2606.30040 abstract (retrieved 2026-07-02)]
