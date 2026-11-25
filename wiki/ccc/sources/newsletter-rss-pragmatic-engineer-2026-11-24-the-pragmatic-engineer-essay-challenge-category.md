---
title: "Pragmatic Engineer 2026-11-24 — essay challenge category winners (Part 1)"
type: source
related:
  - concepts/claude-code-software-factory.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agent-pr-volume-exceeds-human.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Pragmatic Engineer Essay Challenge: Category Winners (Part 1) |
| Author | Gergely Orosz (The Pragmatic Engineer) |
| Type | Newsletter (RSS, free tier) |
| Location | research to be indexed/newsletter-rss-pragmatic-engineer-2026-11-24-the-pragmatic-engineer-essay-challenge-category.md |
| Retrieved | 2026-11-24 |
| File | `newsletter-rss-pragmatic-engineer-2026-11-24-the-pragmatic-engineer-essay-challenge-category.md` |
| URL | https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-essay-challenge |
| Read status | read |

## Narrative

Excerpts from a fifth-birthday essay contest on how software building changed after coding agents. Three categories are covered. The material is practitioner testimony, not measurement.

**Code review collapse (Anton Zaides, HoneyBook).** Across three repositories, review went from two reviewers to zero in a few months. The author names the cause: once nobody reviews, it is easy to cut corners in your own understanding. The output rose and the codebase grew duplicative and buggy. A 10k-line PR from a designer included dummy data where backend calls belonged.

**Tornado of parallel sessions.** The same author reports 6 to 8 parallel agent sessions, up from 2 to 3. That is a workflow change, not a tool change.

**Software machinist (Paul D'Ambra, PostHog).** Engineers stop hand-writing every line and start building tooling, inspecting samples, and producing in volume. Two predictions: CI and review change next; we make tools for our workshop.

**Devolutions migration.** A migration estimated at three years per platform finished in under one year for Windows and Linux. An internal hackathon produced 60 useful skills. AI spend reached $2M per year.

**Steering versus rowing (Bruno Felix, XEO360).** The main activity shifts from producing good code to managing many workstreams and exercising judgment.

**Why it matters to this wiki.** The review-collapse story is the failure mode of the software-factory pattern: output rises, review falls, quality drops. It is the counterweight to every agent-throughput gain. Treat all figures as self-reported by the essay authors. [TENTATIVE]

## Snippets

> "So, in the span of a couple of months, we dropped from two people reviewing and understanding the code, to zero!" [Source: `newsletter-rss-pragmatic-engineer-2026-11-24-the-pragmatic-engineer-essay-challenge-category.md`, retrieved 2026-11-24]
