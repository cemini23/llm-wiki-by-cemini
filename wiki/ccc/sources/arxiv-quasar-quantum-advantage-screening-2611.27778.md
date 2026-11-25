---
title: "QuASAR — LLM-assisted screening for quantum-advantage opportunities (2611.27778)"
type: source
related:
  - concepts/agent-completion-verification-gates.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | QuASAR: Toward an LLM-Assisted Framework for Screening, Prototyping, and Assessing Quantum-Advantage Opportunities in Scientific Computing |
| Author | Mark L. Carroll, Jordan A. Caraballo-Vega, Brian P. Powell, John L. Schnase (NASA Goddard, Adnet System) |
| Type | arXiv preprint |
| ID | 2611.27778 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.27778-quasar-toward-an-llm-assisted-framework-for-scre.pdfarxiv-2611.27778-quasar-toward-an-llm-assisted-framework-for-scre.pdf
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.27778-quasar-toward-an-llm-assisted-framework-for-scre.pdf` |
| Pages | unknown (read p.1 only) |
| Read status | read (abstract, intro) |

## Narrative

**Off-domain.** This is a quantum-computing-for-science paper. It is not about the `/route` lane, Claude Code, or MCP.

The pipeline has two agents. Agent one screens literature for computational kernels with a plausible quantum analogue, and proposes candidates with citations. Agent two independently verifies the citations. For surviving candidates, the pipeline reconstructs the source computation, formulates a quantum mapping, builds and runs a prototype, and benchmarks it against classical baselines.

Ten astrophysics candidates went in. Nine reached a benchmarked prototype. Three are reported in detail: combinatorial optimisation, stochastic simulation, and Bayesian inference. None showed quantum advantage at tested scale.

**Why it matters to this wiki.** The weak link is the interesting one. Generation and independent citation check are separate agents. That is the pattern this wiki already uses for verification, applied to literature screening. The paper adds no measurement of whether the citation check catches errors. No numbers on verification accuracy are reported on page 1. [TENTATIVE]
