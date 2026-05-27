---
title: "Prediction Markets — Wolfers & Zitzewitz (NBER w10504, 2004)"
type: source
tags: [source, prediction-markets, market-efficiency, nber, academic]
keywords: [wolfers-zitzewitz, nber-10504, winner-takes-all, index-contracts, spread-betting, conditional-markets]
related:
  - concepts/prediction-markets-efficiency-wolfers-zitzewitz.md
  - entities/platforms/polymarket.md
  - concepts/polymarket-microstructure-findings.md
maturity: core
read_status: deep-read
created: 2026-05-27
updated: 2026-05-27
clusters: [prediction-markets, quant-finance]
---

## Relations

- @concepts/prediction-markets-efficiency-wolfers-zitzewitz.md — synthesized reference
- @entities/platforms/polymarket.md — modern CLOB PM; contract types map to classic IA literature
- @concepts/polymarket-microstructure-findings.md — microstructure layer built atop efficiency priors

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Prediction Markets |
| Authors | Justin Wolfers, Eric Zitzewitz |
| Venue | NBER Working Paper 10504; prepared for *Journal of Economic Perspectives* |
| Date | May 2004 |
| URL | https://www.nber.org/papers/w10504 |
| Pages | 28 |
| Location | `research to be indexed/w10504.pdf` → `cemini-librarian:/opt/cemini-bulk/research/w10504.pdf` |
| Read | 2026-05-27, deep-read (intro + contract taxonomy + efficiency evidence) |

## Narrative

Canonical **survey of prediction-market design and empirical accuracy** (IEM, Tradesports, NewsFutures, corporate/internal markets, DARPA Policy Analysis Market controversy). Core claim: **market-generated forecasts are typically accurate** and beat most moderately sophisticated benchmarks when markets are liquid and well-designed.

**Contract taxonomy (Table 1):**

| Type | Price reveals | Example |
|------|---------------|---------|
| Winner-takes-all | Risk-neutral **probability** P(event) | $p pays $1 iff Gore wins |
| Index | **Mean** E[y] | Payoff scales with vote share |
| Spread | **Median** (even-money spread bets) | Cutoff y* for Gore % |

Families of winner-takes-all or spread contracts can reconstruct **full distributions** and uncertainty. **Conditional markets** can surface beliefs about regression coefficients (correlation vs causation caveat noted).

**Design lessons for Cemini:** Polymarket/Kalshi prices are winner-take-all–like binaries; interpret mid as probability only under risk-neutrality and small-stakes assumptions. Combinatorial/conditional structures in the paper inform multi-leg and basket research. DARPA PAM section documents political failure mode of PM deployment — relevant to compliance narrative.

## Snippets

> "We show that market-generated forecasts are typically fairly accurate, and that they outperform most moderately sophisticated benchmarks." [Source: w10504.pdf abstract]

> "The price on a winner-take-all market represents the market's expectation of the probability that an event will occur (assuming risk neutrality)." [Source: w10504.pdf p.3]
