---
title: hermes-lcm — Lossless Context Management (DAG-based hierarchical summarization engine)
type: entity
tags: [entity, tool, context-management, memory-engine, llm-agents, cemini-steal-from]
keywords: [hermes-lcm, lossless-context-management, dag-summarization, hierarchical-compression, context-window, sqlite, lcm-grep, lcm-expand, MIT]
related:
  - sources/wave-5-1-link-eval-stacks.md
  - concepts/context-compression-resume-pattern.md
  - entities/frameworks/langgraph.md
maturity: draft
created: 2026-05-01
updated: 2026-05-01
---

## Relations

- @sources/wave-5-1-link-eval-stacks.md — Wave 5.1 Steal-from recommendation; primary evaluation source
- @concepts/context-compression-resume-pattern.md — hermes-lcm's DAG-based hierarchical summarization extends the cpr pattern (Compress/Preserve/Resume) with a specific implementation architecture; the concept page describes the abstract pattern; this entity page describes the concrete engine
- @entities/frameworks/langgraph.md — LangGraph is the target surface for Steal-from extraction; the lcm_grep/lcm_expand tool schemas would be reimplemented as native Python functions within LangGraph nodes

## Raw Concept

Surfaced as a Steal-from recommendation in Wave 5.1 link evaluation (@sources/wave-5-1-link-eval-stacks.md). hermes-lcm (Lossless Context Management) is a context-engine plugin for the Hermes Agent ecosystem that uses a hierarchical DAG + immutable SQLite store to achieve "bounded context, unbounded memory" for long-running LLM agents. MIT license.

## Narrative

### What it is

Hermes-lcm departs from standard flat-summarization approaches (where older messages are simply compressed into a single summary paragraph and the original text is discarded). Instead, it:

1. **Stores all messages immutably** in a SQLite database with unique identifiers
2. **Builds a hierarchical DAG** where messages are recursively compressed into escalating tiers:
   - **L1** (detailed): near-verbatim retention, preserving nuance
   - **L2** (bullets): key points extracted, moderate compression
   - **L3** (truncate): aggressive summarization, minimum viable context
3. **Maintains lossless pointers** from each summary node back to the original raw text
4. **Exposes retrieval tools**: `lcm_grep` (search compressed history) and `lcm_expand` (drill back into original text from any summary node)

The "lossless" guarantee: no information is ever permanently discarded. Summaries can always be expanded back to source. The DAG structure ensures the agent can navigate from high-level summaries down to verbatim quotes with O(log n) lookup.

### Steal-from extraction for Cemini

The Wave 5.1 evaluation identifies three extractable components:

1. **3-Level Escalation protocol**: The L1→L2→L3 compression ladder with deterministic thresholds (τsoft, τhard) that trigger each escalation tier. Extract the algorithm and reimplement directly in `agents/orchestrator.py` to manage LangGraph's context window during long-running trading sessions.

2. **lcm_grep / lcm_expand tool schemas**: The retrieval API design — how the agent queries compressed history and navigates the DAG. Reimplement as native Python functions using PostgreSQL (Cemini's existing persistence layer) instead of SQLite.

3. **Immutable-store DAG data model**: The schema mapping message IDs → summary nodes → parent pointers. Translates cleanly to PostgreSQL/pgvector — SQLite is the Hermes plugin's local constraint, not an architectural requirement.

### Risks of extraction

**Background LLM costs**: The system uses a secondary LLM process to continuously generate hierarchical summaries. Replicating this within Cemini will increase background DeepSeek API calls, adding operational costs and potential rate-limiting during high-volatility trading periods. The τsoft and τhard thresholds must be tuned to balance context fidelity against API expenditure.

**Hermes coupling**: The plugin wrapper is tightly bound to the Hermes Agent runtime. Extraction requires decoupling the core algorithm from the plugin architecture — the evaluation explicitly recommends against deploying the plugin "as-is."

### License

MIT — fully clean for extraction and adaptation. No copyleft, no commercial-use restrictions.

## Snippets

### Wave 5.1 Steal-from rationale
"Hermes-lcm (Lossless Context Management) is a highly sophisticated memory engine plugin engineered specifically to prevent context window degradation and hallucination in long-running LLM agents. It departs from standard flat-summarization techniques by utilizing an immutable SQLite store combined with a hierarchical Directed Acyclic Graph (DAG). This architecture recursively compresses older messages into escalating tiers of summaries (L1 detailed, L2 bullets, L3 truncate) while maintaining lossless pointers back to the original raw text. The mathematical approach to achieving 'bounded context, unbounded memory' utilizing a summary DAG is exceptional." [Source: wave-5-1-link-eval-stacks.md]

### Operational caveat
"A critical operational caveat is the reliance on auxiliary LLM token costs. The system utilizes a background LLM process to continuously generate the hierarchical summaries within the DAG. Replicating this architecture within Cemini will significantly increase the volume of background API calls to DeepSeek, dramatically impacting daily operational costs and potentially introducing rate-limiting bottlenecks during high-volatility trading periods." [Source: wave-5-1-link-eval-stacks.md]

### Open question
"What are the exact soft (τsoft) and hard (τhard) token thresholds utilized in the deterministic control loop to trigger summarization, and how were they mathematically optimized?" [Source: wave-5-1-link-eval-stacks.md]
