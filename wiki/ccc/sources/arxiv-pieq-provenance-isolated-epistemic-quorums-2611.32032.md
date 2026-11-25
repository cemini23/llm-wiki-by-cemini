---
title: "Provenance-Isolated Epistemic Quorums — execution-bound evidence certification (2611.32032)"
type: source
related:
  - concepts/execution-bound-evidence-certification.md
  - concepts/agent-completion-verification-gates.md
  - concepts/evidence-grounded-debate-stopping.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Provenance-Isolated Epistemic Quorums: Execution-Bound Evidence Certification and Plausible-World Safety Gating in Agentic Control Planes |
| Author | Jun He, Deying Yu (OpenKedge LLC) |
| Type | arXiv preprint (cs.AI) |
| ID | 2611.32032 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.32032-provenance-isolated-epistemic-quorums-execution.pdfarxiv-2611.32032-provenance-isolated-epistemic-quorums-execution.pdf
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.32032-provenance-isolated-epistemic-quorums-execution.pdf` |
| Pages | 22 |
| Read status | read (abstract, intro) |

## Narrative

The paper makes one claim: agreement among language models is not evidence. Models share pretraining priors. They conform to each other during debate. A voting ensemble therefore correlates errors. It does not give independent fault tolerance.

The strict fix fails too. A deterministic verifier in front of free-form proposals blocks everything. In a 40-case pilot with five models, strict verification blocked every unsafe action (0 of 40) and also every useful action (0 of 19 mitigations). It dropped 140 of 284 submitted proofs.

**PIEQ** (Provenance-Isolated Epistemic Quorums) is the middle path. It keeps every language model outside the trusted computing base. It combines four parts:

1. **Assumption-based truth maintenance** — track which faults are ruled out, not which answers are popular.
2. **Physical provenance isolation** — evidence must come from disjoint failure domains. In-band SQL probes and out-of-band management telemetry are separate witnesses.
3. **Plausible-world safety gating** — gate a mutation across all unrefuted fault worlds, and fall back to read-only probes under ambiguity.
4. **Execution binding** — admission certificates bind to snapshot barriers, revision checks, authorization freshness, and capability tiers.

Reported results: zero unsafe admissions within stated assumptions, and zero false-precondition commits. The system turns agent proof omissions into recoverable false blocks. It does not turn them into unsafe actions.

The authors also bound where the LLM adds value. It helps in multi-hop proof search over large rule spaces, where bounded deterministic search saturates. It helps in unstructured incident triage over authenticated telemetry. Elsewhere deterministic rules suffice.

**Why it matters.** This is a design for a safety gate around an agent that mutates live infrastructure. The useful idea for this wiki is domain separation: two agents that read the same logs are not a quorum. They are one witness with two voices. The same rule applies to any multi-agent review in this workspace.

Caveats. The authors label their own benchmarks. The API confirmation run used provider aliases, not immutable dated snapshots. Physical failover promotion and multi-host hardware fault isolation remain open work. [TENTATIVE]

## Snippets

> "Agreement among large language models is not physical evidence for mutating production infrastructure." [Source: `arxiv-2611.32032-provenance-isolated-epistemic-quorums-execution.pdf` p.1, retrieved 2026-11-25]
