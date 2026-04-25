---
title: DeepSeek-R1-14B
type: entity
tags: [infrastructure, llm, local-model, reasoning, retracted]
keywords: []
related:
  - sources/3-18-crypto-integration-technical-audit.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - sources/3-19-telegram-discord-research.md
  - entities/infrastructure/ollama.md
  - entities/infrastructure/deepseek-api.md
  - entities/frameworks/langgraph.md
  - concepts/scatter-gather-topology.md
maturity: retracted
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-18-crypto-integration-technical-audit.md — source PDF proposing DeepSeek-R1-14B as reference architecture (NOT deployed state)
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md — same
- @sources/3-19-telegram-discord-research.md — same
- @entities/infrastructure/ollama.md — also retracted on 2026-04-24
- @entities/infrastructure/deepseek-api.md — **the operative LLM path**; cloud API (key in `.env`) replaces the retracted local-weights design
- @entities/frameworks/langgraph.md — LangGraph is real; DeepSeek-on-LangGraph claim is retracted (API equivalent captured on deepseek-api.md)
- @concepts/scatter-gather-topology.md — topology is real; DeepSeek-as-LOCAL-LLM-inside-it is retracted (API invocation remains valid, pending wiring)

## Raw Concept

`[RETRACTED 2026-04-24]` — This page previously claimed DeepSeek-R1-14B is Cemini's primary local LLM, deployed on the Hetzner host via Ollama. **That claim is disproven.** User confirmed on 2026-04-24 that neither DeepSeek-R1-14B weights nor Ollama is installed on the Hetzner server. The reason (also user-confirmed, same date): **the server does not have the hardware to host a local 14B model, and the user has no at-home inference hardware either.** The wiki lives on this laptop precisely because the server cannot carry the full knowledge-and-LLM loop locally.

**The model family is NOT retracted — only the local-weights deployment is.** Cemini's intended LLM brain uses the **DeepSeek cloud API** (key in `/opt/cemini/.env`). See @entities/infrastructure/deepseek-api.md for the operative design. This page stays as the retraction-of-record for anyone who rediscovers the corpus's reference architecture and wonders why it isn't shipped.

The source PDFs (3-18 crypto-integration audit, 3-19 LangGraph scatter-gather research, 3-19 Telegram/Discord research) propose DeepSeek-R1-14B + Ollama as a **reference architecture** that assumes local hardware the user doesn't yet have. The wiki synthesis incorrectly crossed the line from "the research proposes X" to "Cemini runs X in production." If/when local-inference hardware lands, this page can be re-examined with user re-authorization and fresh server-side evidence.

**Ground truth (2026-04-24 server-Claude diagnostics):**
- `du -sh ~/.ollama 2>/dev/null` → not found
- `echo $OLLAMA_MODELS` → empty
- `ls /usr/share/ollama /opt/ollama 2>/dev/null` → no match
- `cemini_mcp` container requirements.txt contains no ollama, torch, transformers, or LLM-inference deps

## Narrative

`[RETRACTED]` Do not cite this page as evidence of a deployed local LLM on Cemini. Do not use it to justify LLM-dependent architecture claims on downstream pages.

**What's actually true (as of 2026-04-24):**
- The operative LLM path is the **DeepSeek cloud API** — see @entities/infrastructure/deepseek-api.md. The model-family continuity is intentional; the runtime is not local.
- Cemini's deployed LLM inference layer (local or API-client) has not been verified from this workspace yet. The burden of evidence sits with the 2026-04-24 post-capacity-alarm follow-up brief (Workstream B).
- The source PDFs remain legitimate research references for a future deployment — the architecture they describe is internally coherent; it's just gated on hardware the user doesn't yet have.
- If and when local-inference hardware lands, this page can be promoted from `retracted` → `validated` with a new `updated:` date, explicit user re-authorization, and fresh server-side evidence.

**Previous (retracted) narrative:**
> DeepSeek-R1-14B is the 14-billion-parameter reasoning model that serves as Cemini's primary local LLM. Chosen for the balance of reasoning quality and CPU-tractable inference latency on a single 128GB-RAM Hetzner host. Used across the stack for: scatter-gather financial analysis, Telegram/Discord classification, compliance-report drafting. Weights vendored locally for IP-sale reproducibility.

Retained above strictly as the retracted-claim-of-record.

## Snippets

*(empty — no source-text snippets support the retracted claim that Cemini runs DeepSeek-R1-14B in production. The source PDFs do propose this architecture; see the source pages themselves for faithful summaries.)*
