---
title: Kalshi
type: entity
tags: [platform, prediction-markets, exchange, cemini-venue]
keywords: []
related:
  - sources/3-10-algorithmic-trading-ip-sale-audit.md
  - sources/3-10-cryptographic-research.md
  - sources/3-17-competition-research.md
  - sources/3-19-alternative-data-for-prediction-markets-research.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-29-research-4.md
  - sources/3-9-pm-research.md
  - sources/kalshi-2-3-29.md
  - sources/kalshi-3-3-29.md
  - sources/kalshi-4-3-29.md
  - sources/osint-prediction-markets-trading-architecture.md
  - sources/cftc-anprm-prediction-markets-2026-03-16.md
  - sources/cftc-selig-house-ag-testimony-2026-04-16.md
  - sources/cftc-v-arizona-tro-liburdi-2026-04-10.md
  - concepts/favorite-longshot-bias.md
  - concepts/macro-weather-regime.md
  - concepts/ip-sale-readiness.md
  - concepts/dcm-state-preemption.md
  - entities/platforms/polymarket.md
  - entities/data-sources/open-meteo.md
  - concepts/ensemble-weather-forecasting.md
  - sources/3-19-signal-fusion-engine-research.md
  - sources/3-26-a.md
  - sources/ai-5-4-3.md
  - sources/ai-trading-ethics-4-5.md
  - sources/forex-1-4-4.md
  - sources/insights-from-a-gemini.md
  - sources/kalshi1-3-29.md
  - sources/trading-3-4-5.md
maturity: validated
created: 2026-04-23
updated: 2026-04-27
---

## Relations

- @sources/3-10-algorithmic-trading-ip-sale-audit.md — K6 2026-04-27 — Kalshi DCM status named in the audit's compliance-leverage discussion as a structural cleanliness factor for the IP-sale narrative (CFTC-jurisdiction venue is cleaner due-diligence story than offshore-unregistered alternatives); SEC Rule 3a5-4 sub-$50M dealer-registration carve-out works for the OpCo at Kalshi-volume scale
- @sources/3-10-cryptographic-research.md
- @sources/3-17-competition-research.md
- @sources/3-19-alternative-data-for-prediction-markets-research.md
- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-29-research-4.md
- @sources/3-9-pm-research.md
- @sources/kalshi-2-3-29.md
- @sources/kalshi-3-3-29.md
- @sources/kalshi-4-3-29.md
- @sources/osint-prediction-markets-trading-architecture.md
- @sources/cftc-anprm-prediction-markets-2026-03-16.md — March 12 2026 ANPRM (RIN 3038-AF65); the regulatory signal cascading to DCM Core Principles 3 & 4
- @sources/cftc-selig-house-ag-testimony-2026-04-16.md — Chairman defended ANPRM agenda + confirmed federal counter-suits vs AZ/CT/IL on the public record
- @sources/cftc-v-arizona-tro-liburdi-2026-04-10.md — first federal-court ruling in this cycle finding CFTC "likely to ultimately win" on preemption
- @concepts/favorite-longshot-bias.md
- @concepts/macro-weather-regime.md
- @concepts/ip-sale-readiness.md
- @concepts/dcm-state-preemption.md — the swap-vs-gambling structural dispute that determines whether role 3 (compliance-leverage) survives
- @entities/platforms/polymarket.md
- @entities/data-sources/open-meteo.md
- @concepts/ensemble-weather-forecasting.md

## Raw Concept

Synthesized from 12 source(s) referencing this entity across the Cemini research corpus. Category: platforms.

## Narrative

Kalshi is a CFTC-regulated designated contract market (DCM) for event
contracts — US-domiciled yes/no prediction markets on outcomes ranging from
weather and macroeconomic prints to elections and regulatory events. Within
Cemini it occupies three roles:

1. **Execution venue** — the Kalshi API (REST + WebSocket) is wired through
   the LangGraph scatter-gather topology alongside Alpaca and Hyperliquid;
   position sizing flows through the Kelly/CVaR risk engine.
2. **Alternative-data generator** — intraday price series on weather and
   event contracts provide a forward-looking signal layer that's fused with
   GDELT, FRED, and Open-Meteo ensembles before being dispatched to equity
   and crypto strategies.
3. **Compliance leverage point** — Kalshi's DCM status means event-contract
   trading sits under CFTC jurisdiction, which is structurally cleaner for
   an IP-sale-to-institutional-buyer story than operating on an unregistered
   offshore exchange. **As of 2026-04-25 this status is actively defended by
   federal counter-suit**: the CFTC has filed declaratory-judgment actions
   vs. Arizona, Connecticut, and Illinois (confirmed by Chairman Selig in
   House Ag testimony Apr 16; see `@sources/cftc-selig-house-ag-testimony-2026-04-16.md`),
   and a D. Ariz. TRO (Liburdi, Apr 10; see `@sources/cftc-v-arizona-tro-liburdi-2026-04-10.md`)
   found CFTC "likely to ultimately win" on preemption. The thesis
   strengthens conditional on preemption holding through SCOTUS and weakens
   to a state-by-state cascade if SCOTUS sides with states. See
   `@concepts/dcm-state-preemption.md` for the full structural framing and
   the brief at `briefs/2026-04-25_post-kalshi-advisory-regulatory-update.md`
   for the synthesis.

Key microstructure facts documented across the corpus: the 2024 election-
contract ruling cemented Kalshi's regulatory moat; tick sizes are \$0.01 on
binary contracts; settlement is cash-only at \$1.00/\$0.00 on resolution;
the venue exhibits a strong favorite-longshot bias that several Cemini
strategies explicitly monetize via Avellaneda-Stoikov market-making in logit
space.

## Snippets

*(populate as source stubs are deep-read.)*
