---
title: Scatter-gather topology (LangGraph)
type: concept
tags: [concept, llm-orchestration, methodology]
keywords: []
related:
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - sources/sakana-conductor-rl-orchestration.md
  - sources/sakana-trinity-llm-coordinator.md
  - entities/frameworks/langgraph.md
  - entities/infrastructure/deepseek-r1-14b.md
  - entities/infrastructure/deepseek-api.md
  - entities/infrastructure/sakana-fugu.md
  - entities/infrastructure/redis.md
  - entities/data-sources/telethon.md
  - sources/4-5-links.md
  - entities/frameworks/autoagent.md
  - concepts/context-compression-resume-pattern.md
  - entities/infrastructure/localai.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/librarian-server-architecture.md
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/omc-talent-container-paper.md
  - concepts/ai-organisation-design.md
  - sources/vibe-trading-hkuds.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - sources/4-5-links-2.md
maturity: validated
created: 2026-04-23
updated: 2026-04-28
---

## Relations

- @sources/3-19-langgraph-scatter-gather-financial-analysis.md
- @sources/sakana-conductor-rl-orchestration.md — user-dropped 2026-04-27 — ICLR 2026 Sakana AI Conductor paper; **direct architectural counterpart**: where this concept's source prescribes a *hand-designed* `Send()`-based fan-out + `operator.add` reducer + gather pattern, the Conductor *learns* topology design as a per-task RL-trained meta-controller decision. Strong evidence for the open Option A vs Option B P1 ticket — a learned orchestrator outperforms hand-designed scaffolds (incl. MoA, MasRouter, RouterDC, Smoothie baselines)
- @sources/sakana-trinity-llm-coordinator.md — sibling ICLR 2026 Sakana AI paper (ingested 2026-04-28). Methodologically distinct from Conductor: Trinity uses a 0.6B SLM + ~10K-param head (<20K total learnable params) trained with **sep-CMA-ES** (evolutionary, not RL) to assign **Thinker/Worker/Verifier roles** across multiple turns. **Strengthens Option C** (outsource orchestration to Fugu) by establishing two distinct tiers in the Fugu lineup: Trinity → likely Fugu Mini 🐟 (lightweight low-latency); Conductor → likely Fugu Ultra 🐡 (heavyweight full-orchestration). Trinity's structured-role schema is also **closer to a typed-state-graph contract** than Conductor's free-form natural-language prompts — easier mapping onto LangGraph's typed Pydantic-output substrate, which matters for any in-house Cemini-side reproduction (Option A variant) that wants to retain the Pydantic `StrategyRecommendation` handoff
- @entities/infrastructure/sakana-fugu.md — **adds Option C to this page's P1 ticket** (2026-04-27): outsource orchestration to Sakana's productized Conductor + Trinity API (closed beta, launched 2026-04-24). Engineering effort ~1–3 engineer-days (config swap + Pydantic glue + audit-trail integration) — lowest-effort path to "learned-orchestrator quality" without training one in-house. Trade-offs: data-egress posture (Fugu sees all prompts), opaque per-worker routing (audit trail captures only top-level prompt/completion tuple), acquirer optics (defensible only with vertical-domain fine-tuning + custom worker-pool composition + typed-output Pydantic glue named explicitly as the moat)
- @entities/frameworks/langgraph.md
- @entities/infrastructure/deepseek-r1-14b.md `[RETRACTED 2026-04-24]` — page retracted; backlink kept for discoverability
- @entities/infrastructure/deepseek-api.md — operative LLM brain via cloud API; replaces the retracted local-runtime path
- @entities/infrastructure/redis.md
- @entities/data-sources/telethon.md — sibling K3 reframe (2026-04-26); same Cemini-internal-blueprint pattern, same prescribed-vs-deployed collapse caught and reset
- @sources/4-5-links.md — K8 deep-read 2026-04-28 — multi-topic Cemini-internal evaluation. K8 server-probe finding strengthens this page's Option B default: **the prescribed scatter-gather is still not deployed** (linear 4-node `StateGraph` ships per Track C 2026-04-24). The K8 doc's "scatter-gather as canonical topology" framing is reading the *blueprint* as as-built — same J-pattern collapse caught here on 2026-04-26
- @entities/frameworks/autoagent.md — K8 promotion 2026-04-28 — sibling LangGraph-orchestration pattern. AutoAgent optimizes *harness configuration* (prompts, tools, routing); scatter-gather optimizes *runtime topology*. Different axes of the same orchestration problem; both would land naturally during any P1-ticket resolution work
- @concepts/context-compression-resume-pattern.md — K8 promotion 2026-04-28 — the prescribed serialization/recovery layer for any LangGraph topology (linear or scatter-gather). When/if Option A (build Send() fan-out fresh) lands, the cpr-pattern's checkpoint+restore is the natural state-management partner; resume from a crashed scatter-gather becomes feasible without re-running upstream nodes
- @entities/infrastructure/localai.md — K8 promotion 2026-04-28 — local-inference runtime that any scatter-gather node would call (in the retracted-but-architecturally-coherent local-runtime path). LocalAI's OpenAI-compatible shim means the deployed `services/llm_analyst/deepseek_client.py` works against it with a one-line `base_url` change — the topology is unaffected
- @concepts/wiki-tooling-evaluation.md — 2026-04-28 synthesis: any wiki/memory tooling adopted by the workspace librarian (recommended: `llm-wiki-compiler`) would expose its retrieval surface via MCP, which the analyst-node DeepSeek client would query when building scatter-gather context. Adoption decision is upstream of the Send-API topology decision; doesn't block, but the wiki-tooling MCP shape would inform the analyst-prompt construction

## Raw Concept

Synthesized across 1 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[RESOLVED — 2026-04-26 primary-source deep-read]** Earlier framing on this page collapsed *prescription* into *as-built*: it described "Cemini's canonical LLM-agent topology" in present tense as if `agents/orchestrator.py` already shipped a Send()-based scatter-gather. The 2026-04-24 Track C audit retracted that ("not what's built on main — linear multi-node `StateGraph` with 4 analyst nodes, no `Send()` import"). The 2026-04-26 deep-read of `@sources/3-19-langgraph-scatter-gather-financial-analysis.md` confirms the source itself is a **prescriptive architectural blueprint**, not a description of deployed code: it uses imperative voice throughout ("the architecture *must* elegantly decouple…", "the platform *must* completely decouple…", "Timeouts *must* be explicitly handled…") and proposes Send/Pregel-BSP as the path to IP-sale-grade modularity for a future acquirer's GPU cluster. So both the source and the wiki were locally consistent — the wiki's prior error was reading prescriptive language as descriptive, the same J-pattern collapse caught on `@concepts/cryptographic-audit-trail.md`. **Note also**: para 85 of the source name-drops *pymerkle* and *OpenTimestamps* as "the implemented…stack" — the source itself committed the same prescription-as-as-built error from its end (those libraries are not installed in `cemini_mcp`; what's deployed is the custom SHA-256 chain). Documenting that here so future readers see the pattern at the source layer too.

**As-built ground truth (verified 2026-04-24, holds 2026-04-26)**: `agents/orchestrator.py:1004` is a **linear multi-node `StateGraph`** with 4 analyst nodes (`technical`, `fundamental`, `sentiment`, `cio_debate`) + `publish_to_bus`, wired via `add_conditional_edges`. `from langgraph.graph import StateGraph, END` — **no `Send()` import**, no `types.Send`. `operator.add` / `add_messages` reducers: 0 hits in main-tree LangGraph code. The LLM Analyst (`services/llm_analyst/deepseek_client.py`) is a **single shared client** against the hosted DeepSeek API, not per-subagent Ollama contexts. The `.worktrees/step83-llm-analyst/` branch is **docs-only** (two commits: implementation plan + design spec); orchestrator.py in step83 is byte-identical to main and the cemini_mcp requirements/Dockerfile are unmodified.

**Open P1 ticket — option space (carried from 2026-04-24 Track C, unchanged by deep-read)**:
- **Option A** — build Send() topology fresh per step83's design spec (significantly larger than a merge — **~1–2 engineer-weeks** depending on spec scope; was estimated 2–5 days when Track C briefly thought step83 was a merge-ready prototype).
- **Option B** — keep the deployed linear StateGraph as the documented topology; treat the Send/Pregel blueprint as forward-looking IP-sale prep that a buyer's GPU-cluster engineer can pick up from this page + step83's design spec. **~0.5 engineer-days** (relabel work only).

Default recommendation: **Option B** unless Send() is specifically on the IP-sale critical path. The acquirer narrative reads the 4-analyst linear workflow as a legitimate LangGraph pattern, and the prescriptive blueprint above is more valuable to a buyer with H100s than a CPU-bound prototype would be. Gap memo: `briefs/track-c-walk-results.md` + `briefs/2026-04-24_track-c-ticket-memo.md` (P1-4).

Original prescriptive narrative retained below as the canonical *blueprint-form* description of the topology — useful as the IP-sale buyer's-eye reference, but **not** describing current deployment.

---

Scatter-gather is Cemini's canonical LLM-agent topology for financial
analysis tasks, implemented via LangGraph's Send API + Pregel BSP model.

### The pattern (as prescribed by `@sources/3-19-langgraph-scatter-gather-financial-analysis.md`, **not as deployed**)
1. **Supervisor node** receives the task (e.g., "analyze the last 24h
   of GDELT + price + order-flow for ticker X and return a
   Pydantic-v2 StrategyRecommendation").
2. **Fan-out via Send** — the supervisor dispatches N subagent nodes,
   one per data slice (news, fundamentals, microstructure,
   alt-data, cross-asset context). Each subagent gets its own
   LLM reasoning context, typed state, and tool-budget. *(The source
   prescribes local Ollama + DeepSeek-R1-14B per-subagent contexts;
   neither is deployed — `@entities/infrastructure/deepseek-r1-14b.md`
   is retracted and the as-built path is the hosted DeepSeek API at
   `@entities/infrastructure/deepseek-api.md`. A buyer post-acquisition
   would be expected to swap in their own per-subagent inference; see
   para 84 in source page Snippets.)*
3. **Shared state with operator.add reducers** — each subagent
   writes its Pydantic-typed partial result into a shared state dict
   whose keys are merged, not overwritten, via `typing.Annotated[…,
   operator.add]`. Without the reducer, parallel writes raise
   `InvalidUpdateError` / `INVALID_CONCURRENT_GRAPH_UPDATE`.
4. **Gather node** reads the merged state, resolves any cross-slice
   contradictions, and emits a single final Pydantic output.

### Why it would work on CPU-only (the source's claim)
No single reasoning pass has to hold the entire payload in context —
each subagent sees a curated slice. The critical decoupling
prescription (source paras 27–30, quoted in source page Snippets) is
that LangGraph's graph-level parallelism must **not** translate to
parallel CPU LLM inference: KV-cache thrash drops a 14B-param model
from ~15 tok/s sequential to ~1–2 tok/s per thread under 4-way
parallel CPU inference. The blueprint's resolution: queue inference
sequentially at the Ollama layer, parallelize only at the graph
layer. Moot in current deployment because there is no local Ollama;
the hosted DeepSeek API handles its own concurrency.

### Audit properties (as prescribed)
Every Send edge + every reducer application would be checkpointed to
PostgreSQL. The source proposes pymerkle + OpenTimestamps for the
cryptographic envelope (para 85, see source Snippets — and note the
source's own prescription-as-as-built collapse there). What's
actually deployed in `cemini_mcp` is the custom SHA-256 chain in
`services/audit/chain.py`; see `@concepts/cryptographic-audit-trail.md`
for the parallel resolution on the audit-trail side.

## Snippets

*(Verbatim pulls live on the source page — see `@sources/3-19-langgraph-scatter-gather-financial-analysis.md#snippets` for paras 3, 27–28, 30, 33, 84, 85. Concept-page synthesis above paraphrases those with the prescribed-vs-deployed framing made explicit.)*
