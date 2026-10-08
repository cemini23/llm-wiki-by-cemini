---
title: "Rapid-MLX — local Apple Silicon inference server"
type: entity
tags: [tool, local-inference, mlx, apple-silicon, atto, k285]
keywords: [rapid-mlx, mlx, apple-silicon, local-inference, openai-endpoint, anthropic-endpoint, k285]
related:
  - sources/eval-github-repository-revenue-2026-10-08.md
  - concepts/k285-eval-wave.md
  - entities/tools/strata.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- @sources/eval-github-repository-revenue-2026-10-08.md — K285 eval (tier: **Integrate**)
- @concepts/k285-eval-wave.md — K285 cluster hub
- @entities/tools/strata.md — the K284 local-inference sibling

## Raw Concept

- **Repo:** `github.com/raullenchai/Rapid-MLX`
- **Tier (K285):** **Integrate** (route: Atto; local lab)
- **License:** ⚠ **NOASSERTION** at the API level; the description claims **Apache-2.0**. Treat as unverified.
- **Stars:** 3,941 (verified 2026-10-08), active
- **Description:** "OpenAI/Anthropic-compatible LLM inference server for Apple Silicon on MLX"

## Narrative

A drop-in **MLX inference server** for Apple Silicon that exposes an **OpenAI/Anthropic-compatible endpoint on localhost**.

### Why it matters here

Same lane as **`Strata`** (K284): keep at-risk work **entirely local** — no cloud call, no token cost. Because the endpoint is OpenAI/Anthropic-shaped, existing agent code points at it with **no code change**. The eval's play: zero-PII local parsing for Atto's Italian civil-record work.

**Two local-inference workers in two waves** (`Strata` K284, `Rapid-MLX` K285) make the local-inference lane the wiki's most consistently-recurring Integrate.

### Constraints

- **Apple Silicon + MLX-quantized weights** required.
- ⚠ **Confirm the licence** before wiring — the API reports NOASSERTION.

### Boundary

FILE only. **No client PII to any cloud endpoint.** Human-gated; no install.

## Snippets

> "Rapid-MLX — OpenAI/Anthropic-compatible LLM inference server for Apple Silicon on MLX." [Source: eval-github-repository-revenue-2026-10-08.md, Phase-0 verified]
