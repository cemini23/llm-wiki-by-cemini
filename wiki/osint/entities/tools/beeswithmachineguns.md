---
title: beeswithmachineguns (newsapps)
type: entity
tags: [tool, load-testing, pm-canary, k175, k202, context]
keywords: [AWS EC2 swarm, load test, Paramiko]
related:
  - sources/eval-url-revenue-and-project-analysis-2026-07-20.md
  - sources/eval-github-revenue-journalism-geo-2026-07-28.md
maturity: draft
created: 2026-07-20
updated: 2026-07-28
---

## Relations

- @sources/eval-url-revenue-and-project-analysis-2026-07-20.md — K175 Watch
- @sources/eval-github-revenue-journalism-geo-2026-07-28.md — K202 Context (cyber wiki)

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [newsapps/beeswithmachineguns](https://github.com/newsapps/beeswithmachineguns) |
| **License** | MIT [CONFIRMED 2026-07-28] |
| **Stars / push** | ~6.6k★ · pushed 2024-03 [CONFIRMED] |
| **Verdict** | **NO-GO install (Context)** — K175 Watch reaffirmed; journalism batch Context only |
| **Routing** | Cybersec wiki historical load-test note; never GuruWatcher/Atto scrape |

### Phase-0 (2026-07-20)

| Field | Value |
|-------|-------|
| **Clone** | — (metadata only; no shallow clone) |
| **SPDX** | MIT [CONFIRMED] |
| **Verdict** | **NO-GO install** |
| **Risk** | Aging AWS swarm wrapper — accidental self-DoS / bill / ToS risk |

Report: `.local/reports/k175-phase0-2026-07-20.md`.

## Snippets

> EC2 micro-instance swarm for coordinated load tests. [Source: @sources/eval-url-revenue-and-project-analysis-2026-07-20.md]
