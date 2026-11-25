---
title: Operator NFL slate packet workflow — DFS and parlay desks
type: concept
maturity: draft
related:
  - sources/operator-dfs-slate-2026-11-22.md
  - sources/operator-dfs-slate-2026-11-15.md
  - sources/operator-parlays-slate-2026-11-22.md
  - sources/operator-parlays-slate-2026-11-15.md
  - sources/operator-dfs-recap-week10-2026-11-15.md
  - sources/operator-parlays-recap-week9-2026-11-08.md
  - sources/operator-fanduel-salaries-2026-11-22.md
  - sources/operator-fanduel-salaries-2026-11-15.md
  - concepts/parlay-market-making.md
updated: 2026-11-25
---

## Raw Concept

Question this page answers: how does the operator build a read-only NFL slate packet, and which rules are stable enough to ship?

Built from eight operator working files covering NFL Weeks 9 to 11 (2026-11-08 to 2026-11-22): two DFS slate packets, two parlay slate packets, two salary exports, and two recaps.

## Narrative

### The packet

Every weekend the desk compiles a read-only packet before the games. It contains injuries, reserve lists, weather, starting-quarterback confirmation and a timed pre-lock checklist. It contains no lineups, no projections and no bets. The packet is a gate, not a forecast. [Source: 11.21dfs.docx, 11.21parlays.docx]

### Slate construction

Two schedule sources: NFL.com and the ESPN scoreboard API. Kicks are reconciled in code. Differences are logged, not averaged. The Week 11 packet shows the correct handling of a week-label conflict: the task text said Week 12, but both sources placed 22 November in Week 11, so the packet used Week 11.

### Injury status

The NFL.com designation is primary. The ESPN feed is a second read. Where ESPN is stricter, the row keeps the NFL.com token and is labelled CONFLICT with both readings. This is the right pattern: it preserves the primary source and makes the disagreement visible.

Hard-exclude tokens: Out, IR, inactive, Doubtful, NFI, PUP, suspended. Questionable, limited and DNP are flagged but kept.

### Starting quarterbacks

Two confirmation tiers:

| Tier | Rule |
|---|---|
| CONFIRMED | Two agreeing sources |
| CONFIRMED_CLUB_NEWS | Official club news overrides the depth chart |
| CLAIMED | Single source only |

The parlay packet reached 19 of 20 CONFIRMED. The DFS packet for the same week had 20 of 20 CLAIMED, because its cache held no second source. The gap is a data-plumbing issue, not a method difference, and it shows the tiering works.

Every listed backup is a hard exclude.

### Weather

NWS hourly forecast at the kickoff instant, with Open-Meteo as a second read. Roof type comes from a static stadium table: open and retractable are exposed, dome and semi-open are not. When two products from the same provider disagree, the packet shows both and does not pick one. Wind at or above 10 mph adds a review note; the leg stays.

### The T-90 checklist

Timed per window: about 90 minutes before each kick. It re-runs the starting-QB check, re-runs the inactives diff, confirms the named never-enter players, and rechecks the CONFLICT rows. Displayed prices are read by the operator only; the packet holds no price.

### Recaps

The recaps keep two things apart: cash P&L and model-fair units. Paper tickets carry zero stake, so cash P&L is zero by construction. The recap records leg-level citations to the official box score and play-by-play, and labels players with no box line rather than imputing a score. The Week 10 DFS recap pins the scoring-code hash so a scoring change cannot pass silently.

### Transferable rules

1. Two schedule sources, reconciled in code, disagreements logged.
2. Primary injury source keeps its token; stricter secondary read is labelled CONFLICT.
3. Starting-QB tiers with a hard exclude on backups.
4. Weather from two reads, with a static roof-exposure table.
5. Recap separates cash from model-fair and labels missing data.

These rules are what the CeminiDFS and CeminiParlays pipelines should encode. The individual leans expire with each slate.

### Gaps

- [OPEN QUESTION 2026-11-25] The DFS packet and the parlay packet compute starting-QB confirmation separately. One shared cache would remove the CLAIMED-versus-CONFIRMED gap.
- [OPEN QUESTION 2026-11-25] The recap has no contest rank or cash line, so it cannot score lineup quality, only within-portfolio rank.
