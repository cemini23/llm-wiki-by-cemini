---
title: Agent-Toolkit Routing Research Backlog
type: concept
tags: [concept, routing, llm, infra, backlog, k233]
keywords: [routing, failover, kv-capacity, workload-aware, provider-proxy, backlog]
related:
  - sources/arxiv-2608.11152-mixed-rl-rollouts-2026-08-12.md
  - sources/newsletter-pragmatic-engineer-optiver-2026-08-11.md
  - sources/newsletter-pragmatic-engineer-charity-majors-ai-2026-08-12.md
  - concepts/agent-harness-verification-bottleneck.md
  - entities/tools/opencodex.md
  - entities/tools/quotio.md
  - entities/tools/reasoning-bank.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/prop-trading-engineering-2026.md
  - entities/tools/codex-self-improving-loop.md
  - entities/tools/sentrux.md
tags: [concept, routing, llm, infra, backlog, k233, k234]
updated: 2026-08-12
---

## Relations

- @sources/arxiv-2608.11152-mixed-rl-rollouts-2026-08-12.md — MISA-T
- @sources/newsletter-pragmatic-engineer-optiver-2026-08-11.md — AI gateway + MCP hosting platform
- @sources/newsletter-pragmatic-engineer-charity-majors-ai-2026-08-12.md — harness > model; verification bottleneck (K234)
- @concepts/agent-harness-verification-bottleneck.md
- @entities/tools/opencodex.md — GO Integrate provider proxy
- @entities/tools/quotio.md — quota-aware failover
- @entities/tools/reasoning-bank.md — WATCH
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @concepts/prop-trading-engineering-2026.md
- @entities/tools/codex-self-improving-loop.md
- @entities/tools/sentrux.md

## Raw Concept

What this page answers: what routing-related research/patterns the agent-toolkit lane (llm-routing-deepseek-openrouter-failover) should track next. Accumulated from K233–K234 sources.

## Narrative

**Backlog bump (K233):**

1. **MISA-T (arXiv 2608.11152)** — workload-aware KV-capacity + residency-time-aware admission for mixed RL rollout serving (+53.3% throughput over sweep-tuned vLLM router). Research relevance: heterogeneous agentic sessions competing for KV/capacity need priority/weight-aware admission, not just latency/cache optimization. Not a prod wiring — RL-post-training infra.
2. **opencodex (K233 GO Integrate)** — universal provider proxy unifying Codex/Claude Code/Grok lanes across Anthropic/Gemini/Grok/DeepSeek/Ollama; candidate to consolidate the DeepSeek/OpenRouter failover surface.
3. **Quotio (K233 Extract)** — quota-aware round-robin/fill-first failover pattern for stall-proof token-heavy sessions.
4. **Optiver AI gateway + MCP hosting platform** — industry blueprint of the "models-as-a-service + agent tool layer" pattern this workspace approximates with conductor + MCP tools; validates the direction.

**Backlog bump (K234):**

5. **Charity Majors / harness verification** — harness infrastructure and post-generate verification beat model-chasing; maps to `/route` SIP Verify gate. See `@concepts/agent-harness-verification-bottleneck.md`.

Any of these being wired to prod requires a separate `/phase1` proposal — this page is the tracking surface, not a wire.

[Source: arXiv 2608.11152; Pragmatic Engineer 2026-08-11 + 2026-08-12; K233 eval]
