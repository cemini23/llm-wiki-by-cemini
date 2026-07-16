---
title: Nagus ops control plane — packetized agents + write-back state
type: concept
tags: [concept, llm-agents, orchestration, xsp, ops, nagus]
keywords: [nagus, working-brain, notion, linear, packetized-agents, xsp-ops, thin-roles, filesystem-queue]
related:
  - concepts/xsp-lane-trading-framework.md
  - concepts/agents-all-the-way-down-methodology.md
  - concepts/code-as-agent-harness.md
  - entities/tools/twelve-factor-agents.md
  - entities/tools/fable-advisor.md
maturity: draft
created: 2026-07-16
updated: 2026-07-16
---

## Relations

- @concepts/xsp-lane-trading-framework.md — first Cemini vertical (Macro Charts → XSP packets)
- @concepts/agents-all-the-way-down-methodology.md — Turtle / ship-as-CLI composition
- @concepts/code-as-agent-harness.md — harness discipline cluster
- @entities/tools/twelve-factor-agents.md — custom pipelines over generic frameworks
- @entities/tools/fable-advisor.md — Cursor plan + Grok implementer lane used for MVP

## Raw Concept

Operator-shared description (2026-07-15 Signal / “Nagus”) of a market-data multi-agent stack: scheduled sensors, Notion as live operational memory, Linear as work/scale queue, thin Claude agents on “optimal packets,” dual write-back so the system stays aware of its own data paths (“working brain of info”). Cemini locked a **native analog** without Notion/Linear/Robinhood-on-laptop: `.local` JSON brain + filesystem queue + 7 CLI roles.

## Narrative

### Pattern (what to steal)

| Layer | Nagus framing | Cemini MVP (2026-07-15) |
|-------|---------------|-------------------------|
| Sensors | Scheduled market-data pulls (RH cited) | Macro Charts RSS via existing pollers |
| Brain | Notion DBs (queryable live state) | `.local/ops/xsp/state/brain.json` + `posts/` |
| Queue | Linear (backlog + “need more agents”) | `.local/ops/xsp/queue/{pending,running,done,failed}/` |
| Workers | Thin multi-agent Claude packets (~7 roles; “500” = concurrency theater) | `scripts/xsp_ops/` roles: sensor → parse → land → enqueue → triage → packet → scale |
| Write-back | Every action logged to Notion/Linear | Brain audit + queue moves + escalate events |
| Token discipline | One agent must not do fetch→parse→land→distribute | One job per CLI role |

Core insight: treat agents as an **ops control plane** (state that moves), not only a research wiki (canon that compounds). Markdown remains durable knowledge; the brain/queue is for live paths.

### What not to copy

- “500 agents” as a success metric
- Replacing wiki canon with Notion
- Assuming Linear “recognizes” scale needs — *your* rules/watcher decide; Linear is just a queue API/UI
- Auto-writing `briefs/` or `/opt/cemini` from the laptop loop

### Cemini implementation pointer

- Package: `scripts/xsp_ops/` (+ `scripts/xsp_ops/README.md`)
- Orchestrator: `bash scripts/run_xsp_ops_loop.sh` / `--dry-run`
- LaunchAgent: `com.cemini.xsp-ops-loop` via `scripts/install_workflow_launchagents.sh` (hourly)
- Packets land under `.local/ops/xsp/packets/` — **human promote** to `briefs/xsp-*` before any prod scp
- **No prod brief required** for the scaffolding itself; stage an `xsp-` prod brief only when server RH / Redis / Lane monitors must change

### Pointer path (for chats / briefs)

`@concepts/nagus-ops-control-plane.md`

## Snippets

> Goal is to reduce the reliance on .md files… every single thing … gets logged into Notion and Linear… entire infrastructure is constantly aware of its own data pulls… working brain of info. [Source: Nagus Signal thread 2026-07-15 — operator paraphrase]

> One agent calling RH → parse → land Notion → distribute would burn tokens absurdly fast → 7-agent packet setup; Linear helps recognize when more agents are needed. [Source: same thread — operator paraphrase]
