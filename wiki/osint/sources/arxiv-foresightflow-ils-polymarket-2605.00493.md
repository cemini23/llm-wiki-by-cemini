---
title: "ForesightFlow — Information Leakage Score for prediction markets (arXiv:2605.00493)"
type: source
tags: [source, arxiv, polymarket, prediction-markets, informed-trading, market-microstructure, k59]
keywords: [foresightflow, information-leakage-score, ils, deadline-ils, brier-score, polymarket, mnpi, wallet-forensics, nechepurenko]
related:
  - concepts/prediction-market-information-leakage-score.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/polymarket-bot-architecture.md
  - sources/arxiv-polymarket-fill-side-2605-11640.md
  - sources/polymarket-microstructure-anatomy-2604.24366.md
  - entities/tools/polymarket-insider-tracker.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
read_status: read
---

## Relations

- @concepts/prediction-market-information-leakage-score.md — primary synthesis (ILS / deadline-ILS)
- @concepts/polymarket-microstructure-findings.md — microstructure + informed-flow context
- @concepts/polymarket-copy-trading-strategy.md — wallet surveillance complements copy-trading adversary model
- @concepts/polymarket-bot-architecture.md — detection features for bot/risk layers
- @sources/arxiv-polymarket-fill-side-2605-11640.md — empirical non-retail flow tiers
- @sources/polymarket-microstructure-anatomy-2604.24366.md — LOB anatomy baseline
- @entities/tools/polymarket-insider-tracker.md — commercial post-hoc trackers vs forward ILS

## Raw Concept

- **Title**: ForesightFlow: An Information Leakage Score Framework for Prediction Markets
- **Author**: Maksym Nechepurenko (Devnull FZCO)
- **Type**: arXiv preprint v2 (May 15, 2026) — arXiv:2605.00493
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.00493_foresightflow-ils-polymarket.pdf`
- **Retrieved**: 2026-05-23 (K59 Tier-2 sweep `@sweeps/2026-05-23.md`, Tier-A)
- **Read status**: read (41 pp)

## Narrative

Methodological paper + open artifacts for **quantifying informed flow** on Polymarket-class markets before resolution. Core label: **Information Leakage Score (ILS)** — fraction of terminal information move priced in **before** public news at `T_news`, with clean link to **Murphy decomposition of Brier score**.

**Scope conditions (original ILS):** event-resolved binaries with substantive uncertainty at open; article-derived (not proxy) news timestamps; anchor-sensitivity robustness. Pilot negatives: proxy `T_news` fails to separate event vs control markets; high ILS on high-consensus markets can be formula edge; wallet-level features needed beyond ILS alone.

**Deadline extension:** documented insider cases skew to **“by date Y?”** contracts → **deadline-ILS** anchored to underlying event time + category hazard baselines.

**Microstructure layer:** adapts PIN, VPIN, Kyle λ to discrete binary CLOB; adds **wallet-novelty** composite (age, participation, funding concentration, entry timing). Category priors focus monitoring on military/geopolitical, corporate disclosure, regulatory markets; sports/weather/elections as controls.

**FFIC inventory:** eight public suspected-insider episodes (CC-BY-4.0); code at github.com/ForesightFlow. Companion population paper cited (2605.00459) for large-scale audit — not ingested this batch.

**Cemini posture [TENTATIVE]:** reference methodology for **pre-resolution surveillance** and research briefs; not wired to prod without label pipeline + news timestamp QA. Pairs with @concepts/regime-conditioned-evaluation.md discipline when backtesting “edge” from early movers.

## Snippets

> "We introduce the Information Leakage Score (ILS), a label generator that quantifies how much of a market's terminal information move was priced in before the corresponding public news event." [Source: 2605.00493_foresightflow-ils-polymarket.pdf p.1]

> "Documented cases are systematically deadline-resolved … We accordingly extend the score to a deadline-ILS variant anchored to the underlying event timestamp." [Source: 2605.00493_foresightflow-ils-polymarket.pdf p.1]

> "Real-time detection requires that the relevant features … can be computed from information available before resolution." [Source: 2605.00493_foresightflow-ils-polymarket.pdf p.4]
