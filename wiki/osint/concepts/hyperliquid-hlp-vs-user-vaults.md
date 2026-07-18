---
title: "Hyperliquid — HLP vs user vaults vs DIY copy"
type: concept
tags: [concept, hyperliquid, vaults, copy-trading, funding, k165]
keywords: [hlp, user-vaults, diy-mirror, 10-percent-perf-fee, 4-day-lockup, min-notional]
related:
  - sources/gemini-dr-pm-hl-strategies-2026-07-14.md
  - sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md
  - sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md
  - concepts/cemini-pm-lp-vs-copy-capital-decision.md
  - entities/platforms/hyperliquid.md
  - entities/tools/hyperliquid-python-sdk.md
  - concepts/perp-dex-price-discovery-lead-lag.md
  - sources/substack-rss-wublock-2026-07-17-weekly-iranian-wallets.md
maturity: draft
created: 2026-07-14
updated: 2026-07-18
clusters: [hyperliquid]
---

## Relations

- @entities/platforms/hyperliquid.md — venue + Agent Wallet (custody ≠ vault-follow)
- @concepts/cemini-pm-lp-vs-copy-capital-decision.md — capital ADR
- @concepts/perp-dex-price-discovery-lead-lag.md — Binance leads HL ~700ms → DIY copy late
- @sources/gemini-dr-pm-hl-strategies-2026-07-14.md — primary vault economics source
- @sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md — HLP fee/lockup table
- @sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md — HLP-preferring sibling (conflict)
- @entities/tools/hyperliquid-python-sdk.md — official vault transfer APIs

## Raw Concept

K165 Gemini DR wave: first dedicated OSINT page for **trader vault-follow** economics (distinct from AES-GCM key vault narrative on the platform page).

## Narrative

### Three modes

| Mode | What it is | Doc-stated economics |
|------|------------|----------------------|
| **HLP (protocol)** | Deposit into protocol vault; share MM/liquidation PnL | ~15–30% APR cited (windows); **short vol**; **4-day** withdraw lockup; 0% perf/mgmt fees `[TENTATIVE]` |
| **User vaults** | Deposit to leader vault | **10%** perf fee HWM; leader **5%** skin; default **1-day** lockup |
| **DIY fill-mirror** | Watch leader fills → follower orders | Taker fees + lag; **$10 min notional** breaks small % sizing |

### Verdicts across DRs (do not flatten)

- All three: **skip live DIY** fill-mirroring.
- Conflict: HLP vs User Vaults as preferred passive — `[NEEDS VERIFICATION 2026-07-14]` until operator ADR.

### DIY failure modes (CONFIRMED as structural risks; EV unproven)

1. Lead-lag vs Binance (wiki Arrakis study + DR synthesis)
2. Min notional rejects → position drift vs leader
3. Funding / margin asymmetry → follower liquidates while leader survives

### Cemini stack note

Official `hyperliquid-python-sdk` already covers `vault_usd_transfer`, agent approve, vault equity queries — prefer product path over vendoring unlicensed copy bots.

## Snippets

> Agent Wallet on `@entities/platforms/hyperliquid.md` is **signing custody**. HLP/User Vaults are **capital allocation products**. Do not conflate.
