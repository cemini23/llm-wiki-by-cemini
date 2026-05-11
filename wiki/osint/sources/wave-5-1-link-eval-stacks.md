---
title: "Evaluating Project Links for Stacks 5_1.docx — Wave 5.1 link evaluation (25 URLs, systems-architecture brief)"
type: source
tags: [cemini-internal, competitive-intelligence, link-evaluation, wave-5-1, k-series, may-2026]
keywords: [deepseek-v4-pro, fireworks-ai, refero-styles, three-man-team, hermes-ecosystem, hyper-extract, langalpha, paperclip, timesfm, finceptterminal, st3gg, mirofish, agent-orchestrator]
clusters: [llm-agents]
related:
  - sources/wave-5-1-link-eval-more.md
  - sources/wave-5-1-link-eval-even-more.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/mcp-tool-marketplace.md
  - concepts/ip-sale-readiness.md
  - concepts/context-compression-resume-pattern.md
  - concepts/cryptographic-audit-trail.md
  - entities/frameworks/langgraph.md
  - entities/infrastructure/deepseek-api.md
  - entities/models/timesfm.md
  - entities/tools/hermes-lcm.md
  - concepts/mcp-context-optimization.md
maturity: draft
read_status: read
created: 2026-05-01
updated: 2026-05-11
---

## Relations

- @sources/wave-5-1-link-eval-more.md — sibling Wave 5.1 doc (12 URLs, agent-framework focused)
- @sources/wave-5-1-link-eval-even-more.md — sibling Wave 5.1 doc (27 URLs, infra + data-engineering focused)
- @concepts/wiki-tooling-evaluation.md — same three-surface evaluation methodology
- @concepts/mcp-tool-marketplace.md — MCP-server evaluation patterns reflected in Refero Styles and Hermes evaluations
- @concepts/ip-sale-readiness.md — AGPL-3.0 poison-pill license assessments (FinceptTerminal, ST3GG, MiroFish)
- @concepts/context-compression-resume-pattern.md — hermes-lcm's DAG-based hierarchical summarization is a Steal-from pattern extending the cpr concept
- @concepts/cryptographic-audit-trail.md — hermes-a2a's HMAC security architecture as Steal-from hardening pattern
- @entities/frameworks/langgraph.md — LangGraph used as benchmark for agent-framework evaluations throughout
- @entities/infrastructure/deepseek-api.md — DeepSeek-V4-Pro Fireworks endpoint as primary Adopt candidate
- @entities/models/timesfm.md — Google Research 200M-param time-series foundation model; Wave 5.1 Adopt for CPU-viable zero-shot forecasting
- @entities/tools/hermes-lcm.md — DAG-based hierarchical context summarization engine; Wave 5.1 Steal-from for L1/L2/L3 escalation architecture

## Raw Concept

- Original title: Evaluating Project Links for Stacks 5_1.docx (Word document, title "Systems Architecture and Integration Intelligence Brief")
- Author(s): Cemini-internal (Claude-agent-authored link evaluation)
- Type: Word document (.docx)
- Location: cemini-librarian:/opt/cemini-bulk/research/Evaluating Project Links for Stacks 5_1.docx
- Retrieved: 2026-05-01
- Evaluation date: 2026-05-01
- Pages / length: 532 paragraphs, ~71K chars
- Read status: read
- SHA256: 696ed462eaa756f7...

## Narrative

Wave 5.1 link-evaluation brief evaluating 25 software projects, vendor products, and repositories against the standard three-surface framework: Cemini production trading stack (Python/LangGraph/FastAPI on Hetzner 7 GB CPU), Wiki/librarian server (Node.js/Ollama on CPX21 4 GB), and solo-developer Workflow (macOS laptop, Claude Code, Obsidian). Each URL receives an 8-section evaluation: Identity, What It Is, Scoring Table, Detailed Evaluation per Category, Recommendation Tier, Risks & Caveats, Open Questions, and Primary Sources Cited.

The document covers a broad spectrum: LLM API endpoints (DeepSeek-V4-Pro via Fireworks), design-tool MCP servers (Refero Styles), agent-framework ecosystems (Hermes suite — 6 plugins), financial applications (FinceptTerminal, LangAlpha), ML infrastructure (MapAnything, TimesFM), extraction pipelines (Hyper-Extract), orchestration dashboards (Paperclip, Agent Orchestrator), security toolkits (ST3GG), and swarm simulators (MiroFish). Five URLs were UNAVAILABLE due to primary-source fetch failure (oh-my-claudecode, headroom, dair-workshops, LibreChat, clawless).

### Recommendation distribution

**Adopt (3):** DeepSeek-V4-Pro Fireworks endpoint (seamless OpenAI-compatible API swap, $1.74/1M input, $3.48/1M output, 1M token context), Hyper-Extract (YAML-template-driven extraction into Polars, Apache-2.0), TimesFM (200M-param time-series foundation model, ~400-800MB RAM, CPU-viable, Apache-2.0).

**Steal-from (6):** Refero Styles (DESIGN.md schema for AI-consumable design tokens), Three-Man-Team (Architect/Builder/Reviewer role definitions + token-optimization rules for CLAUDE.md), hermes-web-search-plus (multi-provider query-scoring matrices + adaptive fallback), hermes-lcm (DAG-based 3-level hierarchical summarization — "bounded context, unbounded memory"), hermes-a2a (HMAC-SHA256 constant-time comparison + outbound redaction filters), LangAlpha (PostgreSQL LangGraph checkpointing, Redis SSE event buffer, Programmatic Tool Calling schemas).

**Defer (0).**

**Reference-only (5):** Agentic-Design-Patterns (educational, dual-license code/textbook), hermes-skill-factory (Hermes-bound workflow observer), hermes-agent (Nous Research core framework — architectural paradigm conflict with LangGraph), Paperclip (orchestration dashboard — massive Node.js/React overhead for solo dev), Agent Orchestrator (Git-worktree multi-agent manager — overkill for single Claude Code collaborator).

**Reject (6):** FinceptTerminal (AGPL-3.0 + $50K/yr documented commercial penalty), MapAnything (140 GB VRAM requirement, domain mismatch), ST3GG (AGPL-3.0 poison pill, zero utility for financial stack), MiroFish (AGPL-3.0 via OASIS dependency, thousands of agents on 7 GB impossible), icarus-plugin (data egress to Together AI, no GPU), lark-cli (requires Lark/Feishu ecosystem).

### Cross-document signals

The Hermes ecosystem evaluation (URLs 11–16) is structurally significant: six tightly coupled plugins all under MIT license, all architecturally bound to the Hermes Agent runtime, each evaluated individually. Three emerge as Steal-from candidates (web-search-plus, lcm, a2a), one as Reference-only (skill-factory), one as Reject (icarus — data egress), and the core agent as Reference-only (paradigm conflict with LangGraph). This is the first Wave evaluation to treat an ecosystem as a unified cluster rather than isolated projects.

The AGPL-3.0 pattern is stark: three projects (FinceptTerminal, ST3GG, MiroFish) are hard-rejected on license alone, independent of technical merit. FinceptTerminal's explicitly documented $50,000/yr/organization commercial penalty represents the most severe license exposure encountered across all Wave evaluations to date.

## Snippets

### DeepSeek-V4-Pro Fireworks — Adopt rationale
"Integration vector is seamless and immediate. The endpoint can be slotted directly into agents/orchestrator.py or services/llm_analyst/deepseek_client.py by simply swapping the base URL to https://api.fireworks.ai/inference/v1 and updating the server's .env file with a valid Fireworks API key. Because the 14B+ parameter model executes entirely on Fireworks AI's distributed clusters, it imposes zero local compute or RAM footprint, perfectly respecting the Hetzner server's strict 7 GB CPU-only limitation." [Source: Evaluating Project Links for Stacks 5_1.docx]

### TimesFM — Adopt rationale
"A 200 million parameter model quantized to standard fp32 or fp16 occupies roughly 400 MB to 800 MB of resident RAM. This exceptionally small footprint comfortably fits within the strict 7 GB server limitation, executing alongside the existing Postgres, Redis, and FastAPI stack without triggering Out-Of-Memory kills. Clean Apache-2.0 license." [Source: Evaluating Project Links for Stacks 5_1.docx]

### hermes-lcm — Steal-from rationale
"Hermes-lcm (Lossless Context Management) is a highly sophisticated memory engine plugin engineered specifically to prevent context window degradation and hallucination in long-running LLM agents. It departs from standard flat-summarization techniques by utilizing an immutable SQLite store combined with a hierarchical Directed Acyclic Graph (DAG). This architecture recursively compresses older messages into escalating tiers of summaries (L1 detailed, L2 bullets, L3 truncate) while maintaining lossless pointers back to the original raw text." [Source: Evaluating Project Links for Stacks 5_1.docx]

### LangAlpha — Steal-from rationale
"LangAlpha represents a masterclass in relevant architectural design. Cemini currently utilizes a basic linear 4-node StateGraph. LangAlpha's sophisticated implementation of LangGraph checkpointers — which utilize a dedicated, isolated PostgreSQL connection pool — along with its Redis Server-Sent Events (SSE) event buffer for seamlessly reconnecting to long-running tasks, must be extracted and applied directly to Cemini's orchestrator.py." [Source: Evaluating Project Links for Stacks 5_1.docx]

### FinceptTerminal — AGPL-3.0 poison pill
"The authors have documented a specific penalty of '$50,000 per organization per year' for unlicensed commercial use. In the context of preparing a codebase for institutional acquisition, merely having a component of this repository present in the commit history could derail due diligence processes and trigger massive liability vectors." [Source: Evaluating Project Links for Stacks 5_1.docx]
