---
title: "Execution-bound evidence certification — agreement is not evidence"
type: concept
related:
  - sources/arxiv-pieq-provenance-isolated-epistemic-quorums-2611.32032.md
  - concepts/agent-completion-verification-gates.md
  - concepts/evidence-grounded-debate-stopping.md
  - concepts/self-verification-failure-taxonomy.md
updated: 2026-11-25
maturity: draft
---

## Raw Concept

Question this page answers: how do you certify an agent's claim before it changes live state, when the agents all share the same priors? Synthesised from `@sources/arxiv-pieq-provenance-isolated-epistemic-quorums-2611.32032.md` (2611.32032).

## Narrative

Multi-agent debate looks like fault tolerance. It is not. Agents from the same base model share pretraining priors, and they conform to each other during debate. Agreeing agents correlate their errors. A vote is one witness with several voices.

The opposite fix also fails. A strict deterministic verifier in front of free-form proposals blocks good actions along with bad ones. In the paper's pilot, it blocked all 19 useful mitigations. A gate that blocks everything is not safe; it is off.

**The middle path has four parts.**

1. **Isolate provenance.** Evidence must come from disjoint physical failure domains. Two agents reading the same log are one source. A log plus out-of-band telemetry are two.
2. **Track unrefuted faults.** Reason over assumptions. Enumerate plausible fault worlds, then rule them out with evidence. Do not score answers by popularity.
3. **Gate across all open worlds.** Admit a mutation only if it is safe under every fault world not yet ruled out. When ambiguity remains, fall back to read-only probes.
4. **Bind the certificate to execution.** An admission certificate must bind to a snapshot, a revision, a fresh authorization, and a capability tier. A certificate that can drift from the state it certified is not a gate.

The paper reports zero unsafe admissions within stated assumptions and zero false-precondition commits. It converts missing proofs into false blocks, which are recoverable, instead of unsafe actions, which are not.

**Where the model still helps.** Multi-hop proof search in large rule spaces, and unstructured triage over authenticated telemetry. Elsewhere deterministic rules are enough.

**Status.** Author-labelled benchmarks. Provider aliases instead of immutable snapshots. Physical failover promotion is open work. [TENTATIVE]

## Snippets

> "voting ensembles correlate errors instead of providing independent fault tolerance; yet attaching rigid deterministic checks to unconstrained agent outputs paralyzes incident remediation." [Source: `arxiv-2611.32032-provenance-isolated-epistemic-quorums-execution.pdf` p.1, retrieved 2026-11-25]
