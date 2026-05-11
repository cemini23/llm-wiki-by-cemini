---
title: lazy-tool
type: entity
tags: [entity, tool, mcp, proxy, lazy-loading, context-optimization, go, local-first]
keywords: [lazy-tool, MCP proxy, lazy loading, search mode, BM25, SQLite, rpgeeganage, token optimization]
related:
  - sources/llm-proxy-context-reduction.md
  - sources/openrouter-efficiency-context-audit.md
  - concepts/mcp-tool-marketplace.md
  - entities/tools/bifrost.md
  - entities/tools/claude-code-router.md
  - concepts/context-compression-resume-pattern.md
  - concepts/mcp-context-optimization.md
  - entities/tools/cc-switch.md
  - entities/tools/9router.md
maturity: validated
created: 2026-05-09
updated: 2026-05-11
adopted: 2026-05-09
version: 1.0.2
repo: https://github.com/rpgeeganage/lazy-tool
license_verified: MIT
---

## Relations

- @sources/llm-proxy-context-reduction.md — primary source evaluating lazy-tool vs Bifrost vs Agent Gateway
- @sources/openrouter-efficiency-context-audit.md — sibling audit covering complementary OpenRouter caching strategy
- @concepts/mcp-tool-marketplace.md — lazy-tool is a key entry in the MCP gateway/tool-surface evaluation
- @entities/tools/bifrost.md — evaluated alternative; Bifrost is more powerful but higher complexity
- @entities/tools/claude-code-router.md — complementary proxy layer for OpenRouter traffic routing
- @entities/tools/9router.md — K38 evaluation candidate DOWNGRADED to NO-GO 2026-05-11; eval brief framed 9router as a compression proxy, but Phase-0 audit found its 20-40% compression overlaps with lazy-tool's validated 46% at ~10× heavier footprint
- @concepts/context-compression-resume-pattern.md — addresses the same context-window bloat problem from a state-persistence angle

## Raw Concept

**What prompted this page**: The MCP eager-loading problem (tool schemas consuming 40%+ of context windows) is the #1 architectural blocker for deploying multi-tool LLM agents in the Cemini stack. The `llm-proxy-context-reduction.md` source (K34 ingest) identified lazy-tool as the best-fit solution for a solo developer on Mac Studio + single VPS.

**Which sources synthesize into this**: `llm-proxy-context-reduction.md` (primary), `openrouter-efficiency-context-audit.md` (complementary caching strategy).

## Narrative

### What It Is

lazy-tool is a **local-first MCP proxy** built in Go by rpgeeganage, explicitly designed to solve the MCP tool sprawl / context window exhaustion problem. It requires zero external dependencies — no Docker, no Node.js, no PostgreSQL, no vector database.

### Key Architecture

- **Runtime**: Single Go binary, executable directly from shell. No container runtime required.
- **Storage**: Local SQLite database generated dynamically upon indexing. Zero infrastructure to maintain.
- **Discovery Protocol**: 5 meta-tools that replace the full tool catalog in the system prompt:
  - `search_tools` — query the SQLite index by keyword
  - `inspect_capability` — retrieve full JSON schema of a discovered tool
  - `invoke_proxy_tool` — proxy execution to upstream server
  - `get_proxy_prompt` — fetch prompt templates from upstream servers
  - `read_proxy_resource` — read static resources from upstream servers
- **Search Algorithm**: Hybrid BM25 lexical search (FTS5) + optional cosine-similarity vector search. Scoring: 10pts exact name match, 8pts exact upstream name, 2pts substring/tag, up to 6pts semantic similarity, plus history/favorite boosts.

### Benchmarks (from source document)

| Metric | Direct MCP | lazy-tool | Improvement |
|--------|-----------|-----------|-------------|
| Input tokens/turn | 1,701 | 915 | **46% reduction** |
| Per-turn latency | baseline | 0.158s | **32% reduction** |

### Installation

```bash
# Primary method (shell script)
curl -sSfL https://raw.githubusercontent.com/rpgeeganage/lazy-tool/main/install.sh | sh

# Alternative: compile from source (requires Go 1.25+)
go install github.com/rpgeeganage/lazy-tool/cmd/lazy-tool@latest
```

### Deployment Steps

1. **Index**: `lazy-tool reindex` — reads `claude_desktop_config.json`, connects to all configured MCP servers, builds SQLite index
2. **Verify**: `lazy-tool search "kalshi"` — confirm Kalshi endpoints are mapped
3. **Serve**: `lazy-tool serve --transport http --addr :8080` — runs as persistent HTTP daemon
4. **Configure client**: In Claude Desktop config, replace direct MCP server entries with a single proxy endpoint pointing to `http://localhost:8080/mcp`

### Why It Matters for Cemini

- **Deterministic execution**: Unlike Bifrost's Code Mode (which generates and executes code on the fly), lazy-tool uses proxy passthrough — the LLM acts as a sequential API caller, not an autonomous programmer. This is **significantly safer** for financial systems where rogue hallucinated scripts could execute unintended trades.
- **Zero configuration**: Reads existing Claude/Cursor configs automatically. No complex JSON definitions or Web UI navigation.
- **Token stability**: By locking the system prompt to 5 static meta-tools, prompt caching (both OpenRouter response caching and Anthropic ephemeral caching) works reliably across long trading sessions.

### Limitations

- No built-in LLM routing (unlike Bifrost). Relies on client or external providers for model selection.
- Proxy passthrough paradigm means the LLM cannot autonomously orchestrate multi-step workflows in a single turn (requires multiple round-trips).
- Community-maintained project — evaluate long-term maintenance trajectory before production deployment.

## Adoption (2026-05-09)

- **Install**: `curl -sSfL https://raw.githubusercontent.com/rpgeeganage/lazy-tool/main/install.sh | INSTALL_DIR=$HOME/.local/bin sh` — v1.0.2 (ff5bdab) on macOS arm64
- **Config**: `~/.lazy-tool/config.yaml` with 7 MCP sources (conductor, kb-server, brave-search, playwright, prod-mcp, librarian-stash, stash)
- **Reindex**: 31 tools indexed from 3 reachable servers; 4 tunnel-dependent servers fail (expected — require SSH tunnels active)
- **License**: MIT verified via GitHub
- **Stars**: 20 (single-maintainer — monitor for stagnation)
- **Status**: Installed + configured; .mcp.json NOT yet switched to lazy-tool proxy (requires tunnel-aware migration)