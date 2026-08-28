---
title: StarHarness — stratified harness evolution (ServiceNow)
type: entity
tags: [tool, harness, ccc, k313, k247]
keywords: [StarHarness, ServiceNow, stratified-search, harness-evolution]
related:
  - sources/arxiv-2608.24804-starharness-2026-08-26.md
  - sources/arxiv-2608.27311-verify-smarter-harness-evolution-2026-08-28.md
  - concepts/k247-agent-harness-wave.md
  - concepts/skill-misevolution.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
wire_status: policy_wired
wire_target: .cursor/rules/cemini-phase1-policy-wires.mdc
wire_note: CCC K313 REFERENCE clone; trainer wont_wire
---

## Relations

- @sources/arxiv-2608.24804-starharness-2026-08-26.md
- @sources/arxiv-2608.27311-verify-smarter-harness-evolution-2026-08-28.md — K248 HarnessLens sibling
- @concepts/k247-agent-harness-wave.md
- @concepts/skill-misevolution.md
- @concepts/cemini-license-posture.md

## Raw Concept

K313 policy_wired. MIT REFERENCE clone `.local/adopts/StarHarness` (~24MB). arXiv 2608.24804.

## Narrative

- **URL:** https://github.com/ServiceNow/StarHarness
- **License:** MIT
- **Pattern:** evolve harness (prompts/tools/skills/MCP/subagents/loop) with weights frozen; stratify by baseline failure mode; proposer-visible ≠ selection tasks; held-out generalization eval; 4–12 changes → +20–35 pp.
- **Guardrails:** never optimize pass criteria; no unattended `.cursor/skills` evolution; trainer runtime **wont_wire**.
- **Verdict:** GO REFERENCE (K247 ingest + CCC K313 federation wires).

## Snippets

> "Harness evolution improves full-benchmark performance by 20–35 percentage points over the default harness." [Source: arxiv-2608.24804-starharness-evolving-harnesses-with-stratified-s.pdf]
