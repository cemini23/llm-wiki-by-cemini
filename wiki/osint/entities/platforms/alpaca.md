---
title: Alpaca
type: entity
tags: [platform, equities, broker, cemini-venue]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/fintech-startup-legal-ip-roadmap.md
  - concepts/ip-sale-readiness.md
  - entities/platforms/interactive-brokers.md
maturity: validated
created: 2026-04-23
updated: 2026-04-27
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/fintech-startup-legal-ip-roadmap.md — K7 deep-read 2026-04-27 — K7 frames Alpaca + QuantConnect as the **developer-tier** API alternative appropriate for prototyping but **not for institutional liquidity / routing**; the K7 prescription is to upgrade to IBKR Pro corporate account under the Florida OpCo for the IP-sale-prep institutional-grade execution layer. Alpaca remains the deployed Cemini equities path; IBKR is prescribed-but-not-deployed.
- @concepts/ip-sale-readiness.md
- @entities/platforms/interactive-brokers.md — K7 prescription 2026-04-27 — IBKR is the institutional-grade upgrade path from Alpaca; LEI-gated onboarding; TWS API + (optional) FIX CTCI for low-latency routing; Professional Subscriber market-data fee tier

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: platforms.

## Narrative

Alpaca is a US equities + options broker with a commission-free API-first
model. Within Cemini it's the primary equities execution venue, wired
through the same LangGraph scatter-gather topology as Hyperliquid and
OANDA. Paper and live accounts share the same API surface, which enables
the testing discipline the compliance research recommends: every live
strategy must first accumulate a shadow-paper record under the same
regime-gating rules before capital is allocated.

Key integration points documented: IEX market data feeds (free tier),
fractional share support for Kelly-fractional position sizing, and
regulatory reporting hooks that produce CSV exports suitable for the
milestone ledger that underpins the IP-sale narrative.

## Snippets

*(populate as source stubs are deep-read.)*
