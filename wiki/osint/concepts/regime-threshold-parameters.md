---
title: "Regime watch thresholds — reproducible parameter contract (alert-only)"
type: concept
tags: [concept, trading, regime, mean-reversion, momentum, circuit-breaker, guruwatcher, alert-only]
keywords: [regime watch, rsi threshold, momentum lookback, mean reversion z-score, circuit breaker, threshold contract, reproducible parameter]
related:
  - entities/tools/quants-md.md
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Relations

- @entities/tools/quants-md.md — catalog that triggered this page; pattern only, licence unresolved
- @sources/eval-multi-wiki-link-revenue-v10.10-batch-a-2026-11-01.md — URL 6, Extract tier

## Raw Concept

The question this page answers: **when a watch says "flag when RSI crosses X", where is X defined, and how do two operators get the same answer from the same newsletter?**

`quants.md` carries explicit definitions for mean-reversion and momentum regime watches, and a monthly circuit-breaker sizing rule. This page takes the threshold **definitions** only. It does not take the strategy parameters, and it does not take the order state machines.

GuruWatcher stays alert-only. A threshold here produces an alert. It never produces an order, a size, or a signed transaction.

## Narrative

### What this page fixes

A threshold that lives in a prompt is not reproducible. The same text can yield a different level on a different day, and no reader can check the number against a source.

So a regime watch must declare its parameters in a fixed form. The form below is the contract. The values are separate, and each value must name its source.

### The parameter contract

Every regime watch declares these fields. Empty is a valid state. A guessed value is not.

| Field | Meaning | Example form |
|-------|---------|--------------|
| `instrument` | Named instrument, as printed in the source | `VIX` |
| `series` | Input series the indicator reads | `daily close` |
| `indicator` | Named indicator and its lookback | `RSI(14)` |
| `op` | Comparison operator | `cross_above`, `lt`, `gt` |
| `threshold` | The value the comparison uses | `70` |
| `sustain` | Consecutive closed bars required before an alert | `2` |
| `source` | Page, file, and offset that state the threshold | `issue 2026-10-25, chars 812–860` |
| `date` | Source publication date | `2026-10-25` |

Two watches that declare the same eight fields are the same watch. A watch with an empty `source` does not arm.

### Definition 1 — mean reversion

Mean reversion treats a large departure from an average as a temporary condition.

| Item | Definition |
|------|------------|
| Measure | Distance from the average, in units of standard deviation (z-score). |
| Formula | `z = (close − SMA(n)) / stdev(close, n)` |
| Input | Daily close of the declared series. |
| Trigger | `z` at or beyond the declared band, in either direction, unless the watch states one side. |
| Sustain | The declared count of consecutive closed bars. |

The band is the threshold. It is not fixed by this page.

### Definition 2 — momentum

Momentum treats a sustained move in one direction as likely to continue.

| Item | Definition |
|------|------------|
| Measure | Rate of change over a lookback, or an oscillator that normalises it to a fixed range. |
| Formula (rate of change) | `roc = close / close[n] − 1` |
| Formula (RSI form) | `rsi = 100 − 100 / (1 + average_gain / average_loss)` over the declared lookback |
| Input | Daily close of the declared series. |
| Trigger | The declared operator against the declared threshold. |
| Sustain | The declared count of consecutive closed bars. |

RSI is stated here because a watch names it. The lookback and the crossing level are still the watch's own fields.

### Definition 3 — monthly circuit breaker (documented, not deployed)

The catalog carries a monthly circuit-breaker **sizing** rule: a drawdown gate that reduces exposure after a losing month.

This rule sizes a position. GuruWatcher has no position. **Do not implement this rule in GuruWatcher.** It is recorded here for completeness and it belongs to `xsp-killer`, which is the system that holds order state.

The only GuruWatcher-legal form of this idea is a **drawdown alert**: report that the drawdown gate would fire. Report the number. Take no action.

### What a threshold value must carry

A threshold value enters a watch only when all of these are true:

1. A named source states it. A source is a page, a file, and a character offset.
2. The value is the literal text of that source. The exact-quote invariant applies: `text[start:end] == value`.
3. The operator and the sustain count are stated in the same source, or are marked as operator-set.
4. The value is inside the instrument's declared level band.

A value that fails any line stays empty. The watch holds.

### Status and limits

**Not sourced.** The report that surfaced `quants.md` did not reach the catalog. It records no repository URL and no licence, and it states "NEEDS VERIFICATION" for both. The specific numeric parameters in the catalog are therefore **not available to this page**, and this page does not invent them.

What this page can do without the catalog is fix the **contract**: the eight fields, the two indicator formulas, and the rule that a value must trace to a source. That is enough for two operators to agree, and it is enough to reject a watch that carries an unsourced number.

When the catalog is reachable, add a values table here. Do not copy code. The licence is unresolved.

## Snippets

> "Extract the walk-forward validation harness and order/sizing mechanics rather than deploying raw ETF parameters on XSP." — report, URL 6

> "Many baseline ETF strategies in the catalog post negative or sub-0.5 Sharpe ratios." — report, URL 6

## Dead Ends

- **Deploying the catalog's ETF parameters.** Most sit below 0.5 Sharpe by the report's own numbers.
- **Putting bracket, stop-limit, or trailing stop-limit state machines into GuruWatcher.** They belong to `xsp-killer`. GuruWatcher is alert-only.
- **Writing a threshold from memory.** An unsourced number is an invented number. Leave the field empty and hold the watch.
- **Copying catalog code.** No repository URL and no licence were found. Re-implement from the description only.
