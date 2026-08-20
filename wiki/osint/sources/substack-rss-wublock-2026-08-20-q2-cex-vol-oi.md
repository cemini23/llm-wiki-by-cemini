---
title: "Wu Blockchain — 2026 Q2 CEX Vol/PoR and OI/PoR (whose volume was inflated)"
type: source
tags: [substack, crypto, perps, k243]
keywords: [wublock, vol-por, oi-por, hyperliquid, mexc, gate, proof-of-reserves]
related:
  - entities/platforms/hyperliquid.md
  - concepts/crypto-derivatives-volume-2026.md
  - sources/newsletter-wublock-derivatives-volume-july-2026-2026-08-12.md
  - sources/substack-rss-wublock-2026-08-11-july-spot-volume.md
  - sources/newsletter-rss-latent-space-2026-08-19-memory-prices.md
maturity: draft
created: 2026-08-20
updated: 2026-08-20
read_status: read
---

## Relations

- @entities/platforms/hyperliquid.md — on-chain benchmark (fabricating tape is costly)
- @concepts/crypto-derivatives-volume-2026.md — Q2 quality overlay on July notional series
- @sources/newsletter-wublock-derivatives-volume-july-2026-2026-08-12.md — July $3.03T derivatives notional
- @sources/substack-rss-wublock-2026-08-11-july-spot-volume.md — July spot $429B companion
- @sources/newsletter-rss-latent-space-2026-08-19-memory-prices.md — RWA memory-stock perps overlay

## Raw Concept

| Field | Value |
|-------|--------|
| File | `substack-rss-wublock-2026-08-20-2026-q2-cex-trading-data-review-whose-oi-and-tra.md` |
| sha256 | `5c7c17609e69a06acf59ecec8b40474e512267dec0b16d734e83936c42f591eb` |
| URL | https://wublock.substack.com/p/2026-q2-cex-trading-data-review-whose |
| retrieved | 2026-08-20 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-wublock-2026-08-20-2026-q2-cex-trading-data-review-whose-oi-and-tra.md` |
| Author | @agintender via WuBlockchain |

## Narrative

WuBlockchain Q2 follow-up on CEX **Vol/PoR** and **OI/PoR** vs a Hyperliquid on-chain benchmark. Formulas: Vol/Reserve = 30-day volume ÷ 30 ÷ core PoR (BTC+ETH+USDT+USDC); OI/PoR = open interest ÷ core reserves. HL TVL $4.88B → $6.11B (+25%) with 30-day derivs $206.8B → $237.7B (+15%); benchmark Vol/Reserve **1.44x → 1.30x** (Q2 threshold 1.49x after 15% band; Q1 was 1.66x). Reserves shrank industry-wide (Binance −17%, OKX −21%, Bybit −29%) on BTC ~$63k plus outflows.

**Vol/PoR steal:** Binance 0.59x and OKX ~1.01x look clean; KuCoin's Q1 incentive-inflated spot collapsed (spot $65B → $32.4B). Gate (total 3.25x) and MEXC (derivs 3.73x; 4,699 user BTC vs $354.4B monthly derivs) deteriorated as **reserves fell while reported volume did not**. Suspicious volume above threshold $295B → $519B; even under the old 1.66x bar MEXC+Gate still ~$240B+$180B. Top-3 real share 75.6% → 79.3%.

**OI/PoR:** HL OI/TVL 1.16x ($7.09B/$6.11B, 4 Jul snapshot). MEXC OI $9.69B ≈ Bybit despite ~$3.2B vs $9.9B reserves (OI/PoR 3.06x). Gate 2.33x; KuCoin OI/PoR stuck 2.76x with high OI-to-volume (zombie or embellished OI).

**RWA interlude:** sampled RWA derivs ~$22.3B/day on active days; SanDisk ~$6.4B + SK hynix ~$4B (~half). HL RWA share 20.6% ≈ Binance 20.7%. Removing RWA from MEXC still leaves it ~2.3× the adjusted threshold.

Wiki-only. **No xsp scp** (no named options/flow rule). **No pm scp.** [TENTATIVE] single-author PoR/CoinGecko/CoinGlass construct; OI is a 4 Jul snapshot not a Q2 average; eight-exchange sample.

[Source: https://wublock.substack.com/p/2026-q2-cex-trading-data-review-whose (retrieved 2026-08-20)]
