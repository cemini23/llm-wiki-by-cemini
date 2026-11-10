---
title: "jevals — decision-model guardrails that run fully offline on Apple Silicon"
type: entity
tags: [tool, guardrails, evals, pii, atto, local, mit]
keywords: [jevals, jev, laya, kev, groundedness, yaml gate, presidio, pii, toolchoice]
related:
  - sources/eval-multi-wiki-link-evaluation-2026-11-10.md
  - entities/tools/jeveryword.md
  - entities/tools/ontosmith.md
maturity: draft
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-evaluation-2026-11-10.md, URL 9, **Extract** tier. Routed to Atto, Collectibles, and CeminiParlays.

The question this page answers: **can a guardrail judge run on this machine, with no key and no network?**

## Narrative

### What it is

A Python library from OpenLayer. It runs agent evals and guardrails using **Jev-style decision models instead of an LLM judge**, bundles every check for a single trace into **one request**, and returns **calibrated probabilities**.

Coverage:

- **Agent behaviour** — tool choice, grounding, scope.
- **Security** — injection, PII/PHI, secrets.
- **RAG metrics** — Ragas-style.
- **Gates** — allow, escalate, or block a tool call.

Ships a CLI and an MCP server. **MIT.**

### Phase-0, 2026-11-10 — the correction that makes it usable here

The report presented this as a metered service: Jev at **$0.042 per million input tokens**, "a fraction of a cent per trace". That framing made it a cloud dependency and therefore a ban-4 problem for Atto.

The README says something more useful:

> It "Runs locally with Kev or Laya."

| Backend | Where it runs | Key needed |
|---------|---------------|------------|
| **Laya** | **in-process on Apple Silicon, fully offline** | none |
| **Kev** | self-hosted — `python -m kev.serve --run jaredpalmer/kev-4b` on a 32 GB Mac | none |
| Eikos | your own GPU | none |
| Jev (hosted) | TypeSafe or Vercel AI Gateway | `TYPESAFE_API_KEY` / `AI_GATEWAY_API_KEY` |
| Emulated chat LLM | any provider | their key — "slower, costs more" |

**Laya is the one that matters.** In-process, offline, no key. A guardrail that never sends a record anywhere is the only kind Atto can run against vault material — which is exactly the constraint that has blocked every hosted judge so far.

### The gate shape

```yaml
allow_if:   <condition>
block_if:   <condition>
escalate:   <condition>
```

Three outcomes, and **escalate is the important one**. A binary allow/block forces a judgement on ambiguous input; an escalate path sends it to a human, which is the shape Atto's `truth.ged` gate already has.

Plus `Grounded()` for claim-citation checks and `ToolChoice()` for tool-call validation.

### The family it belongs to

`jevals`, `ontosmith` (which uses Jev as its decision model), and `JEV-Paper-Radar` all orbit the same TypeSafe primitive. The workspace already has `TYPESAFE_API_KEY`, and `jeveryword` — catalogued 2026-11-02 and rejected for Atto because its model was remote — is the same family.

**jevals is the first member of that family with a documented offline path.** That changes the verdict on the family, not just the tool.

### Status

Extract, **Laya backend only** for anything touching private data. Verify the offline path actually runs before depending on it.

## Snippets

> "Runs locally with Kev or Laya." Laya runs in-process on Apple Silicon and is fully offline. [fetched 2026-11-10]

> Kev is self-hosted: "`python -m kev.serve --run jaredpalmer/kev-4b` on a 32GB Mac." [fetched 2026-11-10]

> The repository is "MIT." [fetched 2026-11-10]

## Dead Ends

- **Using the hosted Jev backend for Atto.** It is a cloud call; Laya is the offline path.
- **Assuming the family is cloud-only because jeveryword was.** jevals documents a local backend.
