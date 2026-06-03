---
title: "@RohOnChain — Trade FIFA World Cup like a quant (shock-recovery strategy)"
type: source
tags: [source, trading-posts, polymarket, world-cup-2026, shock-trading, in-play, microstructure, k94]
keywords: [rohonchain, shock-detection, five-dimension-classifier, laddered-limits, dome-api, percentile-depth, football-lp]
related:
  - entities/people/rohonchain.md
  - concepts/polymarket-football-shock-recovery-trading.md
  - concepts/polymarket-sports-microstructure-bot-taxonomy.md
  - concepts/world-cup-advance-market-bot-v1.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - entities/tools/world-cup-bot.md
  - entities/tools/pmxt.md
  - concepts/time-series-arima-garch-framework.md
  - projects/world-cup-bot/Architecture/Architecture - match_shock_v1.md
  - projects/world-cup-bot/Architecture/Architecture - match_shock_pmxt_backtest.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
  - sources/trading-posts-compilation-17-2026-06-03.md
maturity: validated
created: 2026-06-02
updated: 2026-06-03
---

## Relations

- @entities/people/rohonchain.md — author (Roan, @RohOnChain); fourth major quant-framework post after Markov / NN / time-series
- @concepts/polymarket-football-shock-recovery-trading.md — synthesized strategy concept
- @concepts/polymarket-sports-microstructure-bot-taxonomy.md — maps to live shock / stale-probability family
- @entities/tools/world-cup-bot.md — **orthogonal** to v1 advance LP; see WC-bot fit section on concept page
- @sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md — DR 09 hard_halt on in-play LP contradicts this strategy's core execution mode

## Raw Concept

| Field | Value |
|-------|-------|
| Title | How To Trade FIFA Like A Quant on Polymarket (Complete Strategy) |
| Author | Roan (@RohOnChain) |
| Type | X / long-form article (user paste) |
| Location | `research to be indexed/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md` → librarian after ingest |
| Retrieved | 2026-06-02 |
| Read status | deep-read |
| Companion | Author's prior "Math Needed for Trading on Polymarket" article (3M views claim — unverified) |
| Code | GitHub repo offered via DM/comments — **not received** in this ingest |

## Narrative

Long-form strategy post timed **nine days before WC 2026 kickoff (2026-06-11)**. Thesis: football match markets on Polymarket produce **repeatable overreaction shocks** (goals, cards, penalties) that partially recover; edge is **liquidity provision into panic**, not outcome prediction.

### Shock detection (live)

Sliding **2-minute** window. Shock fires when:

- Drop ≥ **15%** from window peak to floor
- Absolute drop ≥ **8¢** (noise filter at low prices)
- **3-minute cooldown** between shocks (no double-count)

### Five-dimension classifier → bucket key

Each shock classified independently; combined into a string key (~720 combos, ~200 with enough history):

| Dim | Buckets | Signal |
|-----|---------|--------|
| **League tier** | deep / thin / unknown | Slug-based (EPL, UCL, La Liga = deep) |
| **Favoritism** | heavy_fav (≥85¢) / moderate_fav (75–85) / slight (60–75) / balanced (45–60) / underdog (<45) | Pre-shock price |
| **Book depth** | top_heavy (≥70% in top 3 bids) / balanced / deep | Top-3 bid size ÷ total bids |
| **Match time** | early (0–15m) / mid (15–60) / late (60–80) / final (>80) | Elapsed ms |
| **Goal state** | level / one / two / blowout (≥3) | Absolute goal diff |

Example key: `deep|underdog|balanced|mid|level`

### Historical distribution engine

- Record **shock depth** = pre-shock price − floor (cents)
- Per bucket: sorted depths → **P50, P75, P90, P95** (linear interpolation)
- **&lt;5 historical shocks** in bucket → conservative defaults (6/9/13/18¢) — do not trade thin buckets aggressively

### Laddered entry + exit

Four limit buys at `pre_price − percentile_depth`:

| Percentile | Capital weight |
|------------|----------------|
| P50 | 10% |
| P75 | 20% |
| P90 | 30% |
| P95 | 40% |

Orders live **60s**. Exit: fixed **~4¢ recovery** target (sell into bounce).

Author claims **moderate_fav (75–85¢)** buckets backtest best; recommends filtering buckets and percentile bands before live.

### Data layer — Dome API

Author recommends **Dome** unified PM/Kalshi API for historical order book + trade history for backtest distribution build. Polymarket **acquired Dome 2026-02-19** [CONFIRMED — crypto.news, YC Fall 2025 cohort]. Free tier cited. Cemini already has **pmxt** 1TB orderbook dataset (@entities/tools/pmxt.md) as alternative data path.

### Bot architecture (author)

1. Data ingestion (Dome)
2. Distribution builder (bucket percentiles)
3. Live shock detector
4. Execution (laddered limits)

Repo **not public in paste** — DM-gated.

### Marketing / credibility flags

- "Insane" backtest results — unverified without repo
- "Win consistent trades" — same hyperbolic framing as prior Markov/time-series posts (wiki strips this)
- WC winner market **$1.4B** volume, **327 active WC markets** — plausible order of magnitude [TENTATIVE]
- Tournament = largest PM stress test — qualitative claim, directionally credible

### WC Bot fit (summary)

| WC Bot v1 (advance LP) | Roan shock strategy |
|------------------------|---------------------|
| `advance to knockout` markets | **Match win / in-play** markets |
| Pregame T-24h → T-10h quote window | **Live** during goals |
| `hard_halt` in-play (DR 09) | **Requires** in-play posting |
| Conviction YAML team selection | Statistical bucket lookup |
| Reward farming + exit before resolution | Scalping 4¢ recovery |

**Verdict:** Does **not** plug into WC Bot v1. Useful as **separate v2 module** or **private fork** on match markets; reinforces why advance LP must **cancel before kickoff** (Roan's shocks are the adverse-selection event DR 09 warns about).

## Snippets

> "The strategy does not predict goals. It waits for a shock to happen, then enters at a mathematically determined depth, and captures the statistical recovery." [Source: rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md]

> "A bucket with 3 shocks is not a distribution. It is noise." [Source: rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md]

```python
def detect_shock(window_trades):
    peak = max(t.price for t in window_trades)
    floor = min(t.price for t in window_trades)
    drop_pct = (peak - floor) / peak
    drop_abs = peak - floor
    if drop_pct >= 0.15 and drop_abs >= 0.08:
        return {"shock": True, "peak": peak, "floor": floor, "depth": peak - floor}
    return {"shock": False}
```

```python
def bucket_key(shock):
    return f"{classify_league(shock.slug)}|{classify_favoritism(shock.pre_price)}|{classify_depth(shock.bids)}|{classify_time(shock.elapsed_ms)}|{classify_goal(shock.goal_diff)}"
```

> "During the World Cup, with billions in fresh volume and thousands of new traders flooding in, will those overreactions get larger because of all the inexperienced money, or will they get smaller because of all the new liquidity?" [Source: rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md — open sizing question for tournament]
