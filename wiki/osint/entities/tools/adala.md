---
title: "Adala — Autonomous Data-Labeling Agent Framework"
type: entity
tags: [tool, data-labeling, cemini-prod-candidate, ingest-pipeline, reflection-loop, apache-2-license]
keywords: [Adala, data labeling, autonomous agents, dataframe, reflection loop, ground-truth refinement, OpenAI-compat, sentiment scoring]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/declarative-data-labeling-skills.md
  - concepts/cemini-license-posture.md
  - concepts/deepseek-models.md
maturity: validated
created: 2026-05-10
updated: 2026-05-10
phase_0_audit: GO (2026-05-10)
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 14)
- `@concepts/declarative-data-labeling-skills.md` — pattern Adala exemplifies
- `@concepts/cemini-license-posture.md` — Apache-2.0, acquirer-friendly
- `@concepts/deepseek-models.md` — Adala's OpenAI-compat layer routes to DeepSeek

## Raw Concept

Adala is an autonomous agent framework purpose-built for data processing and labeling at scale. Ingests Pandas dataframes, dispatches rows to LLMs (OpenRouter or native APIs) for programmatic labeling, then iteratively refines skills against ground-truth datasets.

- **Repo**: `github.com/HumanSignal/Adala`
- **License**: **Apache-2.0 [CONFIRMED 2026-05-10]** — IP-sale clean
- **Stack**: Python ≥3.10, `pandas==2.2.3` hard-pin (boundary cast required vs Cemini's Polars)
- **Last release**: v0.0.4 (2023-11-30) — **BUT main-branch is active**: last commit 2026-05-08 (2 days pre-audit), 113 commits in last 6 months, 677 total. Status: unreleased-dev, **NOT abandoned**.
- **Maturity**: 1,439 stars, 167 open issues, CI green on Python 3.13, comprehensive pytest suite (15+ test files)
- **Key feature**: iterative refinement loop comparing agent outputs against ground-truth
- **DeepSeek routing**: **CONFIRMED 2026-05-10** — `LiteLLMChatRuntime` accepts `base_url` constructor param; docstring explicitly supports "OpenAI-compatible API provider besides OpenAI"

## Narrative

Adala converts the "label this row" problem into a declarative skill the LLM consumes. For Cemini's ingest layer — GDELT events, SEC 10-K text, news streams — Adala's pattern resolves the heavy lifting of mapping LLM prompts systematically across structured dataframes with built-in reflection and evaluation loops that would otherwise require hundreds of lines of boilerplate.

### Integration vectors

**Cemini prod (Adopt — ✅)**:
- Situate in Cemini "Ingest layer" container
- Stream GDELT events / SEC 10-K filings into memory as Pandas dataframes
- Apply custom skills (Bullish/Bearish sentiment, macroeconomic entity extraction)
- Route batch requests to DeepSeek via OpenAI-compat layer
- Dump labeled+validated outputs to PostgreSQL/pgvector via Polars
- Memory: <1.5 GB on 5000-row batches (safely under 7 GB envelope)

**Workflow laptop (Partial — ⚠️)**: `pip install adala` locally for rapid programmatic categorization of PDF dumps before manual Obsidian injection.

**Wiki server (Not applicable)**: ingest-side framework, not librarian-side.

### Risks (post-audit, residual)

- **Unreleased-dev status**: main-branch active, but no v0.0.5+ tag. Upstream may introduce breaking changes without SemVer signaling. **Mitigation**: pin a specific commit hash in prod deployment; quarterly check on upstream movement.
- **Pandas hard-pin (`==2.2.3`)**: not a range, exact version. **Mitigation**: chunked Pandas↔Polars cast at ingest boundary only (acceptable — Adala's own roadmap comment flags "Replace this with Dask or Polars in the future"). Microseconds overhead for typical GDELT/10-K batches.
- **DeepSeek live-key smoke test**: confirmed code path supports `base_url` override; live test still required before prod cutover.

### Cemini significance

Adala is the only K36 batch entry that directly addresses the ingest-side labeling architecture problem. Cemini's hand-rolled Python loops over DeepSeek for GDELT/SEC ingest accumulate hundreds of lines of boilerplate (batching, retry, schema validation, ground-truth comparison). Adala provides reflection loops + skill registries out of the box. With the abandonment risk debunked, **Adala is the strongest K36 prod adoption candidate**.

### Phase-0 audit findings (2026-05-10) — **GO** ✅

- [x] LICENSE = Apache-2.0 confirmed
- [x] **Abandonment-risk claim FALSE**: 677 total commits; 113 in last 6 months; last main commit 2026-05-08 (2 days pre-audit). Project is unreleased-dev since v0.0.4 (Nov 2023), NOT abandoned.
- [x] `LiteLLMChatRuntime` accepts `base_url` constructor parameter; routes cleanly to DeepSeek (`OpenAI(api_key=..., base_url=...)` line 134; `instructor.from_litellm(..., base_url=..., ...)` line 140). Docstring explicit: "If provided, will be used to talk to an OpenAI-compatible API provider besides OpenAI."
- [x] Python ≥3.10 declared; CI green on 3.13; 15+ pytest test files; codecov integration active
- [x] Pandas pin = `==2.2.3` (acceptable; Polars/Pandas coexist)
- [x] Dependencies all current: `openai >=2.0.0,<3.0.0`, `litellm >=1.83.7,<2.0.0` (patched May 2026), `pydantic >=2,<3`, `instructor >=1.14.5`
- [ ] **Adoption gate**: live smoke test with DeepSeek base URL before prod cutover

**Verdict**: GO ✅ — proceed to production adoption brief. Strongest K36 ingest-side asset.

[Source: Evaluating Code for Trading Stacks.docx, URL 14]
[Audit: Phase-0 Explore agent, 2026-05-10]
