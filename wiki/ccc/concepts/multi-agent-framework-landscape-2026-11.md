---
title: "Multi-agent framework landscape, November 2026 — why none of them fit"
type: concept
related:
  - "@osint-wiki/sources/2026-11-26-deep-research-batch-audit.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - "@osint-wiki/entities/tools/letta-memgpt.md"
  - concepts/subagent-orchestration.md
updated: 2026-11-26
---

## Raw Concept

Five orchestration and memory frameworks were graded in the 2026-11-26 batch: `crewAI`,
`smolagents`, `agno`, `letta`, and `autogen`, plus `magnitude` as a Watch item. The
question this page answers: **is a framework the right way to run several agents here?**

Source: @osint-wiki/sources/2026-11-26-deep-research-batch-audit.md.

## Narrative

### The five, and the verdict

| Framework | Licence | Shape | Tier |
|-----------|---------|-------|------|
| `crewAI` | MIT | Role-playing agent crews | Context |
| `smolagents` | Apache-2.0 | Minimal code-writing agents | Context |
| `agno` | Apache-2.0 | Postgres-backed agent control plane | Context |
| `letta` | Apache-2.0 | Stateful agents with a Git-backed MemFS | Context |
| `autogen` | MIT | Conversational multi-agent | Pass |
| `magnitude` | Apache-2.0 | Local inference server | Watch |

None earned adoption. The reasons differ, and together they describe the boundary.

### The three disqualifiers

**1. Deterministic beats role-play.** Every Priority #1 project already does the thing
a crew would do, in code that can be tested. Collectibles resolves an identity with a
match gate that returns one of three outcomes — not a debate between a "researcher"
agent and a "critic" agent. A crew adds latency and non-determinism to a decision that
is already specified.

**2. The dependency cost is real and asymmetric.** Collectibles is Python 3.12
stdlib-only. Atto is a local vault plus MCP. FlavorOrigins is an Astro static site.
seo-pulse is Python, SQLite, and launchd. GuruWatcher is a 15-minute timer. A framework
that wants Postgres — `agno` — is not a library for those projects; it is a new service.

**3. The orchestration we need already exists.** There is a subagent harness with
worktree isolation, and an owned-lab planner plus executor split. See
@concepts/subagent-orchestration.md. A second orchestration layer would duplicate it.

### What is worth taking

**From `letta`** — the Git-backed MemFS idea. Agent memory as a versioned file tree,
where every write is a commit with a diff you can read and revert. Not the service;
the shape. @osint-wiki/entities/tools/letta-memgpt.md holds the earlier evaluation.

**From `smolagents`** — the minimal loop. An agent that writes and runs a small piece
of code, checks the result, then stops, is easier to reason about than one that plans
five steps. Useful as a control when comparing against a heavier harness.

**From `magnitude`** — Watch only. Vendor benchmarks report 1.32x prefill and 2.19x
decode over Ollama defaults on M4 Pro hardware, but the instability reported in the
batch prevents replacing llama.cpp or RunPod vLLM. Revisit when it stabilises; measure
with the harness from
@ccc-wiki/entities/tools/inference-optimisation-skill.md rather than the vendor number.

### The boundary rule

Adopt a framework when the orchestration **is** the product. Do not adopt one when the
orchestration is a wrapper around decisions the project has already specified.

## Snippets

> Every Priority #1–#3 pipeline benefits from deterministic code or direct MCP/stdlib
> calls rather than role-playing LLM crews.
> [Source: Cemini Multi-Wiki Batch Audit.docx, URL 5]

> Git-backed MemFS architecture is CCC wiki reference taxonomy only.
> [Source: Cemini Multi-Wiki Batch Audit.docx, URL 10]

## Dead Ends

- **A Postgres control plane for a 15-minute cron job.** The service outlives the need.
- **A crew where a tested function already returns the answer.**
