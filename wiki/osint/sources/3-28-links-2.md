---
title: 'Targeted Extraction Audit: Cemini Financial Suite Integration Candidates'
type: source
tags: [docx, deep-read, llm-agents, mcp-tools, agent-infra, cemini-internal, link-evaluation, multi-topic]
keywords: [MCP tools, agent infrastructure, Claude Code plugins, code review, prompt testing, memory systems, SWE benchmarks, terminal multiplexing]
related:
  - concepts/llm-agent-systems.md
  - concepts/market-microstructure.md
  - concepts/mcp-tool-marketplace.md
  - concepts/quant-finance.md
  - sources/4-4-link-re.md
  - sources/4-4-link-re-2.md
  - sources/4-6-links.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-04-30
clusters:
  - llm-agents
  - cemini-internal
  - infrastructure
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research
- @concepts/market-microstructure.md — Market Microstructure corpus-index hub
- @concepts/mcp-tool-marketplace.md — MCP Tool Marketplace concept synthesis
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub; several repos evaluated here overlap with MCP adoption rubric
- @sources/4-4-link-re.md — sibling K12 link-evaluation doc; complementary academic-paper focus
- @sources/4-4-link-re-2.md — sibling K12 doc; 7 Target Domains structure
- @sources/4-6-links.md — sibling K12 doc; nvk/llm-wiki + AI governance paper evaluations

## Raw Concept

- **Original title**: Targeted Extraction Audit: Cemini Financial Suite Integration Candidates
- **Author(s)**: Cemini internal (link-evaluation audit)
- **Type**: DOCX
- **Location**: cemini-librarian:/opt/cemini-bulk/research/3_28 links 2.docx
- **Retrieved**: 2026-04-23
- **Read status**: deep-read

## Narrative

This Cemini-internal audit evaluates 13 GitHub repositories (plus 2 failed extractions) for integration into the Cemini Financial Suite stack. Evaluation follows the standard 8-section per-H2 Cemini template: What it is / Architecture patterns / Algorithms / Code & tooling / What they got wrong / IP sale relevance / Solo-dev filter / Conflicts. All evaluations reference the constraint frame of a 128 GB RAM CPU-only Hetzner VPS (now known to be 7 GB — see @entities/infrastructure/hetzner.md K11 refresh).

### Repositories evaluated

**Agent-development infrastructure (6 repos)**:
- **CodeFire** (MIT) — Claude Code plugin for real-time code review. Architecture: websocket-based streaming analysis with AST parsing. Solo-dev filter: PASS (single binary, low maintenance).
- **StealthBrowser MCP** (MIT) — Headless browser as MCP server. Enables Claude agents to scrape JS-rendered pages. Conflict: Playwright already in stack; this adds a second browser automation path → fragmentation risk.
- **MCPHub** (Apache-2.0) — MCP server registry and discovery service. Centralizes MCP tool catalog with health checks. Relevant post-K11 MCP restructuring (code moved to `/opt/cemini/cemini_mcp/server.py`, ~30 tools).
- **Claude Deep Research Skill** (MIT) — Multi-round research loop with sub-agent fan-out. Architecture: iterative deepening with source tracking. Overlaps with the Exa MCP + Tier-2 arXiv sweep workflow already operational in this workspace.
- **Claude Inspector** (MIT) — Session introspection tool: token counts, tool call traces, context-window utilization. Maps to the telemetry patterns discussed in @sources/4-6-links.md (vibeyard session inspector). Could supplement the cryptographic audit trail with per-session cost attribution.
- **Autoresearch** (MIT) — Autonomous research agent with configurable depth. Overlaps with the `/autoresearch` multi-round loop pattern surfaced in Wave 5 (@sources/agriciDaniel-claude-obsidian.md).

**Testing & quality (2 repos)**:
- **Promptfoo** (MIT) — LLM prompt testing framework. Red-team / eval harness for comparing prompt variants with deterministic scoring. Directly applicable to testing LangGraph agent prompts before deployment. Top Steal candidate for the Cemini dev workflow.
- **Compound Engineering Plugin** (MIT) — Claude Code plugin for engineering workflow automation. Evaluates code changes against a rubric. Overlaps with Promptfoo in the testing domain.

**Memory & state (2 repos)**:
- **Memobase** (Apache-2.0) — Episodic memory layer for AI agents. Stores interaction history with pgvector. Overlaps with the `alash3al/stash` episodic memory pattern surfaced in Wave 5 (Phase 7+ candidate).
- **Agent Alchemy** (MIT) — Agent state management with checkpoint/resume. Maps to the LangGraph PostgresSaver pattern discussed in @sources/3-26-b.md.

**Benchmarks & tooling (3 repos)**:
- **SWE-AF** (Apache-2.0) — Software engineering agent benchmark. Evaluates agents on real-world bug fixes. Useful for calibrating Claude Code agent performance against published baselines.
- **CMUX** (MIT) — Terminal multiplexer for Claude Code sessions. Allows parallel session management. Solo-dev filter: borderline — adds operational complexity for a single-developer setup.
- **Gstack** (MIT) — Git worktree manager for parallel agent sessions. Overlaps with the Git worktree isolation pattern evaluated in @sources/4-6-links.md (its-maestro-baby/maestro).

**Failed extractions (2 repos)**: rendergit, mem9 — text extraction from source repos failed; not evaluated.

### Promotion candidates

**Promptfoo** — Top Steal. Deterministic LLM prompt testing with red-team capabilities. MIT license, zero GPL risk. Fills a gap in the Cemini dev workflow: there is currently no systematic prompt-evaluation harness for the LangGraph agent ensemble. Integration: wrap Promptfoo as a CI step that gates agent prompt changes.

**MCPHub** — relevant post-K11 restructuring. As the FastMCP server consolidates from ~130 to ~30 tools, a registry/discovery layer helps maintain visibility. Apache-2.0 license.

### Snippets-only

The remaining repos are Snippets-only: they overlap with already-ingested patterns (CodeFire ≈ existing code-review workflow; StealthBrowser ≈ Playwright MCP; Autoresearch ≈ Exa MCP workflow; Memobase/Agent Alchemy ≈ Wave 5 episodic-memory roadmaps; CMUX/Gstack ≈ Git worktree patterns in 4_6_links).

### Patterns worth noting

Consistent across evaluations: the Cemini-internal analyst enforces a strict **Python 3.12 + FastAPI monoculture** constraint. Any repo introducing Go, Rust, TypeScript, or Electron is flagged as a conflict — the architectural concept may be stolen but the implementation language must be ported. The **solo-dev filter** consistently rejects multi-service architectures, GUI dashboards, and anything requiring a dedicated ops team. The **IP sale relevance** lens evaluates every pattern through the lens of institutional-acquirer due diligence (deterministic over opaque, auditable over black-box, glass-box observability).

## Snippets

> "Promptfoo: LLM prompt testing framework. Red-team / eval harness for comparing prompt variants with deterministic scoring. Directly applicable to testing LangGraph agent prompts before deployment. Top Steal candidate." [Source: 3_28 links 2.docx §Promptfoo]

> "MCPHub: MCP server registry and discovery service. Centralizes MCP tool catalog with health checks. Relevant post-K11 MCP restructuring." [Source: 3_28 links 2.docx §MCPHub]

> "CodeFire: websocket-based streaming analysis with AST parsing. Solo-dev filter: PASS (single binary, low maintenance)." [Source: 3_28 links 2.docx §CodeFire]

> "The Cemini-internal analyst enforces a strict Python 3.12 + FastAPI monoculture constraint. Any repo introducing Go, Rust, TypeScript, or Electron is flagged as a conflict — the architectural concept may be stolen but the implementation language must be ported." [Source: 3_28 links 2.docx, cross-section pattern]
