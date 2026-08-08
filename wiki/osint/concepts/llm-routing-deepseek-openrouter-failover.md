---
title: LLM routing — DeepSeek primary, OpenRouter failover
type: concept
tags: [concept, llm, deepseek, openrouter, routing, failover, infrastructure]
keywords: [llm-routing, openrouter, deepseek, failover, llm_analyst, brain, skill_audit]
related:
  - sources/newsletter-rss-latent-space-2026-08-01-ainews-deepseek-v4-flash-0731.md
  - concepts/api-credential-registry.md
  - concepts/mcp-context-optimization.md
  - entities/infrastructure/deepseek-api.md
  - entities/tools/claude-code-router.md
  - "@ccc-wiki/concepts/llm-routing-deepseek-openrouter-failover.md"
  - "@ccc-wiki/entities/tools/agent-toolkit.md"
  - "@ccc-wiki/entities/skills/route.md"
  - "@ccc-wiki/entities/skills/super-audit.md"
  - "@ccc-wiki/entities/skills/free-audit.md"
  - "@gambling-wiki/concepts/poker-hl-analyst-loop.md"
maturity: draft
created: 2026-06-04
updated: 2026-08-08
---

## Relations

- @sources/newsletter-rss-latent-space-2026-08-01-ainews-deepseek-v4-flash-0731.md
- @concepts/api-credential-registry.md — `DEEPSEEK_*`, `OPENROUTER_*` variable names
- @concepts/mcp-context-optimization.md — Layer 2 claude-code-router (complementary)
- @ccc-wiki/entities/tools/agent-toolkit.md — private `/route` host (`ROUTE_KIT`)
- @ccc-wiki/entities/skills/route.md — federation `/route` skill v2.1
- @entities/infrastructure/deepseek-api.md — prod brain
- @ccc-wiki/concepts/llm-routing-deepseek-openrouter-failover.md — operator-facing CCC copy (same contract)
- @ccc-wiki/entities/skills/super-audit.md — API leg discovers `OPENROUTER_*` / `DEEPSEEK_*` / `ADVISOR_*` via `discover_api_keys.py`
- @ccc-wiki/entities/skills/free-audit.md — Grok-orchestrated free council uses same `OPENROUTER_*` / `DEEPSEEK_*` routing env
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — HL loop sources env at start

## Raw Concept

Shared laptop/prod contract when DeepSeek quota is exhausted: automatic retry on OpenRouter for `scripts/_llm_retry.py`, CeminiSuite `services/llm_analyst/deepseek_client.py`, and optional `ADVISOR_*` for world-cup-bot.

## Narrative

Canonical files: `config/llm-routing.env.example`, `scripts/llm_routing.py`, `scripts/install_llm_routing_env.sh`, `scripts/source_llm_routing_env.sh`.

**Install:** `bash scripts/install_llm_routing_env.sh` → `~/.cemini/llm-routing.env`

**Session:** `source scripts/source_llm_routing_env.sh`

Failover on HTTP 402/429 and quota/balance error strings. Disable with `LLM_FALLBACK_ENABLED=false`.

**`/route` script host (2026-08-08):** private `cemini23/agent-toolkit` (`ROUTE_KIT=~/Projects/agent-toolkit` laptop; `/opt/cemini/agent-toolkit` on prod/egress). TipDrop workspace-kit is redirect-only for route scripts. SIP + verify gates live in agent-toolkit `scripts/lib/`.
