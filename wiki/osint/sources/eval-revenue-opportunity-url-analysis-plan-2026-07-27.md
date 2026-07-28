---
title: "Revenue Opportunity URL Analysis Plan (OpenCLI / local infer) — 2026-07-27"
type: source
tags: [source, tool-eval, k197, revenue, atto]
keywords: [OpenCLI, openclicky, claude-video, youtube-mcp, Qwen3.6, NVFP4]
related:
  - sources/eval-revenue-opportunity-url-analysis-2026-07-27.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/gpuology-genealogy-agent-kit.md
  - entities/tools/opencli.md
  - entities/tools/openclicky.md
  - entities/tools/qiaomu-opencli-skills.md
  - entities/tools/youtube-mcp-cli.md
  - entities/tools/claude-video.md
maturity: draft
read_status: read
created: 2026-07-27
updated: 2026-07-27
clusters: [k197-ingest]
---

## Relations

- @sources/eval-revenue-opportunity-url-analysis-2026-07-27.md — same-day infra batch
- @concepts/wiki-tooling-evaluation.md
- @concepts/gpuology-genealogy-agent-kit.md
- @entities/tools/opencli.md
- @entities/tools/openclicky.md
- @entities/tools/qiaomu-opencli-skills.md
- @entities/tools/youtube-mcp-cli.md
- @entities/tools/claude-video.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Filename** | `Revenue Opportunity URL Analysis Plan.docx` |
| **sha256** | `6a73998b722dd3a2f6d1f7cd63fc09a26d228b2eb42c065ae8332bc74415c80b` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Revenue Opportunity URL Analysis Plan.docx` |
| **License spot-check** | `.local/reports/license-spot-check-2026-07-27-0846.txt` |
| **Theme** | Zero-cost web automation, high-fidelity local inference, visual OSINT |

## Narrative

20-URL plan-style eval (OpenCLI cluster + Qwen local + video OSINT).

| Eval tier | Repo | Verified license | Operator action |
|-----------|------|------------------|-----------------|
| **Integrate** | jackwener/OpenCLI | Apache-2.0 `[CONFIRMED]` | Phase-0 → Atto authenticated portal CLI |
| **Integrate** | bradautomates/claude-video | MIT `[CONFIRMED]` | Refresh K148 entity — TipDrop chart/video OSINT |
| ~~Integrate~~ → **Watch** | MiaAI-Lab/Qwen3.6-27B-NVFP4-vLLM | **null** SPDX | No adopt until LICENSE |
| ~~Integrate~~ → **UNAVAILABLE** | unsloth/Qwen3.6-27B-GGUF (Q4/Q6/Q8) | **404** | Eval dead links — Pass |
| **Extract** | jasonkneen/openclicky | MIT | Atto desktop UI patterns |
| **Extract** | joeseesun/qiaomu-opencli-skills | MIT | TipDrop social scrape skills |
| **Extract** | umbertotancorre/youtube-mcp-cli | MIT | TipDrop transcript MCP |
| **Watch** | opencli-admin (NOASSERTION), GeoLibre | — | Docker/ROI blockers |
| **Pass** | OpenCLIPP, openclinic, js-openclient, spectre.console | — | Aggregated — **no stub farm** |

**Eval gap note:** OpenCLI/YouTube heavy → TipDrop still weak on native Discord/Telegram real-time ingest (engineering priority, not a new Integrate).

## Snippets

> "Make Any Website into CLI & Use your logged-in browser by AI agent." — OpenCLI pitch; pair with K195 ego-lite session isolation.
