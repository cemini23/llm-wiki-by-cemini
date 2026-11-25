---
title: "FanDuel salaries and player pool — NFL Week 10, 2026-11-15"
type: source
related:
  - sources/operator-dfs-slate-2026-11-15.md
  - sources/operator-dfs-recap-week10-2026-11-15.md
  - sources/operator-fanduel-salaries-2026-11-22.md
  - concepts/operator-nfl-slate-packet-workflow.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | FanDuel player list, contest 136490, NFL Week 10 |
| Author | FanDuel export, operator working file |
| Type | CSV, salary and injury export |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/nov14.csv` |
| Retrieved | 2026-11-25 |
| Slate date | 2026-11-15 |
| Read status | read |

## Narrative

### Contents

A FanDuel player pool export for the Week 10 Sunday slate, contest ID 136490. 500 player rows across 20 clubs and 10 games. Same column schema as the Week 11 file.

### Coverage

| Position | Rows |
|---|---|
| WR | 193 |
| TE | 115 |
| RB | 111 |
| QB | 64 |
| D (team defense) | 20 |

91 rows carry an injury indicator.

### Reuse value

Medium-high. This file is the salary input for the Week 10 recap. The recap case cites contest 136490 and 503 rows in its own copy of the same list, so the two should agree. They differ slightly in row count, which suggests this is a nearby snapshot rather than the exact file the recap used. Treat it as a fixture, not as the recap's source of truth. [TENTATIVE]

The recap page `operator-dfs-recap-week10-2026-11-15.md` records the scored results against that contest.
