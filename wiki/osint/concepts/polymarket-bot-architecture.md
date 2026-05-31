---
title: Polymarket bot architecture — playbook from @0x_Punisher (May 2026)
type: concept
tags: [concept, polymarket, trading-bot, prediction-markets, websocket, backtesting, latency, cemini]
keywords: [polymarket, CLOB, websocket, FAK, GTC, latency, hot path, HMAC, backtesting, 6-layer websocket, market maker, ladder bot, NSF, fishy resolution]
related:
  - sources/x-polymarket-bot-playbook-punisher-2026-05.md
  - entities/platforms/polymarket.md
  - concepts/cemini-license-posture.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/kelly-sizing-quarter.md
  - entities/tools/bukosabino-ta.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-gamma-api.md
  - sources/alterego-eth-polymarket-gamma-vs-clob.md
  - sources/alterego-eth-polymarket-endpoint-cheatsheet.md
  - sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md
  - sources/trading-posts-compilation-38-2026-05-26.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - entities/tools/harrier-pm-toolkits.md
  - entities/tools/polymarket-skills-mjunaidca.md
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - concepts/polymarket-api-reference.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - entities/tools/polymarket-websocket-api.md
  - concepts/prediction-market-information-leakage-score.md
  - sources/arxiv-foresightflow-ils-polymarket-2605.00493.md
  - entities/tools/discountifu-polymarket-trading-bot.md
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - concepts/perps-dex-funding-carry-strategy.md
  - concepts/sports-prediction-consensus-agent.md
  - entities/people/gustafssonkotte.md
  - sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md
  - concepts/polymarket-wallet-alpha-pipeline.md
  - entities/tools/ai-polymarket-agent.md
  - concepts/event-based-prediction-market-ml.md
  - sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md
  - concepts/polymarket-three-quadrant-blacklist-microtrend.md
  - concepts/polymarket-retail-trading-discipline.md
  - entities/tools/flox.md
  - concepts/polymarket-copy-trading-strategy.md
  - entities/tools/nofx-ai-os.md
  - sources/analyzing-github-projects-agentic-infra-2026-05-21.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/cme-settlement-mechanics-for-prediction-markets.md
  - entities/tools/polymarket-near-resolution-bot.md
  - sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md
  - sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md
  - entities/tools/trademaster.md
  - sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md
  - entities/people/coldmath-polymarket.md
  - sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md
  - concepts/polymarket-btc-already-position-gate.md
  - concepts/polymarket-news-resolution-speed-game.md
  - sources/trading-posts-compilation-20-2026-05-27.md
  - sources/trading-posts-compilation-k84-2026-05-30.md
  - sources/trading-posts-compilation-42-2026-05-31.md
  - concepts/polymarket-negative-filter-trading.md
  - concepts/polymarket-updown-indicator-stack.md
  - sources/alterego-eth-five-weather-methodologies-2026-05-27.md
  - concepts/polymarket-weather-bot-methodology-taxonomy.md
  - concepts/production-trading-blind-spots.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/pnl-attribution-versioning.md
  - concepts/clean-room-software-design.md
  - concepts/zero-trade-edge-signal-diagnostics.md
  - sources/algorithmic-trading-pipeline-zero-trade-analysis-2026-05-28.md
  - sources/clean-room-design-proprietary-software-2026-05-28.md

maturity: draft
created: 2026-05-12
updated: 2026-05-29
---

## Relations

- `@sources/x-polymarket-bot-playbook-punisher-2026-05.md` — original X thread + long-form article
- `@entities/platforms/polymarket.md` — platform entity page (create stub if absent)
- `@concepts/cemini-license-posture.md` — IP-sale-readiness frame (no license issue here; pattern, not code)
- `@sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md` — @bored2boar's independent bot playbook (May 2026), corroborating this page
- `@sources/alterego-eth-polymarket-endpoint-cheatsheet.md` — K51 @AlterEgo_eth full endpoint cheat sheet; the API surface this playbook's bot consumes
- `@concepts/polymarket-api-reference.md` — canonical five-surface endpoint index
- `@sources/x-posts-quant-oss-polymarket-bots-2026-05.md` — K52 X-posts batch; Post 6 (@adiix_official) independently corroborates this playbook's build discipline
- `@concepts/polymarket-updown-bot-taxonomy.md` — the 6-type *strategy* taxonomy that sits on top of this *engineering* playbook
- `@entities/tools/polymarket-websocket-api.md` — WebSocket channels the 6-layer websocket system subscribes to
- `@entities/tools/discountifu-polymarket-trading-bot.md` — K53 Adopt-eligible MIT bot; a concrete CLOB-V2 / WebSocket-orderbook implementation of this playbook
- `@sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md` — K55 source; @morpphhhaw perps-funding-carry bot independently corroborates the "infrastructure-first / failed-open-on-one-leg = first-class risk event" lessons
- `@sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md` — K55 source; @Gustafssonkotte Polymarket BTC bot adds the broken-data + multi-module conflict-detector lessons (fourth independent operator confirmation)
- `@concepts/polymarket-lp-rewards-farming.md` — K55: the *maker-side* yield strategy on Polymarket; complement to this taker-side bot architecture
- `@sources/trading-posts-compilation-42-2026-05-31.md` — K88 @myttle_web3 negative-filter + @DankoWeb3 indicator stack
- `@concepts/polymarket-negative-filter-trading.md` — skip-before-speed pattern
- `@concepts/perps-dex-funding-carry-strategy.md` — K55: portable failure-mode lessons from cross-venue perps strategies; same "execution > strategy" thesis
- `@concepts/production-trading-blind-spots.md` — K75: operational checklist including phantom-WIN and reconciliation rows from this playbook
- `@concepts/pnl-attribution-versioning.md` — K75: prod `logic_version` pattern generalizes CSV-as-truth lesson
- `@concepts/trading-bot-logging-discipline.md` — K75: structured reconciliation logs
- `@sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md` — K57 Posts.docx (Gustafsson, vorty, spottr, polydao)
- `@concepts/polymarket-three-quadrant-blacklist-microtrend.md` — K57 Gustafsson blacklist + micro-trend
- `@concepts/polymarket-retail-trading-discipline.md` — K57 retail edge framing
- `@concepts/polymarket-copy-trading-strategy.md` — K57 Spottr hybrid CLOB latency section
- `@entities/tools/trademaster.md` — K60 Steal-from RL platform; simulator/benchmark patterns for future bot eval (not a Polymarket bot itself)
- `@sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md` — K61 ColdMath micro-scaling adversary on weather books
- `@entities/people/coldmath-polymarket.md` — K61 adversary operator
- `@sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md` — K62 position-already gate (Gustafsson)
- `@concepts/polymarket-btc-already-position-gate.md` — K62 synthesized pattern
- `@sources/alterego-eth-five-weather-methodologies-2026-05-27.md` — K70 weather-specific strategy taxonomy (types 1–2 ↔ this engineering playbook)
- `@concepts/polymarket-weather-bot-methodology-taxonomy.md` — K70 five-type framework

## Raw Concept

X-thread + long-form article by @0x_Punisher (handle: punisher) detailing how a Polymarket bot operator went from -$8K to $100K+ public PnL profile (`polymarket.com/@pbot-6`). Self-described as "the full fix guide from someone who has repaired 1,000+ broken bots publicly." Distilled into a concept page so Cemini's own Polymarket adapter can absorb the operational lessons.

## Narrative

### Top-line architecture (8 steps)

1. **Prerequisites** — Python + NumPy, dedicated low-latency infra (VPS/home server, 100-300+ websockets concurrent), live Polymarket API access + real wallet (zero-balance dry-runs as part of testing), CLOB + Gamma websockets + external (Binance/Coinbase) feeds, **own historical tick data** (18+ months recorded, no public substitutes for serious work).

2. **6-layer websocket system** — see dedicated subsection below; the load-bearing engineering content of the playbook.

3. **Historical data collection** — record every tick yourself via the websocket setup. Store order-book depth, fills, slippage.

4. **Backtesting discipline** — split strategies into two types:
   - **Type 1 (~90% of working bots)**: bet-at-window-open on external signals (Binance direction, mean reversion, candles). AI-backtestable from strike + close + signal alone.
   - **Type 2 (more profitable, harder)**: mid-window trading, GTC bids, stops, order-book modeling. Requires own tick recordings.

   Backtest workflow: 20-min manual test → 2-hr multivariate sweep + 3-fold CV + overfit checks → 30-min strategy template → live dry-run with zero balance → treat every NSF rejection as data → re-backtest → deploy only if backtest matches live within ~3%.

   **Critical rule — win rate vs entry price**: 70% WR strategy loses money if you enter at 57¢ (needs >57% WR to break even). Enter at 40¢ → only need >40% WR. Rule of thumb: +5¢ to break even, +10¢ to profit. You cannot filter for lower prices (removes probable winners). Base strategy must *naturally* enter lower with higher probability.

5. **Strategy development cycle** — idea → manual test (20m) → full sweep (2h) → template (30m) → dry-run + re-backtest (1-7d). "99 out of 100 ideas die here." Survivors are usually **market-maker** or **ladder bots** — most common and profitable bot class on the platform. Directional strategies work but are least profitable.

6. **Stop losses + risk controls** — Polymarket has no native stops; code them with zero added latency. Test thoroughly — sometimes no-stop performs better on shorter windows. Best results on BTC with strict filters (avoid betting blindly above 85¢).

7. **Dry run + deploy + monitor** — real wallet with zero balance until backtest and live match perfectly. Deploy small first. Monitor for **fishy resolutions** (1¢ discrepancies vs Binance/Coinbase charts) → pause + cross-verify. Log everything, review daily.

8. **Common-issue catalog** — fishy final prices, stale/jittery data, over-optimistic AI backtests, adverse selection, magic 0¢-100% wallets (Polymarket's NegRisk infrastructure, PnL = 0, ignore them).

### The 6-layer websocket system (load-bearing)

Raw Polymarket websockets are full of stale snapshots, missed ticks, jitter, brief disconnects. The 6-layer system turns them into ultra-clean streams. Applies to CLOB, Gamma, Binance, or any other feed.

- **Layer 1 — warmup + quality gate**: start every connection 15s before window opens (both yes + no tokens). In final 5s require ≥3 ticks per token + no single jump bigger than 5¢. Fail → skip the entire window.
- **Layer 2 — volume + dynamic spawning**: 100-300 parallel websockets. Every 4s, kill + respawn slowest 10%. Bot always takes the first unique (deduplicated) tick.
- **Layer 3 — stale tick guard**: compare every new tick against warmup-period price. Reject delta >15¢, log `STALE TICK REJECTED`.
- **Layer 4 — first-tick skip**: drop the very first tick from any new connection (almost always cached snapshot).
- **Layer 5 — staggered startup**: spread connection starts over 1s (not all at same ms).
- **Layer 6 — anti-jitter reaper**: per-connection Jitter EMA; cull most-erratic first. New sockets get 8s grace period. Budget: max 20 respawns/min, max 2/cycle. Culled replicas lose tracking data.

Claimed result: cleaner, faster data than 99% of competitors; single biggest profitability lever.

### Latency targets

- Internal hot path (signal-detect → order-fire): **<0.5ms**
- P50 round-trip to CLOB: **6-8ms** on good infrastructure
- Anything higher → consistently second in line
- Best server locations cited: **Ireland, Montreal** (proximity to Polymarket infra)

### Pre-staging discipline

Hot path should do almost zero work at execution time:
- Pre-build HMAC signatures
- Pre-build headers
- Pre-build request bodies
- Clone-on-fire when window opens

Every millisecond of serialization at entry costs fills.

### Liquidity / order-type tactics

When FAK orders fail in thin books:
- GTC limits at mid+1 tick
- Naked-sell the opposite side
- Pre-split shares + rest GTC on other side as synthetic position

All three "manufacture entries when the order book has nothing for you."

### Silent fill bug (post-V2)

Don't trust only the API exception to confirm a fill. After any timeout:
- Poll the order-status endpoint manually
- Run a **full reconciliation pass every 30 seconds minimum**

### Strategy taxonomy (what actually survives)

Surviving long-term strategies use:
- **CLOB momentum**
- **Spot distance from strike**
- **Time-weighted signals**
- **Day-of-week edges**

Avoid: layered indicator stacks (RSI + MACD + divergence). Every indicator adds a failure surface.

### Window sizing

Start with **15-minute BTC markets**, not 5-minute. 5-min is brutal; same logic on 15-min can print immediately.

### Sizing + risk

- Don't size all-in on single entries — chunk
- Aggressive stop losses on clear losers
- DCA into winners
- Capital preservation > perfect entries

### Why this matters for Cemini

Cemini already has a Polymarket adapter (per K30/K31 work). Specific extraction candidates from this playbook:

1. **6-layer websocket system** — direct architectural lift. Compare against Cemini's current websocket stack (likely simpler than 6 layers).
2. **Latency budget** (<0.5ms hot path, 6-8ms P50 CLOB) — verify Cemini's current measurements against this target.
3. **Pre-staged HMAC** — confirm Cemini's Polymarket client pre-builds signatures rather than serializing per-call.
4. **Reconciliation cadence** (30s full pass) — verify Cemini's reconciliation interval; this is a concrete number to audit against.
5. **Strategy taxonomy** — the four surviving signals (CLOB momentum / spot-from-strike / time-weighted / day-of-week) are direct candidates for `agents/strategies/` modules.
6. **NSF-as-data principle** — every wallet rejection in dry-run is a signal that should re-enter the backtest dataset.

**Verification call**: cross-reference @0x_Punisher's `polymarket.com/@pbot-6` profile against current PnL claims before treating any specific number as authoritative.

### Risks / caveats with the playbook

- Author's TG channel + public profile = self-promotional component. Strategy + architecture is plausible and matches independent knowledge of CLOB microstructure; specific PnL claims need independent verification.
- "99% of bots use simple X" type claims are unverifiable.
- The 6-layer system is described with operational specificity (timing, counts, EMAs) consistent with production experience — most credible part of the playbook.

### Independent corroboration — @bored2boar (May 2026)

A second Polymarket bot operator (@bored2boar, claiming 1,500+ bots built and ~$12.7K/week public PnL) published an independent failure-mode list in `posts.docx`. It was written separately from the @0x_Punisher playbook yet converges on the same lessons — which upgrades several of this page's claims from single-source toward `[CONFIRMED]`:

| @bored2boar failure mode | Matches this page's section |
|---|---|
| "Trading on dirty data" — late/out-of-order ticks, reconnect gaps, stale snapshots; fix is infrastructure (reject abnormal jumps, discard post-reconnect first ticks, parallel feeds, respawn slow connections) | 6-layer websocket system (Layers 1–6) — `[CONFIRMED]` two independent operators |
| "Backtests are fiction" — ignore fill probability, depth, latency, slippage, competition; "70% strategy usually becomes 53–56%" | Backtesting discipline; win-rate-vs-entry-price — `[CONFIRMED]` |
| "Started too complex" — begin with one market / one timeframe / one signal (15-min BTC, one external signal, hold to resolution) | Strategy development cycle; window sizing — `[CONFIRMED]` |
| "Optimizing win rate over profit" — 90% WR at 85–90¢ risks $1 for 5–10¢; compute breakeven WR | Critical rule — win rate vs entry price — `[CONFIRMED]` |
| "Never tested real execution" — run a real (even zero-balance) wallet, let orders fail, feed failures back | NSF-as-data principle; dry-run discipline — `[CONFIRMED]` |
| "Infrastructure too weak" — dedicated low-latency server; FIFO punishes second-in-line | Latency targets — `[CONFIRMED]` |
| "Rushing the process" — manual test → backtest → execution sim → live dry test → deploy | Strategy development cycle — `[CONFIRMED]` |

Net: the @0x_Punisher playbook's *operational principles* are now two-source-confirmed. Specific numbers (latency in ms, exact PnL) remain `[TENTATIVE]` single-source each. @bored2boar adds nothing the @0x_Punisher page lacks at the engineering-detail level (no 6-layer-equivalent spec), so this page stays canonical; @bored2boar is corroboration, not new architecture.

### K64 corroboration — @farxxxxx1 (May 2026)

@sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md adds a third operator narrative: **pre-resolution exits** (91% of top wallets, volume-spike trigger), **don't hold to settlement**, kill sports/low-volume books, consensus filter reduces losers. Synthesized in @concepts/polymarket-wallet-alpha-pipeline.md — complements copy-trading / whale-watch, not a replacement for @0x_Punisher latency stack.

### Independent corroboration — @adiix_official (May 2026)

A *third* operator (@adiix_official, K52 `posts.docx` Post 6) published "Why your Claude bot doesn't work" — a follow-up to a 12M-view part-1 article — diagnosing why reader-built Polymarket **latency-arbitrage** bots fail. Its bot class is @0x_Punisher's "Type 1": a Binance WebSocket BTC/ETH ticker feed driving Polymarket 5/15-min crypto contracts. It converges on the same discipline yet once again adds no engineering detail this page lacks — corroboration, not new architecture:

| @adiix_official guidance | Matches this page |
|---|---|
| Paper-mode-first; go-live gate = ≥200 paper trades, >75% paper win rate, ≥7 crash-free days | Backtesting discipline; dry-run discipline — `[CONFIRMED]` three operators |
| Credentials only from a `.env` (python-dotenv); never hardcode; `.env` in `.gitignore` | Pre-staging discipline / opsec — corroborated |
| Reject price data older than 10s as stale; pause trading on stale data; WS auto-reconnect with exponential backoff | Layer 3 stale-tick guard; Layer 1 quality gate — `[CONFIRMED]` |
| Deploy to a \$5/mo VPS before live; laptop is not a deploy target | Latency targets / dedicated infra — `[CONFIRMED]` |
| Half-Kelly sizing, hard 8%-of-portfolio cap, recalc portfolio before every trade | Sizing + risk (chunk, don't all-in) — corroborated |
| Risk halts: daily −20% P&L halt, permanent halt below 60% of all-time high, 30-min pause after 5 losses | Stop losses + risk controls — `[CONFIRMED]`, with concrete thresholds |

The genuinely new artifact in Post 6 is a **"battle-tested" Claude prompt** — a full production-bot spec (credentials / price-monitoring / edge-detection / position-sizing / risk-management / execution / monitoring / paper-mode blocks). It is a reusable scaffold for *generating* a Type-1 bot, not a new architecture; captured as a Snippet below. Post 6 also restates that **Polymarket is geo-blocked to US residents** — independent confirmation of the Cemini geo-routing findings (see `@concepts/cemini-deployment.md`). The 9-mistake list the article advertises did not survive the `.docx`→text extraction (embedded image/table); the prompt and setup checklist did.

## Snippets

> Latency is killing you before strategy even matters. Measure every single step from signal detection to order fire. Target under 0.5ms on your internal hot path. P50 round trip to CLOB should sit around 6-8ms on good infrastructure.

> Silent fill bug is destroying your state management post-V2. Never trust only the API exception to confirm a fill. After any timeout - poll the order status endpoint manually. Run a full reconciliation pass every 30 seconds minimum.

> The bots that survive long term use: CLOB momentum, spot distance from strike, time-weighted signals and day of week edges. That is it. Nothing else needed.

### @adiix_official "battle-tested" Type-1 bot prompt (K52, Post 6)

A full production-bot spec the article supplies as a copy-paste Claude prompt. Reproduced condensed as a scaffold reference — *not* a Cemini adoption (Cemini's adapter already exists; this is the requirement checklist a from-scratch Type-1 bot should satisfy):

> **Credentials** — load all keys from `.env` via python-dotenv, never hardcode; required vars `POLY_API_KEY`, `POLY_PRIVATE_KEY`, `TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID`, `ALCHEMY_RPC_URL`.
> **Price monitoring** — Binance WS `wss://stream.binance.com:9443`, BTC/USDT + ETH/USDT tickers; auto-reconnect exponential backoff (max 10 retries); reject price data >10s old as stale; pause trading on stale data.
> **Edge detection** — min detectable edge 5%, min execution edge 8%; only BTC/ETH 5-min & 15-min contracts; min market liquidity \$50k; max 20 markets monitored.
> **Position sizing** — half-Kelly per position; hard cap 8% of portfolio per trade; recalc portfolio value before every trade.
> **Risk management** — daily halt if P&L < −20% of day-start; permanent halt if portfolio < 60% of all-time high; 30-min pause after 5 consecutive losses; all halts → Telegram alert + manual restart.
> **Execution** — full async (asyncio + aiohttp, no blocking calls); Alchemy RPC for Polygon; <800ms detection-to-order target.
> **Monitoring** — Telegram alert on every entry/exit/error/kill-switch; hourly heartbeat (balance, trades, win rate); rotating 50MB log.
> **Paper mode** — default; three explicit flags to enable live (`--live --confirm --i-understand-risks`); paper trades logged to SQLite.
> [Source: posts-2026-05-18.docx — Post 6, @adiix_official]

## Dead Ends

- RSI + MACD + divergence-layer stacks — author explicitly flags as load-bearing failure pattern across the 1000+ bots he's seen break.
- 5-minute BTC windows for beginners — too noisy; author recommends 15-min as starting point.
- Trusting public PnL profiles without on-chain verification — author flags that competitor "magic 0¢-100% wallets" are usually Polymarket's NegRisk contract infrastructure, not real bots.
