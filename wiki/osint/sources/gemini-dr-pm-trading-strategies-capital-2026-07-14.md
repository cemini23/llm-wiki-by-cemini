---
title: "Gemini DR — Polymarket trading strategies / capital matrix (2026-07-14)"
type: source
tags: [source, gemini-deep-research, polymarket, lp-rewards, hyperliquid, capital-allocation, k165]
keywords: [capital-tiers, july-13-cuts, oddpool, world-cup-bot, openclaw-npm]
related:
  - sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md
  - sources/gemini-dr-pm-hl-strategies-2026-07-14.md
  - concepts/cemini-pm-lp-vs-copy-capital-decision.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/hyperliquid-hlp-vs-user-vaults.md
  - entities/tools/oddpool.md
  - entities/tools/world-cup-bot.md
  - entities/tools/hyperliquid-python-sdk.md
  - concepts/openclaw-security-taxonomy.md
  - entities/tools/openclaw.md
maturity: validated
read_status: deep-read
created: 2026-07-14
updated: 2026-07-14
clusters: [polymarket]
---

## Relations

- @concepts/cemini-pm-lp-vs-copy-capital-decision.md — synthesis
- @concepts/hyperliquid-hlp-vs-user-vaults.md — HLP lean in this report (conflicts with sibling)
- @entities/tools/oddpool.md — INTEGRATE-CANDIDATE analytics for low-competition LP filter
- @entities/tools/openclaw.md — AVOID live trading skills
- @concepts/openclaw-security-taxonomy.md — supply-chain frame

## Raw Concept

- **Title**: Quantitative Analysis of Capital Allocation Strategies: Polymarket Liquidity Provision vs. Decentralized Copy-Trading Infrastructure
- **Type**: Gemini Deep Research docx (filename overclaims “Trading Strategies”)
- **Location**: `cemini-egress-fi:/opt/cemini-bulk/research/osint/Polymarket Trading Strategies Research.docx`
- **Retrieved**: 2026-07-14
- **sha256**: `c2bbedb3b1c9d7b5...` · **size**: 57,633 bytes · **Preingest**: NEW

## Narrative

Same A/B/C/D capital frame as sibling LP-vs-copy DR, with stronger emphasis on **July 13, 2026 incentive cuts** and post–**July 19** WC window compression.

**Ranked posture (this report):** skip B (copy); $500→D; $2k→D or tiny HLP canary; $10k→HLP (C) **or** selective A with Oddpool low-competition filter; skip DIY HL + discretionary user vaults.

**INTEGRATE:** py-clob-client (legacy note — prefer v2), hyperliquid-python-sdk, cemini23/world-cup-bot, Oddpool, official LP docs.  
**STEAL-FROM:** realfishsam / CoinMLabs copy bots, Brobicho/HLCopy, python-order-utils.  
**AVOID:** OpenClaw skills, neosun100/polycopy, ethuncledealer copy-trader, polycopy.app SaaS.

Security wave: Unit 42 OpenClaw supply chain, npm postinstall key steal IoCs, CVE-2026-25253 cited.

## Snippets

> Small-capital PM LP ($500/$2k) framed as failing $1/day floor + midpoint-pin math in post–July 2026 regime — conflicts with earlier MatiasScalbi $50 anecdotes; tag `[OPEN QUESTION 2026-07-14]`.
