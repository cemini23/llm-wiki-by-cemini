---
title: Bun (oven-sh)
type: entity
tags: [tool, javascript, runtime, k157, watch]
keywords: [segfault, Zig, test runner, stability]
related:
  - sources/eval-multi-wiki-link-evaluation-genealogy-agent-2026-07-10.md
maturity: draft
created: 2026-07-10
updated: 2026-07-10
---

## Relations

- @sources/eval-multi-wiki-link-evaluation-genealogy-agent-2026-07-10.md — K157 Watch

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [oven-sh/bun](https://github.com/oven-sh/bun) |
| **License** | Eval claims MIT; GitHub API `NOASSERTION` SPDX [NEEDS VERIFICATION 2026-07-10] |
| **Verdict** | **Watch** — performance upside blocked by runtime stability (segfaults, GC panics, non-AVX2) |
| **Routing** | wiki-only; **no** TipDrop prod until issue volume drops |

~94k★ JS runtime/bundler/test runner. Unacceptable incident risk for revenue bots per K157 eval — monitor only.

## Snippets

> "pervasive reports of segmentation faults, garbage collection panics" [Source: eval docx URL 1]
