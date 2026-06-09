---
title: "AARRI-bench — research-intern agent eval suite"
type: entity
tags: [entity, tool, benchmark, agent-evaluation, reject, k107]
keywords: [aarri-bench, aarr, no-license, phase-0-nogo, research-ethics-benchmark]
related:
  - sources/arxiv-aarri-research-intern-bench-2606-07462-2026-06-09.md
  - concepts/conductor-orchestrator.md
  - concepts/wiki-tooling-evaluation.md
  - "@ccc-wiki/briefs/2026-06-09_k107-ccc-dynamic-workflows-skills-from-osint.md"
maturity: draft
created: 2026-06-09
updated: 2026-06-09
---

## Relations

- @sources/arxiv-aarri-research-intern-bench-2606-07462-2026-06-09.md — paper + benchmark description
- @concepts/wiki-tooling-evaluation.md — Phase-0 registry
- @concepts/conductor-orchestrator.md — harness eval target

## Raw Concept

GitHub: https://github.com/AARR-bench/AARRI-bench — data for arXiv 2606.07462.

## Narrative

**Phase-0 audit (2026-06-09): NO-GO**

| Signal | Value |
|--------|-------|
| License | **None** (`gh api` `.license` null; `/license` 404) |
| Stars | ~2 |
| Last push | 2026-06-09 |
| Maturity | Brand-new benchmark drop |

**Verdict:** **REFERENCE** rubric only — track paper/tasks; do not install or vendor until SPDX license appears. Re-run `gh api repos/AARR-bench/AARRI-bench` before any adoption.

**Steal-from (no install):** task categories emphasizing research ethics + field sensitivity — extend CCC/conductor eval smoke matrix beyond GTFA coding tasks.

## Snippets

> "Developing researcher-like AI requires further exploration of research behavior, rather than merely complex scaffolding." [Source: arxiv-2606-07462 Abstract]
