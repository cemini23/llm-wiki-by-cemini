---
title: FanDuel NFL slate export — 2026-10-25 (509 players)
type: source
tags: [source, dfs, fanduel, nfl, cemini-dfs]
keywords: [FanDuel, DFS, NFL, salary, FPPG, player pool]
related: []
maturity: draft
created: 2026-10-25
updated: 2026-10-25
read_status: skimmed
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FanDuel NFL player list, 2026-10-25 EDT |
| Type | Platform export (CSV, 509 rows) |
| Source | FanDuel DFS lobby export |
| Inbox | `research to be indexed/osint/FanDuel-NFL-2026 EDT-10 EDT-25 EDT-135562-players-list.csv` |
| Slate ID | `135562` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/FanDuel-NFL-2026 EDT-10 EDT-25 EDT-135562-players-list.csv` |

## Narrative

A raw FanDuel player-pool export for one NFL slate. This is input data for CeminiDFS lineup construction, not a document with claims.

Columns: `Id`, `Position`, `First Name`, `Nickname`, `Last Name`, `FPPG`, `Played`, `Salary`, `Game`, `Team`, `Opponent`, `Injury Indicator`, `Injury Details`, `Tier`, `Roster Position`.

First rows, for shape only:

| Pos | Player | FPPG | Salary | Game |
|-----|--------|------|--------|------|
| RB | Jahmyr Gibbs | 29.24 | 9800 | GB@DET |
| RB | Bijan Robinson | 20.75 | 9400 | SF@ATL |

### Value

The export carries `Salary` and `FPPG`, so a salary-per-point ranking needs no external join. `Injury Indicator` and `Injury Details` are present but empty in this file.

`[TENTATIVE]` One slate. It is not a season series and supports no backtest on its own. CeminiDFS needs a slate history before this column set is useful for anything but same-day lineups.

## Snippets

```
Id,Position,First Name,Nickname,Last Name,FPPG,Played,Salary,Game,Team,Opponent,Injury Indicator,Injury Details,Tier,,,Roster Position
135562-129368,RB,Jahmyr,Jahmyr Gibbs,Gibbs,29.23999938964844,5,9800,GB@DET,DET,GB,,,,,,RB/FLEX
```

## Dead Ends

- Treating a single slate export as a dataset. It is one date of one platform.
