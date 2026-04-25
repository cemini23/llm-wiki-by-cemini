---
title: "Amortizing Perpetual Options (AmPOs)"
type: source
tags: [pdf, options-derivatives, perpetual-options, defi, panoptic, installment-options, greeks, black-scholes]
clusters: [options-derivatives]
related: []
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

*(Cross-references will be added in Phase 2.)*

## Raw Concept

- **Original title**: Amortizing Perpetual Options
- **Author(s)**: Zachary Feinstein (Stevens Institute of Technology, School of Business)
- **Type**: PDF (arXiv:2512.06505v2 [q-fin.PR])
- **Location**: research for cemini/greeks 10 3:29.pdf
- **Length**: 12p
- **Retrieved**: 2026-04-23
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: options-derivatives

## Narrative

Introduces **AmPOs (Amortizing Perpetual Options)**, a novel exchange-tradable perpetual-option design. Standard continuous-installment (CI) options require the holder to pay a continuous stream cₜdt to the underwriter to keep the contract alive, granting dual optionality (exercise or lapse). The fatal flaw for exchanges is fungibility: partial-payment lapsing means notional units are not identical, so CI options only trade OTC. Feinstein's construction replaces the explicit installment with an *implicit* amortization of the claimable notional — the holder effectively sells a fraction of their holdings back to the underwriter at the current premium, at rate proportional to the amortization rate α. All units then evolve identically, preserving fungibility.

Key technical result: **AmPOs reduce to vanilla perpetual American options on a dividend-paying asset** with the amortization rate α acting analogously to a dividend yield. This reduction yields closed-form exercise boundaries and BSM-framework closed-form Greeks. Comparative statics with respect to α: higher α tightens the exercise boundary (faster amortization → earlier optimal exercise) and modulates the effective volatility sensitivity in a non-monotone way. Positions the design against Everlasting Options [Paradigm/White 2021] and Panoptic [Lambert 2023] as a third perpetual-option primitive with the explicit advantage of being exchange-listable rather than AMM-bound.

Provisional US patent filed. Relevant to Cemini because perpetual options on crypto and prediction markets are a Cemini target-venue class; the AmPO design solves the fungibility blocker that currently prevents Panoptic-style perpetuals from trading on standard CLOB venues. Honest limits: (a) no empirical calibration to real market data; (b) closed-form results depend on BSM (constant-vol, no jumps); (c) the amortization-rate selection problem is punted to §4.1 with only heuristic guidance; (d) patent-pending status is flagged for IP-awareness but means open adoption is constrained.

## Key findings

- AmPOs = fungible perpetual-option variant of CI options: implicit amortization of claimable notional replaces explicit installment payments and removes lapsing logic.
- **Key equivalence**: AmPO value reduces to vanilla perpetual American option on dividend-paying asset, α ↔ dividend yield. → closed-form exercise boundaries and Greeks under BSM.
- Direct conceptual comparison with Everlasting Options and Panoptic; AmPO's novelty is exchange-listability (fungibility) with positive cost-of-carry.
- Amortization rate α shapes both exercise boundary (monotone tightening) and effective vega (non-monotone).
- Provisional US patent filed by Feinstein — adoption constraint flagged.
- Target markets: crypto perpetuals (Hyperliquid, Binance), DeFi perpetual-option protocols, potentially traditional installment-warrant venues.
- Relevance to Cemini: if perpetual-options venues come online that adopt AmPO structure, the closed-form BSM Greeks are directly consumable by the options feature pipeline (no MC required).

## Snippets

- **Abstract** — "AmPOs replace explicit installment payments and the need for lapsing logic with an implicit payment scheme via the decay of the claimable notional. This amortization ensures all units evolve identically, preserving fungibility."
- **Abstract** — "We demonstrate that AmPO valuation can be reduced to an equivalent vanilla perpetual American option on a dividend-paying asset."
- **§1** — "lapsing destroys fungibility across units of notional, i.e. partial lapsing by making a partial installment payment is not permissible, traditional CI options are not amenable to exchange-based trading."
- **§1** — "Instead of directly paying the continuous installments, the option holder implicitly sells a fraction of his or her option holdings back to the underwriter at the current premium."
- **Footnote** — "Portions of this work are the subject of a provisional U.S. patent application filed by the author."
