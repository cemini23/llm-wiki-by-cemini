---
title: "Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents"
type: source
tags: [arxiv, source, k270, agents, harness]
keywords: [k270, Growing-Harness, BrowseComp-Plus, WebArena-Verified]
related:
  - concepts/k270-harness-evolution-wave.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
read_status: skimmed
---

## Relations

- @concepts/k270-harness-evolution-wave.md

## Raw Concept

| Paper | arXiv:2609.26760 |
| File | `arxiv-2609.26760-grow-the-harness-not-the-context-from-strategy-f.pdf` |
| Location | `local inbox (archive blocked 2026-09-23): research to be indexed/arxiv-2609.26760-grow-the-harness-not-the-context-from-strategy-f.pdf` |
| Authors | Laizhen Li, Jiarui Li, Juanjuan Zhao, Kejiang Ye, Ye Li, Cheng-zhong Xu, Xitong Gao (Shenzhen Institutes of Advanced Technology, CAS; University of Chinese Academy of Sciences; Shenzhen University of Advanced Technology; University of Macau) |
| Retrieved | 2026-09-23 |
| Pages | 16 |
| Dual-ID | **OSINT K270** |
| sha256 | `511b4d701caa5b59a2950f831cf963bd23e031e6f8db6ee2228bb1294c92aae4` |

## Narrative

Standard LLM-agent harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. The paper asks whether task feedback can turn that recurring control into **reusable executable code**, while LLM calls stay reserved for task-specific semantic reasoning.

**Method — Growing Harness.** A failure-guided training paradigm learns the agent harness itself. It starts from a **strategy-free scaffold** that exposes fixed model and tool interfaces, but encodes no task-solving controller.

Three mechanisms drive it:

1. **Function-level execution traces** localize each failure to a bounded code surface.
2. **An optimizer** repairs a window of failures jointly.
3. **A success-first held-out gate** rolls back repair sequences that harm prior capability.

Accepted edits accumulate in one shared harness. The control structure emerges from task feedback rather than from context.

**Reported results.** Across BrowseComp-Plus and WebArena-Verified with three deployment models from **4B to 120B** parameters, Growing Harness achieves the highest mean success in **five of six** benchmark–model settings. It trails the best mean by **0.7 pp.** in the sixth. Relative to a Tool-Calling agent it reduces LLM calls by **76.0–91.8%** and deployed-agent inference cost by **74.4–98.6%**. On WebArena-Verified, success stays at **44.7–45.3%** across model scales, whereas Tool-Calling falls to **6.7%** with the 4B model.

**Cemini relevance:** harness-over-context pattern for CCC. **FILE only. 0 product Integrate GO. Do not swap `/route`. Never auto-evolve `.cursor/skills`.**
