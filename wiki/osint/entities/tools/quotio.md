---
title: Quotio — macOS multi-provider LLM quota proxy
type: entity
tags: [entity, tool, api-proxy, macos, mit, ccc-fit, k233]
keywords: [quotio, quota-tracking, auto-failover, macos-menu-bar, llm-proxy, rate-limit]
related:
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 eval, Extract tier
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept

Repo `nguyenphutrong/quotio`. MIT (gh api resolved; docx claimed NOT FOUND), ~4.6k★. Native macOS menu-bar app unifying Claude/Gemini/OpenAI/Qwen subscriptions with real-time quota tracking + smart auto-failover for Claude Code, OpenCode, Droid. CLIProxyAPI architecture with round-robin / fill-first routing on rate-limit/cool-down.

## Narrative

**Verdict: GO Extract (CCC).** Pattern steal for the llm-routing failover lane: quota-aware round-robin/fill-first cascading between providers prevents silent workflow stalls during token-heavy sessions. **Do not route Atto PII through unverified fallback endpoints.** Business risk: third-party unsigned macOS app; verify appcast/Sparkle auto-update surface before any production-adjacent use. Extract the routing/quota logic, not the binary.

[Source: nguyenphutrong/quotio (retrieved 2026-08-12)]
