---
title: "Generative Agents — Interactive Simulacra of Human Behavior (Park et al., Stanford + Google + DeepMind, UIST 2023)"
type: source
tags: [paper, llm-agents, multi-agent-simulation, memory-architecture, reflection, planning, stanford, google, uist-2023, arxiv, k41]
keywords: [generative-agents, sims-style-sandbox, agent-memory-stream, reflection-loop, planning-hierarchy, observe-plan-act, 25-agent-society, park, obrien, cai, morris, liang, bernstein]
related:
  - concepts/llm-agent-systems.md
  - concepts/multi-agent-trading.md
  - sources/tradingagents.md
  - sources/react-yao-2022.md
  - sources/toolformer-schick-2023.md
maturity: validated
read_status: skimmed
created: 2026-05-13
updated: 2026-05-13
clusters: [llm-agents, multi-agent]
---

## Relations

- @concepts/llm-agent-systems.md — Generative Agents is the canonical reference for **memory + reflection + planning** as a three-tier agent architecture; foundational for any multi-agent LLM simulation
- @concepts/multi-agent-trading.md — tradingagents uses a memory-stream pattern adapted from this paper's architecture; conceptual lineage is direct
- @sources/tradingagents.md — TradingAgents framework explicitly cites this paper as architectural ancestor
- @sources/react-yao-2022.md — ReAct gives the per-step loop; Generative Agents adds the **long-horizon memory and reflection** that turns single-step actions into coherent long-running behaviors
- @sources/toolformer-schick-2023.md — Toolformer trains tool-use; Generative Agents assumes tool-use exists and focuses on **what to do with persistent agent state over hundreds of timesteps**

## Raw Concept

- **Original title**: "Generative Agents: Interactive Simulacra of Human Behavior"
- **Authors**: Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
- **Affiliations**: Stanford University (Park, O'Brien, Liang, Bernstein); Google Research (Cai); Google DeepMind (Morris)
- **Publication**: UIST 2023 (arXiv 2304.03442v2, DOI 10.1145/3586183.3606763)
- **PDF location (post-scp)**: `cemini-librarian:/opt/cemini-bulk/research/2304.03442v2.pdf`
- **sha256**: `1b31e77fb24d25d7...` (preingest verdict: NEW)
- **Size**: 11,947,867 bytes, 22 pages
- **Read status**: skimmed
- **Discovered via**: user drop into `research to be indexed/` 2026-05-12

## Narrative

### What it is

Twenty-five LLM-powered agents populate a Sims-like sandbox town. Each agent has:

- **A memory stream**: timestamped, natural-language records of every observation and action
- **A retrieval mechanism**: recency × importance × relevance scoring to surface relevant memories
- **A reflection loop**: periodically the agent generates higher-level abstractions ("synthesized thoughts") from recent memories, which become new memories
- **A planning hierarchy**: daily plans → hourly plans → minute-level actions, each layer expanded from the previous

Agents wake up, eat breakfast, go to work, share gossip, plan parties (yes — the famous "Valentine's party emergent coordination"), and form relationships, all driven by LLM calls grounded in the memory stream.

### Why it matters

The contribution isn't the sandbox — it's the **memory-reflection-planning loop** as a reusable architecture for any long-running LLM agent. Cemini's tradingagents pipeline uses the same loop in spirit: trading "memory" of past trades, reflection on regime patterns, hierarchical planning from portfolio-level mandate to ticker-level orders.

### Cemini relevance

- **Architectural reference**, not a direct port. Cemini does not run multi-agent social simulations.
- **Memory stream pattern**: Cemini's per-agent journal logs are a structural cousin (records-then-retrieve-then-reason).
- **Reflection cadence**: Cemini's tradingagents pipeline runs daily / weekly reflection passes that compress recent trades into thesis-level updates. Inherited pattern.
- **Planning hierarchy**: portfolio mandate → strategy → ticker selection → order placement is a 4-tier planning hierarchy directly analogous to the paper's day-hour-minute decomposition.
- **Foundational, not actionable**: documents the lineage of Cemini's long-horizon agent state management. No new work derives from re-reading this paper.

### Beware over-attribution

The paper's headline result (emergent social coordination) is **not** something Cemini's trading agents need or attempt. The architecture is portable; the demonstration goal is not. Avoid framing trading agents as "social" beyond what the trading task literally requires.

## Snippets

> "Believable proxies of human behavior can empower interactive applications ranging from immersive environments to rehearsal spaces for interpersonal communication to prototyping tools. In this paper, we introduce generative agents: computational software agents that simulate believable human behavior." [Source: 2304.03442v2.pdf p.1]
