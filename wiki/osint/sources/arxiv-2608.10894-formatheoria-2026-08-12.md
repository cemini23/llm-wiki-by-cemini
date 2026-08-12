---
title: "FORMATHEORIA — Large-Scale Lean Theories from Mathematical Literature"
type: source
tags: [arxiv, k233, ccc, formal-verification, lean]
keywords: [2608.10894, formatheoria, lean, formalization, cfsg, ai-assisted-proof, verification]
related:
  - concepts/ai-assisted-formal-verification.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: skimmed
---

## Relations

- @concepts/ai-assisted-formal-verification.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.10894 |
| sha256 | `99140b349df27a01829c7cd506c5436a579df0356a2ba0925fe4ac10186ae014` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.10894-formatheoria-constructing-large-scale-lean-theor.pdf` |
| retrieved | 2026-08-12 |
| authors | Tianjiao Nie, Ao Zhang, et al. (Tsinghua Qiuzhen, Warwick, Tsinghua AIR) |

## Narrative

FORMATHEORIA coordinates an **AI-assisted workflow for large-scale Lean formalization** of advanced mathematics, applied to major components of the Classification of Finite Simple Groups (CFSG). Four challenges: discovering implicit dependencies, correcting source defects, preserving semantic fidelity, and reconciling cross-source misalignments.

The agent framework supports long-horizon execution via tool use, **context compaction**, review-gated termination, section-level source context, and **dependency-aware batch parallelization** — the workflow-process lessons (provenance preservation, protected approved declarations, independent review gates) are the transferable part, not the math.

Deliverable: machine-checked Lean development through Bender–Suzuki, encompassing Feit–Thompson Odd Order, Glauberman's Z*, and Brauer–Suzuki theorems.

Route: **WATCH / CCC awareness.** No Lean stack in this workspace; the transferable surface is the review-gated long-horizon agent workflow + formal-verification discipline for high-stakes automation. Phase-0 not run (no lean tooling need; not a tool-integration candidate).

[Source: arXiv:2608.10894]
