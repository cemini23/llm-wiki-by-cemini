---
title: "LangChain — Building a Harness with Jev (@sydneyrunkle)"
type: source
tags: [source, k266, ccc, jev, langchain, harness]
keywords: [k266, Jev, System One, TypeSafeClassifier, langchain-typesafe, AutoModeMiddleware, model routing]
related:
  - concepts/k266-ccc-jev-x-wave.md
  - concepts/k266-ood-stub-wave.md
  - entities/tools/jev-mcp.md
  - entities/tools/langchain-typesafe.md
  - sources/x-article-0xmovez-jev-engineering-2026-09-19.md
  - sources/x-article-shreyanshpatni-agent-harness-2026-09-19.md
  - sources/x-post-parcadei-jev-skill-classify-2026-09-19.md
maturity: draft
created: 2026-09-19
updated: 2026-09-19
read_status: read
---

## Relations

- @sources/x-post-parcadei-jev-skill-classify-2026-09-19.md
- @sources/x-article-shreyanshpatni-agent-harness-2026-09-19.md
- @concepts/k266-ccc-jev-x-wave.md
- @concepts/k266-ood-stub-wave.md
- @entities/tools/jev-mcp.md
- @entities/tools/langchain-typesafe.md
- @sources/x-article-0xmovez-jev-engineering-2026-09-19.md

## Raw Concept

| File | `x-article-sydneyrunkle-building-a-harness-with-jev-2026-09-19.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/x-article-sydneyrunkle-building-a-harness-with-jev-2026-09-19.md` |
| Retrieved | 2026-09-19 |
| Dual-ID | **OSINT K266** |
| Author | @sydneyrunkle (LangChain) — post id `2100754364545761643` |
| Kind | X Article — *Building a Harness with Jev* |
| Metrics | 4,141 likes · 9,390 bookmarks · 1,221,679 impressions (X MCP 2026-09-19) |
| sha256 | `b7df8b84b262f3f68108a6d0fccf6e3a2e4f9bb14f5c51679a7e1f236a182169` |

## Narrative

Best-performing Jev long-form of the wave: **1.22M impressions / 9,390 bookmarks**. LangChain's own framing of where a decision model sits inside an agent loop. **CCC FILE. Do not swap `/route`.**

**What Jev is.** Not an LLM — it does not generate text. TypeSafe calls it a **System One** model: evaluate a state, return typed answers and probabilities. Trained with reinforcement learning for calibrated decisions (RLCD). This is the same System One framing already on `@entities/tools/jev-mcp.md` and in the K265 clone wave.

**Three question types** (matches the K265/K264 record):

| Type | Answer shape |
|------|--------------|
| **Choice** | Pick from a set of options. Returns a probability per option plus overall confidence. |
| **Score** | Rate against ordered levels. Returns a continuous score, distribution, confidence. |
| **Noul** | Yes/no. Returns P(statement is true). |

Parallel questions: every question in a request is evaluated at once. Adding questions barely changes response time and costs only the extra question tokens. Questions cannot read each other's answers.

**LangChain integration.** Provider-agnostic model layer exposes Jev through **`TypeSafeClassifier`** via the `langchain-typesafe` package. Pass state plus questions to `.invoke()`, get classification results rather than a chat response. State can be text, structured data, or LangChain messages — so a node, tool, or middleware hook can call Jev with context the agent already holds. Key env var `TYPESAFE_API_KEY`.

**Use cases named in the post.**

1. **Model routing middleware** — Jev assesses the request and picks the model from criteria you define. Router selects from the latest user message and holds that choice for the run. Probabilities and confidence stay in agent state.
2. **Auto Mode** — `AutoModeMiddleware` uses Jev to check tool calls for risky decisions and **blocks the call before the tool executes**. The post's argument: Claude / Codex / Cursor already ship a dangerous-action classifier, but that step is locked inside closed source. A cheap classifier model lets every agent adopt the same pattern.

**Cited third-party builders** (vendor-side list, single source — do not treat as verified): Kyle Jeong (Browserbase) powering browser-use agents for fractions of a cent; Jarrod Watts a **live trading agent**; Ryan Vogel email triage at scale.

**Cemini reading.** FILE only. Two concrete borrows for CCC: the AutoMode gate is a **claim-ledger / tool-call gate** pattern for GuruWatcher, and model-routing middleware is a candidate at the `/route` boundary — but **do not swap `/route`**. **No unattended browser-use. No live trading agent.** The Jarrod Watts example is a named live trading agent and stays out of scope.

## Snippets

> "Jev is actually not a traditional LLM, it doesn't generate text. It's what the TypeSafe AI team calls a System One model: A System One model evaluates a state and returns typed answers and probabilities." [Source: x-article-sydneyrunkle-building-a-harness-with-jev-2026-09-19.md]

> "AutoModeMiddleware uses Jev to check tool calls for risky decisions it may take, and block calls before the tool executes." [Source: x-article-sydneyrunkle-building-a-harness-with-jev-2026-09-19.md]

> "System One models evaluate every question in a request in parallel. Adding questions barely changes the response time and costs only the tokens for the extra questions, which are cheap." [Source: x-article-sydneyrunkle-building-a-harness-with-jev-2026-09-19.md]

> "The company reports up to 200x faster inference and 400x lower cost than comparable LLMs on classification tasks." [Source: x-article-sydneyrunkle-building-a-harness-with-jev-2026-09-19.md] — vendor claim, not measured here.
