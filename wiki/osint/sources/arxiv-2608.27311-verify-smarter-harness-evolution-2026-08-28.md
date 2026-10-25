---
title: "Verify Smarter / HarnessLens — behavior-aware harness verification (arXiv 2608.27311, CCC K313 sibling)"
type: source
tags: [arxiv, k248, harness, ccc, k313]
keywords: [HarnessLens, Verify-Smarter, harness-evolution, behavior-aware-verification]
related:
  - concepts/k248-agent-harness-wave.md
  - sources/arxiv-2608.24804-starharness-2026-08-26.md
  - entities/tools/starharness.md
  - sources/arxiv-2608.25593-jit-agent-2026-08-29.md
maturity: draft
created: 2026-08-28
updated: 2026-10-25
read_status: read
---

## Relations

- @concepts/k248-agent-harness-wave.md — K248 harness cluster
- @sources/arxiv-2608.24804-starharness-2026-08-26.md — StarHarness stratified evolution sibling (CCC K313)
- @entities/tools/starharness.md — existing MIT REFERENCE entity

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.27311, Verify Smarter, Evolve Further: Efficient Harness Evolution with Behavior-Aware Verification |
| Retrieved | 2026-08-28 |
| File | `arxiv-2608.27311-verify-smarter-evolve-further-efficient-harness.pdf` |
| sha256 | `120feb7d4e2c67efc743fc5d3284c3ad4451bb8770d6f171927ae1f1ae88cb27` |
| Repo | https://github.com/jhxu5214/HarnessLens |
| Dual-ID | **OSINT K248** + **CCC K313 sibling** to StarHarness 24804 (HarnessLens / Verify Smarter) |

## Narrative

Verify Smarter introduces **HarnessLens**-style **behavior-aware verification** for harness evolution: accept changes when behavior metrics improve, not only when pass rates move. Reported **+7.6–13.6%** on held-out tasks. This is a CCC **K313 sibling** to StarHarness (arXiv 2608.24804) — same federation lane (harness evolution with frozen weights), different verification discipline. Policy: REFERENCE awareness only; do not auto-evolve `.cursor/skills`; do not swap `/route`. Pair StarHarness stratification with HarnessLens behavior checks before any Phase-0 clone.

## Snippets

> "HarnessLens behavior-aware verification; +7.6–13.6% held-out." [Source: arxiv-2608.27311-verify-smarter-evolve-further-efficient-harness.pdf (retrieved 2026-08-28)]

> "Repo: https://github.com/jhxu5214/HarnessLens" [Source: same]
