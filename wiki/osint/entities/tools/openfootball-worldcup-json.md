---
title: openfootball/worldcup.json — CC0 fixture data
type: entity
tags: [tool, data, world-cup-2026, open-source, cc0, calendar, k82]
keywords: [openfootball, worldcup.json, fixtures, kickoff, calendar-guard]
related:
  - sources/world-cup-github-repo-eval-2026-05-29.md
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - entities/tools/world-cup-bot.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - sources/gemini-wc-tournament-phase-router-2026-05-30.md
maturity: validated
created: 2026-05-29
updated: 2026-06-06
---

## Relations

- @entities/tools/world-cup-bot.md — vendored copy at `data/worldcup2026-fixtures.json`
- @concepts/polymarket-sports-lp-operating-rules.md — T-6h–10h pre-kickoff cancel rule

## Raw Concept

Phase-0 **Steal-from** from K82 GitHub eval. Public-domain JSON for World Cup fixtures including **2026** (104 matches).

| Field | Value |
|-------|-------|
| Repo | [openfootball/worldcup.json](https://github.com/openfootball/worldcup.json) |
| License | **CC0-1.0** |
| Stars | ~245 (2026-05-29) |
| Last push | 2026-05-26 |

## Narrative

Used for **calendar guard only** — map team → next kickoff UTC → cancel LP inside `MIN_HOURS_BEFORE_KICKOFF`. Not used for pricing (Gamma/CLOB at runtime).

Vendored into public OSS:

```
cemini23/world-cup-bot/data/worldcup2026-fixtures.json
```

Refresh via curl documented in repo `data/DATA_ATTRIBUTION.md`.

K102 reaffirms [openfootball/worldcup](https://github.com/openfootball/worldcup) Football.TXT sibling — **CC0**; canonical ingest path remains **worldcup.json** for structured JSON calendar guard.

## Snippets

> 104 group-stage + knockout fixtures with `date`, `time` (e.g. `13:00 UTC-6`), `team1`, `team2`. [Source: worldcup2026-fixtures.json vendored 2026-05-29]
