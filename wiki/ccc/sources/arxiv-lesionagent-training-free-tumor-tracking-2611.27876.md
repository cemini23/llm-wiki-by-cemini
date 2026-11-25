---
title: "LesionAgent — training-free agentic tumor tracking in longitudinal CT (2611.27876)"
type: source
related:
  - concepts/agent-harness-operational-definition.md
  - concepts/agent-completion-verification-gates.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT |
| Author | Maximilian Rokuss et al. (DKFZ Heidelberg, Heidelberg University, Microsoft Research, Stanford) |
| Type | arXiv preprint |
| ID | 2611.27876 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.27876-lesionagent-training-free-agentic-tumor-tracking.pdfarxiv-2611.27876-lesionagent-training-free-agentic-tumor-tracking.pdf
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.27876-lesionagent-training-free-agentic-tumor-tracking.pdf` |
| Pages | 23 |
| Read status | read (abstract, figure 1) |

## Narrative

**Off-domain.** This is a medical-imaging paper. It does not address `/route` or coding harnesses.

The transferable result is a clean harness-versus-model separation. LesionAgent is an LLM agent with **no task-specific training**. It runs frozen 3D foundation models as tools, acts in 3D through coordinate-labelled views, keeps a lesion registry across visits, verifies every model output it relies on, and leaves every measurement to a deterministic guideline engine (RECIST).

The reported numbers separate the model from the harness:

- Lesion detection F1: frozen foundation-model pipeline 62%; Qwen3.8-27B one-shot 6%, inside LesionAgent 73%; Opus 5.5 one-shot 21%, inside Claude Code 31%, inside LesionAgent 78%.
- On clinical follow-ups it agrees with radiologists at 20 of 23 follow-ups, including every change in response.
- A fixed-rule chain of the same 3D models calls progression falsely at 33 of 56 follow-ups. LesionAgent does so twice.

The authors state the harness, not the LLM, makes the difference.

**Why it matters to this wiki.** The one-shot scores are the point. The same model scores far higher inside a harness that checks its tools and keeps state. This is the "harness over model" claim in a second domain, with measurement. It is adjacent evidence, not a replication of a coding result. [TENTATIVE]
