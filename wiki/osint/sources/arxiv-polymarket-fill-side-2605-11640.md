---
title: "Fill-Side Non-Retail Trading on Polymarket — Behavioral Tiers & Microstructure (arXiv:2605.11640)"
type: source
tags: [source, arxiv, polymarket, microstructure, prediction-markets, trader-tiers, k48]
keywords: [polymarket, fill-side-analysis, non-retail-trading, whale-tier, behavioral-tiers, quote-attribution, orderfilled-events, nechepurenko]
related:
  - concepts/polymarket-microstructure-findings.md
  - concepts/prediction-market-information-leakage-score.md
  - sources/arxiv-foresightflow-ils-polymarket-2605.00493.md
maturity: validated
read_status: skimmed
created: 2026-05-15
updated: 2026-05-23
---

## Relations

- @concepts/polymarket-microstructure-findings.md — adds an empirical fill-side trader-tier finding to the wiki's Polymarket microstructure understanding

## Raw Concept

- **Title**: Fill-Side Non-Retail Trading on Polymarket: An Empirical Study of Behavioral Tiers and Microstructure Signatures Under Quote-Attribution Constraints
- **Author**: Maksym Nechepurenko
- **Type**: arXiv preprint — arXiv:2605.11640
- **Submitted**: 2026-05-12
- **Retrieved**: 2026-05-15 (Tier-2 arXiv sweep `@sweeps/2026-05-15.md`, Q4 #1)
- **Read status**: skimmed (abstract-level)

## Narrative

An empirical microstructure study of **13.36M OrderFilled events** across 77,204 addresses and 43,116 markets on Polymarket (2026-04-21 to 04-27).

Key findings:
- **Architectural limit**: Polymarket's off-chain order architecture prevents address-level quote-lifecycle attribution — analysis is restricted to *fill-side* metrics. The author withdrew market-making claims and downgraded manipulation-detection accuracy because of this.
- **Behavioral clustering**: density-based clustering found a *single* behavioral mode, contradicting the expected distinct trader archetypes.
- **Tier stratification**: whale-tier + high-frequency-operator + power-trader tiers jointly hold **81.4% of total notional across just 12.6% of addresses** — a clean retail-vs-professional separation.

**Caveat**: single author (Nechepurenko — see also `@sources/arxiv-coordination-layer-multi-agent-2605-03310.md`); treat as single-source. The honest withdrawal of market-making/manipulation claims on architectural grounds is a positive credibility signal.

**Why it matters here**: the 81/13 notional concentration is a usable prior for any Polymarket strategy work and for the newsletter — "smart money" on Polymarket is a small, identifiable set of addresses.

## Snippets

> "whale-tier, high-frequency-operator, and power-trader tiers jointly hold 81.4% of total notional across 12.6% of addresses"
> — [Source: https://arxiv.org/abs/2605.11640 (retrieved 2026-05-15)]
