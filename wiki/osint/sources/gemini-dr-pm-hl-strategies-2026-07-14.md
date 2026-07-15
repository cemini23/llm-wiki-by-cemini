---
title: "Gemini DR — Polymarket + Hyperliquid strategies (2026-07-14)"
type: source
tags: [source, gemini-deep-research, polymarket, hyperliquid, vaults, copy-trading, k165]
keywords: [hlp, user-vaults, diy-copy, ghostguard, maxisontosomething, funding-asymmetry]
related:
  - sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md
  - sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md
  - concepts/cemini-pm-lp-vs-copy-capital-decision.md
  - concepts/hyperliquid-hlp-vs-user-vaults.md
  - entities/platforms/hyperliquid.md
  - entities/tools/hyperliquid-python-sdk.md
  - concepts/polymarket-copy-trading-strategy.md
maturity: validated
read_status: deep-read
created: 2026-07-14
updated: 2026-07-14
clusters: [hyperliquid, polymarket]
---

## Relations

- @concepts/hyperliquid-hlp-vs-user-vaults.md — HLP vs user-vault economics + conflict with sibling DR
- @entities/platforms/hyperliquid.md — platform update target
- @concepts/polymarket-copy-trading-strategy.md — DIY/HL copy adversary framing

## Raw Concept

- **Title**: Capital Allocation and Execution Vector Analysis for Decentralized Prediction Markets and Perpetual Exchanges
- **Type**: Gemini Deep Research docx
- **Location**: `cemini-egress-fi:/opt/cemini-bulk/research/osint/Polymarket and Hyperliquid Strategies.docx`
- **Retrieved**: 2026-07-14
- **sha256**: `7e69a7ce92c79714...` · **size**: 3,004,022 bytes · **Preingest**: NEW

## Narrative

Broadest PM+HL matrix in the three-report wave. Strongest **DIY HL copy kill** detail: Binance lead-lag, **$10 min notional** (small follower rejects), funding/liquidation asymmetry.

**This report’s HL leaning:** skip DIY; HLP is short-vol with 5–12% DD windows + 4-day lockup; if HL at $10k prefer **vetted market-neutral funding User Vault** (10% perf fee, 5% leader skin) **or D (Kalshi proprietary)** — **conflicts** with sibling report that prefers HLP and skips user vaults.

**PM overlap:** Jul 13 pool cuts; V2 **~3.5-minute delayed self-pause**; GhostGuard as CLOB↔on-chain fill verify; skip PM LP at small capital in this framing.

**INTEGRATE-CANDIDATE:** GhostGuard, py-clob-client-v2, warproxxx/poly-maker (license TBD), MaxIsOntoSomething Hyperliquid_Copy_Trader (sim-first), Lindagrey copy-trader (patterns), official HL SDK.  
**STEAL-FROM:** poly-market-maker (V1 only), Brobicho/HLCopy.  
**AVOID:** OpenClaw Polymarket skills.

## Snippets

> DIY HL: profitable wallets often HFT vs Binance; Python WS copy enters after window; $500 follower cannot size 1% of $1M whale without hitting $10 min notional rejects.
