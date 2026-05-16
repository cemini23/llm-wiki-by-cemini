---
title: Architectural Blueprint for LLM Context Optimization and OpenRouter Integration in Financial Technology Environments
type: source
tags: [source, docx, llm-agents, mcp, context-window, openrouter, prompt-caching, token-optimization, quant-finance, cemini-internal]
keywords: [OpenRouter, context optimization, prompt caching, Aider, claude-code-router, cc-switch, dynamic context pruning, mcp-codebase-index, fintech]
related:
  - sources/openrouter-efficiency-context-audit.md
  - concepts/context-compression-resume-pattern.md
  - concepts/mcp-tool-marketplace.md
  - entities/tools/lazy-tool.md
  - entities/tools/claude-code-router.md
  - entities/tools/cc-switch.md
  - entities/tools/bifrost.md
  - sources/llm-proxy-context-reduction.md
  - concepts/mcp-context-optimization.md
maturity: validated
read_status: deep-read
created: 2026-05-09
updated: 2026-05-11
---

## Relations

- @sources/llm-proxy-context-reduction.md — sibling document; covers MCP proxy comparison (Bifrost vs lazy-tool) and gateway deployment
- @concepts/context-compression-resume-pattern.md — the CPR pattern addresses context-window bloat from a state-persistence angle
- @concepts/mcp-tool-marketplace.md — MCP tool-surface evaluation rubric
- @entities/tools/claude-code-router.md — primary proxy recommendation for OpenRouter traffic routing
- @entities/tools/cc-switch.md — alternative Rust-based SSE-fixing proxy
- @entities/tools/bifrost.md — MCP gateway with Code Mode
- @entities/tools/lazy-tool.md — MCP proxy for lazy tool discovery
- @concepts/openclaw-security-taxonomy.md — security context for proxy-layer tool routing

## Raw Concept

Ingested 2026-05-09 from `research to be indexed/OpenRouter Efficiency & Context Audit.docx` (46,217 chars). The document is a comprehensive architectural audit (not tied to a specific arXiv ID or DOI) focused on bypassing the Claude Code desktop's artificial 200K-token context ceiling, optimizing OpenRouter token economics, and selecting optimal proxy/pruning tooling for a solo developer running a Python fintech platform.

## Narrative

### Problem Statement

Two intertwined challenges for solo developers running LLM-based fintech platforms:

1. **Artificial context ceiling** — Claude Code desktop enforces a hard ~200K-token limit even though the underlying Anthropic API supports 1M tokens. Root cause: the `CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE` environment variable (historically set to 197000) persists in shell profiles and is silently enforced by the client-side application logic.
2. **Token cost explosion** — Without aggressive caching and pruning, routing large codebases and tool schemas through OpenRouter is economically unviable.

### Key Technical Findings

#### Bypassing the 200K Ceiling
- Use the **CLI** (`claude` binary), not the Desktop GUI — the CLI correctly identifies the 1M context window
- Purge `CLAUDE_CODE_BLOCKING_LIMIT_OVERRIDE` from `.bashrc`/`.zshrc` and fully restart the shell
- Auto-compact OFF in v2.1.7 causes crashes at 165K tokens — use explicit proxy-based context management instead

#### Three-Layer Optimized Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Core Client | **Aider** | Terminal-native, AST-based Repo Map for codebase-aware context (replaces Claude Code UI) |
| Routing | **claude-code-router** (Node.js) or **cc-switch** (Rust) | Local proxy for dynamic model switching, OpenRouter header injection, failover routing |
| Pruning | **opencode-dynamic-context-pruning (DCP)** | `Compress` tool for LLM-driven context summarization; `Purge Errors` strategy for traceback bloat |
| MCP Gateway | **Bifrost** + **mcp-codebase-index** | Codebase parsed into metadata; only targeted symbol lookups sent to LLM (87% token reduction) |

#### OpenRouter Caching Economics

- **Response Caching**: `X-OpenRouter-Cache: true` header returns cached responses at zero cost; `X-OpenRouter-Cache-TTL: 3600` extends retention to 1 hour
- **Prompt Caching**: Anthropic's `cache_control: { type: "ephemeral", ttl: "1h" }` on system prompt blocks; 1.25× write cost for 5min TTL, 2.0× for 1h TTL; reads at 0.1× base cost
- **Economic break-even**: Writing 100K tokens to 1h cache is only profitable if queried >2 times within the hour
- **Cache invalidation**: modifying tool definitions or any character in the system prompt busts the entire downstream cache

#### Context Pruning Comparison

| Tool | Mechanism | Cache Impact |
|------|-----------|-------------|
| opencode-dynamic-context-pruning (DCP) | LLM-driven Compress tool; range/message modes | ~5% cache hit rate drop |
| pi-context-prune | Turn-end summarization with side-index | Additional API call latency |
| OpenRouter native middle-out | Blind central truncation | Destructive; breaks reasoning models |

### Aider as Primary Client

Aider is the recommended client for this stack because:
- **Repo Map**: AST-based PageRank-style ranking sends only relevant files (default `--map-tokens 1000`), avoiding raw file dumps
- **Native caching**: `--cache-prompts` organizes chat history to maximize Anthropic prefix cache hits
- **Keepalive**: `--cache-keepalive-pings 12` maintains warm caches during manual review pauses
- **Bypasses desktop UI**: No hard 200K ceiling

### Cited Works

- claude-code-router: https://github.com/musistudio/claude-code-router
- cc-switch: https://github.com/farion1231/cc-switch
- opencode-dynamic-context-pruning: https://github.com/Opencode-DCP/opencode-dynamic-context-pruning
- Aider Repo Map: https://aider.chat/docs/repomap.html
- Aider prompt caching: https://aider.chat/docs/usage/caching.html
- OpenRouter prompt caching: https://openrouter.ai/docs/guides/best-practices/prompt-caching
- mcp-codebase-index: referenced in lazy-tool evaluation sister document