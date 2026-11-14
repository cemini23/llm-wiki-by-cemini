---
title: AnalogLayoutWorld — open benchmark for agentic analog layout
type: entity
related:
  - sources/arxiv-analoglayoutworld-agentic-analog-layout-2611.16991.md
  - concepts/generation-verification-gap-agent-artifacts.md
  - concepts/harness-as-eval-artifact.md
updated: 2026-11-14
---

## Raw Concept

What prompted this page: the 2026-11-14 ingest of AnalogLayoutWorld (2611.16991). The benchmark is a concrete example of physical-constraint grading for coding agents, so it gets a page for future reference.

## Narrative

| Field | Value |
|-------|-------|
| Owner | Nova-Silicon Team |
| Tasks | 40, expert-reviewed |
| Input | fixed transistor-level netlist, specifications, process design kit |
| Output | GDS layout |
| Checks | DRC, LVS, PEX, post-layout simulation, layout-quality metrics |
| Process kits named | SKY130, SG13G2 |
| Open source | benchmark repository announced as "open-sourced soon" at preprint time [NEEDS VERIFICATION 2026-11-14] |

The scoring model is worth reusing. A task score combines five parts: submission, physical verification gate, compactness against a target area ratio, engineering quality (device matching, critical-net routing, power delivery), and the verified fraction of an electrical test manifest. Partial credit needs verified progress, and full acceptance needs every check plus complete evidence.

The benchmark ships an internal system, **Novara**, which scores 0.8154 and passes acceptance on 72.5% of attempts. That is far above the best external configuration in the paper. Any comparison should treat the internal system as a strong reference point, not as a neutral entry.

The negative result is the durable one. 91.1% of attempts produce a layout, and 21.3% meet acceptance. A coding agent can make the artifact. It struggles to prove the artifact is correct.

Cemini has no analog-design work. The page is a reference for benchmark design: gate on evidence, keep a separate quality axis, and hold a hidden check that the prescribed tests do not cover.

## Snippets

> "Our benchmark repository will be open-sourced soon." [Source: arxiv-2611.16991-analoglayoutworld-an-open-benchmark-for-agentic.pdf p.1]

> "we introduce AnalogLayoutWorld, an open-source agent benchmark with 40 expert-reviewed tasks for end-to-end layout generation from fixed transistor-level netlists" [Source: arxiv-2611.16991-analoglayoutworld-an-open-benchmark-for-agentic.pdf p.1]
