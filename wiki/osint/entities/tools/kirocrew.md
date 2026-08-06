---
title: "KiroCrew — multi-agent crew orchestration (Atto/CCC)"
type: entity
tags: [tool, extract, apache-2, k225, atto, ccc]
keywords: [KiroCrew, kirodotdev, crew, orchestration]
related:
  - sources/eval-tech-stack-opportunity-2026-08-06.md
  - entities/tools/deepcode-hku.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
phase_0_verdict: EXTRACT patterns — Apache-2.0 K225; NO local clone (size gate)
wire_status: pending
---

## Relations

- @sources/eval-tech-stack-opportunity-2026-08-06.md
- @entities/tools/deepcode-hku.md
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

| Field | Value |
|-------|--------|
| **Repo** | https://github.com/kirodotdev/KiroCrew |
| **License** | Apache-2.0 `[CONFIRMED]` gh api K225 |
| **Size** | gh ~244MB; shallow clone ~395MB — **skipped** (Phase-0 &lt;500MB batch budget) |
| **Eval** | Extract → Atto/CCC |
| **Local** | none this batch |

## Narrative

Crew-style agent orchestration — compare against federation Task/subagent patterns before adopt. **No `.local/adopts/KiroCrew`** in K225 (size). Steal role/crew framing from docs + Atto/CCC briefs only until a dedicated size-budgeted Phase-0.

## Snippets

> gh SPDX Apache-2.0 overrides eval NOT FOUND. [Phase-0 K225]
