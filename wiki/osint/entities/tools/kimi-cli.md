---
title: "Kimi CLI (Moonshot)"
type: entity
tags: [tool, k173]
keywords: [kimi-cli]
related:
  - sources/eval-revenue-opportunity-url-evaluation-2026-07-18.md
  - concepts/wiki-tooling-evaluation.md
  - sources/newsletter-rss-latent-space-2026-07-17-kimi-k3.md
  - concepts/agent-setup-instruction-supply-chain.md
  - concepts/coding-agent-substrate-steerability.md
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
| **Repo / docs** | MoonshotAI/kimi-cli |
| **License** | Apache-2.0 (~25MB) |
| **Verdict** | **Extract** |
| **Routing** | CCC |

Official Moonshot CLI for Kimi models. Mac = **API CLI** after login. **K3 open weights (when shipped) → David's PC**, not OSINT laptop.

## Wired (K173 local)

- Binary: `~/.local/bin/kimi` via `uv tool install`
- Wrapper: `scripts/run_kimi_cli.sh`
- **Operator (Mac):** `kimi` then `/login` (API only)
- **Weights:** David PC if/when K3 weights are adopted — TipDrop brief `2026-07-18_k173-david-pc-model-weights.md`

