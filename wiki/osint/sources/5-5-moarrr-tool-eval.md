---
title: "5_5 moarrr links — Technology Stack Evaluation Report (19 tools)"
type: source
tags: [llm-agents, dev-tooling, hft-backtesting, structured-generation, agent-memory, license-compliance, cemini-internal]
keywords: [tool-evaluation, gemini-deep-research, hftbacktest, guidance-ai, letta-memgpt, simonw-ttok, git-rewind, research-paper-writing-skills, the-rosetta-prompt]
related:
  - sources/5-5-links-tool-eval.md
  - sources/5-5-links-2-tool-eval.md
  - sources/links-3-5-4-tool-eval.md
  - sources/polymarket-5-5-tool-eval.md
  - concepts/cemini-license-posture.md
  - entities/tools/hftbacktest.md
  - entities/tools/daily-stock-analysis.md
  - entities/tools/guidance-ai.md
  - entities/tools/letta-memgpt.md
  - entities/tools/ttok.md
  - entities/tools/git-rewind.md
  - sources/5-6-links-eval-batch.md
  - sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md
maturity: draft
read_status: deep-read
created: 2026-05-05
updated: 2026-05-11
---

## Relations

- @sources/5-5-links-tool-eval.md, @sources/5-5-links-2-tool-eval.md, @sources/links-3-5-4-tool-eval.md, @sources/polymarket-5-5-tool-eval.md — companion 2026-05-04/05 K30 Gemini DR eval batches; this is a follow-on K31 batch in the same family
- @entities/tools/hftbacktest.md — Adopt-tier carry-forward; high-frequency backtesting framework for Cemini production stack
- @entities/tools/guidance-ai.md — Adopt-tier carry-forward; structured-generation library for DeepSeek output enforcement
- @entities/tools/letta-memgpt.md — Steal-from-tier carry-forward; agent-memory framework (formerly MemGPT)
- @entities/tools/ttok.md — Adopt-tier carry-forward; Simon Willison's token-counting CLI utility
- @entities/tools/git-rewind.md — Adopt-tier carry-forward; AI-powered git-state CLI utility
- @concepts/cemini-license-posture.md — license-pattern catalog applied; no new patterns surfaced in this batch

## Raw Concept

- Original title: "Technology Stack and Link Evaluation Report for Target Systems" (Gemini Deep Research output)
- Author: Gemini Deep Research
- Type: docx — Cemini-internal architecture evaluation
- Location: cemini-librarian:/opt/cemini-bulk/research/5_5 moarrr links.docx
- Retrieved: 2026-05-05
- Length: ~73 KB, 19 candidates evaluated using identical 8-section template
- Read status: deep-read

## Narrative

Same 8-section per-URL template as K30 batches. Mix of Cemini-production-stack tooling (hftbacktest, guidance-ai, letta), workflow-side utilities (git-rewind, ttok, Research-Paper-Writing-Skills), and methodology references (The-Rosetta-Prompt).

**Recommendation distribution:**

| Tier | Count | Items |
|------|-------|-------|
| **Adopt** | 5 | URL 3 git-rewind (Rust CLI for git-state natural-language briefing; laptop-side), URL 4 Research-Paper-Writing-Skills (Claude Code skills for academic writing), URL 15 **hftbacktest** (microsecond-level HFT backtesting framework — direct Cemini production-stack relevance), URL 17 **guidance-ai/guidance** (Microsoft structured-generation library for deterministic LLM output), URL 19 **simonw/ttok** (Python token-counting CLI utility) |
| **Steal-from** | 4 | URL 2 The-Rosetta-Prompt (agentic prompt-optimization framework — extract methodology only), URL 10 InsForge (MCP server schemas for Postgres state inspection — extract for FastMCP layer), URL 12 daily_stock_analysis (technical indicator aggregation patterns — Cemini-prod relevant), URL 18 **letta-ai/letta** (formerly MemGPT — extract architectural schemas, do NOT mount full Docker infra) |
| **Defer** | 1 | License or maturity gating |
| **Reject** | 3 | License or stack mismatch |
| **Reference-only** | 3 | Documentation / educational |
| **Unavailable** | 3 | URL retrieval failed |

### Critical findings

#### 1. hftbacktest — direct Cemini production-stack Adopt

> "Highly specialized framework engineered for ultra-precise, high-frequency trading and market-making backtesting... ingests microsecond-level tick data—specifically Level-2 Market-By-Price and Level-3 Ma[rket-by-Order]." [Source: 5_5 moarrr links.docx URL 15]

This is a **load-bearing addition** to Cemini's prediction-market backtest pipeline (per `@concepts/prediction-market-historical-analysis.md`). Standard daily-bar backtesting tools (yfinance EOD per polygon-doctrine; FinanceToolkit's GARCH on daily series) don't capture the microstructure that prediction-market market-making + cross-venue arbitrage actually depend on. hftbacktest fills that gap.

The eval explicitly recommends: "implement[ing] the utility's event-order correction algorithm" to "enable latency-adjusted backtesting that accurately simulates hyper-liquid environments."

Direct integration target. Stage as a brief candidate alongside the K30 quant-libs FastMCP integration brief (`@briefs/2026-05-04_quant-libs-fastmcp-integration.md`) — they're both production-side adoption work in the same code area.

#### 2. guidance-ai/guidance — structured-output enforcement for DeepSeek

> "Advanced structural control paradigm designed specifically to intercept and manipulate the token-generation logic of Large Language Models... Instead of relying on stochastic natural-language prompts to hopelessly enforce output formats, Guidance algorithmically binds the generation p[rocess]." [Source: 5_5 moarrr links.docx URL 17]

This addresses a real pain point: Cemini's LangGraph orchestrator + FastMCP tool-use require deterministic JSON outputs from DeepSeek. The K28 quant-libs integration brief (`@briefs/2026-05-04_quant-libs-fastmcp-integration.md`) and K30 Polymarket Stack brief (`@briefs/2026-05-05_polymarket-stack-adoption.md`) both lean on tool-call schemas; guidance-ai would force structural compliance at token generation time.

Eval recommends: "Apply the @guidance decorator around the core DeepSeek execution wrappers to enforce deterministic JSON outputs, structurally eliminating parsing errors within the LangGraph orchestrat[or]."

Production-stack Adopt. Worth a focused brief.

#### 3. letta-ai/letta (formerly MemGPT) — Steal-from for architectural patterns only

> "Letta, previously known as the MemGPT framework, is an infrastructure platform engineered to endow autonomous artificial intelligence agents with perpetual, stateful memory... bypassing standard context-window limitations." [Source: 5_5 moarrr links.docx URL 18]

Cemini already has `alash3al/stash` deployed as the episodic-memory layer (per `@sources/alash3al-stash.md`, Wave 5 Adopt 2026-05-02). Letta is a competing framework. Eval explicitly says: **don't mount Letta's full Docker infrastructure on the Hetzner CPX21** (memory constraints). Instead, lift architectural schemas — specifically the memory-block partition + paginate patterns.

The decision: stash stays as Cemini's deployed episodic-memory layer; letta-ai is reference-only for architectural schemas. Add to the librarian-tooling alternatives list in `@concepts/wiki-tooling-evaluation.md` IF stash ever needs replacement (no current trigger).

#### 4. simonw/ttok — universal install for token discipline

> "Ultra-lightweight, dedicated Python utility engineered exclusively to audit, count, and truncate text payloads against specific LLM token limits." [Source: 5_5 moarrr links.docx URL 19]

Simon Willison's token-counting CLI. Tiny, single-purpose, hard to argue against. Universal install: laptop + cemini-prod backend.

Use cases:
- Pre-call token-budget audits in Cemini's DeepSeek wrappers
- Brief-staging token estimation (how many tokens does this brief consume when fed to a downstream agent?)
- Conductor's audit-trail Phase 1 (`@briefs/2026-05-05_conductor-audit-trail-phase1.md`) cost calculations

#### 5. git-rewind — laptop-side workflow utility

> "Artificial Intelligence-powered command-line interface developed in Rust that evaluates the current state of a Git repository and provides a natural-language briefing to the developer." [Source: 5_5 moarrr links.docx URL 3]

Local Ollama compatible — synergizes with the existing Karpathy LLM Wiki workflow without exposing proprietary code. Laptop-side install, low operational risk.

### Architectural patterns worth extracting (Steal-from-tier)

- **The-Rosetta-Prompt's ReAct-loop methodology** (URL 2) — provider-doc-reading pattern for prompt optimization. Could inform a future Cemini "read DeepSeek pricing/parameters page" automation when API model IDs change.
- **InsForge's MCP server schemas for Postgres state inspection** (URL 10) — relevant to Cemini's existing 130-tool FastMCP layer. Specific pattern: state-inspection MCP tools for Postgres — could harden Cemini's stash + kb-server observability.
- **daily_stock_analysis technical indicator aggregation** (URL 12) — Python functions for technical-indicator aggregation + DeepSeek-context formatting. Could supplement K28 FinanceToolkit's 150-metric library if specific TA indicators aren't covered.
- **letta-ai memory-block partition/paginate schemas** (URL 18) — architectural reference for stash's memory layout if/when stash hits scale limits.

### License-posture observations

No new license patterns surfaced. License field was sparse in the docx eval excerpts — entity stubs note `[NEEDS VERIFICATION 2026-05-05]` for license verification on each Adopt before any production deployment.

## Snippets

- **hftbacktest scope** (URL 15): "Highly specialized framework engineered for ultra-precise, high-frequency trading and market-making backtesting... ingests microsecond-level tick data—specifically Level-2 Market-By-Price and Level-3 Ma[rket-by-Order]." [Source: 5_5 moarrr links.docx URL 15]

- **guidance-ai philosophy** (URL 17): "Instead of relying on stochastic natural-language prompts to hopelessly enforce output formats, Guidance algorithmically binds the generation p[rocess]." [Source: 5_5 moarrr links.docx URL 17]

- **letta-ai (MemGPT) framing** (URL 18): "infrastructure platform engineered to endow autonomous artificial intelligence agents with perpetual, stateful memory... bypassing standard context-window limitations." [Source: 5_5 moarrr links.docx URL 18]

- **ttok simplicity** (URL 19): "Ultra-lightweight, dedicated Python utility engineered exclusively to audit, count, and truncate text payloads against specific LLM token limits." [Source: 5_5 moarrr links.docx URL 19]

- **git-rewind synergy framing** (URL 3): "Because the architecture supports local Ollama instances, it synergizes perfectly with the existing Karpathy LLM Wiki-pattern workflow without exposing proprietary research or codeba[se]." [Source: 5_5 moarrr links.docx URL 3]

## Dead Ends

*(none yet — first ingest of this source.)*
