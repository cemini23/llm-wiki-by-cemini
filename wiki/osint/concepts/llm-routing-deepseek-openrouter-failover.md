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
  - "@ccc-wiki/entities/tools/deepseek-harness.md"
  - "@ccc-wiki/entities/skills/super-audit.md"
  - "@ccc-wiki/entities/skills/free-audit.md"
  - "@gambling-wiki/concepts/poker-hl-analyst-loop.md"
  - concepts/agent-toolkit-routing-research-backlog.md
  - entities/tools/opencodex.md
  - entities/tools/opencode.md
  - entities/tools/reasonix.md
  - entities/tools/quotio.md
  - sources/arxiv-2608.11152-mixed-rl-rollouts-2026-08-12.md
  - sources/newsletter-latent-space-ainews-reasoning-trace-2026-08-12.md
  - sources/eval-github-repository-stack-2026-08-16.md
  - entities/tools/dshackle.md
  - entities/tools/dsh-vision-toolkit.md
  - sources/newsletter-rss-latent-space-2026-08-14-ainews-cursors-60b.md
  - sources/newsletter-rss-latent-space-2026-08-17-stripe-openrouter.md
  - sources/substack-rss-outlier-weekly-2026-08-18-cursor-route.md
  - entities/tools/cursor-route.md
maturity: draft
created: 2026-06-04
updated: 2026-08-17
---

## Relations

- @sources/newsletter-rss-latent-space-2026-08-01-ainews-deepseek-v4-flash-0731.md
- @concepts/api-credential-registry.md — `DEEPSEEK_*`, `OPENROUTER_*` variable names
- @concepts/mcp-context-optimization.md — Layer 2 claude-code-router (complementary)
- @ccc-wiki/entities/tools/agent-toolkit.md — private `/route` host (`ROUTE_KIT`)
- @ccc-wiki/entities/skills/route.md — federation `/route` skill v2.3.2
- @ccc-wiki/entities/tools/deepseek-harness.md — official `dsh` `/route` worker behind `claude-ds`
- @sources/eval-github-repository-stack-2026-08-16.md — K240 dsh ecosystem; do not replace `claude-ds`
- @entities/tools/dshackle.md — RPC proxy (name collision, not DSH)
- @entities/tools/dsh-vision-toolkit.md — Extract; do not replace PATH `claude-ds`
- @sources/newsletter-rss-latent-space-2026-08-14-ainews-cursors-60b.md — DSH-as-infrastructure talk
- @entities/infrastructure/deepseek-api.md — prod brain
- @ccc-wiki/concepts/llm-routing-deepseek-openrouter-failover.md — operator-facing CCC copy (same contract)
- @ccc-wiki/entities/skills/super-audit.md — API leg discovers `OPENROUTER_*` / `DEEPSEEK_*` / `ADVISOR_*` via `discover_api_keys.py`
- @ccc-wiki/entities/skills/free-audit.md — Grok-orchestrated free council uses same `OPENROUTER_*` / `DEEPSEEK_*` routing env
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — HL loop sources env at start
- @concepts/agent-toolkit-routing-research-backlog.md — K233 routing backlog (MISA-T/opencodex/Quotio)
- @entities/tools/opencodex.md — K233 GO Integrate provider proxy (consolidates this failover surface)
- @entities/tools/opencode.md — sst/OpenCode coding agent Phase-0; **not** opencodex; NO-GO `/route` swap
- @entities/tools/reasonix.md — DeepSeek-native CLI Phase-0; NO-GO `/route` swap
- @entities/tools/quotio.md — K233 quota-aware failover pattern
- @sources/arxiv-2608.11152-mixed-rl-rollouts-2026-08-12.md — MISA-T workload-aware admission
- @sources/newsletter-latent-space-ainews-reasoning-trace-2026-08-12.md — provider-proxy security surface

## Raw Concept

Shared laptop/prod contract when DeepSeek quota is exhausted: automatic retry on OpenRouter for `scripts/_llm_retry.py`, CeminiSuite `services/llm_analyst/deepseek_client.py`, and optional `ADVISOR_*` for world-cup-bot.

## Narrative

Canonical files: `config/llm-routing.env.example`, `scripts/llm_routing.py`, `scripts/install_llm_routing_env.sh`, `scripts/source_llm_routing_env.sh`.

**Install:** `bash scripts/install_llm_routing_env.sh` → `~/.cemini/llm-routing.env`

**Session:** `source scripts/source_llm_routing_env.sh`

Failover on HTTP 402/429 and quota/balance error strings. Disable with `LLM_FALLBACK_ENABLED=false`.

**`/route` script host (2026-08-08):** private `cemini23/agent-toolkit` (`ROUTE_KIT=~/Projects/agent-toolkit` laptop; `/opt/cemini/agent-toolkit` on prod/egress). TipDrop workspace-kit is redirect-only for route scripts. SIP + verify gates live in agent-toolkit `scripts/lib/`.

**Research improvement loop (2026-08-11):** OSINT digest cluster `cursor-route-harness` + active_topic `/route + agent-toolkit` steals failover / harness-evolution papers into CCC briefs. Standing backlog on `@ccc-wiki/entities/skills/route.md`. K231/K232 brief: CCC `briefs/2026-08-11_route-skill-k231-k232-steals.md`.

**claude-ds worker (2026-08-14 v2.3.2):** official DeepSeek Harness `dsh` (pin `install-dsh.ps1` → `~/.dsh-cemini`) behind PATH name `claude-ds`. Default `deepseek-v4-flash`; `-Model deepseek-v4-pro` is the **Grok CLI usage-out stand-in**. Always-approve = `DSH_PERMISSION_MODE=danger-full-access`. Isolated Claude Code **2.1.222** at `~/.deepseek-claude` is **fallback** (`CLAUDE_DS_FORCE_LEGACY=1`). OpenCode/Reasonix remain **NO-GO** as extra coding loops (`@ccc-wiki/entities/tools/deepseek-harness.md`).
