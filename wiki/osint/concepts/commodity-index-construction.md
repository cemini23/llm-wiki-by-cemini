---
title: Commodity index construction — an index is an oil bet unless it is not
type: concept
related:
  - sources/substack-rss-moontower-2026-11-08-moontower-335.md
  - concepts/dispersion-trading.md
updated: 2026-11-10
---

## Raw Concept

What a commodity index actually holds, and what a risk-balanced alternative does differently. Prompted by the Moontower #335 summary of Bruno Schwalbach's work.

## Narrative

### The problem

The standard commodity indices are concentrated in energy by weight and even more by risk.

| Index | Energy weight | Share of risk from energy |
|---|---|---|
| S&P GSCI | over 50% in 2026 | about 85% historical |
| BCOM | capped at 33% per sector | about half |
| RICI | about 40% | not stated |

[Source: substack-rss-moontower-2026-11-08-moontower-335.md]

A sector weight cap does not cap risk, because energy is far more volatile than the other sectors.

### Variance drag

Arithmetic and geometric returns diverge.

- GSCI average annual return: **5.1%**
- GSCI compound annual return: **2.7%**

The gap is variance drag. A volatile, poorly diversified index gives up most of its arithmetic mean to compounding. [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

### The correlation structure

Across 26 commodity futures:

- average pairwise correlation **across sectors**: 0.14
- average pairwise correlation **within a sector**: 0.53

Low cross-sector correlation is real. It is the reason a risk-balanced construction has room to work.

### The alternative

**Balanced Commodity** as described:

- equal **risk** across six sectors, not equal capital;
- tilt toward markets that trend up;
- hold cash when every sector trends down;
- long-only, unlevered.

Backtest from 1996, after costs:

| Metric | Balanced Commodity | GSCI |
|---|---|---|
| Annual return | 8.2% | 2.8% |
| Maximum drawdown | 35% | 88.5% |
| Correlation to global equities | 0.29 | not stated |
| 2008 | +1.1% | not stated |
| 2022 | +7.5% | not stated |

[Source: substack-rss-moontower-2026-11-08-moontower-335.md]

### The honest failure case

From January to mid-October 2026:

- GSCI: **+60%**
- Balanced Commodity: **+16%**

A risk-balanced index must underperform when one sector rips. That is a property, not a defect.

### The design principle

The author's framing is the transferable part: **do not mix two allocation motives in one instrument**.

- If the goal is broad commodity exposure, buy a well-built index.
- If the goal is a strategic oil position, buy oil directly.

An index that quietly carries 85% of its risk in one sector serves neither goal. [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

### The roll-date wrinkle

RICI's distinguishing feature is not its weights. It is that its roll dates **front-run the much larger GSCI rolls**. That is a microstructure choice with a plausible return effect and no published attribution here.

## Snippets

> "Energy was over half of the S&P GSCI's weight in 2026 and has carried about 85% of its risk over history." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

> "The GSCI averaged 5.1% a year but compounded at 2.7%." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

> "If you're looking for broad exposure to commodities, you're looking for a well-constructed index." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

## Dead Ends

- **Using a sector weight cap as a risk control.** BCOM caps at 33% and still carries about half its risk in energy.
- **Expecting a risk-balanced index to keep up in an energy rally.** 2026 year-to-date was 16% against 60%.
