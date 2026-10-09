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
updated: 2026-10-09
wire_status: runtime_wired
wire_target: wiki-only
wire_note: "CLI rapid-mlx 0.16.0. Venv .local/tools/rapid-mlx/.venv. Symlink ~/.local/bin/rapid-mlx. Telemetry off. No model pull (13 GB free). No settings edit. No serve."
---

## Relations

- @sources/eval-github-repository-revenue-2026-10-08.md — K285 eval (tier: **Integrate**)
- @concepts/k285-eval-wave.md — K285 cluster hub
- @entities/tools/strata.md — the K284 local-inference sibling

## Raw Concept

- **Repo:** `github.com/raullenchai/Rapid-MLX`
- **Tier (K285):** **Integrate** (route: Atto; local lab)
- **License:** **Apache-2.0** `[CONFIRMED]` 2026-10-08. The `LICENSE` file reads "Licensed under the Apache License, Version 2.0". GitHub's API reports the `license` field as `NOASSERTION` / `other` only because its detector could not match the file (a `NOTICE` file is present). **The licence itself is Apache-2.0.**
- **Stars:** 3,941 (verified 2026-10-08), active
- **Description:** "OpenAI/Anthropic-compatible LLM inference server for Apple Silicon on MLX"

## Narrative

A drop-in **MLX inference server** for Apple Silicon that exposes an **OpenAI/Anthropic-compatible endpoint on localhost**.

### Why it matters here

Same lane as **`Strata`** (K284): keep at-risk work **entirely local** — no cloud call, no token cost. Because the endpoint is OpenAI/Anthropic-shaped, existing agent code points at it with **no code change**. The eval's play: zero-PII local parsing for Atto's Italian civil-record work.

**Two local-inference workers in two waves** (`Strata` K284, `Rapid-MLX` K285) make the local-inference lane the wiki's most consistently-recurring Integrate.

### Constraints

- **Apple Silicon + MLX-quantized weights** required.
- ✅ **Licence confirmed Apache-2.0** (2026-10-08) — clean to wire.

### Boundary

The CLI is installed. Package `rapid-mlx` 0.16.0 (Apache-2.0). The venv is `.local/tools/rapid-mlx/.venv`. The symlink is `~/.local/bin/rapid-mlx`. Doctor on 2026-10-09: Apple M4, 16 GB RAM, 13 GB free disk. That is too low for a model pull. Telemetry was on by default and is now off. No model was pulled. No settings file was edited. `rapid-mlx launch` was not run. The server is not running. **No client PII to any cloud endpoint.** GitHub's API still reports the licence field as NOASSERTION. The LICENSE file is Apache-2.0.

## Snippets

> "Rapid-MLX — OpenAI/Anthropic-compatible LLM inference server for Apple Silicon on MLX." [Source: eval-github-repository-revenue-2026-10-08.md, Phase-0 verified]
