---
title: "PolyGnosis 2.0 — Polymarket anomaly + GDELT harness (arxiv 2605.25958)"
type: source
tags: [source, arxiv, polymarket, prediction-markets, gdelt, agent-harness, osint]
keywords: [polygnosis, perspective-mismatch, gdelt, websocket, clustering-agent, harness-engineering]
related:
  - entities/tools/polygnosis.md
  - entities/platforms/polymarket.md
  - entities/data-sources/gdelt.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-wallet-alpha-pipeline.md
  - concepts/sports-prediction-consensus-agent.md
  - "@gambling-wiki/sources/polygnosis-2-polymarket-osint-2026-06-01.md"
  - "@gambling-wiki/concepts/pm-perspective-mismatch-trading.md"
maturity: validated
read_status: deep-read
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @entities/tools/polygnosis.md — implementation stub + Cemini mapping
- @entities/data-sources/gdelt.md — Keywords Agent media pull
- @entities/platforms/polymarket.md — anomaly alert + CLOB surface
- @gambling-wiki/sources/polygnosis-2-polymarket-osint-2026-06-01.md — retail wagering framing (do not duplicate narrative)
- @gambling-wiki/concepts/pm-perspective-mismatch-trading.md — “Perspective Mismatch” for bankroll discipline

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2605.25958](https://arxiv.org/abs/2605.25958) |
| **Authors** | Wang, Xu, Xian (CUHK / Evolution AI Lab) |
| **Retail mirror PDF** | `@gambling-wiki` → `raw-sources/arxiv-2605.25958-polygnosis-2-0.pdf` |
| **Code** | No public production repo cited in abstract — treat as **research harness** until author release |

## Narrative

### Pipeline (prod-relevant)

1. **Ingest** — Polymarket WebSocket / anomaly alerts (price shock, whale volume).
2. **Clustering Agent** — partition events for downstream agents.
3. **Keywords Agent** — GDELT query from cluster keywords.
4. **Analysis Agent** — score **Perspective Mismatch**: PM-implied direction vs global media direction vs alignment label.

**Alpha thesis:** narrative divergence between PM traders and GDELT media is a tradeable or research signal — not sportsbook CLV.

### Harness engineering (Cemini-relevant)

| Finding | Implication for agent stacks |
|---------|------------------------------|
| Divide-and-conquer partitioning | Multi-agent PM research needs explicit stage boundaries (cluster → keywords → analysis) |
| Unconstrained terminal reflection → logical drift | Prefer structured passes over open-ended “reflect” loops in conductor |
| Consensus bias across configs | Add deterministic validation on narrative alignment scores |
| Pareto accuracy vs latency/tokens | Budget tier for alert→research path (cf. `@entities/tools/revfactory-harness.md`) |

### Cemini integration map [TENTATIVE]

| PolyGnosis stage | Existing OSINT / Cemini surface |
|------------------|-------------------------------|
| PM price / whale alerts | `@entities/tools/polymarket-websocket-api.md`, wallet-alpha pipeline |
| GDELT pull | `@entities/data-sources/gdelt.md`, prod `gdelt_harvester` (see architecture briefs) |
| LLM analysis | Conductor + `lazy-tool` / DeepSeek brain — **not** a new venue executor |
| Order placement | **Out of scope** for PolyGnosis paper — route via `@entities/tools/polymarket-agents.md` if operator adopts |

**Verdict:** **REFERENCE** for alert→OSINT research workflows; **CONDITIONAL-GO** for automated trading only after ToS, latency, and GDELT lag tests. **NO-GO** as substitute for Kalshi sports fee/CLV math (`@gambling-wiki`).

## Snippets

> "Perspective Mismatches — the narrative divergence between Polymarket sentiment and global media flows — as high-alpha trading signals." [Source: arxiv:2605.25958 abstract]

> "Unconstrained terminal reflection actively induces logical drift." [Source: arxiv:2605.25958 §3.2 — paraphrase from gambling-wiki deep-read]

## Dead Ends

- Paper does not ship MIT reference implementation in repo — Phase-0 cannot clone a trading bot
- GDELT indexing lag vs sub-minute PM moves — live arb unlikely without custom news feed
