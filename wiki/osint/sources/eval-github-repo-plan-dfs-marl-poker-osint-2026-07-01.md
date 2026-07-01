---
title: "GitHub Repository Evaluation Plan.docx — DFS / MARL / poker / OSINT batch (2026-07-01)"
type: source
tags: [tool-evaluation, dfs, marl, poker, osint, k138, docx]
keywords: [espn-api, draftfast, AI_pokergame, sportsbook-api, Live-Sports-Arbitrage, google-research-football, CastleSimWeb, gemini-deep-research]
related:
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/espn-api.md
  - entities/tools/draftfast.md
  - entities/tools/ai-pokergame.md
  - entities/tools/sportsbook-api-evangelist.md
  - sources/eval-github-repos-plan-multi-wiki-2026-06-29.md
  - sources/eval-poker-github-repos-2026-06-26.md
  - sources/tool-eval-metaplan-81url-2026-06-24.md
  - sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md
maturity: draft
read_status: read
created: 2026-07-01
updated: 2026-07-01
clusters: [wiki-tooling, dfs, poker, osint]
---

## Relations

- @entities/tools/espn-api.md — K138 Adopt (MIT; gh verified)
- @entities/tools/draftfast.md — K138 CONDITIONAL-GO (no SPDX on gh)
- @entities/tools/ai-pokergame.md — K138 Steal-from (MIT; gh corrected docx)
- @entities/tools/sportsbook-api-evangelist.md — K138 Steal-from (apis.json index)
- @sources/tool-eval-metaplan-81url-2026-06-24.md — prior draftfast Reference-only row

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | GitHub Repository Evaluation Plan (Gemini Deep Research RUNTIME v9) |
| **Type** | DOCX |
| **sha256** | `4e221300936df96cc3b98f32eee76241520d0bf188e72c74317d141648a3b2de` |
| **Batch theme** | DFS pipeline optimization, MARL, poker range analysis, OSINT sportsbook telemetry |
| **URLs** | 20 |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repository Evaluation Plan.docx` |
| **Retrieved** | 2026-07-01 |
| **Read status** | read (`gh api` on GitHub rows) |

## Narrative

K138 batch — **20 URLs** (sports data, DFS optimizers, poker AI, castle sim refs, arb scrapers).

### Tier distribution (docx + gh spot-check 2026-07-01)

| Tier | Count | Items |
|------|-------|-------|
| **Adopt** | 1 | cwendt94/espn-api (MIT) |
| **CONDITIONAL-GO** | 1 | BenBrostoff/draftfast (no LICENSE file on gh; docx Adopt downgraded) |
| **Steal-from** | 3 | PENEEEEE732/AI_pokergame (MIT), api-evangelist/sportsbook-api, personal-coding/Live-Sports-Arbitrage-Bet-Finder |
| **Reference-only** | 2 | jokecamp/FootballData (MIT), PodeCaradox/CastleSimWeb |
| **Defer** | 2 | google-research/football (Apache-2.0; TF1.15 debt), Kehom/GDotCSV2Json |
| **Reject** | 8 | statsbomb/open-data (NC UA), FantasyFootballAnalyticsR, RangeTrainer, poker-planning, MogekoCastle, cristianhosu/castle-builder, stdlib-js/blas-gdot, … |
| **UNAVAILABLE** | 4 | rucchettad/poker-range-viewer, ianmann56/CastleBuilder, mehpackers13/fanduel-bot, api-evangelist/fanduel |

### gh api corrections vs docx

| Repo | Docx license | Verified 2026-07-01 |
|------|--------------|---------------------|
| PENEEEEE732/AI_pokergame | NOT FOUND | **MIT** — steal posture unchanged; audit exploit logic before merge |
| BenBrostoff/draftfast | NOT FOUND | **No LICENSE file** — CONDITIONAL-GO not Adopt |
| cwendt94/espn-api | MIT | **MIT** confirmed (~912★) |

### Cross-wiki routing

| Wiki | Action |
|------|--------|
| **OSINT** | sportsbook-api apis.json; Live-Sports-Arbitrage arb-infra patterns |
| **Gambling** | espn-api + draftfast → CeminiDFS; FootballData static archive |
| **Game-dev** | google-research/football MARL defer; CastleSimWeb WebGPU reference brief |
| **Poker Arena** | AI_pokergame opponent heuristics steal |

**Prod:** no Adopt rows touch cemini-prod trading stack directly.

## Snippets

> "statsbomb/open-data — strict non-commercial user agreement — Reject for TipDrop/Cemini production." [Source: GitHub Repository Evaluation Plan.docx URL 3 (retrieved 2026-07-01)]

> "espn-api — MIT Python wrapper for undocumented ESPN Fantasy v3 endpoints." [Source: GitHub Repository Evaluation Plan.docx URL 5 (retrieved 2026-07-01)]
