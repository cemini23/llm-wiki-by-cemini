---
title: "GitHub NFL / DFS repo evaluation — Cemini active-project batch (K125)"
type: source
tags: [docx, tool-evaluation, nfl, ceminidfs, license-audit, k125]
keywords: [tool-evaluation, nflverse, nfl-fantasy-football, NFL-Data, danmorse314, polymarket-sports-trading-bot]
related:
  - concepts/cemini-license-posture.md
  - concepts/active-project-research-routing.md
  - concepts/polymarket-bot-architecture.md
  - "@gambling-wiki/concepts/diy-nfl-dfs-model-architecture.md"
  - concepts/polymarket-bot-architecture.md
  - sources/cemini-tool-evaluation-plan-62url-2026-06-23.md
  - entities/tools/sportsdataverse-py.md
maturity: draft
read_status: deep-read
created: 2026-06-21
updated: 2026-06-23
clusters: [cemini-internal]
---

## Relations

- @concepts/cemini-license-posture.md — `gh api` overrides eval docx license claims
- @concepts/active-project-research-routing.md — CeminiDFS co-primary brief routing
- @gambling-wiki/concepts/diy-nfl-dfs-model-architecture.md — canonical CeminiDFS architecture

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | GitHub Repository Evaluation And Classification (NFL / DFS / PM sports bot cluster) |
| **Type** | Internal evaluation document (.docx) |
| **sha256** | `5b0e02c63189ccef87f0f6a33e46cea0f73abbec17774044c4006be6c85e09f4` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repository Evaluation And Classification.docx` |
| **Retrieved** | 2026-06-21 |
| **License spot-check** | `.local/reports/license-spot-check-2026-06-21-0901.txt` |
| **Read status** | deep-read + `gh api` spot-check on Adopt/Steal candidates |

## Narrative

Gemini DR eval of NFL fantasy / DFS / PM sports-bot GitHub URLs against Cemini active-project surfaces. **Eval systematically under-reports licenses** — batch `post_tool_eval_license.sh` required.

### Verified rollup (post-`gh api`)

| Repo | Eval tier | Verified license | Cemini verdict |
|------|-----------|------------------|----------------|
| `bbenbenek/nfl-fantasy-football` | Reference | **MIT** | REFERENCE — duplicates CeminiDFS fetch stage (Yahoo API); nflverse preferred |
| `hvpkod/NFL-Data` | Reference | **MIT** | REFERENCE — static 2015–24 CSV dump; backtest params only |
| `danmorse314/nfl-stuff` | Steal-from | **null** | **REFERENCE clean-room** — EPA edge-case R logic; no merge until SPDX |
| `thiagocavalheiro/polymarket-sports-trading-bot` | Reject | **null** | **REJECT** — Rust PM bot; unverified license on prod-touching surface |
| `maisymylod/nfl-moneyball` | — | **MIT** (spot-check) | REFERENCE — eval had null; MIT confirmed but not Adopt (overlap nflverse) |
| `nflverse/nfl_data_py` | — | **MIT** | Already canonical CeminiDFS ingest path |

### Reject / unavailable cluster

Majority of URLs **UNAVAILABLE** (network resolution failure during eval) or **null license** — no entity stub farm. Yahoo API wrappers (`MinaDo7a/yfs-api` TypeScript), ticketmaster monitors, best-ball scrapers: **Reject** (domain mismatch or no license).

### Cross-wiki routing

| Wiki | Action |
|------|--------|
| **Gambling-wiki** | Reference table for Yahoo-era fantasy scrapers vs nflverse |
| **OSINT-wiki** | This source page + CeminiDFS brief (EPA clean-room) |
| **PM bot** | `thiagocavalheiro/…` stays Reject — exploratory pm-kalshi bot uses Python CLOB stack |

**Posture:** No Adopt installs from this batch. CeminiDFS brief stages **EPA half-sack / tackle exclusion** clean-room audit against existing `nflverse` PBP pipeline.

## Snippets

> "The logic duplicates the fetch stage of the shipped CeminiDFS pipeline, which already standardizes on nflverse abstractions rather than raw Yahoo JSON handling." [Source: GitHub Repository Evaluation And Classification.docx URL 1 (retrieved 2026-06-21)]

> "Transcribing this corrected logic into Python extends the analytical accuracy of CeminiDFS stage 2 … blocked by the R runtime environment and the lack of a verified open-source license." [Source: same docx URL 9 danmorse314/nfl-stuff (retrieved 2026-06-21)]

## Dead Ends

- Installing Yahoo scrapers alongside nflverse — redundant fetch paths.
- Rust PM sports bot without license — cannot port to `/opt/cemini` regardless of latency appeal.
