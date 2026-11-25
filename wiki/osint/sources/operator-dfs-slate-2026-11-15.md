---
title: "Operator DFS slate packet — NFL Week 10, 2026-11-15"
type: source
related:
  - concepts/operator-nfl-slate-packet-workflow.md
  - sources/operator-fanduel-salaries-2026-11-15.md
  - sources/operator-dfs-recap-week10-2026-11-15.md
  - sources/operator-dfs-slate-2026-11-22.md
updated: 2026-11-25
read_status: skimmed
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | FanDuel Sunday Million packet: NFL 2026 Week 10, Sunday Nov 15 |
| Author | Operator working file (CeminiDFS desk) |
| Type | Operator document, .docx, read-only slate packet |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/dfsslate.docx` |
| Retrieved | 2026-11-25 |
| Slate date | 2026-11-15 |
| Read status | skimmed (opening sections and tables) |

## Narrative

### What it is

The Week 10 version of the read-only DFS slate packet, for Sunday 15 November 2026. Same template as the Week 11 packet: injuries, reserve lists, weather, starting-QB confirmation and a T-90 checklist. No lineups or projections. Compiled Saturday 14 November 2026 at 8:10 AM ET, with the prior copy preserved. [Source: dfsslate.docx]

### Slate

A FanDuel salary CSV was available for this week, so the contest slate is the ten games in that file. The NFL.com Sunday daytime list has eleven games, including the Munich international game, New England at Detroit at 9:30 AM ET. The contest slate is ten of those eleven. SNF and MNF are excluded. Byes: Chicago, Denver, Philadelphia and Tampa Bay, confirmed by three independent counts.

### Data coverage

- Kick and venue reconciliation across NFL.com, ESPN and the salary CSV. Zero kick disagreements.
- Weather for exposed sites from NWS hourly plus Open-Meteo, with domes skipped.
- Injuries from the NFL.com Week 10 report, cross-checked against club pages and the ESPN injury feed.
- Starting-QB confirmation and a roster whitelist export.

### Reuse value

Medium. The Week 11 packet supersedes the template, but this file is the worked example where the salary CSV drove slate inclusion. That is the variant worth keeping: it shows how the packet changes when a contest file is present. The player rows expire after the slate.

Deliberately thin description: the file is a working packet, and its content is mechanical restatement of public injury and weather feeds, not analysis.
