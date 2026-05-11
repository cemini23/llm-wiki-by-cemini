---
title: Sakana Fugu (multi-agent orchestration API, closed beta)
type: entity
tags: [infrastructure, llm, llm-orchestration, hosted-api, openai-compatible, beta-product, sakana-ai, third-party-service]
keywords: [sakana, fugu, fugu-mini, fugu-ultra, multi-agent-orchestration, conductor-product, trinity-product, openai-compatible-api, learned-orchestrator-as-a-service]
related:
  - entities/infrastructure/deepseek-api.md
  - entities/frameworks/langgraph.md
  - concepts/scatter-gather-topology.md
  - concepts/llm-agent-systems.md
  - concepts/rl-marl-research.md
  - concepts/ip-sale-readiness.md
  - sources/sakana-conductor-rl-orchestration.md
  - sources/sakana-trinity-llm-coordinator.md
maturity: validated
created: 2026-04-27
updated: 2026-05-10
---

## Relations

- @entities/infrastructure/deepseek-api.md — sibling hosted-LLM service in the Cemini-considered API pool. Where DeepSeek serves a single frontier-class model behind the OpenAI-compatible endpoint, Fugu serves a *learned orchestrator over a pool of frontier models* behind the same shape of endpoint. Both could coexist as worker-pool entries OR Fugu could subsume the DeepSeek-API role for orchestration-heavy paths
- @entities/frameworks/langgraph.md — Fugu offers an *outsourced* alternative to the framework Cemini uses to *hand-design* orchestration. Where LangGraph requires the engineer to design the graph topology + state-passing reducers, Fugu hides the orchestration entirely behind an OpenAI-compatible chat-completions endpoint. **Architecturally orthogonal**: one could keep LangGraph as the outer-supervisor / state-checkpointer + call Fugu as a single "smart" worker node in the StateGraph, OR replace the LangGraph orchestration layer entirely with Fugu's API for the LLM-reasoning portion of the pipeline
- @concepts/scatter-gather-topology.md — Fugu is the **commercial productization of the alternative path** to Cemini's prescribed scatter-gather. The 3-19 source prescribes a hand-designed `Send()`-based fan-out + `operator.add` reducer; Fugu *learns* the topology and delivers it as an API call. **This adds a third option to the open Option A vs Option B P1 ticket: Option C — outsource orchestration to Fugu (or equivalent), preserve the deployed linear StateGraph as a thin front-end**. Likely the lowest-engineering-effort path to "learned-orchestrator quality" without training one in-house
- @concepts/llm-agent-systems.md — cluster-hub backlink; Fugu is the first commercial-API entry in the cluster (vs all-academic-paper sources that preceded it). Marks the transition of "learned LLM orchestration" from research to commodity service
- @concepts/rl-marl-research.md — cluster-hub backlink; Fugu's underlying methodology is the GRPO-trained Conductor (rl-marl cluster). Productized closed-beta launch of an RL-trained meta-controller is a noteworthy datapoint for the cluster's "RL-on-orchestration-layer" thread
- @concepts/ip-sale-readiness.md — Fugu directly affects the IP-sale narrative. An institutional buyer reading the Cemini stack will now ask: "why didn't you just call Fugu's API?" The defensible answer is *vertical-domain fine-tuning* + *custom worker-pool composition* + *typed-output structured Pydantic StrategyRecommendation handoff* — Fugu's chat-completions interface doesn't natively handle Pydantic-typed agent outputs the way Cemini's LangGraph nodes do. But the question must be anticipated and answered
- @sources/sakana-conductor-rl-orchestration.md — parent academic paper (one of two); Fugu Ultra 🐡 is the productized Conductor (+ improvements on top per Sakana's "substantially further improved" framing)
- @sources/sakana-trinity-llm-coordinator.md — **second parent academic paper** (ingested 2026-04-28). Trinity's lightweight 0.6B-SLM + 10K-head + sep-CMA-ES coordinator architecture is the likely **Fugu Mini 🐟** basis, paralleling Conductor's likely Fugu Ultra basis. The Sakana announcement explicitly names *both* "Trinity and Conductor" as the underlying ICLR 2026 papers; the two-tier API split (Mini latency-optimized / Ultra full-orchestration) maps cleanly onto the two papers' compute-envelope split (Trinity <20K params / Conductor 7B params). Trinity also adds a **structured-output orchestration option** Conductor doesn't directly provide — the Thinker/Worker/Verifier role schema is closer to a typed-state-graph contract than Conductor's free-form natural-language prompts

## Raw Concept

- **Product name**: Sakana Fugu (Mini / Ultra two-tier lineup)
- **Vendor**: Sakana AI (Japan-based frontier-research lab)
- **Launch announcement**: 2026-04-24 (`sakana.ai/fugu-beta/`) — three days before this page was created
- **Status**: Closed beta — application gate, not generally available
- **Interface**: API, OpenAI-compatible chat-completions endpoint shape
- **Underlying methodology**: Productization of two ICLR 2026 papers — *Learning to Orchestrate Agents in Natural Language with the Conductor* (Nielsen, Cetin, Schwendeman, Sun, Xu, Tang) + *TRINITY: An Evolved LLM Coordinator* (Xu, Sun, Schwendeman, Nielsen, Cetin, Tang). Both name the same six authors in slightly different lead orderings, indicating Fugu is the joint productization
- **Why it's in the corpus**: User-dropped 2026-04-27 (URL `https://sakana.ai/fugu-beta/`) as a follow-up to the Conductor paper ingest the same day. Fugu is the load-bearing operationalization datapoint — the Conductor paper proves an RL-trained orchestrator beats GPT-5; Fugu proves the result is being commercialized within months of paper publication

## Narrative

### One-paragraph summary

Sakana Fugu is a closed-beta multi-agent orchestration API that wraps a learned meta-controller (the productized Conductor + Trinity from Sakana's ICLR 2026 papers) behind an OpenAI-compatible chat-completions endpoint. Two tiers: **Fugu Mini 🐟** (latency-optimized) and **Fugu Ultra 🐡** (full orchestration, performance-optimized). Reported to beat the frontier-model field on coding (LCBv6 93.2 vs Opus 4.6's 92.4), scientific reasoning (GPQAD 95.1 vs Gemini 3.1's 94.4), and software-engineering benchmarks (SWEPro 54.2 vs Opus 4.6's 53.4) using a *small* internal orchestrator that calls into the frontier-model pool. Behind the OpenAI-compatible facade, Fugu handles model-routing + topology-design + role-assignment + subtask-dispatch automatically. Recursive self-calling unlocks a tunable test-time-scaling axis. Launched April 24, 2026.

### Productization framing — Conductor + Trinity → Fugu

The Sakana announcement explicitly names the dual paper foundation:

> "Sakana Fugu models are based on our ICLR 2026 papers (Trinity and Conductor), and we have substantially further improved the methods to increase the performance and user experience, to be offered as a commercial product."

This collapses two key research → product gaps:

1. **Time gap**: ICLR 2026 paper submission to commercial closed-beta launch in months. The Conductor paper (arXiv 2512.04388v4) was finalized 1 March 2026; the Fugu beta launched 24 April 2026 — ~7 weeks elapsed. Suggests Sakana ran the productization in parallel with the academic submission, not after
2. **Interface gap**: The Conductor paper benchmarks a research-grade harness; Fugu wraps the same methodology behind the OpenAI-compatible API shape (the de facto integration standard since GPT-3 days). This eliminates the "interesting research, but how do I use it" friction that kills most MoA / multi-agent-orchestration academic results

### Two-tier lineup

| Tier | Symbol | Optimization target | Use case |
| --- | --- | --- | --- |
| **Fugu Mini** | 🐟 | Latency | Lower-budget paths that can't afford full pool-call latency. Equivalent throughput envelope to a single frontier-model call |
| **Fugu Ultra** | 🐡 | Full orchestration / performance | The complete Conductor-style worker-pool fan-out + topology-design + recursive-self-call path |

The two-tier framing is itself an architectural signal: Sakana is acknowledging the latency cost of full multi-model orchestration (each pool member is its own API round-trip + a Conductor round-trip on top) and offering a stripped-down variant for cost/latency-sensitive integrations.

### Benchmarks (Sakana-reported, beta numbers)

From the Sakana announcement page:

| Task | Gemini 3.1 (high) | GPT 5.4 (high) | Opus 4.6 (max) | Fugu Mini 🐟 | Fugu Ultra 🐡 |
| --- | --- | --- | --- | --- | --- |
| GPQAD | 94.4 | 90.9 | 92.7 | 92.4 | **95.1** |
| LCBv6 | 90.3 | 92.1 | 92.4 | 90.4 | **93.2** |
| SWEPro | 48.4 | 51.2 | 53.4 [^a] | 51.3 | **54.2** |

[^a] Opus SWEPro uses Anthropic's self-reported max-thinking score; Sakana's own evaluation runs hit timeouts.

**Read**:

- Fugu Ultra **wins every benchmark** in the comparison set. The lift over the best individual frontier model is small but consistent (GPQAD: +0.7 over Gemini 3.1; LCBv6: +0.8 over Opus 4.6; SWEPro: +0.8 over Opus 4.6 self-reported)
- The benchmark comparison set names **forward-dated frontier models** (Gemini 3.1, GPT 5.4, Opus 4.6) — these are 2026-release-calendar version numbers, not arbitrary version bumps. Sakana is benchmarking against the contemporary frontier, not the versions in the Conductor paper (which compared against GPT-5, Claude Sonnet 4, Gemini 2.5 Pro)
- Fugu Mini sits between Gemini 3.1 and GPT 5.4 on most benchmarks — it's a competitive single-model alternative even before the latency optimization is taken into account
- **Independence not yet verified** [NEEDS VERIFICATION 2026-05-10] — these are vendor-reported beta numbers; no third-party reproduction yet. Exa cross-check 2026-05-10: no independent benchmarks surfaced; Fugu still closed beta.

### OpenAI-API compatibility

> "If you are already using GPT, Gemini, or Claude via API, Sakana Fugu can be integrated into existing workflows with minimal changes. Behind that familiar interface, Sakana Fugu handles coordination across the model pool automatically — establishing the collaboration topology, assigning the roles and dispatching the subtasks to complete complex tasks."

The OpenAI-compatible endpoint shape means the Cemini DeepSeek client at `services/llm_analyst/deepseek_client.py` (`openai.OpenAI(base_url=..., api_key=...)` pattern per @entities/infrastructure/deepseek-api.md) could swap to Fugu by changing two strings: the base URL and the model name. **This is the integration cost**: ~5 lines of config + an API-key swap, not a port.

### Recursive test-time scaling (paper footnote, expanded)

The Sakana page calls out the recursive-self-call axis explicitly:

> "When a Fugu model is allowed to call itself recursively, reading its own prior output as context and deciding whether to revise its coordination strategy, a new form of test-time scaling emerges. The model recognizes when its first attempt fell short and spins up a corrective workflow. The depth of recursion becomes a tunable compute axis at inference time, requiring no retraining. A small model, by reading itself, can iterate toward answers that neither it nor any of its workers could reach in a single pass."

Mirrors @sources/sakana-conductor-rl-orchestration.md S2 (Recursive Conductor variant, Section 3.2 / 4.4). Fugu offers this as a knob exposed through the API rather than a fixed inference-time setting — meaning a Fugu API consumer could trade compute budget for accuracy on a per-call basis.

### Cemini-relevance read

**4 hooks tying Fugu directly into the deployed Cemini stack**:

1. **DeepSeek client reframing extends to Fugu** — @entities/infrastructure/deepseek-api.md was already reframed (post-Conductor-ingest) from "single shared client across 4 analyst nodes" to "worker pool entry the meta-controller dispatches to." Fugu is the *materialized* meta-controller. So the reframing tightens: Cemini could stop shipping a custom orchestrator entirely for the LLM-reasoning leg and instead point its analyst node directly at `https://api.sakana.ai` (or Sakana's beta endpoint). The DeepSeek-API path becomes a worker pool entry *inside Fugu's pool*, not a Cemini-side dispatch

2. **Scatter-gather Option C** — adds a third option to the existing P1 ticket on @concepts/scatter-gather-topology.md:
    - **Option A**: build Send() topology fresh per step83 design spec (~1–2 engineer-weeks, hand-designed)
    - **Option B**: keep deployed linear 4-analyst StateGraph as IP-sale narrative (~0.5 engineer-days, relabel only)
    - **Option C (NEW 2026-04-27)**: outsource orchestration to Fugu's API; the deployed linear StateGraph becomes a thin Pydantic-output formatter wrapping a single Fugu chat-completion call. Engineering effort: ~1–3 engineer-days (config swap + Pydantic glue + audit-trail integration). Requires Fugu beta access (application-gated)
    - **Decision drivers**: data-egress posture (Fugu sees prompts), audit-trail integration (Fugu's internal sub-routing is opaque to the pg_tamperlog chain — only the (prompt, completion, model_id, timestamp) tuple is locally verifiable, not the per-worker fan-out), and acquirer optics (an acquirer might value *vertical-domain fine-tuning* over *commodity-API consumption*). Option C is the lowest-effort path but cedes the most architectural surface

3. **IP-sale narrative impact** — an acquirer with a GPU cluster reading the Cemini stack will ask: *"if Sakana's Fugu beats GPT-5 with a 7B orchestrator and is shipping as an API, why is your moat?"* The defensible answer must include:
    - **Vertical-domain RL training** — Cemini's MAPPO trader-agents trained on ticker-environment rewards are a fundamentally different artifact than Fugu's general-purpose orchestrator
    - **Typed-output structured handoff** — Cemini's analysts return Pydantic-typed `StrategyRecommendation` objects, which Fugu's chat-completions interface doesn't natively handle (would need post-call schema validation + retry logic on the Cemini side)
    - **Custom worker-pool composition** — Cemini gets to choose which worker LLMs are in scope (compliance, data-egress, cost) rather than accept Sakana's fixed-pool decisions
    - **Audit-trail completeness** — pg_tamperlog captures Cemini's full per-node reasoning chain; Fugu only exposes the top-level (prompt, completion) tuple
    - These are real differentiators but they need to be *named explicitly in the IP-sale prep narrative*. Track-record-of-using-Fugu-as-a-baseline could itself be a credibility marker (Cemini benchmarked against Fugu and chose vertical-fine-tuning — defensible)

4. **Trinity sibling paper now in corpus** `[RESOLVED 2026-04-28]` — sibling ICLR 2026 paper *TRINITY: An Evolved LLM Coordinator* (Xu, Sun, Schwendeman, Nielsen, Cetin, Tang) ingested 2026-04-28 as `@sources/sakana-trinity-llm-coordinator.md`. arXiv ID confirmed at **2512.04695** (range-neighbor to Conductor's 2512.04388, both submitted same week of December 2025). Trinity's "evolved coordinator" framing turns out to mean **separable Covariance Matrix Adaptation Evolution Strategy (sep-CMA-ES)** — a derivative-free training method that the paper's ablations show *dominates* RL/REINFORCE under binary-reward + weak-parameter-coupling regimes (REINFORCE collapses to 0.253 on LCB vs sep-CMA-ES's 0.615). Confirms the architectural read on this page: Fugu Mini 🐟 likely productizes Trinity (lightweight: 0.6B SLM + 10K head, total <20K learnable params), Fugu Ultra 🐡 likely productizes Conductor (heavyweight: 7B Qwen2.5-base meta-controller). The two-tier Fugu API now has clean academic-paper backing on both tiers

### Integration risk + open questions

- **[NEEDS VERIFICATION 2026-05-10]** Beta acceptance gate — application-only access. Exa cross-check 2026-05-10: still closed beta, no change to application gate. Cemini would need to apply, with no guarantee of acceptance. Sakana explicitly targets “researchers and engineers” — Cemini-as-prop-trading-shop may or may not match the target persona
- **[NEEDS VERIFICATION 2026-05-10]** Pricing — still not publicly disclosed (Exa cross-check 2026-05-10). Per-call cost likely meaningfully higher than single-frontier-model API calls (each Fugu call = N worker calls + 1 Conductor call). Cost envelope blocks an honest cost-of-Option-C comparison
- **[NEEDS VERIFICATION 2026-05-10]** Beta SLA + GA timeline — still undisclosed (Exa cross-check 2026-05-10). Closed beta status implies non-production-grade SLA. Cemini's market-hours strategies need uptime commitments that beta APIs typically don't guarantee
- **[NEEDS VERIFICATION 2026-05-10]** Worker pool composition — Fugu's commercial pool still not disclosed (Exa cross-check 2026-05-10). Academic papers confirm 7-model pool: Conductor used Gemma3-27B + Qwen3-32B + R1-Distill-Qwen-32B + Claude Sonnet 4 + Gemini 2.5 Pro + GPT-5; Trinity v2 adds Qwen-3-32B (reasoning). Fugu's commercial pool likely includes newer models (benchmark table compares against Gemini 3.1 / GPT 5.4 / Opus 4.6) but composition unconfirmed. Nahornyi analysis (2026-04-25) notes o4-mini involvement in some results.
- **[NEEDS VERIFICATION 2026-05-10]** Data-egress + retention policy — still not publicly documented (Exa cross-check 2026-05-10). Terms-of-service detail not available from the launch page. For a regulated-data path this is load-bearing

## Snippets

### S1 — Productization framing (Sakana announcement, 2026-04-24)

> "Sakana Fugu models are based on our ICLR 2026 papers (Trinity and Conductor), and we have substantially further improved the methods to increase the performance and user experience, to be offered as a commercial product."

*— `sakana.ai/fugu-beta/`, retrieved 2026-04-27. Direct linkage of Fugu-as-product to the two ICLR 2026 papers (Conductor in this corpus, Trinity not yet ingested).*

### S2 — Two-tier API + OpenAI-compatibility (Sakana announcement)

> "Sakana Fugu is accessible via APIs, with compatibility for standard OpenAI-format endpoints. If you are already using GPT, Gemini, or Claude via API, Sakana Fugu can be integrated into existing workflows with minimal changes. Behind that familiar interface, Sakana Fugu handles coordination across the model pool automatically — establishing the collaboration topology, assigning the roles and dispatching the subtasks to complete complex tasks."
>
> "Two variants are available: Sakana Fugu Mini 🐟, optimized with latency in mind, and Sakana Fugu Ultra 🐡, the full orchestration system, optimized for performance for demanding tasks."

*— `sakana.ai/fugu-beta/`. The OpenAI-compatible endpoint shape is the integration-friction-killer; the two-tier lineup acknowledges the latency cost of full pool orchestration.*

### S3 — Benchmark table (Sakana announcement)

> | Task | Gemini 3.1 (high) | GPT 5.4 (high) | Opus 4.6 (max) | fugu-mini 🐟 | fugu-ultra 🐡 |
> | --- | --- | --- | --- | --- | --- |
> | GPQAD | 94.4 | 90.9 | 92.7 | 92.4 | 95.1 |
> | LCBv6 | 90.3 | 92.1 | 92.4 | 90.4 | 93.2 |
> | SWEPro | 48.4 | 51.2 | 53.4* | 51.3 | 54.2 |
>
> *Self-reported score with custom Anthropic scaffold. SWEPro evaluated with the mini-swe-agent scaffold.*

*— `sakana.ai/fugu-beta/`. Sakana-reported beta numbers; independent reproduction not yet available. Fugu Ultra wins on every benchmark in the comparison set; Fugu Mini sits between Gemini 3.1 and GPT 5.4.*

### S4 — Recursive self-call as test-time-scaling axis (Sakana announcement, footnote 1)

> "When a Fugu model is allowed to call itself recursively, reading its own prior output as context and deciding whether to revise its coordination strategy, a new form of test-time scaling emerges. The model recognizes when its first attempt fell short and spins up a corrective workflow. The depth of recursion becomes a tunable compute axis at inference time, requiring no retraining. A small model, by reading itself, can iterate toward answers that neither it nor any of its workers could reach in a single pass."

*— `sakana.ai/fugu-beta/` footnote 1. The commercial framing of @sources/sakana-conductor-rl-orchestration.md S2 (Recursive Conductor variant). Productized as an API knob exposing a compute-vs-quality trade-off.*

### S5 — Sibling Trinity paper publication (Sakana announcement, Publications section)

> "Xu, Sun, Schwendeman, Nielsen, Cetin, Tang. TRINITY: An Evolved LLM Coordinator. ICLR 2026."
>
> "Nielsen, Cetin, Schwendeman, Sun, Xu, Tang. Learning to Orchestrate Agents in Natural Language with the Conductor. ICLR 2026."

*— `sakana.ai/fugu-beta/` Publications section. Trinity is the sibling paper; same six authors with different lead ordering. Trinity sits in the rl-marl + llm-agents clusters alongside Conductor; not yet in the Cemini corpus — open ingest decision pending user confirmation.*

### S6 — Sakana research lineage context (Sakana announcement, opening paragraphs)

> "A core conviction at Sakana AI is that the most capable AI systems will not be monolithic models scaled in isolation, but collections of specialized agents working together. This thread runs through everything we have built: evolutionary model merging, which showed that diverse open-source models can be combined to produce capabilities none possessed individually; The AI Scientist, which demonstrated that coordinated AI agents can autonomously execute the full cycle of scientific research; ShinkaEvolve, which uses evolutionary search over a pool of LLM-generated programs to discover algorithms that outperform human-written solutions; and AB-MCTS, which showed that multiple frontier models cooperating through tree search can substantially outperform any individual model on hard reasoning tasks."

*— `sakana.ai/fugu-beta/`. Sakana's broader research lineage situates Fugu within evolutionary-model-merging + multi-agent-coordination thesis. Useful for the IP-sale narrative read: an institutional buyer recognizing this lineage would treat Fugu as a credible API surface that the Cemini stack should benchmark against.*
