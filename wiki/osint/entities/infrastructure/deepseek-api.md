---
title: DeepSeek Cloud API
type: entity
tags: [infrastructure, llm, cloud-api, cemini-brain, intended-architecture]
keywords: [deepseek, api, cloud-inference, openai-compatible, chat-completions]
related:
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/deepseek-r1-14b.md
  - entities/infrastructure/ollama.md
  - entities/infrastructure/sakana-fugu.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/fastmcp.md
  - concepts/scatter-gather-topology.md
  - concepts/ip-sale-readiness.md
  - sources/sakana-conductor-rl-orchestration.md
  - sources/sakana-trinity-llm-coordinator.md
  - sources/4-5-links.md
  - concepts/context-compression-resume-pattern.md
  - entities/infrastructure/localai.md
  - concepts/wiki-tooling-evaluation.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - concepts/librarian-server-architecture.md
  - concepts/ai-organisation-design.md
  - sources/omc-talent-container-paper.md
  - sources/langextract-google.md
  - sources/vibe-trading-hkuds.md
  - sources/agentic-harness-engineering.md
  - sources/incompressible-knowledge-probes-li-2026.md
  - sources/moe-efficiency-leverage-tian-2026.md
  - sources/moe-surpass-dense-equal-resource-li-2026.md
maturity: validated
created: 2026-04-24
updated: 2026-04-29
---

## Relations

- @entities/infrastructure/hetzner.md — host that will hold the API client + key
- @entities/infrastructure/deepseek-r1-14b.md — the local-weights alternative; retracted because the hardware isn't available (see @that-page)
- @entities/infrastructure/ollama.md — the local-runtime alternative; retracted for the same reason
- @entities/frameworks/langgraph.md — the orchestration framework that would call this API
- @entities/frameworks/fastmcp.md — the tool layer the model would use
- @concepts/scatter-gather-topology.md — the LangGraph topology this API would drive
- @concepts/ip-sale-readiness.md — API-based model access is a known IP-sale consideration (portability vs lock-in)
- @sources/sakana-conductor-rl-orchestration.md — user-dropped 2026-04-27 — ICLR 2026 Sakana AI Conductor paper; evaluates **DeepSeek-R1-Distill-Qwen-32B** as one of its open-source worker LLMs (Table 3, Section A.2) — same model family as the deployed DeepSeek-Reasoner brain. In the Conductor framework, the Cemini DeepSeek client at `services/llm_analyst/deepseek_client.py` would be a worker-pool entry, not a per-node analyst — the meta-controller would *decide* when to dispatch to DeepSeek vs GPT-5 vs Claude Sonnet 4 vs Gemini 2.5 Pro per scatter-gather slice. More flexible than the deployed pattern (single shared client across all 4 analyst nodes); the kind of architectural lift an institutional buyer's GPU-cluster engineer would do post-acquisition
- @entities/infrastructure/sakana-fugu.md — sibling hosted-LLM service in the Cemini-considered API pool. Where DeepSeek serves a single frontier-class model behind the OpenAI-compatible endpoint, Fugu (closed beta, launched 2026-04-24) serves a *learned orchestrator over a pool of frontier models* behind the same shape of endpoint. Both could coexist (DeepSeek as a worker-pool entry inside Fugu, Cemini's existing client repointed at Fugu); could also be redundant (Cemini routes through Fugu's pool, Fugu internally calls DeepSeek). Adds a third option to the @concepts/scatter-gather-topology.md P1 ticket (outsource orchestration to Fugu)
- @sources/sakana-trinity-llm-coordinator.md — second of the two ICLR 2026 papers underlying Sakana Fugu (ingested 2026-04-28 as Conductor sibling, arXiv 2512.04695). The Trinity poster doesn't enumerate its worker-pool composition the way Conductor's Table 3 does; the DeepSeek-family worker-pool relevance to this entity is therefore mediated *primarily* through Conductor (which explicitly evaluates DeepSeek-R1-Distill-Qwen-32B as a pool entry) and only secondarily through Trinity. Cross-link kept lightweight to capture the Sakana-research-lineage proximity without overstating the operational tie
- @sources/4-5-links.md — K8 deep-read 2026-04-28 — multi-topic Cemini-internal evaluation. The DeepSeek API is the operative LLM brain LocalAI would sit beside (or substitute, in the retracted local-runtime path); both expose OpenAI-compatible chat-completions
- @concepts/context-compression-resume-pattern.md — K8 promotion 2026-04-28 — the cpr-pattern's "compression node" would call the DeepSeek API to summarize sprawling debate trajectories into dense strings before persistence to pgvector. DeepSeek is the LLM brain Phase 1 (Compress) of the pattern targets
- @entities/infrastructure/localai.md — K8 promotion 2026-04-28 — sibling local-inference runtime that exposes the same OpenAI-compatible Chat Completions schema as this hosted API. Architectural slot: when local-inference hardware lands, swap `base_url="https://api.deepseek.com"` for `base_url="http://localai:8080"` with zero Python orchestration changes
- @concepts/wiki-tooling-evaluation.md — 2026-04-28 — wiki-tooling adoption candidates (recommended: `llm-wiki-compiler`) all support DeepSeek-API access via `OPENAI_BASE_URL` swap pattern; same architectural slot this entity page documents. Adopting llm-wiki-compiler means the workspace librarian uses the same DeepSeek API the deployed Cemini stack already targets — single API key, single rate-limit envelope across both layers
- @sources/atomicmemory-llm-wiki-compiler.md — 2026-04-28 — primary wiki-tooling adoption candidate; multi-provider config supports DeepSeek API directly via `LLMWIKI_PROVIDER=openai` + `OPENAI_BASE_URL=https://api.deepseek.com`. Workspace-side compile/query loop and deployed-stack analyst nodes share the same LLM brain
- @sources/agentmemory-rohitg00-cpr-impl.md — 2026-04-28 — Apache-2.0 cpr-pattern reference implementation; the "LLM compress" phase calls a configurable LLM, swappable to DeepSeek API. When the cpr-pattern lands in Python on the Cemini stack, the Compress phase invokes this entity's hosted DeepSeek brain
- @sources/agentic-harness-engineering.md — 2026-04-29 — arXiv 2604.25850 (Lin et al., Fudan/PKU/Shanghai Qiji Zhifeng, 28 Apr 2026) tests AHE's auto-evolved harness across 5 cross-model bases including **deepseek-v4-flash**: largest measured cross-family gain at **+10.1 pp pass@1** (51.7% → 61.8% on Terminal-Bench 2). Empirical evidence that harness-level optimization generalizes to DeepSeek-family models; reduces Cemini's brain-vendor lock-in risk. The AHE pattern (7-component decoupling + falsifiable manifest) survives a DeepSeek substitution without re-evolution
- @sources/incompressible-knowledge-probes-li-2026.md — 2026-04-29 — arXiv 2604.24827 (Bojie Li, Pine AI, 27 Apr 2026) calibrates a black-box parameter-estimator on 89 open-weight models (R²=0.917) **explicitly including `deepseek-v3`, `deepseek-v4-flash`, `deepseek-v4-flash-think`, and `deepseek-v4-pro-think` in the calibration set**. Operational implications for this entity: (a) factual recall on DeepSeek tracks log(total params), not active params — critical MoE deployment finding; (b) **Densing Law does not apply to factual capacity** — newer cheaper models will NOT compress long-tail factual recall, so Cemini's analyst-orchestrator cannot swap-down to smaller models for ticker/entity-recall tasks without proportional loss; (c) the IKP "hallucination-similarity" technique (rare-fact agreement on wrong answers) is a low-effort silent-swap detector if Cemini's vendor ever quantizes / reroutes / replaces the served model — drift signal usable as daily cron alerting

## Raw Concept

DeepSeek's hosted Chat Completions API is the **intended LLM brain** for Cemini given the current hardware constraint: the Hetzner server is CPU-only with no capacity for local 14B weights, and the user has no local-inference hardware at home yet either (per 2026-04-24 clarification). Running the local-model path described in @entities/infrastructure/deepseek-r1-14b.md is not feasible until hardware lands. In the interim, the DeepSeek *model family* is still accessible — via the vendor's cloud API, using an `OpenAI`-compatible SDK pattern.

This page documents the intended design, *not* a verified deployed state. Server-side verification of the API key's presence, any existing client code, and whether any LangGraph node currently calls the API is pending (first Workstream B of the 2026-04-24 post-capacity-alarm follow-up brief will capture it).

## Narrative

### Why API, not local

- **Hardware constraint (2026-04-24, user-confirmed)**: no local-inference hardware — not on the Hetzner VPS (CPU-only, 8 GB RAM per most recent server-Claude diagnostics; earlier "128 GB RAM" claims on @entities/infrastructure/hetzner.md are part of the same proposal-vs-production drift and will be re-verified)[NEEDS VERIFICATION 2026-04-25], not at home. Local 14B weights are infeasible for now.
- **The wiki lives on this laptop for exactly this reason.** Because the server can't host the full knowledge-and-LLM loop locally, the librarian layer (this workspace) runs here, and the dev stack on the server gets curated briefs via `scp`. The DeepSeek API fills the LLM-brain gap on the server side without requiring a local-inference runtime.

### Expected integration

1. **Auth**: API key in `/opt/cemini/.env` (name to be verified — likely `DEEPSEEK_API_KEY`). Loaded by `python-dotenv` or the existing Cemini env-loader, same pattern as Polygon / Kalshi / OANDA keys.
2. **Client**: `openai.OpenAI(base_url="https://api.deepseek.com", api_key=os.environ["DEEPSEEK_API_KEY"])` — DeepSeek's API is OpenAI-compatible, so the existing OpenAI-SDK idiom works with one base-URL override. Model names: `deepseek-chat` (general) and `deepseek-reasoner` (R1 reasoning). [NEEDS VERIFICATION — confirm model IDs against current DeepSeek API docs at time of wiring]
3. **Orchestration**: LangGraph supervisors invoke the client at each scatter-gather node; the Send-API fan-out remains unchanged from @concepts/scatter-gather-topology.md. The key difference vs the retracted local-runtime design: API calls have external latency + rate-limit exposure, so the scatter-gather budget should account for that (batch size, concurrent-call ceiling).
4. **RAG integration**: the model queries the **local pgvector wiki-search** (Track B of the 2026-04-23 wire-in brief, currently in re-deploy investigation per the 2026-04-24 post-capacity-alarm follow-up). The model stays in the cloud; the knowledge base stays local. This is the core architectural decoupling — no proprietary research leaves the workspace except as the model's own response completions.
5. **Cost + rate-limit envelope**: to be captured when server-side wiring lands. [NEEDS VERIFICATION 2026-04-25]

### Architectural implications

- **Data-egress posture**: every scatter-gather call now leaves the host and hits DeepSeek's endpoint. Prompts include research context and reasoning traces. Evaluate against:
  - The cryptographic-audit-trail design (@concepts/cryptographic-audit-trail.md) — reasoning traces are now produced by a third-party service; the pg_tamperlog anchor should capture the (prompt, completion, model_id, timestamp) tuple, not a locally-verifiable forward pass.
  - The IP-sale readiness doctrine (@concepts/ip-sale-readiness.md) — an acquirer gets a design that's portable to any OpenAI-compatible endpoint (DeepSeek today, their own Claude/GPT/Anthropic/OpenAI account tomorrow), which the research PDFs already flagged as deal-favorable. The local-weights version stays as a future option if/when hardware lands.
  - Compliance: for any regulated data path (EDGAR filings, client PII if it ever enters the stack), API egress has to be explicitly approved. Current scope is OSINT + market data, which doesn't trip this, but flag it in the supervisor-vetting ledger.
- **Replacement-cost claim adjustment**: the revised replacement-cost line-item (@concepts/replacement-cost-valuation.md) should reflect "DeepSeek API integration + prompt engineering + wiki-search RAG wiring," not "trained DeepSeek-R1 reasoning harness." Cheaper to replicate; priced accordingly.

### Status

**Partial validation — 2026-04-24 Track C walk**: the client layer is `[CONFIRMED]`; the full scatter-gather topology + RAG loop remain pending.

- **API key**: presumed present in `/opt/cemini/.env` per user statement 2026-04-24. Server-side verification pending (Workstream B of `briefs/2026-04-24_post-capacity-alarm-followup.md`). [NEEDS VERIFICATION 2026-04-25]
- **Client wiring** `[CONFIRMED 2026-04-24]` — `services/llm_analyst/deepseek_client.py` exists as a **single shared client** (per Track C walk, concept #3 scatter-gather evidence). `agents/orchestrator.py` imports and uses this client from the 4-analyst linear `StateGraph` (`technical`, `fundamental`, `sentiment`, `cio_debate` nodes). The model name and base-URL used by the client on the server-side have not been read from this workspace yet; pending visual confirmation when Workstream B returns. [NEEDS VERIFICATION — model ID, base-URL string]
- **LangGraph integration** `[TENTATIVE 2026-04-24]` — the client is wired into `agents/orchestrator.py` as a linear multi-node workflow, **not** the Send()-based scatter-gather topology described in @concepts/scatter-gather-topology.md (see that page's retraction). Correction (post-inventory): `.worktrees/step83-llm-analyst/` is **docs-only** — contains the step83 design spec + implementation plan, no Python code; orchestrator.py in step83 is identical to main. A Send()-topology prototype does **not** exist on any branch. Next wiring step depends on (a) Track B `wiki_search` being live for the RAG loop, and (b) decision on the P1-4 ticket on @concepts/scatter-gather-topology.md — which is now "build fresh per step83's design spec" (Option A, ~1–2 engineer-weeks) vs. "retract + rename" (Option B, ~0.5 days). Option B is the default recommendation unless Send() is on the IP-sale critical path.
- **RAG via `wiki_search`**: blocked on Track B deploy investigation (see `briefs/2026-04-24_post-capacity-alarm-followup.md`, Workstream B). Track B source code is currently untracked on the server; triage path pending.

## Snippets

*(populate when server-side wiring lands and actual client-config snippets + model-ID confirmations are available.)*
