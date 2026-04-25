---
title: Scatter-gather topology (LangGraph)
type: concept
tags: [concept, llm-orchestration, methodology]
keywords: []
related:
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - entities/frameworks/langgraph.md
  - entities/infrastructure/deepseek-r1-14b.md
  - entities/infrastructure/deepseek-api.md
  - entities/infrastructure/redis.md
maturity: retracted
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @entities/frameworks/langgraph.md
- @entities/infrastructure/deepseek-r1-14b.md `[RETRACTED 2026-04-24]` — page retracted; backlink kept for discoverability
- @entities/infrastructure/deepseek-api.md — operative LLM brain via cloud API; replaces the retracted local-runtime path
- @entities/infrastructure/redis.md

## Raw Concept

Synthesized across 1 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[RETRACTED — 2026-04-24 Track C audit]** The topology described here is **not** what's built on main. `agents/orchestrator.py:1004` is a **linear multi-node `StateGraph`** with 4 analyst nodes (`technical`, `fundamental`, `sentiment`, `cio_debate`) + `publish_to_bus`, wired via `add_conditional_edges`. `from langgraph.graph import StateGraph, END` — **no `Send()` import**, no `types.Send`. `operator.add` / `add_messages` reducers: 0 hits in main-tree LangGraph code. The LLM Analyst (`services/llm_analyst/deepseek_client.py`) is a **single shared client**, not per-subagent contexts.

**Correction 2026-04-24 (post-inventory)**: Track C's walk speculated that `.worktrees/step83-llm-analyst/` carried a Send()-based *prototype*. A follow-up inventory probe by server-Claude refutes this: step83 is **docs-only** — two commits (Step 83 implementation plan + design spec), orchestrator.py in step83 is identical to main (same `StateGraph, END` imports, no `Send()`), and the cemini_mcp requirements/Dockerfile are unmodified. The Send() topology + richer audit trail are **planned in step83's design spec**, not built. So the P1 ticket option space is:
- **Option A** — build Send() topology fresh per step83's design spec (significantly larger than a merge — **~1–2 engineer-weeks** depending on spec scope; was estimated 2–5 days when I thought step83 was a merge-ready prototype).
- **Option B** — retract + rename: rename this page to describe the actual linear StateGraph topology in `agents/orchestrator.py:1004`; keep step83 as the design reference for a future build. **~0.5 engineer-days**.

Default recommendation: **Option B** unless the Send() topology is specifically on the IP-sale critical path; the acquirer narrative reads the 4-analyst linear workflow as a legitimate LangGraph pattern, and renaming closes the wiki-vs-code drift cheaply. Gap memo: `briefs/track-c-walk-results.md` + `briefs/2026-04-24_track-c-ticket-memo.md` (P1-4, to be revised per this correction).

Original claimed narrative retained below as retracted-claim-of-record.

---

Scatter-gather is Cemini's canonical LLM-agent topology for financial
analysis tasks, implemented via LangGraph's Send API + Pregel BSP model.

### The pattern
1. **Supervisor node** receives the task (e.g., "analyze the last 24h
   of GDELT + price + order-flow for ticker X and return a
   Pydantic-v2 StrategyRecommendation").
2. **Fan-out via Send** — the supervisor dispatches N subagent nodes,
   one per data slice (news, fundamentals, microstructure,
   alt-data, cross-asset context). Each subagent gets its own
   LLM reasoning context, typed state, and tool-budget. `[RETRACTED 2026-04-24]`
   Earlier phrasing named "DeepSeek-R1 reasoning context" specifically;
   DeepSeek/Ollama are not deployed (see @entities/infrastructure/deepseek-r1-14b.md),
   so whichever LLM provider actually backs the supervisor today stays
   unclaimed until verified.
3. **Shared state with operator.add reducers** — each subagent
   writes its Pydantic-typed partial result into a shared state dict
   whose keys are merged, not overwritten, via `typing.Annotated[…,
   operator.add]`.
4. **Gather node** reads the merged state, resolves any cross-slice
   contradictions, and emits a single final Pydantic output.

### Why it works on CPU-only
No single reasoning pass has to hold the entire payload in context —
each subagent sees a curated slice. Slices run in parallel at the
subprocess level and the token budget per subagent is tight, so
even a slow CPU-bound backend stays tolerable. `[RETRACTED 2026-04-24]`
Previous phrasing here quoted "DeepSeek-R1-14B's ~8–12 tok/s on CPU"
as the concrete envelope; since DeepSeek/Ollama are not deployed, the
numeric envelope cannot be cited. The topology-level argument still
holds for any CPU-bound LLM.

### Audit properties
Every Send edge + every reducer application is checkpointed to
PostgreSQL. The pg_tamperlog receipts for those checkpoints feed the
cryptographic audit trail, so the full reasoning graph is deterministically
replayable for IP-sale due diligence.

## Snippets

*(populate as source stubs are deep-read.)*
