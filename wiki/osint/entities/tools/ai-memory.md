---
title: "ai-memory — local agent memory (MIT Extract)"
type: entity
tags: [tool, atto, ccc, k242, mit, extract]
keywords: [ai-memory, reconstruct-before-inject, k230]
related:
  - sources/eval-local-agent-infra-2026-08-19.md
  - concepts/cemini-license-posture.md
  - concepts/atto-genealogy-agent-kit.md
  - sources/eval-repository-revenue-2026-08-20.md
maturity: draft
created: 2026-08-19
updated: 2026-08-20
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
wire_note: Reconstruct before inject (pairs MemHarness / K230)
---

## Relations

- @sources/eval-local-agent-infra-2026-08-19.md — K242 eval
- @concepts/cemini-license-posture.md
- @concepts/atto-genealogy-agent-kit.md — no Barone PII in memory stores

## Raw Concept

K242 Phase-0 Extract. Clone `.local/adopts/ai-memory` (~18MB). https://github.com/akitaonrails/ai-memory

## Narrative

| Field | Value |
|-------|--------|
| License | **MIT** [CONFIRMED gh 2026-08-19] |
| Local | `.local/adopts/ai-memory` |
| Verdict | **Extract** |
| wire_status | `policy_wired` |

Local memory store for coding agents. Steal: rewrite prior session state for the current task before injecting (K230 reconstruct-before-inject). Do not dump verbatim `hot.md` or Discord into a new turn. No living-person vitals in memory fixtures.

## Snippets

> ai-memory MIT Extract. Reconstruct before inject. [Source: `.local/reports/license-k242-2026-08-19.md`]
