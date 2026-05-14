---
title: "Shannon Entropy + KL Divergence for Prediction-Market Edge"
type: concept
tags: [concept, polymarket, quant, shannon-entropy, kl-divergence, information-edge, sizing, kl-bits-threshold]
keywords: [shannon-entropy, kl-divergence, kullback-leibler, information-edge, bits-of-information, scan-markets, threshold-table, recheck-gate]
related:
  - sources/de1lymoon-three-formulas-2026-05.md
  - entities/platforms/polymarket.md
  - concepts/poisson-edge-rare-events.md
  - concepts/taleb-fat-tails-barbell-prediction-markets.md
  - concepts/insider-detection-entropy-collapse.md
  - concepts/kelly-sizing-quarter.md
  - concepts/three-formula-system-polymarket-rare-events.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @sources/de1lymoon-three-formulas-2026-05.md — primary source (Formula 2 of 3)
- @entities/platforms/polymarket.md — execution venue
- @concepts/poisson-edge-rare-events.md — Formula 1
- @concepts/taleb-fat-tails-barbell-prediction-markets.md — Formula 3
- @concepts/insider-detection-entropy-collapse.md — sub-pattern using rolling Shannon entropy
- @concepts/kelly-sizing-quarter.md — sizing rule
- @concepts/three-formula-system-polymarket-rare-events.md — synthesis combining all three

## Raw Concept

What this page answers: how to express the gap between your subjective probability and the market's implied probability as **bits of information**, and use that quantity directly as a position-sizing input.

## Narrative

### The intuition

A market price `p_market` (between 0 and 1) is a probability statement. Your model's probability `p_mine` is another probability statement. The information-theoretic distance between them — how many bits of new information your number contains relative to the market — is the **Kullback-Leibler (KL) divergence**:

```
KL(p_mine || p_market) = p_mine · log₂(p_mine / p_market)
                       + (1 − p_mine) · log₂((1 − p_mine) / (1 − p_market))
```

If KL is large, you and the market disagree strongly; if KL is small, you're agreeing in expectation. Either way, the size of the disagreement (in bits) is the edge signal.

### Implementation (paraphrased from @de1lymoon)

```python
import math

def shannon_entropy(p: float) -> float:
    if p in (0.0, 1.0):
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)

def kl_divergence(p_mine: float, p_market: float) -> float:
    # both in (0, 1)
    eps = 1e-9
    p_mine = max(eps, min(1 - eps, p_mine))
    p_market = max(eps, min(1 - eps, p_market))
    return (p_mine * math.log2(p_mine / p_market)
            + (1 - p_mine) * math.log2((1 - p_mine) / (1 - p_market)))

def scan_markets(estimates: list[float], prices: list[float], names: list[str]) -> list[dict]:
    rows = []
    for est, price, name in zip(estimates, prices, names):
        bits = kl_divergence(est, price)
        rows.append({"market": name, "kl_bits": bits, "estimate": est, "market_price": price})
    return sorted(rows, key=lambda r: -r["kl_bits"])
```

### Trade thresholds (operator heuristic)

| KL bits | Action | Rationale |
|---------|--------|-----------|
| < 0.05 | **SKIP** | Edge is in the noise; transaction costs eat it |
| 0.05 – 0.10 | **WEAK** | Small position only |
| 0.10 – 0.20 | **TRADE** | Normal position size |
| 0.20 – 0.30 | **STRONG TRADE** | Above-average size |
| > 0.30 | **RECHECK** | Suspiciously large edge — your input is probably wrong |

The **>0.30 RECHECK gate** is the operational humility rule. A quarter-bit-of-information edge over a liquid market is enormous. If the model says you have it, the most-likely explanation is a model bug; the second-most-likely is the market is pricing news you haven't seen.

### Worked example

Market: "Will Fed cut rates in September 2026?"
- Your model: 60% (0.60)
- Market price: 45¢ (0.45)

```
KL(0.60 || 0.45) = 0.60 · log₂(0.60/0.45) + 0.40 · log₂(0.40/0.55)
                 ≈ 0.60 · 0.415 + 0.40 · (−0.459)
                 ≈ 0.249 − 0.184
                 ≈ 0.065 bits
```

→ falls in the **0.05–0.10 WEAK** bucket. Small position on YES (you think market is underpricing).

### Combining with Poisson signal

The KL formula doesn't require a Poisson-shaped probability. You can compute KL between **any** subjective probability and any market implied probability. In practice for Cemini:

- Poisson markets → use Poisson formula to get `p_mine`, then KL against `p_market` for sizing
- Non-Poisson markets → use whatever calibrated model produces `p_mine`, KL is the universal sizing primitive

### Cemini relevance

- **Universal triage filter** at Conductor level: any Polymarket signal can be pre-scored against the bits-of-edge gate before consuming downstream compute.
- **Quarter-Kelly compatible**: multiply KL-bucket by quarter-Kelly fraction for the final position size.
- **Insider detection sub-pattern**: rolling Shannon entropy of price series → 3σ collapse → see `@concepts/insider-detection-entropy-collapse.md`.

## Snippets

> "KL < 0.05: skip. 0.05–0.10: weak. 0.10–0.20: trade. > 0.30: recheck — if you think you have this much edge over the market, you're probably wrong." [Source: @de1lymoon.docx, paraphrased]

## Dead Ends

- **Trusting >0.30 bits of edge without verification** — the RECHECK gate exists for a reason. The default response to a giant edge is "find the bug in my model first."
- **Treating KL as an entry price** — KL is sizing-only. Entry price comes from the market's bid/ask + slippage budget; KL tells you how much to put on.
- **Using KL where the two distributions aren't really probability statements** — KL requires both inputs to be valid probabilities (0 < p < 1). Edge cases (p = 0 or p = 1) blow up the log; clip to ε.
