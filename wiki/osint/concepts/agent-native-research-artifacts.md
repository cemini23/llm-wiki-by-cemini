---
title: "Agent-Native Research Artifacts — Structured Knowledge over Narrative"
type: concept
tags: [llm-agents, research-methodology, infrastructure, reproducibility]
keywords: [ARA, agent-native, structured-knowledge, exploration-graph, research-artifacts, forensic-bindings, reproducibility, Live-Research-Manager, Seal-protocol]
related:
  - sources/agent-native-research-artifacts-2604.24658.md
  - concepts/coding-agents-alphazero.md
  - concepts/agent-memory-critique.md
  - concepts/policy-distillation.md
  - concepts/exploration-graph-dead-ends.md
  - concepts/evidence-withheld-verification.md
  - concepts/typed-relation-dependencies.md
  - concepts/conductor-orchestrator.md
maturity: draft
created: 2026-05-02
updated: 2026-05-02
---

## Raw Concept

What if the primary output of research wasn't a narrative paper but an agent-executable knowledge package? The ARA protocol proposes exactly this — a four-layer artifact format designed to be operated on by agents, not read by humans.

## Narrative

The ARA protocol (Liu et al., 2026) is a response to two structural failures of PDF-based scientific communication:

**The Storytelling Tax**: Publication compiles a branching research process into a linear success narrative, discarding dead ends, rejected hypotheses, and design pivots. METR analysis: 90.2% of agent compute dollars on RE-Bench are spent on failed exploration that publication erases. Median failed-to-success token ratio: 113×.

**The Engineering Tax**: Papers are written at the precision needed to convince a reviewer (sufficient to produce belief), not the precision agents need to execute (sufficient to produce correct execution). Only 45.4% of 8,921 PaperBench reproduction requirements are fully specified in PDFs. Missing hyperparameters alone account for 26.2% of gaps.

ARA's answer is four interlocking layers within a plain-text directory structure:

1. **Cognitive Layer** (`/logic`) — claims with falsification criteria and proof pointers, algorithms as self-contained pseudocode, experiments with declarative procedures, typed dependencies replacing passive citations. The "why" of the research.

2. **Physical Layer** (`/src`) — executable code in kernel mode (core modules with typed I/O, 1-2 orders of magnitude smaller than full repos) or repository mode (full implementation with annotated manifest). Every hyperparameter annotated with rationale and search range.

3. **Exploration Graph** (`/trace`) — research DAG with five typed node kinds (question, decision, experiment, dead_end, pivot). A "git log for research" where dead-end nodes preserve hypothesis, failure mode, and lesson.

4. **Evidence Layer** (`/evidence`) — raw outputs only. Claim → experiment → evidence chain is machine-traversable. Withholding this layer from verification agents prevents fabrication by copying expected values.

**Forensic bindings** are the connective tissue: every claim links to the code that tests it and the evidence that supports it. These cross-layer references are what conventional artifacts lack — claims, code, and evidence exist in separate unlinked formats.

Three ecosystem mechanisms surround the protocol:

- **Live Research Manager**: An agent skill (not a custom SDK) that captures decisions and dead ends as a side effect of normal researcher-agent conversation. Silent, framework-independent, with faithful epistemic provenance tagging (user, ai-suggested, ai-executed, user-revised).

- **ARA Compiler**: An agent skill that translates legacy PDFs + repos into ARA format via four stages (semantic deconstruction → cognitive mapping → physical grounding → forensic cross-linking). The core problem is recovering lineage, not populating layers.

- **ARA Seal**: Three-level machine-verifiable credential. Level 1 (structural integrity) checks schema conformance and reference resolution. Level 2 (argumentative rigor) uses a rubric-anchored agent to assess claim scope, evidence coverage, and baseline coverage. Level 3 (execution reproducibility) has an agent reproduce central claims directionally with evidence layer withheld.

For this workspace: ARA formalizes what we already do with `wiki/` — structured, cross-linked knowledge with explicit provenance. The Compiler pattern mirrors our ingest pipeline (read source → extract claims → cross-link → file). The Live Research Manager connects to Conductor's agent-memory ambitions and the Stash episodic store. The Seal Level 3 evidence-withholding design is a reusable anti-fabrication pattern for any system where agents might copy expected outputs.

**Limitations**: The Compiler cannot recover what was never recorded — papers without code or trajectory data produce ARA shells. The Live Research Manager assumes AI-native workflows. Adversarial robustness and schema evolution are aspirational, not implemented.

## Snippets

- "An agent engaging with a research project asks four structurally distinct questions: why does this work, how is it implemented, what was tried along the way, and what are the numbers." [Source: agent-native-research-artifacts-2604.24658.pdf p.4]
- "Knowledge over Narrative — the organized, evolving knowledge produced during research is the primary scientific object; the narrative paper is a compiled view." [Source: agent-native-research-artifacts-2604.24658.pdf p.4]
- "Compressing them into a single document is not merely suboptimal but lossy: once flattened into narrative, the original structure cannot be recovered." [Source: agent-native-research-artifacts-2604.24658.pdf p.4]
- Live Research Manager: "for the first time, the research process is born digital and born textual. Every instruction, intermediate result, design choice, and abandoned direction already exists as machine-readable text — lacking only a system to let it crystallize naturally." [Source: agent-native-research-artifacts-2604.24658.pdf p.6]
- Compiler principle: "Knowledge lineage, not flat extraction. Narrative compilation destroys the provenance chains connecting claims to experiments, experiments to evidence, and evidence to code." [Source: agent-native-research-artifacts-2604.24658.pdf p.8]
- ARA Seal P1: "Automate the mechanical; reserve humans for judgment. The review system should never ask a human to verify that Experiment E03 matches Claim C02 when a machine can do so in seconds." [Source: agent-native-research-artifacts-2604.24658.pdf p.9]
- "Publishing becomes a Git-like operation, reviewers consume Seal-attested artifacts through their preferred surfaces, and downstream agents read ARAs as structured baselines, training environments, or starting points for new questions." [Source: agent-native-research-artifacts-2604.24658.pdf p.11]
