---
title: Kimi Agent Swarm vs Claude Agent Teams — scale, topology, and fit
type: concept
tags: [concept, multi-agent, kimi, claude, orchestration, k65]
keywords: [agent swarm, agent teams, moonshot, anthropic, coordinator, peer-to-peer, parallel research, coding workflows]
related:
  - sources/x-kirillk-kimi-agent-swarm-guide-2026-05-24.md
  - entities/tools/kimi-agent-swarm.md
  - entities/models/kimi-k2-6.md
  - concepts/llm-agent-systems.md
  - concepts/agent-cost-routing-model-orchestra.md
  - concepts/scatter-gather-topology.md
  - concepts/conductor-orchestrator.md
  - "@ccc-wiki/concepts/kimi-agent-swarm-vs-claude-agent-teams.md"
maturity: draft
created: 2026-05-24
updated: 2026-05-26
---

## Relations

- @sources/x-kirillk-kimi-agent-swarm-guide-2026-05-24.md — K65 primary source (@kirillk_web3)
- @entities/tools/kimi-agent-swarm.md — Moonshot product entity
- @entities/models/kimi-k2-6.md — Kimi coordinator model
- @concepts/llm-agent-systems.md — parent corpus for agent coordination patterns
- @concepts/scatter-gather-topology.md — Cemini's bounded parallel pattern (contrast to 300-agent fan-out)
- @concepts/conductor-orchestrator.md — prod routing layer; not replaced by Kimi Swarm
- @ccc-wiki/briefs/2026-05-24_k65-kimi-agent-swarm-vs-claude-teams.md — CCC-facing orchestration brief
- @ccc-wiki/concepts/kimi-agent-swarm-vs-claude-agent-teams.md — CCC synthesis (orchestration fit)

## Raw Concept

Synthesizes K65 comparison: **Moonshot Kimi Agent Swarm** (hub-and-spoke, 300× parallelism, web UI, content/research deliverables) vs **Anthropic Claude Agent Teams** (small peer group, terminal, codebase refactoring/debug).

## Narrative

### Topology

| | Kimi Agent Swarm | Claude Agent Teams |
|--|------------------|-------------------|
| **Coordination** | Central coordinator only | Peer-to-peer + lead |
| **Typical scale** | Up to 300 sub-agents [vendor claim] | ~4–6 (up to ~20 reported) |
| **Step budget** | Up to 4,000 coordinated steps | Session-bound, coding-scoped |
| **Interface** | `kimi.com` web | Claude Code / terminal |
| **Strength** | Broad coverage, batch files, research fan-out | Refactor, parallel review, multi-service debug |

### When each wins [TENTATIVE — single curator source + vendor docs]

- **Swarm** — N independent similar subtasks (N CVs, N papers, N landing pages); output is **synthesis of many parallel reads**, not deep single-repo reasoning.
- **Teams** — shared codebase state; agents challenge each other's patches; **lateral context** matters.

### Cemini / Conductor mapping

Cemini already implements **bounded** multi-agent patterns (conductor routing, LangGraph, scatter-gather briefs). Swarm's lesson is **task decomposition for embarrassingly parallel work** — not "add 300 LLM calls to prod."

**Do not** mirror 300-agent fan-out on market paths: cost, latency, and reconciliation explode. Use wiki RAG + Exa Tier-1 for research gaps instead.

**Do** steal: explicit output schema in prompts, coordinator-only merge (audit trail), human review before external deploy — aligns with @concepts/agent-cost-routing-model-orchestra.md scope-lock discipline.

### Risk notes

- **Scaled errors** — source concludes speed without verification multiplies mistakes.
- **Prompt specificity** — vague swarm prompts → vague bulk output.
- **Vendor lock-in** — no self-host path comparable to @entities/tools/hermes-agent.md or LangGraph.

## Snippets

> "In Kimi Agent Swarm, all outputs flow to the coordinator. There's no direct agent-to-agent communication." [Source: @kirillk_web3.docx, K65]

> "Inside a codebase, need agents to challenge each other → Claude Agent Teams. Need 100+ parallel workstreams, one synthesized output, web interface → Kimi Agent Swarm." [Source: @kirillk_web3.docx, K65]
