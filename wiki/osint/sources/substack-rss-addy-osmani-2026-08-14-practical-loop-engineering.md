---
title: "Addy Osmani — Practical Loop Engineering (K239)"
type: source
tags: [source, substack, rss, ccc, loop-engineering, k239]
keywords: [Addy Osmani, /goal, /loop, /schedule, HITL, Ralph, verify-frontend-change]
related:
  - concepts/practical-loop-engineering.md
  - entities/tools/loop-engineering.md
  - concepts/agent-steering-action-boundary.md
  - concepts/code-as-agent-harness.md
  - sources/arxiv-2608.12654-steerbench-work-2026-08-15.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: read
---

## Relations

- @concepts/practical-loop-engineering.md — synthesized /goal vs /loop vs proactive
- @entities/tools/loop-engineering.md — cobusgreyling repo ≠ this methodology
- @concepts/agent-steering-action-boundary.md — don't delegate the proceed/hold judgment
- @concepts/code-as-agent-harness.md
- @sources/arxiv-2608.12654-steerbench-work-2026-08-15.md

## Raw Concept

| Field | Value |
|-------|--------|
| URL | https://addyo.substack.com/p/practical-loop-engineering |
| Published | 2026-08-14 |
| sha256 | `d96e75b785eb4bf78d01a8d4e70590bbed4b9c4d2418a06076be660684f4c213` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-addy-osmani-2026-08-14-practical-loop-engineering.md` |
| retrieved | 2026-08-14 |
| Feed | addy-osmani |

## Narrative

Osmani runs 5–10 agents (typically ≤5 concurrent). A **loop** is an autonomous, self-correcting cycle: act → test → adjust until a specified goal. Pre-primitive era = hand-rolled bash / Ralph. Now Claude Code + Codex primitives are reliable enough *if* stop conditions are deterministic.

Claude Code team's four rungs (Osmani's summary of their write-up):

1. **Manual / agentic loop** — every prompt; human directs each turn.
2. **Goal-based (`/goal`)** — evaluator model checks a stated done-condition (tests passed, Lighthouse ≥90). Independent of the worker. Abort if two consecutive turns show no metric improvement.
3. **Time-based (`/loop`)** — cron-like; session-scoped; expires **7 days** (not 3). Laptop dies → loop dies. Cloud: `/schedule`.
4. **Proactive** — event/schedule, no human in real time; route routine work to small models.

Hard rules:

- **Do not let the worker decide the work is good.** Separate verifier sub-agent.
- The `/goal` evaluator only checks the transcript against hard rules — it is **not** a taste/judgment checker.
- Do not delegate **taste**. Osmani almost merged competitor-gap PRs that added complexity for little user gain.
- Watch closely: auth, security, finance, any privileged system.
- Spinning in place: same command three times with no change → stop.
- Bad fit: "keep going until the UI is good."

### Cemini steal (CCC)

- Encode `/goal` with **tool-named metrics**, max turns, and a no-improvement abort.
- `/loop` for inbox/PR triage — not for skill auto-evolution.
- Pair with SteerBench: the loop may *propose* a state-changing action; HITL still **holds** merge/deploy/scp.

**Brief:** `../Cemini claude code CCC/briefs/2026-08-15_k239-ccc-steerbench-flue-loop.md`.

## Snippets

> "The other habit that matters here is not letting the agent that did the work decide the work is good. One sub-agent drafts the change. A separate one verifies it." [Source: addyo.substack.com/p/practical-loop-engineering]

> "Recurring loops expire seven days after creation. … loops are session-scoped, so they stop when you start a new conversation." [Source: same]
