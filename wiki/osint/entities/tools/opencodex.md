---
title: Opencodex — universal provider proxy for Codex/Claude Code
type: entity
tags: [entity, tool, provider-proxy, mit, ccc-fit, k233]
keywords: [opencodex, provider-proxy, codex, claude-code, gemini, grok, deepseek, model-routing]
related:
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 20-URL eval, Integrate tier
- @concepts/agent-toolkit-routing-research-backlog.md
- @concepts/llm-routing-deepseek-openrouter-failover.md

## Raw Concept

Repo `lidge-jun/opencodex`. MIT, 9,505★, ~93MB (asset-heavy; 175MB depth-1 clone), very active (pushed 2026-08-12). TypeScript/Bun local proxy. Translates OpenAI Codex Responses API ↔ Anthropic, Gemini, Grok, GLM, DeepSeek, Kimi, Qwen, Ollama (and any OpenAI-compatible endpoint), with streaming, tool calls, reasoning tokens, images both directions. Works with Codex CLI/App/SDK, Claude Code, Claude Desktop, and Grok Build. Dashboard on `localhost:10100`; ChatGPT account-pooling with quota refresh, sessions pinned to starting account; history-safe on unclean shutdown.

## Narrative

**Verdict: GO Integrate (CCC).** Directly attacks vendor lock-in across the agent harnesses this workspace actually uses (Claude Code + Codex + Grok lanes). Two concrete uses:

1. **Cross-provider delegation** — route heavy-context work (e.g. GEDCOM parsing) to a large-context model and cheap local fast-iteration to a small model, without changing IDE config.
2. **DeepSeek/OpenRouter failover consolidation** — supersedes the ad-hoc llm-routing failover with a single proxy surface that also covers Grok/Codex CLI lanes.

Risk: proxy subject to undocumented upstream schema changes (Anthropic/OpenAI deprecations); "history-safe injection" needs verification on forced shutdown. Do not route secrets/PII (Atto) through it until the audit-trail surface is understood. Keep the underlying models' own auth isolated (account-pooling touches credentials by design — restrict to lab/CCC contexts, not Atto fixtures).

[Source: lidge-jun/opencodex README (retrieved 2026-08-12)]
