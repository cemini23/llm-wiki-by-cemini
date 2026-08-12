---
title: Sentrux — real-time architectural sensor / code-quality gate
type: entity
tags: [entity, tool, code-quality, rust, mit, ccc-fit, k233]
keywords: [sentrux, architectural-sensor, code-quality, tree-sitter, treemap, quality-gate]
related:
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 eval, Extract tier
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept

Repo `sentrux/sentrux`. MIT (docx claimed MIT), ~817★. Pure Rust real-time architectural sensor: maps dependencies/bottlenecks/structural relations as an AI agent writes code; 5 root-cause metrics + continuous quality score; treemap visualization via tree-sitter.

## Narrative

**Verdict: GO Extract (CCC / Atto quality gate).** Use the continuous architectural-quality signal as a pre-commit gate blocking AI-generated PRs that degrade structure. Local, passive, doesn't execute untrusted code. Needs verification: semantic validity of the score on highly modular dynamically-typed Python/TypeScript (built/tested primarily in Rust contexts).

[Source: sentrux/sentrux (retrieved 2026-08-12)]
