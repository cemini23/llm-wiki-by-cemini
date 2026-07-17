---
title: "Polymarket LP rewards — comprehensive backtest architecture (v2)"
type: concept
tags: [concept, polymarket, lp-rewards, backtest, markout, q-score, k171]
keywords: [pm-lp-backtest, q-min, reward-proxy, trade-tape, adverse-selection, one-dollar-floor, canary-calibration]
related:
  - meta/pm-lp-backtest-cadence.md
  - concepts/cemini-backtest-report-kit.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/cemini-pm-lp-vs-copy-capital-decision.md
  - concepts/lp-algorithm-live-promotion-gates.md
  - entities/tools/polymarket-quotebot.md
  - entities/tools/yieldpilot.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/oddpool.md
maturity: draft
created: 2026-07-16
updated: 2026-07-16
clusters: [polymarket, market-making, backtesting]
---

## Relations

- @meta/pm-lp-backtest-cadence.md — quarterly ritual; v1 proxy vs this v2 target
- @concepts/cemini-backtest-report-kit.md — HTML sweep report shell
- @concepts/polymarket-lp-bot-phase0-spec.md — Phase-0 bot design this backtest must validate
- @concepts/polymarket-lp-rewards-farming.md — strategy + scoring narrative
- @concepts/cemini-pm-lp-vs-copy-capital-decision.md — empirical kill + restart gates
- @concepts/lp-algorithm-live-promotion-gates.md — DSR / MCPT / markout promotion stack
- @entities/tools/polymarket-quotebot.md — best external measurement-rig steal-from
- @entities/tools/yieldpilot.md — maxSpread-fraction quoting heuristic
- @entities/tools/polymarket-clob-api.md · @entities/tools/polymarket-gamma-api.md — data plane
- @entities/tools/oddpool.md — low-competition filter class for selective LP

## Raw Concept

Federation research (2026-07-16) across OSINT wiki, CeminiSuite, prod `/opt/cemini`, gambling/CCC wikis, GitHub, and Polymarket docs. Goal: specify a **comprehensive** LP-rewards backtest that can gate capital restart — replacing the 2026-05-27 laptop **reward-proxy** pilot.

## Narrative

### Why v1 is insufficient

| Artifact | What it does | Failure mode |
|----------|--------------|--------------|
| Laptop `scripts/pm_lp_backtest/` (2026-05-27) | Hourly mid ± `spread_cents`; PnL = `reward_scale` proxy − mid-crossing adverse | Not Polymarket \(Q\)-score; no competition share; no tape/queue |
| Prod `logs/pm_backtests/pm-lp-{7,30}d.json` (2026-05-31) | UI paper cards via `pm_backtest_refresh` | **Empty** — 0 trades, $0 rewards |
| Live sleeve accountant | Shadow canary + markout kills (K166) | Ops telemetry, not historical sim |

Cemini attributed LP PnL remains ~**+$0.94** / ~23 events; sleeve **KILLED** 2026-06-13. Retail anecdotes ($50→$18) are **not** Cemini evidence.

### Official scoring (CLOB / docs) [CONFIRMED]

From [Polymarket Liquidity Rewards docs](https://docs.polymarket.com/market-makers/liquidity-rewards) (retrieved 2026-07-16):

- Order score: \(S(v,s) = ((v-s)/v)^2 \cdot b\) with \(v\) = max incentive spread, \(s\) = distance from size-cutoff-adjusted mid, \(b\) = size.
- Two-sided boost via \(Q_{\min}\); one-sided in mid∈[0.10,0.90] divided by \(c=3\); extreme mids require two-sided.
- Daily share = trader \(Q\) / market total; payout only if day ≥ **$1**.
- Per-market `max_spread` / `min_size` from CLOB metadata.

**Do not** mix Polymarket US discount-factor incentive formula into CLOB global scoring.

### Target equation

```
net_yield = reward_share_usd + captured_spread − adverse_selection_markout
```

Every backtest row must expose these three terms separately (promotion gates need markout ladders).

### Architecture (phases)

| Phase | Deliverable | Acceptance |
|-------|-------------|------------|
| **A** | This concept + prod brief | Operator GO (done 2026-07-16) |
| **B** | Q_min engine using CLOB `max_spread`/`min_size` + daily pool | Matches docs formula on ≥3 reward markets |
| **C** | Trade-tape fill model + 30m (and 1–5s if WS) markout | Report columns: rewards, spread, adverse, net |
| **D** | Sweep: spread × capital ($200/$500/$2k) × horizon × competition | $1/day clearance table |
| **E** | Calibrate paper sim vs 7d K166 canary accountant | Calibration constant pinned; **no** `PM_LP_LIVE_POST` |

### Steal-from

1. **polymarket-quotebot** — Q-share vs real book; fills only when tape crosses *through* quote; 30m markout; paper-first.
2. **YieldPilot** — quote at ~40% of `maxSpread` as default farm distance.
3. **Oddpool-class** filters — avoid crowded books when sizing for $1/day.
4. **himyeticapital/polymarket-lp-bot** (Reddit + GitHub) — auto-close on fill vs “Didi Flip” opposite-side BUY; retail confirmation that directional inventory kills LP PnL.
5. Existing Cemini: `pm_lp_reward_rebaseline.py`, markout kills, promotion gates, report kit HTML shell.

### Social pass (opencli — 2026-07-16)

Used **agent-reach / OpenCLI** (`twitter` + `reddit` backends). Loose “LP rewards” queries are DeFi spam; require `Polymarket` in query.

| Signal | Source | Backtest implication |
|--------|--------|----------------------|
| LP rewards ≪ adverse inventory | Reddit `himyeticapital` post; X `@Celesweb3` | v2 must net **rewards − adverse**; auto-close cost as fill model |
| Q-score + `rewards_min_size` + extreme-mid two-sided | Same Reddit technical block | Matches docs — already Phase B |
| `$1M` WC LP program through **Jul 19** | X `@gawronkuba` | Aligns with K165 “post–Jul-19 re-baseline” |
| Retail claims $7k / $20k / $3k LP | X `@ZP_12_`, `@0x_Punisher`, `@mfardecrouz` | Anecdotes — **not** Cemini evidence |
| Payout projection is hard / opaque | X `@TTx0x` | Calibration Phase E is first-class |
| Unusual wide `max_spread` niches | X `@DextersSolab` | Sweep should include odd-parameter markets |
| `@polybacktest` | X | **Up/Down** directional backtester — **not** LP rewards sim |
| Mid-price fills in backtests are fake | X `@Poly_Historical` | Phase C tape-through / queue model mandatory |
| Sub-second sell after fill | X `@herman_m8` bot thread | Auto-close latency as adverse parameter |
| Repo list: `polymarket_lp_tool`, `prediction-market-backtesting` | Reddit r/PredictionsMarkets | Steal-from for LP tooling / general PM backtest — evaluate separately |

**No** high-quality public thread described a full historical LP Q-score + markout backtest matching Cemini v2 — social validates risk model, not a ready simulator.

### Hard non-goals

- Flipping `pivot_posture.yaml` or `PM_LP_LIVE_POST=true`
- Treating May 2027 proxy Sharpe as live edge
- Blind copy / Telegram key bots

### Data plane

- **Public:** Gamma markets + CLOB `prices-history` + book snapshots + trade tape + rewards metadata.
- **Prod (read-only calibrate):** daily report, markout state, accountant net — never secrets in wiki/briefs.

## Snippets

> "The pilot SHALL state that LP reward accrual is a **proxy model**, not Polymarket’s on-chain scoring formula." — OpenSpec `pm-lp-backtest-pilot` (v1)

> net yield = rewards + captured spread − adverse selection — polymarket-quotebot README (2026-07-15)
