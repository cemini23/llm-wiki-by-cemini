---
title: Architecting Scatter-Gather Multi-Agent Workflows for Algorithmic Trading Intelligence
type: source
tags: [docx, rl-marl, llm-agents, market-microstructure, quant-finance, crypto, cemini-internal]
clusters: [rl-marl, llm-agents, market-microstructure, quant-finance, crypto, cemini-internal]
related:
  - entities/platforms/hyperliquid.md
  - entities/platforms/oanda.md
  - entities/data-sources/gdelt.md
  - entities/data-sources/fred.md
  - entities/infrastructure/ollama.md
  - entities/infrastructure/deepseek-r1-14b.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/fastapi.md
  - entities/frameworks/fastmcp.md
  - entities/frameworks/pydantic-v2.md
  - concepts/ip-sale-readiness.md
  - concepts/scatter-gather-topology.md
maturity: validated
read_status: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @entities/platforms/hyperliquid.md
- @entities/platforms/oanda.md
- @entities/data-sources/gdelt.md
- @entities/data-sources/fred.md
- @entities/infrastructure/ollama.md
- @entities/infrastructure/deepseek-r1-14b.md
- @entities/frameworks/langgraph.md
- @entities/frameworks/fastapi.md
- @entities/frameworks/fastmcp.md
- @entities/frameworks/pydantic-v2.md
- @concepts/ip-sale-readiness.md
- @concepts/scatter-gather-topology.md

## Raw Concept

- **Original title**: Architecting Scatter-Gather Multi-Agent Workflows for Algorithmic Trading Intelligence
- **Author(s)**: AI-generated research report (Cemini-internal architectural blueprint; no individual human author attributed)
- **Type**: DOCX
- **Location**: research for cemini/3_19 LangGraph Scatter-Gather Financial Analysis.docx
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 137 non-empty paragraphs (~35,400 chars), 7 sections + Works cited
- **Read status**: validated (deep-read 2026-04-26)
- **Primary cluster**: rl-marl
- **All clusters**: rl-marl, llm-agents, market-microstructure, quant-finance, crypto, cemini-internal

## Narrative

> **Framing note**: This is a *prescriptive architectural blueprint* for a Send-API/Pregel-BSP scatter-gather topology over LangGraph + local Ollama, **not** a description of what is currently deployed in `agents/orchestrator.py`. The doc uses imperative language throughout ("the architecture *must* elegantly decouple…", "the platform *must* completely decouple…", "Timeouts *must* be explicitly handled…") and proposes the topology as the path to IP-sale-grade modularity for a future acquirer's GPU cluster. The 2026-04-24 Track C audit correctly retracted the wiki's earlier present-tense "Cemini *uses* scatter-gather" framing — actual `main` ships a linear 4-node `StateGraph` with no `Send()` import. `@concepts/scatter-gather-topology.md` carries a `[RESOLVED 2026-04-26]` header making the prescribed-vs-deployed distinction explicit. **Note also**: the source itself name-drops *pymerkle* and *OpenTimestamps* as "the implemented…stack" (para 85), which is the same prescription-as-as-built collapse J caught from the source side — those libraries are not installed in `cemini_mcp` either; what's deployed is the custom SHA-256 chain.

### Abstract
Prescriptive architectural blueprint for migrating Cemini's monolithic prompt pipeline to a LangGraph Send-API scatter-gather (dynamic map-reduce / fan-out-fan-in) topology within a Hetzner-VPS / 128GB-RAM / zero-GPU / 26-Docker-container hardware envelope. Recommends Pregel BSP execution model with super-step synchronization barriers, `typing.Annotated[List, operator.add]` reducer functions to prevent `InvalidUpdateError` race conditions, per-node `asyncio.wait_for` timeouts (rejects global `step_timeout` as destructive anti-pattern), and — most importantly — fully decouples LangGraph orchestration parallelism from Ollama hardware inference parallelism (parallel CPU LLM inference is shown to catastrophically degrade tokens/sec via KV-cache thrash; the prescription queues inference at the Ollama layer while parallelizing only at the graph layer). Models the IP-sale narrative around model-agnosticism (institutional acquirer can swap Ollama for H100 cluster without rewriting trading logic), zero-trust cryptographic traceability (the source itself names *pymerkle* + *OpenTimestamps* as the audit-trail stack — see Framing note above; neither is actually installed), and partial-intelligence fault-tolerance. None of this topology exists in the deployed `cemini_mcp` codebase as of 2026-04-26.

### Key findings
- Send API spawns isolated concurrent subgraphs with scoped payloads, avoiding prompt pollution
- Pregel BSP model: plan super-step → execute concurrent actors → sync barrier → next super-step
- Parallel state writes without reducers trigger InvalidUpdateError / INVALID_CONCURRENT_GRAPH_UPDATE — must declare typing.Annotated[List, operator.add] for mergeable state keys
- Subgraphs must return partial state (only their owned keys), never full state
- Naive parallel CPU inference with DeepSeek-R1-14B catastrophically degrades tokens/sec due to KV cache thrash — queue inference at Ollama layer, parallelize only at graph layer
- Global step_timeout is destructive anti-pattern — use asyncio.wait_for per-node
- Architecture is portable to GPU cluster post-acquisition (high IP-sale value signal)

### Entities referenced
LangGraph, Send API, Pregel, Ollama, DeepSeek-R1-14B, FastMCP, FastAPI, Pydantic v2, OANDA, Hyperliquid, FRED, GDELT

### Concepts covered
scatter-gather topology, fan-out / fan-in, Bulk Synchronous Parallel (BSP), super-step, synchronization barrier, reducer function, partial state update, context firewall (prompt isolation), KV cache, memory bandwidth bound inference, deterministic execution

## Snippets

> **Para 3 — IP-sale framing + Hetzner constraints (the document's thesis statement)**
>
> "Deploying this multi-agent topology within a strictly constrained, bootstrapped hardware environment—specifically a single Hetzner Virtual Private Server (VPS) with a 128GB RAM ceiling, zero GPU acceleration, and twenty-six co-located Docker containers—presents profound orchestration challenges. The architecture must elegantly decouple asynchronous control flow from heavily memory-bandwidth-bound language model inference. […] Furthermore, the ultimate objective of an intellectual property (IP) acquisition by an institutional trading firm dictates that the architecture must prioritize deterministic execution, zero-trust cryptographic auditability, and frictionless portability to distributed, accelerated compute clusters."
>
> *Note the imperative voice — "must elegantly decouple", "must prioritize" — confirming this is prescriptive, not descriptive of the current `agents/orchestrator.py`.*

> **Paras 27–28 — KV cache memory bandwidth bottleneck + logarithmic degradation under parallel CPU inference**
>
> "Central Processing Unit (CPU) inference for Large Language Models is fundamentally bounded by memory bandwidth rather than raw compute cycles. When an inference engine is configured to process multiple generative requests concurrently, the engine must allocate and maintain separate Key-Value (KV) caches for each active context window in the system RAM. A 14-billion parameter model with a base footprint of 9GB might require an additional 1GB to 2GB per parallel request depending on context length, rapidly consuming the available 128GB RAM ceiling alongside the 26 operational Docker containers."
>
> "More critically, parallel CPU processing forces the processor to constantly context-switch, fetching different neural network weights and KV caches from the RAM across the memory bus. This behavior thrashes the CPU cache and decimates the tokens-per-second generation rate. An architecture generating 15 tokens per second sequentially may experience a logarithmic degradation, dropping to 1 or 2 tokens per second per thread when running four parallel requests, vastly increasing overall latency and risking TCP/IP connection drops across the FastAPI server."
>
> *This is the empirical core of the "decouple graph parallelism from inference parallelism" prescription — and it is moot for `cemini_mcp` today, which calls the hosted DeepSeek API and has no local Ollama in the loop.*

> **Para 30 — the decoupling prescription, stated bluntly**
>
> "To optimize system throughput without abandoning the architectural benefits of the scatter-gather topology, the platform must completely decouple LangGraph's asynchronous graph orchestration from Ollama's hardware-level inference execution."

> **Para 33 — `step_timeout` as destructive anti-pattern**
>
> "Because the tasks are queued sequentially at the inference layer, the final task in the queue will inherently experience high apparent latency. Utilizing LangGraph's global step_timeout parameter is a highly destructive anti-pattern in this specific paradigm. A timeout at the Pregel super-step level will abruptly terminate all concurrent branches, raise an exception, and cause the total loss of all successfully computed intelligence within that execution cycle."

> **Para 84 — model agnosticism for IP-sale buyers**
>
> "First, the architecture enforces absolute model agnosticism and modularity. Institutional buyers possess proprietary, highly tuned foundation models running on massive GPU clusters. Because LangGraph orchestrates the control flow completely independently of the underlying LLM, buyers can seamlessly swap the local CPU-bound Ollama endpoints for their clustered H100 arrays without rewriting a single line of trading logic."

> **Para 85 — the source's own prescription-as-as-built collapse (KEY snippet for the J-pattern reframe)**
>
> "Second, the architecture provides zero-trust cryptographic traceability. By appending agent reasoning to an immutable list via state reducers, the synthesis node can generate a cryptographic hash—using the **implemented pymerkle and OpenTimestamps stack**—of the exact inputs, weights, and individual agent signals that informed every trade execution. This satisfies the strict regulatory and institutional audit requirements demanded by Tier-1 financial institutions."
>
> *Emphasis added. The source itself uses the word "implemented" for libraries that are not present in `cemini_mcp` (`pip list` shows neither `pymerkle` nor `opentimestamps`; what's deployed is the custom SHA-256 chain in `services/audit/chain.py`). This is exactly the prescription-as-as-built collapse the J pass caught — the source-level error that propagated into the wiki's earlier present-tense framing on `@concepts/cryptographic-audit-trail.md`. Documenting it here so future deep-reads can spot the pattern at the source layer.*
