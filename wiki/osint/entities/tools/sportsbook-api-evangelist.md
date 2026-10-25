---
title: sportsbook-api (api-evangelist) — apis.json sportsbook index
type: entity
tags: [entity, tool, osint, sportsbook, k138]
keywords: [api-evangelist, sportsbook-api, apis.json, Kalshi, Polymarket, FanDuel, DraftKings]
related:
  - sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md
  - sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md
  - concepts/polymarket-bot-architecture.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-01
updated: 2026-07-28
---

## Relations

- @concepts/wiki-tooling-evaluation.md — K198 backlink

- @sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md — K138 Steal-from row
- @sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md — arb infra landscape

## Raw Concept

K138 eval of [api-evangelist/sportsbook-api](https://github.com/api-evangelist/sportsbook-api) — curated **apis.json** / apis.yml index of US sportsbook and prediction-market endpoints.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `api-evangelist/sportsbook-api` |
| **License** | **NOT FOUND** |
| **Stars / pushed** | ~0★; pushed 2026-06-27 |
| **Stack** | JSON APIs catalog |
| **Verdict** | **Steal-from** — OSINT endpoint map only |
| **Steal** | Kalshi, Polymarket, FD, DK base URLs + auth parameter notes for discovery scripts |

**Not executable scraper** — intelligence chart for endpoint drift monitoring. Freshness vs live gateways unverified `[OPEN QUESTION 2026-07-01]`.

## Snippets

> "Maps real-time data ingestion pipelines across both traditional fiat sportsbooks and emerging blockchain/prediction markets." [Source: GitHub Repository Evaluation Plan.docx URL 11 (retrieved 2026-07-01)]
