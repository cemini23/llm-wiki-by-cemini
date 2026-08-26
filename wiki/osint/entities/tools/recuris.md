---
title: Recuris — EM/WM recursive memory harness
type: entity
tags: [tool, memory, harness, ccc, k314, k247]
keywords: [Recuris, Gen-Verse, experiential-memory, working-memory]
related:
  - sources/arxiv-2608.24876-recuris-em-wm-memory-2026-08-26.md
  - concepts/k247-agent-harness-wave.md
  - concepts/skill-misevolution.md
  - sources/arxiv-2608.21230-agent-memory-poisoning.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
wire_status: policy_wired
wire_target: .cursor/rules/cemini-phase1-policy-wires.mdc
wire_note: CCC K314 REFERENCE clone; runtime wont_wire
---

## Relations

- @sources/arxiv-2608.24876-recuris-em-wm-memory-2026-08-26.md
- @concepts/k247-agent-harness-wave.md
- @concepts/skill-misevolution.md
- @sources/arxiv-2608.21230-agent-memory-poisoning.md — K304 memory poisoning limits

## Raw Concept

K314 policy_wired. Apache-2.0 REFERENCE clone `.local/adopts/Recuris` (~4MB). arXiv 2608.24876.

## Narrative

- **URL:** https://github.com/Gen-Verse/Recuris
- **License:** Apache-2.0
- **Pattern:** Working Memory tracks task state and picks skills from Experiential Memory; execution traces localize failures; Meta-Agent applies validation-gated skill patches; bounded recursive loop.
- **Guardrails:** HITL before skill self-write (pairs K237/K307/K309); runtime **wont_wire** on prod harness.
- **Verdict:** GO REFERENCE (K247 ingest + CCC K314 federation wires).

## Snippets

> "Recuris improves task success in 35 of the 37 completed model–benchmark pairs." [Source: arxiv-2608.24876-recursive-experiential-working-memory-evolution.pdf]
