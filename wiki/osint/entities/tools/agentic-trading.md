---
title: AgenticTrading — DAG-Planner Multi-Agent Trading Framework (Open-Finance-Lab)
type: entity
tags: [tool, multi-agent, financial-orchestration, neurips-2025, reference-only, license-tbv, hardware-mismatch]
keywords: [agentic-trading, dag-planner, mcp-acp-a2a-anp, four-layer-protocol, neo4j-agent-memory, finagent-orchestration, conductor-design-input]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/conductor-orchestrator.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 4, **REFERENCE-ONLY** tier
- @concepts/conductor-orchestrator.md — AgenticTrading's 4-layer agent communication protocol (MCP/ACP/A2A/ANP) is potential design input for Cemini's in-house Conductor evolution path; reference comparison for the existing in-house Conductor (v0.1.1 shadow mode)
- @concepts/cemini-license-posture.md — license [TBV — DR couldn't access upstream LICENSE file, surfaced ambiguity]

## Raw Concept

Open-Finance-Lab/AgenticTrading is a multi-agent orchestration framework engineered to transition traditional algorithmic trading workflows into dynamic, multi-agent ecosystems. Backed by a NeurIPS 2025 academic paper.

K32 DR verdict: **REFERENCE-ONLY**. Cannot deploy on Cemini's 7GB-RAM Hetzner ceiling, cannot integrate code without verified license, but the architectural concepts are valuable input to Conductor evolution.

## Narrative

- **URL**: `https://github.com/Open-Finance-Lab/AgenticTrading` ✓ DR-cited
- **License**: [NEEDS VERIFICATION 2026-05-06] — DR explicitly noted upstream LICENSE file inaccessible; suggested a related repo (`kweinmeister/agentic-trading`) carries Apache-2.0 but unable to confirm canonical Open-Finance-Lab repo
- **Stack**: Python; Neo4j (graph database for execution traces); FastAPI (concurrent agent calls); LangGraph or similar (DAG planner)
- **Paper**: "Orchestration Framework for Financial Agents: From Algorithmic Trading to Agentic Trading" (NeurIPS 2025) — `https://www.researchgate.net/publication/398269858_Orchestration_Framework_for_Financial_Agents_From_Algorithmic_Trading_to_Agentic_Trading`
- **Docs**: `https://finagent-orchestration.readthedocs.io`

### Architecture summary

**DAG Planner Agent** interprets high-level strategic directives → orchestrates task execution across specialized agent pools:

- **Data Agent Pool** — ingestion (Polygon.io, Yahoo Finance)
- **Alpha Agent Pool** — LLM-driven factor mining
- **Risk Agent Pool** — exposure and limit checks
- **Portfolio Agent Pool** — allocation
- **Execution Agent Pool** — order routing

Inter-agent communication via four custom protocol layers:

| Layer | Acronym | Role |
|-------|---------|------|
| MCP | Multi-agent Control Protocol | lifecycle control, agent spawning/killing, supervisor commands |
| ACP | Agent Communication Protocol | typed message-passing between any two agents in the topology |
| A2A | Agent-to-Agent | peer-to-peer coordination (no supervisor in path) |
| ANP | Agent Network Protocol | network-level routing and discovery |

Persistent execution memory in **Neo4j** — execution traces, performance feedback, iterative strategy improvement loop.

DR claims simulated benchmark performance against S&P 500 + Bitcoin baselines.

### Why REFERENCE-ONLY (not adopt for Cemini-prod)

Three independent blockers:

**1. Hardware mismatch**: Up to 20 parallel agents across 5 pools + Neo4j + FastAPI concurrent stack would exceed Cemini's 7GB Hetzner RAM ceiling. Cemini-prod runs CPU-only, no GPU; Neo4j adds operational dependency Cemini doesn't currently carry.

**2. Architectural divergence**: Cemini deploys a tightly-controlled linear 4-node StateGraph in LangGraph, intentionally minimalist. AgenticTrading's 5-pool / 4-protocol architecture is a different design philosophy — neither is wrong, but mixing them would break Cemini's "minimalist deployment" doctrine.

**3. License uncertainty**: DR couldn't reach the upstream `LICENSE` file. Without explicit verification, integrating any code is an IP-due-diligence vulnerability. **Note (per monetization-priority frame)**: even softening the license stance for revenue-generation purposes, you can't import code under genuinely unknown legal status into a production codebase.

### Why REFERENCE-ONLY is still valuable

The 4-layer agent protocol (MCP/ACP/A2A/ANP) is **research-grade thinking** about agent topology. Cemini's in-house Conductor is currently single-supervisor (DAG planner ≈ Conductor itself, no inter-agent peer comm). Reading the AgenticTrading paper would clarify:

- Whether peer-to-peer A2A messaging adds value over hub-and-spoke (Conductor-as-supervisor)
- Whether Cemini's Conductor evolution should adopt typed-protocol message-passing (ACP) or stay with prose JSON
- How Neo4j-backed execution memory compares to Cemini's current PostgreSQL+pgvector approach

These are inputs to the **deferred Conductor autoresearch brief** (`cemini-prod:/opt/cemini/briefs/2026-05-04_autoresearch-conductor-evolution.md`, DEFERRED with traffic-threshold trigger).

### Action items (low priority, pull when needed)

1. Read the NeurIPS 2025 paper directly when Conductor evolution moves from deferred to active
2. Document the 4-layer protocol in `concepts/conductor-in-house-build.md` as comparison-reference
3. If license verifies as Apache-2.0 and Cemini eventually expands beyond 7GB RAM, revisit deployment fit

### Open questions

- ⚠ Upstream LICENSE: must be checked directly via `gh api` or git clone before any deeper engagement
- ⚠ How does the 4-layer protocol differ from existing standards (LangChain, AutoGen, CrewAI agent comms)?
- ⚠ Does the NeurIPS paper benchmark replicate? (cherry-picked S&P/BTC simulation results are common in agent papers)
- ⚠ What's the LLM-call cost profile for 20 concurrent agents at production scale?

### Adoption status — REFERENCE-ONLY

Not adopted. Not staged for adoption. Documented for Conductor-evolution research input.

## Snippets

### 4-layer agent protocol (DR-cited)

> "Routing inter-agent communications through four custom protocol layers: MCP (Multi-agent Control Protocol), ACP, A2A, and ANP. To maintain contextual continuity and facilitate iterative strategy improvement, it relies heavily on a Neo4j graph database to store execution traces and performance feedback, reportedly achieving strong benchmark performance against the S&P 500 and Bitcoin in simulated tests." [Source: 5_6 links.docx URL 4]

### Why hardware-block for Cemini-prod (DR direct framing)

> "AgenticTrading introduces a hard dependency on Neo4j for its graph-based execution memory. Furthermore, orchestrating up to 20 parallel agent tasks across multiple pools (Alpha, Risk, Portfolio, Execution) via FastAPI over concurrent LLM calls would easily overwhelm the ~7 GB RAM ceiling on the CPU-only Hetzner production server." [Source: 5_6 links.docx URL 4]
