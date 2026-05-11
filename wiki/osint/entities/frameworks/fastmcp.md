---
title: FastMCP
type: entity
tags: [framework, mcp, llm-tooling, python]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - concepts/skill-vetting.md
  - entities/frameworks/langgraph.md
  - entities/infrastructure/deepseek-api.md
  - sources/4-5-links.md
  - entities/frameworks/autoagent.md
  - concepts/wiki-tooling-evaluation.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/willynikes2-knowledge-base-server.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - concepts/ai-organisation-design.md
  - concepts/mcp-tool-marketplace.md
  - sources/playwright-mcp-microsoft.md
  - sources/sentrux-ast-sensor.md
  - sources/vibe-trading-hkuds.md
  - sources/4-5-links-2.md
  - sources/agent-browser-vercel-labs.md
  - sources/piebald-claude-code-system-prompts.md
  - sources/3-26-b.md
  - sources/3-26-link-re-3.md
  - sources/wave-5-1-link-eval-more.md
  - sources/4-3-link-re-2.md
  - sources/3-29-research-6.md
  - concepts/agent-identity-protocol.md
  - sources/3-17-agent-research.md
  - sources/3-25-git-research.md
  - sources/git-3-5-pt3.md
  - concepts/mcp-context-optimization.md
  - concepts/mitre-atlas-taxonomy.md
  - entities/tools/guidance-ai.md
maturity: validated
created: 2026-04-23
updated: 2026-05-11
---

## Relations

- @sources/3-19-compliance-research.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @concepts/skill-vetting.md
- @entities/frameworks/langgraph.md
- @entities/infrastructure/deepseek-api.md — LLM brain that consumes MCP-exposed tools
- @sources/4-5-links.md — K8 deep-read 2026-04-28 — Cemini-internal evaluation doc. K8 server-probe finding: **130 registered `@mcp.tool` decorators** (vs the doc's "22" claim, ~6× over). **[UPDATE 2026-04-30 K11]**: FastMCP upgraded to **3.1.0**; MCP code restructured from `services/cemini_mcp/` → `/opt/cemini/cemini_mcp/server.py` (2,536 lines); current tool registration count ~30 lines matching `mcp.tool` — down from K8's 130, reflecting code consolidation and FastMCP 3.x API changes. The growth in tool count amplifies the doc's prescription to consolidate FastMCP tools into a hot-reloadable single-file registry behind a fixed adapter boundary
- @entities/frameworks/autoagent.md — K8 promotion 2026-04-28 — Single-File Registry-Driven Harness pattern is the named architectural recipe for consolidating the 130 `@mcp.tool` decorators into one structured, hot-reloadable file. AutoAgent's pattern is the operative target for the FastMCP tool-registry consolidation work prescribed in K8
- @concepts/wiki-tooling-evaluation.md — 2026-04-28 — wiki-tooling adoption candidates each ship their own MCP server (llm-wiki-compiler: 7 tools / knowledge-base-server: 16 tools / agentmemory: full MCP+REST). Any of them coexists with the deployed `cemini_mcp` (130 `@mcp.tool` decorators here) on a separate transport / endpoint; no integration conflict. Tool-namespace discipline: workspace-side wiki-tooling MCP runs on laptop or stdio; the deployed `cemini_mcp` runs on Hetzner over its own transport
- @sources/atomicmemory-llm-wiki-compiler.md — 2026-04-28 — primary wiki-tooling adoption candidate; ships an MCP server (`llmwiki serve`) with 7 tools (`ingest_source`, `compile_wiki`, `query_wiki`, `search_pages`, `read_page`, `lint_wiki`, `wiki_status`) + 5 resources. Closes the laptop ↔ server gap for the dev-stack DeepSeek brain to query the workspace wiki without re-deploying Track B `wiki_search` server-side
- @sources/willynikes2-knowledge-base-server.md — 2026-04-28 — sibling MCP-server-with-memory-engine candidate; 16 MCP tools + REST API + OpenAPI 3.1 + ChatGPT Custom GPT integration. Heavier integration surface than llm-wiki-compiler; deferred adoption decision
- @sources/agentmemory-rohitg00-cpr-impl.md — 2026-04-28 — Apache-2.0 cpr-pattern reference impl exposes its functionality via MCP server. Pattern is more useful than the runtime for the deployed Python stack; pipeline shape (PostToolUse hook → SHA-256 dedup → privacy filter → LLM compress → BM25+Vector+Graph RRF) ports into Python on the Cemini stack alongside FastMCP tool-call wrappers
- @sources/wave-5-1-link-eval-more.md — Wave 5.1 agent-framework evaluation; Instructor's structured-output extraction pattern integrates via FastMCP `@mcp.tool` decorators on LangGraph nodes
- @sources/4-3-link-re-2.md — K14 deep-read 2026-05-01; references FastMCP tool integration patterns across Docs 1, 3, 4
- @sources/3-29-research-6.md — K15 deep-read 2026-05-01; Formal Tool Safety Typing (side_effects enum + failure_modes mapping) promoted from Paper 6 (Schlapbach)
- @concepts/agent-identity-protocol.md — K15 promotion 2026-05-01; IBCT tokens pass through FastMCP via X-AIP-Token header binding middleware

## Raw Concept

Synthesized from 4 source(s) referencing this entity across the Cemini research corpus. Category: frameworks.

## Narrative

FastMCP is a Python framework for building Model Context Protocol (MCP)
servers — the Anthropic-originated standard for LLM-tool interaction.
Cemini exposes its internal toolkits (position lookup, venue order
submission, historical-data query, risk-check) as MCP servers so that
any MCP-compatible agent (LangGraph supervisors, external clients) calls
them through a uniform, typed, permission-gated interface. `[RETRACTED 2026-04-24]`
Earlier phrasing named "LangGraph DeepSeek-R1 agents" as the caller —
DeepSeek/Ollama are not deployed on Cemini; the MCP servers are
LLM-agnostic by design, which is the point of the protocol.

**Deployed version (server probe 2026-04-30 K11)**: FastMCP **3.1.0**
(upgraded from ~2.x referenced in K8/K9/K10 docs — major version bump).
MCP code lives at `/opt/cemini/cemini_mcp/server.py` (2,536 lines;
restructured from the earlier `services/cemini_mcp/` path). ~30 tool
registration lines (consolidated from K8's 130 — reflects FastMCP 3.x
API changes + code reorganization). Container: `cemini_mcp` (image
`cemini-mcp:latest`, healthy).

Why FastMCP matters to the IP-sale thesis: MCP is the emerging
cross-vendor tooling standard. By wrapping all Cemini capabilities
behind MCP servers, the acquiring firm can plug in any compliant MCP
client (Claude, GPT-class models, their own fine-tunes, or a future
local model) without rewriting the tool layer. This decouples the
trading logic from any single LLM provider — a deal-favorable piece of
forward-compatibility.

### Formal Tool Safety Typing (K15 — Paper 6, Schlapbach et al.)

Standard MCP tools lack machine-readable safety flags. A `submit_kalshi_order` tool and a `get_portfolio` tool are indistinguishable at the schema level — both are just `@mcp.tool` decorators. The paper proves this is a critical expressivity gap in the MCP spec and proposes a type-system extension with two schema-level annotations:

**side_effects enum** — embedded in Pydantic v2 tool schema metadata via `Field(json_schema_extra={...})`. Three strict states:
- `read-only` — no side effects, safe for autonomous execution (e.g., `get_portfolio`)
- `idempotent` — repeated calls produce the same result (e.g., `check_order_status`)
- `destructive` — irreversible side effects, requires explicit approval (e.g., `submit_kalshi_order`)

A `requires_approval` boolean accompanies destructive tools. The LangGraph supervisor reads these flags during tool discovery and automatically injects a human-in-the-loop interruption or IBCT token validation before permitting execution.

**failure_modes array** — each tool formally enumerates expected error conditions (`ErrorType`) with explicit machine-readable recovery strategies (`RecoveryStrategy`):
- `Retry(n)` — retry with exponential backoff up to n attempts
- `Fallback(tool)` — invoke an alternative tool (e.g., `check_order_status` fallback on `execute_trade` timeout)
- `Abort` — terminate the current workflow, notify operator

This eliminates the LLM guessing how to recover from tool errors. When a Robinhood API timeout occurs, the tool schema itself instructs the agent to invoke `check_order_status` before attempting a retry.

**CI/CD enforcement via Semgrep** — custom Semgrep rules verify that every `@mcp.tool` decorator includes a defined `side_effects` parameter and a valid `failure_modes` mapping. The GitHub Actions pipeline fails automatically if a new destructive trading tool is merged without the required approval workflows declared in its schema. Implementation: ~3h to write the Semgrep rules.

**Progressive disclosure** — tools provide lightweight summaries for discovery (read by the LangGraph router to select agents) and only reveal full token-heavy schemas on actual invocation. Preserves context window budget during the routing phase.

This pattern affects every `@mcp.tool` decorator in the Cemini stack — it's a schema-level architectural change, not a per-tool annotation. Paired with @concepts/agent-identity-protocol.md (IBCT header binding), it provides defense-in-depth: the schema declares what's safe, and the cryptographic token chain enforces who can execute what.

## Snippets

*(populate as source stubs are deep-read.)*
