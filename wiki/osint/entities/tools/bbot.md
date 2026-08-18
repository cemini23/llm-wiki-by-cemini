---
title: "bbot — OSINT recon (AGPL-3.0 Extract-only)"
type: entity
tags: [tool, cyber, k241, agpl, extract-only]
keywords: [bbot, blacklanternsecurity, AGPL-3.0]
related:
  - sources/eval-multi-wiki-revenue-plan-2026-08-18.md
  - concepts/cemini-license-posture.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - entities/tools/sherlock.md
  - entities/tools/mitaka.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
---

## Relations

- @sources/eval-multi-wiki-revenue-plan-2026-08-18.md — K241 eval (docx said GPL — **wrong**)
- @concepts/cemini-license-posture.md — AGPL isolate
- @concepts/local-abliterated-llm-pentest-stack.md — authorized-target only
- @entities/tools/sherlock.md — username sibling
- @entities/tools/mitaka.md — browser OSINT sibling

## Raw Concept

K241 Phase-0 Extract-only. Clone `.local/adopts/bbot` (16MB). **AGPL-3.0** (LICENSE) — eval docx claimed GPL-3.0.

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/blacklanternsecurity/bbot |
| License | **AGPL-3.0** [CONFIRMED gh + LICENSE 2026-08-18] |
| Local | `.local/adopts/bbot` (16MB) |
| Verdict | **GO Extract-only REFERENCE** |
| wire_status | `policy_wired` |

Authorized-target recon modular scanner. **Do not vendor into proprietary Atto / CeminiSuite kits.** Subprocess/sidecar only if ever used. No mass scan. No PrivFu/HTB/C2 chaining.

## Snippets

> bbot: claimed GPL-3.0 → **AGPL-3.0**. Extract-only. [Source: `.local/reports/license-k241-2026-08-18.md`]
