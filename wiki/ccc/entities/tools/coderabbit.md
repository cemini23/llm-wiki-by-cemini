---
title: coderabbit — AI code-review product and an outlier AI-spend case
type: entity
related:
  - sources/newsletter-rss-pragmatic-engineer-2026-11-18-software-factories-and-code-reviews-with-harjot.md
  - concepts/agent-pr-volume-exceeds-human.md
  - concepts/claude-code-software-factory.md
maturity: draft
updated: 2026-11-22
---

## Raw Concept

Entity page for CodeRabbit. Prompted by the Pragmatic Engineer episode `@sources/newsletter-rss-pragmatic-engineer-2026-11-18-software-factories-and-code-reviews-with-harjot.md`.

## Narrative

CodeRabbit sells AI code review. Founder and CEO Harjot Gill reports shipping more than 5,000 pull requests in one month with agents, at about $250,000 per month across 40 engineers, roughly $150 per PR.

The work cited is mostly maintenance: CI improvements, flaky-test fixes, caching, migrations. One agent ran six weeks to build a write-ahead log on object storage in Rust.

### Reading

This is a vendor case, self-reported and not audited. [TENTATIVE] The spend is an outlier against the $200–$2,000 per developer per month that other teams report. The transferable observation is the bottleneck shift: agent PR volume exceeds human review capacity, so review itself must be automated or gated. See `@concepts/agent-pr-volume-exceeds-human.md`.

No Phase-0 audit was run. This page records a market signal, not an adoption decision.
