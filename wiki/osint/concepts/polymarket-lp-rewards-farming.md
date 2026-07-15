---
title: "Polymarket LP-rewards farming — provide-liquidity-as-yield + $POLY-airdrop positioning"
type: concept
tags: [concept, polymarket, liquidity-provision, lp-rewards, market-making, prediction-markets, airdrop-farming, poly-token, time-weighted-open-interest, k55]
keywords: [lp-rewards, providing-liquidity-polymarket, time-weighted-open-interest, two-sided-limit-orders, maker-rebate, midpoint-scoring, $48-top-10pct, $5m-sports-incentive, poly-airdrop, polymarket-fdv-estimator, matiasscalbi, ice-investment, cftc-approval, kelly-fraction-lp]
related:
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - sources/posts-prediction-markets-quant-frameworks-2026-05-21.md
  - concepts/polymarket-bot-architecture.md
  - sources/trading-posts-compilation-k84-2026-05-30.md
  - sources/trading-posts-compilation-42-2026-05-31.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/non-latency-arbitrage-strategies.md
  - concepts/kelly-sizing-quarter.md
  - entities/people/matias-scalbi.md
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/ai-polymarket-agent.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/cl-amm-dynamic-fees-lvr.md
  - sources/arxiv-cl-amm-dynamic-fees-lvr-2606.23070-2026-06-24.md
  - concepts/polymarket-lp-weather-market-discovery.md
  - concepts/polymarket-lp-weather-guard.md
  - concepts/lp-algorithm-live-promotion-gates.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/zero-trade-edge-signal-diagnostics.md
  - sources/quant-bot-lp-live-promotion-criteria-2026-05-28.md
  - concepts/cemini-backtest-report-kit.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
  - concepts/polymarket-preopen-queue-priority.md
  - sources/trading-posts-compilation-7-2026-06-09.md
  - sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md
  - sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md
  - concepts/cemini-pm-lp-vs-copy-capital-decision.md
  - entities/tools/oddpool.md
  - entities/tools/oracle3.md
maturity: validated
created: 2026-05-20
updated: 2026-07-14
clusters: [polymarket, market-making, yield-farming]
---

## Relations

- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — Post 2 (@MatiasScalbi Spanish-language guide) is the primary source
- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — Post 4 (@MatiasScalbi 21 tactical tips) is the tactical layer
- @sources/posts-prediction-markets-quant-frameworks-2026-05-21.md — K56 Post 1 (anonymous trader live $50 LP-farming test on Drake "Iceman" + Neymar FIFA-2026 setup) confirms $300-600 boosted-reward range and Top-15% LP rank at $50 capital in 48h
- @concepts/polymarket-bot-architecture.md — bot-side of the same edge; LP-farming is the maker-orientation complement
- @concepts/polymarket-market-making-architectures.md — overlapping market-making concept; this page focuses on the *rewards-scheme* incentive, that page on the structural MM patterns
- @concepts/polymarket-updown-bot-taxonomy.md — Type-1 bots (resting LP orders) are the closest existing taxon
- @concepts/non-latency-arbitrage-strategies.md — LP-rewards farming is structurally a *slow-yield* strategy alongside calendar/Dutch-book arb
- @concepts/kelly-sizing-quarter.md — sizing reference for capital deployment across markets
- @entities/people/matias-scalbi.md — primary-source author
- @entities/platforms/polymarket.md — venue entity
- @entities/tools/polymarket-clob-api.md, @entities/tools/polymarket-gamma-api.md — API surfaces required
- @concepts/polymarket-lp-bot-phase0-spec.md — Phase-0 implementation spec (K56 follow-up, design-only)
- @concepts/polymarket-lp-weather-market-discovery.md — Cemini weather LP discover pass + retail validation (Seoul/Warsaw May 2026)
- @concepts/polymarket-lp-weather-guard.md — pre-resolution exit on accidental weather LP fills
- @concepts/world-cup-advance-market-bot-v1.md — K82 FIFA advance-market LP vertical (OSS + Cemini)
- @concepts/polymarket-sports-lp-operating-rules.md — sports cancel/fill rules (6–10h pre-kickoff)
- @sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md — WC LP economics deep-read
- @concepts/cemini-pm-lp-vs-copy-capital-decision.md — K165 capital ADR + empirical sleeve kill
- @sources/gemini-dr-pm-lp-vs-copy-trading-2026-07-14.md — Jul 2026 incentive / $1-day floor refresh
- @entities/tools/oddpool.md — low-competition LP filter candidate
- @entities/tools/oracle3.md — INTEGRATE-CANDIDATE stub (Phase-0 pending)

## Raw Concept

What prompted this page: User-flagged interest in @MatiasScalbi's "provide liquidity to Polymarket and earn rewards" idea (K55 ingest, Posts.docx Post 2 + Posts 2.docx Post 4). Operationalizes a **maker-side** yield strategy that's distinct from every directional / arbitrage strategy currently in the Cemini Polymarket stack, and is unusually time-sensitive due to a credible (but unconfirmed) $POLY airdrop catalyst.

## Narrative

### The core idea

Polymarket pays **LP Rewards** in USDC, daily, to traders who place limit orders that improve the orderbook near the midpoint. The reward pool is funded by Polymarket itself (currently boosted by **$5M+ in sports-liquidity incentives for April 2026** alone). Two implications:

1. **You can earn yield on Polymarket without betting.** Posting YES + NO limit orders near midpoint of an active reward-eligible market generates LP rewards independent of which side wins on resolution.
2. **Active LPs are positioned for a potential $POLY airdrop.** Polymarket has signaled a forthcoming token (team statements + market signals; **not formally announced**). Active LPs accruing rewards through pre-token-launch are the most-likely airdrop-eligible cohort based on the Uniswap / Arbitrum / Hyperliquid precedent of rewarding pre-token power users.

This is a **maker** strategy. Every previously-documented Cemini Polymarket workstream (@0x_Punisher playbook, @AlterEgo_eth weather bot, @adiix_official latency arb, @0xMovez Hermes weather bot, @Gustafssonkotte 5-min UpDown bot) is a **taker** strategy. The LP-farming approach has fundamentally different economics: instead of edge × win-rate − fees, it's `LP_reward_share × time_in_book − adverse_fill_loss`.

### Reward-mechanism specifics [CONFIRMED — multiple sources]

From @MatiasScalbi (two posts) + `docs.polymarket.com` cross-references:

- **Reward pool structure**: published per-market reward budget; LPs share the budget by **participation score**.
- **Scoring formula** (high-level — actual coefficients on docs.polymarket.com):
  - **Distance-from-midpoint**: orders closer to the midpoint earn higher score. The 3-4¢ window (or 2¢ for aggressive small accounts) is the workable range; closer is better but raises adverse-selection risk.
  - **Two-sided liquidity bonus**: one-sided LP score is **divided by 3**. Posting both YES and NO at competitive spreads gives 3× the score for the same nominal exposure.
  - **Time-Weighted Open Interest (TWOI)**: holding limit orders in the book over time accrues weight. **Posts.docx claims a 72h+ multiplier**; verify against current docs.
  - **Per-market participation share**: your score / (sum of all LPs' scores) on that market → fraction of the market's daily reward pool.
- **Minimum daily payout threshold**: $1/day; below that, the day's reward forfeits. Spread liquidity across enough markets to clear $1 daily, not just chase one.
- **Reward eligibility**: not all markets pay rewards. Live list on the Polymarket "Rewards" page.

### Documented thresholds (as of Apr/May 2026) [CONFIRMED]

- **Top 10% of historical LP-reward recipients**: ~$48 accumulated rewards.
- **Top 1%**: ~$1,576 accumulated rewards.
- **Total historical LP rewards distributed**: $15,856,173.
- **April 2026 sports-liquidity incentive**: $5M+ for sports markets alone. Per-match scale: Champions League up to $24K/match, Premier League $10K, Liga Argentina $550.

The thresholds are unusually low because the active LP cohort is small; small capital can capture meaningful participation share in less-competitive markets.

### Tactical rules — the operator layer (synthesized from 21 @MatiasScalbi tips)

| Category | Rule | Why |
|---|---|---|
| **Market selection** | Vol ≥ $40K (ideally $100K); avoid markets resolving <14 days | Thin books = no exit; near-resolution swings 20-30% on news |
| **Market selection** | Mid 40-60¢ markets are safest | Symmetric tail risk; 85¢ filled → 50¢ = -32¢/share; 50¢ → 40¢ = -7¢ |
| **Market selection** | Mix themes (politics + crypto + sports + foreign elections) | Avoid correlated drawdowns (e.g. all-Iran positions break together) |
| **Order placement** | Place YES + NO limits 3-4¢ from mid (or 2¢ aggressive) | Reward scales with proximity to mid; one-sided penalizes 3× |
| **Order placement** | Look for walls ≥ 10× market min-shares; place above or 1¢ inside | Walls anchor the orderbook; placing inside captures fills first |
| **Order placement** | Place LP orders at night (00 UTC start) | Front-loads the daily reward calculation; ensures $1/day floor is cleared |
| **Capital sizing** | Position cap: 35% small account / 15% bot per market | 30% adverse move with 7+ markets absorbs the hit |
| **Capital sizing** | With $200, choose 3-7 markets at market's min-share | On 20-share-min markets, 20 shares per side can capture 10% participation |
| **Capital sizing** | Aim ≥ 0.5% participation share | $500/day pool × 0.2% = $1/day, not worth the risk |
| **Risk** | Check positions every 4-6h minimum | No stop-loss on Polymarket; sleeping through a 10¢ move = locked LP at a loss |
| **Risk** | If filled, sell as LIMIT not market | Maker rebate + continued LP rewards while waiting; market sell = 10-30% slippage |
| **Risk** | Reserve $50-100 bot / $10-15 small as "tuition" | First-week errors are expected; don't blow the float |
| **Rotation** | Don't marry a market | If participation drops below 1%, pull capital and rotate |
| **Rotation** | Manual: watch live participation %; pull capital if < 0.3% | Cost not worth the LP-reward income at that share |
| **Rotation** | Cancel/reposition only when mid moves ≥ 2¢ | Each cancel resets your time-in-book sampling |
| **Bot-specific** | Avoid entertainment / AI-release / single-day-event markets | 50%+ moves in minutes |
| **Bot-specific** | "Edge is in the plumbing not the algorithm" | Fill detection, position reconciliation, orphan-order cancellation, dust cleanup = 80% of code |
| **Logging** | Log every fill (entry, exit, time-to-sell, P&L) | Pattern emergence after ~30 trades |
| **Diversification** | Diversify themes across the LP book | Reduces airdrop-criterion concentration risk too |
| **Discipline** | First week: most effort, least capital | Treat as paid training |
| **Discipline** | Patience > aggression | LP rewards accrue per-minute in book |

### The $POLY airdrop thesis [TENTATIVE — single-source, multiple converging signals]

The airdrop is **not formally announced**. Treat the LP rewards as the certain payoff; the airdrop is upside.

**Signals listed by @MatiasScalbi** [verifiable via X / podcasts]:
- Shayne Coplan (founder) tweet 2025-10-08: `$BTC $ETH $BNB $SOL $POLY 🤔` — explicit non-denial.
- Mustafa (Polymarket team) tweet 2026-02-11: "1m markets and $POLY next."
- Matthew Modabber (CMO) on Degenz Live podcast: confirmed token + airdrop coming, post US-relaunch.

**Material catalysts** [CONFIRMED]:
- **NYSE / ICE strategic investment, 2025-10-07**: $2B at $9B post-money. (Intercontinental Exchange = parent of NYSE.)
- **CFTC approval, November 2025**: Polymarket regulated as US exchange (after 2022 CFTC settlement that blocked US users).
- **Revenue scale**: #4 daily-revenue project in crypto — $1.95M/day, $7.55M/30d. Volume: $3.6B in 2024 US elections alone.

**Independent estimator math** (community-built airdrop checker, **unofficial**):
- One @MatiasScalbi account: 1,754 $POLY × 1.20× multiplier = 2,105 $POLY
- At $20B FDV: ~$35,080 USD [TENTATIVE — FDV is speculative]
- Author's own caveat: "Can it be more? Yes. Less? Also. Can it not happen? Of course."

### Architecture for a Cemini LP bot

Translating the tactics into a runtime architecture:

```
┌─────────────────────────────────────────────────┐
│  MARKET SCANNER (Gamma API + Rewards page)      │
│    filter: vol≥$40K, resolution≥14d,            │
│            reward-eligible, mid 40-60¢          │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  PARTICIPATION FORECASTER                        │
│   for each candidate market:                    │
│     est. share = my_size / (current_lps + my)   │
│     daily $: share × pool_daily                 │
│   skip if est. share < 0.5% OR daily < $1       │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  ORDER PLACEMENT (CLOB API)                      │
│   for each selected market:                     │
│     post BOTH YES + NO at mid ± Xc              │
│     X = 3-4¢ standard, 2¢ tight                 │
│     size = capital / market_count / 2 sides     │
│     respect 15% per-market cap                  │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  POSITION RECONCILER (WebSocket fills)          │
│   on fill: post LIMIT sell at fill+1¢ (or BE)   │
│   never market-sell                              │
│   detect orphans → cancel; dust cleanup          │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  ROTATION LOGIC                                  │
│   every cycle:                                   │
│     if participation < 1% on any market → pull   │
│     if mid moves ≥ 2¢ → reposition              │
│     else hold (preserve time-in-book sampling)  │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│  TWOI WATCHDOG + REWARD CLAIMER                  │
│   track time-in-book per order                  │
│   verify $1/day floor cleared                   │
│   daily reward claim via Polymarket UI/API      │
└──────────────────────────────────────────────────┘
```

**Capital sizing reference**: at $200 starting capital with 3-7 markets, expect ~$40 LP rewards over 10 days at Top 6-7% (matches @MatiasScalbi's challenge-account claim, [TENTATIVE]). Scale linearly to start.

### Risks

| Risk | Mitigation |
|---|---|
| **Adverse fill in thin market** | Vol ≥ $40K filter; never use one-sided LP; mid 40-60¢ markets only |
| **Near-resolution swing** | 14-day-to-resolution minimum |
| **Sleeping through 10¢ move** | Position monitor every 4-6h max; bot runs 24/7 with alerts |
| **VPN/IP geofence change** | Don't park full capital; have a withdrawal-ready balance |
| **Airdrop never happens / undersized / wrong cohort** | Don't price airdrop into capital decisions — rewards alone justify |
| **Phishing on "$POLY claim" pages** | No claim mechanism exists today; ignore any link claiming otherwise |
| **Polymarket changes reward formula** | Monitor `docs.polymarket.com` Rewards page for parameter changes |
| **Concentration in correlated themes** | Mix politics + sports + crypto + foreign + long-tail |

### What this does NOT replace

LP-rewards farming is **complementary** to, not a substitute for:
- @concepts/polymarket-weather-trading-strategy.md — directional weather edge
- @concepts/polymarket-bot-architecture.md — taker-side bot lessons
- @concepts/cross-venue-arbitrage-pattern.md — fast arbitrage
- @concepts/non-latency-arbitrage-strategies.md — slow arb (Dutch-book, calendar, cross-venue)

The LP bot is a **fourth distinct workstream** on the Polymarket stack — running it doesn't preclude any of the others, and capital can be allocated across all four orientations.

## K56 live-test confirmation (2026-05-21)

An anonymous trader documented a $50 LP-farming live test on Polymarket (K56 Posts.docx Post 1 — see @sources/posts-prediction-markets-quant-frameworks-2026-05-21.md). Three sub-tests with concrete numeric outcomes:

### Drake "Iceman" first-week-album-sales market

**Day 1** ($50 deposit, 5 positions across sales-range buckets):

| Bucket | Probability | Yes | No |
|---|---|---|---|
| 300k-350k | 7% | 7.3¢ | 92.8¢ |
| 350k-400k | 7% | 6.9¢ | 93.2¢ |
| 400k-450k | 12% | 12.6¢ | 88.3¢ |
| 450k-500k | 17% | 17.3¢ | 83.7¢ |
| 500k-550k | 24% | 25.0¢ | 76.8¢ |

Result: **$4 returned in 5 hours** (~8% intra-day yield, no directional bet). [Source: K56 Posts.docx Post 1]

**Day 2**: $18 cumulative LP rewards. Rank **#21,829 / 145,703 = Top 14.98%**. **$17 from Top 10% threshold.** [Source: K56 Posts.docx Post 1]

### Boosted-rewards parameter `[CONFIRMED]`

The K55 page noted boosted rewards on new markets at $300-600/market as a `[TENTATIVE]` claim from @MatiasScalbi. **K56 Post 1 independently confirms the same range** ($300-600/market on top of regular fees) from a different anonymous author. Promote to `[CONFIRMED 2026-05-21]` — two independent sources within 1 week reporting the same numeric range.

### Neymar FIFA-2026 "zero-risk" LP setup

The K56 source highlights the Neymar FIFA-2026 World Cup market as an unusually clean LP setup:

- Current price: **94¢** (crowd highly convinced Neymar plays)
- Yes spread: **1¢**
- Order book: asks 94-97¢ totalling **$830k+**, bids 90-93¢ totalling **$328k+**
- LP rewards: **$300/market**

The structural pitch: hundreds of thousands of dollars on both sides with 1¢ spread → constant fills → LP earns base $300 + per-fill on top. 94¢ price → crowd already convinced → low directional swing risk. **Closest the framework gets to a textbook "zero-risk" LP setup** — though the residual risks (Polymarket changes reward structure, market resolves NO via late injury/withdrawal, market gets less active as resolution nears) still apply.

### Capital-sizing data point

The K55 capital reference was `$200 → $40 in 10 days at Top 6-7%` ([TENTATIVE], @MatiasScalbi self-reported). K56 adds a smaller-capital data point: **$50 → $18 in 48 hours at Top 15%**.

Rewards-per-capital efficiency is **back-loaded at small sizes** because the leaderboard rewards `time-weighted-open-interest × participation-share`; small LPs farming light markets capture proportionally more of the reward pool than whales (who concentrate in deep markets where their fractional participation share is small). This validates the K55 "$50-$200 sweet-spot for retail entry" framing.

### Cemini empirical sleeve kill (K165, 2026-07-14) — do not conflate with retail anecdotes

| Claim | Status |
|-------|--------|
| Retail `$50 → $18 / 48h` (K56) | **Third-party anecdote** — not Cemini PnL |
| Cemini `pm_lp_rewards` attributed ~**+$0.94** / ~23 events | Operator/prod (~2026-06-11) |
| Sleeve **KILLED** 2026-06-13; `PM_LP_LIVE_POST=false`; posture “Defer; no capital spend” | Prod `pivot_posture.yaml` |
| Jul 13 2026 incentive cuts + Jul-19 WC window compression | Gemini DR wave `[TENTATIVE]` until docs re-baselined |

**Do not auto-restart LP** from wiki nostalgia. Capital ADR: `@concepts/cemini-pm-lp-vs-copy-capital-decision.md`.

### Weather LP retail validation (2026-05-26) `[CONFIRMED — screenshot]`

X thread @GnatykA promoted a “limit buy + 99¢ sell” lifehack on **weather markets** with **~5% per day** returns. Operator screenshot + prod brief corroborate **same-day city temperature bins** (Seoul 25°C+, Warsaw 26°C on May 26) with fills at **30¢ / 48¢** and a **$5.96 maker rebate** exceeding individual **~$4.80** sell legs. See @concepts/polymarket-lp-weather-market-discovery.md for Cemini discover gates and tuning backlog. The 99¢ meme is likely **not** the paying mechanism; **maker rebate + two-sided mid quotes** are.

## K107 LP window tactics — @0xbobaaa (2026-06-09)

Retail framing: platform fees ~**$1M/day**; maker rewards for **resting near midpoint**, ideally **unfilled**. K107 Post 14 checklist [TENTATIVE — single source]: target markets **21–24h** to resolution; quote **both sides within ~2% of mid**; if either side **< $0.10**, post both sides; getting filled = directional gamble not farm. WC pre-kickoff inflows (digest R3–R5) deepen books — higher reward pool and adverse-fill risk [TENTATIVE 2026-06-09].

## Dead Ends

- **"LP rewards are guaranteed yield"** — false. Adverse fills in thin markets, mis-priced near-resolution markets, and Polymarket changing the reward formula are all real risks. Treat as a yield strategy with execution + adverse-selection risk, not a savings account.
- **"$POLY airdrop is a guaranteed 50× upside"** — speculative. The airdrop is not formally announced; FDV is a guess; cohort criteria are guesses. Size positions on rewards alone; treat airdrop as a possible bonus.
- **"Use third-party LP-tracker checkers as reward predictors"** — unofficial estimators (community-built) have no insight into Polymarket's actual reward formula or eventual airdrop criteria. Useful as rough benchmarks; not as decision inputs.

## Snippets

> "No, no aposté mi dinero. ... Lo que hago es proveer liquidez en el orderbook. Básicamente le pongo plata al mercado para que otros puedan operar, y Polymarket me paga por hacer eso." [Source: Posts.docx — Post 2, @MatiasScalbi]

> "El total de LP Rewards repartidos es de $15,856,173. Y para estar en el Top 10% necesitás apenas $48 dólares acumulados en rewards. Para el Top 1%, $1,576." [Source: Posts.docx — Post 2, @MatiasScalbi]

> "Always place orders on both sides. Buy YES + Buy NO. Polymarket heavily penalizes one-sided liquidity, they divide your score by 3. Two sides = 3x more rewards for the same capital." [Source: Posts 2.docx — Post 4, @MatiasScalbi]

> "Calculate your participation before entering. If the market has $2K in liquidity and you put in $200, your share is 0.2%. If the reward pool is $500/day, you earn $1/day." [Source: Posts 2.docx — Post 4, @MatiasScalbi]

> "For bot: the edge is in the plumbing, not the algorithm. Fill detection, position reconciliation, cancellation of orphaned orders, dust cleanup. 80% of the code isn't strategy, it's survival." [Source: Posts 2.docx — Post 4, @MatiasScalbi]

> "$50 deployed, sitting top 15% of all LP providers on the platform and the window is still open." [Source: K56 Posts.docx Post 1 — Drake Iceman LP-farming Day 2]

> "Polymarket currently running boosted LP rewards on new markets -> $300-600 per market on top of regular fees." [Source: K56 Posts.docx Post 1 — independent confirmation of @MatiasScalbi's earlier claim]
