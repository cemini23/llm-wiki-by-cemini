---
title: langchain-typesafe — LangChain Jev integration (FILE)
type: entity
tags: [tool, k266, ccc, jev, langchain]
keywords: [langchain-typesafe, TypeSafeClassifier, AutoModeMiddleware, TYPESAFE_API_KEY, model routing]
related:
  - concepts/k266-ccc-jev-x-wave.md
  - sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
  - entities/tools/jev-mcp.md
maturity: draft
created: 2026-09-19
updated: 2026-09-19
phase_0_verdict: FILE REFERENCE
harness_verb: FILE
wire_status: wont_wire
wire_note: FILE only. No clone. No product Integrate. Live laptop path stays jev-mcp. Do not swap /route.
---

## Relations

- @concepts/k266-ccc-jev-x-wave.md
- @sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
- @entities/tools/jev-mcp.md

## Raw Concept

K266 stub. Surfaced by the LangChain X Article *Building a Harness with Jev* (@sydneyrunkle). **No Phase-0 clone for K266.**

## Narrative

| Field | Value |
|-------|-------|
| **Package** | `langchain-typesafe` |
| **Owner** | LangChain / TypeSafe AI |
| **Class** | `TypeSafeClassifier` |
| **Env key** | `TYPESAFE_API_KEY` |
| **Source** | @sydneyrunkle X Article 2026-09-19 (`2100754364545761643`) |
| **Verdict** | **FILE REFERENCE. `wont_wire`. No clone. 0 product Integrate GO.** |

Provider-agnostic LangChain model layer that exposes Jev through `TypeSafeClassifier`. Pass state plus questions to `.invoke()` and receive classification results rather than a chat response. State may be text, structured data, or LangChain messages, so a node, tool, or middleware hook can call Jev with context the agent already holds.

**Two patterns named in the source article.**

- **Model-routing middleware** — Jev assesses the request and selects the model from criteria you define; the choice is held for the run and the probabilities stay in agent state.
- **`AutoModeMiddleware`** — Jev checks tool calls for risky decisions and blocks calls before the tool executes. This is the same position as a coding harness's closed-source dangerous-action classifier.

**Why FILE and not WIRE.** The Cemini laptop path is **jev-mcp** (TypeSafe MCP server, tools `jev_verify` / `jev_screen` / `jev_find`). Adding a second Jev integration in a different runtime framework duplicates the exit path without adding a new decision capability. No clone, no install, no Phase-0 clone this wave. The two named patterns are recorded as candidate **HITL experiments** only. **Do not swap `/route`.** Do not copy LangChain or Jev skills into `~/.cursor/skills`.

Read-only reference: https://github.com/langchain-ai (repo path not verified this wave — no gh api call made).
