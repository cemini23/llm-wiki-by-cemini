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
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 14)
- `@concepts/declarative-data-labeling-skills.md` — pattern Adala exemplifies
- `@concepts/cemini-license-posture.md` — Apache-2.0, acquirer-friendly
- `@concepts/deepseek-models.md` — Adala's OpenAI-compat layer routes to DeepSeek

## Raw Concept

Adala is an autonomous agent framework purpose-built for data processing and labeling at scale. Ingests Pandas dataframes, dispatches rows to LLMs (OpenRouter or native APIs) for programmatic labeling, then iteratively refines skills against ground-truth datasets.

- **Repo**: `github.com/HumanSignal/Adala`
- **License**: Apache-2.0 [NEEDS VERIFICATION 2026-05-10]
- **Stack**: Python, hard-requires Pandas
- **Last release**: v0.0.4, 2023-11-30 [NEEDS VERIFICATION 2026-05-10 — 2.5-year gap]
- **Key feature**: iterative refinement loop comparing agent outputs against ground-truth
- **Integration**: OpenAI-compatibility layer (route to DeepSeek with custom base URL)

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

### Risks

- **Abandonment risk**: last release v0.0.4 in Nov 2023 → ~2.5 years without formal release. Upstream bug fixes + newer-Python compat may not materialize. **Mitigation**: fork to Cemini-internal branch, accept maintenance burden.
- **Pandas hard-requirement**: Cemini uses Polars for quantitative analysis. Adala forces Pandas serialization/copy overhead at the boundary. **Mitigation**: chunked Pandas→Polars cast acceptable for batch ingest (not hot trading path).
- **DeepSeek base-URL override [NEEDS VERIFICATION 2026-05-10]**: confirm `OpenAIChatRuntime` cleanly intercepts base URL vs hardcoding `api.openai.com`. Critical integration prerequisite.
- **Apache-2.0**: assertion from brief; verify before commit.

### Cemini significance

Adala is the only K36 batch entry that addresses the ingest-side labeling architecture problem directly. Currently Cemini does this with hand-rolled Python loops; Adala provides reflection loops + skill registries out of the box. **Phase-0 audit blocking**: the 2.5-year release gap is the dominant risk signal — Cemini may inherit maintenance ownership of any deployed code.

### Phase-0 audit checklist

- [ ] Clone to `/tmp/adala-audit/`; verify LICENSE = Apache-2.0
- [ ] Confirm commit recency (>v0.0.4 commits despite no release?)
- [ ] Verify `OpenAIChatRuntime.base_url` is overridable (DeepSeek routing prerequisite)
- [ ] Test Python 3.11+/3.12 compatibility (release gap risk)
- [ ] Estimate Pandas→Polars boundary overhead on 10k-row batch
- [ ] Decide: fork to internal branch vs accept upstream-stale risk

[Source: Evaluating Code for Trading Stacks.docx, URL 14]
