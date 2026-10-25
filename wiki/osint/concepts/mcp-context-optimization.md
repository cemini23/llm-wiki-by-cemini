---
title: MCP Context Window Optimization
type: concept
tags: [concept, mcp, context-window, token-optimization, lazy-loading, prompt-caching, openrouter, llm-agents]
keywords: [MCP context optimization, eager loading, lazy loading, context window bloat, token optimization, prompt caching, OpenRouter, Bifrost, lazy-tool]
related:
  - sources/llm-proxy-context-reduction.md
  - sources/openrouter-efficiency-context-audit.md
  - entities/tools/lazy-tool.md
  - entities/tools/bifrost.md
  - entities/tools/claude-code-router.md
  - entities/tools/cc-switch.md
  - concepts/context-compression-resume-pattern.md
  - concepts/mcp-tool-marketplace.md
  - concepts/llm-agent-systems.md
  - sources/4-5-links.md
  - sources/wave-5-1-link-eval-stacks.md
  - entities/frameworks/fastmcp.md
  - sources/tool-attention.md
  - sources/arxiv-inference-scaling-llms-2605.19775.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/self-compacting-language-model-agents.md
  - entities/tools/headroom.md
maturity: draft
created: 2026-05-09
updated: 2026-10-25
---

## Relations

- @sources/llm-proxy-context-reduction.md — primary source: MCP proxy comparison (Bifrost vs lazy-tool vs Agent Gateway) and lazy loading strategies
- @sources/openrouter-efficiency-context-audit.md — primary source: OpenRouter caching, client-side context ceiling bypass, pruning tooling
- @entities/tools/lazy-tool.md — recommended MCP proxy for Cemini's solo-dev deployment
- @entities/tools/bifrost.md — evaluated enterprise MCP gateway alternative
- @entities/tools/claude-code-router.md — OpenRouter routing proxy for caching header injection
- @entities/tools/cc-switch.md — SSE streaming repair proxy
- @concepts/context-compression-resume-pattern.md — complementary state-persistence approach to the same problem space
- @concepts/mcp-tool-marketplace.md — tool-surface evaluation rubric that MCP context optimization feeds into
- @concepts/llm-agent-systems.md — parent cluster; this concept sits in the "MCP tool surface" and "Memory / context architectures" sub-topics
- @entities/frameworks/fastmcp.md — the MCP framework Cemini deploys; context optimization wraps around its tool surface
- @sources/4-5-links.md — K8 source that first identified context window as a production constraint on the Cemini stack
- @sources/wave-5-1-link-eval-stacks.md — Wave 5 evaluation context where these optimizations matter
- @sources/arxiv-inference-scaling-llms-2605.19775.md — reasoning workloads hit KV capacity wall (orthogonal to MCP tool bloat)

## Raw Concept

**What prompted this page**: Eager loading of MCP tool schemas is the #1 context-window bloat vector for the Cemini stack. A pair of documents (K34 ingest, 2026-05-09) provided a comprehensive architectural analysis of this problem and a full stack of solutions. This concept page synthesizes the key patterns into an actionable reference for Cemini's deployment architecture.

**Which sources synthesize into this**: `llm-proxy-context-reduction.md`, `openrouter-efficiency-context-audit.md` (both K34 ingest, 2026-05-09).

## Narrative

### The Core Problem

The Model Context Protocol (MCP) standard lets AI agents discover and invoke tools via a shared interface. However, the default implementation uses **eager loading**: every connected MCP server injects its full JSON schema catalog into the system prompt at session initialization. For Cemini's stack (Kalshi trading engine + custom Python bots + ~150 tools), this means:

- **200–500 tokens per tool schema** × 150 tools = 30,000–75,000 tokens burned before any user query
- **32% per-turn latency penalty** from "lost in the middle" effect
- **Prompt caching invalidation**: every tool connect/disconnect rewrites the system prompt, busting the KV cache on every turn
- **Hard client ceiling**: Claude Code desktop enforces ~200K tokens even though the API supports 1M

At OpenRouter pricing, this eager-loading overhead alone can push per-session costs from cents to dollars for high-frequency trading workflows.

### The Solution Stack

The following layered approach addresses the problem at every level:

#### Layer 1: Lazy-Loading Proxy (MCP Protocol Layer)

Replace eager schema injection with **lazy discovery** via a local MCP proxy.

**Recommended tool**: [lazy-tool](entities/tools/lazy-tool.md)
- Single Go binary, zero dependencies, reads existing `claude_desktop_config.json`
- Replaces the full tool catalog with 5 meta-tools (search, inspect, invoke, prompt, resource)
- Hybrid BM25 + vector retrieval against local SQLite index
- **46% reduction in input tokens, 32% reduction in per-turn latency**

**Alternative**: [Bifrost](entities/tools/bifrost.md)
- More powerful (Code Mode with autonomous script execution)
- Higher complexity (PostgreSQL + Docker + Kubernetes orientation)
- Better suited for multi-developer team deployments

#### Layer 2: LLM API Proxy (Transport Layer)

Route all LLM traffic through a local proxy for caching headers, model switching, and failover.

**Recommended tool**: [claude-code-router](entities/tools/claude-code-router.md)
- Dynamic model routing (simple tasks → cheap models, complex tasks → capable models)
- Injects `X-OpenRouter-Cache: true` and `X-OpenRouter-Cache-TTL: 3600` headers
- Automatic failover to secondary providers on rate limit

**Alternative**: [cc-switch](entities/tools/cc-switch.md)
- Focused on SSE streaming repair through OpenRouter
- Rust zero-dependency binary
- Narrower scope but critical for streaming reliability

#### Layer 3: Client-Side Optimizations

- **Use CLI, not Desktop GUI**: The `claude` CLI correctly uses the 1M-token context window; the desktop enforces 200K
- **Purge `CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE`**: This ghost environment variable is the root cause of the artificial ceiling
- **Use Aider as primary client**: AST-based Repo Map sends only relevant code (not full file dumps), `--cache-prompts` maximizes prefix cache hits, `--cache-keepalive-pings` maintains warm caches
- **Dynamic Context Pruning (DCP)**: LLM-driven `Compress` tool that summarizes completed work and purges error tracebacks after configurable turns

#### Layer 4: OpenRouter Caching Strategy

- **Response Caching**: `X-OpenRouter-Cache: true` → zero-cost cache hits for identical requests (ideal for unit test suites, repeated evaluations)
- **Prompt Caching (Anthropic)**: `cache_control: { type: "ephemeral", ttl: "1h" }` on static system prompt blocks; write at 2× cost, read at 0.1× cost
- **Economic break-even**: 100K-token cache write is profitable only if queried >2 times per TTL window
- **Cache architecture**: Place volatile data (terminal output, stack traces) at the END of the prompt; keep static prefixes (tool definitions, system instructions) at the beginning to maximize cache longevity

### The Three Caches (In Invalidation Order)

1. **OpenRouter Response Cache** — cheapest, zero-cost hits, invalidated by any prompt change
2. **OpenRouter Edge Cache** — provider-sticky routing required, invalidated by model/routing changes
3. **Anthropic KV Cache** — `cache_control` ephemeral markers, invalidated by any character change in cached prefix

Lazy-tool's approach of **locking the system prompt to 5 static meta-tools** means caches 1–3 all remain stable for the duration of a session, since the tool surface never changes regardless of how many upstream MCP servers are configured.

### Key Insight

The lazy-tool approach doesn't just reduce tokens — it makes the system prompt **deterministic and cacheable**. This transforms OpenRouter from a cost center into a near-free caching layer: the initial system prompt is written to cache once, and every subsequent turn reads from cache at 0.1× cost. For Cemini's long-running trading sessions, this alone can reduce per-session LLM costs by 80–95%.

### Status

- [ ] Evaluate lazy-tool on Cemini dev stack (install, index, benchmark)
- [ ] Configure claude-code-router with failover routing + caching headers
- [ ] Deploy Aider as primary CLI client with `--cache-prompts --cache-keepalive-pings`
- [ ] Purge `CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE` from `.bashrc`/`.zshrc` on all dev machines
- [ ] Measure before/after token costs on a representative trading session
- [ ] Document results in `briefs/` for CeminiSuite distribution