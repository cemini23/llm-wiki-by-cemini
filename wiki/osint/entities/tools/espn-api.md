---
title: espn-api — Python ESPN Fantasy API wrapper
type: entity
tags: [entity, tool, dfs, nfl, k138]
keywords: [espn-api, cwendt94, ESPN Fantasy, MIT, CeminiDFS, fetch]
related:
  - sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/sportsdataverse-py.md
  - sources/github-nfl-repo-eval-cemini-2026-06-21.md
maturity: draft
created: 2026-07-01
updated: 2026-07-01
---

## Relations

- @sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md — K138 Adopt row
- @entities/tools/sportsdataverse-py.md — complementary nflverse/sportsdataverse fetch lane

## Raw Concept

K138 Phase-0 on [cwendt94/espn-api](https://github.com/cwendt94/espn-api) — MIT wrapper for ESPN's undocumented Fantasy v3 REST API.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `cwendt94/espn-api` |
| **License** | **MIT** (`gh api` 2026-07-01) |
| **Stars / pushed** | ~912★; pushed 2026-05-04 |
| **Stack** | Python |
| **Verdict** | **Adopt** — CeminiDFS fetch-stage module |
| **Steal** | League/Team/Player object model; SWID + `espn_s2` private-league auth |

**Gap filled:** normalized ESPN roster/projection ingress in Python for CeminiDFS pipeline vs brittle R scrapers (K138 Reject: FantasyFootballAnalyticsR).

**Risk:** ESPN endpoint stability undocumented `[NEEDS VERIFICATION 2026-07-01]`.

Brief: `../projects/CeminiDFS/briefs/2026-07-01_k138-espn-api-fetch-adopt.md`

## Snippets

> "MIT — actively maintained Python wrapper for undocumented ESPN Fantasy API." [Source: eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md URL 5 (retrieved 2026-07-01)]
