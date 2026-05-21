---
title: "Trading posts compilation (Posts 2) — Time-series ARIMA/GARCH framework, OpenHuman desktop agent, conflict-detector multi-module BTC bot, 21 LP-rewards tactical tips (May 2026)"
type: source
tags: [source, trading-posts, social-media, time-series-analysis, arima-garch, openhuman-agent, multi-module-bot, polymarket-btc-bot, lp-rewards-tactics, k55]
keywords: [rohonchain, time-series-framework, arima, garch, unit-root-spurious-regression, alphasignalai, senamakel, openhuman, memory-tree, tokenjuice, gustafssonkotte, polymarket-btc-bot, conflict-detector-spread-filter, chainlink-data-streams, matiasscalbi, polymarket-lp-tactics, time-weighted-open-interest]
related:
  - concepts/time-series-arima-garch-framework.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/polymarket-bot-architecture.md
  - concepts/markov-regime-switching-models.md
  - entities/people/rohonchain.md
  - entities/people/matias-scalbi.md
  - entities/people/gustafssonkotte.md
  - entities/tools/openhuman.md
  - entities/tools/chainlink-data-streams.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/quant-finance.md
  - entities/platforms/polymarket.md
  - concepts/polymarket-lp-bot-phase0-spec.md

maturity: validated
read_status: deep-read
created: 2026-05-20
updated: 2026-05-20
clusters: [quant-finance, polymarket]
---

## Relations

- @concepts/time-series-arima-garch-framework.md — synthesized from Post 1 (@RohOnChain time-series framework with code)
- @concepts/multi-module-bot-conflict-detector-pattern.md — synthesized from Post 3 (@Gustafssonkotte "deleted half my code" rewrite)
- @concepts/polymarket-lp-rewards-farming.md — extended with Post 4 (@MatiasScalbi 21 tactical LP-rewards tips)
- @concepts/polymarket-bot-architecture.md — Post 3 adds the "broken-data-corrupts-the-brain" lesson + the multi-module synthesis pattern
- @concepts/markov-regime-switching-models.md — Post 1 is the @RohOnChain author's companion to his earlier Markov-chain piece
- @entities/people/rohonchain.md — author of Post 1
- @entities/people/matias-scalbi.md — author of Post 4 (second installment after the Posts.docx LP-rewards guide)
- @entities/people/gustafssonkotte.md — author of Post 3
- @entities/tools/openhuman.md — Post 2 covers the OpenHuman desktop AI agent (off-topic OSINT-side → routed to ccc-wiki brief)
- @entities/tools/chainlink-data-streams.md — Post 3 explicitly uses Chainlink Data Streams as the BTC price feed

## Raw Concept

- **Title**: `Posts 2.docx` — second compilation of four trader social-media posts/articles
- **Type**: social-media long-form posts (Twitter/X creators)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/posts-2-time-series-conflict-detector-2026-05-20.docx`
- **Retrieved**: 2026-05-20 (dropped into `research to be indexed/`)
- **Contents**: 4 posts — (1) @RohOnChain "How To Build A Time Series Model To Win Every Single Trade" — ARIMA/GARCH framework with code; (2) @AlphaSignalAI deep-dive on @senamakel's OpenHuman (open-source desktop AI agent, 20k+ stars) — off-topic for OSINT, routed to ccc-wiki brief; (3) @Gustafssonkotte "Deleted half my bot's code and it started winning" — Polymarket BTC 5-min bot rewrite with multi-module conflict-detector pattern, 41% → 60% WR; (4) @MatiasScalbi 21 tactical LP-rewards tips for Polymarket farming (companion to the earlier Spanish-language guide in Posts.docx).

## Narrative

### Post 1 — @RohOnChain: "How To Build A Time Series Model To Win Every Single Trade (Quant Framework)"

Third in @RohOnChain's quant-framework series — the time-series layer that complements his earlier Markov Chains (regime detection, K49) and Neural Networks (signal generation) posts. Title hyperbole notwithstanding, the body is a careful, mathematically literate walkthrough. → synthesized into `@concepts/time-series-arima-garch-framework.md`.

**Headline thesis**: every time series is the visible output of an invisible *data-generating process*; the time-series model fits the visible component while the invisible component (the actual underlying economy) is what eventually breaks it. The 2008 mortgage-securities crisis is the canonical example — the price series said "trend up" while the actual loan-creditworthiness data quietly deteriorated.

**Three tasks of time-series analysis**:
1. **Filtering** — estimate current state from past + present (every charting indicator is a filter; e.g. moving averages).
2. **Smoothing** — estimate past state using past + future data (research-only; cannot be used for live trading because it requires future information).
3. **Forecasting** — produce an *expectation* about the future. **Critically**: a forecast is not a prediction. It is the conditional expectation E[Xₜ₊₁ | X₁..Xₜ] — the single value that minimizes squared error across all possible outcomes. It will essentially never equal the realized value. The market-maker analogy: quote a spread around the imperfect estimate and collect across thousands of trades.

**The unit-root trap** — the most important practical section. Most beginners run a regression of tomorrow's close on today's close, get R² > 0.99, and think they have a predictive model. They have **spurious regression**. The cure: use **returns**, not prices.
- Augmented Dickey-Fuller test (`statsmodels.tsa.stattools.adfuller`) — null hypothesis is that the series has a unit root; p < 0.05 means stationary; price series fail the test, return series pass.
- Convert prices to log returns: `r_t = ln(P_t) - ln(P_{t-1})`. Approximately stationary; still has volatility clustering + fat tails (handled by GARCH below).

**The ARMA family**:
- **AR(p)**: `X_t = φ₁X_{t-1} + ... + φ_pX_{t-p} + ε_t`. φ > 0 captures momentum, φ < 0 captures mean reversion.
- **MA(q)**: `X_t = ε_t + θ₁ε_{t-1} + ... + θ_qε_{t-q}`. Effect of past shocks on current value.
- **ARMA(p,q)**: combined. Differencing first if non-stationary → ARIMA(p,d,q).
- **GARCH(1,1)**: models variance as `σ_t² = ω + α₁ε²_{t-1} + β₁σ²_{t-1}`. Captures volatility clustering (large moves follow large moves). **For trading, GARCH is essential for position sizing** — high σ² → reduce position; low σ² → take more risk.

**Implementation** (runnable Python; verified — uses `yfinance`, `statsmodels`, `arch`):
```python
class TimeSeriesTradingSystem:
    def __init__(self, ticker, period="5y")
    def fetch_and_prepare()      # log returns ×100
    def check_stationarity(s)    # ADF test
    def fit_arima_garch(returns, arima_order=(1,0,1), garch_order=(1,1))
    def generate_signals(returns, lookback=252)  # walk-forward 1-step ahead
```
**Three critical implementation notes** the author flags explicitly:
1. **GARCH-based position sizing does more work than the ARIMA forecast direction**. Volatility-scaled sizing at 52-55% directional accuracy beats fixed sizing at 60% directional accuracy on risk-adjusted returns.
2. **Walk-forward is non-negotiable**. Fit on history-only, forecast 1-step ahead. Never fit on full dataset and call the in-sample predictions a backtest.
3. **Alternative data is the ceiling**; this framework is the floor. ARMA captures patterns *inside* the price series; alt-data (earnings sentiment, order flow, credit signals, cross-asset regime info) captures information about the underlying process *before* it appears in price.

**Closing prompt** (worth carrying forward): if GARCH says volatility is about to spike based on return autocorrelations, and a Markov chain says the market is about to transition from low-vol to high-vol regime based on state, **agreement** is one of the strongest risk-management signals; **disagreement** is itself information about current conditions. → links the time-series page to `@concepts/markov-regime-switching-models.md` as natural complements.

### Post 2 — @AlphaSignalAI on @senamakel: "How OpenHuman Works, And How to Set It Up in 5 Minutes"

OpenHuman is an open-source GPL-3.0 desktop AI agent from TinyHumans AI. Rust (65%) + TypeScript + React 19 frontend, Tauri v2 desktop app, macOS/Win/Linux. Crossed +20K GitHub stars in days; #1 on Product Hunt daily/weekly/monthly as of 2026-05-17. Pitch: most agents start cold; OpenHuman walks your tools every 20 minutes and writes the memory into Markdown files you can open and edit.

**Architecture** (the parts worth recording even though OSINT-side adoption is out of scope):
- **Memory Tree** — deterministic, bucket-sealed pipeline (source adapters → canonicalize → chunker → content_store → store → score → source/topic/global trees → retrieval). Data canonicalized to Markdown, ≤3K-token chunks with deterministic IDs, scored + folded into 3 trees: source (one per source, L0→L1→L2), topic (per high-hotness entity), global (per UTC day). SQLite-backed (`<workspace>/memory_tree/chunks.db`); Markdown vault at `<workspace>/wiki/` is the readable surface.
- **Auto-fetch on 20-minute tick**: only Gmail/Notion/Slack auto-ingest natively today; the 118+ Composio catalog is callable but does not auto-feed Memory Tree.
- **TokenJuice**: rule-based HTML→Markdown compression in the tool-execution path. Claim 80%, third-party measurement (PrimeAIcenter) 70%. Three-layer rule stack: builtin → user (`~/.config/tokenjuice/rules/`) → project (`.tokenjuice/rules/`).
- **Local AI** (opt-in): all-minilm (~23MB embedding) + gemma3:1b-it-qat (~700MB summary tree). 8 GB RAM floor, 16+ ideal. Five workloads can run local: embeddings, summary-tree, heartbeat, learning, subconscious. **Chat, vision, web search, OAuth proxying, TTS streaming stay cloud** — "local-first" applies to memory, not the whole stack.
- **v0.54.0** (2026-05-19): fully-local STT/TTS via Whisper + Piper; **agentmemory backend bridge** sharing a durable store with Claude Code, Cursor, Codex, OpenCode; MCP stdio memory server; NotebookLM-style folder ingestion.
- **Mascot + Meet agent**: lip-syncs to TTS; can join Google Meet through embedded CEF webview as a real participant (mic = TTS injection, camera = mascot frame producer).

**Cross-wiki routing**: this entire post is **agent-architecture / coding-tooling content**, not OSINT/financial. Routed to ccc-wiki as a brief. An entity stub for OpenHuman already exists from the K42 evaluation (`@entities/tools/openhuman.md`) — updated with the May 2026 v0.54.0 numbers + the agentmemory bridge.

**Cemini-relevance angle**: agentmemory's role mirrors Cemini's `librarian-stash` MCP — durable cross-agent memory. The Memory Tree's append-buffer → seal → L0/L1/L2 cascade is also conceptually similar to kb-server's wiki indexing, but with a different (deterministic vs vector) retrieval model. Worth a comparative note in the ccc brief.

### Post 3 — @Gustafssonkotte: "Deleted half my bot's code and it started winning"

A Polymarket BTC 5-minute Up/Down bot rewrite. The most pragmatically useful post in either batch for the Cemini stack. → synthesized into `@concepts/multi-module-bot-conflict-detector-pattern.md`.

**Numbers**:
- Before (old system, 2 weeks): 17 trades, **WR 41%**, direction-correct 47%, P&L red.
- After (v4, day 1): 33 trades, **WR 60%**, direction-correct 60% (UP 61% / DOWN 58%), P&L green.

**Three silent bugs that corrupted weeks of stats** (the *real* main lesson — Polymarket-bot-architecture-level):
1. **Voter→entry tier-field drop**: the voter labeled trades "top tier, max size" but between voter output and order placement the tier field was lost in the handoff → every "confident" entry was undersized.
2. **Drawdown-limit was a no-op**: when triggered, the code wrote "PAUSED" in red to the log and **returned success** in the risk check. Bot kept trading. Defense-in-depth turned off by default.
3. **Order-confirm fail-safe was a wreck**: "if order doesn't confirm in N seconds, assume it filled" → half the recorded "wins" never opened on the exchange. Bot was making decisions on phantom WIN data.

After fixing the bugs and re-examining the *clean* stats, WR was **worse than a coin flip** → the brain itself was broken at its foundation.

**The old "brain" — what was wrong**:
```
indicators vote → weighted sum [-1..+1] → category (top/mid/weak/min) → "fair prob" lookup table → edge = lookup - market - fee → if edge ≥ threshold, ENTER
```
Three architectural failures:
- **The "probability" table was a lookup, not a probability** — numbers picked 6 months earlier with no connection to outcome frequencies. WR by category on clean data: top 0/1, mid 1/2, weak 2/4, parse-misses 4/8 → parse misses beat "top tier" entries. Noise dressed as confidence.
- **The edge formula had the sign inverted** — model confidence vs WR: low 57%, mid 20%, **high 0%**. More "confident" = worse.
- **Indicators were averaged when they disagreed** — trend up + momentum down + levels silent → average positive → "mid category, enter." Average of contradictions.

**The new brain — three modules, conflict-detector filter** (the pattern worth lifting):

Each module answers one question and outputs `(probability ∈ [0,1], strength ∈ [0,1])`. The three questions:
1. **Where is the price going?** — MTF trends, EMA(5min) cross, EMA50/EMA200 structural filter, VWAP deviation.
2. **Where are the magnets and barriers?** — structural highs/lows, liquidity-sweep detection, order walls across Binance/Bybit/OKX/Coinbase, anti-spoof filter.
3. **Is momentum for or against?** — RSI (two periods), Bollinger Bands (squeeze + breakout), Parabolic SAR, Fair Value Gap, orderbook pressure.

The brain then computes:
```python
confidence = weighted_average(p_trend, p_level, p_momentum)
strength   = average(s_trend, s_level, s_momentum)
spread     = max(p_trend, p_level, p_momentum) - min(p_trend, p_level, p_momentum)

if spread > THRESHOLD:
    return SKIP("internal_conflict")
```
**The conflict-detector filter is not a feature — it is a fix.** It removes false entries the system should never have been making. Example:
```
Q1 TREND:    p_up=0.76  S=0.51
Q2 LEVELS:   p_up=0.67  S=0.34
Q3 MOMENTUM: p_up=0.10  S=0.80   (RSI overbought, waiting for pullback)
SKIP: internal_conflict, spread=0.66
```

**Time-aware sizing** (5-min market structural insight): last 90 seconds are statistically more predictable than the first 3 minutes — price has already chosen direction. Position size scales:
```python
def time_factor(mins_left):
    if mins_left >= 4.0:  return 0.7
    if mins_left >= 3.0:  return 0.85
    if mins_left >= 2.0:  return 1.0
    if mins_left >= 1.0:  return 1.2
    return 1.3
size = base * confidence * (1 - spread) * strength * time_factor
```

**Protections in firing order**: trading hours → weekend block → loss streak (3 losses → short pause) → drawdown limit → daily loss limit → internal conflict → low confidence → low strength.

**Stack**:
- Python
- **Chainlink Data Streams for BTC price feed** (explicitly bypasses exchange APIs — see new entity page `@entities/tools/chainlink-data-streams.md`)
- Polymarket CLOB for execution
- Multi-exchange WebSocket orderbook feeds (Binance/Bybit/OKX/Coinbase)
- Ubuntu VPS

**Cemini relevance**: third independent operator (after @0x_Punisher, @adiix_official) corroborating the **execution > strategy** lesson, plus a concrete architectural pattern (multi-module conflict-detector) that maps directly onto how a Cemini Polymarket UpDown bot should be structured. Several elements should be lifted: (i) the "modules disagree → SKIP" filter; (ii) time-aware sizing on short-resolution markets; (iii) using a price-feed oracle (Chainlink) instead of the exchange API that you trade against; (iv) Polymarket exports as the source-of-truth for stats, never the bot's internal counter.

### Post 4 — @MatiasScalbi: 21 LP-rewards tactical tips for Polymarket farming

Companion to the Posts.docx Spanish-language airdrop guide — same author, same thesis, but tactical and English. → extends `@concepts/polymarket-lp-rewards-farming.md` with the practical layer.

Tactics worth recording (consolidated; numbered in source post):

| # | Tip | Rationale |
|---|---|---|
| 1 | **Start with high-liquidity markets** (vol ≥ $40K, ideally $100K) | If you provide the liquidity in a thin market, there's no one to sell to when you get filled |
| 2 | **Avoid markets resolving in <14 days** | Near resolution price moves 20-30% on any news; LP becomes a gift for informed traders |
| 3 | **Bot: place orders 3-4¢ from mid; small/aggressive account: from 2¢** | Reward score scales with proximity to mid; don't go to 1¢ without experience |
| 4 | **Always place BOTH sides** (buy YES + buy NO) | Polymarket divides one-sided LP score by 3 — two sides = 3× rewards for same capital |
| 5 | **Calculate participation share before entering** | If pool is $500/day and your share is 0.2%, you earn $1/day. Aim for ≥0.5% participation |
| 6 | **If filled, sell as LIMIT (not market)** | LP-rewards + maker rebates while waiting; market sell on thin book = 10-30% slippage |
| 7 | **With $200, choose 3-7 markets** | Position at market's min-share size; on 20-share-min markets, 20 shares per side can capture 10% participation |
| 8 | **Mid 40-60¢ markets are safest** | Symmetric tail-risk; 85¢ filled → drop to 50¢ = 32¢/share loss vs 50¢ → 40¢ = 7¢ |
| 9 | **Look for large walls; rule: wall = 10× market min-shares** | Position above or 1¢ cheaper if you can quickly flip to limit sell on fill |
| 10 | **Bot: avoid entertainment/AI-release/single-day-event markets** | 50%+ moves in minutes; only long-term political or stable binary questions |
| 11 | **Check positions every 4-6h minimum** | No stop-loss on Polymarket; 10¢ adverse move while you sleep → executed LP with growing loss |
| 12 | **Don't chase high-reward pools blindly** | Competition lowers your participation share; small markets at $20-50 min-share with +5-10% participation beat huge pools at 0.2% |
| 13 | **Diversify by theme** | Iran-themed positions all break together on a Trump-Iran deal — mix US politics + foreign elections + long-term |
| 14 | **Bot: edge is in plumbing, not algorithm** | Fill detection, position reconciliation, cancel-orphaned-orders, dust cleanup — 80% of code is survival |
| 15 | **Position cap: 35% of capital small-acct / 15% bot** | 30% adverse move with 7+ markets absorbing the hit doesn't blow the portfolio |
| 16 | **First week: most effort, lowest capital** | Reserve $50-100 bot / $10-15 small acct as "tuition" |
| 17 | **Keep a fill log** | Entry, exit, time-to-sell, P&L. After 30 trades patterns emerge |
| 18 | **Manual: watch live participation %**; pull capital if <0.3% | Move to less-competitive markets |
| 19 | **Start LP provision at night (00 UTC)** | Front-loads the daily reward calculation; must hit $1/day minimum to claim |
| 20 | **Don't marry a market** | If participation drops below 1% on a market, rotate out; small capital's edge is mobility |
| 21 | **Patience > aggression** | Rewards accrue per minute in book; cancel/reposition every 5 minutes loses 5 min of sampling |

**Author's "challenge account" run**: $200 starting capital → +$40 net profit / $38 LP rewards over 10 days. The author's two other accounts are at $4-6K capital each.

**Cemini relevance**: the tactical layer is what would actually configure a Polymarket LP bot for Cemini. Every tip translates to a runtime parameter or filter on the order-placement engine. Folds directly into the cemini-prod brief.

## Snippets

> "A time series can tell you what that line has been doing. It cannot tell you what is actually causing it. And the moment the underlying reality changes, your model becomes a liability instead of an asset." [Source: Posts 2.docx — Post 1, @RohOnChain]

> "A forecast is not a prediction. It is the conditional expectation, the single value that minimizes average squared error across all possible future outcomes. It will essentially never equal the realized value." [Source: Posts 2.docx — Post 1, @RohOnChain]

> "The GARCH-based position sizing is doing more work than the ARIMA forecast direction. Reducing exposure during high volatility regimes is the most reliable edge in the entire system." [Source: Posts 2.docx — Post 1, @RohOnChain]

> "The bot wasn't losing because it was bad. The bot was losing because I was listening to its broken brain. Every loss was a signal. I was averaging them into an 'entry'. The hard part wasn't writing new indicators. The hard part was deleting the old ones that pretended to work." [Source: Posts 2.docx — Post 3, @Gustafssonkotte]

> "The conflict filter doesn't add new logic. It removes false entries the system should never have been making. It's not an improvement. It's a fix." [Source: Posts 2.docx — Post 3, @Gustafssonkotte]

> "Always place orders on both sides. Buy YES + Buy NO. Polymarket heavily penalizes one-sided liquidity, they divide your score by 3. Two sides = 3x more rewards for the same capital." [Source: Posts 2.docx — Post 4, @MatiasScalbi]

> "For bot: the edge is in the plumbing, not the algorithm. Fill detection, position reconciliation, cancellation of orphaned orders, dust cleanup. 80% of the code isn't strategy, it's survival." [Source: Posts 2.docx — Post 4, @MatiasScalbi]
