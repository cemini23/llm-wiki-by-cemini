---
title: "gabagool — Polymarket Arbitrage Bot (Steal-from)"
type: entity
tags: [tool, polymarket, prediction-markets, arbitrage, trading-bot, python, steal-from, k39]
keywords: [gabagool, polymarket, arbitrage, kalshi-adapter, risk-manager, yes-threshold, max-concurrent-arbitrages]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - entities/tools/cloddsbot.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 8)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@entities/tools/cloddsbot.md` — K38 Polymarket arbitrage bot pattern peer; together they form the **2nd-and-3rd Polymarket arb reference architecture** for Cemini's planned Kalshi adapter

## Raw Concept

- **Repo / URL** (per source brief): `github.com/strongca22-cpu/gabagool`
- **Tier (per source brief)**: **Steal-from**
- **License** (per source brief): MIT — pending Phase-0 verification (3rd-occurrence pattern: K36 finance-skills + K38 AI-Trader + K38 Readme.skill all had missing LICENSE files despite README claims)
- **Stack**: Python; Polymarket-specific API + wallet integration

## Narrative

Polymarket arbitrage bot — single-developer project. Eval brief recommends pattern extraction (not deployment) into Cemini's planned Kalshi ingestion + execution layer.

### Patterns to lift

1. **Python Risk Manager schemas** — extract structure, port to Kalshi adapter
2. **`.env` threshold parameters**: `yes_threshold`, `max_concurrent_arbitrages` — operational thresholds for arbitrage gating
3. **Arbitrage mathematical models** — core spread / mispricing detection logic (verify against CloddsBot's existing equivalents)

### Why not deploy

- Too tightly coupled to Polymarket API + wallet (Solana DeFi adapter pattern from CloddsBot, K38, is more generalizable)
- Single-dev maintenance bus-factor
- Cemini's strategic direction is **Kalshi-first** (regulated CFTC venue), not Polymarket — adapter logic must port across venues

### NEEDS VERIFICATION

- LICENSE file actually present in repo (per 3rd-occurrence pattern caution)
- Star count, contributor count, recency of last push
- Whether arbitrage math is novel or reproduces published Kelly-criterion / spread-arbitrage literature

### Phase-0 audit status

Not yet performed. Phase-0 priority MEDIUM — verify license + extract Risk Manager schemas as a pattern study for the Kalshi adapter; do not deploy.

[Source: Evaluating Project Links for Stacks.docx URL 8; retrieved 2026-05-11]
