---
title: "X-posts (May 2026) — Polymarket LP-farming live test + copy-trading + event-based ML + MCPT + Karpathy-meta + Obsidian"
type: source
tags: [source, x-posts, twitter, polymarket, lp-farming, copy-trading, neural-networks, monte-carlo-permutation-test, time-series, karpathy, system-prompt-learning, claude-md, obsidian, k56]
keywords: [alexo_0x, polymarket-lp-farming-drake-iceman, igor-mikerin-pretracer, dexterssolab-kreopolybot, _avichawla-karpathy-system-prompts, phosphenq-mcpt-monte-carlo-permutation, 0xdepressionn-karpathy-claude-md, cyrilxbt-obsidian-personal-os, rohonchain-time-series-duplicate, polymarketanalytics-com, neymar-fifa-2026-lp-market]
related:
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/event-based-prediction-market-ml.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/time-series-arima-garch-framework.md
  - entities/people/alexo-0x.md
  - entities/people/igor-mikerin.md
  - entities/people/dexterssolab.md
  - entities/people/phosphenq.md
  - entities/people/rohonchain.md
  - entities/tools/pretracer.md
  - entities/tools/kreopolybot.md
  - entities/tools/polymarketanalytics-com.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/market-memory-hurst-regime.md
  - sources/trading-posts-compilation-38-2026-05-26.md

maturity: validated
created: 2026-05-21
updated: 2026-05-26
read_status: read
clusters: [polymarket, quant-finance, copy-trading]
---

## Relations

- @concepts/polymarket-lp-rewards-farming.md — Post 1 (anon Drake-market case study + Neymar-FIFA setup) provides concrete live-test numbers
- @concepts/polymarket-copy-trading-strategy.md — Posts 2 + 3 (igor_mikerin + DextersSolab) synthesize into the strategy page
- @concepts/event-based-prediction-market-ml.md — Post 0 (@Alexo_0x) primary source
- @concepts/monte-carlo-permutation-test-mcpt.md — Post 5 (@phosphenq) primary source
- @concepts/time-series-arima-garch-framework.md — Post 8 is a duplicate of @RohOnChain's K55 article (already synthesized there); cross-referenced for completeness
- @entities/people/alexo-0x.md, @entities/people/igor-mikerin.md, @entities/people/dexterssolab.md, @entities/people/phosphenq.md, @entities/people/rohonchain.md — authors
- @entities/tools/pretracer.md, @entities/tools/kreopolybot.md, @entities/tools/polymarketanalytics-com.md — copy-trading infrastructure surfaced

## Raw Concept

- **Title**: Posts.docx (9 X-posts compiled, separator: "Next Post:")
- **Provenance**: Dropped into `research to be indexed/` by Claudio on 2026-05-21
- **Canonical location**: `cemini-librarian:/opt/cemini-bulk/research/posts-prediction-markets-quant-frameworks-2026-05-21.docx` (post-ingest move)
- **Retrieved**: 2026-05-21
- **Type**: X (Twitter) long-form posts, compiled
- **Length**: ~145,000 chars across 9 posts
- **Read status**: read

## Narrative

Nine X-posts spanning prediction-market trading mechanics, quant frameworks, and Claude-Code meta-topics. Of the nine, **5 are OSINT-relevant** (Polymarket LP-farming, copy-trading, event-based ML, quant validation, time-series — though the last is a re-share of a K55-ingested article), and **3 route to ccc-wiki** (Karpathy meta-RL, Karpathy's CLAUDE.md, Obsidian-as-personal-OS). The user-flagged centerpiece is the **anonymous LP-farming live test on the Drake "Iceman" first-week-album-sales market** — a 5-position spread that returned $4 on $50 in 5 hours, then $18 in LP rewards on day 2, ranking the test wallet at #21,829/145,703 (Top 15%) — providing the first concrete numbers for the K55 LP-rewards-farming page.

### Post 0 — @Alexo_0x: "Neural Networks for Polymarket & Crypto Prediction Markets: Why 94% of Signal Models Fail in Product"

A rigorous, math-literate breakdown of why most neural-network models on prediction markets lose money, and what the failure modes look like at the architectural level. The post sits at the intersection of @RohOnChain's quant-framework series (Markov / NN / time-series) and @phosphenq's strategy-validation thinking, but specifically targets the **event-resolution structure** of prediction markets that breaks equity-style modeling.

The five-part framework:

1. **What a NN actually learns on Polymarket**: probability `P(Outcome=1 | X_t)`, not price `E[P_{t+1} | X_t]`. Seems simpler — isn't. The distribution shifts qualitatively as resolution date approaches: 60 days out → 0.6, 1 hour out → 0.95/0.05, post-resolution → 1.0/0.0. A model trained on 60-day-out data knows nothing about final-hour dynamics. Algorithmic MMs arbitrage final-hour edges aggressively; news flow has accelerated; large players enter late.
2. **Stability filter (event-aware ADF)**: Standard ADF on rolling window works on equities (one continuous series). On Polymarket, the filter must operate **per event** (events can't be concatenated). Code in source: `event_rolling_adf_filter(event_price_series, lookback_hours=168, step_hours=24)` → passes if <20% of windows are non-stationary.
3. **Why LSTMs fail on Polymarket**: equities = 750 samples over 3 years; Polymarket = one sample per event. Cannot train an LSTM on a single event. Two workable approaches: **(A) cross-event learning** across 150-250 events (elections / crypto / regulatory / AI events); **(B) synthetic Ornstein-Uhlenbeck trajectories** (10,000+) then fine-tune on 3-5 real events from new category.
4. **Hard parameter rule**: max trainable params ≤ total samples / 20. Example: 150 events × 500h avg = 75,000 samples → 3,750 params max. `hidden_size=8` or `16` is normal; `32` is risky; `64+` guarantees overfitting.
5. **Honest validation (temporal-split-by-start-date)**: sort by `start_date`, train on older, normalize per-event. Prohibitions: no random shuffling, no future events in training, no cross-event normalization. Lookahead check: any feature using info available after the timestamp = cheating.
6. **Kill conditions for event-based models** (90-day Sharpe doesn't work — 3-5 events isn't statistics):
   - **Log-loss gap**: kill if model log-loss > market log-loss over last 5-7 events ("the market predicts better than your model")
   - **Bayesian Factor** (truncated in source) for small samples

→ Synthesized into `@concepts/event-based-prediction-market-ml.md`.

### Post 1 — Anonymous: LP-farming live test on Polymarket (Drake "Iceman" + Neymar FIFA-2026)

Three sub-posts compiled. The most-cited live test of the K55 LP-rewards-farming concept page:

**Drake "Iceman" First Week Album Sales market** ($50 deposit, 5 positions on first-week-album-sales ranges):
- 300k-350k → 7% prob → Yes 7.3¢ / No 92.8¢
- 350k-400k → 7% → Yes 6.9¢ / No 93.2¢
- 400k-450k → 12% → Yes 12.6¢ / No 88.3¢
- 450k-500k → 17% → Yes 17.3¢ / No 83.7¢
- 500k-550k → 24% → Yes 25.0¢ / No 76.8¢
- **Result Day 1**: $4 returned in 5 hours (~8% in a few hours, no directional bet)
- **Result Day 2**: $18 LP rewards total. Rank #21,829 / 145,703 = **Top 14.98%** ($17 from Top 10%).
- **Confirmation**: Polymarket running boosted LP rewards on new markets at **$300-600 per market** on top of regular fees.

**Neymar FIFA-2026 World Cup market** (cited as "zero-risk" setup):
- Current price 94¢, Yes spread just 1¢
- Order book: asks 94-97¢ totalling $830k+, bids 90-93¢ totalling $328k+
- LP rewards: $300/market
- Claim: hundreds of thousands of dollars on both sides with 1¢ spread → constant fills; 94¢ price → crowd already convinced → low directional risk; LP earns base $300 + per-fill on top.

These numbers convert the K55 page from "@MatiasScalbi says this works" into "an independent retail trader documented the math, the ranges, and the exact rewards-per-market figure." The capital-sizing analysis in the K55 page (`@concepts/polymarket-lp-rewards-farming.md`) gains a concrete data point: **$50 of capital → $18 of rewards over 48 hours → Top 15% LP rank**. Rewards/capital ratio is enormous at small sizes (because the leaderboard is back-loaded with whales who don't bother farming).

### Post 2 — @igor_mikerin: "Polymarket Copy-trading. $10,000/month."

Promotional post for **Pretracer** (Telegram bot, `@pretracer`) wrapped around a copy-trading tutorial. Three discovery channels:
- **A. Polymarket Leaderboard** (`polymarket.com/leaderboard`) — filter for consistency, specialization, early entry, controlled sizing.
- **B. Pretracer Wallet Tracker** — real-time notifications on selected wallets with custom filter criteria (win-rate, total-profit, etc.).
- **C. Pretracer Wallet Parser** — passive observer mode (study a wallet's pattern before deciding to copy).

Five "recommended wallets" given as referral links:
- `polymarket.com/@RN1`
- `polymarket.com/@wooter`
- `polymarket.com/@212121212121212121212`
- `polymarket.com/livebreathevolatility`
- `polymarket.com/@BulkeyBull`

**Self-reported result**: $10,000 net profit in February following these five wallets. Pretracer pitched at ~100ms latency, no fees, runs inside Telegram, USDC funding only.

`[TENTATIVE 2026-05-29]` Pretracer's claim of 100ms latency and zero fees — single-source referral marketing; no independent Pretracer docs found via web search. See @entities/tools/pretracer.md for competitor latency/fee benchmarks.

### Post 3 — @DextersSolab: "I publicly made 6 figs on Polymarket copy trading"

Substantive long-form on copy-trading mistakes and the right setup. Author claims $32,700 in one month; promotes **KreoPolyBot** (`t.me/KreoPolyBot?start=ref-dexter`). Four catastrophic copy-trading mistakes:

1. **Copying bots and HFT wallets** — they have co-located infra, sub-20ms execution; your bot fires after the price has moved → you're buying their exit at full price. Skip wallets with hundreds of trades/day at tiny margins.
2. **Copying short track records** — 10 wins in a row in a small sample is random chance. Never copy <3 months of consistent history.
3. **Copying the same wallet as everyone** — when a wallet goes viral, liquidity disappears, entry prices worsen, returns compress. Best wallets are unknown.
4. **Copying without understanding strategy** — some traders hedge across multiple wallets / off-platform; copying one leg of a hedged position = pure directional risk they never had.

Wallet-discovery framework via `polymarketanalytics.com` (free filter platform):
- Overall PnL: $15,000 - $400,000
- Current value: at least $5,000
- Active positions: at least 2
- Total positions: at least 20
- Win rate: at least 70%
- Consistency: 2-3 months of steady results, not one spike
- Trade frequency: 30-200 trades/month (not 10, not 1,000)
- Specialization: 1-3 niches (politics / weather / sports)
- Drawdown control: cut losses quickly, no doubling down

KreoPolyBot setup (4 sizing options): Fixed / Exact / Percentage / Portfolio. Recommends 5% slippage, 70% percentage-stop-loss, Buys + Sells. Latency claim: faster than Pretracer.

→ Synthesized with Post 2 into `@concepts/polymarket-copy-trading-strategy.md`.

### Post 4 — @_avichawla: "How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea)"

Off-topic for OSINT. CCC-relevant: Karpathy's "system prompt learning" framing of meta-RL; how Anthropic/OpenAI/DeepSeek are converging on using system-prompt mutations as the RL primitive. **→ Routed to ccc-wiki via brief.**

### Post 5 — @phosphenq: "How To Tell If Your Trading Strategy Is Real Or Random (Quant Framework)"

Substantive long-form. Introduces the **Monte Carlo Permutation Test (MCPT)** formalized for trading by Timothy Masters (*Permutation and Randomization Tests for Trading System Development*, 2020). Live case study: a Polymarket market that resolved one day prior. The case-study strategy **fails** the test.

Core insight: every backtest is guilty until proven innocent. Two questions every quant asks pre-go-live: (1) "Is this excellent?" (calibration — PF 1.05 isn't interesting; PF 2.5 might be) and (2) "Is this obviously overfit?" (overfitting check — PF 4 + zero drawdown = future leak or memorization).

Two-types-of-edge framing:
- **Alpha**: intrinsic market pattern; a real backtest captures it; live strategy exploits it.
- **Data-mining bias**: residual signal any sufficiently powerful optimizer finds in any sufficiently long noise stream.

MCPT is the test that distinguishes them. (Full mechanics documented in `@concepts/monte-carlo-permutation-test-mcpt.md`.)

→ Synthesized into `@concepts/monte-carlo-permutation-test-mcpt.md`.

### Post 6 — @0xDepressionn: "Karpathy's CLAUDE.md hit #1 on GitHub with 82,000 stars"

Off-topic for OSINT. CCC-relevant: Karpathy published his `CLAUDE.md` instructions file, hitting GitHub Trending #1 with 82k stars and 7.8k forks. **→ Routed to ccc-wiki via brief** (CCC's `concepts/claude-md-12-rule-template.md` is the natural extension point).

### Post 7 — @cyrilXBT: "How to Turn Obsidian Into a Personal Operating System That Never Breaks Down"

Off-topic for OSINT. CCC-relevant for personal-knowledge-management / curator workflow comparison. **→ Routed to ccc-wiki via brief** (cross-reference to OSINT's own curator/librarian model).

### Post 8 — Anonymous: "How To Build A Time Series Model To Win Every Single Trade (Quant Framework)"

**Duplicate of K55 source**. This is the same @RohOnChain article already ingested in `@sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md` Post 1 and synthesized into `@concepts/time-series-arima-garch-framework.md`. Re-shared by author or a syndication account. No new pages required; backlink only.

## Snippets

> "60 days before an event: probability around 0.6. 1 hour before the event: 0.95 or 0.05. After resolution: 1.0 or 0.0. A model trained 60 days before an event knows nothing about the dynamics of the final hour."
> — @Alexo_0x [Source: Posts.docx Post 0]

> "Maximum trainable parameters should not exceed the number of samples divided by 20. […] `hidden_size=8` or `16` is normal. `hidden_size=32` is risky. `hidden_size=64` or more guarantees overfitting."
> — @Alexo_0x [Source: Posts.docx Post 0]

> "$50 deployed, sitting top 15% of all LP providers on the platform and the window is still open."
> — Anonymous [Source: Posts.docx Post 1 — Drake Iceman LP-farming Day 2]

> "Polymarket currently running boosted LP rewards on new markets -> $300-600 per market on top of regular fees."
> — Anonymous [Source: Posts.docx Post 1]

> "You are not copying their entry. You are buying their exit at full price."
> — @DextersSolab on copying HFT wallets [Source: Posts.docx Post 3]

> "Quants treat every backtest as guilty until proven innocent. They run one statistical test on it. […] It is the Monte Carlo permutation test. MCPT for short."
> — @phosphenq [Source: Posts.docx Post 5]

> "A measure that becomes a target is no longer a good measure. Your validation set is the measure. Every time you reuse it, you turn it into a target."
> — @phosphenq paraphrasing Goodhart [Source: Posts.docx Post 5]
