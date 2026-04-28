---
title: google/langextract — Source-Grounded Structured Extraction (Python, Apache-2.0)
type: source
tags: [llm-tooling, structured-extraction, source-grounding, python, google, json-schema, edgar, gdelt, cemini-adopt-candidate, ip-sale-clean]
keywords: [langextract, source-grounding, byte-mapping, structured-output, edgar, gdelt, regex-replacement, langchain-replacement, openai-compatible, deepseek-compatibility, gemini-api, ollama]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/deepseek-api.md
  - entities/infrastructure/ollama.md
  - entities/frameworks/fastapi.md
  - entities/frameworks/pydantic-v2.md
maturity: validated
created: 2026-04-28
updated: 2026-04-28
clusters: [llm-agents, ingest-tooling]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — parent canonical Gemini DR source; this URL is the second of two Adopt-for-Cemini recommendations (other is `sources/vibe-trading-hkuds.md`)
- @concepts/wiki-tooling-evaluation.md — Wave 2 evaluation parent; langextract is the highest-impact Cemini-stack ingestion-layer adoption
- @concepts/ip-sale-readiness.md — Apache-2.0 license clears IP-sale checks; verified via Exa `crawling_exa` 2026-04-28 (36073 ★, 2464 forks)
- @entities/infrastructure/deepseek-api.md — Cemini's current LLM brain; langextract supports OpenAI-compatible APIs natively, so DeepSeek slots in via `OPENAI_BASE_URL` swap. Strict-schema JSON enforcement compatibility [NEEDS VERIFICATION]
- @entities/infrastructure/ollama.md — langextract supports local Ollama models as a backend; relevant if Cemini ever pivots to local inference (no current plans, per `polygon_not_authorized_doctrine` memory the API path is intended)
- @entities/frameworks/fastapi.md — Cemini's existing backend; langextract slots into the ingest layer alongside (not replacing) FastAPI routes
- @entities/frameworks/pydantic-v2.md — langextract uses Pydantic-style schemas for output structure; integrates cleanly with Cemini's existing Pydantic v2 typing

## Raw Concept

- **URL**: https://github.com/google/langextract
- **Type**: Open-source Python library
- **License**: Apache-2.0 (Exa-verified 2026-04-28)
- **Stars / Forks (Exa-verified 2026-04-28)**: 36073 ★ / 2464 forks / 161 watchers / 110 open issues
- **Stack**: Python 99.6%, Shell 0.4%, Dockerfile (negligible)
- **Org**: google (canonical Google Research repo)
- **Created**: 2025-07-08; **Last push**: 2026-04-25; **Latest release**: v1.2.1 (2026-04-08)
- **Topics**: gemini, gemini-ai, gemini-api, gemini-flash, gemini-pro, information-extration, large-language-models, llm, nlp, python, structured-data
- **Homepage**: https://pypi.org/project/langextract/
- **Contributors**: 30 (top: aksg87, gerritcloete, kleeena, mariano, wuli666, tonebeta, the-vampiire, dependabot[bot], voidborne-d, YuqiGuo105)
- **Releases**: 14 published

## Narrative

### What it does
langextract is a Python library that systematically parses unstructured text (clinical documents, financial reports, dense academic papers) and rigorously enforces strict JSON-schema extraction using LLMs. **Defining feature**: source grounding — every extracted entity is algorithmically mapped and verified to exist verbatim at a specific byte location in the source text. The library also autonomously manages text chunking and parallel processing for monolithic documents that exceed the model context window, with no fine-tuning required.

### Why Adopt-for-Cemini

The Gemini DR evaluation cuts to the bone: replace brittle regex-based parsing logic and generic LangChain prompt-extractors currently operating in the EDGAR + GDELT ingest layers. Reasoning (Exa-verified 2026-04-28):

1. **Python-native** — drops directly into Cemini's FastAPI backend via `pip install langextract`. No language porting.
2. **Heavy compute offloaded to API** — the LLM call goes to DeepSeek (or Gemini, OpenAI, Ollama); langextract's local job is chunking + byte-mapping orchestration. Negligible local RAM footprint.
3. **Source grounding eliminates hallucinations** — for macro-financial data ingested from SEC EDGAR filings or GDELT news events, every extracted entity must be byte-mapped to source. This is the strongest-known defence against LLM hallucination on data fields where wrong numbers create immediate alpha decay or trade-off-reality risk.
4. **Apache-2.0** — clears IP-sale-readiness with the most permissive of the major OSI licenses. No copyleft concern.
5. **Active development by Google** — 36k ★, 30 contributors, 14 releases. Project velocity is institutional-grade.

### Required verification before ship

**[NEEDS VERIFICATION] — DeepSeek + langextract structured-output compatibility**

The library officially lists Gemini, OpenAI, and Ollama as integrations. DeepSeek's chat-completions API is OpenAI-compatible, so the integration *should* work via `OPENAI_BASE_URL=https://api.deepseek.com`. However, the Gemini DR evaluation flagged a specific failure mode:

> "While the tool officially lists Gemini, OpenAI, and Ollama integration support, utilizing the DeepSeek Chat Completions API introduces minor parsing risks. The systems engineer must ensure that the DeepSeek endpoint correctly accepts and honors the specific strict-schema JSON enforcement parameters (such as structured output enforcement) utilized by the LangExtract prompt templates to prevent systemic parsing failures."

**Pre-ship test protocol**:
1. Pick one EDGAR filing (a known-good 10-K excerpt) with a known schema (e.g., `{revenue, operating_income, fiscal_year}`).
2. Run langextract via `OPENAI_BASE_URL=https://api.deepseek.com` + `model=deepseek-chat`.
3. Verify (a) the library does not throw on response-format-not-supported errors, (b) the extracted JSON matches schema, (c) source-grounding byte ranges are valid against the source.
4. If steps (a)-(c) pass: Adopt for Cemini. If any fail: file a separate brief for either DeepSeek-side schema-enforcement upgrade or a Gemini Pro fallback path.

**Block deploy** until the verification protocol passes.

### Integration vector

```
EDGAR filings + GDELT news events
        ⬇ ingested as raw text
Cemini ingest layer (FastAPI route)
        ⬇ pip-imported langextract
LangExtract: chunk → schema-enforce → byte-map → parallelise
        ⬇ via OpenAI-compatible API
DeepSeek API (or Gemini Pro fallback if strict-schema fails on DeepSeek)
        ⬇ returns
{ structured JSON, byte-grounded source spans }
        ⬇ persists
PostgreSQL (existing Cemini tables: edgar_filings, gdelt_events)
```

### Cemini-specific replacement targets

Per the Gemini evaluation's "concrete integration vector":

1. **EDGAR ingest layer** — currently uses regex + custom LangChain prompts. Replace with langextract's source-grounded structured extraction. Schema definitions live in Pydantic v2 models that already exist in Cemini.
2. **GDELT news event normaliser** — currently uses regex + heuristics for event-type extraction. Replace with langextract calling DeepSeek with the GoldsteinScale + event-actor schemas. Source-grounding is critical here because GDELT events drive macro-regime classification — a wrong actor or event type cascades into wrong macro-state.

### Workflow-fit (laptop curation)

Beyond Cemini's production stack, the Gemini evaluation also rates langextract Adopt for the laptop workflow: process dense research PDFs at curation time, extract structured YAML frontmatter for Obsidian, ground the extraction back to PDF page numbers. Pairs naturally with `kepano/obsidian-skills` (this wave's other Workflow Adopt) and the existing PDF-ingest workflow.

### Risks & limitations

1. **Source-grounding is only as good as the chunker** — if langextract's text-chunking misaligns with paragraph boundaries (e.g., a SEC table split across chunks), the byte-mapping is correct but the *meaning* is fragmented. Test against monolithic SEC 10-Ks before declaring victory.
2. **No SBOM-level dependency audit yet** — Apache-2.0 at the top level is verified, but langextract's transitive Python dependencies must be SBOM'd before production deploy. Standard `pip-licenses` sweep.
3. **DeepSeek strict-schema compatibility** — gating verification described above. Don't ship until it passes.
4. **Cost discipline** — every EDGAR filing + GDELT event becomes a DeepSeek API call. At Cemini's ingest volume, budget the additional API spend in advance. Worth testing GoldsteinScale-only extraction first to bound monthly cost.

## Snippets

> "Adopt for Cemini. Replace the legacy, brittle Regex-based parsing logic or generic LangChain prompt extractors currently operating in the EDGAR and GDELT ingest layers with LangExtract. The deterministic source grounding feature eliminates dangerous LLM hallucinations when parsing critical macro-financial data, directly generating actionable alpha." [Source: Gemini DR report, URL 18]

> "A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization." [Source: GitHub repo description, retrieved via Exa crawling_exa 2026-04-28]

> "While the tool officially lists Gemini, OpenAI, and Ollama integration support, utilizing the DeepSeek Chat Completions API introduces minor parsing risks. The systems engineer must ensure that the DeepSeek endpoint correctly accepts and honors the specific strict-schema JSON enforcement parameters (such as structured output enforcement) utilized by the LangExtract prompt templates to prevent systemic parsing failures." [Source: Gemini DR report, URL 18 — Risks & caveats]
