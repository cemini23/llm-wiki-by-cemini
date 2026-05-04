---
title: Klaassen-Magnus Elo — Tennis Win-Probability Model (MIT code, NC-data-coupled)
type: entity
tags: [financial-research, sports-prediction, prediction-markets, elo-ratings, mit, steal-from, license-trap]
keywords: [klaassen-magnus-elo, tennis-prediction, sports-prediction-markets, kalshi-tennis, polymarket-tennis, win-probability, hierarchical-markov, efron-morris-estimator]
related:
  - sources/5-4-links-tool-eval.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/5-4-links-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 3 (`jgollub1/tennis_match_prediction`), **Steal-from** tier verdict
- @concepts/cemini-license-posture.md — exemplar of pattern #4 (CC-BY-NC training-data contamination): code is MIT, data dependency is CC-BY-NC-SA, derivative-models inherit NC restriction unless retrained on commercially-licensed data

## Raw Concept

Klaassen-Magnus Elo is a tennis-specific Elo variant that beats traditional Elo and Barnett-Clarke models on win-probability prediction. Identified as **Steal-from-tier** in the 2026-05-04 Gemini DR eval — algorithm extracts cleanly under MIT license; data dependency (Jeff Sackmann's CC-BY-NC-SA tennis_atp dataset) blocks production deployment unless retrained on commercially-licensed feeds.

## Narrative

- **Source repo URL**: https://github.com/jgollub1/tennis_match_prediction
- **License**: MIT (code)
- **Data dependency**: Jeff Sackmann tennis_atp / tennis_slam_pointbypoint datasets — CC BY-NC-SA 4.0
- **Academic source**: 2021 Journal of Sports Analytics (https://content.iospress.com/articles/journal-of-sports-analytics/jsa200345)
- **Stack**: Jupyter Notebook 75.4%, Python 24.6%
- **Maturity**: 31 stars, 8 forks, 34 commits, 5 active PRs

### Performance benchmarks (2016 ATP data)

| Methodology | Accuracy | Log Loss |
|-------------|----------|----------|
| Barnett-Clarke | 64.6% | 0.663 |
| Barnett-Clarke + opponent-adjusted EM | 67.6% | 0.632 |
| **Klaassen-Magnus Elo** | **69.7%** | **0.594** |

The +5.1pp accuracy lift from baseline Barnett-Clarke to Klaassen-Magnus Elo is the load-bearing performance signal.

### Why Steal-from (not Adopt)

The Jupyter-notebook codebase is academic-grade, not production-grade — no headless API, no error handling for live data streams, no FastAPI/LangGraph integration. **Production deployment requires the math, not the code:**

1. Extract Klaassen-Magnus Elo formulation from notebooks
2. Refactor into pure Python module under `services/llm_analyst/quant_methods/`
3. Wrap as `@mcp.tool` decorator
4. Wire to commercially-licensed tennis data feed (NOT tennis_atp)

### License trap (pattern #4 in `@concepts/cemini-license-posture.md`)

The code is MIT — extract freely. But the *trained model weights* and *feature pipelines* derived from CC BY-NC-SA tennis_atp data inherit the NC restriction. To deploy in Cemini's commercial trading stack:

1. Implement the algorithm from MIT code (safe)
2. **Retrain weights from scratch using commercially-licensed tennis data** (Sportradar, Stats Perform, etc.)
3. Document the data-source provenance for IP-sale audit trail

Failing to retrain = NC license contamination of derivative models = M&A-due-diligence failure.

### Direct prediction-market relevance

Per user note 2026-05-04: Cemini's Kalshi + Polymarket scope covers sports markets. **Tennis match outcomes are an in-scope prediction-market vertical**, not a tangential reference. Klaassen-Magnus Elo is **the canonical tennis prediction model** in the academic literature. Adopting it (plus retrained on commercial data) gives Cemini a defensible edge on tennis prediction-market contracts.

This reframes the Gemini DR's "Steal-from with caveats" verdict: it's actually a high-priority adopt for tennis-prediction markets specifically, gated only on commercial-data licensing.

### Generalization

Klaassen-Magnus's variance-decomposition + opponent-adjustment approach generalizes beyond tennis. The mathematical pattern (Bayesian-weighted serve-performance estimator with hierarchical Markov dependence) transfers to any 1-on-1 binary-outcome contest:

- **Other sports prediction markets** — boxing, MMA, golf head-to-heads, esports duels (any tennis-shaped match contract)
- **Any binary-outcome two-party contest** — not just sports

### Action items

1. Stage `briefs/2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md` — math extraction + commercial data sourcing decision for the prod-server-side Claude session
2. License-audit checklist for retraining (data-source documentation, inference-pipeline isolation from NC sources)
3. Benchmark adapted version on Kalshi tennis contracts in shadow mode before live deployment

## Snippets

- **Performance benchmarks** (2016): "Methodology / 2016 Accuracy / 2016 Log Loss: Barnett-Clarke 64.6% .663; Barnett-Clarke opponent-adjusted EM 67.6% .632; Klaassen-Magnus Elo 69.7% .594" [Source: 5_4 links.docx URL 3]

- **Algorithmic stack**: "specifically leveraging the Klaassen-Magnus Elo method, Efron-Morris estimators, and hierarchical Markov Models." [Source: 5_4 links.docx URL 3]

- **Data-license caveat**: "the algorithms natively consume datasets provided by Jeff Sackmann, which are encumbered by the restrictive CC BY-NC-SA 4.0 license. To legally deploy these models within the commercial Cemini stack, the input pipelines must be entirely decoupled from the Sackmann datasets and rewired to consume proprietary or commercially licensed data feeds." [Source: 5_4 links.docx URL 3]

- **Recommendation tier (revised)**: "Steal-from. The Jupyter-centric runtime architecture is wholly inappropriate for a 24/7 automated FastAPI trading stack. However, the specific Klaassen-Magnus Elo implementation and Efron-Morris estimator design patterns yield quantifiable predictive performance advantages... These specific mathematical functions should be extracted, refactored into strict, type-hinted Python, and added to the quantitative utility modules in the Cemini codebase." [Source: 5_4 links.docx URL 3]
