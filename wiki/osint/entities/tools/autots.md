---
title: "AutoTS — automated time-series forecasting (Adopt, Cemini analyst-node)"
type: entity
tags: [tool, time-series, forecasting, financial-prediction, mcp-compatible, scikit-learn, gemini-eval-doc1, phase-0-adopt-candidate]
keywords: [autots, automated forecasting, m6 competition, scikit-learn, mcp, winedarksea, analyst-node, prediction-layer]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
gemini_eval_doc1_url: 9
phase_0_verdict: ADOPT-CANDIDATE 2026-05-12 (highest-confidence Cemini-prod adopt from Doc 1)
adoption_status: PRE-PHASE-0 2026-05-12
---

## Relations

- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — source eval (URL 9)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — corrected multi-wiki prompt
- `@concepts/tool-evaluation-framework.md` — three-surface methodology
- `@concepts/cemini-license-posture.md` — MIT-clean license posture

## Raw Concept

- **Repo**: `github.com/winedarksea/AutoTS`
- **License** [per Gemini eval]: MIT — `[NEEDS VERIFICATION 2026-05-12]` confirm via `gh api repos/winedarksea/AutoTS --jq '.license.spdx_id'`
- **Stars** [per Gemini eval]: ~1,400
- **Tier**: Adopt
- **Primary fit**: Cemini financial (analyst-node prediction layer)

## Narrative

Automated time-series forecasting library; per Gemini eval won the M6 2023 financial-forecasting competition (`[NEEDS VERIFICATION 2026-05-12]`). MCP-compatible with scikit-learn API idioms. Direct integration target for Cemini's analyst-node prediction layer.

### Integration vector

Schedule Phase-0 audit (license verification, runtime resource profile, MCP server compatibility check against existing FastMCP container hardening from K39 OpenShell extraction). If clean: file Cemini-prod adoption brief with concrete `agents/orchestrator.py` integration plan.

### Open questions

- Resource footprint (RAM + CPU per forecast batch) vs Cemini analyst-node budget
- MCP compatibility tier (full MCP server vs callable-from-MCP-container)
- M6 placement claim verification — important if cited externally
