---
title: OpenPatchLab polymarket-weather-trading-bot
type: entity
tags: [entity, tool, polymarket, weather-trading, defer, k63]
keywords: [openpatchlab, polymarket-weather, mit, k63]
related:
  - sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/tools/suislanchez-polymarket-kalshi-weather-bot.md
  - entities/tools/katbrink-polymarket-weather-trading-bot.md
maturity: draft
created: 2026-05-24
updated: 2026-05-28
---

## Relations

- @sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md — K63 URL 19 (eval UNAVAILABLE → MIT verified)
- @concepts/polymarket-weather-trading-strategy.md — weather bot cluster
- @entities/tools/suislanchez-polymarket-kalshi-weather-bot.md — K60 cross-venue reference

## Raw Concept

Eval marked **UNAVAILABLE**; `gh api` shows **MIT** + ~147★ (pushed 2026-05-16). **Defer Phase-0** — compare vs alteregoeth weatherbot + suislanchez before steal-from extract.

## Narrative

### Verdict: **NO-GO (404 — unavailable source)**

Do not batch-reject with K60 weather URL cluster. Phase-0: clone `/tmp/openpatchlab-weather-audit/`; diff Polymarket-only scan vs canonical MIT weatherbot.

### Phase-0 availability update (2026-05-28)

`gh api repos/<owner>/<repo>` now returns 404 for this repository. Treat prior eval/API metadata as stale.

**Verdict: NO-GO (unavailable source)** until repository is publicly reachable again.

## Snippets

> "Status: UNAVAILABLE" in eval — **superseded** by GitHub API verification 2026-05-24.
