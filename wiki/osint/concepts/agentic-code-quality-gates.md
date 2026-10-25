---
title: Agentic code quality gates (constraints over review volume)
type: concept
tags: [ccc, quality, agents, k228]
keywords: [quality gates, back-pressure, agent constraints]
related:
  - concepts/agent-harness-auditing-a2e.md
  - entities/tools/lifeos.md
  - concepts/ideal-state-artifact-verification.md
  - sources/substack-rss-addy-osmani-2026-08-08-agentic-code-quality.md
  - concepts/code-as-agent-harness.md
  - entities/tools/pi-earendil.md
  - sources/substack-rss-pragmatic-engineer-2026-10-06-state-of-tech-2026.md
  - concepts/k284-feeds-wave.md
  - concepts/k285-feeds-wave.md
  - sources/arxiv-2610.13647-a-saw-agentic-software-architecture-2026-10-12.md
  - sources/newsletter-rss-pragmatic-engineer-2026-10-07-sam-newman-resilience.md
maturity: draft
created: 2026-08-08
updated: 2026-10-25
---

## Relations
- @concepts/agent-harness-auditing-a2e.md — K230
- @entities/tools/lifeos.md
- @concepts/ideal-state-artifact-verification.md — K229 ISA

- @sources/substack-rss-addy-osmani-2026-08-08-agentic-code-quality.md
- @concepts/code-as-agent-harness.md
- @entities/tools/pi-earendil.md

## Raw Concept

Osmani 2026-08-08: agent throughput forces quality into harness constraints.

## Narrative

Prefer deterministic gates (tests, mutation, lint, security, architecture rules) with continuous back-pressure; escalate humans only when gates break. Aligns with Cemini skill-audit / pre-commit / CI as production boundary.

[Source: https://addyo.substack.com/p/agentic-code-quality]

## K284 — code-review theater is the failure this page guards against (2026-10-07)

The Pragmatic Engineer's 2026 snapshot reports the mechanism this page exists to prevent: **"everyone is playing the theater of doing reviews … just stamp everything with LGTM."** Volume of agent PRs rose ~9× in eight months and **exceeded human PRs in August 2026**; humans cannot read that much, so human review degrades to a stamp. The response is not "review harder" — it is the **deterministic gate**: tests, mutation, lint, security, architecture rules, with continuous back-pressure. It also reports **quality/reliability down** and **agent-only PR reviews rising**. [Source: @sources/substack-rss-pragmatic-engineer-2026-10-06-state-of-tech-2026.md]
