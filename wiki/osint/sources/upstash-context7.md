---
title: "upstash/context7 — Up-to-date Code Documentation for LLMs (TypeScript, MIT client + proprietary backend, 53.7k★)"
type: source
tags: [github, mcp-server, llm-documentation, anti-hallucination, claude-code, typescript, mit-license-client-only, vendor-dependency, gemini-dr-wave4, workflow-adopt]
keywords: [context7, upstash, ctx7, llm-documentation, version-specific-api, mcp-server-bridge, mcp-context7-com, claude-code-skill, cursor-skill, opencode-skill, gemini-cli-skill, ctx7-telemetry-disabled, anti-hallucination-via-docs-injection, polars-langgraph-fastapi-fresh-docs, vendor-dependency-upstash]
clusters: [llm-agents, dev-tooling]
related:
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/alash3al-stash.md
  - sources/piebald-claude-code-system-prompts.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - sources/llms-corrupt-documents-laban-2026.md
  - concepts/mcp-tool-marketplace.md
  - sources/caiovicentino-polymarket-mcp-server.md
maturity: validated
read_status: read-skim
created: 2026-04-30
updated: 2026-05-17
---

## Relations

- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A URL 14 Adopt; promoted to dedicated source in Phase 2 (2026-04-30) as the highest-maturity Wave 4 Adopt by stars (53.7k)
- @concepts/wiki-tooling-evaluation.md — Wave 4 evaluation parent
- @concepts/ip-sale-readiness.md — MIT client clears IP-sale; **but vendor-dependency on proprietary Upstash backend creates a service-availability risk distinct from license risk**
- @concepts/high-signal-paper-patterns.md — rubric: highest-maturity Wave 4 Adopt by every signal (stars, contributors, releases, recent activity)
- @sources/llms-corrupt-documents-laban-2026.md — operationally-paired: LLMs corrupt documents at 25%+ rates partly because of stale-API-knowledge hallucinations. context7's documentation-injection directly mitigates this failure mode for code-domain delegation (where context7 covers the library APIs the LLM is editing). **Pairing**: context7 reduces the input-side hallucination rate; LLMs-Corrupt's round-trip-relay measures the output-side corruption that remains.
- @sources/alash3al-stash.md — Wave 5A Adopt sibling: context7 = "what does the API surface look like *now*" (external knowledge); stash = "what did *this* user/session learn *across time*" (internal episodic memory). Together they form a complete LLM memory stack for Cemini's Wiki/Librarian server.
- @sources/piebald-claude-code-system-prompts.md — Wave 5B Steal-from; **parallel grounding-data pair**. context7 grounds LLMs in current library API documentation (anti-hallucination via fresh docs injection); piebald grounds LLMs in Anthropic's deployed Claude Code system-prompts (anti-improvisation via observed-prompt reference). Both reduce free-form generation in favor of cite-and-anchor patterns. Adopt context7 for code-API grounding; study piebald for harness/agent-prompt design grounding

## Raw Concept

- **URL**: https://github.com/upstash/context7
- **Type**: Open-source CLI + Skill + MCP server (client side); **proprietary backend hosted by Upstash**
- **License**: **MIT (CLIENT ONLY)** — the CLI utility (`ctx7`), MCP adapter, and Skill bundle are MIT-licensed. The backend crawling + parsing engines + documentation index hosted at `mcp.context7.com` are **proprietary and remain entirely with Upstash**.
- **Stars / Forks (Exa-verified 2026-04-30)**: 53,681 ★ / 2,540 forks
- **Stack**: TypeScript 92.7% / JavaScript 7.0% / Dockerfile 0.2%
- **Org**: Upstash (Redis-as-a-service company; ~120 contributors on this repo)
- **Created**: 2025-03-26; **Last push**: 2026-04-24 (very active)
- **Releases**: 67 published; latest `ctx7@0.4.0` 2026-04-24
- **Topics**: llm, mcp, mcp-server, vibe-coding
- **Homepage**: https://context7.com
- **Discovered via**: Gemini DR Wave 4A 2026-04-29 (URL 14); promoted 2026-04-30
- **Read status**: read-skim (Exa-fetched README + Gemini brief; deep-read deferred until Cemini integration scoping)

## Narrative

### What it is

A documentation-injection layer that **mitigates LLM API-hallucination** by retrieving up-to-date, version-specific library documentation on demand. Two integration modes:

1. **CLI + Skills** — installs an agent-callable skill (`ctx7 library`, `ctx7 docs`) that fetches docs without requiring MCP infrastructure
2. **MCP server registration** — registers a Context7 MCP server (`https://mcp.context7.com/mcp`) so Claude Code / Cursor / OpenCode / Gemini CLI agents can call documentation tools natively

MCP tools exposed:
- `resolve-library-id` — turns a general library name into a Context7-compatible library ID (e.g., `/mongodb/docs`, `/vercel/next.js`)
- `query-docs` — retrieves documentation for a library given the resolved ID + a query

### The architectural split — what's open and what's not

The MIT client adapter is open-source. **The heavy lifting (web crawling + documentation parsing + indexing) is entirely proprietary, hosted on Upstash's servers.**

For Cemini, this creates a **two-axis risk model**:
- **License axis**: clean MIT on the client. No Family A/B/C concerns. ✓
- **Service-availability axis**: every documentation query requires a network call to `mcp.context7.com`. If Upstash's service experiences an outage, the local MCP adapter becomes entirely non-functional. **This is a service dependency, not a code dependency**.

### Why Cemini-direct (Workflow only)

**Adopt for laptop Workflow only**. Per the Gemini brief: "the trading stack is a hardened, locked-down execution environment. Allowing the quantitative orchestrator to initiate external HTTP calls to an Upstash documentation server during volatile market hours introduces an unacceptable network failure vector."

Workflow value: when DeepSeek-V4-flash drafts code in the laptop's Claude Code environment (e.g., new quantitative feature using Polars + LangGraph), context7 lets the agent fetch fresh API documentation rather than relying on potentially-stale training-set knowledge. Direct mitigation of the LLM-API-hallucination failure mode that `@sources/llms-corrupt-documents-laban-2026.md` quantified at 25%+ across 19 frontier models.

Concrete laptop-side install:
```bash
npm install -g ctx7
ctx7 setup --claude --mcp           # register as MCP server
export CTX7_TELEMETRY_DISABLED=1     # MUST add to ~/.zshrc
```

### Critical configuration: telemetry disable

**The CLI utility collects anonymous usage telemetry by default.** The Gemini brief flags this explicitly: "To safeguard proprietary research queries from external monitoring, this telemetry must be explicitly disabled."

Mandatory pre-adoption setup:
```bash
echo 'export CTX7_TELEMETRY_DISABLED=1' >> ~/.zshrc
source ~/.zshrc
```

This must be done BEFORE the first `ctx7` invocation. Otherwise proprietary research-query patterns may be transmitted to Upstash before the disable takes effect.

### Risks & open questions

1. **Vendor service dependency** (already covered) — single point of failure on Upstash uptime
2. **Telemetry default-on** — must be explicitly disabled; risk of accidental query-leakage in the window between install and zshrc-source
3. **Data egress policy** [CONFIRMED 2026-05-17] — per Context7's published data-privacy docs (context7.com/docs/security/data-privacy), only the MCP-client-formulated `query` string + `libraryName`/`libraryId` + API key + client metadata + transport type are sent to the Context7 API. The full prompt, source code, and conversation history are NOT transmitted; tool descriptions instruct the client to strip secrets/credentials/proprietary code from the query. Formulated queries are stored anonymously for retrieval benchmarking and passed to OpenAI/Gemini/Anthropic for server-side reranking. Egress is limited to the search query — acceptable for Cemini-laptop dev-doc lookups; the residual concern is that a query string could itself leak a research direction (mitigated by forking the MCP server to edit the query-formulation tool descriptions if needed).
4. **API-key-gated rate limits** — foundational queries are unauthenticated, but advanced/high-volume use requires registration + API key. Cemini-laptop usage should fit in the free tier; verify before relying on it.
5. **Library coverage** — context7's index may not cover every library Cemini uses. For obscure or proprietary libraries (e.g. internal Cemini SDKs), context7 provides no value. Best for popular open-source libraries (Polars, LangGraph, FastAPI, SQLAlchemy, etc.).

### Cemini-side adoption assessment

**Decision: Adopt for laptop Workflow** — highest-maturity Wave 4 Adopt; the documentation-injection pattern directly addresses a known LLM failure mode. Concrete next-steps:

1. License + telemetry audit ✅ done via Exa
2. Install: `npm install -g ctx7` + register as MCP + export `CTX7_TELEMETRY_DISABLED=1` to zshrc ~10 min
3. Use during next code-drafting session against Polars or LangGraph — measure subjective hallucination-rate improvement
4. If improvement is real: keep as default Claude Code MCP for wiki-curation + research workflows
5. **Do NOT install on cemini-prod** — the brief's reasoning is correct (network failure vector during market hours). Workflow scope only.

### Citation

> Upstash. (2025-2026). *Context7 — Up-to-date Code Documentation for LLMs and AI Code Editors*. https://github.com/upstash/context7 (MIT client + proprietary backend; ctx7@0.4.0 latest 2026-04-24; 53.7k stars)

## Snippets

> **Mission framing**:
>
> "Context7 Platform — Up-to-date code documentation for LLMs and AI code editors. CLI + Skills — installs a skill that guides your agent to fetch docs using ctx7 CLI commands (no MCP required). MCP — registers a Context7 MCP server so your agent can call documentation tools natively." [Source: https://github.com/upstash/context7 README, retrieved 2026-04-30 via Exa]

> **The two-mode integration**:
>
> "ctx7 library: Searches the Context7 index by library name and returns matching libraries with their IDs. ctx7 docs: Retrieves documentation for a library using a Context7-compatible library ID (e.g., /mongodb/docs, /vercel/next.js). MCP Tools: resolve-library-id, query-docs." [Source: https://github.com/upstash/context7 README, retrieved 2026-04-30]

> **The proprietary-backend caveat**:
>
> "While the MCP client adapter is open-source (MIT), the heavy lifting—the backend crawling and parsing engines—remains entirely proprietary and hosted by Upstash." [Source: Gemini DR Wave 4A 2026-04-29 URL 14 evaluation]
