---
title: "Quarter-Kelly Sizing (House Default for Prediction Markets)"
type: concept
tags: [concept, kelly-criterion, fractional-kelly, position-sizing, risk-management, polymarket, default-rule]
keywords: [quarter-kelly, fractional-kelly, kelly-criterion, position-sizing, blow-up-risk, model-error-buffer, capital-preservation]
related:
  - sources/kelly-1956-information-rate.md
  - sources/de1lymoon-three-formulas-2026-05.md
  - concepts/poisson-edge-rare-events.md
  - concepts/shannon-entropy-kl-divergence-prediction-markets.md
  - concepts/taleb-fat-tails-barbell-prediction-markets.md
  - concepts/polymarket-bot-architecture.md
  - concepts/three-formula-system-polymarket-rare-events.md
  - entities/platforms/polymarket.md
  - concepts/issue1-worked-example-anthropic-pentagon-2026.md
  - concepts/issue2-worked-example-iran-airspace-2026.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/sports-prediction-consensus-agent.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/gambling-wiki-federation.md
  - concepts/reviewer-passive-injection-corpus.md

maturity: validated
created: 2026-05-13
updated: 2026-07-08
---

## Relations

- @sources/kelly-1956-information-rate.md — primary source for the Kelly criterion; derives the optimal fraction from first principles
- @sources/de1lymoon-three-formulas-2026-05.md — quarter-Kelly default used by all three formulas
- @concepts/poisson-edge-rare-events.md — applies quarter-Kelly to Poisson signal
- @concepts/shannon-entropy-kl-divergence-prediction-markets.md — applies quarter-Kelly to KL-bits-sized signal
- @concepts/taleb-fat-tails-barbell-prediction-markets.md — applies quarter-Kelly inside both buckets of the barbell
- @concepts/polymarket-bot-architecture.md — "capital preservation > perfect entries" explicit principle
- @concepts/gambling-wiki-federation.md — general Kelly theory in @gambling-wiki/concepts/kelly-criterion-betting.md
- @concepts/reviewer-passive-injection-corpus.md — K37 reviewer bundle cites sizing caps

## Raw Concept

What this page answers: why every Polymarket strategy in Cemini's playbook defaults to **quarter-Kelly** (¼ of the Kelly-optimal fraction), not full-Kelly.

## Narrative

### The Kelly criterion (brief)

Given a positive-edge bet, the Kelly fraction `f*` is the bet size that maximizes expected long-run log wealth. For a binary bet with probability `p` of winning, payout-to-stake ratio `b`:

```
f* = (p · (b + 1) − 1) / b
```

For an even-money bet (`b = 1`) with `p = 0.55`: `f* = (0.55 · 2 − 1) / 1 = 0.10` → bet 10% of bankroll.

### Why not full-Kelly

Full-Kelly is **optimal under the assumption that `p` is exactly known**. In practice on Polymarket:

1. **Model error** — your `p_mine` is a guess. If the true `p` is 5 percentage points lower than your estimate, full-Kelly is over-betting.
2. **Fat tails** — Polymarket markets are fat-tailed (resolution disputes, oracle delays, on-chain settlement quirks). Full-Kelly under fat tails has worse drawdowns than the log-utility math predicts.
3. **Regime change** — the parameters change. A `p` calibrated on six months of data may not hold for the next six months.
4. **Concurrent positions** — Kelly is single-bet. With many simultaneous positions, the sum of full-Kelly fractions overshoots true Kelly for the portfolio.

The empirical observation across multiple decades of fractional-Kelly research: **half-Kelly captures ~75% of full-Kelly's growth rate with ~50% of the volatility**. Quarter-Kelly captures ~50% of the growth with ~25% of the volatility.

### Quarter-Kelly = the house default

@de1lymoon's three formulas all default to **quarter-Kelly**. Reasons specific to Polymarket:

- **The quarter level is below the "model error blow-up" threshold** for typical Polymarket `p` uncertainty
- **Multiple concurrent positions** in Cemini's planned architecture mean the effective portfolio-Kelly is lower than per-bet Kelly anyway
- **Capital preservation > perfect entries** (see `@concepts/polymarket-bot-architecture.md`) — the operational discipline the punisher playbook also defaults to

### Implementation pattern

```python
def quarter_kelly_fraction(edge: float, payout_ratio: float = 1.0) -> float:
    # `edge` here is the absolute edge proxy:
    # for Poisson: |fair_value − market_price| / 100
    # for KL-bits: bucketed via the threshold table, then scaled to a fraction
    full_kelly = abs(edge) / payout_ratio
    return full_kelly / 4
```

### When to override

Quarter-Kelly is the default, not the law. Operator overrides:

| Override | When |
|----------|------|
| **Half-Kelly** | High-conviction signal with multiple independent confirmations (e.g., Poisson + KL agree, fat-tail bucket says safe) |
| **Eighth-Kelly** | Unknown new strategy in dry-run / first 30 days live |
| **Full position cap** | Hard cap at N% of bankroll regardless of Kelly output — typically 5% per position |

### Cemini relevance

Cemini's planned Polymarket trading surface should encode quarter-Kelly as a **default**, not a **hardcoded** value:

- Strategy modules read a `kelly_fraction` config (default 0.25)
- Operator can override per-strategy via config
- A separate per-position **hard cap** (5–10% of bankroll) acts as the second safety layer

The hard cap is non-negotiable. Quarter-Kelly mis-sized by 2–3x is recoverable; full-portfolio Kelly mis-sized by 2–3x is a blow-up.

## Snippets

> "Capital preservation > perfect entries." [Source: @concepts/polymarket-bot-architecture.md citing @0x_Punisher's playbook]

> "Full-Kelly assumes you know p. You don't." [Source: paraphrased fractional-Kelly literature — Thorp, MacLean]

## Dead Ends

- **Full-Kelly on Polymarket** — model error + fat tails + multiple concurrent positions all push the safe ceiling well below full-Kelly. The math is correct under the assumptions; the assumptions don't hold.
- **Hardcoding 0.25 with no override path** — the right default isn't the right number for every signal. Make the fraction a config, not a constant.
- **Quarter-Kelly without a hard per-position cap** — Kelly outputs scale with edge. A high-edge signal under quarter-Kelly can still produce a 30%-of-bankroll position. Hard caps are the safety net.
