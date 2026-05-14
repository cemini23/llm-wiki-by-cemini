---
title: "Three-Formula System for Polymarket Rare-Event Trading (Synthesis)"
type: concept
tags: [concept, polymarket, quant, synthesis, rare-events, complete-rare-event-system, weighted-ensemble]
keywords: [complete-rare-event-system, three-formula-synthesis, poisson-shannon-taleb, 40-35-25-weights, ensemble, polymarket-strategy]
related:
  - sources/de1lymoon-three-formulas-2026-05.md
  - concepts/poisson-edge-rare-events.md
  - concepts/shannon-entropy-kl-divergence-prediction-markets.md
  - concepts/taleb-fat-tails-barbell-prediction-markets.md
  - concepts/kelly-sizing-quarter.md
  - concepts/insider-detection-entropy-collapse.md
  - entities/platforms/polymarket.md
  - entities/tools/aulekator-polymarket-btc-bot.md
  - concepts/issue1-worked-example-anthropic-pentagon-2026.md
maturity: draft
created: 2026-05-13
updated: 2026-05-14
---

## Relations

- @sources/de1lymoon-three-formulas-2026-05.md — primary source (synthesis layer)
- @concepts/poisson-edge-rare-events.md — Formula 1 component
- @concepts/shannon-entropy-kl-divergence-prediction-markets.md — Formula 2 component
- @concepts/taleb-fat-tails-barbell-prediction-markets.md — Formula 3 component
- @concepts/kelly-sizing-quarter.md — universal sizing primitive
- @concepts/insider-detection-entropy-collapse.md — defensive sub-signal
- @entities/platforms/polymarket.md — execution venue
- @entities/tools/aulekator-polymarket-btc-bot.md — K44 NautilusTrader-based bot; operates on 15-min bars (different timescale, complementary)

## Raw Concept

What this page answers: when all three of @de1lymoon's formulas exist independently, how does the `complete_rare_event_system` function weight them into a single position decision?

## Narrative

### The synthesis function

```python
def complete_rare_event_system(
    event_name: str,
    historical_rate: float,
    operator_estimate: float,      # your subjective probability
    market_price_cents: int,
    time_periods: int,
    safe_or_tail_bucket: str,      # "safe" | "tail"
    bankroll: float,
) -> dict:
    # 1. Poisson signal
    poisson_result = polymarket_poisson_edge(
        event_name, historical_rate, market_price_cents, time_periods
    )

    # 2. Operator-estimate signal (KL-bits sized)
    estimate_kl_bits = kl_divergence(operator_estimate, market_price_cents / 100)
    estimate_size = _kl_bucket_to_size(estimate_kl_bits)

    # 3. Fat-tail adjustment
    tail_multiplier = _fat_tail_size_multiplier(safe_or_tail_bucket)

    # Weighted combination
    weighted_fraction = (
        0.40 * poisson_result["quarter_kelly_fraction"]
        + 0.35 * estimate_size
        + 0.25 * tail_multiplier
    )

    # Apply quarter-Kelly cap regardless
    final_fraction = min(weighted_fraction, 0.25)
    return {
        "event": event_name,
        "final_fraction": final_fraction,
        "position_usd": bankroll * final_fraction,
        "components": {
            "poisson": poisson_result,
            "kl_bits": estimate_kl_bits,
            "bucket": safe_or_tail_bucket,
        },
    }
```

### The weights — 40 / 35 / 25

- **40% Poisson** — the highest-weight component because Poisson edge is grounded in historical data (not operator opinion). When the Poisson signal is strong, it's load-bearing.
- **35% operator estimate (KL bits)** — the second-highest. This is "your number" — model output or hand-calibrated probability. KL-bits-sized so its weight is in information units, not raw probability difference.
- **25% fat-tail adjustment** — the smallest because it's a multiplier on the asset-allocation decision (safe vs tail bucket), not a directional signal. Modifies size, not direction.

The 40/35/25 split is the source author's default; like the 85/15 barbell split, it's a starting point, not a sacred constant.

### Worked example

Market: "Will there be ≥1 magnitude-7+ earthquake in country X in next 30 days?" Bankroll $10,000. Bucket: tail.

- Poisson edge: 3.3¢ → quarter-Kelly 0.0083
- Operator estimate: 0.30 vs market 0.25 → KL ≈ 0.012 bits → SKIP bucket → size 0
- Fat-tail (tail bucket): multiplier 1.5

Weighted: `0.40 · 0.0083 + 0.35 · 0 + 0.25 · 1.5 · 0.0083 ≈ 0.00643`

Final fraction: 0.643% → position size **$64**.

The combination is intentionally conservative — when only one signal fires (Poisson, in this example), the weighted output stays small.

### Operational gates (apply after weighted output)

1. **>0.30 KL bits anywhere → RECHECK**, override → 0 position
2. **|Poisson edge| > 30¢ → RECHECK**, override → 0 position
3. **Insider entropy collapse with no news → STAY OUT**, override → 0 position
4. **Per-position hard cap** (default 5%) — applied after all weighted math

### Why combine instead of pick-the-best

A pick-the-best approach (use whichever single formula has highest signal) over-trusts whatever's loudest. Combining:

- **Down-weights single-source signals** — if only Poisson fires, the weighted fraction is small
- **Up-weights agreement** — when Poisson + KL both fire on the same side, weights compound
- **Allows graceful degradation** — if one input is unavailable (e.g., no kurtosis data → fat-tail term = 0), the system still produces a sized position from the remaining components

### Cemini relevance

- **Direct adoption candidate** as the top-level entry point for Cemini's Polymarket strategy module: `/opt/cemini/agents/strategies/polymarket_rare_events.py`
- **Configurable weights** — surface 40/35/25 as YAML config so the operator can adjust without code change
- **Override hooks** for the three RECHECK gates — should compose with Cemini's reviewer-agent v2 (K37 OpenSpec, currently deferred) once the production tool surface lands
- **The defensive sub-signal** (insider entropy collapse → stay out) is the cleanest place to wire `@concepts/insider-detection-entropy-collapse.md` into the trading loop

## Snippets

> "complete_rare_event_system: 40% Poisson + 35% your estimate + 25% fat-tail adjustment." [Source: @de1lymoon.docx]

## Dead Ends

- **Picking single-formula winner instead of weighted combination** — over-trusts whichever signal is loudest. The weighted ensemble produces smaller, more-resilient positions.
- **Adjusting weights inside the hot loop** — weights are operator config, not runtime variable. Live tuning of weights is a route to over-fitting on recent history.
- **Skipping the override gates** — the three RECHECK gates exist because high-magnitude signals are usually bugs, not edges. Bypassing them is the documented blow-up path.
