---
title: "Do LLM agents execute the plans they declare? (2609.38108)"
type: source
tags: [source, k276, agents, planning, harness]
keywords: [k276, plan-declaration, execution-gap, routing, FILE]
related:
  - concepts/k276-harness-evolution-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-harness-evolution-wave.md

## Raw Concept

| File | `arxiv-2609.38108-do-llm-agents-execute-the-plans-they-declare-fro.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.38108-do-llm-agents-execute-the-plans-they-declare-fro.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `dbc766c3d2c10db704388a506aa5d67162474c28880bc217112124ceaefd4c1e` |
| arXiv | 2609.38108 |
| Authors | Subba Reddy Oota, Francisco Herrera, Jordi Cabot Sagrera, Marcos Lopez de Prado, Shadab Khan |

## Narrative

The paper separates two capabilities that final task success hides: choosing a good plan, and executing the chosen plan faithfully. A run can fail at either stage, and the score cannot tell you which.

The authors define a Plan Declaration-Execution Gap. Their method, planning-as-routing, makes the model declare one of four planning modes: Predefined, Sequential, Hierarchical, or Search. A deterministic router then sends the task to a pattern-specific executor.

Three results. First, a generic plan-plus-ReAct loop fails to preserve the declared structure: only 22% to 45% of trajectories keep it, across three benchmarks. The pattern-specific executors enforce the structure. Second, the best planning mode depends on the environment and on the model: Search wins on ALFWorld, Hierarchical on SWE-bench. Third, the largest gain comes from execution, not selection: pattern-specific executors lift task success from 0.48 to 0.92 on ALFWorld and from 0.36 to 0.44 on SWE-bench Verified.

The authors admit that current models do not reliably pick the strongest mode for a task. Few-shot examples help in some combinations only.

Marcos Lopez de Prado is a co-author. The design claim transfers to our own harness: declare the pattern, then route to an executor that enforces it. We already do a form of this with `/route`. The paper is a name and a pattern. No code URL found. No clone. Do not swap `/route`.
