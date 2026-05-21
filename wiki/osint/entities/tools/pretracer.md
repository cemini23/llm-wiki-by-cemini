---
title: "Pretracer — Telegram-based Polymarket wallet tracker + copy-trading bot"
type: entity
tags: [entity, tool, polymarket, telegram-bot, copy-trading, wallet-tracker, prediction-markets, k56]
keywords: [pretracer, telegram-bot, polymarket-wallet-tracker, polymarket-copy-trading, usdc-funding, 100ms-latency, igor-mikerin, polygun-competitor, polycule-competitor, kreopolybot-competitor]
related:
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/polymarket-copy-trading-strategy.md
  - entities/people/igor-mikerin.md
  - entities/tools/kreopolybot.md
  - entities/tools/polymarketanalytics-com.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
phase_0_verdict: NO-AUDIT — third-party Telegram bot; not a candidate for Cemini adoption (we don't outsource execution to external opaque bots)
---

## Relations

- @sources/posts-prediction-markets-quant-frameworks-2026-05-21.md — Post 2 (@igor_mikerin) primary source
- @concepts/polymarket-copy-trading-strategy.md — workflow concept
- @entities/people/igor-mikerin.md — promoter / referrer
- @entities/tools/kreopolybot.md — competing Telegram bot

## Raw Concept

What prompted this page: K56 Posts.docx Post 2 — @igor_mikerin's referral-marketing post for Pretracer.

## Narrative

**Pretracer** (`@pretracer` on Telegram, also a Telegram link target referenced as `t.me/pretracer`) is a Telegram-based bot offering three Polymarket-related services:

1. **Real-time wallet tracker** — push notifications when watched wallets open / close positions. Custom filter criteria including win rate, total profit, etc.
2. **Wallet parser (passive observer)** — monitor a wallet's trades without copying, for study before commitment.
3. **Copy-trading executor** — auto-mirror trades from a watched wallet to your funded balance.

### Operational claims (per @igor_mikerin)

| Claim | Status |
|---|---|
| ~100ms latency from source-wallet trade to copy execution | `[NEEDS VERIFICATION 2026-05-21]` |
| Zero fees | `[NEEDS VERIFICATION 2026-05-21]` |
| USDC-funding only (no MetaMask, no browser dashboard, no app install) | `[CONFIRMED]` — typical Telegram-bot pattern |
| Setup in under 5 minutes | `[TENTATIVE]` |

### Onboarding flow (per source)

1. Open Telegram, find `@pretracer` or follow link
2. `/start` and make a first USDC deposit
3. Tap "Copy Trading" → "Add Task" → enter wallet **address** (not username)
4. Choose sizing mode (Fixed / Exact / Percentage / Portfolio)
5. Confirm and start

### Position in the market

Per @igor_mikerin, Pretracer competes against **PolyGun**, **Polycule**, and **Kreo** (also referenced as **KreoPolyBot** by @DextersSolab — see naming conflict in @concepts/polymarket-copy-trading-strategy.md). Author claims Pretracer wins on latency and fee structure; @DextersSolab claims KreoPolyBot wins on latency. Without independent benchmarks, both claims are referral-marketing.

### Cemini relevance

**Not a Cemini adoption candidate.** Cemini's Polymarket strategy is LP-rewards-farming (maker-side) and (eventually) directional bots executed through pmxt + cemini-egress-fi (Helsinki egress relay). We control our own execution stack — outsourcing to a third-party Telegram bot would:

1. Surrender execution latency observability
2. Custody funds inside a Telegram-bot wallet of unknown auditability
3. Tie Cemini's trading to external operator goodwill

Pretracer is documented here because:
- It defines the **competitive surface** for any future Cemini copy-trading-style feature
- Its existence (with ~100ms claim) sets the latency benchmark Cemini must match if entering this niche
- It's the apparent funnel that drove much of the K30/K55-era "smart-money-copy" pattern adoption among retail Polymarket traders

### Verification follow-ups

- Resolve the Kreo / KreoPolyBot naming question via direct check of `t.me/KreoPolyBot` and `t.me/pretracer`
- Confirm whether Pretracer is custodial (holds user USDC) or non-custodial (signs from user wallet). The "USDC deposit" flow implies custodial — `[TENTATIVE 2026-05-21]`
- Spot-check the 100ms latency claim against any third-party benchmark

## Dead Ends

- The source post is referral-marketing. Treat all self-reported metrics as marketing claims, not specs. The technical viability of "~100ms wallet-to-execution" depends entirely on Pretracer's infrastructure topology (collocated with Polymarket's matching engine? RPC-polling?) which is not disclosed.
