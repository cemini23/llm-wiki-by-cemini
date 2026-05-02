---
title: 'Strategic Architecture and Agentic Integration for the Cemini Financial Suite'
type: source
tags: [docx, rl-marl, llm-agents, quant-finance, prediction-markets, cemini-internal, k17, prescribed-not-built]
keywords: [anthropic-harness, generator-evaluator, context-reset, constitutional-architecture, self-evolving-agents, openspace, tradingagents, vibecoding, adr, agent-skills, memory-budget]
related:
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
  - concepts/scatter-gather-topology.md
  - concepts/context-compression-resume-pattern.md
  - concepts/cryptographic-audit-trail.md
  - concepts/ip-sale-readiness.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/fastmcp.md
  - entities/infrastructure/timescaledb.md
  - entities/infrastructure/redis.md
  - sources/4-5-links.md
  - sources/3-17-agent-research.md
  - sources/tradingagents.md
  - sources/git-3-5-pt3.md
  - sources/crypto-7-4-11.md
  - concepts/sae-execution-contract.md
  - sources/ai-2-4-3.md
  - concepts/openclaw-security-taxonomy.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-01
clusters:
  - rl-marl
  - llm-agents
  - quant-finance
  - prediction-markets
  - cemini-internal
---

## Relations

- @concepts/quant-finance.md — Quantitative Finance corpus-index hub
- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus
- @concepts/scatter-gather-topology.md — Generator-Evaluator Loop extension: adversarial bifurcation with subjective quantification metrics (Statistical Significance, Correlation Robustness, Drawdown Probability, Execution Latency Tolerance)
- @concepts/context-compression-resume-pattern.md — Context Reset vs Context Compaction extension: structured handoff artifact → PostgreSQL → fresh Ollama session (Anthropic harness pattern), State Compactor threshold-triggered routine
- @concepts/cryptographic-audit-trail.md — Agentic decision anchoring: hash → pymerkle → OpenTimestamps per debate cycle; SHA-256 chain linking linguistic reasoning to TorchRL execution
- @concepts/ip-sale-readiness.md — Competitive benchmarking (TradingAgents / AI Hedge Fund comparison) + Constitutional Architecture as institutional buyer confidence signal
- @entities/frameworks/langgraph.md — LangGraph orchestrator referenced throughout all sections; Devil's Advocate debate protocol, agent skill definitions, state serialization
- @entities/frameworks/fastmcp.md — Agent skill prescriptions (Subjective Grading Calibrator, Sprint Contract Negotiator, State Compactor); Pydantic v2 schema enforcement against upstream API drift
- @entities/infrastructure/timescaledb.md — pgvector similarity caching for OpenSpace-inspired CAPTURED pattern + state persistence for Context Reset handoffs
- @entities/infrastructure/redis.md — Redis pub/sub bus as inter-agent blackboard for Generator-Evaluator debate protocol + decoupled execution layer
- @sources/4-5-links.md — K8 sibling; shares stale-snapshot lineage (128 GB RAM, DeepSeek-14B/Ollama local path, pymerkle/OpenTimestamps prescription-as-built collapse)
- @sources/3-17-agent-research.md — K16 sibling (2026-03-17, ~1 week earlier); both prescribe local DeepSeek-R1-14B + CPU-only architecture + 128 GB RAM baseline — K17 refines the agentic architecture in more detail
- @sources/tradingagents.md — TradingAgents multi-agent framework source page; K17 provides direct competitive benchmarking (TradingAgents vs AI Hedge Fund vs Cemini hybrid neuro-symbolic)

## Raw Concept

- **Original title**: "Strategic Architecture and Agentic Integration for the Cemini Financial Suite"
- **Author**: Cemini-internal (per voice + Cemini-stack-specific framing throughout)
- **Type**: DOCX
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/3_25 git research.docx` (3,043,750 bytes)
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Authoring date**: ~2026-03-25 (per Works cited footer dates "accessed March 25, 2026")
- **Length**: ~47KB text-extracted; 10 sections + 25 works-cited footnotes
- **Read status**: deep-read (full ingest 2026-05-01; promotion-vs-snippets-only discipline applied)
- **Inbound count at K17 ingest**: 2 (per ROADMAP; quant-finance + rl-marl-research cluster hubs)

This source records the seventh Cemini-internal document processed in the K-series. K17 has **zero promotions** (0/~10 content sections), consistent with K14 (0/11) and K16 (0/16). The document is a prescriptive strategic architecture report — it evaluates external frameworks for Cemini integration, defines agent skill requirements, and provides competitive benchmarking against open-source multi-agent trading platforms. Its primary contributions are the Anthropic Harness-derived Generator-Evaluator architecture, the Context Reset vs Context Compaction distinction, the Constitutional Architecture (ADR enforcement) governance pattern, and the hybrid neuro-symbolic architecture framing. Three existing concept pages receive extensions.

## Narrative

### Document framing

K17 is a prescriptive strategic architecture report authored ~2026-03-25 — one week after K16 (2026-03-17) and roughly one week before the Hetzner April 1, 2026 pricing adjustment. Like K16, it prescribes a local DeepSeek-R1-14B inference path on a CPU-only Hetzner VPS with a 128 GB RAM ceiling. It evaluates five research vectors (Anthropic Harness, HKUDS OpenSpace, last30days-skill, vibecoding discourse, competitive benchmarking) plus three rejected repositories (kimaki, editor.glass, iron-sensor) and defines three new FastMCP agent skills. The document is the most architecturally ambitious Cemini-internal doc in the K-series — it attempts a comprehensive resource allocation model, a detailed competitive positioning, and a governance framework (Constitutional Architecture) spanning agent behavior, CI/CD enforcement, and institutional buyer optics.

### Section register

| Section | Topic | Integration verdict | Notes |
|---|---|---|---|
| 1 | Anthropic Harness (context anxiety, Context Reset, Generator-Evaluator, Subjective Quantification) | ADOPT patterns, not library | Most directly applicable external research; maps natively to LangGraph Devil's Advocate protocol |
| 2 | HKUDS OpenSpace (FIX/DERIVED/CAPTURED self-evolving agents) | Steal-from CAPTURED + FIX patterns; reject Shared Evolution | 4.2× revenue + 46% fewer tokens in benchmarks; pgvector adaptation prescribed |
| 3 | last30days-skill (multi-signal social sentiment) | Reject direct use (Node.js); steal algorithms for Polars | 6,400 stars MIT; multi-signal quality-ranked relevance scoring reimplemented natively |
| 4 | Vibecoding + Constitutional Architecture | ADOPT ADR enforcement; reject vibecoding ethos | Architectural Decision Records as immutable constraints; CI/CD as automated enforcer |
| 5 | Inaccessible/incompatible repos (kimaki, editor.glass, iron-sensor, arc.donothinglabs) | REJECT all | TypeScript, Discord bot, inaccessible — supply-chain disqualifiers |
| 6 | TradingAgents / AI Hedge Fund competitive benchmarking | Reference for positioning | Pipeline (12-13% return) vs adaptive (149.6% return with catastrophic volatility); Cemini's hybrid neuro-symbolic as the differentiator |
| 7 | Resource allocation + memory budget | Prescribed-not-built | Detailed 86-96 GB budget model based on stale 128 GB assumption |
| 8 | Cryptographic audit trail | Reinforces @concepts/cryptographic-audit-trail.md | SHA-256 chain + pymerkle + OpenTimestamps per debate cycle |
| 9 | API maintenance burden | Agent-driven defensive engineering | Pydantic v2 schema validation → grace degradation → agent-proposed hotfix |
| 10 | Agent skill prescriptions (3 skills) | Prescribed-not-built | Subjective Grading Calibrator, Sprint Contract Negotiator, State Compactor |

### Section 1: Anthropic Harness — Context Reset + Generator-Evaluator

The most architecturally significant section. The Anthropic harness research identifies **context anxiety** — LLM degradation over extended sessions (premature task termination, state hallucination, objective drift). Two mitigation strategies are contrasted:

- **Context Compaction**: Summarize prior turns inline to reduce token count. The document rejects this for core logic — *"Compaction fails to fully alleviate context anxiety because the model remains burdened by the dense, localized history."*
- **Context Reset**: Clear the active context window entirely, injecting a structured handoff artifact (serialized state with current objectives, milestones, open tasks, key decisions, assumptions, strategic posture). A fresh session with only the artifact + current prompt.

The Reset pattern maps directly to LangGraph: instead of passing token-heavy message histories over Redis pub/sub, serialize state to PostgreSQL as structured JSON, then inject only the synthesized state representation alongside the current prompt. This minimizes context window → faster CPU inference → protects the 128 GB RAM limit.

**Generator-Evaluator Loop**: The research demonstrates autonomous agents are incapable of objective self-evaluation (reliably skew positive). The architecture bifurcates workload into a generator (executes task) and an isolated, skeptical evaluator (quality assurance, calibrated with few-shot examples, instructed to demand concrete verification). This maps to the 5-agent Devil's Advocate debate protocol: one agent serves as thesis generator, a dedicated adversarial evaluator challenges statistical assumptions, liquidity constraints, and historical backtest alignments.

**Subjective Quantification**: Abstract qualities must be converted to gradable terms. The Anthropic harness uses Design Quality, Originality, Craft, Functionality. The document translates these to financial equivalents: **Statistical Significance, Correlation Robustness, Drawdown Probability, and Execution Latency Tolerance**. The evaluator assigns quantitative scores, translating linguistic reasoning into the 28-feature Polars RL observation space.

### Section 2: HKUDS OpenSpace — Self-Evolving Agents

OpenSpace (HKUDS, MIT, ~532 stars, 75.1% Python) implements three self-evolution modes:
- **FIX**: Dynamically repair broken skills/parsing upon execution failure
- **DERIVED**: Create specialized iterations of existing parent skills
- **CAPTURED**: Extract novel, reusable code patterns from successful workflows

Benchmarks: 4.2× revenue increase + 46% fewer tokens. The shared evolution model (uploading improvements to a public community cloud) is explicitly rejected — *"broadcasting evolved trading skills to a public cloud community is a catastrophic breach of confidentiality."*

Cemini adaptation: vectorize successful LangGraph tool-call sequences into TimescaleDB/pgvector. Future queries with high cosine similarity bypass DeepSeek-R1 inference, returning the cached execution path. Auto-Fix adapted locally: Pydantic schema failure → async alert → isolated agent proposes regex/schema fix → diff presented for manual approval via GitHub Actions CI.

### Section 3: last30days-skill — Sentiment Aggregation

last30days-skill (mvanhorn, MIT, ~6,400 stars) aggregates social data across Reddit, X, YouTube, Bluesky, TikTok, Instagram, Hacker News, Polymarket, and general web — 30-day rolling window with multi-signal quality-ranked relevance scoring (engagement velocity, source authority, temporal recency decay, cross-platform convergence). Native Polymarket integration with 5-factor weighted composite.

**Rejected for direct use**: Node.js 22+ runtime requirement violates Python-only constraint. But algorithms stolen for Polars reimplementation: engagement velocity + exponential temporal recency decay calculated via Polars DataFrame aggregations, appended as discrete columns to the 28-feature RL observation space.

### Section 4: Vibecoding + Constitutional Architecture

The "vibecoding" paradigm — heavy AI-assisted code generation — produces insidious architectural degradation: agents lack long-term context, introduce fragile short-term hacks, compromise caching layers, ignore backpressure mechanisms, violate component boundaries. The "yes to all" approval problem: generative tools overwhelm the developer with noisy diffs, creating security theater.

**Constitutional Architecture**: Embed the physical laws and unalterable constraints of the trading system into immutable Architectural Decision Records (ADRs). Before any LangGraph agent or DeepSeek model is permitted to write or modify code, the initial prompt injection must force the agent to ingest, read, and trace its logic against these records. If an agent proposes a modification violating memory ceilings or CPU-only constraints, the adversarial evaluator cites the specific ADR and immediately terminates the generation. The existing CI/CD pipeline (Ruff, Trivy, Semgrep, TruffleHog) serves as the automated enforcer.

### Section 5-6: Competitive Benchmarking

TradingAgents (TauricResearch, Apache 2.0, 6.8K-24.8K stars) deploys specialized agentic roles (Fundamental, Sentiment, Technical, Risk Management) coordinated by a central orchestrator. AI Hedge Fund (~42.3K stars). The research reveals a critical dichotomy:

- **Pipeline systems**: 12-13% annualized returns, stable
- **Adaptive multi-agent systems**: 149.6% returns, but catastrophic volatility — agents misinterpret nuanced data, engage in groupthink, fail during edge-case events

Cemini's differentiator: **hybrid neuro-symbolic architecture**. The 5-agent Devil's Advocate debate generates hypotheses and analyzes edge cases, but the output is a deterministic feature input (numerical score) fed into the 28-feature Polars observation space. Actual execution is governed exclusively by TorchRL MAPPO and the Kelly/CVaR risk engine. *"This strict separation of concerns represents the exact architectural maturity required to deploy nine-figure capital allocations safely."*

### Section 7: Memory Budget Allocation

Prescribed allocation model (based on stale 128 GB assumption):

| Component | Allocation |
|---|---|
| PostgreSQL/TimescaleDB shared buffers | 32 GB |
| TorchRL/PettingZoo (state spaces, replay buffers) | 16-24 GB |
| 26 microservice containers (~1 GB each) | ~26 GB max |
| Ollama DeepSeek-R1-14B (4-5 bit GGUF) | 10-14 GB |
| **Total consumed** | **86-96 GB** |
| Buffer (OS, Redis, FastAPI, network) | ~30 GB |

CPU inference: 5-12 tok/s estimated for DeepSeek-R1-14B on CPU. Inference is permanently decoupled from the high-frequency execution loop — agents operate in medium-frequency mode (minute/hourly), updating the Redis blackboard with strategic parameters without blocking execution threads.

### Stale-snapshot analysis

K17 inherits the stale-snapshot baseline from K8 (same authoring window March-April 2026):

| Claim | Doc value | Actual (probe date) | Over/under |
|---|---|---|---|
| RAM ceiling | "128 GB" | 7 GB (K8, 2026-04-28) | ~18× over |
| Container count | "26" | 40 (K8, 2026-04-28) | 1.5× under |
| DeepSeek-R1-14B / Ollama | Prescribed inference path | Retracted — DeepSeek API is actual brain | Path-level divergence |
| pymerkle / OpenTimestamps | Prescribed as deployed | Custom SHA-256 chain only (K8 Track C) | Prescription-as-built collapse |
| CPU inference speed | 5-12 tok/s (estimated) | Not independently benchmarked | Unverified |
| "28-feature" observation space | Claimed | Not independently verified (FEATURE_VECTOR_DIM=34 per K12) | Dimensionality discrepancy (28 vs 34) |

### Cross-source corroboration

- **Context Reset vs Context Compaction**: Directly extends @concepts/context-compression-resume-pattern.md's CPR taxonomy. The Reset pattern (structured handoff → PostgreSQL → fresh session) is a more aggressive variant than the existing cpr-pattern's checkpoint-and-resume — it actively destroys context rather than serializing it for later restoration.
- **Generator-Evaluator Loop**: Extends @concepts/scatter-gather-topology.md's Devil's Advocate debate protocol with adversarial bifurcation and subjective quantification metrics. The "agents cannot self-evaluate" finding provides empirical grounding for the topology's adversarial design.
- **Constitutional Architecture**: Novel governance pattern not previously surfaced in the K-series. ADRs as immutable constraints enforced by CI/CD bridges agent autonomy and institutional safety.
- **TradingAgents benchmarking**: Direct primary-source comparison between Cemini's hybrid neuro-symbolic architecture and the two dominant open-source paradigms (pipeline vs adaptive). References @sources/tradingagents.md.
- **pgvector CAPTURED pattern**: Complements K16's Redis Semantic Caching with a database-level variant — cosine similarity on structured execution paths rather than prompt hashing.
- **128 GB RAM**: Same false propagation caught in K5/K8/K11/K13/K14/K15/K16 — now K17. The memory budget allocation table (§7) is the most detailed prescription based on this stale baseline, making it the most architecturally consequential instance of the error.

### Promotion decision: 0 of ~10 content sections (0%)

K17 promotes **zero** content items to standalone concept/entity pages. This continues the pattern established in K14 (0/11) and K16 (0/16) — Cemini-internal docs beyond K8/K12/K13/K15 surface applied-tooling evaluations, methodology prescriptions, and competitive positioning rather than novel architectural primitives.

Three existing concept pages receive extensions:
- **@concepts/scatter-gather-topology.md** — Generator-Evaluator Loop: adversarial bifurcation with financial-grade subjective quantification metrics
- **@concepts/context-compression-resume-pattern.md** — Context Reset vs Context Compaction: structured handoff → PostgreSQL → fresh session (Anthropic harness pattern); State Compactor threshold-triggered routine
- **@concepts/cryptographic-audit-trail.md** — Agentic decision anchoring per debate cycle

### Historical significance

K17 is the most architecturally ambitious Cemini-internal doc in the K-series. It attempts a comprehensive synthesis — external research evaluation, competitive positioning, resource allocation modeling, agent skill definition, and governance framework — within a single document. Its detailed memory budget table (§7) is the most concrete resource model prescribed in any K-series doc, even though it rests on the stale 128 GB baseline. The Generator-Evaluator architecture and Context Reset pattern represent the most sophisticated agentic control framework prescribed in the corpus, directly from Anthropic's published harness research. The Constitutional Architecture governance pattern is unique to K17 — no prior Cemini-internal doc prescribes immutable ADRs as agent-behavior constraints enforced by CI/CD.

## Snippets

### Anthropic Harness: Context Anxiety & Context Reset

> "The core problem identified within the literature is the degradation of model coherence over extended operational horizons, a phenomenon explicitly termed 'context anxiety.' As large language models fill their context windows, they exhibit a predictable tendency to prematurely conclude tasks, hallucinate state, or lose track of initial objectives."

> "Compaction, which involves summarizing previous conversational turns to keep the history short, fails to fully alleviate context anxiety because the model remains burdened by the dense, localized history and the implicit pressures of an ongoing, lengthy session. Conversely, a Context Reset completely clears the active context window, initializing a pristine, mathematically fresh session."

> "Instead of passing immense, token-heavy message histories between the three cooperating engines via the Redis publish/subscribe bus, the system must persist state to the PostgreSQL database as highly structured JSON objects. When the LangGraph orchestrator invokes a DeepSeek-R1-14B inference session via Ollama, it must inject only the synthesized state representation alongside the current prompt."

### Generator-Evaluator Loop

> "The research demonstrates that autonomous agents are inherently incapable of objective self-evaluation; they reliably skew positive when grading their own outputs, frequently praising mediocre work or overlooking subtle logical flaws."

> "The Anthropic harness uses specific criteria such as Design Quality, Originality, Craft, and Functionality. In the context of the Cemini Financial Suite, the FastMCP intelligence server must translate these concepts into financial equivalents: Statistical Significance, Correlation Robustness, Drawdown Probability, and Execution Latency Tolerance. The evaluator agent assigns quantitative scores to these metrics."

> "This highly deterministic, adversarial interaction dramatically increases the platform's intellectual property valuation by proving to institutional buyers that the artificial intelligence is systematically prevented from executing rogue, unchecked financial decisions based on hallucinated correlations."

### HKUDS OpenSpace: Self-Evolving Agents

> "Benchmark testing on the GDPVal economic dataset demonstrates that agents utilizing the OpenSpace framework achieved a 4.2x increase in revenue generation while consuming 46% fewer tokens. This efficiency is achieved simply by reusing battle-tested solutions and cached reasoning paths rather than forcing the large language model to reason from fundamental principles for every repetitive task."

> "The actionable integration path is not to import the OpenSpace library directly as an orchestration layer, but to surgically replicate its core 'CAPTURED' token-efficiency mechanism within the existing FastMCP intelligence server and PostgreSQL infrastructure."

> "When a LangGraph agent successfully executes a complex FastMCP tool call — for example, correlating a GDELT geopolitical event with a specific OANDA forex pair — the exact sequence of parameters, the Pydantic v2 validation schema, and the reasoning path are vectorized and stored in the database. Future queries that exhibit high cosine similarity in the pgvector index will bypass the DeepSeek-R1 inference phase entirely."

### last30days-skill: Sentiment Aggregation

> "The architectural brilliance of this repository lies in its advanced scoring and discovery mechanisms. It does not merely perform keyword searches; it utilizes a 'multi-signal quality-ranked relevance scoring' pipeline that calculates engagement velocity, source authority, temporal recency decay, and cross-platform convergence."

> "Introducing a Node.js runtime environment into the carefully orchestrated twenty-six container Docker Compose environment introduces unacceptable system bloat, violates the explicit technology stack limitation (Python, FastAPI, Redis, Postgres only), and severely complicates the continuous integration and deployment pipeline."

### Vibecoding + Constitutional Architecture

> "The primary vulnerability of heavy reliance on autonomous coding agents or rapid generative iteration is the insidious degradation of the underlying system architecture. While artificial intelligence agents operate with incredible speed, they fundamentally lack long-term architectural context. When tasked with modifying a system, they predictably introduce fragile, short-term hacks, compromise established caching layers, ignore critical backpressure mechanisms, and violate component boundaries."

> "The Cemini suite must actively reject the unstructured vibecoding ethos and implement a rigid 'Constitutional Architecture.' This methodology requires embedding the physical laws and unalterable constraints of the trading system into immutable Markdown files, commonly known as Architectural Decision Records."

> "Before the local DeepSeek-R1-14B model or any orchestrating LangGraph agent is permitted to write, modify, or suggest code within the system, the initial prompt injection must explicitly force the agent to ingest, read, and trace its logic against these records."

### Competitive Benchmarking: TradingAgents

> "Adaptive agents, which are granted high degrees of operational autonomy to negotiate and shift strategies dynamically based on incoming text data, achieve substantially higher baseline annualized returns — often cited around 149.6% compared to the 12-13% returns of rigid pipeline models. However, this adaptive flexibility introduces massive volatility, severe risk concentration, and unpredictable drawdowns."

> "The Cemini Financial Suite diverges from these open-source models in a fundamental manner that significantly enhances its institutional value and operational safety. While platforms like TradingAgents rely on generalized agentic consensus or basic linguistic guardrails for risk management, the Cemini platform structurally isolates the statistical execution layer from the linguistic reasoning layer."

> "This hybrid neuro-symbolic architecture — where deep learning and generative linguistic agents propose hypotheses and analyze edge cases, but rigorous, mathematically provable algorithms dictate the position sizing, stop-losses, and risk exposure — solves the volatility crisis observed in purely adaptive open-source frameworks."

### Resource Allocation: Memory Budget

> "Executing a 14-billion parameter model requires severe integer quantization — typically 4-bit or 5-bit quantization techniques like GGUF — to physically fit the model weights within the memory constraints. Even highly optimized, this inference process will permanently occupy approximately 10 to 14 gigabytes of the system's random-access memory during execution."

> "The LangGraph orchestrator and the FastMCP intelligence server must be structurally decoupled from the critical path of the high-frequency trading execution loop. The three cooperating engines governing equities, crypto spot via CCXT, crypto perpetuals via Hyperliquid, and forex via OANDA must operate on rapid, independent asynchronous event loops in pure Python."

> "The total memory budget must be rigidly enforced to prevent the Linux Out-Of-Memory (OOM) killer from arbitrarily terminating critical database or execution containers. This highly disciplined allocation strategy consumes roughly 86 to 96 gigabytes of the total capacity, leaving a safe 30-gigabyte buffer."

### Agent Skills: Subjective Grading Calibrator + Sprint Contract Negotiator + State Compactor

> "When evaluating complex, non-binary datasets such as GDELT geopolitical news events or the severity of Open-Meteo weather predictions impacting a Kalshi market, the evaluator agent must not provide simplistic true/false responses. It must be explicitly forced to output graded, numerical scoring vectors based on historical correlation confidence, recency decay, and source authority."

> "Before the LangGraph orchestrator initiates a data extraction run on massive repositories like SEC EDGAR or intricate data feeds like Polygon, a planner agent must construct a 'sprint contract.' This contract details the precise extraction parameters, the required date ranges, and the expected Pydantic validation schema that the output must match."

> "As the context approaches the model's degradation threshold — typically around sixty to seventy percent of the total available context window — the State Compactor automatically triggers a Context Reset. It commands the generation of the structured handoff artifact, commits it to the PostgreSQL pgvector database, and allows the debate to continue seamlessly in a fresh inference session."
