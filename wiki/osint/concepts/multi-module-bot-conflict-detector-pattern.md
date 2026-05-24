---
title: "Multi-module bot conflict-detector pattern — skip on internal disagreement"
type: concept
tags: [concept, trading-bot, polymarket, multi-signal-synthesis, conflict-detection, risk-management, broken-data, k55]
keywords: [conflict-detector, signal-spread-threshold, multi-module-synthesis, polymarket-btc-5min, phantom-win, broken-data-corruption, time-aware-sizing, chainlink-data-streams, gustafssonkotte, three-question-architecture]
related:
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/algorithmic-stopping-conditions.md
  - entities/people/gustafssonkotte.md
  - entities/tools/chainlink-data-streams.md
  - entities/platforms/polymarket.md
  - concepts/polymarket-three-quadrant-blacklist-microtrend.md
  - concepts/polymarket-btc-already-position-gate.md
  - sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md
maturity: validated
created: 2026-05-20
updated: 2026-05-24
clusters: [polymarket, bot-architecture, risk-management]
---

## Relations

- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — Post 3 (@Gustafssonkotte) primary source
- @concepts/polymarket-bot-architecture.md — third independent operator (after @0x_Punisher, @adiix_official) corroborating the broader bot-discipline lessons; conflict-detector is a structural addition
- @concepts/polymarket-updown-bot-taxonomy.md — applies to short-resolution UpDown markets specifically (5-min BTC bots)
- @concepts/algorithmic-stopping-conditions.md — the conflict-detector is a stopping condition fired on internal disagreement
- @entities/people/gustafssonkotte.md — author
- @entities/tools/chainlink-data-streams.md — price feed used; explicitly bypasses the exchange API the bot trades against
- @concepts/polymarket-three-quadrant-blacklist-microtrend.md — K57 follow-on (blacklist + micro-trend)
- @concepts/polymarket-btc-already-position-gate.md — K62 replaces direction vote with position-already gate
- @sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md — K62 source

## Raw Concept

What prompted this page: K55 Posts 2.docx Post 3 — @Gustafssonkotte's "Deleted half my bot's code and it started winning." Documents two distinct lessons: (i) silent-bug-driven broken-data corruption pattern, and (ii) the multi-module conflict-detector architectural fix. The combination took a Polymarket 5-minute BTC bot from 41% WR (negative P&L) to 60% WR (positive P&L) on day-1 of the rewrite.

## Narrative

### The story (compressed)

Operator was running a Polymarket BTC 5-min Up/Down bot with `WR=41%` over 17 trades, P&L creeping down. Decision was made to audit before adding "more indicators."

The audit found **three silent bugs that had been corrupting weeks of stats**:

1. **Voter→entry tier-field drop**: voter outputs "top signal, max size" but the tier field was being lost in the handoff between voter and order-placement. Every "confident" entry was actually sized at the minimum.
2. **Drawdown limit was a no-op**: when triggered, the code wrote "PAUSED" to the log in red and **returned success** in the risk check. Bot kept trading.
3. **Order-confirm fail-safe wrote phantom WINs**: "if order doesn't confirm in N seconds, assume it filled." Half the recorded wins never opened on the exchange.

After fixing the bugs and re-examining the *clean* data, WR was **worse than a coin flip**. The brain itself was broken.

The fix wasn't more indicators. The fix was deleting half the codebase and adding **one** new check: a conflict-detector.

### Part 1 — the broken-data lesson (the deeper of the two)

> The bot wasn't losing because it was bad. The bot was losing because I was listening to its broken brain. Every loss was a signal. I was averaging them into an "entry." The hard part wasn't writing new indicators. The hard part was deleting the old ones that pretended to work.

The pattern: a trading bot's failure mode is rarely "the strategy is wrong." It's almost always **data integrity is wrong** — phantom fills, dropped tier fields, defenses that report success while doing nothing. The bot then makes decisions on data that doesn't match reality, and no amount of strategy tuning fixes that.

**Diagnostic pattern**: when WR is below coin-flip on supposedly-confident trades, the question is not "is the strategy broken?" It is **"what is my evidence that the data I'm scoring against is real?"**

Concrete rules from the post:
- **Source-of-truth = exchange exports**, never the bot's internal counter. The internal counter at the time of writing still wasn't fully cleaned of the phantom-WIN legacy.
- **Add real-balance checks before AND after each order**. The fail-safe should return "nothing happened" on timeout, not "WIN."
- **All "defense in depth" gates** (drawdown limits, daily loss caps, hour windows) must actually be tested. A defense that returns success on its own failure is worse than no defense.

This is independent corroboration of the same lesson the @0x_Punisher / @adiix_official / @bored2boar Polymarket-bot writers all stated independently: **execution infrastructure dominates strategy** for any production bot. Recorded as a fourth-operator corroboration on `@concepts/polymarket-bot-architecture.md`.

### Part 2 — the conflict-detector architectural pattern

After bug fixes, the strategy itself needed rebuilding. The old architecture was a **single weighted vote across indicators**:

```
indicators → weighted sum → category lookup → "fair probability" → edge formula → enter
```

Three structural failures:
- The "probability" was a **lookup table**, not a real probability. WR-by-category on clean data: top 0/1, mid 1/2, weak 2/4, parse-misses 4/8 — parse-misses outperformed "top tier." Numbers had been picked 6 months earlier with no connection to outcome frequencies.
- The **edge formula's sign was inverted**: low confidence → 57% WR, mid → 20%, high → 0%. The more confident the model, the worse it performed.
- **Indicators were averaged when they disagreed**: trend up + momentum down + levels silent → small positive sum → "enter." An average of contradictions.

**The replacement** — three modules, three questions, one synthesizer:

```
Q1: Where is the price going?
    inputs: MTF trends, EMA(5m) cross, EMA50/200 filter, VWAP deviation
    output: (p_trend, s_trend) where p ∈ [0,1] probability up, s ∈ [0,1] strength

Q2: Where are the magnets and barriers?
    inputs: structural highs/lows, liquidity sweeps, multi-exchange order walls (Binance/Bybit/OKX/Coinbase), anti-spoof filter
    output: (p_level, s_level)

Q3: Is momentum for or against?
    inputs: RSI (two periods), Bollinger Bands (squeeze + breakout), Parabolic SAR, Fair Value Gap, orderbook pressure
    output: (p_momentum, s_momentum)
```

Each module combines its internal sources to one probability + one strength. The synthesizer then computes:

```python
confidence = weighted_average(p_trend, p_level, p_momentum)
strength   = average(s_trend, s_level, s_momentum)
spread     = max(p_trend, p_level, p_momentum) - min(p_trend, p_level, p_momentum)

if spread > THRESHOLD:
    return SKIP("internal_conflict")
```

**The conflict-detector filter is the architectural insight**: when three independent answers disagree by more than a threshold, the system **does not enter**. This is *not* a new feature — it *removes* false entries the system should never have been making.

**Worked example from the source's logs**:
```
Q1 TREND:    p_up=0.76  S=0.51
Q2 LEVELS:   p_up=0.67  S=0.34
Q3 MOMENTUM: p_up=0.10  S=0.80   (RSI overbought, waiting for pullback)
SKIP: internal_conflict, spread=0.66
```
The old single-vote system would have averaged the votes (positive net) and entered long. The new system sees the 0.66 spread between trend (0.76) and momentum (0.10) and passes. This is the kind of trade that was destroying the old bot's WR.

### Part 3 — time-aware sizing on short-resolution markets

Structural observation specific to 5-minute Polymarket UpDown markets: **the last 90 seconds are statistically more predictable than the first 3 minutes**. Price has already chosen direction by then. Position size scales:

```python
def time_factor(mins_left):
    if mins_left >= 4.0:  return 0.7    # early, noisy
    if mins_left >= 3.0:  return 0.85
    if mins_left >= 2.0:  return 1.0
    if mins_left >= 1.0:  return 1.2
    return 1.3                          # late, sharper

size = base * confidence * (1 - spread) * strength * time_factor
```

`size = base × confidence × (1 − spread) × strength × time_factor` is the final formula. Each factor reduces size on a different kind of uncertainty:
- `confidence` < 0.5 → size near zero (weak signal)
- `(1 − spread)` → size shrinks as modules disagree
- `strength` < 0.5 → size shrinks when no module is confident
- `time_factor` < 1 → size shrinks early in the candle

Generalizes beyond 5-minute markets: any short-resolution UpDown market has a structural "noise window → settling window" arc; the late-window predictability premium is real.

### Part 4 — protections in firing order

```
1. Trading hours.       Outside working hours, entries blocked.
2. Weekend block.       Saturday/Sunday fully off.
3. Loss streak.         3 losses → short pause.
4. Drawdown limit.      Sharp balance drop → stop.
5. Daily loss limit.    Daily loss cap → stop until tomorrow.
6. Internal conflict.   Spread > threshold → skip.
7. Low confidence.      Weak overall confidence → skip.
8. Low strength.        Weak overall signal → skip.
```

The hours-block and weekend-block are interesting structural choices: **bot doesn't shut down outside hours, it just blocks entries**. WebSocket feeds keep accumulating, candles keep building, walls keep being tracked. Monday morning the bot starts with full weekend history. This pattern — accumulate state continuously, gate the action stage — is generally applicable.

### Performance — single-day datapoint

| Phase | Trades | WR | Direction-correct | P&L |
|---|---|---|---|---|
| Old (2 weeks, broken data) | 17 | 41% | 47% | red |
| v4 (day 1, clean data + new brain) | 33 | 60% | 60% (UP 61% / DOWN 58%) | green |

[TENTATIVE — single-day post-rewrite sample; author's stated goal is 70% over the next 100+ trades.] The interesting feature isn't the WR number — it's the **symmetry restored between UP and DOWN sides** (61% / 58%). The old bot had longed a falling market 7 times in a row → systematic skew, broken brain.

### Stack used

- Python
- **Chainlink Data Streams for BTC price feed** — explicit choice to bypass exchange APIs (no exchange API in the BTC-pricing path). The bot's execution venue (Polymarket CLOB) is independent of the price-truth source.
- Polymarket CLOB for execution
- Multi-exchange WebSocket orderbook feeds (Binance, Bybit, OKX, Coinbase) for the Q2 levels-and-walls module
- Ubuntu VPS

### Cemini fit

**High-fit lift candidates** for the Cemini Polymarket stack:

1. **Conflict-detector filter** — universal pattern. Any multi-signal Cemini strategy (UpDown bot, sports-consensus agent, GARCH-vs-Markov regime-cross-check) can use the `spread > threshold → SKIP` pattern.
2. **Multi-exchange price-feed oracle separate from the trading venue** — already done in spirit (Chainlink → execution-on-Polymarket); document the pattern, recommend explicitly.
3. **Time-aware sizing on short-resolution Polymarket markets** — directly applicable to the UpDown bot taxonomy already documented.
4. **Polymarket exports as source-of-truth for stats** (never the bot's internal counter) — already implicit in the @0x_Punisher playbook; reinforce as an explicit rule.

### Generalization beyond 5-min BTC

The conflict-detector pattern is **domain-agnostic**:
- Sports consensus agent (this batch, separate concept): "consensus_strength" already does the same job (5 sources at 0.78 strength) — that's the same idea named differently.
- GARCH-vs-Markov regime check (this batch): "if both forecast vol-up → cut exposure aggressively; if disagree → reduce sizing pending more data" — same pattern at the regime layer.
- Any future multi-model orchestration: cross-validate; SKIP on disagreement.

Recorded as a Cemini-wide **multi-model orchestration pattern**, not just a 5-min UpDown bot trick.

## Snippets

> "Three silent bugs were corrupting data for weeks. I was looking at 41% WR and thinking my brain was bad. The brain was fine. It was just making decisions on broken data." [Source: Posts 2.docx — Post 3, @Gustafssonkotte]

> "The 'probability' table wasn't a probability, it was a lookup table. The numbers were picked at random six months ago. Zero connection to real outcome frequencies." [Source: Posts 2.docx — Post 3, @Gustafssonkotte]

> "If the spread is too large, the modules are disagreeing too much. Don't trade. ... The conflict filter doesn't add new logic. It removes false entries the system should never have been making. It's not an improvement. It's a fix." [Source: Posts 2.docx — Post 3, @Gustafssonkotte]

> "Source of truth: Polymarket exports, not the bot's internal counter. The internal counter isn't fully cleaned of the phantom WIN legacy." [Source: Posts 2.docx — Post 3, @Gustafssonkotte]

> "The bot wasn't losing because it was bad. The bot was losing because I was listening to its broken brain. Every loss was a signal. I was averaging them into an 'entry'. The hard part wasn't writing new indicators. The hard part was deleting the old ones that pretended to work." [Source: Posts 2.docx — Post 3, @Gustafssonkotte]
