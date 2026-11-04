---
title: "Pragmatic Engineer — 200 PRs a month: what AI-native actually changed"
type: source
tags: [source, newsletter, engineering, productivity, ai-native, culture]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | How Software Engineering Is Changing: A Tale of Two Eras |
| Source | pragmatic-engineer (The Pragmatic Engineer) |
| Published | 2026-11-03 |
| Author of the piece | Neil Kakkar, software engineer (Bloomberg, PostHog, Tano) |
| Read status | skimmed — editorial introduction and opening sections |

Winning entry of 125 submissions to the publication's five-year essay challenge.

## Narrative

### The number

At PostHog, pre-AI, Kakkar merged **8–20 PRs per month**. At Tano, an AI-native startup, he now ships **200+ PRs per month** — roughly a **tenfold** increase.

He is careful about the comparison: PostHog stats are pre-AI and he treats them as a **baseline for excellent engineering work**, not as a criticism. Tano was founded after AI agents emerged.

### Old constraints that disappeared

- Communications overhead.
- Code review as a bottleneck.

The explicit trade: **moving faster and breaking things.**

### New constraints that appeared

This list is the valuable part, because it is what actually replaced the old bottlenecks:

- **Thrashing** — too much context switching.
- **Losing shared context** — across the team.
- **Pacing is harder** to sustain.
- **Less focus on design.**
- **AI plan limits** — a real operational constraint that did not exist before.

### Why "less focus on design" belongs on that list

The other four are throughput problems. That one is a quality problem, and it points at the failure mode of a tenfold loop: when producing code is cheap, the expensive thing becomes deciding what to produce. A team that does not reallocate effort toward design will produce ten times as much of whatever it was already thinking.

### The cultural claim

The essay's summary: everyone needs to be on board with AI for the benefits to materialise, encouraging experimentation matters, and **many existing technologies and processes crack under the change**.

That last point is the practical one — the constraint moves from writing code to everything around it: review, integration, deployment, and the shared understanding that used to accumulate automatically because writing was slow.

**Caveat.** One engineer's data, three employers, self-reported. The PostHog baseline is a different company from the Tano comparison, so the tenfold is not a controlled measurement.

## Snippets

> "Until last year, he was merging between eight and 20 PRs per month. But since joining an AI-native startup, Neil now ships 200+ PRs per month, approximately a tenfold increase." [retrieved 2026-11-03]

> "Too much context switching (thrashing), losing shared context, pacing yourself is harder, less focus on design, and worries about AI plan limits." [retrieved 2026-11-03]

## Dead Ends

- **Treating the tenfold as a controlled result.** Different companies, different eras, self-reported.
