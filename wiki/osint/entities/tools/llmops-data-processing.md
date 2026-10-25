---
title: "LLMops/data-processing (andysingal) — Reference Architecture for LLM ETL"
type: entity
tags: [tool, steal-from, llmops, etl, hamilton-dataflow, llm-as-judge, mit-license]
keywords: [LLMops, data processing, ETL, Hamilton, LLM Guard, LLM-as-judge, feature store, Ray-LLM, ZenML, Trulens]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/reasoning-safety-monitor.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 13)
- `@concepts/reasoning-safety-monitor.md` — LLM-as-judge prompts relevant here

## Raw Concept

Educational reference architecture for LLMOps pipelines (data processing, security, scaling). The `data-processing` module focuses on ETL for generative AI: text cleaning, Hamilton dataflow patterns, LLM-specific preprocessing, feature stores.

- **Repo**: `github.com/andysingal/LLMops`
- **License**: MIT [NEEDS VERIFICATION 2026-05-10]
- **Stack**: Python (Jupyter notebook-driven)
- **Heavy deps**: ZenML, Trulens, Ray-LLM (NOT to be adopted)
- **Position**: educational quarry mapped to a deep-learning course

## Narrative

**Recommendation: Steal-from, do not deploy any orchestration framework.** Treat as educational reference; extract specific Python primitives, port to lightweight functions in Cemini codebase.

### Patterns worth stealing

1. **Python regex data-cleaning patterns** — apply during SEC EDGAR text → structured JSON conversion in Cemini ingest layer.
2. **`LLM-as-judge.md` prompt schemas** — incorporate into Obsidian knowledge base; enhance Claude Code's ability to evaluate contradictory research papers.
3. **LLM Guard sanitization logic** — manually transcribe into Cemini API request sanitation layer to prevent prompt injection before DeepSeek dispatch on critical trades.
4. **Hamilton dataflow architecture** — study as reference for data-pipeline structure; port lightweight equivalents in pure Python (no Hamilton dependency).
5. **Feature Store architectural theory** — reference design; Cemini may implement light-weight version using existing PostgreSQL/pgvector.

### Why not deploy

- ZenML/Trulens/Ray-LLM add massive computational overhead unjustified by Cemini's existing clean LangGraph orchestration
- Code represents "happy path" educational scenarios — lacks production error handling (exponential backoff, rate-limit handling, malformed JSON recovery)

### Risks (if mining code)

- **Hamilton dataflow Python decorator conflict [OPEN QUESTION 2026-05-10]**: heavy decorator usage may intercept FastMCP `@mcp.tool` decoration sequence. Avoid bringing Hamilton itself; reimplement patterns natively.
- **License verification**: confirm MIT before extracting
- **Production-readiness gap**: any extracted code needs explicit error-handling additions

[Source: Evaluating Code for Trading Stacks.docx, URL 13]
