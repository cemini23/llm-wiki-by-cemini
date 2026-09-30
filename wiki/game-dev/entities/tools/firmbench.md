---
title: FirmBench / EnterpriseBench — strategic decision-making agent bench
type: entity
tags: [entity, tool, benchmark, harness, phase-0]
keywords: [firmbench, enterprisebench, beer-game, delayed-feedback, apache-2.0]
related:
  - sources/arxiv-2609.37658-enterprisebench-strategic-agents-2026-09-30.md
  - entities/tools/gamedevbench.md
  - concepts/agent-harness-castle-project.md
  - sources/inbox-arxiv-reject-batch-2026-09-30.md
maturity: validated
created: 2026-09-30
updated: 2026-09-30
wire_status: deferred
wire_target: concepts/agent-harness-castle-project.md
---

## Relations

- Paper: [arXiv:2609.37658](https://arxiv.org/abs/2609.37658)
- GitHub: [sduyangmin/FirmBench](https://github.com/sduyangmin/FirmBench)

## Raw Concept

Benchmark for LLM agents on enterprise-level strategic reasoning and decision-making, with three interactive settings. The **Beer Game** setting is a supply-chain simulation with delayed feedback — the part relevant to a castle sim.

## Narrative

### Phase-0 verdict (2026-09-30)

| Check | Result |
|-------|--------|
| SPDX / LICENSE | **Apache-2.0** (`LICENSE.txt` at repo root) |
| Verdict | **CONDITIONAL-GO** — clone permitted; not adopted now |

### castle-sim mapping

| EnterpriseBench idea | castle-sim use |
|----------------------|----------------|
| Beer Game delayed feedback | Design lens for Stronghold 2 storage + production chains |
| Capability + difficulty annotation | Tagging scheme for W2 story difficulty |
| Nine-agent × four-backbone grid | **Skip** — too large for a solo project |

The useful transfer is conceptual, not operational. The delayed-feedback loop explains why an order placed now shows its effect several ticks later, which is the same oscillation problem a granary or bread chain can produce.

## Dead Ends

- Running the full eval grid in a hobby project.
- Treating enterprise QA scores as evidence about lord AI.
