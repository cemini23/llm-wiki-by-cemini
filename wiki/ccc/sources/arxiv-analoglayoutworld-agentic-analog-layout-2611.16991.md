---
title: "AnalogLayoutWorld — 91.1% of attempts produce GDS, 21.3% pass acceptance"
type: source
related:
  - concepts/generation-verification-gap-agent-artifacts.md
  - entities/tools/analoglayoutworld.md
  - concepts/harness-as-eval-artifact.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AnalogLayoutWorld: An Open Benchmark for Agentic Analog Layout Design |
| Author | Nova-Silicon Team |
| Type | arXiv preprint, 2611.16991; preprint, 2026-11 |
| Location | `research to be indexed/ccc/arxiv-2611.16991-analoglayoutworld-an-open-benchmark-for-agentic.pdf` |
| Retrieved | 2026-11-14 |
| Pages | 19 |
| Read status | read |

## Narrative

AnalogLayoutWorld tests whether coding agents can do **long-horizon engineering under physical constraints**. The task is analog circuit layout. The agent receives a fixed transistor-level netlist, specifications, and a process design kit. It must construct, place, and route a layout, then refine it from verification feedback.

The benchmark has 40 expert-reviewed tasks. It ships an integrated design environment and independent checks: design-rule checking (DRC), layout-versus-schematic (LVS), parasitic extraction (PEX), and post-layout simulation. Layout-quality metrics were co-designed with analog layout experts. The score combines submission and physical verification, compactness, engineering quality, and electrical verification.

Results across 13 model–harness configurations show a wide **generation-to-verification gap**:

- 91.1% of attempts produce a GDS layout.
- Only 21.3% satisfy all acceptance criteria.
- The internal Novara agent system scores highest at 0.8154 and passes acceptance on 72.5% of attempts.
- DeepSeek V4 Pro on Claude Code reaches 23.3% DRC and 3.3% acceptance.

Two analyses matter beyond analog design. First, device count predicts difficulty: final score correlates negatively with circuit size (Spearman rho = −0.73 across six configurations). Second, the prescribed tests are not the whole quality bar. In one LDO example, both submissions pass DRC, LVS, and all electrical cases. A via-current check still separates them: 10 via3 cuts carry 4.8 mA against a 30 mA load, where at least 63 cuts are needed. The check gives a physical reason for the score difference that functional tests miss.

The authors conclude that test-time scaling helps, but gains shrink under a fixed budget. Reasoning efficiency and the use of verification feedback decide how quality holds as tasks grow.

## Snippets

> "Across 13 model–harness configurations, 91.1% of attempts produce GDS layouts, but only 21.3% satisfy the benchmark's acceptance criteria." [Source: arxiv-2611.16991-analoglayoutworld-an-open-benchmark-for-agentic.pdf p.1]

> "The via-capacity check supplies a physical basis for a quality distinction that the prescribed functional tests do not expose." [Source: arxiv-2611.16991-analoglayoutworld-an-open-benchmark-for-agentic.pdf p.10]
