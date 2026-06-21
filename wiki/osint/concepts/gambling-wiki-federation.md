---
title: Gambling wiki federation (cross-wiki)
type: concept
tags: [concept, meta, federation, gambling-wiki]
keywords: [gambling-wiki, sports-betting, dfs, ceminidfs, scope, routing]
related:
  - concepts/game-dev-wiki-federation.md
  - concepts/active-project-research-routing.md
  - "@gambling-wiki/entities/tools/ceminidfs.md"
  - "@gambling-wiki/concepts/diy-nfl-dfs-model-architecture.md"
  - concepts/kelly-sizing-quarter.md
  - concepts/favorite-longshot-bias.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/tools/momentum-odds.md
  - entities/tools/odds-jam-prediction-insiders.md
  - sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
maturity: validated
created: 2026-05-31
updated: 2026-06-20
---

## Relations

- @gambling-wiki/concepts/gambling-wiki-scope.md — scope boundary (primary)
- @game-dev-wiki/concepts/game-dev-wiki-scope.md — sibling federation wiki (K115)
- @gambling-wiki/concepts/prediction-markets-crossover.md — Kalshi/Polymarket retail lens
- @gambling-wiki/concepts/kelly-criterion-betting.md — general Kelly
- @concepts/kelly-sizing-quarter.md — quarter-Kelly bot default (osint primary)
- @concepts/favorite-longshot-bias.md — FLB PM monetization (osint primary)
- @entities/platforms/kalshi.md — execution/regulatory (osint primary)
- @entities/platforms/polymarket.md — bots/LP (osint primary)

## Raw Concept

Pointer hub for the public **@gambling-wiki** repo (`../projects/Gambling wiki/`). OSINT keeps automation; gambling-wiki keeps retail/strategy.

## Narrative

### Eval prompt (bulk URL batches)

Use `@ccc-wiki/concepts/deep-research-evaluation-prompt.md` (v7 body at CCC `prompts/deep-research-multi-wiki-eval-v7-2026-06-13.md`) — nine surfaces; **gambling-wiki** = surface 3 (retail betting/DFS vs OSINT bots). **game-dev-wiki** = surface 8.

### Split

| Topic | gambling-wiki | osint-wiki |
|-------|---------------|------------|
| Sportsbook / DFS / casino / poker | **Primary** | cross-link |
| **CeminiDFS** (NFL DIY pipeline) | **Primary** (`@gambling-wiki/entities/tools/ceminidfs.md`) | brief routing only |
| PM/Kalshi bots, LP, CeminiSuite | cross-link | **Primary** |
| WC physical-ticket resale alerts | cross-link (`@entities/tools/wc-ticket-monitor.md`) | entity + brief routing |
| Kelly, FLB (theory) | general pages | PM implementations |

### Shared pages to keep bidirectional

- `@gambling-wiki/concepts/kelly-criterion-betting.md` ↔ `@concepts/kelly-sizing-quarter.md`
- `@gambling-wiki/concepts/favorite-longshot-bias.md` ↔ `@concepts/favorite-longshot-bias.md`
- `@gambling-wiki/entities/platforms/kalshi.md` ↔ `@entities/platforms/kalshi.md`
- `@gambling-wiki/entities/tools/momentum-odds.md` ↔ `@entities/tools/momentum-odds.md`

### Ingest routing

Sources teaching **how to bet** → route stub to gambling-wiki. Sources teaching **how to deploy bots** → stay here. See `@gambling-wiki/meta/cross-wiki-routing.md`.

## Snippets

*(none)*
