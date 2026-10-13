---
title: "DistressBench: crisis support evaluated on care delivered, not refusal (arXiv 2610.12758)"
type: source
tags: [source, k290, arxiv, evaluation-methodology, ai-safety, llm-judge]
keywords: [distressbench, scale-ai, crisis-support, refusal, rubric-weighted, recognition-action-gap, llm-judge-calibration, ssh, k290]
related:
  - concepts/k290-arxiv-wave.md
  - concepts/ai-safety.md
  - concepts/agent-harness-verification-bottleneck.md
  - concepts/k289-arxiv-wave.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
read_status: read
---

## Relations

- @concepts/k290-arxiv-wave.md
- @concepts/ai-safety.md
- @concepts/agent-harness-verification-bottleneck.md
- @concepts/k289-arxiv-wave.md

## Raw Concept

| Title | DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models |
| Authors | Drew Rein, Patrick Oathout, Vishal Kumar (work done while at Scale AI), Udari Madhushani Sehwag — Scale AI |
| Type | arXiv preprint (cs.CL), 38 pages |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.12758-distressbench-evaluating-multi-dimensional-crisi.pdf` |
| Retrieved | 2026-10-13 |
| Published | 2026-10-08 |
| arXiv | 2610.12758v1 |
| Artifacts | https://labs.scale.com/papers/distressbench (corpus, rubrics, judge calibration labels, 20-thread red-team annex; a private half is held out) |
| read-status | read |

## Narrative

A **safety benchmark that scores care delivered instead of refusal**. 718 English conversations with **clinician-authored user turns** across **23 suicide-and-self-harm (SSH) subcategories**, each with a **task-specific rubric of weighted atomic criteria across 7 dimensions** and a **clinician reference response**. A model's score is the **weighted average over the criteria its reply satisfies** — read directly as **the fraction of required care delivered**.

### Headline numbers

**25 frontier models evaluated.** Best model satisfies **88.4%** of weighted criteria; **median 71.4%**; **clinician references 98.7%** (ceiling).

| Model | Weighted score |
|-------|----------------|
| Muse Spark 1.2 | **0.884** [0.875, 0.893] |
| Muse Spark 1.3 | 0.849 |
| Muse Glimmer 30B | 0.806 |
| Qwen3.8 Max | 0.776 |
| GPT-5.6 Terra | 0.764 |
| Claude Fable 5.1 | 0.716 |
| Claude Opus 4.8 | **0.714 (median)** |
| DeepSeek v4 Flash | 0.697 |
| Mistral Large | 0.588 |
| Llama 4 Maverick | **0.412 (lowest)** |

**25 models fall into only 12 separable bands** — only 11 of 24 adjacent gaps separate. **Complete rubric satisfaction is rare:** leader 40.4%, second 18.3%, **median 2.3%**.

### The recognition–action gap (the finding worth keeping)

**Pooled across all 25 models, in 35.3% of conversations where the model satisfied every clinician-written criterion for recognizing the crisis, it failed to route the user toward human help.** Strongest model 15.9%; weakest 69.6%.

**Per-dimension, the shortfall is in the dimensions that require the model to act, not to withhold:**

| Dimension | Median | Best | Δ |
|-----------|--------|------|---|
| Safety disclaimers | 8.3% | 84.6% | +0.763 |
| De-escalation | 46.0% | 74.6% | +0.286 |
| Actionable resources | 70.3% | 86.6% | +0.163 |
| Identification | 82.5% | 93.3% | +0.107 |
| Compassion | 85.2% | 96.9% | +0.117 |
| Harmless response | 94.5% | 97.0% | — |
| Moralization | 98.2% | 99.2% | — |

**Multi-turn scores below single-turn: 0.685 vs 0.742.**

**Failure decomposition:** standard divergence accounts for **85.0%** of forfeited weight; discrimination failure only **4.1%**. Endorsement of the omission appears in justifications: resources 39.4%, identification 34.3%, de-escalation 33.6%.

**Filter misfire:** one served model returns nothing on **7.5%** of conversations — firing on **34.2% of escalation-pattern** but only **0.8% of suicide-planning** conversations. **A refusal-style benchmark would score that silence as a pass.**

**Judge panel:** `claude-opus-4-8` + `llama4-maverick` + `gemini-3.1-pro`; ranked **1st of 455** panels; **Cohen's κ 0.732**, macro-F1 0.862 (clinician Fleiss κ 0.640).

**Invariance (nulls):** under-18 0.707 vs over-18 0.710; borderline intent 0.716 vs explicit 0.707.

### Limitations (stated)
English-only and U.S.-centric resources; **simulated** not live transcripts; every task carries a disclaimers criterion (drafting-menu artefact); reply length uncontrolled; the per-turn degradation instrument failed (**Fleiss κ ≈ 0.03**).

### Why it matters here
Two transferable lessons beyond the domain:

1. **Rubric-weighted "fraction of required care" beats binary refusal scoring.** A refusal benchmark **registers filter silence as a pass** — the same blind spot as scoring an agent on what it declines instead of what it does.
2. **The recognition–action gap (35.3%) is an evaluation-methodology shape**, not an SSH fact. It is the same failure mode the K289 ToFu work found one layer down: **the model recognizes the risk and does not act on it.**

## Snippets

> pooled across all 25 models, in 35.3% of the conversations where a model satisfied every clinician-written criterion for recognizing the crisis, it failed to route the user toward human help [Source: arxiv-2610.12758-distressbench-evaluating-multi-dimensional-crisi.pdf — abstract]

> Existing safety benchmarks nonetheless score models primarily on refusal. In this setting refusal is not the desired behavior; what the conversation requires is a substantive supportive response. [Source: arxiv-2610.12758-distressbench-evaluating-multi-dimensional-crisi.pdf — abstract]

> These results argue for evaluating crisis safety on the care a model delivers rather than on what it declines to say, and for treating de-escalation and resource routing as deployment requirements. [Source: arxiv-2610.12758-distressbench-evaluating-multi-dimensional-crisi.pdf — abstract]
