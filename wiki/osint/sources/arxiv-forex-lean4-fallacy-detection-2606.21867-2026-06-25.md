---
title: "ForEx — Lean4 formal verification for fallacy detection (arXiv 2606.21867)"
type: source
tags: [source, arxiv, formal-verification, lean4, llm-reasoning, k129]
keywords: [2606.21867, ForEx, Lean4, logical fallacy, LLM Argument Verification Matrix]
related:
  - sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md
  - sources/arxiv-relaxed-nfl-auto-formalization-2606.24443-2026-06-26.md
  - sources/arxiv-rlvf-formally-verified-law-2606.23913-2026-06-26.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/relaxed-nfl-auto-formalization.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/rlvf-verifier-feedback-training.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-10-25
clusters: [llm-agents]
---

## Relations

- @sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md — complementary agent verification lane
- @concepts/poker-arena-multi-axis-cognitive-profile.md — verifier-steering for poker eval

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ForEx: A Formal Verification Framework for Explainable Reasoning in Logical Fallacy Detection and Annotation |
| **Authors** | Pei-Cing Huang et al. |
| **arXiv** | 2606.21867v1 (Jun 2026) |
| **sha256** | `a5eee801dbbd5997a01704c4198147f9786591b228c70565a8a9bebe37508b79` |
| **Repo** | https://github.com/D3-Laboratory/ForEx [TENTATIVE] |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.21867-2606-21867v1-forex-a-formal-verification-framewo.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + verification matrix) |

## Narrative

**ForEx** translates LLM-generated explanations into **Lean4** and verifies whether the formalized rationale is **derivable under encoded premises** — not whether the natural-language argument is valid.

**LLM Argument Verification Matrix:** separates **label consistency** from **formal verification status**.

**LOGIC-Climate results:** >90% of outputs translate to chains passing verification, yet ~20% agreement with human fallacy labels [TENTATIVE] — exposes gap between formal derivability and annotation agreement invisible to prediction metrics.

**Cemini steal:** **Label vs proof status decoupling** for poker trajectory verifiers and ingest gate reasoning — reference pattern, not Lean4 prod dependency without audit.

## Snippets

> "ForEx moves LLM evaluation beyond label correctness toward machine-checkable analysis of formalized reasoning chains." [Source: arXiv:2606.21867 abstract (retrieved 2026-06-25)]

> "Over 90% of LLM outputs can be translated into formal reasoning chains that pass verification, while agreement with human annotations remains around 20%." [Source: arXiv:2606.21867 abstract (retrieved 2026-06-25)]

> "We introduce the LLM Argument Verification Matrix, which separates label consistency from formal verification status." [Source: arXiv:2606.21867 abstract (retrieved 2026-06-25)]

## Dead Ends

- Fallacy detection ≠ poker equity proof — Lean4 toolchain not on Cemini prod path without Phase-0.
