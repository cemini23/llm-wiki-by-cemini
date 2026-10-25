---
title: "Strata — local 125B-MoE inference on consumer hardware"
type: entity
tags: [tool, local-inference, moe, mit, k284, local-abliterated-lab]
keywords: [strata, 125b, moe, qwen3.8, local-inference, nvme, openai-endpoint, air-gapped, k284]
related:
  - sources/eval-url-revenue-opportunity-2026-10-07.md
  - concepts/k284-eval-wave.md
  - entities/tools/rapid-mlx.md
maturity: draft
created: 2026-10-07
updated: 2026-10-25
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-10-07.md — K284 eval (tier: **Integrate**)
- @concepts/k284-eval-wave.md — K284 cluster hub

## Raw Concept

- **Repo:** `github.com/Niko1221/Strata`
- **Tier (K284):** **Integrate** (route: local abliterated lab; Atto air-gapped parsing)
- **License:** **MIT** (verified 2026-10-07)
- **Stars:** **16,491** (verified), active, pushed 2026-10-07
- **Description:** "Qwen3.8-Flash-Next on any consumer hardware; Strata inference engine, OpenAI/Anthropic API on localhost"

## Narrative

A local inference engine that runs a **125B-parameter MoE** model on consumer hardware — cited at a gaming GPU + 64 GB RAM. It exposes a **localhost OpenAI/Anthropic-compatible endpoint**, so existing agent code points at it with no cloud call.

### Why it matters here

For the **local abliterated lab** and for **Atto air-gapped parsing**, this removes the trade-off between expensive cloud APIs and weak local models: frontier-grade local reasoning with **zero token cost** and strict data confinement. A candidate for the private Latin/genealogical parsing work.

### Constraints (from the eval)

- **First load locks 35–55 GB of system RAM** and needs a fast **NVMe SSD** for n-gram table paging.
- RAM/VRAM footprint means it competes with other local workloads.
- Authorized-pentest scope applies for any security-lab use.

### Boundary

FILE only — no install this session. Verify the hardware fit before committing. **No client PII to any cloud endpoint**; this tool is specifically the local path.

## Snippets

> "Strata … Initial load locks 35 to 55 GB of system RAM and requires fast NVMe SSD storage for low-latency n-gram lookup table paging." [Source: eval-url-revenue-opportunity-2026-10-07.md]
