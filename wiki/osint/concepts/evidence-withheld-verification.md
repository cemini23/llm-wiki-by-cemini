---
title: "Evidence-Withheld Verification — Blind Judge Anti-Fabrication Pattern"
type: concept
tags: [verification, prompt-design, agent-safety, anti-fabrication]
keywords: [evidence-withholding, blind-verification, anti-fabrication, LLM-as-judge, ARA-Seal, prompt-engineering]
related:
  - sources/agent-native-research-artifacts-2604.24658.md
  - concepts/agent-native-research-artifacts.md
  - concepts/conductor-orchestrator.md
maturity: validated
created: 2026-05-02
updated: 2026-05-02
---

## Raw Concept

When an LLM evaluates an answer as "correct," how do we know it didn't just see the reference answer and copy it? The ARA Seal Level 3 solves this with a simple structural constraint: the verifying agent receives the code kernel and algorithm descriptions but never the reported numbers. This prevents fabrication by copying expected outputs. The same principle applies to any LLM-as-judge evaluation.

## Narrative

The pattern has three rules:

**1. Separate the question from the answer.** The judge receives the task specification and the candidate's output, but never the reference answer or expected output. This is the core constraint.

**2. Judge against criteria, not against the answer.** Instead of "does this match the reference?", ask "does this satisfy these criteria: correctness, completeness, specificity?" Criteria must be written before seeing either the candidate or reference output.

**3. Withhold, don't redact.** Redaction implies the answer exists and was hidden — judges can infer from context. Withholding means the evaluation pipeline never has access to the reference at all. The reference lives in a separate system (or separate stage of the pipeline) that the judge cannot call.

**Concrete application in this workspace**:

- **Ingest quality check**: When evaluating whether a source page accurately reflects the paper, the judge receives the source page + the paper's abstract. It does NOT receive the full paper text. The check is "does the source page's claims contradict the abstract?" — a coarse filter, not a fidelity check.
- **Conductor routing evaluation**: When Meta-Router's LLM-as-judge evaluates whether a routing decision was correct, it receives the query + the routed model's output. It does NOT receive the "correct" model's output for comparison. It judges sufficiency, not relative quality.
- **Claim verification**: When checking a `[NEEDS VERIFICATION]` claim against an external source, the judge receives the claim text + the external source text. It does NOT receive the wiki page's conclusion about whether the claim is true. It extracts independently.

**Why this matters now**: The ARA Reproduction experiment found fabrication in 1 ARA run and 2 baseline runs. Structured artifacts reduce but don't eliminate hallucinated results. Evidence withholding is a structural defense, not a prompt-engineering trick — it removes the temptation vector rather than asking the model to resist it.

## Snippets

- "The verifying agent is isolated from the artifact's evidence layer: it receives only the code kernel and algorithm descriptions, never the reported numbers, preventing fabrication by copying expected outcomes." [Source: agent-native-research-artifacts-2604.24658.pdf p.10]
- "A verification agent can be granted the code kernel and algorithm descriptions while the evidence layer is withheld, preventing fabrication by copying expected values." [Source: agent-native-research-artifacts-2604.24658.pdf p.5]
