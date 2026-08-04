---
title: "URL Revenue Opportunity Analysis (2026-07-22)"
type: source
tags: [tool-evaluation, revenue, k182, docx, xsp, tipdrop, atto]
keywords: [outlines, cloudflare-temp-email, omlx, likec4, worldmonitor, pi-web, gigatoken]
related:
  - entities/tools/outlines.md
  - entities/tools/cloudflare-temp-email.md
  - entities/tools/omlx.md
  - entities/tools/likec4.md
  - entities/tools/pi-web.md
  - entities/tools/gigatoken.md
  - entities/tools/worldmonitor.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/active-project-research-routing.md
  - sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md
maturity: draft
read_status: read
created: 2026-07-22
updated: 2026-08-03
clusters: [k182-ingest, wiki-tooling]
---

## Relations

- @sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md — K220 cyber/agent-harness revenue eval

- @entities/tools/outlines.md — **Integrate** Apache-2.0 (XSP/TipDrop structured output)
- @entities/tools/cloudflare-temp-email.md — **Integrate** MIT (Atto portal verify)
- @entities/tools/omlx.md — **Integrate** Apache-2.0 (Atto local LLM)
- @entities/tools/likec4.md — **Extract** MIT (CCC arch-as-code)
- @entities/tools/pi-web.md — **Extract** MIT (CCC agent UI)
- @entities/tools/gigatoken.md — **Extract** MIT (tokenizer benches)
- @entities/tools/worldmonitor.md — **Watch** AGPL — not product Integrate
- @concepts/wiki-tooling-evaluation.md
- @concepts/active-project-research-routing.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | URL Revenue Opportunity Analysis |
| **URLs** | 20 |
| **sha256** | `645e48e5e7f24815b50c685f9762aa746d85fe4f72957a8d3a02e238d170c0a6` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/URL Revenue Opportunity Analysis.docx` |
| **License report** | `.local/reports/license-spot-check-2026-07-22.txt` |
| **Phase-0** | `.local/reports/k182-phase0-2026-07-22.md` · `scripts/adopt_k182_phase0.sh` |
| **Theme** | OSINT ingest + local LLM + infra for XSP / TipDrop / Atto |

## Narrative

Gemini v10 revenue-first batch. Eval claimed **Integrate** worldmonitor — **overridden** to Watch after LICENSE = AGPL-3.0.

| Tier | Items |
|------|-------|
| **Integrate (3)** | `dottxt-ai/outlines` (Apache-2.0); `dreamhunter2333/cloudflare_temp_email` (MIT); `jundot/omlx` (Apache-2.0) |
| **Extract (3)** | `likec4/likec4` (MIT); `agegr/pi-web` (MIT); `marcelroed/gigatoken` (MIT) |
| **Watch** | openship (Apache); buzz.xyz SaaS; HF Laguna; **worldmonitor AGPL** |
| **Context** | RuView; Tess/GLM HF; PrismML llama.cpp fork; VulnLLM-R |
| **Pass / UNAVAILABLE** | LibreYOLO; languagemodelbuilder.com; blaze-bpe UNAVAILABLE |
| **NO weights** | Agents-A1-NVFP4; Qwen uncensored HF — no download |

Local adopts under `.local/adopts/` ≈ **279MB** (ex-worldmonitor) << 500MB.
