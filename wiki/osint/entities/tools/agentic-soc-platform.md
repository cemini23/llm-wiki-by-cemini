---
title: agentic-soc-platform — Redis Stream + LangGraph Reference Pattern (MIT)
type: entity
tags: [llm-agents, redis-streams, langgraph, multi-agent, mit, steal-from, architecture-reference]
keywords: [agentic-soc-platform, redis-stream-pattern, langgraph-pattern, sirp, multi-agent-orchestration, queue-flushing]
related:
  - sources/links-2-5-4-tool-eval.md
  - entities/tools/atlas-gic-autoresearch.md
maturity: draft
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/links-2-5-4-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 5, **Steal-from** tier verdict
- @entities/tools/atlas-gic-autoresearch.md — different multi-agent architecture (Darwinian autoresearch vs SIRP-pattern Redis-streams); both use LangGraph for state management

## Raw Concept

Localized SIRP (Security Incident Response Platform) using Python + LangGraph + Redis Streams. Security-domain content is irrelevant to Cemini, but the **architectural pattern for high-velocity stream processing** transfers cleanly. Identified as **Steal-from-tier** in the 2026-05-04 Gemini DR eval.

## Narrative

- **URL**: https://github.com/FunnyWolf/agentic-soc-platform
- **License**: MIT (clean for IP-sale)
- **Stack**: Python 100%, Redis Streams, LangGraph, Dify, Nocoly platform (proprietary frontend dependency)
- **Maturity**: 784 stars, 254 commits, v0.3.0 released 2026-04-08

### Why Steal-from

The architectural runtime is a **near-exact mirror of Cemini's Python + LangGraph + Redis stack**. The security domain (SIEM alerts, firewall modifications) is wrong, but the queue / state / orchestrator topology is right.

Specifically extractable:

1. **Redis Stream consumer patterns** — how the platform handles persistent message queuing, backpressure, dead-letter routing
2. **LangGraph state-management methodologies** — multi-stage agent topology with intermediate state persistence
3. **Memory-release / queue-flushing protocols** — defensive patterns to prevent OOM on long-running 24/7 streams
4. **Webhook ingestion patterns** — generalizable to any external-event-driven trading signal

### What to ignore

- **Nocoly platform dependency** — proprietary frontend, irrelevant to Cemini's headless architecture. Skip entirely.
- **Security-domain agent prompts** — wrong domain.
- **Wholesale deployment** — would consume too much RAM on the 4 GB librarian and is irrelevant to either trading or wiki layers.

### Adaptation work

Read the source statically for architectural patterns; do **not** attempt to deploy. Re-apply the Redis Stream + LangGraph patterns within `agents/orchestrator.py` to harden Cemini's existing 4-node StateGraph against:

- API latency / partial-failure scenarios
- Long-running queue exhaustion
- State checkpointing across multi-agent decisions

### Caveats

- Redis Stream memory consumption requires "highly disciplined memory management to prevent out-of-memory kernel panics on the 7 GB RAM primary trading server" [Source: links 2 5_4.docx URL 5]
- Performance metrics during peak load not yet verified [OPEN QUESTION 2026-05-04]

## Snippets

- **Stack alignment**: "The integration of a purely Python environment, LangGraph orchestration, and a Redis message queue perfectly mirrors the exact infrastructure Cemini utilizes for processing high-velocity, 24/7 cryptocurrency market intelligence." [Source: links 2 5_4.docx URL 5]

- **Recommendation tier**: "Steal-from. The architectural runtime matches Cemini's rigid constraints flawlessly, but the security domain is entirely incorrect. The developer should actively lift the Redis Stream processing functions and LangGraph state schemas to harden the financial intelligence ingestion layer." [Source: links 2 5_4.docx URL 5]
