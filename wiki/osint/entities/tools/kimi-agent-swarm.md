---
title: Kimi Agent Swarm — Moonshot parallel multi-agent web product
type: entity
tags: [entity, tool, kimi, moonshot, multi-agent, agent-swarm, reference-only, k65]
keywords: [kimi agent swarm, moonshot ai, k2.6 coordinator, 300 sub-agents, 4000 steps, agent-swarm]
related:
  - sources/x-kirillk-kimi-agent-swarm-guide-2026-05-24.md
  - entities/models/kimi-k2-6.md
  - concepts/kimi-agent-swarm-vs-claude-agent-teams.md
  - concepts/agent-cost-routing-model-orchestra.md
  - concepts/llm-agent-systems.md
  - concepts/agent-cost-routing-model-orchestra.md
maturity: draft
created: 2026-05-24
updated: 2026-05-24
---

## Relations

- @sources/x-kirillk-kimi-agent-swarm-guide-2026-05-24.md — K65 ingest ( @kirillk_web3 )
- @entities/models/kimi-k2-6.md — coordinator LLM
- @concepts/kimi-agent-swarm-vs-claude-agent-teams.md — comparison vs Anthropic Agent Teams
- @concepts/llm-agent-systems.md — multi-agent systems hub
- @concepts/agent-cost-routing-model-orchestra.md — same K2.6 vendor / cost-routing family

## Raw Concept

Moonshot AI **consumer web product** for massively parallel task execution. Announced limits: **≤300 sub-agents**, **≤4,000 steps** per task, **central coordinator** (no lateral agent mailboxes). URL: `https://www.kimi.com/agent-swarm` [TENTATIVE product surface 2026-05-24].

## Narrative

### Architecture (as documented)

1. **Decompose** — K2.6 splits prompt into parallel subtasks (e.g. one sub-agent per paper, per job listing, per store).
2. **Execute** — sub-agents run concurrently (not queued serially).
3. **Synthesize** — coordinator merges into one deliverable (file bundle, report, spreadsheet).

### vs Cemini stack

| Dimension | Kimi Agent Swarm | Cemini (conductor + prod) |
|-----------|------------------|---------------------------|
| Venue | Moonshot web UI | Hetzner `/opt/cemini`, MCP tools |
| Parallelism | O(100) homogeneous sub-agents | LangGraph / scatter-gather, bounded cost |
| Best fit | Broad research, batch content | Trading signals, wiki RAG, governed briefs |
| Integration | None (no prod MCP) | kb-server, prod-mcp, stash |

**Verdict: NO-GO for production trading** — no market connectivity, no audit trail comparable to Cemini briefs, coordinator is vendor black box. **REFERENCE** for prompt-decomposition patterns and when to prefer @ccc-wiki concepts/subagent-orchestration.md (Claude Code Agent Teams) for codebase work.

### Related Moonshot surface

**Claw Groups** (mentioned in source) — multi-specialist chat room; adjacent to OpenClaw lineage; see @concepts/openclaw-security-taxonomy.md if evaluating hosted agent rooms.

## Snippets

> "K2.6 coordinates up to 300 sub-agents working in parallel, with up to 4,000 coordinated steps, on a single complex task." [Source: @kirillk_web3.docx, K65]
