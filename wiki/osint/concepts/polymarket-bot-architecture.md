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
maturity: draft
created: 2026-05-12
updated: 2026-05-13
---

## Relations

- `@sources/x-polymarket-bot-playbook-punisher-2026-05.md` — original X thread + long-form article
- `@entities/platforms/polymarket.md` — platform entity page (create stub if absent)
- `@concepts/cemini-license-posture.md` — IP-sale-readiness frame (no license issue here; pattern, not code)

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

## Snippets

> Latency is killing you before strategy even matters. Measure every single step from signal detection to order fire. Target under 0.5ms on your internal hot path. P50 round trip to CLOB should sit around 6-8ms on good infrastructure.

> Silent fill bug is destroying your state management post-V2. Never trust only the API exception to confirm a fill. After any timeout - poll the order status endpoint manually. Run a full reconciliation pass every 30 seconds minimum.

> The bots that survive long term use: CLOB momentum, spot distance from strike, time-weighted signals and day of week edges. That is it. Nothing else needed.

## Dead Ends

- RSI + MACD + divergence-layer stacks — author explicitly flags as load-bearing failure pattern across the 1000+ bots he's seen break.
- 5-minute BTC windows for beginners — too noisy; author recommends 15-min as starting point.
- Trusting public PnL profiles without on-chain verification — author flags that competitor "magic 0¢-100% wallets" are usually Polymarket's NegRisk contract infrastructure, not real bots.
