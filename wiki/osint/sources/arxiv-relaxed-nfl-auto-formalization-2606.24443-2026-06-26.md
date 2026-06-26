---
title: "Relaxed NFL auto-formalization for verifiable math (2606.24443)"
type: source
tags: [auto-formalization, formal-verification, relaxed-nfl, k131]
keywords: [Relaxed-NFL, Core-NFL, autoformalization, theorem-prover, intermediate-representation]
related:
  - concepts/relaxed-nfl-auto-formalization.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - sources/arxiv-forex-lean4-fallacy-detection-2606.21867-2026-06-25.md
  - sources/arxiv-rlvf-formally-verified-law-2606.23913-2026-06-26.md
maturity: draft
read_status: read
created: 2026-06-26
updated: 2026-06-26
clusters: [llm-agents, verifier, poker]
---

## Relations

- @concepts/relaxed-nfl-auto-formalization.md — intermediate formal language pattern
- @sources/arxiv-forex-lean4-fallacy-detection-2606.21867-2026-06-25.md — K129 ForEx verifier cluster
- @concepts/poker-arena-multi-axis-cognitive-profile.md — trajectory legality as informal→formal gap

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Verifiable Auto-Formalization of Mathematics Using a Relaxed Natural Formal Language |
| **Authors** | Zhicheng Hui et al. (Shanghai Jiao Tong University) |
| **arXiv** | [2606.24443](https://arxiv.org/abs/2606.24443) |
| **sha256** | `4712ab3ad9725a30d5bf973363b54897fd344e0dd6875cf953a85c4ef82b7eab` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.24443-2606-24443v1-verifiable-auto-formalization-of-ma.pdf` |
| **Retrieved** | 2026-06-26 |
| **Read status** | read (abstract + method skim) |

## Narrative

Addresses the **representational gap** between informal math and prover-ready formal languages by introducing **Relaxed Natural Formal Language (Relaxed NFL)** — close to informal writing, allows partial specs; **elaboration** later resolves ambiguity into **Core NFL** for prover check.

**Cemini steal:** same two-stage pattern for **poker decision traces** — Relaxed NFL analog = structured action log (street, pot, sizing intent); elaboration = PokerKit legality + stack accounting; verifier = static harness / ForEx-style fallacy check on explanation text.

**Posture:** REFERENCE + poker-arena brief (steal pattern, not repo Adopt — paper-only).

### Two-stage pipeline

| Stage | Math paper | Poker Arena analog |
|-------|------------|-------------------|
| Auto-formalize | Informal proof → Relaxed NFL | NL reasoning → structured `DecideTrace` JSON |
| Elaborate | Relaxed NFL → Core NFL | Fill implicit pot/stack fields via engine |
| Verify | Theorem prover | Harness tests + hand-legality + axis rubric |

## Snippets

> "Relaxed NFL … preserves the usual structure of informal reasoning and allows partially specified expressions … resolved during a later elaboration stage" [Source: arxiv-2606.24443 abstract (retrieved 2026-06-26)]
