---
title: "ag-ui — event protocol between an agent and a front end (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - entities/tools/plannotator.md
updated: 2026-11-16
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md, URL 2,
**Extract** tier. Routed to Atto.

The question this page answers: **how does an agent tell a user interface what it is
doing, without the interface polling it?**

## Narrative

### What it does

AG-UI is a wire protocol, not a framework. It defines a typed event stream between an
agent backend and any front end:

- **State deltas** — the agent publishes changes to shared state; the UI applies them
  incrementally instead of refetching.
- **Lifecycle events** — run start, step, finish, and error.
- **Human-in-the-loop interrupts** — the agent stops and asks for approval, and the
  answer returns on the same channel.
- **Transport-agnostic** — Server-Sent Events, WebSockets, or plain HTTP.

Two implementations ship: `@ag-ui/core` in TypeScript and `ag-ui-protocol` in Python.
The repository also holds reference middleware for the three transports.

### Why it fits Atto

Atto already has a human-gate truth workflow and an Access share tier. What it does not
have is a standard way to say "the agent is waiting for your decision" across
`atto-mcp` and the portal UI. Phase-0 on 2026-11-16 found no `text/event-stream` or
`EventSource` usage anywhere under `atto/apps` or `atto/docs`. [CONFIRMED]

That is the gap: the approval-gate event contract. AG-UI supplies it as a schema, so
Atto can emit conformant events without adopting the whole SDK.

The same contract serves Collectibles high-value grading and consignment triage, where
an operator must approve before a manifest commits.

### Where the cost sits

Adopting the full SDK would mean a new dependency and a new protocol in the portal.
Extracting only the event schema costs a document and a small emitter, and keeps the
option open. The freeze blocks installing the SDK as a server regardless.

### Status

**SHIPPED in Atto — `b31dae4` (2026-11-24).** The event contract is implemented in both
languages:

- `apps/desktop/src-tauri/src/ipc/agui.rs` and `apps/desktop/src/ipc/agui.ts`
- a v1 envelope with **14 closed event types**, `deny_unknown_fields`, and a **64 KiB
  cap**
- a `domain: "agent"` truth boundary, so event payloads cannot claim to be truth
- local Tauri transport `atto-agui` plus `to_sse`
- shared round-trip and rejection fixtures at `fixtures/agui/events.json`
- `docs/AGUI_EVENTS.md`

We took the schema, not the SDK. That is exactly what the freeze allowed, and the
result is a typed interrupt contract with no new dependency.

## Snippets

> Standardizing bi-directional state deltas and human-in-the-loop interrupt events
> between `atto-mcp` and the Atto portal UI.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 2]

## Dead Ends

- **Adopting the SDK to get the schema.** The schema is the value; the runtime is a new
  dependency the freeze does not allow.
