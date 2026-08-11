---
title: SHE — Safety Harness Evolution (trajectory-driven)
type: entity
tags: [tool, harness, agent-safety, ccc, cyber, k232]
keywords: [she, safety-harness, rule-bank, tool-policy, safety-memory, agentsafetybench, harness-evolution]
related:
  - sources/arxiv-2608.09885-she-safety-harness-2026-08-11.md
  - concepts/ralph-autonomous-agent-pattern.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
---

## Relations

- @sources/arxiv-2608.09885-she-safety-harness-2026-08-11.md
- @concepts/ralph-autonomous-agent-pattern.md
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

What prompted this page: K232 ingest of arXiv:2608.09885. SHE is the **GO Extract** tool of the batch — an Apache-2.0 reference implementation for trajectory-driven safety-harness evolution relevant to CCC and the local abliterated lab. Not a prod harness; HITL gate for any mutation.

## Narrative

**SHE** (github.com/RainbowQTT/SHE, Apache-2.0, Shanghai AI Laboratory AgentDoG team) is a framework that learns evolving safe boundaries for LLM-agent harnesses from rollout trajectories. It decouples the harness into four editable artifacts with explicit safety responsibilities:

1. **System Prompt** — general safety behavior
2. **Rule Bank** — explicit safety rules
3. **Safety Memory** — experience from unresolved failure cases
4. **Tool Policy** — tool-use authority

The **attribution-guided evolution loop** converts trajectory failures into structured diagnoses, routes each to the responsible artifact, applies validity-checked bounded edits, and retains the best harness via safety–utility validation (base LLM, environment, and eval protocol fixed).

Evidence: on Agent-SafetyBench, ASR 8.6%→5.5% (vs static SafeHarness 17.1%→5.5%, a 3.1× reduction), clean UBR 25.7%→19.8%, UA 33.5%→47.6%; evolved harness generalizes to held-out AgentHarm (Harm Score 19.8%→9.8%; Harm Refusal 78.4%→86.4%) and transfers across agent models without re-evolution. Repo cloned at `.local/adopts/SHE` (~5.1MB).

**Adoption posture:** Extract as a REFERENCE for harness-evolution patterns in CCC + local-abliterated-lab; **do not auto-mutate prod harness without HITL**. The four-artifact decomposition is a useful vocabulary for auditing existing harnesses.

## Snippets

> "The safety of LLM agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control." [Source: arXiv:2608.09885 p.1]

> "SHE decomposes the harness into four artifacts with explicit safety responsibilities, including the System Prompt, Rule Bank, Safety Memory, and Tool Policy." [Source: arXiv:2608.09885 p.1]

## Dead Ends

- **Not a drop-in prod harness:** evolution loop mutates harness artifacts from trajectories — unsafe to run unattended against live agent stack; HITL only.
- **No weight download:** SHE is harness-side, not a model; nothing to pull from HF.
