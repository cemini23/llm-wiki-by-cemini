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
maturity: validated
created: 2026-04-24
updated: 2026-04-27
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
