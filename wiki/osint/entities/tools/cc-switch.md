---
title: cc-switch
type: entity
tags: [entity, tool, proxy, openrouter, rust, sse, streaming]
keywords: [cc-switch, Rust proxy, SSE streaming, OpenRouter, header stripping, zero-dependency]
related:
  - sources/openrouter-efficiency-context-audit.md
  - entities/tools/claude-code-router.md
  - entities/tools/lazy-tool.md
  - entities/tools/bifrost.md
maturity: validated
created: 2026-05-09
updated: 2026-05-09
---

## Relations

- @sources/openrouter-efficiency-context-audit.md — primary source evaluating cc-switch as the SSE-compatible proxy alternative
- @entities/tools/claude-code-router.md — primary comparison target; claude-code-router is Node.js-based with richer routing features, cc-switch is Rust-based with superior streaming compatibility
- @entities/tools/lazy-tool.md — MCP gateway layer; cc-switch operates at a different level (LLM API proxy vs MCP protocol proxy)
- @entities/tools/bifrost.md — another proxy/gateway option; Bifrost is heavier and more feature-rich, cc-switch is lighter and more focused

## Raw Concept

**What prompted this page**: cc-switch is the Rust-based alternative to claude-code-router evaluated in the `openrouter-efficiency-context-audit.md` source (K34 ingest). It solves a specific problem: SSE streaming compatibility when routing Claude Code through OpenRouter.

**Which sources synthesize into this**: `openrouter-efficiency-context-audit.md` (primary).

## Narrative

### What It Is

cc-switch is a **zero-dependency, Rust-based proxy** engineered specifically for high-performance routing of Claude Code requests through OpenRouter. It addresses a critical technical problem: when routing through OpenRouter, Server-Sent Events (SSE) streaming responses from Anthropic models get translated into OpenAI-compatible streaming format, which strict SDK-based clients (like Claude Code's native parser) often reject with HTTP 400 errors.

Repository: https://github.com/farion1231/cc-switch

### Key Capabilities

- **SSE Stream Repair**: Actively strips conflicting hop-by-hop headers and repairs SSE payloads in real-time, preventing HTTP 400 errors from malformed streaming responses.
- **Output Block Filtering**: Dynamically filters out unsupported output blocks (e.g., redacted internal reasoning blocks from thinking models) that would crash the local client's parser.
- **Zero Dependency**: Single Rust binary — no Node.js, no Docker, no external dependencies.
- **System Tray Interaction**: Minimal UI via system tray for configuration and monitoring.

### Why It Exists

The core problem cc-switch solves: OpenRouter acts as a translation layer converting Anthropic's native SSE streaming format into OpenAI-compatible streams. This translation introduces structural discrepancies that strict SDK clients reject. cc-switch sits between the client and OpenRouter, repairing these discrepancies transparently.

### Comparison with claude-code-router

| Dimension | claude-code-router | cc-switch |
|-----------|-------------------|-----------|
| Runtime | Node.js | Rust (zero-dependency binary) |
| Primary strength | Dynamic model switching, failover routing, Web UI | SSE streaming repair, header stripping |
| Configuration | JSON config file | System tray + minimal config |
| OpenRouter integration | Full routing + failover | Focused on streaming compatibility |
| Best for | Multi-model routing + caching strategy | Streaming reliability through OpenRouter |

### Role in the Cemini Stack

cc-switch is the **alternative proxy** choice if the primary concern is streaming reliability rather than dynamic model routing. For Cemini's use case:
- If using Aider in terminal mode with OpenRouter, cc-switch ensures SSE streaming works without HTTP 400 errors
- Could be layered alongside claude-code-router (cc-switch handles SSE repair, claude-code-router handles model routing) — though this adds latency
- Less relevant if routing through Anthropic's API directly (no translation layer needed)

### Limitations

- **Less visual configuration**: No Web UI; configuration is more opaque compared to claude-code-router
- **Narrower scope**: Focused on SSE/streaming repair rather than full routing/failover
- **System tray interaction**: Requires a desktop environment with system tray support