---
title: "Agent harness tooling, November 2026 — four Context-grade items and what they encode"
type: concept
related:
  - "@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - concepts/repeated-correction-mining.md
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Four URLs in the 2026-11-22 batch are coding-agent harness tools, all capped at Context
by the Workstation Harness Freeze. The question this page answers: **what do they
encode that survives without installing them?**

Source: @osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md.

## Narrative

### The four

| Tool | What it is | Tier |
|------|-----------|------|
| `topjohnwu/agy-gyro` v0.2.3 | Android tooling release; agent-adjacent CLI | Context |
| `diggerhq/opencomputer` | Open computer-use harness for agents | Context |
| `googlecolab/google-colab-cli` | Official Colab CLI — drive a remote notebook from a terminal | Context |
| `aicodewith-team/pi-superagent` | Pi harness superagent scaffold | Context |

All four are harness components. Under Gate 3 none may be wired into this workstation,
and none is a runtime component of Atto, Collectibles, or game-time, so none can escape
the cap by shipping inside a product.

### The one with a real second use

**`google-colab-cli`** is the exception worth noting. It is not only an agent tool — it
is a way to run a GPU job from a terminal without a local GPU. For Collectibles, that
is a different path to the same capability Inkling 2 Mini provides locally: a rented
T4 on a free or paid Colab tier instead of a RunPod worker.

It does not beat the local model on privacy — the images still leave the machine — but
it is a cheaper fallback than a dedicated RunPod deployment, and it competes on cost
for the workloads that exceed a 20 GB local model.

### What the cluster says about the freeze

Four harness tools in one batch, all capped, is a pattern rather than a coincidence.
The supply of coding-harness tooling is large and growing; almost none of it can be
adopted. The wiki's role becomes recording the *pattern* each one encodes so the idea
can be reimplemented in the project's own rules rather than installed.

That is the same conclusion as @concepts/repeated-correction-mining.md: read for the
mechanism, write the mechanism into `AGENTS.md` or `CLAUDE.md`, install nothing.

### What to take

- **From `opencomputer`** — the containment question: what does the agent see, and what
  can it touch. Relevant when the operator lab exists.
- **From `colab-cli`** — a terminal-drivable GPU session as a cheap fallback to a local
  VLM.
- **From `pi-superagent`** — the scaffold shape of a harness superagent, useful as a
  comparison against `subagent-orchestration.md`.

## Snippets

> Batch theme: ... coding-agent harnesses and linters.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, research plan]

## Dead Ends

- **Installing any of the four during the freeze.** Gate 3 applies to all harness tools
  regardless of quality.
- **Expecting a harness tool to beat a product-level gap.** It cannot ship inside a
  product, so it cannot lift its own cap.
