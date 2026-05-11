---
title: Ollama
type: entity
tags: [infrastructure, llm-inference, local-models, retracted]
keywords: []
related:
  - sources/3-18-crypto-integration-technical-audit.md
  - sources/3-19-langgraph-scatter-gather-financial-analysis.md
  - entities/infrastructure/deepseek-r1-14b.md
  - entities/infrastructure/deepseek-api.md
  - entities/infrastructure/localai.md
  - concepts/librarian-server-architecture.md
  - sources/langextract-google.md
  - entities/tools/swarmvault.md
maturity: retracted
created: 2026-04-23
updated: 2026-05-11
---

## Relations

- @sources/3-18-crypto-integration-technical-audit.md — source PDF proposing Ollama as reference architecture (NOT deployed state)
- @sources/3-19-langgraph-scatter-gather-financial-analysis.md — same
- @entities/infrastructure/deepseek-r1-14b.md — companion retraction
- @entities/infrastructure/localai.md — K8 promotion 2026-04-28 — peer alternative for the same local-runtime slot. Both Ollama and LocalAI wrap llama.cpp + GGUF and expose OpenAI-compatible endpoints; either could fill the slot when hardware lands. K8 evaluates LocalAI in detail; Ollama gets only the retraction lineage on this page

## Raw Concept

`[RETRACTED 2026-04-24]` — This page previously claimed Ollama runs on the Hetzner host as Cemini's local-LLM inference runtime. **That claim is disproven.** User confirmed on 2026-04-24 that Ollama is not installed on the server, and that the reason is **hardware**: the Hetzner VPS cannot host a 14B local model, and there is no at-home inference hardware available either. Cemini's intended LLM path is the **DeepSeek cloud API** (see @entities/infrastructure/deepseek-api.md), which is LLM-runtime-agnostic from an integration standpoint (OpenAI-compatible SDK). Ollama as a local runtime remains feasible only if/when hardware lands.

**Ground truth (2026-04-24 server-Claude diagnostics):**
- `du -sh ~/.ollama 2>/dev/null` → not found (no directory)
- `echo $OLLAMA_MODELS` → empty
- `ls /usr/share/ollama /opt/ollama 2>/dev/null` → no match
- No ollama process, no ollama binary on PATH, no ollama in any `docker-compose.yml`

## Narrative

`[RETRACTED]` Do not cite this page as evidence of a deployed LLM-inference runtime on Cemini. Do not use it to justify "OpenAI-compatible REST endpoint" or "tok/s envelope" claims on downstream pages.

**What's actually true (as of 2026-04-24):**
- Ollama is a real open-source project (local-inference runtime for open-weight LLMs); the tool itself exists. The retraction is specifically about the claim it's running on Cemini's Hetzner host.
- The source PDFs that reference Ollama treat it as a design-proposal component of a CPU-only inference stack — not as an observed production artifact.

**Previous (retracted) narrative:**
> Ollama is a local-inference runtime for open-weight LLMs, used by Cemini to run DeepSeek-R1-14B on the CPU-only Hetzner host. The LangGraph scatter-gather topology invokes Ollama via its OpenAI-compatible REST endpoint. Documented performance envelope: DeepSeek-R1-14B produces ~8–12 tok/s on CPU; scatter-gather calls are made in small batches with tight token budgets.

Retained above strictly as the retracted-claim-of-record.

## Snippets

*(empty — no source-text snippets support the retracted claim that Cemini runs Ollama in production.)*
