---
title: "Brain Researcher — neuroimaging agent harness + claim cards (2608.19902)"
type: source
tags: [arxiv, science-agents, harness, neuroimaging, ood, k245]
keywords: [Brain-Researcher, Poldrack, claim-card, multiverse, BR-KG]
related:
  - concepts/harness-optimization-bench.md
maturity: draft
created: 2026-08-22
updated: 2026-08-22
read_status: skimmed
---

## Relations

- @concepts/harness-optimization-bench.md — harness lifts tool-selection; claim scope stays with the researcher

## Raw Concept

- **title:** Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis
- **author:** Zijiao Chen, Nicholas Lu, … Russell A. Poldrack (Stanford; TReNDS; Inria; UT Austin; NUS; UQ)
- **type:** arXiv paper
- **location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.19902-bringing-analytic-rigor-to-agentic-ai-for-scienc.pdf`
- **retrieved:** 2026-08-22
- **pages:** 103 (skim: abstract + intro + results through tool-calling / grounding benches)
- **read-status:** skimmed
- **arXiv:** 2608.19902
- **sha256:** `a3c93c8ba592226843690055f0d52cb08f26aafccac11266c4442211b5ca65b4`

## Narrative

K244 archived this as OOD neuroimaging with no page. Re-dropped 2026-08-22; file a thin wiki-only source so the RSS/arxiv watcher stops looping.

Brain Researcher is a **researcher-governed harness** inside an existing neuroimaging compute environment: admissible analyses, required checks, and claim scope are declared up front. Commitment card (hashed before any run) + claim card after review (accepted / qualified / revised / blocked / rejected / deferred). BR-KG: 745,949 nodes / 2,461,469 edges (2026-07-07 snapshot).

Paired seven-model bench: first-choice tool-selection **23.3% → 93.6%** (+70.2 pp); verifiable grounding **4.6% → 22.0%** (improved, not solved). Multiverse analyses expose specification sensitivity.

**OSINT steal (pattern only):** commitment-before-results + explicit claim states. Do not clone a 103-page neuroimaging stack. No Phase-0 GO. No Atto/Barone path.

## Snippets

> AI agents can execute scientific analyses, but an analytic output becomes a defensible claim only after alternatives are weighed and the claim is limited to what the evidence supports. [Source: arxiv-2608.19902 p.1]

> Brain Researcher increased first-choice tool-selection accuracy across seven models by 70.2 percentage points (23.3% without it versus 93.6% with it) and verifiable grounding from 4.6% to 22.0%. [Source: arxiv-2608.19902 p.1]

Paper: https://arxiv.org/abs/2608.19902 [Source: URL (retrieved 2026-08-22)]
