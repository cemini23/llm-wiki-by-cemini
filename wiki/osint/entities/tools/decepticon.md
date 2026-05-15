---
title: "Decepticon — Autonomous Red-Team Multi-Agent Framework (PurpleAILAB)"
type: entity
tags: [security, red-team, multi-agent, langgraph, neo4j, litellm, apache, steal-from-tier]
keywords: [decepticon, autonomous-red-team, langgraph-agents, kill-chain, liteLLM-fallback, neo4j, offensive-security]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Steal-from tier, Cybersec wiki primary fit

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). Apache-2.0 licensed, 3.7k stars. Dual-network sandboxed architecture with 16 specialist agents organized by kill chain phase, driven by LangGraph with PostgreSQL + Neo4j dual persistence.

## Narrative

Decepticon dictates the cutting edge of autonomous red-team operations. Key architectural features: formal Rules of Engagement (RoE) generation, OPPLAN creation, interactive tmux session handling for msfconsole and sliver-client, and credentials-aware model fallback chains (Anthropic → Gemini → local Ollama).

**Tier: Steal-from** — extract the LangGraph subagent logic organized by kill chain phase and the LiteLLM model management parameters. The multi-agent topology mirrors /opt/cemini architecture (LangGraph + PostgreSQL) but repurposed for offensive security. Full adoption blocked to prevent conflation of financial state tools with offensive network operations. Apache-2.0 safe for extraction. Cross-wiki routing: document model fallback chain logic in CCC wiki.

**NEEDS VERIFICATION:** "Offensive Vaccine" feedback loop connecting attack telemetry to defensive network configurations.
