---
title: Multi-Wiki Link Evaluation — 20 URLs (2026-11-10)
type: source
tags: [source, eval, tool-evaluation, revenue-lens]
keywords: [runtime v10.11, phase-0, jevals, gbrain, ontosmith, dzhng skills, browser-use]
related:
  - entities/tools/jevals.md
  - entities/tools/gbrain.md
  - entities/tools/ontosmith.md
  - "@ccc-wiki/entities/tools/dzhng-skills.md"
  - entities/tools/browser-use.md
  - "@ccc-wiki/entities/tools/worktrunk.md"
  - sources/eval-multi-wiki-link-revenue-v10-11-2026-11-05.md
maturity: draft
created: 2026-11-10
updated: 2026-11-10
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cemini Multi-Wiki Link Evaluation — Gemini Deep Research RUNTIME (v10.11) |
| Received | 2026-11-10 |
| Inbox | `research to be indexed/Multi-Wiki Link Evaluation.docx` |
| Batch | 20 URLs, none deferred |
| Lens | revenue plus project fit, same stack |

**Fifth batch labelled v10.11**, and only 51 KB — the smallest document yet for a full 20-URL run.

## Narrative

### Tier table

| # | Tool | Tier | Project fit | License (verified) |
|---|------|------|-------------|--------------------|
| 1 | google-deepmind/mujoco | Pass | none | Apache-2.0 / CC-BY-4.0 |
| 2 | anthropics/claude-quickstarts | Context | CCC | MIT |
| 3 | ZhuLinsen/daily_stock_analysis | Context | OSINT | MIT |
| 4 | garrytan/gbrain | **Extract** | atto, family-tree | **MIT** |
| 5 | max-sixty/worktrunk | **Integrate** | game-time, atto, collectibles | MIT OR Apache-2.0 |
| 6 | browser-use/browser-use v1.0.0 | **Extract** | collectibles, atto | **MIT** *(report: not found)* |
| 7 | Eliot5566/JEV-Paper-Radar | Context | OSINT | MIT |
| 8 | hft.md/grok-bots | Context | OSINT | not found |
| 9 | openlayer-ai/jevals | **Extract** | atto, collectibles, parlays | **MIT** |
| 10 | Dongbumlee/ontosmith | **Extract** | atto, family-tree | **MIT** |
| 11 | jaw.id | Pass | none | Apache-2.0 |
| 12 | pirateface.co | Context | cybersec | n/a (mirror) |
| 13 | anomalyco/opencode v2.2.6 | Context | CCC | MIT |
| 14 | dzhng/skills | **Integrate** | game-time, atto, collectibles | **MIT** |
| 15 | littledivy/tailnet-do | Watch | guruwatcher | not found |
| 16 | utillayer/youtube-agent-skill | **Extract** | basgiath, game-time | not found |
| 17 | INDXDev/jevlint | Context | CCC | MIT |
| 18 | yjid/kensaku | Watch | CCC | MIT |
| 19 | Thysrael/Horizon | **Extract** | collectibles | not found |
| 20 | sepi2p/research-explainer-skill | Pass | none | not found |

Tally: **2 Integrate**, 6 Extract, 2 Watch, 7 Context, 3 Pass.

### Phase-0, 2026-11-10 — two licence clears and one hidden blocker

| Tool | Report claim | Phase-0 finding | Effect |
|------|--------------|-----------------|--------|
| **browser-use** | "NOT FOUND" | **MIT**, stated in the README and the repo metadata. **And it runs fully local:** `Browser('chromium')` with a local model through `ChatOpenAI`, no key needed. The **default** is the paid Browser Use Cloud, which is where `BROWSER_USE_API_KEY` comes from. | Cleared, and the important distinction is default-vs-possible. The free local path exists; the documented quickstart steers you to the metered one. |
| **ontosmith** | Extract for Atto; "without Neo4j" | **MIT**, 264 stars. **Requires Neo4j 5.x Community for live builds** and fails early without it. **Needs an LLM connection** — the default preset routes through **OpenRouter to Claude Haiku and Sonnet** on one key, with no local NLP stack included. **Developed and tested on Linux only; WSL2 required on Windows.** macOS is not mentioned. | **Three blockers the report missed.** Neo4j is a new local service, the default model path is a cloud call, and this is a macOS laptop. Its flags-free claim is wrong. |
| **jevals** | Presented around hosted Jev at $0.042/M input tokens | **MIT.** It also **runs locally**: *"Runs locally with Kev or Laya."* **Laya runs in-process on Apple Silicon and is fully offline**; Kev self-hosts (`python -m kev.serve --run jaredpalmer/kev-4b` on a 32 GB Mac). **No API key for any local option.** | **The most useful correction in the batch.** The report framed this as a metered cloud service; the offline path is the one that matters here, and it makes the tool compatible with Atto's ban 4. |
| **gbrain** | "hybrid Markdown pages + atomic facts + timelines, ~86% token cut" | **MIT.** **Local by default** — Markdown in a git repo, with PGLite (WASM Postgres 17) as a *rebuildable index*, not the store. **But:** synthesis requires a configured chat model, and optional embedding/reranking providers receive text. **Keyword-only search needs no model API.** Install note: **not on npm** — an unrelated `gbrain` package can shadow it, so install via Bun from GitHub. | The local-first claim holds for storage. The synthesis path is where data would leave, and the README says so. |
| **dzhng/skills** | Integrate; write-spec, implement-spec, find-state-machines, auto-research | **MIT.** A large library — engineering, visual review, authoring, and graphics skills — installable with `npx skills add dzhng/skills`. | Integrate holds. |
| **worktrunk** | Integrate | **Fourth evaluation.** MIT OR Apache-2.0, unchanged across all four. | See @ccc-wiki/entities/tools/worktrunk.md. |

### What this batch is actually about

**Jev, three times.** `jevals`, `ontosmith` (which uses Jev as its decision model), and `JEV-Paper-Radar` all orbit the same TypeSafe decision-model primitive this workspace already has a key for. That is the first batch where a tool family recurs rather than a single tool, and the local-install correction on `jevals` is what makes the family usable here.

**Two Integrates, both about how work gets done rather than what gets built.** `worktrunk` isolates parallel agents; `dzhng/skills` slices features into reviewable passes. Neither touches Atto's data boundary, which is why they can be adopted while the interesting Extract items cannot yet.

**The three Atto extracts form a pipeline.** ontosmith proposes facts under a human-approved schema with evidence spans; jevals gates groundedness and PII in one local pass; gbrain indexes approved facts and pages for cheap recall. Read as a chain it is coherent — and each link has a blocker: Neo4j, the model path, and synthesis respectively.

## Snippets

> "It 'Runs locally with Kev or Laya.' Laya runs in-process on Apple Silicon and is fully offline." — jevals README [fetched 2026-11-10]

> The default preset routes through OpenRouter to four models, including Claude Haiku and Sonnet, with a single API key. It is "developed and tested only on Linux, with WSL2 required on Windows." — ontosmith [fetched 2026-11-10]

> "GBrain is MIT-licensed and free to self-host; gbrain.io is optional paid hosting." and "the database is an index rebuildable from it." [fetched 2026-11-10]

> The README says the library is "MIT licensed", and a local model can be used "e.g. Ollama through `ChatOpenAI(...)`". [browser-use, fetched 2026-11-10]

## Dead Ends

- **Reading browser-use as cloud-only.** The local path exists; the quickstart just points at the metered one.
- **Treating ontosmith as "without Neo4j".** Live builds require it.
- **Assuming jevals needs a paid key.** Laya is offline and keyless.
- **Installing gbrain from npm.** A different package shadows it.
