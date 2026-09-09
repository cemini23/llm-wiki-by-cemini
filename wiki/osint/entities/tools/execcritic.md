---
title: ExecCritic — Microsoft Research test-then-repair coding-agent scaffold
type: entity
tags: [tool, k258, apache, ccc]
keywords: [execcritic, SWE-bench, fail-closed, MSR-Orchard]
related:
  - concepts/k258-harness-evolution-wave.md
  - sources/arxiv-2609.09133-execcritic-2026-09-09.md
  - concepts/k258-eval-github-wave.md
maturity: draft
created: 2026-09-09
updated: 2026-09-09
phase_0_verdict: GO REFERENCE
harness_verb: FILE
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
wire_note: REFERENCE clone only. Steal fail-closed test freeze. Do not PATH-wire.
---

## Relations

- @concepts/k258-harness-evolution-wave.md
- @sources/arxiv-2609.09133-execcritic-2026-09-09.md
- @concepts/k258-eval-github-wave.md

## Raw Concept

K258 Phase-0. Never trust eval docx SPDX.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/MSR-Orchard/execcritic |
| **License** | Apache-2.0 `[CONFIRMED]` gh api SPDX 2026-09-09 |
| **Local** | `.local/adopts/execcritic` |
| **Stars** | 2 (2026-09-09) |
| **Size** | ~1.1MB git |
| **Last push** | 2026-09-08 |
| **Verdict** | **GO REFERENCE** FILE. **0 Integrate GO.** |

Split Test agent from Repair agent. Fail-closed harness qualifies and freezes tests. Do not let one trajectory write both patch and test. CCC policy steal only. No SWE-bench runner install.

