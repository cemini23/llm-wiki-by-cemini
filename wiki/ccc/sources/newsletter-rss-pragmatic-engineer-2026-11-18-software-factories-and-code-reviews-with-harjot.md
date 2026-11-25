---
title: "The Pragmatic Engineer — software factories and code reviews with Harjot Gill"
type: source
related:
  - concepts/claude-code-software-factory.md
  - concepts/agent-pr-volume-exceeds-human.md
  - concepts/agent-completion-verification-gates.md
  - entities/tools/coderabbit.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|------|
| Title | Software factories and code reviews with Harjot Gill |
| Author | Gergely Orosz (The Pragmatic Engineer), with Harjot Gill |
| Type | Newsletter podcast recap (RSS, free tier) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-pragmatic-engineer-2026-11-18-software-factories-and-code-reviews-with-harjot.md` |
| Retrieved | 2026-11-22 (published 2026-11-18) |
| Pages | n/a |
| Read status | read |

## Narrative

Harjot Gill is founder and CEO of CodeRabbit, an AI code-review company. He reports shipping more than 5,000 pull requests in one month with agents, at a monthly AI run rate of about $250,000 across 40 engineers. He estimates about $150 per PR.

The work is mostly janitorial: CI improvements, flaky-test fixes, caching refinement, migrations. One agent ran for six weeks to build a write-ahead log on object storage in Rust, and that code is in production. Another migrated all services to Bun over a weekend. A third replaced a slow CI system.

His claim is that human code review is dead, and that quality holds because agents do the first pass and the review itself is automated.

Two cautions. First, this is a vendor CEO whose product is AI code review; the numbers are self-reported and not audited. [TENTATIVE] Second, the spend is an outlier. Orosz notes that other teams he hears from spend $200–$2,000 per developer per month.

For Cemini the pattern is familiar from `@concepts/agent-pr-volume-exceeds-human.md`: agent PR volume exceeds human capacity to review, so the bottleneck moves to verification. The CodeRabbit answer is to automate review too. The Cemini answer is the audit council and the completion gate. Both accept that a human reads every diff is no longer possible.

## Snippets

> "He shipped over 5,000 pull requests last month, spending on AI at a monthly run rate of $250,000." [Source: newsletter-rss-pragmatic-engineer-2026-11-18-software-factories-and-code-reviews-with-harjot.md]

> "He estimates that a PR costs him around $150 in a personal spend of around $250-$275K per month." [Source: newsletter-rss-pragmatic-engineer-2026-11-18-software-factories-and-code-reviews-with-harjot.md]
