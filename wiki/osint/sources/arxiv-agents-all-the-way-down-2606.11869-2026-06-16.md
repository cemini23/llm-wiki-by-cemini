---
title: "Agents All the Way Down — custom AI agent methodology (arXiv 2606.11869)"
type: source
tags: [source, arxiv, llm-agents, agent-engineering, methodology, mcp, k118]
keywords: [2606.11869, custom-agent, turtle-pattern, agent-tests-agent, liteshell, substrate, aac-lamb]
related:
  - concepts/agents-all-the-way-down-methodology.md
  - concepts/llm-agent-systems.md
  - concepts/mcp-tool-calling-eval-scaffold.md
  - concepts/conductor-orchestrator.md
  - sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md
  - concepts/code-as-agent-harness.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-06-16
clusters: [llm-agents, agent-harness]
---

## Relations

- @concepts/agents-all-the-way-down-methodology.md — five-phase practice distilled from paper
- @concepts/llm-agent-systems.md — corpus hub
- @concepts/mcp-tool-calling-eval-scaffold.md — P5 agent-tests-agent complements MAVEN smoke matrix
- @concepts/conductor-orchestrator.md — multi-agent = CLI composition corollary
- @sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md — sibling "named methodology from shipped agent" pattern

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agents All the Way Down: A Methodology for Building Custom AI Agents from Substrate to Production |
| **Authors** | Alier Forment, Pereira, García-Peñalvo, Casañ Guerrero (UPC / UPV-EHU / USAL) |
| **arXiv** | 2606.11869 |
| **sha256** | `81e95097862642e7c34a562ebac1ab4d702f228146a5106d8095ac1022e7c793` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.11869-2606-11869v1-agents-all-the-way-down-a-methodolo.pdf` |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (abstract + §1–1.4 contributions + P1–P5 outline) |
| **Worked example** | AAC (Agent-Assisted Creator) on LAMB educational platform — ~10 days, one developer, production at two universities since April 2026 |

## Narrative

Named **framework-free** methodology for **custom agents** (purpose-built, in-app, domain tools, operator-controlled security) vs general-purpose tier (Claude Code, Cursor).

**Asymmetry:** two **preconditions** (cross once, keep) + three **iterated practices** (loop forever):

| Phase | Name | Content |
|-------|------|---------|
| P1 | Substrate | LLM as software component: tools → system → messages; prompt-cache discipline |
| P2 | Building blocks | Function calling, MCP, CLI orchestration, liteshell, agent loop, skills, characters, hooks, scaffolding |
| P3 | Prototype | Pair with general-purpose agent against real platform |
| P4 | Turtle pattern | Harvest P3 artifacts → small agent loop → **ship as CLI** |
| P5 | Agent-tests-agent | General-purpose agent drives custom agent through behavioral scenarios — complements unit/integration tests |

**Turtle corollary:** multi-agent orchestration = **CLI composition** (supervisor/worker, fan-out, Ralph loops) without framework primitives.

**Security posture (argument, not demonstrated):** small dependency surface vs framework stacks — cite 2024–2026 supply-chain incidents.

**Cemini posture:** **REFERENCE** — steal **P4 ship-as-CLI** + **P5 behavioral eval layer** for prod-mcp / conductor smoke discipline. Cross-wiki handoff to `@ccc-wiki` for harness canon. No AAC/LAMB code install.

## Snippets

> "What separates custom agents from the general-purpose tier… is fit, not capability." [Source: arxiv-2606.11869-2606-11869v1-agents-all-the-way-down-a-methodolo.pdf abstract]

> "Once the preconditions are in hand, the engineer's working life is the loop P3 → P4 → P5 → P3." [Source: arxiv-2606.11869-2606-11869v1-agents-all-the-way-down-a-methodolo.pdf abstract]

> "Multi-agent orchestration is just CLI composition." [Source: arxiv-2606.11869-2606-11869v1-agents-all-the-way-down-a-methodolo.pdf abstract]

> "Agent-tests-agent… does not replace classical software testing." [Source: arxiv-2606.11869-2606-11869v1-agents-all-the-way-down-a-methodolo.pdf §1.4]
