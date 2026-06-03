---
title: Polymarket football shock-recovery trading (in-play microstructure)
type: concept
tags: [concept, polymarket, sports, world-cup-2026, microstructure, shock-trading, in-play, k94]
keywords: [shock-detection, percentile-ladder, five-dimension-bucket, overreaction-recovery, match-markets]
related:
  - sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md
  - entities/people/rohonchain.md
  - concepts/polymarket-sports-microstructure-bot-taxonomy.md
  - concepts/world-cup-advance-market-bot-v1.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - entities/tools/world-cup-bot.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
  - projects/world-cup-bot/Architecture/Architecture - match_shock_v1.md
  - projects/world-cup-bot/Architecture/Architecture - match_shock_pmxt_backtest.md
  - entities/tools/pmxt.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - sources/trading-posts-compilation-17-2026-06-03.md
maturity: draft
created: 2026-06-02
updated: 2026-06-03
---

## Relations

- @sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md — primary source (@RohOnChain WC 2026 article)
- @concepts/polymarket-sports-microstructure-bot-taxonomy.md — sports microstructure map; this is a distinct **live shock recovery** archetype
- @entities/tools/world-cup-bot.md — v1 advance LP bot; see **WC Bot integration** below
- @sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md — defensive mirror: advance LP must **avoid** being the counterparty to this strategy

## Raw Concept

Systematic **in-play** strategy on Polymarket **football match markets**: detect violent price drops after goals/cards, classify shock context, enter via **percentile-based limit ladders**, exit on fixed **mean-reversion target** (~4¢). Does not predict match outcomes — trades **panic overreaction**.

## Narrative

### Core loop

```
live trades → shock detect (2m window) → 5D classify → bucket lookup (P50–P95 depths)
    → ladder limits (60s TTL) → fill → sell at pre_price − depth + 4¢ recovery
```

### Why football (author argument)

1. Low scoring → each goal is a large probability jump
2. 90+ minutes → many events per match
3. WC 2026 → 104 matches in 39 days → repeated samples for bucket stats

### Five-dimension buckets

Independent classifiers combine into a key like `deep|underdog|balanced|mid|level`. ~720 theoretical combos; author trades only buckets with ≥5 historical shocks (else conservative default depths).

**Tuning insight [TENTATIVE]:** author reports **moderate_fav (75–85¢ pre-shock)** buckets outperform in backtest — filter buckets before live, don't run stock config.

### Risk / failure modes

| Risk | Mitigation in framework |
|------|-------------------------|
| Thin bucket overfit | Min 5 shocks; shallow default percentiles |
| Permanent shocks (blowout, late goal) | Goal-state + time dims; final-phase bucket often non-recovering |
| Courtsiding / faster feeds | Not addressed — sub-second stadium data beats TV traders [see DR 09] |
| WC retail influx | Unknown — author frames as open question (larger overreactions vs deeper liquidity) |
| Same-event double shock | 3m cooldown |

### Data for backtest

- **Polymarket Data API** — primary path in `world-cup-bot` (`match-shock-export`); **Dome API EOL 2026-04-28** [CONFIRMED]
- **Live CLOB WS** — `match-shock-record` for WC 2026 slugs
- **pmxt** — optional deep OB on librarian; deprioritized when football slugs sparse (see @projects/world-cup-bot/Architecture/Architecture - match_shock_pmxt_backtest.md)

### WC Bot integration — **Module 8 shipped (orthogonal to advance LP)**

| Dimension | World Cup Bot v1 (Modules 1–7) | Shock-recovery (Module 8) |
|-----------|-------------------------------|---------------------------|
| Markets | Team **advance to knockout** | **Match winner / in-play** |
| Timing | Pregame; cancel **≥10h** before kick | **During live play** |
| Edge | Conviction + LP rewards | Overreaction mean reversion |
| Policy | `hard_halt` in-play (DR 09) | Separate path; `shock_match.yaml` `enabled: false` default |
| Codebase | `quoter.py` / fill-handler | `match_shock.py` — **never** import from quoter |

**Handoff:** `trading_mode.py` — LP on advance markets until kickoff window; SHOCK on match slugs when promoted (`WC_SHOCK_ENABLED=1`).

**K97 (@RohOnChain re-share):** open sizing question — WC retail influx may **widen** shock dips or **dampen** recovery; captured in `config/shock_match.yaml` `operator.wc_volume_hypothesis` (unset until bucket grid on WC tapes).

**What NOT to do:** Enable shock live POST on the advance-LP wallet without isolation and separate promotion gates.

### Relation to taxonomy

@concepts/polymarket-sports-microstructure-bot-taxonomy.md Type 1 (cross-line / connected-line desync) adjacent; this strategy is narrower — **single-line shock fade** on match win markets with explicit historical depth priors.

## Snippets

> "You are not betting on the match. You are providing liquidity into a panic and getting paid for it." [Source: rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md]

Default ladder weights: P50 10%, P75 20%, P90 30%, P95 40% of capital per shock event.
