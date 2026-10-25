---
title: PrismML Bonsai-demo (1-bit / ternary local LLM)
type: entity
tags: [tool, local-llm, xsp, k168, extract]
keywords: [Bonsai, PrismML, ternary, llama.cpp prism, Apache-2.0]
related:
  - sources/eval-github-repo-revenue-evaluation-2026-07-15.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-15
updated: 2026-07-15
---

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [PrismML-Eng/Bonsai-demo](https://github.com/PrismML-Eng/Bonsai-demo) |
| **License** | Apache-2.0 (~1.3k★; ~2MB git size) |
| **Verdict** | **Extract patterns** — local low-bit inference hedge for XSP/CCC brief eval; not prod trading critical path |
| **NV** | Metal/CUDA footprint + parallel request limits for 256k context [OPEN QUESTION 2026-07-15] |

Steal quantization / Metal-CUDA alignment notes. Do not drop-in replace cloud models without hardware budget.
