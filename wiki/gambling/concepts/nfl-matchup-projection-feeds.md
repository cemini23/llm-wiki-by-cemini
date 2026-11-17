---
title: "NFL matchup projection feeds — what a public player record proves"
type: concept
related:
  - "@osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md"
  - concepts/dfs-model-orchestration.md
  - concepts/dfs-injury-and-news-workflow.md
updated: 2026-11-17
---

## Raw Concept

Armchair Logan ("The Film Room") was the single Watch item in the 2026-11-17 batch.
The question this page answers: **what should we take from a public NFL projection site,
and what should we not?**

Source: @osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md.

## Narrative

### What it is

A web app at `football.armchairlogan.workers.dev`, running on Cloudflare Workers.
It publishes, per NFL matchup:

- projected score, winning margin, and total
- unit efficiency ratings and tempo
- verified quarterback, injury, and weather notes
- a downloadable prediction export

Refreshed every 15 minutes. Reachable on 2026-11-17 (HTTP 200).

### The rule that makes it interesting

> **Only picks saved before kickoff count toward the record.**

That single line is the difference between a track record and a story. Most public
prediction sites publish accuracy after the fact, when the pick can be massaged. A
timestamped pre-kickoff save is auditable — not by us, but at least by the site's own
record, and the constraint is stated plainly.

Our own PM canary and parlay grading carry the same requirement. Any evaluation that
does not lock before the event is not an evaluation.

### What it is not

It is not a signal source for CeminiDFS. Three reasons:

1. **No methodology.** Projected scores appear without a published model, calibration,
   or feature list. A number with no derivation cannot be audited or combined.
2. **No line comparison.** Without a book line and a closing price, a projection has no
   betting edge, only an opinion.
3. **No stated sample.** The public record starts in Week 8. Eight or so weeks of NFL
   results is a small sample with wide variance; a good stretch is not evidence.

### What to take

The **lock-before-kickoff discipline**. That is a process rule, and it costs nothing.

If the export ever gains a published methodology and a line comparison, re-evaluate.
Until then it is a Watch item.

## Snippets

> Only picks saved before kickoff count toward the record.
> [Source: https://football.armchairlogan.workers.dev/ (retrieved 2026-11-17)]

> Projected scores, team comparisons and detailed matchup research.
> [Source: https://football.armchairlogan.workers.dev/ (retrieved 2026-11-17)]

## Dead Ends

- **Treating a public projection as a signal.** No methodology, no line, no sample.
- **Reading a hot streak as accuracy.** The record starts in Week 8.
