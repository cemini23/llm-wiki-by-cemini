---
title: "Agent runtime tooling, November 2026 — SRE, tenant isolation, and prompt-enforced boundaries"
type: concept
related:
  - "@osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - concepts/agent-verification-patterns.md
updated: 2026-11-24
maturity: draft
---

## Raw Concept

Six URLs in the 2026-11-24 batch are agent runtime or harness tools, all capped at
Context. The question this page answers: **which of their patterns are worth copying
into our own rules?**

Source: @osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md.

## Narrative

### The set

| Tool | Licence | The idea it encodes |
|------|---------|---------------------|
| `opensre` | Apache-2.0 | Separate **CI-caused** from **code-caused** failures, and link every conclusion to evidence |
| `nakama` | **none** | Per-agent tenant isolation, STRIDE threat model, rotating `NAKAMA_SECRETS_KEY_NEXT` |
| `CoreCoder` | **none** | A compact coding-agent loop, readable in one sitting |
| `gemini-api-cli` | **none** | Official experimental CLI ergonomics |
| `book-to-skill` | **none** | PDF/EPUB/web → Markdown → structured reference distillation |
| `watch-mcp` | **none** | Storyboard token budgeting for video input |

Two of six have no licence. `watch-mcp`'s budgeting scheme is described below in our own
words and is not copied text.

### The strongest idea — from `opensre`

An SRE agent's most expensive failure is misattribution: a build that failed for an
infrastructure reason is reported as a code defect, and an engineer spends an afternoon
on it.

The useful rule is a **two-bucket triage with evidence attached to each verdict**:
before blaming the diff, state what the CI environment did. A flake, a runner image
change, and a dependency fetch failure are all distinguishable, and recording which one
happened is cheaper than re-running blind.

That is the same discipline as the pre-read expectation model in
@concepts/agent-verification-patterns.md, pointed at CI.

### Tenant isolation — from `nakama`

The rotation scheme is the transferable part: a `*_NEXT` secret variable allows a new
key to be deployed and validated before the old one is retired. Applied to any
multi-tenant agent, it removes the window where a rotation locks out live sessions.

Useful for the operator lab and for any agent that holds per-user credentials. Not
useful for a single-operator laptop.

### Token budgeting for video — from `watch-mcp`

Video frame selection has a hard budget, and it is small: Claude Code's MCP output
ceiling is 25,000 tokens. Frames are the largest cost.

The scheme worth keeping: a **default of 4 storyboards at roughly 8.5k image tokens**,
and a maximum of 128 keyframes across 8 storyboards at roughly 17k tokens. Sparse
keyframes plus a storyboard summary beats uniform sampling, because uniform sampling
spends the budget on the boring middle of a clip.

### What this cluster says

Six tools, six Contexts, zero adoptions. Two lack a licence entirely. The wiki's role
is the same as in every batch since the freeze began: record the mechanism, write it
into `AGENTS.md` or `CLAUDE.md`, install nothing.

## Snippets

> Separation of CI-caused vs code-caused failures and evidence-linked audit design.
> [Source: Multi-Wiki Link Revenue Evaluation.docx, URL 5]

> Default 4 storyboards / ~8.5k image tokens; max 128 keyframes across 8 storyboards /
> ~17k tokens under Claude Code's 25,000-token MCP ceiling.
> [Source: Multi-Wiki Link Revenue Evaluation.docx, URL 18]

## Dead Ends

- **Copying from `CoreCoder`, `nakama`, `gemini-api-cli`, `book-to-skill`, or
  `watch-mcp`.** No licence on any of them.
- **Uniform frame sampling for video.** It spends the budget on the boring middle.
