---
title: "ProofCoder — continuous reasoning instead of a tactic loop"
type: source
tags: [source, arxiv, formal-verification, proof-assistants, LLM]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ProofCoder: Continuous Reasoning for Automated Software Verification |
| Authors | Martim Afonso, Inês Lynce, Maurizio Morisio, João F. Ferreira (INESC-ID, IST, Politecnico di Torino) |
| arXiv | 2611.14106 |
| Pages | 21 |
| Read status | skimmed (abstract) |

## Narrative

Formal verification with proof assistants gives strong correctness guarantees, but writing the proofs is **labour-intensive and expert work**.

LLM approaches have shown promise, and most of them constrain the model to a **rigid tactic-generation loop**: the surrounding system controls premise retrieval, proof-state management, and backtracking, and the model emits one tactic at a time.

ProofCoder argues for **continuous reasoning** instead — letting the model work across the proof rather than one tactic per turn inside a harness that owns the state.

### Why the harness-controlled loop is the thing under attack

The tactic loop exists for a good reason: it keeps the model from producing an invalid proof. Every step is checked, the state is external, and a wrong move is caught immediately.

The cost is that the model never sees the shape of the proof. It cannot plan, cannot back up for a reason, and cannot choose a different strategy — because the harness owns the strategy.

That is the same trade as scripted versus open-ended agents in the kernel-optimisation paper from an earlier batch: **structure buys reliability and forfeits direction.**

**Caveat.** Abstract only. No success rate or benchmark reproduced.

## Snippets

> "These approaches typically constrain the model to a rigid tactic-generation loop, in which the surrounding system controls premise retrieval, proof-state management, and backtracking." [Source: arxiv-2611.14106 p.1]

## Dead Ends

- **Citing a proof success rate.** Abstract only.
