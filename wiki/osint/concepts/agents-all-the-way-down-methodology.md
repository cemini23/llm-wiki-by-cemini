---
title: Agents All the Way Down — custom agent engineering methodology
type: concept
tags: [concept, llm-agents, agent-engineering, methodology, mcp, evaluation, k118]
keywords: [custom-agent, turtle-pattern, agent-tests-agent, liteshell, substrate, ship-as-cli]
related:
  - sources/arxiv-agents-all-the-way-down-2606.11869-2026-06-16.md
  - concepts/llm-agent-systems.md
  - concepts/mcp-tool-calling-eval-scaffold.md
  - concepts/conductor-orchestrator.md
  - concepts/code-as-agent-harness.md
  - sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md
maturity: draft
created: 2026-06-16
updated: 2026-06-16
cross-wiki-source: "@ccc-wiki/briefs/2026-06-16_agents-all-the-way-down-handoff.md"
---

## Relations

- @sources/arxiv-agents-all-the-way-down-2606.11869-2026-06-16.md — K118 primary source
- @concepts/llm-agent-systems.md — corpus hub
- @concepts/mcp-tool-calling-eval-scaffold.md — P5 extends MAVEN smoke matrix
- @concepts/conductor-orchestrator.md — CLI-composition corollary for multi-agent
- @concepts/code-as-agent-harness.md — harness discipline cluster

## Raw Concept

K118 arXiv 2606.11869 — first published end-to-end methodology chaining substrate → building blocks → prototype → ship-as-CLI → agent-tests-agent for **custom** (in-app, domain-tool) agents.

## Narrative

### Custom vs general-purpose (fit axis)

Custom when needing ≥1 of: embedded domain prompt/skills, private tools/APIs, in-app deployment, tight allow-list, right-sized model mix, brand/audit/compliance voice.

### Five phases

| Phase | Once or loop | Steal-for-Cemini |
|-------|--------------|------------------|
| P1 Substrate | Once | Cache discipline for long MCP sessions (@concepts/context-compression-resume-pattern.md) |
| P2 Building blocks | Once | MCP + CLI + skills vocabulary |
| P3 Prototype | Loop | Use Cursor/Claude Code as pair-programmer |
| P4 Turtle (ship CLI) | Loop | **Prod-mcp / lazy-tool as shipped CLIs** |
| P5 Agent-tests-agent | Loop | **Behavioral eval layer** atop unit tests |

### Turtle corollary

Specialist agents composed via shell — supervisor/worker, parallel fan-out, Ralph loops — without importing orchestration frameworks.

**Verdict:** **REFERENCE** — complements RocketSmith (K105) subagent steal patterns with **explicit QA discipline**. CCC wiki brief staged for harness canon.

## Snippets

> "The custom agent is the cabinet maker's jig: built for one specific job." [Source: arxiv-2606.11869-2606-11869v1-agents-all-the-way-down-a-methodolo.pdf §1.1]
