---
title: beeswithmachineguns (newsapps)
type: entity
tags: [tool, load-testing, pm-canary, k175, watch]
keywords: [AWS EC2 swarm, load test, Paramiko]
related:
  - sources/eval-url-revenue-and-project-analysis-2026-07-20.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- @sources/eval-url-revenue-and-project-analysis-2026-07-20.md — K175 Watch

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [newsapps/beeswithmachineguns](https://github.com/newsapps/beeswithmachineguns) |
| **License** | MIT [CONFIRMED 2026-07-20] |
| **Stars / push** | ~6.6k★ · pushed 2024-03 [CONFIRMED] |
| **Verdict** | **NO-GO install (Watch)** — pm-canary stress-test idea; aging wrapper |
| **Routing** | pm-canary only if modernized |

### Phase-0 (2026-07-20)

| Field | Value |
|-------|-------|
| **Clone** | — (metadata only; no shallow clone this run) |
| **SPDX** | MIT [CONFIRMED] |
| **Verdict** | **NO-GO install (Watch)** |
| **Risk** | Aging AWS swarm wrapper — accidental self-DoS / bill risk |

Report: `.local/reports/k175-phase0-2026-07-20.md`.

## Snippets

> EC2 micro-instance swarm for coordinated load tests. [Source: @sources/eval-url-revenue-and-project-analysis-2026-07-20.md]
