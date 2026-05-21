---
title: "Polymarket copy-trading strategy — wallet selection, latency arms race, hedge-leg trap"
type: concept
tags: [concept, polymarket, copy-trading, smart-money, wallet-tracking, prediction-markets, telegram-bots, k56]
keywords: [pretracer, kreopolybot, polygun, polycule, polymarketanalytics, smart-wallet-selection, hft-copy-trap, hedge-leg-trap, 3-month-track-record-rule, percentage-stop-loss, dexterssolab-32700, igor-mikerin-10000]
related:
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/non-latency-arbitrage-strategies.md
  - entities/tools/pretracer.md
  - entities/tools/kreopolybot.md
  - entities/tools/polymarketanalytics-com.md
  - entities/people/igor-mikerin.md
  - entities/people/dexterssolab.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
clusters: [polymarket, copy-trading]
---

## Relations

- @sources/posts-prediction-markets-quant-frameworks-2026-05-21.md — Posts 2 (@igor_mikerin) + 3 (@DextersSolab) primary sources
- @concepts/polymarket-bot-architecture.md — taker-side bot architecture; copy-trading is one specific taker-side execution pattern
- @concepts/polymarket-market-making-architectures.md — already references smart-money-copy as a multi-source-confirmed K30 pattern
- @concepts/polymarket-microstructure-findings.md — final-hour HFT dynamics motivate the "skip wallets with sub-20ms execution" rule
- @concepts/non-latency-arbitrage-strategies.md — copy-trading is at the boundary of latency-sensitive (need fast bot for fills) but not latency-arbitrage (you're paying spread to a faster wallet)
- @entities/tools/pretracer.md — Telegram bot promoted by @igor_mikerin
- @entities/tools/kreopolybot.md — Telegram bot promoted by @DextersSolab
- @entities/tools/polymarketanalytics-com.md — free filter platform used for wallet discovery

## Raw Concept

What prompted this page: K56 Posts.docx — two independent posts (@igor_mikerin and @DextersSolab) both documenting Polymarket copy-trading workflows with self-reported 5-figure monthly profits. Both posts are partially referral-marketing (promote competing Telegram bots) but together they triangulate the canonical workflow and its failure modes. Pre-existing reference: `concepts/polymarket-market-making-architectures.md` flags smart-money-copy as "the single most-confirmed strategy-pattern in the K30 wave" from multi-source repo audits.

## Narrative

Copy-trading on Polymarket is the **passive-mirror execution pattern** where your account auto-replicates trades from a watched smart-money wallet. It superficially looks like passive income; in practice it requires daily curation of watched wallets, careful selection criteria, and a fast bot — or you lose money.

The Cemini strategic value of this pattern is **not direct adoption** (we're not building a Telegram copy bot). It's:

1. **Adversary modeling**: any LP-farming or directional bot on Polymarket competes against copy-traders who fire seconds after smart wallets — they consume the alpha first.
2. **Smart-wallet feed as alternative-data**: the *selection criteria* documented here — filter for consistency, specialization, controlled sizing — can be lifted into a wallet-quality scoring signal for our own market models. A wallet that ranks high under these filters is informative about which markets have professional flow.
3. **Pretracer / KreoPolyBot latency benchmarks**: ~100ms claimed wallet-to-execution latency sets the bar for any latency-sensitive Cemini Polymarket strategy. We must either match or avoid latency-sensitive niches entirely.

### Four catastrophic mistakes (@DextersSolab)

| Mistake | Why it loses | Heuristic |
|---|---|---|
| Copying HFT / bot wallets | They have co-located infra, sub-20ms execution. Your copy fires *after* the price has moved. You buy their exit at full price. | Skip wallets with hundreds of trades/day at tiny margins. |
| Copying short track records | 10 wins in a row in small N = random chance. | **Minimum 3 months** of consistent history. |
| Copying viral wallets | When a wallet trends, copy-bots flood in. Liquidity disappears, entry prices worsen, returns compress. | Best wallets are unknown. Edge dies in attention. |
| Copying without understanding strategy | Smart traders hedge across wallets / off-platform. You copy one visible leg of a hedged position. What looked like a confident $200k bet was actually insurance. You took directional risk they never had. | **Hedge-leg trap.** Understand the *why*, not just the *what*. |

### Wallet-selection criteria (@DextersSolab via polymarketanalytics.com)

The free filter platform exposes wallet metadata Polymarket itself doesn't surface. Recommended filter parameters:

- **Overall PnL**: $15,000 - $400,000 (whales above $400k make money on absolute size — copy with small capital captures little of that)
- **Current value**: ≥ $5,000 (active wallet, not abandoned)
- **Active positions**: ≥ 2 (diversified)
- **Total positions**: ≥ 20 (sample size)
- **Win rate**: ≥ 70%
- **Consistency**: 2-3 months of steady results, not one spike
- **Trade frequency**: 30-200 trades/month (not 10 = lucky; not 1,000 = bot)
- **Specialization**: 1-3 niches (politics, weather, sports, crypto, macro) — specialists outperform generalists
- **Drawdown control**: cuts losses quickly, no emotional doubling-down, overall curve positive

Critical caveat from DextersSolab: **win rate alone is misleading**. A wallet with 80% win rate risking $1 to make $0.20 has lower expected value than a wallet with 60% win rate risking $0.40 to make $0.80. Use win-rate as a filter, not a ranking.

### Bot setup (KreoPolyBot — DextersSolab's recommendation)

Four sizing options:

| Mode | Behavior |
|---|---|
| **Fixed** | Every copy trade = $X regardless of source size |
| **Exact** | Match source trader's $-amount |
| **Percentage** | Your trade = X% of source trader's trade size |
| **Portfolio** | If trader uses 10% of his balance, you use 10% of your balance |

Recommended config (DextersSolab):
- **Fixed** or **Portfolio** sizing
- **5% slippage** tolerance
- **70% percentage stop-loss** (this is *unique to KreoPolyBot* per the author — most competitors lack it)
- Trade type: **Buys + Sells** (mirror exits, not just entries)

### Pretracer alternative (igor_mikerin's recommendation)

Pretracer (`@pretracer` on Telegram) is the @igor_mikerin-promoted competitor. Self-reported metrics: ~100ms latency, **zero fees** (vs Kreo/Polygun/Polycule charging fees), runs entirely in Telegram, USDC funding only. Three modes:

- **Real-time wallet tracker** — notifications on a watched wallet's new positions
- **Wallet parser** — passive observer mode for studying a wallet before committing to copy

`[NEEDS VERIFICATION 2026-05-21]` Pretracer's zero-fees claim and ~100ms latency — typical referral-marketing inflates both. The independent question is whether Polymarket itself charges enough order/withdrawal fees that bot-level fees are noise. (Polymarket gas: ~$0.10-0.50 per trade on Polygon. If Pretracer takes nothing, that's a real cost saver vs Kreo.)

### Bots compared (per source claims)

| Bot | Author preference | Claimed latency | Fees | Source |
|---|---|---|---|---|
| Pretracer | @igor_mikerin | ~100ms | None | Posts.docx Post 2 |
| KreoPolyBot | @DextersSolab | "fastest available" | Charges | Posts.docx Post 3 |
| Polygun | rejected | "too slow" per igor_mikerin | Charges | Posts.docx Post 2 |
| Polycule | rejected | "too slow" per igor_mikerin | Charges | Posts.docx Post 2 |
| Kreo (alternate name?) | rejected by igor / endorsed by Dexter as KreoPolyBot | conflicting | conflicting | Posts.docx Posts 2+3 |

The Kreo / KreoPolyBot naming conflict between the two sources is unresolved — they may be the same bot with the two authors disagreeing on its speed, or two related products. `[NEEDS VERIFICATION 2026-05-21]`

### Self-reported PnL claims

- **@igor_mikerin**: $10,000 net profit in February 2026 following 5 named wallets (RN1, wooter, 212121212121212121212, livebreathevolatility, BulkeyBull)
- **@DextersSolab**: $32,700 in one month (start-of-2026 timeframe), 6 figures cumulative

`[TENTATIVE]` — both posts are referral-marketing content with clear incentives to inflate. Treat the workflows as instructive, the PnL numbers as marketing claims.

### Adversary-modeling implications for Cemini

If we run a directional Polymarket strategy on a market with active copy-traders:
- **Smart wallet enters** → milliseconds later, copy-bots fire → spread widens, fills worsen
- We are either (a) the smart wallet (impossible without alpha) or (b) a copy-trader (paying spread to a faster wallet) or (c) one of the slowest copies (buying their exit at full price)

The LP-rewards-farming strategy (@concepts/polymarket-lp-rewards-farming.md) **sidesteps this entirely** — you're providing liquidity, not chasing it. This is one structural reason LP-farming is operationally simpler than directional Polymarket trading.

For any Cemini directional bot, **must** include in the design:
- Pre-trade check: is this market being copy-traded heavily (top wallets identified, recent activity inflated)? If yes, expect spread to widen ~5-15bps after any smart-wallet entry.
- Skip markets with >100 trades/hour from wallets in the polymarketanalytics top-N — they're saturated.

## Dead Ends

- The Kreo vs KreoPolyBot naming inconsistency may indicate the two authors are referring to different bots, or that one rebranded. Don't recommend either by name in Cemini briefs until verified.
- Both source posts include referral links (`?via=igor-mikerin`, `?start=ref-dexter`). The recommended wallets and recommended bots both have incentive bias. Cross-reference with `polymarketanalytics.com` independently before trusting any specific wallet recommendation.

## Snippets

> "By the time your copy bot fire, the trade is already done and the price has moved. You are not copying their entry. You are buying their exit at full price."
> — @DextersSolab on copying HFT wallets [Source: Posts.docx Post 3]

> "Never copy a wallet with under 3 months of consistent history."
> — @DextersSolab [Source: Posts.docx Post 3]

> "What looked like a confident $200k bet was actually insurance for something you cannot see. You took on pure directional risk they never had."
> — @DextersSolab on the hedge-leg trap [Source: Posts.docx Post 3]

> "Trader A wins 80% of trades but risks $1 to make $0.20. Trader B wins 60% of trades but risks $0.40 to make $0.80. Trader B might be much stronger long term."
> — @DextersSolab [Source: Posts.docx Post 3]
