---
title: Sentrux — real-time architectural sensor / code-quality gate
type: entity
tags: [entity, tool, code-quality, rust, mit, ccc-fit, k233]
keywords: [sentrux, architectural-sensor, code-quality, tree-sitter, treemap, quality-gate]
related:
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - sources/deep-research-url-evaluation-2026-08-13.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-12
updated: 2026-08-13
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 eval, Extract tier
- @sources/deep-research-url-evaluation-2026-08-13.md — K235 re-eval: Watch (immaturity), MIT re-verified
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept

Repo `sentrux/sentrux`. **MIT verified** (gh api + LICENSE file, 2026-08-13), 2.7k★, last push 2026-03-19. Pure Rust real-time architectural sensor: maps dependencies/bottlenecks/structural relations as an AI agent writes code; 5 root-cause metrics + continuous quality score; treemap visualization via tree-sitter.

## Narrative

**Verdict: GO Extract (CCC / Atto quality gate) — held from K233; K235 docx Watch note acknowledged.** Use the continuous architectural-quality signal as a pre-commit gate blocking AI-generated PRs that degrade structure. Local, passive, doesn't execute untrusted code. K235 re-eval (docx): license claimed "NOT FOUND" — **false negative**; gh api + LICENSE both return MIT, matching the K233 claim. Docx tiered it Watch on immaturity/minimal docs and 6-month stale pushes; both fair Watch signals but they don't overturn the Extract call for a *passive* quality gate. Unbounded recursive feedback loops risk token burn if the sensor misfires — bound the loop. Needs verification: semantic validity of the score on highly modular dynamically-typed Python/TypeScript (built/tested primarily in Rust contexts).

[Sources: sentrux/sentrux (retrieved 2026-08-12); gh api 2026-08-13; Deep Research URL Evaluation.docx]
