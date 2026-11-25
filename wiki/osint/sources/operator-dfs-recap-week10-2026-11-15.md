---
title: "FanDuel Week 10 recap — 150 lineups, contest 136490"
type: source
related:
  - concepts/operator-nfl-slate-packet-workflow.md
  - sources/operator-dfs-slate-2026-11-15.md
  - sources/operator-fanduel-salaries-2026-11-15.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | FanDuel NFL Week 10 recap: Sunday 2026-11-15, contest 136490, 150 lineups |
| Author | Operator working file (CeminiDFS desk) |
| Type | Operator document, .docx, portfolio recap |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/week10recap.docx` |
| Retrieved | 2026-11-25 |
| Slate date | 2026-11-15 |
| Read status | read |

## Narrative

### What it is

A headless recap of 150 FanDuel lineups for contest 136490, Week 10. Built at 8:20 PM ET on 15 November 2026. Nothing was entered, submitted, swapped or signed in. [Source: week10recap.docx]

### Scoring integrity

All 150 lineups scored; none unresolved and none pending. Player IDs re-verified in the players list, with zero name mismatches. Team assignment taken from the ESPN box score, not the salary list, with zero disagreements.

The scoring code is the prior-week scorer, copied with I/O-only edits. The scoring source hash is recorded and matches the prior weeks, so the weights and two-point parsing are unchanged. Four rostered players had no ESPN box line and scored zero; those slots are labelled `NO_BOX_LINE`.

### Results

Score distribution over the 150 scored lineups: minimum 52.40, median 113.61, maximum 194.26.

Best players by points for lineup exposure of ten or more: Christian McCaffrey (SF) 47.30 in 35 lineups; George Pickens (DAL) 41.00 in 33; Dak Prescott (DAL) 38.42 in 14; Patrick Mahomes (KC) 38.42 in 26; Brock Purdy (SF) 34.66 in 24; Jaxon Smith-Njigba (SEA) 30.10 in 13.

Zero-point rows included Jordan Addison, David Montgomery and Omar Cooper Jr., all labelled `NO_BOX_LINE`.

### Portfolio construction

Heavy Dallas and San Francisco exposure, 90 of 150 lineups each, was the core. One roster-construction check passed: all twelve rostered quarterbacks were the confirmed or club-news starters, and none was a listed backup.

### Honest gaps

- `CASH_SET=UNKNOWN`. No standings screenshot or results CSV was provided, so the page states no ranks, cash line, payouts or winnings. The ranks that exist are portfolio ranks among the 150 scored lineups, not contest ranks.
- The fade-coverage report is `NO_EVIDENCE`; neither expected file exists.
- Suggested tool fixes are marked review-only. Nothing was written to any repo.

### Reuse value

High. This is the only page in the batch with measurable outcomes, so it is the calibration anchor for the CeminiDFS recap scorer. The scoring-hash discipline and the `NO_BOX_LINE` labelling are the parts worth copying into the shipped pipeline.
