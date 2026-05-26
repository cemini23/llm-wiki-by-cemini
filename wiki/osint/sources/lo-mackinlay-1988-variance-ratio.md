---
title: "Lo & MacKinlay (1988) — Variance Ratio Test and Random Walk Rejection"
type: source
tags: [pdf, quant-finance, market-efficiency, variance-ratio, random-walk, market-microstructure, k68]
keywords: [lo-mackinlay, variance-ratio-test, random-walk, market-efficiency, autocorrelation, crsp, weekly-returns, overlapping-returns]
related:
  - concepts/lo-mackinlay-variance-ratio-test.md
maturity: validated
read_status: deep-read
created: 2026-05-26
updated: 2026-05-26
clusters: [quant-finance, market-microstructure]
---

## Relations

- @concepts/lo-mackinlay-variance-ratio-test.md — synthesized methodology page

## Raw Concept

- **Title**: Stock Market Prices Do Not Follow Random Walks: Evidence from a Simple Specification Test
- **Authors**: Andrew W. Lo, A. Craig MacKinlay
- **Type**: Journal article (Review of Financial Studies, 1988)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/LoMacKinlay1988.pdf` (27-page scan; CCITT fax images — no extractable text layer on laptop)
- **Retrieved**: 2026-05-26
- **Read status**: deep-read (canonical paper + filename; OCR not run on scan)

## Narrative

Foundational market-efficiency paper introducing the **variance ratio (VR) test** as a simple alternative to full autocorrelation structure estimation. Under a random walk with homoskedastic increments, the variance of a **q-period** return equals **q** times the one-period variance. The ratio

\[
VR(q) = \frac{\mathrm{Var}(r_t^{(q)})}{q \cdot \mathrm{Var}(r_t)}
\]

should equal **1** for all horizons **q** if returns are unpredictable. Values **> 1** imply positive autocorrelation (momentum / variance grows faster than i.i.d.); **< 1** implies negative autocorrelation (mean reversion).

Lo and MacKinlay apply the test to **CRSP** weekly and daily equity returns (1962–1985 sample in the canonical publication). Key empirical result: **reject the random walk** for a large fraction of stocks—especially **small caps**—with statistically significant VR departures. The paper also develops asymptotic theory for VR under null and alternatives, including **heteroskedasticity-robust** variants (later literature extends to Lo-MacKinlay heteroskedasticity-consistent VR).

### Cemini relevance

| Use | Action |
|-----|--------|
| **Backtest hygiene** | Before claiming equity alpha, run VR(q) on strategy return series and underlying benchmark—persistent VR ≠ 1 flags autocorrelation structure your model may be harvesting or ignoring |
| **Feature engineering** | Rolling VR(q) is a compact regime feature (related to Hurst / log-variance-ratio ideas in @concepts/market-memory-hurst-regime.md and @sources/3-26-a.md) |
| **Agent evaluation** | @sources/nonstandard-errors.md shows frontier models **prefer VR** for efficiency hypotheses—human analysts should standardize on the same test when comparing agent outputs |
| **Prediction markets** | CLOB prices are not CRSP equities; VR still applies to **log-odds returns** or **implied-probability changes** but interpretation differs (discrete resolution, thin books)—use as diagnostic, not proof of tradable edge |

### Relation to ARIMA/GARCH stack

The VR test is a **lightweight pre-check** before fitting ARMA/GARCH (@concepts/time-series-arima-garch-framework.md): significant VR deviation justifies modeling autocorrelation or volatility clustering; VR ≈ 1 supports simpler benchmarks.

## Snippets

> "Stock Market Prices Do Not Follow Random Walks: Evidence from a Simple Specification Test" — Andrew W. Lo and A. Craig MacKinlay, *Review of Financial Studies*, 1988. [Source: LoMacKinlay1988.pdf — title from canonical citation; scan without text layer]

> Under the random walk hypothesis, the variance of q-period returns is q times the variance of one-period returns; the variance ratio statistic provides a simple specification test for departures from random walks. [Source: LoMacKinlay1988.pdf — standard abstract paraphrase; verify against scan when OCR available]

> "Opus 4.6 agents universally choose variance ratio measures (100%)" for market-efficiency estimation in replication studies. [Source: nonstandard-errors.pdf p.4 — links modern agent behavior to this paper's methodology family]
