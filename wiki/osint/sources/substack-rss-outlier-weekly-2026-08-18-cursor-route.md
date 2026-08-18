---
title: "Outlier Weekly — cursor-route MIT CLI (2026-08-18)"
type: source
tags: [newsletter, ccc, routing, k241]
keywords: [cursor-route, DeepSeek, Grok, tmux, always-approve]
related:
  - entities/tools/cursor-route.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/agent-cost-routing-model-orchestra.md
  - sources/newsletter-rss-latent-space-2026-08-17-stripe-openrouter.md
  - sources/arxiv-2608.16798-clawgym-ii-2026-08-18.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @entities/tools/cursor-route.md — public MIT CLI `cemini23/cursor-route`
- @concepts/llm-routing-deepseek-openrouter-failover.md — mid lane is DeepSeek, not Claude
- @concepts/agent-cost-routing-model-orchestra.md — planner vs worker price tiers
- @sources/newsletter-rss-latent-space-2026-08-17-stripe-openrouter.md — routing layer same week
- @sources/arxiv-2608.16798-clawgym-ii-2026-08-18.md — do not swap `/route` worker

## Raw Concept

| Field | Value |
|-------|--------|
| File | `substack-rss-outlier-weekly-2026-08-18-how-i-run-deepseek-and-grok-in-parallel-from-cur.md` |
| sha256 | `bf33c4c05552843f94f4c95fb8f8b63ea5134a7346d407f60523c1507c90163d` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-outlier-weekly-2026-08-18-how-i-run-deepseek-and-grok-in-parallel-from-cur.md` |
| URL | https://outlierweekly.substack.com/p/how-i-run-deepseek-and-grok-in-parallel (retrieved 2026-08-18) |
| Repo | https://github.com/cemini23/cursor-route (MIT) |
| Dual-ID | **OSINT K241**. CCC **must** bump `entities/skills/route.md` backlog (K240 did not). |

## Narrative

Serial Cursor sessions become a waiting room: one expensive context plans, edits, tests, and writes the handoff. cursor-route (MIT, npm `0.1.1`, `/route-orch` skill) splits lanes: **Cursor plans; DeepSeek mid; Grok CLI hard.** Workers run in real **tmux** sessions (list/capture/attach/stop). **Always-approve is the worker default** (`--ask` to opt out) — coding jobs in controlled worktrees only; **not** permission to automate Discord, trading, or irreversible actions.

Mid lane: Claude Code harness pointed at `https://api.deepseek.com/anthropic`. The env names are harness interface, not Anthropic billing. `cursor-route health` must prove the mid lane is actually DeepSeek.

**CCC steal:** backlog row on `entities/skills/route.md` — public MIT sibling to `/route`. Do **not** swap the `/route` worker. Do **not** replace PATH `claude-ds`.

## Snippets

> "Cursor plans. DeepSeek handles the mid lane. Grok CLI handles the hard lane." [Source: https://outlierweekly.substack.com/p/how-i-run-deepseek-and-grok-in-parallel (retrieved 2026-08-18)]

> "Always-approve is the worker default… It is not permission to automate live Discord, trading, or other irreversible actions." [Source: same]
