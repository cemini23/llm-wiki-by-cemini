---
title: "AirLLM"
type: entity
tags: [tool, k173]
keywords: [airllm]
related:
  - sources/eval-revenue-opportunity-url-evaluation-2026-07-18.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/polymarket-bot-architecture.md
maturity: draft
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- @sources/eval-revenue-opportunity-url-evaluation-2026-07-18.md
- @concepts/wiki-tooling-evaluation.md

## Narrative

| Field | Value |
|-------|-------|
| **Repo / docs** | lyogavin/airllm |
| **License** | Apache-2.0 (~5MB) |
| **Verdict** | **Extract** |
| **Routing** | TipDrop / **David PC** for weights; Mac = smoke only |

Layer-wise inference to run large models on limited VRAM. **Weights host = David's PC** (disk/GPU). OSINT Mac keeps clone + import smoke only.

## Wired (K173 local)

- Venv: `.local/venvs/airllm` + `mlx` on Apple silicon; import smoke OK
- Smoke: `bash scripts/run_airllm_smoke.sh`
- **Weights:** do **not** download on Mac — TipDrop brief `2026-07-18_k173-david-pc-model-weights.md`

