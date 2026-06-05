---
title: LLM routing — DeepSeek primary, OpenRouter failover
type: concept
tags: [concept, llm, deepseek, openrouter, routing, failover, infrastructure]
keywords: [llm-routing, openrouter, deepseek, failover, llm_analyst, brain, skill_audit]
related:
  - concepts/api-credential-registry.md
  - concepts/mcp-context-optimization.md
  - entities/infrastructure/deepseek-api.md
  - entities/tools/claude-code-router.md
  - "@ccc-wiki/concepts/llm-routing-deepseek-openrouter-failover.md"
  - "@gambling-wiki/concepts/poker-hl-analyst-loop.md"
maturity: draft
created: 2026-06-04
updated: 2026-06-04
---

## Relations

- @concepts/api-credential-registry.md — `DEEPSEEK_*`, `OPENROUTER_*` variable names
- @concepts/mcp-context-optimization.md — Layer 2 claude-code-router (complementary)
- @entities/infrastructure/deepseek-api.md — prod brain
- @ccc-wiki/concepts/llm-routing-deepseek-openrouter-failover.md — operator-facing CCC copy (same contract)
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — HL loop sources env at start

## Raw Concept

Shared laptop/prod contract when DeepSeek quota is exhausted: automatic retry on OpenRouter for `scripts/_llm_retry.py`, CeminiSuite `services/llm_analyst/deepseek_client.py`, and optional `ADVISOR_*` for world-cup-bot.

## Narrative

Canonical files: `config/llm-routing.env.example`, `scripts/llm_routing.py`, `scripts/install_llm_routing_env.sh`, `scripts/source_llm_routing_env.sh`.

**Install:** `bash scripts/install_llm_routing_env.sh` → `~/.cemini/llm-routing.env`

**Session:** `source scripts/source_llm_routing_env.sh`

Failover on HTTP 402/429 and quota/balance error strings. Disable with `LLM_FALLBACK_ENABLED=false`.
