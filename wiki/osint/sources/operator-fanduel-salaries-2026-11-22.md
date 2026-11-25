---
title: "FanDuel salaries and player pool — NFL Week 11, 2026-11-22"
type: source
related:
  - sources/operator-dfs-slate-2026-11-22.md
  - concepts/operator-nfl-slate-packet-workflow.md
  - sources/operator-fanduel-salaries-2026-11-15.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | FanDuel player list, contest 136799, NFL Week 11 |
| Author | FanDuel export, operator working file |
| Type | CSV, salary and injury export |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/11.21fanduel` (CSV text, no extension) |
| Retrieved | 2026-11-25 |
| Slate date | 2026-11-22 |
| Read status | read |

## Narrative

### Contents

A FanDuel player pool export for the Week 11 Sunday slate, contest ID 136799. 500 player rows across 20 clubs and 10 games.

Columns: `Id`, `Position`, `First Name`, `Nickname`, `Last Name`, `FPPG`, `Played`, `Salary`, `Game`, `Team`, `Opponent`, `Injury Indicator`, `Injury Details`, `Tier`, `Roster Position`.

### Coverage

| Position | Rows |
|---|---|
| WR | 187 |
| TE | 114 |
| RB | 112 |
| QB | 68 |
| D (team defense) | 20 |

82 rows carry an injury indicator. `FPPG` is season points per game. `Played` is games played.

### Reuse value

Medium. This is the raw salary input the CeminiDFS projection and lineup tools consume. The file is a snapshot: salaries and injury tags change up to lock. Keep it as a fixture for parser tests and for backtesting salary-based ownership heuristics. Do not treat the injury tags as current.

This is the Week 11 file. Its Week 10 counterpart is `operator-fanduel-salaries-2026-11-15.md`. The schemas are identical, so one parser covers both.
