---
title: "Conductor — Lightweight Multi-Model Orchestrator"
type: concept
tags: [concept, orchestration, model-routing, grpo, training-free, multi-agent, conductor, synthesis]
keywords: [conductor, orchestrator, model-routing, grpo, multi-model, tool-use, cascade, token-prior, api-only, cemini-architecture]
related:
  - concepts/llm-agent-systems.md
  - concepts/scatter-gather-topology.md
  - concepts/agent-native-research-artifacts.md
  - sources/toolorchestra-2511.21689.md
  - sources/mmgrpo-iclr-2026.md
  - sources/training-free-grpo-iclr-2026.md
  - sources/select-then-route-emnlp-2025.md
  - sources/masrouter-acl-2025.md
  - sources/gigpo-neurips-2025.md
  - sources/meta-router-2509.25535.md
  - concepts/recursive-multi-agent-systems.md
  - concepts/kimi-agent-swarm-vs-claude-agent-teams.md
  - sources/blade-bayesian-listwise-alignment.md
  - concepts/llm-listwise-alignment.md
  - sources/regime-conditioned-bo-evaluation.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/verbalized-sampling-llm-diversity.md
  - concepts/llms-get-lost-mitigation-audit.md
  - sources/arxiv-coordination-layer-multi-agent-2605-03310.md
  - concepts/interaction-native-knowledge-harness.md
  - sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - sources/arxiv-maven-agentic-tool-calling-2605.30738-2026-06-05.md
  - concepts/agent-memory-cross-scenario-generality.md
  - concepts/agents-last-exam-benchmark.md
  - concepts/adk-arena-framework-evaluation.md
  - sources/arxiv-agents-last-exam-2606.05405-2026-06-06.md
  - sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md
  - sources/arxiv-less-context-better-agents-2606.10209-2026-06-10.md
  - concepts/context-compression-resume-pattern.md
  - concepts/context-fractured-decomposition-attacks.md
  - sources/arxiv-context-fractured-decomposition-cfd-2606.09084-2026-06-12.md
  - sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598-2026-06-16.md
  - concepts/orchestration-reward-modeling-orch-rm.md
  - sources/arxiv-agents-all-the-way-down-2606.11869-2026-06-16.md
  - concepts/agents-all-the-way-down-methodology.md
maturity: validated
hub: true
created: 2026-05-01
updated: 2026-06-16
---

## Relations

- @concepts/agents-last-exam-benchmark.md — long-horizon professional workflow eval (REFERENCE)
- @concepts/adk-arena-framework-evaluation.md — framework choice at ecosystem scale (REFERENCE)
- @sources/arxiv-agents-last-exam-2606.05405-2026-06-06.md — ALE source (K101)
- @sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md — ADK Arena source (K101)
- @concepts/agent-memory-cross-scenario-generality.md — conductor fan-out vs agent-controlled recall (2606.04315)
- @concepts/interaction-native-knowledge-harness.md — passive injection vs query-time wiki-walk (K99)
- @sources/arxiv-interaction-native-knowledge-harness-2606.01886.md — InKH retrieval model (K99)
- @sources/arxiv-maven-agentic-tool-calling-2605.30738-2026-06-05.md — tool-calling OOD generalization REFERENCE (K100)
- @ccc-wiki/concepts/maven-agentic-tool-calling-generalization.md — CCC-primary MAVEN synthesis
- @concepts/agent-team-five-gate-decision-memo.md — K98 five-gate org chart
- @concepts/nemo-execution-aware-optimization-modeling.md — K98 sandboxed OR agents (REFERENCE)
- @concepts/seclaw-agent-security-evaluation.md — K98 agent security eval (REFERENCE)
- @concepts/context-fractured-decomposition-attacks.md — K112 provenance gap / CFD (artifact lineage)
- @concepts/orchestration-reward-modeling-orch-rm.md — K118: orchestration-level BoN + reward-guided continued training
- @sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598-2026-06-16.md — Orch-RM source (K118)
- @concepts/agents-all-the-way-down-methodology.md — K118: ship-as-CLI + agent-tests-agent eval layer
- @sources/arxiv-agents-all-the-way-down-2606.11869-2026-06-16.md — Agents All the Way Down source (K118)
- @concepts/llm-agent-systems.md — Conductor is the orchestration layer for the LLM agent systems cluster.
- @sources/arxiv-coordination-layer-multi-agent-2605-03310.md — argues coordination should be a separable, configurable architectural layer; Brier/Murphy evaluation method applicable to the conductor
- @concepts/scatter-gather-topology.md — Conductor replaces manual scatter-gather topology selection with learned routing decisions.
- @sources/toolorchestra-2511.21689.md — **Architecture blueprint**: 8B orchestrator beats GPT-5 at 2.5× efficiency.
- @sources/mmgrpo-iclr-2026.md — **Optimization method A**: Multi-module GRPO for compound AI systems. 11% gain, open source.
- @sources/training-free-grpo-iclr-2026.md — **Optimization method B**: Token-prior approach for API-only deployment. Tested on DeepSeek-V3.1.
- @sources/select-then-route-emnlp-2025.md — **Routing layer**: Taxonomy-guided two-stage routing + cascade. 4× cost reduction.
- @sources/masrouter-acl-2025.md — **Multi-agent extension**: Collaboration mode + role allocation + LLM selection. 52% cost reduction.
- @sources/gigpo-neurips-2025.md — **Multi-turn credit assignment**: Two-level GRPO for agent trajectory optimization.
- @sources/meta-router-2509.25535.md — **Evaluation framework**: Causal correction of LLM-as-judge bias for router training.
- @concepts/verbalized-sampling-llm-diversity.md — **Third orthogonal training-free layer** (K39): VS at generation time complements reviewer-agent (inline call gating) and signals (post-hoc triage). All three sit on the same prompt-and-orchestration substrate.
- @ccc-wiki/entities/tools/conductor-mcp.md — CCC-side entity page for Cemini's `conductor` MCP server (the cross-wiki query router that implements this orchestration concept at the federation level)
- @ccc-wiki/concepts/subagent-orchestration.md — CCC-side concept covering when Cemini delegates work to a subagent inside Claude Code, which composes with this orchestration layer

## Raw Concept

K25 Conductor targeted research sweep (7 papers ingested from 25 candidates across 5 queries). Three clusters converged: GRPO optimization, model routing, and orchestration frameworks. The synthesis: a **lightweight orchestrator that routes queries to the right model+tool combination**, optimized via GRPO without requiring model weight access, producing better results at lower cost than any single frontier model.

## Narrative

### What is Conductor?

Conductor is a proposed Cemini architecture component: a small, lightweight model (or token-prior prefix on an existing model) that decides **which model and which tool should handle each query**. Instead of sending every request to DeepSeek-V4 (expensive) or a single cheap model (inaccurate), Conductor classifies the query, selects the right model from a pool, and escalates only when confidence is low.

The K25 sweep found that this architecture is not just viable — it's **proven to beat frontier models**. ToolOrchestra's 8B orchestrator surpasses GPT-5 on HLE (37.1% vs 35.1%) at 2.5× lower cost.

### Why Conductor?

Cemini currently routes all analyst queries through DeepSeek-V4-flash via the hosted API. This is:
- **Expensive**: every query pays the frontier-model cost
- **Inflexible**: can't use cheaper models for simple queries or specialized models for specific domains
- **Single point of failure**: if DeepSeek API is down, the analyst is blind

Conductor introduces a routing layer that:
1. Classifies each query by type (ticker lookup, options analysis, sentiment, market microstructure, etc.)
2. Selects the appropriate model from a pool (could be DeepSeek-V4 for hard queries, Qwen2 7B for simple lookups, a specialized finance model for quantitative tasks)
3. Cascades upward only when a multi-judge confidence check signals low reliability
4. Optimizes this routing policy over time via GRPO on observed outcomes

### Architecture blueprint (from K25 papers)

```
QUERY → ┌─────────────────────────────────────┐
        │  STAGE 1: Taxonomy Classifier        │  ← StR (Select-Then-Route)
        │  "What kind of question is this?"     │
        │  → reasoning / code / data / fact     │
        └─────────────────────────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────────┐
        │  STAGE 2: Model Pool Selection       │  ← StR + MasRouter
        │  "Which 2-4 models can handle this?"  │
        │  Select from pool, cheapest first     │
        └─────────────────────────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────────┐
        │  STAGE 3: Cascade + Confidence Gate  │  ← StR multi-judge
        │  Try cheapest model → judge output    │
        │  If low confidence → escalate         │
        └─────────────────────────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────────┐
        │  STAGE 4: Tool Orchestration          │  ← ToolOrchestra
        │  Route to appropriate tool            │
        │  (calculator, RAG, web search, etc.)  │
        └─────────────────────────────────────┘
                          │
                          ▼
                    RESPONSE

        ┌─────────────────────────────────────┐
        │  OPTIMIZATION LOOP                   │
        │  MMGRPO (full training)               │
        │  OR Training-Free GRPO (token prior)  │
        │  + GiGPO multi-turn credit assignment │
        │  + Meta-Router evaluation correction  │
        └─────────────────────────────────────┘
```

### Two deployment paths

**Path A — Trained Orchestrator** (ToolOrchestra + MMGRPO + GiGPO):
- Train a small (8B) orchestrator model via RL
- Highest performance ceiling (beats GPT-5)
- Requires model hosting (need a GPU for the 8B orchestrator)
- Full GRPO optimization with multi-module + multi-turn credit assignment

**Path B — Token-Prior Orchestrator** (Training-Free GRPO):
- No model training needed — construct token priors as prompt prefixes
- Works with API-only deployment (DeepSeek hosted API)
- Lower performance ceiling but zero infrastructure cost
- Few dozen calibration samples sufficient
- Tested on DeepSeek-V3.1 (same family as Cemini's V4-flash)

Path B is the pragmatic starting point for Cemini: build token-prior routing prefixes, calibrate on analyst runs, deploy without infrastructure changes. Graduate to Path A when the cost/performance inflection justifies a dedicated orchestrator model.

### Evaluation framework

Meta-Router provides the causal framework for evaluating routing quality:
- LLM-as-judge evaluates 95% of routing decisions (cheap, scalable)
- Periodic gold-standard expert calibration corrects judge bias
- Causal adjustment prevents systematic drift toward judge-preferred models

### What Conductor is NOT

- **Not a model trainer** — Conductor doesn't fine-tune the models it routes to. It optimizes the *routing decision*, not the model weights.
- **Not a replacement for LangGraph** — Conductor sits above the existing scatter-gather topology, deciding which agents to activate, not replacing the execution engine.
- **Not a real-time trading component** — routing decisions add latency. Conductor is for analyst queries, not tick-level execution.

**Agent-skill architecture validated**: Both the ARA Live Research Manager and ARA Compiler (@concepts/agent-native-research-artifacts.md) are implemented as natural-language specifications loaded into context windows — not custom SDKs. This independently validates Conductor's Path B approach (prompt-based token-prior routing rather than a trained model). The agent-skill pattern (spec in context → agent becomes specialist) is emerging as a general architecture for LLM-native infrastructure, not just a Conductor shortcut. When Path A activates, the orchestrator training data will come from Path B's agent-skill routing logs — the two paths are sequential, not competing.

**Path C — RecursiveLink-style training**: @concepts/recursive-multi-agent-systems.md provides a training-based alternative. Conductor's current 4-stage pipeline (taxonomy → pool → tools → cascade) communicates through text-based handoffs. RecursiveMAS replaces text communication with lightweight 2-layer residual connector modules (RecursiveLinks) between pipeline stages, then co-optimizes the entire pipeline via inner-outer loop training. Only the RecursiveLinks are trained (0.31% of params) — model weights stay frozen. This would enable: (1) gradient-based credit assignment across pipeline stages (vs post-hoc calibration logging); (2) latent-space information transfer between stages (vs prompt-based handoffs); (3) system-level co-optimization through joint backpropagation. The cost is low: RecursiveLink training uses 56% less GPU than LoRA while achieving better performance. Path C is a long-term research direction — Path B (token priors) is the pragmatic zero-training entry point.

### Next steps

1. **Calibration data collection**: log current analyst query → model → outcome triplets to build routing training data
2. **Token-prior prototype (Path B)**: construct routing prefixes from calibration data, A/B test against baseline (always DeepSeek-V4)
3. **Taxonomy design**: define Cemini's query type taxonomy (ticker lookup, options analysis, sentiment, market microstructure, etc.) based on historical analyst query patterns
4. **Pool selection**: identify candidate models for each taxonomy class (DeepSeek-V4 for hard, Qwen2-7B for simple, KronosTokenizer for technical, etc.)
5. **Path A evaluation gate**: if Path B shows meaningful cost reduction with quality preservation, evaluate whether the 8B orchestrator hosting cost is justified

### Planned taxonomy class additions (K30 derivative)

Per `@briefs/2026-05-05_polymarket-stack-adoption.md`, Conductor's taxonomy will gain a new class once the Polymarket integration ships:

| Taxonomy class | Pool | Tools | Special handling |
|----------------|------|-------|------------------|
| `prediction_market_polymarket` | `[deepseek-v4-flash, deepseek-v4-pro]` | `polymarket_place_order`, `polymarket_get_market`, `polymarket_get_positions`, `polymarket_cancel_order` | `require_human_confirmation_above_usdc: 1000` (per `@concepts/sae-execution-contract.md` M0029 mitigation from `@concepts/mitre-atlas-taxonomy.md`) |

This pairs with the planned `prediction_market_kalshi` taxonomy class (gates on `pykalshi` adoption per `@entities/tools/pykalshi.md`). Both classes will route through Conductor's existing 4-stage pipeline; the addition is to the taxonomy + pool + tools registry, not the runtime architecture.

**Cross-references**:
- `@briefs/2026-05-05_polymarket-stack-adoption.md` — the brief that lands this class
- `@concepts/polymarket-market-making-architectures.md` — downstream consumer (MM strategies route via this class)
- `@concepts/cross-venue-arbitrage-pattern.md` — downstream consumer (arb routes via this + Kalshi class)
- `@entities/tools/polymarket-agents.md`, `@entities/tools/polymarket-python-order-utils.md` — the integration stack the tools wrap

### Conductor evolution candidates (active workstreams)

Two distinct Conductor evolution paths surfaced in K28 + K29 + K30, both staged as briefs:

1. **atlas-gic-style autoresearch** — `@briefs/2026-05-04_autoresearch-conductor-evolution.md`. Sharpe-loss + git-commit/revert mutation loop applied to routing rules. Clean-room re-implementation (atlas-gic NO LICENSE).
2. **XSKILL-style cross-rollout critique** — `@briefs/2026-05-04_xskill-cross-rollout-critique-conductor.md`. MLLM-judged comparison of routing decisions feeds proposal stage of #1's loop. Companion to #1; ships together.

Both pair with the autoresearch-loop-pattern concept (`@concepts/autoresearch-loop-pattern.md`) which K30 extended with a fifth documented instantiation (DW-GRPO from Deep GraphRAG). DW-GRPO is the model-weight-level mutation variant, distinct from prompt/config-level mutations targeted by the two briefs above. **Cemini does not yet have a model-weight-mutation workstream**; DW-GRPO stays at concept-page-only depth until/unless training infrastructure is built.

## Snippets

**S1 — ToolOrchestra core claim**:
> "We show that small orchestrators managing other models and a variety of tools can both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks." [Source: @sources/toolorchestra-2511.21689.md]

**S2 — 8B beats GPT-5**:
> "On HLE, Orchestrator achieves a score of 37.1%, outperforming GPT-5 (35.1%) while being 2.5x more efficient." [Source: @sources/toolorchestra-2511.21689.md]

**S3 — Training-Free GRPO on DeepSeek**:
> "Training-free GRPO, when applied to DeepSeek-V3.1, significantly improves out-of-domain performance. With just a few dozen training samples, Training-free GRPO outperforms fine-tuned small LLMs." [Source: @sources/training-free-grpo-iclr-2026.md]

**S4 — StR routing efficiency**:
> "StR improves the end-to-end accuracy from 91.7% to 94.3% while reducing inference cost by 4×." [Source: @sources/select-then-route-emnlp-2025.md]

**S5 — MasRouter cost reduction**:
> "Reducing overhead by up to 52.07% compared to baseline approaches." [Source: @sources/masrouter-acl-2025.md]

**S6 — MMGRPO improvement**:
> "mmGRPO improves accuracy by 11% on average against the post-trained LM — and by 5% against prompt optimization on its own." [Source: @sources/mmgrpo-iclr-2026.md]
