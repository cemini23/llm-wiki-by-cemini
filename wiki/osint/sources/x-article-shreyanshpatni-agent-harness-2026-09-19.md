---
title: "How to Build a Custom Agent Harness (@shreyanshpatni_)"
type: source
tags: [source, k266, ccc, harness, seo]
keywords: [k266, agent harness, middleware, HITL, subagents, observability]
related:
  - concepts/k266-ccc-jev-x-wave.md
  - concepts/k266-seo-x-voice-wave.md
  - sources/x-article-0xmovez-jev-engineering-2026-09-19.md
  - sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
  - sources/x-article-borjafat-internal-linking-2026-09-19.md
maturity: draft
created: 2026-09-19
updated: 2026-09-19
read_status: read
---

## Relations

- @sources/x-article-borjafat-internal-linking-2026-09-19.md
- @concepts/k266-ccc-jev-x-wave.md
- @concepts/k266-seo-x-voice-wave.md
- @sources/x-article-0xmovez-jev-engineering-2026-09-19.md
- @sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md

## Raw Concept

| File | `x-article-shreyanshpatni-custom-agent-harness-2026-09-19.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/x-article-shreyanshpatni-custom-agent-harness-2026-09-19.md` |
| Retrieved | 2026-09-19 |
| Dual-ID | **OSINT K266** |
| Author | @shreyanshpatni_ — post id `2100650701143863584` |
| Kind | X Article — *How to Build a Custom Agent Harness* |
| Metrics | 52 likes · 89 bookmarks · 5,665 impressions (X MCP 2026-09-19) — weakest of the wave |
| sha256 | `5b194684c4925a9076eccae3d9a031d51c2b279d55fd8d666386cfd1aa999c65` |

## Narrative

Generic harness tutorial. **Little Jev content** — Jev is not named in the article. Value is the component checklist and the framework counts, not a new capability. **CCC FILE.** Weakest metrics in the wave (5,665 impressions), so steal structure only.

**Core frame.** `Agent = Model + Harness`. The model provides inference; the harness supplies scaffolding that connects the model to the real world.

**Three core modules.** (1) **LLM module** — model selection, system prompts, message history, structured outputs, streaming, token usage, retries and fallbacks. Keep the model interface separate so providers can be swapped. (2) **Tools module** — file ops, web search, database, code execution, API calls, browser actions, internal systems, data analysis. Prefer MCP-style tools for interoperability. (3) **Agent loop** — connects the two and decides continue / stop / retry / ask for help.

**Production additions.** Context management, tool limits, retry logic, human approval, memory, subagents, cost controls, observability, safety checks.

**The discipline points that match Cemini practice.**

- Keep the system prompt minimal. Put deterministic behaviour in code: permission checks in code, approval gates in middleware, external actions in tools, counters and progress in state, prompts only for flexible reasoning.
- One middleware component, one concern. Hook points: before/after model calls, before/after tool calls, startup, shutdown, streamed output.
- Add observability from day one: agent-level, model-level, and tool-level events.
- Build a small evaluation set — simple tool calls, multi-step reasoning, missing information, tool errors, long conversations, ambiguous instructions, sensitive actions, verification tasks. A small repeatable set beats a large suite you never run.
- Expand gradually: skills, memory, subagents, planning, cost controls, guardrails.

**Framework counts (the stealable detail).** Minimal agent primitive plus middleware customization: **LangChain `create_agent`** — model, tools, system prompt, middleware architecture. More opinionated, batteries-included options: **Deep Agents** and the **Claude Agent SDK**. The trade-off stated plainly: build from scratch to understand the foundations, use a framework to accelerate, customize the harness when generic agents do not fit.

**Five-stage path.** Stage 1 minimal loop → Stage 2 reliability (errors, retries, validation, step limits, evaluations) → Stage 3 context (summarization, memory, task state) → Stage 4 control (permissions, human approval, cost limits, model routing, guardrails) → Stage 5 specialization (skills, subagents, domain tools, custom workflows).

**Cemini reading.** FILE. The component list is a checklist for harness evaluation, not a new wire. **No harness rewrite. No unattended autonomy.** Good structural exemplar for Cemini23 voice; see `@briefs/2026-09-19_k266-seo-voice.md`.

## Snippets

> "Agent = Model + Harness. The model handles inference. The harness provides the scaffolding that connects the model to the real world." [Source: x-article-shreyanshpatni-custom-agent-harness-2026-09-19.md]

> "A common mistake is trying to solve every problem inside the system prompt. ... Put deterministic behavior in code when possible." [Source: x-article-shreyanshpatni-custom-agent-harness-2026-09-19.md]

> "A small, repeatable evaluation set is often more useful than a complicated test suite you never run." [Source: x-article-shreyanshpatni-custom-agent-harness-2026-09-19.md]

> "The model provides intelligence. The harness turns that intelligence into useful work." [Source: x-article-shreyanshpatni-custom-agent-harness-2026-09-19.md]
