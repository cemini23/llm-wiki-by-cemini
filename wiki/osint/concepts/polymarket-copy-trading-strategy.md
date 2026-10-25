---
title: "Polymarket copy-trading strategy — wallet selection, latency arms race, hedge-leg trap"
type: concept
tags: [concept, polymarket, copy-trading, smart-money, wallet-tracking, prediction-markets, telegram-bots, k56]
keywords: [pretracer, kreopolybot, polygun, polycule, polymarketanalytics, smart-wallet-selection, hft-copy-trap, hedge-leg-trap, 3-month-track-record-rule, percentage-stop-loss, dexterssolab-32700, igor-mikerin-10000]
related:
  - sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md
  - entities/people/spottr-trade.md
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/prediction-market-information-leakage-score.md
  - sources/arxiv-foresightflow-ils-polymarket-2605.00493.md
  - sources/arxiv-polymarket-ils-population-scale-2605.00459.md
  - concepts/non-latency-arbitrage-strategies.md
  - entities/tools/pretracer.md
  - entities/tools/kreopolybot.md
  - entities/tools/polymarketanalytics-com.md
  - entities/people/igor-mikerin.md
  - entities/people/dexterssolab.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/polymarket-retail-trading-discipline.md
  - entities/infrastructure/cemini-egress-fi.md
  - concepts/cemini-ai-assistant.md
  - concepts/interaction-native-knowledge-harness.md
  - sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md
  - sources/trading-posts-compilation-38-2026-05-26.md
  - sources/trading-posts-compilation-25-2026-05-27.md
  - concepts/polymarket-wallet-alpha-pipeline.md
  - concepts/polymarket-updown-15min-execution-latency.md
  - entities/tools/warproxxx-poly-data.md
  - entities/tools/crisp-predict.md
  - sources/alterego-eth-five-weather-methodologies-2026-05-27.md
  - concepts/polymarket-weather-bot-methodology-taxonomy.md
  - concepts/polymarket-weather-trading-strategy.md
  - sources/youtube-polymarket-bots-batch-2026-05-29.md
  - sources/youtube-kalshi-bots-batch-2026-05-29.md
  - entities/tools/bullpen-cli.md
  - entities/tools/odds-jam-prediction-insiders.md
  - sources/youtube-kalshi-bots-batch-2026-05-29.md
  - entities/tools/momentum-odds.md
  - sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md
  - concepts/cemini-pm-lp-vs-copy-capital-decision.md
  - sources/gemini-dr-pm-hl-strategies-2026-07-14.md
maturity: validated
created: 2026-05-21
updated: 2026-10-25
clusters: [polymarket, copy-trading]
---

## Relations

- @sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md — Post 7 (@spottr_trade) hybrid CLOB latency
- @entities/people/spottr-trade.md — Spottr author
- @sources/posts-prediction-markets-quant-frameworks-2026-05-21.md — Posts 2 (@igor_mikerin) + 3 (@DextersSolab) primary sources
- @sources/trading-posts-compilation-38-2026-05-26.md
- @sources/trading-posts-compilation-25-2026-05-27.md — K72 Post 24 (daily wallet hygiene emphasis) — Post 31 (CAR wallet anecdote); Post 0 (CrispPredict / 15m latency)
- @concepts/polymarket-bot-architecture.md — taker-side bot architecture; copy-trading is one specific taker-side execution pattern
- @concepts/polymarket-market-making-architectures.md — already references smart-money-copy as a multi-source-confirmed K30 pattern
- @concepts/polymarket-microstructure-findings.md — final-hour HFT dynamics motivate the "skip wallets with sub-20ms execution" rule
- @concepts/non-latency-arbitrage-strategies.md — copy-trading is at the boundary of latency-sensitive (need fast bot for fills) but not latency-arbitrage (you're paying spread to a faster wallet)
- @entities/tools/pretracer.md — Telegram bot promoted by @igor_mikerin
- @entities/tools/kreopolybot.md — Telegram bot promoted by @DextersSolab
- @entities/tools/polymarketanalytics-com.md — free filter platform used for wallet discovery
- @concepts/polymarket-retail-trading-discipline.md — retail sizing + resolution hygiene (K57)
- @entities/infrastructure/cemini-egress-fi.md — K57 egress-fi adoption: gateway must not over-promise copy latency (hybrid CLOB / 0-block semantics)
- @concepts/cemini-ai-assistant.md — assistant disclosure rule for copy-trading answers (K57)
- @sources/alterego-eth-five-weather-methodologies-2026-05-27.md — K70 type 4 (weather copy-trading / smart-money)
- @concepts/polymarket-weather-bot-methodology-taxonomy.md — K70 five-type framework
- @concepts/polymarket-weather-trading-strategy.md — weather-specific copy context
- @sources/youtube-polymarket-bots-batch-2026-05-29.md — K80 Odds Jam 30d experiment + Bullpen CLI build
- @entities/tools/bullpen-cli.md — Claude Code copy-bot stack (Sharbel tutorial)
- @entities/tools/odds-jam-prediction-insiders.md — alert-feed copy product + measured ROI
- @concepts/cemini-pm-lp-vs-copy-capital-decision.md — K165: blind copy remains NO-GO; Daleep whale-edge inverse
- @sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md — OpenClaw/Telegram AVOID + capital tiers

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

`[TENTATIVE 2026-05-29]` Pretracer's zero-fees and ~100ms latency — single-source referral marketing; Exa/web search found no Pretracer fee/latency docs (May 2026). Named competitor PolyCop publishes 0.5%/trade and ~2s execution [Source: https://polycop.trade/ (retrieved 2026-05-29)]. Cemini relevance: copy-trading is adversary modeling, not adoption — but latency bar for any taker strategy remains ~1–2s on Polygon unless we colocate.

### Bots compared (per source claims)

| Bot | Author preference | Claimed latency | Fees | Source |
|---|---|---|---|---|
| Pretracer | @igor_mikerin | ~100ms | None | Posts.docx Post 2 |
| KreoPolyBot | @DextersSolab | "fastest available" | Charges | Posts.docx Post 3 |
| Polygun | rejected | "too slow" per igor_mikerin | Charges | Posts.docx Post 2 |
| Polycule | rejected | "too slow" per igor_mikerin | Charges | Posts.docx Post 2 |
| Kreo (alternate name?) | rejected by igor / endorsed by Dexter as KreoPolyBot | conflicting | conflicting | Posts.docx Posts 2+3 |

The Kreo / KreoPolyBot naming conflict is **resolved** `[CONFIRMED 2026-05-29]` — same bot family (`@KreoPolyBot`, Kreo docs). Speed/fee superiority between Pretracer vs Kreo remains **unbenchmarked** — both sides are referral posts.

### Self-reported PnL claims

- **@igor_mikerin**: $10,000 net profit in February 2026 following 5 named wallets (RN1, wooter, 212121212121212121212, livebreathevolatility, BulkeyBull)
- **@DextersSolab**: $32,700 in one month (start-of-2026 timeframe), 6 figures cumulative

`[TENTATIVE]` — both posts are referral-marketing content with clear incentives to inflate. Treat the workflows as instructive, the PnL numbers as marketing claims.

### Hybrid CLOB latency model (K57, @spottr_trade) [CONFIRMED architecture]

Polymarket matches orders **off-chain** first; settlement batches to Polygon later. Three moments:

1. **Backend match** (leader trade happens — not publicly streamed)
2. **Mempool broadcast** (earliest practical follower detection without privileged access)
3. **Block confirmation** (public, slowest)

**"0-block execution"** (follower settlement in same Polygon block as leader) measures step 3, not step 1. Polygon block time ~1.75s; mempool visibility often &lt;1s after match. Copy-bot marketing that leads with block metrics understates the irreducible detection floor.

**Fastest public detection path cited:** self-hosted Polygon node + mempool subscription (third-party RPC adds relay hops). **Execution cited:** colocation near Polymarket infra + EIP-712 signing (~50–300ms backend round-trip) [TENTATIVE vendor claims].

Design implication for Cemini: any copy-trading or smart-wallet-mirror strategy must budget latency in **detection + CLOB order submission**, not block parity alone. See `@entities/people/spottr-trade.md`.

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

### K67 anecdote — CAR wallet / Lebanon market [TENTATIVE]

@undefinedKi (Post 31): **garbagefriends** wallet allegedly copied **CAR** into Israel–Lebanon March 20 market at **1¢** → $50→$3,456 in 72h. Illustrates **latency + wallet selection** story; not independently verified. Promotional copy-trading guide structure.

### K80 YouTube — Odds Jam + Bullpen CLI [TENTATIVE]

**Prediction Insiders (Odds Jam)** — @entities/tools/odds-jam-prediction-insiders.md: Financial Wolf $1K / 30-day trial. **54% win rate**, drawdown to ~$740 mid-challenge; final **~$224 PM profit** on ~$7.5K wagered vs ~$187 fee-drag baseline. Marketing stats (~481% product return) **not reproduced**. Lesson: alert-feed copy can beat random+fees slightly but underperforms hype; combine with confidence filters (>80 score in video).

**Bullpen CLI + Claude Code** — @entities/tools/bullpen-cli.md: Sharbel tutorial builds TypeScript copy bot — top 10 **active weekly PnL** wallets, $5 fixed mirror, polling/watch loop, local dashboard. Steal-from for **rapid prototype** path vs Cemini `py-clob-client` stack **`[TENTATIVE 2026-05-29]`** — official CLI docs confirmed; binary distribution only.

### K80 YouTube — Beast Sports whale tracker [TENTATIVE]

Beast Sports Picks (`iF6ZWEbkxzM`) promotes a **closed-source tracker** sorting Polymarket wallets by win rate, ROI, active bets, and displayed wallet size — surfacing top-50 "sharps" with live positions (e.g. $80k Manchester United YES). Marketing claims (93% hit rate, $17M PnL) are **unverified** and likely survivorship-biased. Same category as @entities/tools/polymarketanalytics-com.md / @entities/tools/parity-polymarket-analytics.md wallet discovery — apply existing copy-trading hygiene (3-month rule, hedge-leg trap, latency filter).

## Snippets

> "By the time your copy bot fire, the trade is already done and the price has moved. You are not copying their entry. You are buying their exit at full price."
> — @DextersSolab on copying HFT wallets [Source: Posts.docx Post 3]

> "Never copy a wallet with under 3 months of consistent history."
> — @DextersSolab [Source: Posts.docx Post 3]

> "What looked like a confident $200k bet was actually insurance for something you cannot see. You took on pure directional risk they never had."
> — @DextersSolab on the hedge-leg trap [Source: Posts.docx Post 3]

> "Trader A wins 80% of trades but risks $1 to make $0.20. Trader B wins 60% of trades but risks $0.40 to make $0.80. Trader B might be much stronger long term."
> — @DextersSolab [Source: Posts.docx Post 3]

### K165 refresh (2026-07-14)

Three Gemini DRs + gambling-wiki prior reaffirm: **blind PM/HL DIY copy = structural negative EV**. Daleep/Deleep-class results: large wallets can have **worse** edge than small traders. OpenClaw Polymarket skills + private-key Telegram bots = **hostile**. Wallets remain **adversary / filter signal**, not capital allocation. See `@concepts/cemini-pm-lp-vs-copy-capital-decision.md`.
