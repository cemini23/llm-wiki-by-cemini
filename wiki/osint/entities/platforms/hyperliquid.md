---
title: Hyperliquid
type: entity
tags: [platform, crypto, perpetuals, dex, cemini-venue]
keywords: []
related:
  - sources/3-18-crypto-integration-technical-audit.md
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - concepts/cryptographic-audit-trail.md
  - concepts/ip-sale-readiness.md
  - entities/frameworks/ccxt.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-18-crypto-integration-technical-audit.md
- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @concepts/cryptographic-audit-trail.md
- @concepts/ip-sale-readiness.md
- @entities/frameworks/ccxt.md

## Raw Concept

Synthesized from 4 source(s) referencing this entity across the Cemini research corpus. Category: platforms.

## Narrative

Hyperliquid is a high-performance on-chain perpetuals DEX with sub-second
block times and a fully on-chain orderbook. Cemini integrates via
**Hyperliquid Agent Wallets** — a delegated-signing pattern that lets the
trading agent submit orders from a hot wallet without exposing the master
seed. Orders are EIP-712 signed, routed through Flashbots Protect RPC to
mitigate MEV, and every on-chain transaction is logged into pg_tamperlog
before going to the Merkle-anchored audit ledger.

The venue is central to the crypto execution layer described in the 3-18
crypto integration technical audit: AES-GCM vault for agent-wallet private
keys, Web3.py for signing, CCXT for a normalized interface alongside
Binance/Bybit, and strict regime-gating through the Macro Weather system
before any perpetuals position is opened.

## Snippets

*(populate as source stubs are deep-read.)*
