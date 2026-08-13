---
title: OpenCode — sst/anomalyco coding agent (not opencodex)
type: entity
tags: [entity, tool, coding-agent, deepseek, mit, phase0]
keywords: [opencode, sst/opencode, anomalyco, claude-ds, name-collision]
related:
  - entities/tools/opencodex.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - entities/infrastructure/deepseek-api.md
  - entities/tools/reasonix.md
  - "@ccc-wiki/entities/tools/opencode.md"
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @ccc-wiki/entities/tools/opencode.md — **canon Phase-0** (MIT, CONDITIONAL-GO reference only; NO-GO PATH and `/route` swap)
- @entities/tools/opencodex.md — **different repo** (`lidge-jun/opencodex` provider proxy, K233)
- @entities/tools/reasonix.md — sibling DeepSeek-native CLI Phase-0
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @concepts/agent-toolkit-routing-research-backlog.md
- @entities/infrastructure/deepseek-api.md

## Raw Concept

2026-08-12 claude-ds refresh. Evaluated OpenCode as a DeepSeek-API coding harness vs isolated Claude Code.

## Narrative

**Verdict: NO-GO for `/route` mid.** Keep updated `claude-ds` (Claude Code 2.1.222 + `deepseek-v4-flash`). OpenCode can run headless (`opencode run --auto`) against `DEEPSEEK_API_KEY`, but it is a different protocol (OpenAI-compat, not Anthropic `/anthropic`), has no PromptFile, and the README first-install is `curl | bash`. Full audit: `@ccc-wiki/entities/tools/opencode.md`.
