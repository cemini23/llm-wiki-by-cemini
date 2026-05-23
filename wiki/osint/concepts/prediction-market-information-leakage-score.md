---
title: "Prediction-market Information Leakage Score (ILS / ForesightFlow)"
type: concept
tags: [concept, polymarket, prediction-markets, informed-trading, market-microstructure, forensics, k59]
keywords: [ils, deadline-ils, foresightflow, brier-score, informed-flow, mnpi, wallet-novelty, pin, vpin, kyle-lambda]
related:
  - sources/arxiv-foresightflow-ils-polymarket-2605.00493.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/polymarket-bot-architecture.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/regime-conditioned-evaluation.md
  - sources/arxiv-polymarket-fill-side-2605-11640.md
  - entities/tools/polymarket-insider-tracker.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
clusters: [polymarket, market-microstructure]
---

## Relations

- @sources/arxiv-foresightflow-ils-polymarket-2605.00493.md — K59 primary source (ForesightFlow, arXiv:2605.00493)
- @concepts/polymarket-microstructure-findings.md — LOB / final-hour dynamics context
- @concepts/polymarket-copy-trading-strategy.md — informed wallets as adversaries, not alpha sources
- @concepts/polymarket-bot-architecture.md — where detection hooks might live in stack
- @concepts/regime-conditioned-evaluation.md — backtests on “ILS edge” need per-regime reporting
- @sources/arxiv-polymarket-fill-side-2605-11640.md — non-retail tier signatures
- @entities/tools/polymarket-insider-tracker.md — post-hoc commercial analogues

## Raw Concept

K59 Tier-2 sweep ingest of **ForesightFlow** — a framework to label and detect **informed flow** on decentralized prediction markets using an **Information Leakage Score** tied to pre-news price moves vs terminal outcomes.

## Narrative

### ILS (event-resolved)

For a resolved binary market, ILS measures how much of the **terminal information** (outcome surprise) was already reflected in price **before** a verifiable public news timestamp `T_news`. Interpretation links to **proper scoring rules** (Murphy/Brier decomposition) — not just “price moved early.”

**Valid use requires:**
- Event-resolved (not spurious deadline-only without extension)
- Real uncertainty at market open
- High-quality `T_news` (article-derived > proxy anchors)
- Anchor robustness checks

### deadline-ILS extension

Public insider case studies concentrate on **“by date Y?”** markets. Extension anchors to **underlying event time** and uses **category-conditional hazard** baselines for time-to-event — aligns methodology with documented case population.

### Feature stack (detection-oriented)

| Layer | Content |
|-------|---------|
| Microstructure | PIN, VPIN, Kyle λ adapted to **discrete binary CLOB** |
| On-chain wallets | Novelty: age, prior markets, funding graph, entry vs resolution |
| Category priors | Focus: geopolitical/military, corporate MNPI, regulatory; controls elsewhere |

### vs existing corpus

| Approach | Timing | Cemini note |
|----------|--------|-------------|
| Post-hoc profit screens (Mitts-style) | After resolution | Not actionable live |
| @entities/tools/polymarket-insider-tracker.md | Ex-post dashboards | No ILS label |
| **ILS / ForesightFlow** | Label from history; features causal pre-resolution | Research / surveillance reference |

**Cemini posture:** CONDITIONAL-GO for **offline label generation + monitoring research** on Polymarket/Kalshi stacks — not a trading signal without independent validation. Do not conflate high ILS with illegal insider trading without legal context.

## Snippets

> "The gap between post-hoc identification and real-time detection is substantial." [Source: 2605.00493_foresightflow-ils-polymarket.pdf p.3]

> "ILS is interpretable only for event-resolved markets with substantive uncertainty at T_open, with article-derived rather than proxy-anchored news timestamps." [Source: 2605.00493_foresightflow-ils-polymarket.pdf p.1]
