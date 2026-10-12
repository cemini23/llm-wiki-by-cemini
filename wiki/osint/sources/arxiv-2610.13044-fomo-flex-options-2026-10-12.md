---
title: "FOMO: FLEX options and market outcomes (arXiv 2610.13044)"
type: source
tags: [source, k289, arxiv, options, volatility, quant, institutional-flow]
keywords: [fomo, flex-options, difference-in-differences, open-interest, iv-rv-spread, short-straddle, institutional-demand]
related:
  - concepts/k289-arxiv-wave.md
  - concepts/xsp-vol-regime-gates.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
read_status: read
---

## Relations

- @concepts/k289-arxiv-wave.md
- @concepts/xsp-vol-regime-gates.md

## Raw Concept

| Title | FOMO: FLEX Options and Market Outcomes |
| Authors | Shivesh Prakash (UC Berkeley Haas), Frank Ferstler, Nicholas Pezolano (Newmark Risk) |
| Type | arXiv preprint (q-fin.PR) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.13044-fomo-flex-options-and-market-outcomes.pdf` |
| Retrieved | 2026-10-12 |
| arXiv | 2610.13044v1 |
| read-status | read |

## Narrative

**FLEX options** are customisable, centrally cleared single-name options — the institutional instrument. This is the first direct event study of whether FLEX activity **leaks a measurable footprint** into the listed-option and equity markets.

### Method

**Matched-control difference-in-differences** with date fixed effects, using the **event-day IV-minus-realised-volatility spread** as a short-straddle execution-stress proxy. Data: **250 trading days (Mar 2025–Mar 2026), 41 underlyings, 53 event dates.**

### Results

- **Post-event listed-option open interest rises:** β = 0.3061, p = 0.0042 (BH p = 0.0168).
- **Selection into high-IV environments:** ATM IV premium β = 0.1235, p = 0.0030.
- The **IV − RV spread predicts short-straddle P&L** (β = 0.0366, p = 0.0100).
- **Short-lived equity effect:** CAR₀ difference **−0.85%**, p = 0.0442, decaying over 1–5 days.

### The conclusion

**FLEX is a marker of institutional vol demand, not a directional predictor.** That is the honest read — the footprint is in **open interest and the vol premium**, not in a tradeable equity drift.

### Why it matters here

A **measurable institutional-vol-demand signal** and a **short-straddle stress proxy** (the IV−RV spread) for the xsp lane. The event-study design (matched-control DiD on option OI) is reusable. **No trade, no scp.**

## Snippets

> "FLEX is a marker of institutional vol demand, not a directional predictor." [Source: arxiv-2610.13044-fomo-flex-options-and-market-outcomes.pdf]

> "Post-event listed-option open interest rises (β=0.3061, p=0.0042)." [Source: arxiv-2610.13044-fomo-flex-options-and-market-outcomes.pdf]
