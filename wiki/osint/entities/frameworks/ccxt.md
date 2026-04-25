---
title: CCXT
type: entity
tags: [library, framework, crypto, exchange-connectivity]
keywords: []
related:
  - sources/3-18-crypto-integration-technical-audit.md
  - sources/3-19-compliance-research.md
  - entities/platforms/hyperliquid.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-18-crypto-integration-technical-audit.md
- @sources/3-19-compliance-research.md
- @entities/platforms/hyperliquid.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: frameworks.

## Narrative

CCXT is the Python crypto-exchange-connectivity library providing a
normalized interface over 100+ venues. Cemini uses CCXT to abstract
Hyperliquid, Binance, Bybit, and Coinbase Advanced behind a single
order-submission and market-data surface.

Documented choices:
- **Only-CEX** venues go through CCXT. Hyperliquid (on-chain perp DEX)
  uses its native SDK + CCXT's contributed adapter simultaneously —
  orders double-sign for the tamper-evident audit trail.
- **Rate-limit budgeting** — CCXT's built-in throttling is
  supplemented by a Redis-backed global rate-limit layer because
  multiple strategy instances share credentials.
- **Deal-killer flag** per the compliance research: CCXT's MIT license
  is clean, but some venue-specific adapters bundle venue-provided
  snippets with murkier licenses — the IP-sale due-diligence ledger
  tracks these per-adapter.

## Snippets

*(populate as source stubs are deep-read.)*
