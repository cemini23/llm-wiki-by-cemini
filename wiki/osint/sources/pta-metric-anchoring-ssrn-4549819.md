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
  - concepts/high-signal-paper-patterns.md
  - sources/lob-regime-detection-hiremath-2026.md
  - meta/internal-benchmark-deployment-map.md
  - meta/pta-backtest-cadence.md
maturity: validated
read_status: skimmed
created: 2026-04-29
updated: 2026-05-29
clusters: [quant-finance]
---

## Relations

- @sources/4-5-links-2.md — K9 canonical source where this paper was promoted (Document 11 of 12); K9 framed it as a quant-paper-to-Cemini-adoption candidate paralleling the Schadner BSIV path
- @sources/black-scholes-iv-explicit-schadner-2026.md — peer Cemini quant-paper adoption candidate (Wave 3 Adopt-Cemini-Wiki-Workflow). Both follow the same "laptop-side empirical reproduction → brief to cemini-prod" adoption pattern
- @concepts/options-derivatives.md — adjacent concept hub; PTA is an equity/cross-sectional metric rather than options-specific but shares the cross-sectional-returns framing
- @concepts/quant-finance.md — primary cluster hub for quantitative-finance research in the Cemini corpus
- @concepts/ip-sale-readiness.md — multi-factor models with peer-reviewed academic alpha factors are valuation positives during IP-sale technical due diligence
- @entities/infrastructure/timescaledb.md — prescribed implementation surface (continuous aggregate over `public.klines` hypertable handles the rolling 52-week-high/low calculation natively)
- @meta/internal-benchmark-deployment-map.md — **where PTA/backtests run** (laptop compute + librarian data; never prod/egress)
- @meta/pta-backtest-cadence.md — pilot cadence + command

## Raw Concept

- **URL**: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4549819`
- **Title** [CORRECTED 2026-05-17 from SSRN]: "Predicting Cross-Sectional Return Variation in Past-Winner Stocks and Past-Loser Bonds with a Stock's 52-week Price Anchor" (paper introduces the PTA metric — price-to-52-week-anchor — as a cross-sectional return predictor). K9's rendering ("Predicting Stock Returns of Past-Winner Stocks and Bond Returns") was a paraphrase, not the verbatim title.
- **Authors** [CONFIRMED 2026-05-17 via SSRN]: Chen Chen, Sounak Saha, Mobina Shafaati, Licheng Sun (Old Dominion University); Chris T. Stivers (University of Louisville, corresponding author)
- **Type**: Academic working paper (SSRN); 75 pages; 53 references
- **License**: SSRN academic-paper terms (extract math + paraphrase findings into Cemini documentation; do not redistribute the paper itself; standard academic fair-use)
- **Vintage** [CORRECTED 2026-05-17]: SSRN posted 2023-08-24, last revised 2024-05-24, date-written 2024-06-04. **This is a 2023/2024 working paper — NOT a "2026 publication"** as K9 framed it. The "cutting-edge 2026 publication" claim is retracted.
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

### Deployment + pilot (2026-05-29)

- **Run:** laptop — `bash scripts/run_pta_backtest.sh`
- **Data:** cemini-librarian ArcticDB `equity_bars` via SSH (same path as equity momentum lab)
- **Never:** cemini-prod or cemini-egress-fi
- **Report:** `.local/reports/pta-pilot-2026-05-29.md`

**Pilot result (simplified quintile replication, 7 symbols, daily bars through ~2017-11):**

| Window | High−low PTA quintile spread (past winners, 21d fwd) |
|--------|-----------------------------------------------------|
| 252d (52w) | **−0.16%** (wrong sign vs paper) |
| 52d micro | **−0.22%** (wrong sign) |

Verdict: **`[TENTATIVE 2026-05-29]`** — pilot executed on correct surfaces; **does not replicate paper direction** on stale ArcticDB slice. Block MAPPO/TimescaleDB adoption until fresher equity history + paper-exact past-winner horizon. See @meta/internal-benchmark-deployment-map.md.

### Open questions

- **`[CONFIRMED 2026-05-29]`** — SSRN 4549819 abstract + JBF 2026 publication confirm PTA = **price-to-52-week-anchor** blending 52-week high **and** low (not PTH-only); high-PTA past-winners outperform low-PTA past-winners; bond leg on past-loser firms. K9's core summary holds; transaction-cost / sample-period caveats remain in full paper.
- **`[TENTATIVE 2026-05-29]`** — Empirical reproduction on Cemini librarian slice — pilot **negative** quintile spread (see above); inconclusive reject pending fresher data / methodology match.
- **`[TENTATIVE 2026-05-29]`** — 52-day micro-anchor — pilot **negative** spread on same slice; no evidence signal preserves at shorter horizon here.
- **[CONFIRMED 2026-05-17]**: Author identity / institutional affiliation / provenance — verified via SSRN abstract page (Exa crawl 2026-05-17). Authors: **Chen Chen, Sounak Saha, Mobina Shafaati, Licheng Sun** (Old Dominion University — Strome College of Business) and **Chris T. Stivers** (University of Louisville, Finance Dept — corresponding author). Exact title: *"Predicting Cross-Sectional Return Variation in Past-Winner Stocks and Past-Loser Bonds with a Stock's 52-week Price Anchor."* JEL G11/G12/G14; 75 pages; 53 references; 274 downloads. **K9 vintage correction**: posted 2023-08-24, last revised 2024-05-24, date-written 2024-06-04 — this is a **2023/2024 working paper, NOT a 2026 publication**. The "2026 publication" framing in K9 (and propagated into this page's `Vintage` field + `Snippets`) is [RETRACTED 2026-05-17] — see correction below. The abstract also confirms the metric covers **past-WINNER stocks AND past-LOSER corporate bonds** (the bond leg was abstracted away by K9's stock-only summary).

## Snippets

> "This 2026 academic paper introduces a novel metric called the price-to-52-week-anchor (PTA), which quantifies the expensiveness of a stock relative to its 52-week historical highs and lows. The study proves that PTA predicts significant cross-sectional variation in short-term returns; specifically, past-winner assets with a high PTA strongly outperform those with a low PTA due to investor cognitive bias and valuation uncertainty." [Source: 4_5 links 2.docx Document 11 para 274] — **[RETRACTED 2026-05-17: "2026 academic paper" is wrong. SSRN 4549819 was posted 2023-08-24, last revised 2024-05-24. K9's "2026 publication" framing is the source of the error. Verbatim SSRN abstract is in the snippet below.]**

> **Verbatim SSRN abstract** (Exa crawl 2026-05-17): "We show that the expensiveness of a stock's price, relative to its 52-week price history (or price-to-52-week-anchor, PTA), predicts a striking cross-sectional variation in both the stock returns of past-winner stocks and the corporate bond returns of past-loser stocks. The stock returns for past-winner stocks with a high PTA strongly outperform past-winner stocks with a low PTA. And, the corporate-bond returns of firms with high-PTA, past-loser stocks strongly outperform those with low-PTA, past-loser stocks. These PTA patterns are stronger for securities that likely have higher valuation uncertainty. Our new 52-week price-anchor metric equally uses information in both a stock's price-to-52-week-high ratio and its price-to-52-week-low ratio." [Source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4549819 (retrieved 2026-05-17)]

> "The Continuous Aggregate Materialized View pattern is required to compute this metric efficiently. The PTA requires tracking rolling 52-week highs and lows. In the Cemini architecture, this maps perfectly to TimescaleDB. Instead of loading millions of rows into Python memory to calculate the anchor, a continuous aggregate policy is deployed on the public.klines hypertable." [Source: 4_5 links 2.docx Document 11 para 276]

> "By injecting the PTA scalar, the topological Jones polynomial coefficient, and the adverse selection friction metric into the 34-dimensional MAPPO feature vector, the system creates a deeply synthesized, multi-disciplinary alpha factor encompassing behavioral bias, structural topology, and market microstructure." [Source: 4_5 links 2.docx Document 11 para 278]

> "The metric requires a 52-week price history. The current active data accumulation phase only holds ~5K BTC-USD rows and ~2.3K SPY rows. If these are minute or hourly bars, the system lacks the historical depth to calculate a true 52-week anchor. The time horizon must be scaled down (e.g., a 52-day or 52-hour micro-anchor) to fit the existing dataset." [Source: 4_5 links 2.docx Document 11 para 288]
