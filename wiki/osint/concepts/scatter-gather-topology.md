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
  - sources/4-3-link-re-2.md
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/omc-talent-container-paper.md
  - concepts/ai-organisation-design.md
  - sources/vibe-trading-hkuds.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - sources/4-5-links-2.md
  - sources/3-26-b.md
  - sources/3-26-link-re-3.md
  - sources/scaling-roadmap-research.md
  - sources/4-3-link-research.md
  - sources/matching-accuracy-different-geometry-es-grpo.md
  - sources/refinerl-self-refinement-rl.md
  - entities/frameworks/dspy.md
  - sources/wave-5-1-link-eval-more.md
  - sources/3-29-research-6.md
  - concepts/agent-identity-protocol.md
  - sources/3-17-agent-research.md
  - sources/3-25-git-research.md
  - sources/git-3-5-pt3.md
  - sources/crypto-7-4-11.md
  - concepts/sae-execution-contract.md
  - sources/ai-2-4-3.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/agent-authorization-stack.md
maturity: validated
created: 2026-04-23
updated: 2026-05-01
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
- @sources/4-3-link-re-2.md — K14 deep-read 2026-05-01; three scatter-gather reinforcements: AutoMOOSE autonomous failure correction loop → Devil's Advocate reviewer node (Doc 4), diversity-aware RL penalty to prevent MAPPO policy collapse (Doc 8, overlaps with K13 RefineRL), LDP progressive payload modes for inter-agent communication (Doc 7). All Snippets-only.
- @entities/frameworks/dspy.md — Stanford prompt-programming framework (Wave 5.1 Adopt); GEPA optimization loops produce mathematically optimized prompt structures that feed into scatter-gather nodes — offline compilation on laptop, static strings shipped to production LangGraph nodes
- @sources/wave-5-1-link-eval-more.md — Wave 5.1 agent-framework evaluation; DSPy + Instructor Adopt decisions directly supply the analyst-node prompt layer above any scatter-gather topology
- @sources/3-29-research-6.md — K15 deep-read 2026-05-01; Distributed Context Windows + Hybrid Smart Routing promoted from Paper 2 (Dobrovolskyi)
- @concepts/agent-identity-protocol.md — K15 promotion 2026-05-01; IBCT authorization gates each agent-to-agent delegation in the topology
- @sources/3-17-agent-research.md — K16 deep-read 2026-05-01; Redis semantic caching extension (hash prompt+model+temperature → bypass LLM inference) + abliterated-model sandbox pattern
- @sources/3-25-git-research.md — K17 deep-read 2026-05-01; Generator-Evaluator Loop extension: adversarial bifurcation with financial-grade subjective quantification metrics (Statistical Significance, Correlation Robustness, Drawdown Probability, Execution Latency Tolerance)
- @sources/git-3-5-pt3.md — K18 deep-read 2026-05-01; fractals recursive decomposition adds tree-based orchestrator variant (planning/execution phases, isolated Git worktrees, depth-first/breadth-first/layer-sequential strategies)
- @sources/crypto-7-4-11.md — K19 deep-read 2026-05-01; SAE execution-layer middleware adds fourth position in the execution topology: terminal enforcement downstream of the orchestrator. SAE governs execution authorization (ALLOW/LIMIT/BLOCK) while the orchestrator governs computation topology — orthogonal, composable with all three variants
- @concepts/sae-execution-contract.md — K19 promotion 2026-05-01; reusable architectural primitive: standardized API contract for execution-layer safety that composes with Send-API / Generator-Evaluator / Fractals orchestrators
- @sources/ai-2-4-3.md — K20 deep-read 2026-05-01; OpenClaw security taxonomy: §6.7 unified inter-layer policy enforcement is the architectural specification for the execution contract that SAE provides at the scatter-gather terminal leaf
- @concepts/openclaw-security-taxonomy.md — K20 promotion 2026-05-01; the two-axis taxonomy's "absent inter-layer enforcement" structural condition is exactly what SAE + scatter-gather terminal-leaf placement addresses: a unified policy boundary at the execution leaf observes the full call path
- @concepts/agent-authorization-stack.md — K19+K22+K23+K24 cross-cluster synthesis; the authorization stack gates every scatter-gather fan-out.

## Raw Concept

Synthesized across 1 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**[RESOLVED — 2026-04-26 primary-source deep-read]** Earlier framing on this page collapsed *prescription* into *as-built*: it described "Cemini's canonical LLM-agent topology" in present tense as if `agents/orchestrator.py` already shipped a Send()-based scatter-gather. The 2026-04-24 Track C audit retracted that ("not what's built on main — linear multi-node `StateGraph` with 4 analyst nodes, no `Send()` import"). The 2026-04-26 deep-read of `@sources/3-19-langgraph-scatter-gather-financial-analysis.md` confirms the source itself is a **prescriptive architectural blueprint**, not a description of deployed code: it uses imperative voice throughout ("the architecture *must* elegantly decouple…", "the platform *must* completely decouple…", "Timeouts *must* be explicitly handled…") and proposes Send/Pregel-BSP as the path to IP-sale-grade modularity for a future acquirer's GPU cluster. So both the source and the wiki were locally consistent — the wiki's prior error was reading prescriptive language as descriptive, the same J-pattern collapse caught on `@concepts/cryptographic-audit-trail.md`. **Note also**: para 85 of the source name-drops *pymerkle* and *OpenTimestamps* as "the implemented…stack" — the source itself committed the same prescription-as-as-built error from its end (those libraries are not installed in `cemini_mcp`; what's deployed is the custom SHA-256 chain). Documenting that here so future readers see the pattern at the source layer too.

**As-built ground truth (verified 2026-04-24, holds 2026-04-26)**: `agents/orchestrator.py:1004` is a **linear multi-node `StateGraph`** with 4 analyst nodes (`technical`, `fundamental`, `sentiment`, `cio_debate`) + `publish_to_bus`, wired via `add_conditional_edges`. `from langgraph.graph import StateGraph, END` — **no `Send()` import**, no `types.Send`. `operator.add` / `add_messages` reducers: 0 hits in main-tree LangGraph code. The LLM Analyst (`services/llm_analyst/deepseek_client.py`) is a **single shared client** against the hosted DeepSeek API, not per-subagent Ollama contexts. The `.worktrees/step83-llm-analyst/` branch is **docs-only** (two commits: implementation plan + design spec); orchestrator.py in step83 is byte-identical to main and the cemini_mcp requirements/Dockerfile are unmodified.

**Open P1 ticket — option space (carried from 2026-04-24 Track C, unchanged by deep-read)**:
- **Option A** — build Send() topology fresh per step83's design spec (significantly larger than a merge — **~1–2 engineer-weeks** depending on spec scope; was estimated 2–5 days when Track C briefly thought step83 was a merge-ready prototype).
- **Option B** — keep the deployed linear StateGraph as the documented topology; treat the Send/Pregel blueprint as forward-looking IP-sale prep that a buyer's GPU-cluster engineer can pick up from this page + step83's design spec. **~0.5 engineer-days** (relabel work only).

Default recommendation: **Option B** unless Send() is specifically on the IP-sale critical path. The acquirer narrative reads the 4-analyst linear workflow as a legitimate LangGraph pattern, and the prescriptive blueprint above is more valuable to a buyer with H100s than a CPU-bound prototype would be. Gap memo: `briefs/track-c-walk-results.md` + `briefs/2026-04-24_track-c-ticket-memo.md` (P1-4).

### Distributed Context Windows & Hybrid Smart Routing (K15 — Paper 2, Dobrovolskyi et al.)

The paper provides empirical evidence that a single agent accumulating all tool responses within a centralized memory structure inevitably suffers from "context window bloat" — model performance degrades and inference costs grow exponentially as the context accumulates raw tool outputs, historical market data, and previous debate turns.

**Distributed Context Windows**: Instead of the LangGraph orchestrator passing a monolithic State object to every agent, each of the five Devil's Advocate agents maintains a strictly isolated local context window. Agents communicate via minimal JSON summaries transmitted over Redis Streams, mirroring A2A JSON-RPC efficiency. The global LangGraph state contains only lightweight pointers (Redis stream identifiers) rather than raw, token-heavy observation data.

This directly challenges the current LangGraph pattern of passing a shared State dict. The architectural tradeoff: context isolation prevents token bloat and hallucinatory consensus (agents can't leak each other's reasoning), but requires a disciplined serialization layer for inter-agent messages.

**Hybrid Smart Routing**: A lightweight heuristic router at the FastAPI gateway classifies incoming events at runtime with zero LLM inference cost:
- **Simple events** (routine Kalshi news headline, scheduled data release) → routed directly to the Execution agent via high-speed MCP protocol (single-agent fast path)
- **Complex events** (unexpected FOMC rate decision, cross-asset dislocation) → routed to the full five-agent LangGraph debate (multi-agent deep path)

The heuristic uses keyword matching + regex patterns. A mandatory fallback to the deep path handles edge cases where the heuristic misclassifies. This is the traffic-shaping complement to the topology discussion — not every market event needs the full Devil's Advocate treatment, and the token budget should be reserved for genuinely complex decisions.

**6-Metric Observability Dashboard**: The paper's evaluation methodology — measuring wall-clock latency, token count, cost in USD, LLM API calls, Data Source API calls, and code complexity (LoC + AST cyclomatic) — provides a rigorous framework for comparing the as-built linear topology against any future scatter-gather or distributed-context variant. Implementing this dashboard in the LGTM stack (~4h) would provide objective evidence for the Option A vs B decision.

### Redis Semantic Caching (K16, 2026-05-01)

K16 surfaces a cache-aside pattern that complements the topology layer: when a market signal arrives at a LangGraph analyst node, the system hashes the tuple `(prompt, model, temperature)` and queries Redis before invoking the LLM. On a cache hit, the LLM is bypassed entirely — the cached Pydantic-typed output is returned directly, saving the full CPU inference cycle.

The pattern is pragmatic for CPU-bound infrastructure where inference is the bottleneck, but it introduces a topology-level subtlety: cached outputs are frozen at the timestamp of original generation. If two different analyst nodes (e.g., technical and sentiment) receive the same prompt hash — because the input signal is identical — they receive the same cached output, collapsing the diversity that scatter-gather is designed to produce. The mitigation prescribed in K16 is to include the agent role in the hash key (not just prompt+model+temperature), ensuring that each analyst node's cache namespace is independent.

This pattern extends the topology discussion without modifying it: it's a performance optimization at the node level, not a topology change. Redis already serves as the inter-agent communication bus (Redis Streams for scatter-gather message passing); adding a caching dimension reuses the same infrastructure for a different purpose. The cache TTL (5 minutes in the K16 prescription) bounds staleness risk.

### Generator-Evaluator Loop (K17, 2026-05-01)

K17 adds an adversarial control layer on top of the topology, derived from Anthropic's published harness research for long-running autonomous applications. The core finding: LLM agents are incapable of objective self-evaluation — they reliably skew positive, praising mediocre outputs and overlooking subtle logical flaws. The solution bifurcates the topology into asymmetric roles:

- **Generator agent**: Proposes the thesis (e.g., long position on Hyperliquid perpetuals based on Open-Meteo weather data correlated with a Kalshi prediction market)
- **Evaluator agent**: An isolated, skeptical critic calibrated with few-shot examples, instructed to demand concrete verification. Challenges statistical assumptions, liquidity constraints, and historical backtest alignments.

The evaluator uses **financial-grade subjective quantification metrics** — translating the Anthropic harness's abstract criteria (Design Quality, Originality, Craft, Functionality) into: **Statistical Significance, Correlation Robustness, Drawdown Probability, and Execution Latency Tolerance**. Each metric receives a quantitative score, converting linguistic reasoning into numerical inputs for the 28-feature Polars RL observation space.

The Redis pub/sub bus serves as the externalized state mechanism: the generator publishes its structured thesis to a Redis channel; the evaluator consumes, assesses, and responds with an immutable evaluation metric. This interaction pattern is a specialization of the existing Devil's Advocate debate protocol — it adds explicit role asymmetry (generator vs evaluator), few-shot calibration of the evaluator, and mandatory quantitative scoring rather than free-form debate.

**IP-sale significance**: This adversarial structure directly addresses the institutional buyer's primary concern — that an LLM-driven trading system could execute rogue, unchecked decisions based on hallucinated correlations. The generator-evaluator loop provides a mathematically rigorous vetting layer that is independently auditable (each evaluation metric is a scalar in the observation space, logged immutably via the cryptographic audit trail).

### Fractals recursive decomposition (K18, 2026-05-01)

K18 (Resource 8 — TinyAGI/fractals) introduces a third orchestrator topology variant: tree-based recursive decomposition. Unlike the existing Send-API fan-out (flat, single-level scatter) and Generator-Evaluator (adversarial pair), fractals operates as a hierarchical orchestrator that decomposes high-level objectives into a self-similar tree of executable subtasks:

- **Planning phase**: An LLM classifies and decomposes the root task into a strict hierarchy, producing a tree where each node is a discrete subtask with defined inputs/outputs.
- **Execution phase**: Leaf tasks run in fully isolated Git worktrees, using depth-first, breadth-first, or layer-sequential batch strategies. A planned backpropagation agent merges results upward through the tree.
- **Isolation guarantee**: Each subtask executes in its own Git worktree, preventing cross-task context contamination — the same problem the existing topology's per-agent context isolation (K15, Distributed Context Windows) addresses at the agent level.

The Cemini application (per K18): when an anomaly is detected in SEC EDGAR data streams, the root node spawns parallel subtasks — one agent queries Finnhub for news sentiment, another scrapes Quiver Quantitative for congressional trading activity, a third calculates statistical variance — with results merged back through the tree for the Trader Arbiter's final assessment.

This topology is orthogonal to the existing patterns: Send-API (K) handles breadth (fan-out to N analysts), Generator-Evaluator (K17) handles depth (adversarial refinement within a single analysis), and fractals (K18) handles hierarchy (recursive decomposition with tree-structured merge). The three can compose: a fractals root node could fan out via Send-API to N analyst leaf nodes, each of which runs an internal Generator-Evaluator loop.

**Current state**: K18 verdict is "Keep on Radar" — await MCP layer stabilization before deep integration. The Hono/TypeScript runtime is wrong for Cemini's Python stack, but the recursive decomposition pattern is runtime-agnostic and portable to LangGraph's typed StateGraph substrate. The isolated Git worktree execution model is the novel architectural primitive — it provides stronger isolation guarantees than the existing per-agent context isolation (which is process-level, not filesystem-level).

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

### SAE execution-layer middleware (K19, 2026-05-01)

@concepts/sae-execution-contract.md introduces a fourth position in the
execution topology: the **terminal enforcement layer** downstream of the
orchestrator. Where Send-API, Generator-Evaluator, and Fractals
determine *which agents run in what order*, SAE determines *whether
their outputs become side effects*. It sits at the last-mile boundary:

```
Orchestrator (Send / GenEval / Fractals)
       ↓
  Strategy Engine (LLM or non-LLM)
       ↓
  ExecutionRequest
       ↓
  SAE Middleware ← Regime Detector, Trust State, Policy Engine
       ↓
  ExecutionDecision (ALLOW / LIMIT / BLOCK)
       ↓
  Exchange Executor
```

This is orthogonal to the three orchestrator variants and composes with
all of them. The orchestrator governs *computation topology*; SAE
governs *execution authorization*. An Intended Policy Spec (tool/venue
allowlists, risk budgets, market-state constraints, account-state
constraints) provides deterministic out-of-scope labeling — the same
specification drives both enforcement and measurement.

For Cemini: SAE middleware would sit at the terminal leaf of the
scatter-gather graph, downstream of whichever orchestrator variant is
active and upstream of the Binance/hyperliquid executor. The
ExecutionDecision contract maps naturally onto Cemini's existing
config-driven approach — the Intended Policy Spec is a YAML artifact
consistent with K8's YAML-defined topology and K18's SDD contracts.

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
