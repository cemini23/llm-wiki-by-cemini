---
title: "Data Formulator — Microsoft Research AI Visualization Tool (Defer / Reference)"
type: entity
tags: [tool, defer, reference-only, visualization, vega-lite, duckdb, microsoft-research, mit-license]
keywords: [Data Formulator, AI visualization, blended interface, Vega-Lite, LiteLLM, DuckDB, concept encoding shelf, Microsoft Research]
related:
  - concepts/k263-eval-github-wave.md
  - concepts/k263-gambling-pm-wave.md
  - sources/eval-multi-wiki-stack-2026-09-17.md
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-09-17
phase_0_verdict: GO REFERENCE
harness_verb: FILE
wire_status: wont_wire
wire_note: K263 REFERENCE clone. DFS FILE. 0 Integrate GO.
---

## Relations
- @concepts/k263-eval-github-wave.md
- @concepts/k263-gambling-pm-wave.md
- @sources/eval-multi-wiki-stack-2026-09-17.md — K263 MIT `[CONFIRMED]` gh api 2026-09-17; GO REFERENCE ~36MB DFS FILE
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 17)

## Raw Concept

AI-powered data visualization application from Microsoft Research. "Blended interface" combines drag-and-drop column encoding with natural-language prompts. Backend AI (LiteLLM-orchestrated) generates strict Vega-Lite scripts. DuckDB handles local data manipulation to avoid network delays.

- **Repo**: `github.com/microsoft/data-formulator`
- **License**: MIT `[CONFIRMED]` gh api 2026-09-17
- **Status**: research prototype, v0.7-alpha
- **Install**: `uv run data_formulator`
- **Stack**: Python 3.11+ backend, React/Vite frontend, DuckDB local engine, LiteLLM orchestration
- **Sandbox**: Docker isolation via `--sandbox docker` flag (recommended over Python audit hooks)

## Narrative

K263: **GO REFERENCE** FILE for CeminiDFS. Local `.local/adopts/data-formulator`. **0 Integrate GO.** No scrape.

**Recommendation: Defer / Reference-only.** Useful for laptop-side visualization but Alpha-tagged software with breaking-change risk on upgrades. Keep installed for occasional use; don't make it load-bearing.

### Three-surface fit

- **Workflow (✅)**: install locally on macOS. Drive Polars output → DuckDB → Vega-Lite chart pipeline during macroeconomic CSV analysis (e.g., FRED data). Embed generated charts in Obsidian Markdown before briefs ship to prod.
- **Cemini prod (❌)**: GUI React frontend offers zero programmatic utility to headless trading engine. Vega-Lite generation is irrelevant in API-only execution path.
- **Wiki server (❌)**: React/Vite + Python/DuckDB on 4 GB CPX21 alongside Ollama → guaranteed OOM kernel panics.

### Risks / caveats

- **v0.7-alpha designation**: API signatures, routing, storage schemas may break across versions. Export charts as static assets — don't rely on Data Formulator as permanent archive.
- **Sandbox enforcement**: without `--sandbox docker`, security model relies on Python audit hooks → weaker than containerized isolation.
- **Polars Arrow-IPC compatibility [NEEDS VERIFICATION 2026-09-17]**: confirm whether DuckDB layer ingests Apache Arrow IPC streams directly (bypassing CSV encode/decode overhead). If yes, high-performance Polars→viz pipeline becomes feasible.
- **License verification**: confirm MIT before extensive use.

[Source: Evaluating Code for Trading Stacks.docx, URL 17]
