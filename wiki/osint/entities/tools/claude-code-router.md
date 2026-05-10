---
title: claude-code-router
type: entity
tags: [entity, tool, proxy, openrouter, nodejs, routing, caching, claude-code]
keywords: [claude-code-router, proxy, OpenRouter, model routing, caching, failover, Node.js]
related:
  - sources/openrouter-efficiency-context-audit.md
  - sources/llm-proxy-context-reduction.md
  - entities/tools/cc-switch.md
  - entities/tools/lazy-tool.md
  - entities/tools/bifrost.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
created: 2026-05-09
updated: 2026-05-09
adopted: 2026-05-09
version: 2.0.0
repo: https://github.com/musistudio/claude-code-router
license_verified: MIT
---

## Relations

- @sources/openrouter-efficiency-context-audit.md — primary source evaluating claude-code-router as the routing layer in the optimized Cemini stack
- @sources/llm-proxy-context-reduction.md — sibling document covering MCP gateway alternatives
- @entities/tools/cc-switch.md — alternative proxy with complementary SSE-fixing capabilities
- @entities/tools/lazy-tool.md — the MCP gateway recommended alongside claude-code-router for the full stack
- @entities/tools/bifrost.md — MCP gateway alternative; Bifrost handles MCP routing, claude-code-router handles LLM API routing
- @concepts/mcp-tool-marketplace.md — proxy/routing layer in the broader MCP tool ecosystem

## Raw Concept

**What prompted this page**: claude-code-router is the recommended OpenRouter traffic proxy in the `openrouter-efficiency-context-audit.md` source (K34 ingest). It solves dynamic model switching, header injection for caching, and automatic failover — all critical for the Cemini stack's economic viability.

**Which sources synthesize into this**: `openrouter-efficiency-context-audit.md` (primary).

## Narrative

### What It Is

claude-code-router is a **local-first Node.js proxy** that intercepts and translates requests between Claude Code and various OpenAI-compatible or Anthropic-compatible endpoints, including OpenRouter. Runs as a lightweight background daemon (typically port 3456 or 8787).

Repository: https://github.com/musistudio/claude-code-router

### Key Capabilities

- **Dynamic Model Switching**: Route different tasks to different models without altering CLI config or restarting sessions. Example: simple file reads → `qwen3-30b-a3b`; complex crypto implementation → `claude-3.5-sonnet`.
- **Environment Variable Interpolation**: API keys injected via `${OPENROUTER_API_KEY}` in config, avoiding hardcoded secrets.
- **Failover Routing**: If primary Anthropic endpoint is rate-limited, automatically fails over to a secondary OpenRouter provider (e.g., DeepSeek V3) without disrupting the active session.
- **Header Injection**: Can inject `X-OpenRouter-Cache: true` and other caching metadata into outgoing requests.

### Why It Matters for Cemini

In the recommended Cemini stack, claude-code-router serves as the **routing infrastructure layer** (Layer 2 of the three-layer stack from `openrouter-efficiency-context-audit.md`):

1. **Decouples client from provider**: The terminal-based Aider client sends requests to claude-code-router, which handles all OpenRouter communication. This means the developer never hardcodes provider URLs or API keys in the CLI config.
2. **Enables caching headers**: The proxy injects `X-OpenRouter-Cache: true` and `X-OpenRouter-Cache-TTL: 3600` into all requests, enabling OpenRouter's response caching mechanism.
3. **Ensures high availability**: Automatic failover means a rate limit or outage on one provider doesn't halt the trading platform.

### Configuration

JSON config (`~/.claude-code-router/config.json`):
```json
{
  "Providers": [
    {
      "name": "openrouter_primary",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "${OPENROUTER_API_KEY}",
      "models": ["anthropic/claude-3.5-sonnet"]
    },
    {
      "name": "openrouter_fallback",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "${OPENROUTER_API_KEY}",
      "models": ["deepseek/deepseek-v3"]
    }
  ],
  "Routing": {
    "strategy": "failover",
    "primary": "openrouter_primary",
    "fallback": "openrouter_fallback"
  }
}
```

### Limitations

- **Node.js dependency**: Requires Node.js runtime on the host machine.
- **OpenRouter-specific**: Tightly coupled to OpenRouter's API format; switching to a different aggregator would require config changes.
- **Manual config**: Provider definitions must be authored and maintained in JSON — no auto-discovery of available models.

### Complementary Tools

- **cc-switch**: Rust-based alternative that excels at SSE stream repair and hop-by-hop header stripping. Use cc-switch if the primary pain point is streaming compatibility rather than dynamic routing.
- **lazy-tool**: Handles MCP tool schema bloat at the protocol layer; claude-code-router handles LLM API routing at the transport layer. They operate at different levels and are used together.

## Adoption (2026-05-09)

- **Install**: `npm install -g @musistudio/claude-code-router` — v2.0.0, binary `ccr` at `~/.local/bin/ccr`
- **Repo**: `github.com/musistudio/claude-code-router` (33.7K stars, MIT) — NOTE: brief originally referenced `1rgs/claude-code-router`; actual repo is `musistudio/claude-code-router`. The `1rgs/claude-code-proxy` exists (3K stars, Python) but is a different tool (Anthropic→OpenAI/Gemini proxy, not OpenRouter caching router).
- **License**: MIT verified via GitHub API
- **Stars**: 33,733 — strong community adoption, low abandonment risk
- **Status**: Installed. Limited utility for current Cemini stack (DeepSeek direct API). Activates if/when switching to OpenRouter for caching + failover.