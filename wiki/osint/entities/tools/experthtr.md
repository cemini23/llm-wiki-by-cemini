---
title: ExpertHTR — unified VLM handwritten text recognition
type: entity
tags: [tool, k262, atto, htr]
keywords: [ExpertHTR, VLM, MoE, Sparsegen, Transkribus]
related:
  - concepts/k262-atto-htr-wave.md
  - sources/arxiv-2609.12705-experthtr-2026-09-16.md
  - concepts/k261-atto-wave.md
maturity: draft
created: 2026-09-16
updated: 2026-09-16
phase_0_verdict: FILE
harness_verb: FILE
wire_status: wont_wire
wire_note: Method FILE. Transkribus remains sole product HTR.
---

## Relations

- @concepts/k262-atto-htr-wave.md
- @sources/arxiv-2609.12705-experthtr-2026-09-16.md
- @concepts/k261-atto-wave.md

## Raw Concept

K262 method page for ExpertHTR (arXiv:2609.12705). Not a clone.

## Narrative

| Field | Value |
|-------|-------|
| **Paper** | arXiv:2609.12705 |
| **License** | paper method; no product clone |
| **Verdict** | FILE methodology. **Transkribus remains sole product HTR.** |

Unified VLM HTR. Page–Region–Line. Four tasks. Sparse MoE with always-on shared branch + Sparsegen. Seven handwriting benchmarks. Atto FILE. No Barone PII. Human-gated `truth.ged`.
