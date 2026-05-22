---
title: "Polymarket three-quadrant brain, pattern blacklist, and micro-trend override"
type: concept
tags: [concept, polymarket, btc-updown, bot-architecture, blacklist, microstructure, k57]
keywords: [three-quadrant, q1-trend, q2-levels, q3-momentum, pattern-blacklist, micro-trend-override, mtf-skew, journal-vs-csv, gustafssonkotte]
related:
  - sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md
  - entities/people/gustafssonkotte.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/polymarket-retail-trading-discipline.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-updown-bot-taxonomy.md
maturity: draft
created: 2026-05-22
updated: 2026-05-22
clusters: [polymarket, bot-architecture]
---

## Relations

- @sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md — Post 2 primary source (K57)
- @entities/people/gustafssonkotte.md — author/operator
- @concepts/multi-module-bot-conflict-detector-pattern.md — K55 rewrite (conflict-detector + broken-data); this page is the **next iteration** (quadrant skew + blacklist + micro override)
- @concepts/polymarket-bot-architecture.md — parent architecture catalog
- @concepts/polymarket-updown-bot-taxonomy.md — 5-minute UpDown market class
- @concepts/polymarket-retail-trading-discipline.md — complementary retail sizing discipline (different author)
- @concepts/polymarket-bot-architecture.md — parent catalog
- @concepts/polymarket-updown-bot-taxonomy.md — 5-minute UpDown market class
- @sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md — K57 Post 2

## Raw Concept

K57 Posts.docx Post 2 — @Gustafssonkotte day-8 post-mortem after the K55 "deleted half my code" rewrite. Documents why a **working** bot can still exhibit one-sided trade streams (all UP on bullish days) and how **subtractive** filters (blacklist) beat new indicators.

## Narrative

### Three-quadrant brain (Q1/Q2/Q3)

| Module | Role | Outputs |
|--------|------|---------|
| Q1 Trend | Multi-timeframe alignment (shortest window **10m** in pre-patch config) | `p_up`, `strength` |
| Q2 Levels | Swing highs/lows, liquidity sweeps | `p_level`, `s_level` |
| Q3 Momentum | RSI14/7, Bollinger state, PSAR, order flow | `p_momentum`, `s_momentum` |

Combined: `conf = p_trend*s_trend + p_level*s_level + p_momentum*s_momentum` → side + confidence.

**Structural skew:** when Q1 MTF is fully bullish (+4), Q1 dominates `conf` for UP and contributes almost nothing to DOWN — even strong Q2/Q3 reversal signals cannot flip side. Symptom: 30 trades all UP on a bullish day (coin-flip P&L, missed pullback shorts).

### Micro-trend override (hypothesis under test)

Add 1m/2m trends from `candles_30s`:

- If 1m and 2m agree → `micro_dir`
- Else if 1m strength ≥ threshold → use 1m
- Override: macro UP (`p_trend ≥ 0.60`) + micro DOWN + `micro_strength ≥ 0.3` → allow DOWN at 90% confidence (symmetric for bearish macro + micro UP)

First evening: **zero overrides** on a straight-trend day (expected). Lowered thresholds 0.5→0.3 and macro gate 0.65→0.60 on 2026-05-21 to catch moderate pullbacks [TENTATIVE — awaiting chop-regime validation].

### Pattern blacklist (production impact)

Statistic-driven hard skips (not new alpha):

| Rule | Rationale (series stats) |
|------|---------------------------|
| UP + BB `touch_upper` | 13 LOSS / −$29 over 4 days — local top fade |
| UP + RSI7 ≥ 70 | 7L / 2W / −$13 — short-term overbought |
| DOWN + BB flat + RSI14 < 40 | −$13 series — weak bear without structure |

First session: **1,088** would-be entries blocked vs **30** executions; author reports best filter ever added [TENTATIVE single-operator, single session].

### Operational discipline (reinforced)

- **Source of truth:** Polymarket CSV exports, not bot journal (journal still inflates win rate pre-settlement).
- **ENV switches** gate every patch for instant rollback.
- **Planned:** timing-aware momentum — skip entries where BTC cannot reach strike given `mins_left` and observed tick speed (not yet implemented).

### Cemini relevance

Portable to any **short-horizon Polymarket directional bot** on Cemini:

1. Audit MTF minimum window vs market resolution window (10m MTF on 5m markets → directional blindness).
2. Add **subtractive** pattern gates before adding indicators.
3. Treat journal metrics as non-authoritative until exchange-confirmed.

## Snippets

> "Sometimes the best improvement is not to add but to stop doing badly." [Source: Posts.docx — @Gustafssonkotte Post 2]

> "I gate every improvement behind one switch in ENV. If something is going wrong, one command brings the bot back to its previous state." [Source: Posts.docx — @Gustafssonkotte Post 2]
