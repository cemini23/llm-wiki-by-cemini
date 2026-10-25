---
title: "@de1lymoon — Three Quant Formulas for Polymarket (Poisson + Shannon + Taleb, May 2026)"
type: source
tags: [source, polymarket, quant, poisson, shannon-entropy, kl-divergence, fat-tails, kelly, barbell, insider-detection, rare-events, donny-watchlist-adjacent]
keywords: [de1lymoon, polymarket-quant, poisson-distribution, shannon-entropy, kl-divergence, taleb-fat-tails, quarter-kelly, barbell-portfolio, insider-detection, entropy-collapse-3-sigma, prediction-markets, predictparity]
related:
  - entities/platforms/polymarket.md
  - concepts/poisson-edge-rare-events.md
  - concepts/shannon-entropy-kl-divergence-prediction-markets.md
  - concepts/taleb-fat-tails-barbell-prediction-markets.md
  - concepts/insider-detection-entropy-collapse.md
  - concepts/kelly-sizing-quarter.md
  - concepts/three-formula-system-polymarket-rare-events.md
maturity: validated
read_status: deep-read
created: 2026-05-13
updated: 2026-05-13
clusters: [polymarket, quant-formulas]
---

## Relations

- @entities/platforms/polymarket.md — execution venue assumed by all three formulas
- @concepts/poisson-edge-rare-events.md — Formula 1 derived concept page
- @concepts/shannon-entropy-kl-divergence-prediction-markets.md — Formula 2 derived
- @concepts/taleb-fat-tails-barbell-prediction-markets.md — Formula 3 derived
- @concepts/insider-detection-entropy-collapse.md — sub-pattern of Formula 2 (3σ entropy drop)
- @concepts/kelly-sizing-quarter.md — sizing rule used by all three formulas
- @concepts/three-formula-system-polymarket-rare-events.md — combined `complete_rare_event_system` synthesis (weighted 40/35/25)

## Raw Concept

- **Author**: @de1lymoon (X handle; referral URL `predictparity.com?code=moon`)
- **Format**: docx; ~700 substantive lines including full Python implementations
- **Date**: May 2026 (drop date 2026-05-13)
- **Drop location**: `research to be indexed/@de1lymoon.docx` → librarian
- **sha256**: `98649230c3c26ac6...`
- **Size**: 25,707 bytes
- **Preingest verdict**: NEW

**What prompted this page**: a single coherent post containing three production-ready quant formulas for Polymarket, plus a synthesis function combining all three with sensible default weights. Distinctive value: full Python with explicit thresholds, not abstract framings.

## Narrative

### The three formulas

| # | Name | Domain | Core question |
|---|------|--------|----------------|
| 1 | Poisson edge | Rare-event markets (count of occurrences) | Is the market price under/over the Poisson-implied probability? |
| 2 | Shannon entropy + KL divergence | Information-edge sizing | How many bits of information do my odds carry vs the market's? |
| 3 | Taleb fat tails + barbell | Tail-risk sizing | Are tails fat enough that quarter-Kelly across many small bets dominates concentrated bets? |

A fourth function — `complete_rare_event_system` — combines all three with weights **40% Poisson + 35% estimate + 25% fat-tail**.

### Formula 1 — Poisson edge for rare events

Function signature (paraphrased):

```python
polymarket_poisson_edge(
    event_name: str,
    historical_rate: float,      # λ — average events per period
    market_price_cents: int,     # Polymarket YES price in cents
    time_periods: int,           # how many periods accumulate
) -> dict
```

Returns dict with:
- `poisson_probability` — P(at least one event) over the window
- `edge_cents` — Poisson-implied price minus market price (positive → market underpricing the event)
- `quarter_kelly_fraction` — sized for fractional Kelly, defensive (¼ of full Kelly)
- `direction` — `BUY_YES` / `BUY_NO` / `SKIP`

**Where Poisson applies**: any "will rare event X happen N times by date Y" market — earthquakes, plane crashes, individual rare political events, sports rare outcomes (no-hitters, hat-tricks). Bad fit: anything bounded or with strong heterogeneity (election outcomes, binary "yes/no this person").

### Formula 2 — Shannon entropy + KL divergence

```python
shannon_entropy(p: float) -> float
kl_divergence(p_mine: float, p_market: float) -> float
scan_markets(estimates: list, prices: list, names: list) -> list[dict]
```

`scan_markets` ranks markets by KL bits of edge. Trade thresholds:

| KL bits | Action |
|---------|--------|
| < 0.05 | SKIP — edge is in the noise |
| 0.05 – 0.10 | WEAK — small position only |
| 0.10 – 0.20 | TRADE — normal position size |
| 0.20 – 0.30 | STRONG TRADE |
| > 0.30 | RECHECK — suspiciously large edge; verify your input first |

The >0.30 RECHECK threshold is the operational humility gate — if your model says you have a quarter-bit-of-information edge over the market, either you're wrong about the market price or your model has a bug.

### Formula 2.5 — Insider detection via entropy collapse

```python
detect_insider_activity(
    price_history: list[float],
    window: int = 12,
    threshold: float = 3.0,   # sigmas
) -> bool
```

Watches the rolling Shannon entropy of the price series. A 3σ drop in entropy without an accompanying news event is the insider-trading signal. Window = 12 periods.

This is single-source [TENTATIVE] — the 3σ threshold and 12-period window are pulled from one operator's heuristic, not a back-tested study. Flagged as a research candidate, not a deployment-ready signal. See `@concepts/insider-detection-entropy-collapse.md`.

### Formula 3 — Taleb fat tails + barbell

```python
fat_tail_analysis(returns: list[float]) -> dict
polymarket_fat_tail_edge(...) -> dict
barbell_portfolio(bankroll: float, safe_markets: list, tail_markets: list) -> dict
```

`barbell_portfolio` allocates **85% safe / 15% tail** by default. The split is grounded in Taleb's *Antifragile* heuristic for fat-tailed distributions where occasional extreme payoffs dominate expected return.

`fat_tail_analysis` computes kurtosis and a Hill estimator on observed returns. Markets above a fat-tail cutoff get the 15% tail-bucket allocation; everything else lives in the 85% safe bucket.

### Empirical data point — cheap contracts mispricing

The post cites a striking statistic:

- **5¢ contracts win 4.18%** of the time (mispriced — market underpricing rare positive outcomes)
- **1¢ contracts win 0.43%** of the time (overpriced — market is being scammed by lottery-ticket buyers)

[OPEN QUESTION 2026-05-13] Provenance of these specific percentages is unclear from the post. Worth cross-checking against Polymarket historical CSV / on-chain settlement data before treating as a confirmed regime stat.

### Synthesis — `complete_rare_event_system`

The capstone function weights the three formulas:

- **40%** Poisson probability
- **35%** operator estimate (the "your number" input — confidence-weighted)
- **25%** fat-tail adjustment

Returns a recommended position size + direction. This is the "if you only call one function, call this one" entry point.

### Cemini relevance

1. **Direct adoption candidates** for Cemini's polymarket-strategy module: all three core formulas + `complete_rare_event_system` are pure-Python, no external deps beyond numpy/scipy. They land cleanly under `/opt/cemini/agents/strategies/` once the Polymarket trading surface is wired up.
2. **Quarter-Kelly default** matches Cemini's preferred sizing discipline (capital preservation > perfect entries — see `@concepts/polymarket-bot-architecture.md`).
3. **KL-bits threshold table** is directly usable as a triage filter at the Conductor level — every Polymarket-related signal can be pre-scored against the bits-of-edge gate before consuming downstream compute.
4. **Insider-detection sub-formula** needs back-testing before deployment. Good candidate for the harmfulness-audit / trajectory harness from the OpenSpec K37 work.
5. **5¢-mispricing empirical claim** — if confirmed, suggests a "buy all 5¢ contracts above some volume threshold" passive strategy worth testing. If rejected, becomes a [RETRACTED] note.

## Snippets

> "5¢ contracts win 4.18% of the time. 1¢ contracts win 0.43% of the time." [Source: @de1lymoon.docx — single-source claim, verification pending]

> "KL divergence < 0.05 bits: skip. 0.05–0.10: weak. 0.10–0.20: trade. > 0.30: recheck — if you think you have this much edge over the market, you're probably wrong." [Source: @de1lymoon.docx, paraphrased]

> "85% safe markets / 15% tail markets. Taleb barbell, on Polymarket." [Source: @de1lymoon.docx]

> "complete_rare_event_system: 40% Poisson + 35% your estimate + 25% fat-tail adjustment." [Source: @de1lymoon.docx]

## Dead Ends

- **Full-Kelly sizing on Polymarket** — implicit dead end. Every formula in the post defaults to quarter-Kelly. Full-Kelly on a fat-tailed venue with frequent regime changes is a documented blow-up pattern.
- **Using mean-reversion logic on Poisson markets** — Poisson assumes events are independent. Markets that look like they "should mean-revert" (n more occurrences after k already happened) usually don't — that's gambler's fallacy applied to a memoryless process.
- **Treating entropy collapse as standalone insider signal** — without news-event cross-reference, the 3σ entropy drop has too many false positives (genuine market discoveries also collapse entropy). The cross-reference against a news feed is the load-bearing piece, not the threshold itself.
