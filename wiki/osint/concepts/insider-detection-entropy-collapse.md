---
title: "Insider Detection via Entropy Collapse (3σ Heuristic)"
type: concept
tags: [concept, polymarket, insider-detection, anomaly-detection, shannon-entropy, single-source-tentative, research-candidate]
keywords: [insider-detection, entropy-collapse, 3-sigma-drop, rolling-shannon-entropy, detect-insider-activity, news-cross-reference, anomaly-signal]
related:
  - sources/de1lymoon-three-formulas-2026-05.md
  - concepts/shannon-entropy-kl-divergence-prediction-markets.md
  - concepts/three-formula-system-polymarket-rare-events.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @sources/de1lymoon-three-formulas-2026-05.md — single-source origin of the heuristic
- @concepts/shannon-entropy-kl-divergence-prediction-markets.md — parent concept (same entropy primitive)
- @entities/platforms/polymarket.md — venue assumed

## Raw Concept

What this page answers: can a sudden collapse of rolling Shannon entropy in a Polymarket price series be used to detect insider trading? Single-source [TENTATIVE] heuristic from @de1lymoon — not yet backtested.

## Narrative

### The intuition

When a market is **uncertain**, its price oscillates between bid and ask — the Shannon entropy of the price series is **high**. When new information arrives that resolves the uncertainty, the price collapses to one side and stays there — entropy drops sharply.

If the entropy drop happens **without a corresponding public news event**, the most plausible explanation is **insider trading** — someone with non-public information is moving the price.

### The implementation

```python
import statistics

def detect_insider_activity(
    price_history: list[float],
    window: int = 12,
    threshold: float = 3.0,   # sigmas
) -> bool:
    """Watch rolling Shannon entropy; flag 3σ drops without news."""
    entropies = []
    for i in range(window, len(price_history)):
        slice_ = price_history[i - window : i]
        # bin into price-buckets, compute Shannon entropy of the empirical distribution
        h = _empirical_shannon(slice_)
        entropies.append(h)
    mean = statistics.mean(entropies)
    stdev = statistics.stdev(entropies)
    latest = entropies[-1]
    return (mean - latest) > threshold * stdev   # collapse, not spike
```

(`_empirical_shannon` discretizes the slice into N price buckets and applies the standard Shannon formula.)

### Threshold provenance

- **3.0 sigma drop**: chosen by the source operator; no published backtest cited
- **12-period window**: rule-of-thumb size, balances sensitivity (small window → noisy) vs latency (large window → late detection)

Both are **[NEEDS VERIFICATION 2026-05-13]** — heuristics, not validated parameters.

### The critical caveat — news cross-reference

A 3σ entropy collapse with **no news context** is the insider signal. A 3σ entropy collapse **with** news is just the market efficiently incorporating new information — that's not insider trading, that's normal price discovery.

The load-bearing piece is the **news cross-reference**. Without it, the heuristic flags every genuine market discovery as insider activity → false-positive rate too high to be useful.

### Suggested deployment pattern (Cemini-flavored)

1. **Detection layer**: run `detect_insider_activity` on rolling windows for each watched market
2. **Confirmation layer**: on every positive detection, query a news feed for events affecting the underlying within ±N minutes of the entropy drop
3. **Verdict**: flag insider candidate **only** if entropy collapsed AND no news event matched
4. **Action**: alert only — never auto-trade against suspected insider activity. Trading against insiders is trading against information you don't have.

### Why this is a research candidate, not a production signal

- **Single source** — only @de1lymoon's playbook describes the heuristic with these specific parameters
- **No backtest** cited — the 3σ / 12-period choices are operator intuition
- **News-feed integration** is the actual load-bearing component, and the source doesn't specify which feed or how to integrate it
- **Polymarket-specific quirks** may distort the signal: low-liquidity periods → entropy artificially low → false positives; near-resolution windows → entropy correctly collapses for non-insider reasons

### Cemini relevance

Good candidate for the **harmfulness-audit / trajectory harness** from the OpenSpec K37 work — replay historical Polymarket price series, classify which entropy collapses correspond to known news events vs unexplained, and back-out a calibrated threshold table.

If validated, becomes a defensive signal: **don't trade YES on a market that just showed unexplained entropy collapse** — the price already moved and you're trading against the insider.

## Snippets

> "detect_insider_activity(price_history, window=12, threshold=3.0): a 3σ drop in entropy without news is the insider signal." [Source: @de1lymoon.docx, paraphrased]

## Dead Ends

- **Treating entropy collapse as standalone signal** — without news cross-reference, false positives swamp true positives. The signal is `entropy_collapse AND NOT news`, not `entropy_collapse`.
- **Auto-trading against suspected insiders** — you're trading against information you don't have. The right action is "stay out," not "fade them."
- **Hardcoding 3σ / 12-period without backtest** — the parameters are operator heuristics. Treat as starting point for calibration, not production defaults.
