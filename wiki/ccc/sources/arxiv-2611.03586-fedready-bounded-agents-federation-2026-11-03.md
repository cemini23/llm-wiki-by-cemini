---
title: "FedReady — bounded agents for federation formation"
type: source
tags: [source, arxiv, federated-learning, agents, bounded, contracts]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FedReady: Bounded Agents for Federation Formation |
| Authors | Ziyue Xu, Holger R. Roth, Chester Chen, Peter Cnudde (NVIDIA) |
| arXiv | 2611.03586 |
| Pages | 26 |
| Read status | skimmed (abstract) |

## Narrative

Federated-learning runtimes standardise aggregation and deployment, but each new study still needs **federation formation**: choosing eligible sites and preparing their local data and task code. This repeats whenever the target changes.

FedReady does that preparation with **bounded LLM agents**. Agents propose shared contracts, local adapters, and task code. The **runtime owns workflow state** and accepts an artifact only after checks tied to its **digest**.

Two-stage selection:

- **Discovery** favours recall — find candidate sites broadly.
- **Local eligibility verification** checks task support before admission.

Once sites and artifacts are fixed, conventional training proceeds and the readiness agents are gone.

Results: 39 simulated retinal sites, four tasks. Discovery reaches **recall 1.00 at precision 0.65**. Eligibility verification removes **all 17 false positives** without losing an eligible site–task pair. 45,575 task-record instances, four 100-round jobs.

### The pattern

**Bounded agents that prepare, then exit, with the runtime holding state and admitting artifacts by digest.**

That is a clean answer to the usual agent problem: an unrestricted agent that negotiates contracts and modifies shared state is unaccountable. This one proposes into a runtime that verifies. The agent cannot admit its own work.

The recall-then-precision split is the second idea. Discovery is deliberately imprecise because a missed site is worse than a candidate that fails verification.

**Caveat.** Abstract only, and the sites are simulated.

## Snippets

> "Agents propose shared contracts, local adapters, and task code; the runtime owns workflow state and accepts artifacts only after checks tied to their digests." [Source: arxiv-2611.03586 p.1]

## Dead Ends

- **Treating the 39 simulated sites as a real federation.** Simulated.
