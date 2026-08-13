---
title: Quotio — macOS multi-provider LLM quota proxy
type: entity
tags: [entity, tool, api-proxy, macos, mit, ccc-fit, k233]
keywords: [quotio, quota-tracking, auto-failover, macos-menu-bar, llm-proxy, rate-limit]
related:
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - sources/deep-research-url-evaluation-2026-08-13.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-12
updated: 2026-08-13
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 eval, Extract tier
- @sources/deep-research-url-evaluation-2026-08-13.md — K235 eval: upgraded to Integrate (CCC)
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept

Repo `nguyenphutrong/quotio`. **MIT verified** (gh api 2026-08-13), ~4.7k★, pushed 2026-08-13 (active). Native macOS menu-bar app unifying Claude/Gemini/OpenAI/Qwen subscriptions with real-time quota tracking + smart auto-failover for Claude Code, OpenCode, Droid. CLIProxyAPI architecture with round-robin / fill-first routing on rate-limit/cool-down. Cloned `.local/adopts/quotio` (165M, under 500 MB threshold).

## Narrative

**Verdict: GO Integrate (CCC) — upgraded from K233 Extract.** Pattern steal for the llm-routing failover lane: quota-aware round-robin/fill-first cascading between providers prevents silent workflow stalls during token-heavy sessions (Atto extraction runs, GuruWatcher alert parsing). **Do not route Atto PII through unverified fallback endpoints.** Business risks carried: third-party unsigned macOS app (verify appcast/Sparkle auto-update surface); local proxy = single point of failure + potential PII logging (audit before production-adjacent use); CLIProxyAPI translation layer may drop advanced parameters on complex system prompts with pre-filled assistant responses (unverified). Extract the routing/quota logic, not the binary.

[Sources: nguyenphutrong/quotio (retrieved 2026-08-12); gh api 2026-08-13; Deep Research URL Evaluation.docx]
