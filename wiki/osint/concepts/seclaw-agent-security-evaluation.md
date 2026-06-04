---
title: SeClaw — spec-driven agent security benchmarks (trajectory-aware)
type: concept
tags: [concept, agent-security, evaluation, k98]
keywords: [seclaw, trajectory, docker-testbed, openclaw, risk-spec, tool-use]
related:
  - sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md
  - concepts/ems-execution-security-gaps.md
  - concepts/cli-anything-agent-native-computer-use.md
  - "@cybersecurity-wiki/briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md"
  - "@cybersecurity-wiki/sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md"
  - "@cybersecurity-wiki/entities/tools/seclaw-eval.md"
  - "@cybersecurity-wiki/concepts/seclaw-agent-security-evaluation.md"
  - "@cybersecurity-wiki/entities/tools/defenseclaw.md"
  - "@cybersecurity-wiki/briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md"
maturity: draft
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- @sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md
- @concepts/ems-execution-security-gaps.md — prod trading security (complementary scope)
- @cybersecurity-wiki/concepts/seclaw-agent-security-evaluation.md — **canonical** eval methodology
- @cybersecurity-wiki/entities/tools/seclaw-eval.md — benchmark repo entity
- @cybersecurity-wiki/entities/tools/defenseclaw.md — runtime gate (complementary)

## Raw Concept

arXiv:2606.02302 — scalable **agent security eval** via spec-driven task generation + docker testbed.

## Narrative

Fills gap between static prompt-injection lists and **stateful tool-using agents** (files, memory, MCP). Key design choices:

- Tasks synthesized from **structured risk specs** (coverage + control).
- **Trajectory-aware** scoring — unsafe tool steps matter, not final chat politeness.
- Risk taxonomy: resources, user tasks, environment, intrinsic agent behavior.

**Cemini:** CONDITIONAL-GO to run against **conductor + lazy-tool** harness before expanding MCP tool surface — laptop eval only; repo `seclaw-eval/seclaw-eval` needs Phase-0 license + CI cost check [NEEDS VERIFICATION 2026-06-04].

## Snippets

> "bridging systematic task synthesis and reproducible security evaluation"

[Source: arxiv-2606.02302-seclaw-spec-driven-security-task-synthesis-for-e.pdf p.1, retrieved 2026-06-04]
