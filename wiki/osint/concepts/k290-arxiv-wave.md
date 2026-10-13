---
title: K290 arXiv Wave — VEPA agent guardrails, DistressBench crisis-care eval (Oct 2026)
type: source-hub
tags: [k290, arxiv, agent-guardrails, evaluation-methodology, ai-safety]
keywords: [k290, vepa, distressbench, guardrails, typed-events, rubric-weighted, recognition-action-gap, llm-judge]
related:
  - sources/arxiv-2610.12813-vepa-verified-evolving-guardrails-2026-10-13.md
  - sources/arxiv-2610.12758-distressbench-2026-10-13.md
  - concepts/k289-arxiv-wave.md
  - concepts/agent-tool-use-verification.md
  - concepts/ai-safety.md
  - concepts/k290-feeds-wave.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @sources/arxiv-2610.12813-vepa-verified-evolving-guardrails-2026-10-13.md
- @sources/arxiv-2610.12758-distressbench-2026-10-13.md
- @concepts/k289-arxiv-wave.md
- @concepts/agent-tool-use-verification.md
- @concepts/ai-safety.md
- @concepts/k290-feeds-wave.md

## Raw Concept

**OSINT K290 arXiv batch, 2026-10-13.** Two papers. One deferred: `2609.20804v1.pdf` (harness design for coding agents) is a **byte-identical duplicate** of the page already ingested 2026-09-18 — see `@sources/arxiv-2609.20804-harness-design-coding-2026-09-18.md`. Not re-ingested.

## Narrative

### 1. VEPA — verified evolving formal policy for agent guardrails

`arXiv 2610.12813` (Nguyen et al., Google Cloud AI + UNC + DeepMind). A **deterministic, pre-action allow/refuse guardrail** over **typed agent events**, which **keeps evolving** from deployment feedback.

Three-part pattern — **LLM proposes, a deterministic verifier disposes, an evidence gate decides when to trust:**
1. Rules are a finite set `r = (φᵣ, dᵣ)`; **φᵣ is a conjunction of typed predicates**, `dᵣ ∈ {allow, refuse}`. **Not SMT** — conflicts are found by **symbolic scope-overlap** over the schema domains, with a witness event.
2. An LLM proposes **typed patches** (Add/Delete/Rewrite/Split/Merge) from a failure set and a correct set; the verifier admits only **well-formed, conflict-free** candidates; **MAP-Elites-style** sampling walks the Pareto frontier.
3. **Evidence-aware authority:** each rule's error rate is `Beta(α,β)`; a rule activates **only when its posterior risk quantile clears the tolerance**, so uncertain updates cannot move a decision. No rule fires → **abstain to an LLM fallback**.

**Scores (cumulative prequential macro-F1, 5 seeds):** **0.81** ASSEBench-Safety (+0.02 over best baseline), **0.76** ATBench (+0.09). Coverage **~80% / 89% / 88%**. Robust to **mixed streams (~0.86 vs AGrail 0.78)**, **noisy feedback ρ=0.1 (~0.81)**, **30 steps (0.85±0.07)**, and **targeted adversarial labels (0.68 → 0.83)**. **Ablation: removing the verifier costs −0.13 F1.** Rule evaluation ≈**0.25 ms**.

**The open risk:** the **upstream LLM parser is neural and sits outside the guarantee**. Post-parse determinism is **not** end-to-end determinism.

**Relevance.** This is the strongest guardrail artefact of the wave and the direct follow-on to the K289 ToFu finding that **tool arguments from a model are untrusted**. It is the shape of a `PreToolUse` gate. → `@concepts/agent-tool-use-verification.md`.

### 2. DistressBench — score the care delivered, not the refusal

`arXiv 2610.12758` (Scale AI). **718 clinician-authored English conversations**, **23 SSH subcategories**, **task-specific rubrics of weighted atomic criteria across 7 dimensions**, each with a clinician reference. A model's score is the **weighted average over criteria satisfied** = **fraction of required care delivered**.

**25 models. Best 88.4%; median 71.4%; clinician ceiling 98.7%.** **25 models collapse into only 12 separable bands.** Complete rubric satisfaction is rare — median **2.3%**.

**The finding worth keeping — the recognition–action gap:** pooled across all 25 models, **in 35.3% of conversations where the model satisfied every criterion for recognizing the crisis, it failed to route the user to human help.** The shortfall concentrates in the **act** dimensions: safety disclaimers median **8.3%** (best 84.6%), de-escalation median **46.0%** (best 74.6%). **Multi-turn 0.685 < single-turn 0.742.**

**Methodology lesson that transfers:** a **refusal-scored** benchmark **registers filter silence as a pass** — one served model returned nothing on **7.5%** of conversations, firing on **34.2% of escalation-pattern** but only **0.8% of suicide-planning** conversations. That is the same blind spot as scoring an agent on what it withholds instead of what it does.

### Why it matters here
Both papers are **evaluation-methodology** contributions with an **action-over-abstention** theme, arriving one day after the K289 ToFu wave made tool arguments untrusted. VEPA supplies the enforcement pattern; DistressBench supplies the scoring pattern. Neither is a trading input.

## Snippets

> a deterministic verifier only accepts policies that are structurally valid and conflict-free [Source: arxiv-2610.12813-vepa-verified-evolving-formal-policy-for-lifelon.pdf — abstract]

> pooled across all 25 models, in 35.3% of the conversations where a model satisfied every clinician-written criterion for recognizing the crisis, it failed to route the user toward human help [Source: arxiv-2610.12758-distressbench-evaluating-multi-dimensional-crisi.pdf — abstract]
