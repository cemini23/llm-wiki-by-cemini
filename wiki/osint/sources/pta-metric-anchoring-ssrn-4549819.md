---
title: PTA Metric (price-to-52-week-anchor) — 2026 quant-finance paper SSRN 4549819
type: source
tags: [paper, quant-finance, ssrn, anchoring, momentum-continuation, behavioral-finance, cross-sectional-returns, timescaledb-continuous-aggregate, k9-promotion, mappo-feature-vector, cemini-adopt-candidate]
keywords: [pta-metric, price-to-52-week-anchor, anchoring-bias, ssrn-4549819, cross-sectional-returns, past-winner-stocks, valuation-uncertainty, timescaledb-continuous-aggregate, mappo-34-vector, momentum-continuation]
related:
  - sources/4-5-links-2.md
  - sources/black-scholes-iv-explicit-schadner-2026.md
  - concepts/options-derivatives.md
  - concepts/quant-finance.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/timescaledb.md
maturity: validated
read_status: skimmed
created: 2026-04-29
updated: 2026-04-29
clusters: [quant-finance]
---

## Relations

- @sources/4-5-links-2.md — K9 canonical source where this paper was promoted (Document 11 of 12); K9 framed it as a quant-paper-to-Cemini-adoption candidate paralleling the Schadner BSIV path
- @sources/black-scholes-iv-explicit-schadner-2026.md — peer Cemini quant-paper adoption candidate (Wave 3 Adopt-Cemini-Wiki-Workflow). Both follow the same "laptop-side empirical reproduction → brief to cemini-prod" adoption pattern
- @concepts/options-derivatives.md — adjacent concept hub; PTA is an equity/cross-sectional metric rather than options-specific but shares the cross-sectional-returns framing
- @concepts/quant-finance.md — primary cluster hub for quantitative-finance research in the Cemini corpus
- @concepts/ip-sale-readiness.md — multi-factor models with peer-reviewed academic alpha factors are valuation positives during IP-sale technical due diligence
- @entities/infrastructure/timescaledb.md — prescribed implementation surface (continuous aggregate over `public.klines` hypertable handles the rolling 52-week-high/low calculation natively)

## Raw Concept

- **URL**: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4549819`
- **Title (per K9)**: "Predicting Stock Returns of Past-Winner Stocks and Bond Returns" (paper introduces the PTA metric — price-to-52-week-anchor — as a cross-sectional return predictor)
- **Type**: Academic working paper (SSRN)
- **License**: SSRN academic-paper terms (extract math + paraphrase findings into Cemini documentation; do not redistribute the paper itself; standard academic fair-use)
- **Vintage**: 2026 publication per K9 framing ("a peer-reviewed, cutting-edge (2026 publication) metric")
- **Discovered via**: K9 deep-read of `4_5 links 2.docx` Document 11, 2026-04-29
- **Read status**: skimmed via K9 summary; abstract + introduction + methodology not yet read directly from SSRN. **Pre-Cemini-adoption gate**: laptop-side full-paper read + empirical reproduction (analogous to the Schadner BSIV path)

## Narrative

### What the paper claims (per K9 synthesis)

The paper introduces **PTA (price-to-52-week-anchor)**: a scalar metric quantifying a stock's "expensiveness" relative to its 52-week historical high (H) and low (L) prices. The formal definition (per K9 paragraph 274):

```
PTA = (current_price - L) / (H - L)
```

Where H = max price over trailing 52 weeks, L = min price over trailing 52 weeks. PTA ∈ [0, 1] — a stock at its 52-week low has PTA = 0; at its 52-week high, PTA = 1.

**Empirical claim**: PTA predicts cross-sectional variation in short-term returns. Specifically:
- Past-winner stocks (positive prior returns) with **high PTA** (near 52-week high) **outperform** past-winner stocks with low PTA
- The economic rationale (per the paper, paraphrased by K9): investors anchor on the 52-week high as a salient price level. When a stock breaks above prior highs, anchoring bias plus valuation uncertainty drives further momentum continuation.
- Practical interpretation: PTA is a momentum-continuation signal that correlates with — but is not redundant with — standard momentum factors

### Why K9 promoted it (Cemini relevance)

**Direct integration into the MAPPO 34-dimensional feature vector** (per K9 paragraph 278):

Cemini's reinforcement-learning architecture uses a 34-dimensional feature vector for state representation. K9 prescribes adding PTA as a new dimension alongside:
- Topological feature extraction (Jones polynomial coefficients from braided/knotted asset crossovers — per K8 + Cemini-internal corpus)
- Options market adverse-selection proxies (quote midpoint covariance — also from K8 corpus)

Combining these three (PTA + topological coefficient + adverse-selection proxy) creates a multi-disciplinary alpha factor: **behavioral bias + structural topology + market microstructure**.

**Implementation surface**: TimescaleDB continuous aggregate.

```sql
-- Conceptual prescription per K9 paragraph 276
CREATE MATERIALIZED VIEW public.rolling_52w_anchors
WITH (timescaledb.continuous) AS
SELECT
  symbol,
  time_bucket('1 day', ts) AS day,
  max(close) OVER w52 AS h_52w,
  min(close) OVER w52 AS l_52w
FROM public.klines
WINDOW w52 AS (PARTITION BY symbol ORDER BY ts RANGE INTERVAL '52 weeks' PRECEDING);

-- Then per-bar PTA computation in Python
-- pta = (current_close - l_52w) / (h_52w - l_52w)
```

The prescription is to offload the rolling-window calculation to the database layer (TimescaleDB native) rather than loading rows into Python pandas memory. This is a clean example of "the right tool for the job" — TimescaleDB excels at exactly this pattern.

### Cemini-fit (per K9 Document 11)

| Category | Fit | K9 reasoning |
|---|---|---|
| Cemini production stack | ✅ | Pure algebraic scalar requiring no external libraries (numpy + scipy + asyncpg already deployed). TimescaleDB infrastructure already in place |
| Wiki / librarian server | ✅ | Mathematical formula curated into a Markdown wiki page bolsters the LLM analyst's quant-finance reasoning context |
| Workflow (laptop) | ✅ | Standalone read for the developer's quant-research sessions |

The K9 disposition was triple-Adopt — second source in the corpus to hit Adopt-Cemini-Wiki-Workflow (the first was the Schadner BSIV paper from Wave 3).

### Pre-adoption gates (paralleling Schadner BSIV)

Before drafting a `briefs/<date>_pta-metric-cemini-adoption.md` for cemini-prod, the laptop-side reproduction protocol is:

1. **Read the SSRN paper directly** — verify K9's summary against the actual abstract + methodology + numerical results. K9's PTA formula `(P-L)/(H-L)` is plausible but not verbatim; confirm the paper's exact formulation.
2. **Empirical reproduction** — implement PTA computation in Python on a known historical dataset (e.g., SPY components 2020-2025). Replicate the paper's headline finding that high-PTA past-winners outperform low-PTA past-winners.
3. **Speedup verification (DB-side vs Python-side)** — compare TimescaleDB continuous aggregate vs naive Python rolling-window pandas implementation on Cemini-shaped data. Confirm the DB-side is materially faster.
4. **Multi-factor synthesis test** — combine PTA with the topological coefficient + adverse-selection proxy into the 34-dim feature vector. Verify no multicollinearity (PTA could be redundant with standard momentum if not carefully decorrelated).
5. **MAPPO retrain delta** — measure whether adding PTA to the feature vector improves out-of-sample reward. The metric is only worth integrating if it adds incremental signal beyond what's already captured.

### Practical concerns (per K9 paragraphs 287-288)

**Data depth constraint**: The metric requires a full 52-week price history. K9 notes Cemini's "active data accumulation phase" only holds ~5K BTC-USD rows and ~2.3K SPY rows. If those are minute or hourly bars:
- ~5K minute bars = ~3.5 days of trading (insufficient for any 52-period window)
- ~5K hourly bars = ~30 weeks of trading (still insufficient for 52 weeks)

K9 prescribes scaling down the lookback to fit available data — e.g., a 52-day or 52-hour micro-anchor. This is reasonable but means the metric tested in the paper at 52-week scale isn't strictly the metric Cemini deploys; the empirical generalization (does PTA work at shorter horizons?) is part of the laptop-side reproduction work.

### Pattern note

PTA is the **second** quant-paper-to-Cemini-stack-adoption candidate in the corpus, following Schadner BSIV (Wave 3). The shared pattern:
1. Workspace librarian surfaces the paper via wave-ingest pipeline
2. Laptop-side empirical reproduction confirms (or refutes) the paper's claim
3. Cemini adoption brief drafted only if reproduction passes
4. cemini-prod-side Claude Code session implements

This pattern is now templated. Future quant papers (e.g., if a future Wave surfaces a vol-surface model paper, a microstructure friction estimator, or a regime-detection methodology) follow the same flow.

### Open questions

- **[NEEDS VERIFICATION 2026-04-29]**: Read the SSRN paper directly — confirm K9's summary, get the exact PTA formulation, identify any caveats K9 may have abstracted away (e.g., transaction-cost adjustments, sample-period dependencies).
- **[NEEDS VERIFICATION 2026-04-29]**: Empirical reproduction — does the high-PTA-past-winner-outperformance finding hold on a known dataset (CRSP, Wharton WRDS, or Cemini's own historical Polygon equity data once data depth is sufficient)?
- **[NEEDS VERIFICATION 2026-04-29]**: Does scaled-down PTA (52-day or 52-hour micro-anchor) preserve the predictive signal, or does the signal decay?
- **[NEEDS VERIFICATION 2026-04-29]**: Author identity / institutional affiliation — establish provenance before treating the paper as institutional-grade. SSRN ID 4549819 implies recent vintage (~2026); confirm author + affiliation when reading the abstract.

## Snippets

> "This 2026 academic paper introduces a novel metric called the price-to-52-week-anchor (PTA), which quantifies the expensiveness of a stock relative to its 52-week historical highs and lows. The study proves that PTA predicts significant cross-sectional variation in short-term returns; specifically, past-winner assets with a high PTA strongly outperform those with a low PTA due to investor cognitive bias and valuation uncertainty." [Source: 4_5 links 2.docx Document 11 para 274]

> "The Continuous Aggregate Materialized View pattern is required to compute this metric efficiently. The PTA requires tracking rolling 52-week highs and lows. In the Cemini architecture, this maps perfectly to TimescaleDB. Instead of loading millions of rows into Python memory to calculate the anchor, a continuous aggregate policy is deployed on the public.klines hypertable." [Source: 4_5 links 2.docx Document 11 para 276]

> "By injecting the PTA scalar, the topological Jones polynomial coefficient, and the adverse selection friction metric into the 34-dimensional MAPPO feature vector, the system creates a deeply synthesized, multi-disciplinary alpha factor encompassing behavioral bias, structural topology, and market microstructure." [Source: 4_5 links 2.docx Document 11 para 278]

> "The metric requires a 52-week price history. The current active data accumulation phase only holds ~5K BTC-USD rows and ~2.3K SPY rows. If these are minute or hourly bars, the system lacks the historical depth to calculate a true 52-week anchor. The time horizon must be scaled down (e.g., a 52-day or 52-hour micro-anchor) to fit the existing dataset." [Source: 4_5 links 2.docx Document 11 para 288]
