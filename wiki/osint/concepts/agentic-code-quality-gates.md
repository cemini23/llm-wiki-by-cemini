---
title: Agentic code quality gates (constraints over review volume)
type: concept
tags: [ccc, quality, agents, k228]
keywords: [quality gates, back-pressure, agent constraints]
related:
  - sources/substack-rss-addy-osmani-2026-08-08-agentic-code-quality.md
  - concepts/code-as-agent-harness.md
  - entities/tools/pi-earendil.md
maturity: draft
created: 2026-08-08
updated: 2026-08-08
---

## Relations

- @sources/substack-rss-addy-osmani-2026-08-08-agentic-code-quality.md
- @concepts/code-as-agent-harness.md
- @entities/tools/pi-earendil.md

## Raw Concept

Osmani 2026-08-08: agent throughput forces quality into harness constraints.

## Narrative

Prefer deterministic gates (tests, mutation, lint, security, architecture rules) with continuous back-pressure; escalate humans only when gates break. Aligns with Cemini skill-audit / pre-commit / CI as production boundary.

[Source: https://addyo.substack.com/p/agentic-code-quality]
