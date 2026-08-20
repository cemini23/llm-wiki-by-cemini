---
title: "Practical loop engineering — /goal, /loop, HITL (K239)"
type: concept
tags: [concept, loop-engineering, ccc, k239]
keywords: [Addy Osmani, /goal, /loop, /schedule, Ralph, Flue, verifier]
related:
  - sources/substack-rss-addy-osmani-2026-08-14-practical-loop-engineering.md
  - sources/newsletter-rss-latent-space-2026-08-15-react-for-agents-flue.md
  - sources/newsletter-rss-pragmatic-engineer-2026-08-14-meta-resignation-wave.md
  - sources/arxiv-2608.12654-steerbench-work-2026-08-15.md
  - entities/tools/loop-engineering.md
  - concepts/agent-steering-action-boundary.md
  - concepts/code-as-agent-harness.md
  - sources/newsletter-rss-pragmatic-engineer-2026-08-19-osmani-ai-engineering.md
  - sources/substack-rss-moontower-2026-08-19-socrates-highlights.md
  - sources/substack-rss-moontower-2026-08-19-why-should-i-learn-this.md
maturity: draft
created: 2026-08-15
updated: 2026-08-20
---

## Relations

- @sources/substack-rss-addy-osmani-2026-08-14-practical-loop-engineering.md — primary
- @sources/newsletter-rss-latent-space-2026-08-15-react-for-agents-flue.md — React-style hooks / Pi
- @sources/newsletter-rss-pragmatic-engineer-2026-08-14-meta-resignation-wave.md — Grok Bot teaser only
- @sources/arxiv-2608.12654-steerbench-work-2026-08-15.md — gate at commit
- @entities/tools/loop-engineering.md — cobusgreyling MIT *repo* (K129); this page is the 2026 primitive methodology
- @concepts/agent-steering-action-boundary.md
- @concepts/code-as-agent-harness.md
- @sources/newsletter-rss-pragmatic-engineer-2026-08-19-osmani-ai-engineering.md — K243 cognitive surrender + mutual amplification

## Raw Concept

What this page answers: how to run bounded agent loops in Claude Code / Cursor without delegating judgment or auto-evolving skills.

## Narrative

Osmani (2026-08-14) + Claude Code team primitives:

| Primitive | Trigger | Stop | Use |
|-----------|---------|------|-----|
| Manual agentic loop | each prompt | human | default |
| `/goal` | start of a bounded task | evaluator checks **named metric**; abort on no-improvement | Lighthouse, tests, N issues moved |
| `/loop` | interval | session end or 7-day expiry | PR/inbox triage |
| `/schedule` | cloud routine | you turn it off | same, survives laptop off |
| Proactive | event | per-task goal | only well-defined streams |

Hard constraints for Cemini:

1. Worker ≠ verifier. `/goal` evaluator is a **rule checker**, not taste.
2. Same command 3× with no change → stop.
3. Auth / money / prod / skill files stay **watched**.
4. Loops may **propose**; SteerBench HITL still **holds** merge/deploy/scp/LIVE Discord/skill writes.
5. Flue 2 (`useSkill`/`useTool`/`useSubagent`, re-render each turn) is CCC awareness — **not** a Phase-0 install this batch.
6. PE "Grok Bot" is a paywalled teaser — wiki-only.

Do **not** unattended auto-evolve `.cursor/skills/*` as a loop target.

**K243 Osmani (2026-08-19) — cognitive surrender + mutual amplification.** Two failure-mode steals: (1) **cognitive surrender** — delegate tasks you no longer verify to the point you can't judge correctness (junior-dev-from-ChatGPT syndrome); the `/goal`/`/loop` fix is to keep a verifiable artifact, not more tooling. (2) **mutual amplification** — agent + human must each raise the other's capability, not just offload; a loop that runs without a human-checked output is delegation, not engineering. Reinforces: worker ≠ verifier; loops propose, HITL holds. [Source: Pragmatic Engineer 2026-08-19]
