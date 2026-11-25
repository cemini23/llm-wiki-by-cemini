---
title: "plannotator — human review gate for agent plans and diffs (Apache-2.0)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - entities/tools/ag-ui.md
updated: 2026-11-16
maturity: draft
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md, URL 3,
**Integrate** tier. Routed to CCC and game-dev; reference for Atto.

The question this page answers: **where does a human stop an agent before the change
lands, without leaving the workspace?**

## Narrative

### What it does

Plannotator is a browser review layer between an agent and its work. It intercepts
three things and holds them for annotation:

- **plans** — on `exit_plan_mode`, before any edit runs
- **HTML artifacts** — rendered for comment
- **diffs** — line comments that return to the agent

It supports Claude Code, Codex, Pi, and OpenCode, and returns annotations to the agent
through a CLI hook. A review **Inbox** lets several agents queue work for one human
sitting.

### The sharing model

The interesting part is the zero-knowledge share. A small markdown review compresses
into the URL fragment, and larger payloads are AES-256-GCM encrypted client-side with
the key kept **in the fragment**. The server stores ciphertext it cannot read. A
`PLANNOTATOR_SHARE=disabled` switch blocks external upload entirely.

That is the pattern worth taking, not the tool.

### Phase-0, 2026-11-16

| Check | Result |
|-------|--------|
| Licence | Apache-2.0 [CONFIRMED — GitHub API] |
| Maturity | 12.5k stars, pushed the day of the check, 186 open issues |
| Cloud requirement | None for local review; share is opt-in and can be disabled |
| Local gap | Atto ships human-gate truth and Access share; CCC has `code-review` and `simplify` |

Atto already has the human gate. What it does not have is the **URL-fragment ciphertext
paste**, which lets a family researcher share a dossier without an account. That maps
onto Atto's Access share tier.

### Why it does not install

The Workstation Harness Freeze (Gate 3) blocks new local hooks and skills. Plannotator
works by installing a hook that intercepts plan and diff events. That is exactly what
the freeze stops.

Integrate here means the tier the report gave it, not permission to install. The
reference architecture is what ships.

### Status

Integrate, **reference only** under the freeze. Keep the encryption pattern; install
nothing.

## Snippets

> AES-256-GCM WebCrypto client-side encryption, decryption keys kept strictly in the
> URL fragment.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 3]

## Dead Ends

- **Installing the hook during the freeze.** Gate 3 blocks it whatever the tier says.
- **Sharing plain URL fragments over a messaging app.** Unencrypted small shares expose
  the content to browser history and any service that sees the link.
