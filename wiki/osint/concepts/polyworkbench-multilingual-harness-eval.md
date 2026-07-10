---
title: PolyWorkBench — multilingual long-horizon harness eval (K155)
type: concept
tags: [concept, agent-harness, benchmark, eval, ccc, k155, reference-only]
keywords: [PolyWorkBench, multilingual, long-horizon, hybrid eval, structural, executable, LLM semantic]
related:
  - sources/arxiv-polyworkbench-2607.06008-2026-07-10.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/reviewer-agent-inference-time-feedback.md
  - sources/arxiv-reasoning-effort-agentic-code-2607.02436-2026-07-09.md
maturity: draft
created: 2026-07-10
updated: 2026-07-10
---

## Relations

- @sources/arxiv-polyworkbench-2607.06008-2026-07-10.md — PolyWorkBench benchmark (arXiv:2607.06008)
- @ccc-wiki/concepts/agent-rubrics-self-correction.md — federation harness rubric integration point

## Raw Concept

What prompted this page: K155 arXiv **2607.06008** — 67 multilingual long-horizon workplace tasks; SOTA agents degrade vs monolingual baselines because language variation compounds across reasoning and execution steps. **Wiki-only** reference for federation harness eval design.

## Narrative

### Hybrid eval pattern

PolyWorkBench grades trajectories with three complementary layers:

| Layer | What it checks | Failure mode caught |
|-------|----------------|---------------------|
| **Structural** | Schema, file layout, required fields | Format drift, missing artifacts |
| **Executable** | Scripts run, APIs respond, outputs match fixtures | Silent execution errors |
| **LLM semantic** | Intent alignment when structure/execution pass | Correct-looking but wrong deliverable |

Federation harness rubrics should compose all three — not rely on a single LLM-as-judge pass.

### Multilingual compounding

Heterogeneous multilingual inputs in one workflow (commerce, legal, localization, manufacturing) introduce **compounding errors** across turns: a mistranslation in step 2 corrupts tool args in step 5. Monolingual eval suites understate this degradation. When designing CCC regression scenarios, include at least one multi-locale trajectory if the harness touches user-facing copy, legal text, or localized file paths.

### Cemini mapping

| Consumer | Steal |
|----------|-------|
| **CCC harness** | Hybrid structural + executable + semantic rubric rows per scenario |
| **Reviewer corpus** | Not injected — eval reference only |
| **Prod trading** | No direct mapping |

**Verdict:** **REFERENCE** — inform federation eval design; no new benchmark install.

## Snippets

> "Multilinguality introduces compounding effects across reasoning and execution steps." [Source: arXiv:2607.06008 abstract — paraphrase]
