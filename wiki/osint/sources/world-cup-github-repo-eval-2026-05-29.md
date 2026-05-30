---
title: "World Cup GitHub repo eval — Phase-0 (29 repos, K82 bot fit)"
type: source
tags: [source, github, phase-0, world-cup-2026, prediction-markets, k82]
keywords: [openfootball, worldcup.json, dexorynlabs, calendar-guard, lp-bot, steal-from]
related:
  - entities/tools/world-cup-bot.md
  - entities/tools/openfootball-worldcup-json.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md
maturity: validated
created: 2026-05-29
updated: 2026-05-30
---

## Relations

- @entities/tools/world-cup-bot.md — public OSS; adopted openfootball fixtures 2026-05-29
- @sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md — broader PM/agent landscape (K86); Phase-0 queue additions
- @entities/tools/openfootball-worldcup-json.md — CC0 calendar data (Steal-from)
- @concepts/world-cup-advance-market-bot-v1.md — v1 module map

## Raw Concept

| Field | Value |
|-------|-------|
| Title | User-supplied GitHub link batch (31 URLs, 29 unique) |
| Type | Phase-0 eval session |
| Retrieved | 2026-05-29 |
| Read status | deep-read (metadata + README + key files) |

User asked for Phase-0 fit vs **World Cup Bot** (conviction LP on PM advance markets). Method: GitHub API metadata, license check, README skim, pattern extract for top hits.

## Narrative

### Verdict summary

| Verdict | Count | Action |
|---------|-------|--------|
| **Steal-from** | 2 | Vendor CC0 fixtures; read Gamma fetch pattern from dexorynlabs |
| **Reference** | 8 | Lock-hour env patterns, ICS/API alternatives — no code adopt |
| **Reject** | 19 | 2018/2022 ML, office pools, SEO spam, no license |

**None** are drop-in LP bots. Canonical build remains `@entities/tools/world-cup-bot.md`.

### Steal-from (implemented 2026-05-29)

1. **[openfootball/worldcup.json](https://github.com/openfootball/worldcup.json)** — CC0-1.0, updated 2026-05-26, 245★. Vendored `2026/worldcup.json` → `cemini23/world-cup-bot` `data/worldcup2026-fixtures.json`. Powers **Module 5 calendar guard** (`world_cup_bot/calendar_guard.py`).

2. **[dexorynlabs-betting/2026-worldcup-prediction-market](https://github.com/dexorynlabs-betting/2026-worldcup-prediction-market)** — 102★, active 2026-05-29, **no LICENSE** (README: all rights reserved). `scripts/fetch-odds.ts` documents Gamma `?slug=` fetch for winner markets + sim-vs-PM edge UI. **Post-v1** optional conviction overlay — pattern only, not code copy.

### Reference (not adopted)

| Repo | License | Note |
|------|---------|------|
| openfootball/worldcup | CC0 | Football.TXT sibling of .json |
| onno101/worldcup-pool | Apache-2.0 | `PREDICTION_LOCK_BEFORE_KICKOFF_HOURS` |
| ionmx/worldcup-2026-pool | MIT | 10-min pre-kickoff pool lock |
| tylermachado/us-soccer-calendars | none | ICS WC 2026 — no LICENSE file |
| rezarahiminia/worldcup2026 | none | Hosted API; README claims ISC, no LICENSE on GitHub |
| manrajgrover/football-cli | MIT | football-data.org; WC league broken per README |
| cedricblondeau/*-cli-dashboard | MIT | 2018/2022 terminal UX only |
| jfjelstul/worldcup | none | Comprehensive WC DB — no license |

### Reject bucket

2018/2022 sklearn winner models, freeCodeCamp SQL tutorial, Firebase/Databricks office pools (`jjimenezgarcia`, `ErickIstea`), SEO-spam **mooncitydev**, mystic Poisson **mikobinbin**, static 2022 sites, empty stubs.

## Snippets

> "Your fork uses your `.env` and your keys only." — `@entities/tools/world-cup-bot.md` / repo SECURITY.md

> CC0 fixtures: `curl https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json` [Source: openfootball/worldcup.json README (retrieved 2026-05-29)]
