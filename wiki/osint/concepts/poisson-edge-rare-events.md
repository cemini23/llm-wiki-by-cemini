---
title: "Poisson Edge for Rare-Event Prediction Markets"
type: concept
tags: [concept, polymarket, quant, poisson, rare-events, edge-detection, sizing, quarter-kelly]
keywords: [poisson-distribution, rare-events, edge-cents, polymarket-poisson-edge, quarter-kelly, lambda, time-periods, market-mispricing]
related:
  - sources/de1lymoon-three-formulas-2026-05.md
  - entities/platforms/polymarket.md
  - concepts/shannon-entropy-kl-divergence-prediction-markets.md
  - concepts/taleb-fat-tails-barbell-prediction-markets.md
  - concepts/kelly-sizing-quarter.md
  - concepts/three-formula-system-polymarket-rare-events.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @sources/de1lymoon-three-formulas-2026-05.md — primary source (Formula 1 of 3)
- @entities/platforms/polymarket.md — execution venue
- @concepts/shannon-entropy-kl-divergence-prediction-markets.md — Formula 2 of the trio (information-edge sizing)
- @concepts/taleb-fat-tails-barbell-prediction-markets.md — Formula 3 (tail-risk sizing)
- @concepts/kelly-sizing-quarter.md — sizing rule used here
- @concepts/three-formula-system-polymarket-rare-events.md — synthesis combining all three

## Raw Concept

What this page answers: how to compute a Poisson-based fair-value probability for a "will rare event X happen ≥1 time in window Y" market, compare it to the market price, and produce a quarter-Kelly position size + direction.

## Narrative

### When Poisson applies

Poisson distribution is the right tool for prediction markets that ask **"will rare event X occur ≥N times before date Y?"** where X is:

- Memoryless (history of past occurrences doesn't change the rate)
- Rare (the per-period probability is small)
- Approximately independent across periods

**Good fits**: earthquakes ≥M magnitude, plane crashes, hat-tricks / no-hitters / rare sports events, individual rare political events (single named figure resigning, single drone strike).

**Bad fits**: binary outcomes (election winners), bounded counts (will N >= total population), strongly heterogeneous outcomes where the per-period rate clearly changes.

### The formula

Probability of **at least one** event over a window of `T` periods given historical rate `λ` per period:

```
P(X ≥ 1) = 1 − e^(−λT)
```

Implemented (paraphrased from @de1lymoon):

```python
import math

def polymarket_poisson_edge(
    event_name: str,
    historical_rate: float,      # λ — events per period
    market_price_cents: int,     # Polymarket YES price (0–100)
    time_periods: int,           # T — window length
) -> dict:
    poisson_prob = 1 - math.exp(-historical_rate * time_periods)
    fair_value_cents = poisson_prob * 100
    edge_cents = fair_value_cents - market_price_cents

    # Quarter-Kelly sizing
    full_kelly = abs(edge_cents) / 100
    qk = full_kelly / 4

    if edge_cents > 1:    # >1¢ underpricing
        direction = "BUY_YES"
    elif edge_cents < -1: # >1¢ overpricing
        direction = "BUY_NO"
    else:
        direction = "SKIP"

    return {
        "event": event_name,
        "poisson_probability": poisson_prob,
        "fair_value_cents": fair_value_cents,
        "edge_cents": edge_cents,
        "quarter_kelly_fraction": qk,
        "direction": direction,
    }
```

### Why quarter-Kelly, not full-Kelly

Polymarket markets exhibit fat-tailed regime shifts (resolution disputes, oracle delays, on-chain settlement quirks). Full-Kelly sizing assumes the model's probability is correct; under model error, full-Kelly blows up much faster than fractional. Quarter-Kelly is the post-Taleb operational default — see `@concepts/kelly-sizing-quarter.md`.

### Worked example

Market: "Will there be ≥1 magnitude-7+ earthquake in country X in next 30 days?"

- Historical rate: 1 such event per 90 days → λ = 1/90 per day
- Window: 30 days → T = 30
- Market YES price: 25¢

Poisson probability: `1 − exp(−30/90) = 1 − exp(−0.333) ≈ 0.283` → fair value 28.3¢

Edge: 28.3 − 25 = +3.3¢ (market underpricing). Direction: BUY_YES.

Quarter-Kelly: `(3.3/100) / 4 = 0.0083` → 0.83% of bankroll on YES.

### Sanity-check rules

1. **λ must come from genuine historical data**, not back-of-envelope. The single biggest failure mode is fabricated rate estimates.
2. **T must match the market resolution window**, not a convenient round number.
3. **If `|edge| < 1¢`**, SKIP — within bid/ask noise and execution slippage.
4. **If `|edge| > 30¢`** ("too much edge"), do not trust the calculation — either λ is wrong or the market is pricing in information the model doesn't see. RECHECK before trading.

### Cemini relevance

- Direct adoption candidate for `/opt/cemini/agents/strategies/polymarket_poisson.py` once trading surface is wired.
- Quarter-Kelly default matches house sizing discipline.
- The "too much edge → RECHECK" rule is the operational humility gate — same shape as the >0.30-bits-of-KL gate in the Shannon formula.

## Snippets

> "Poisson edge: 1 − e^(−λT). Quarter-Kelly sizing. If edge < 1¢, skip; if edge > 30¢, recheck — you probably have the wrong rate." [Source: @de1lymoon.docx — paraphrased]

## Dead Ends

- **Applying Poisson to non-memoryless events** — election outcomes, individual binary "will X happen by date Y" markets, anything where prior occurrences affect future rate. Poisson assumption breaks; estimate is garbage.
- **Using a fabricated λ** — the rate must be calibrated against multi-year historical data. Naive rate guesses produce the largest single category of model error.
- **Full-Kelly on a Poisson signal** — Polymarket fat tails (resolution disputes, oracle delays) make full-Kelly unsafe regardless of how confident the Poisson rate is.
