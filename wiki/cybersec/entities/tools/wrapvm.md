---
title: "wrapvm — agent desktop VM with shared Chrome (NO-GO: no licence)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
updated: 2026-11-16
maturity: draft
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md, URL 19,
**Extract** tier. Routed to the cybersec wiki and the local operator lab.

The question this page answers: **what does an isolated VM for an agent look like, and
may we use this one?**

## Narrative

### What it does

A desktop virtual machine for agents. It combines three things:

- a base image with XFCE
- a **shared Chrome** instance, with the DevTools port exposed so a CDP agent can drive
  the same browser the user sees
- an agent runtime inside the VM

The shared-Chrome-over-CDP idea is what makes it interesting: a
`chrome-devtools-mcp` client can attach to a browser that is sandboxed from the host,
which is exactly the containment the operator lab wants.

### Phase-0, 2026-11-16 — NO-GO

| Check | Result |
|-------|--------|
| Licence | **None.** No `LICENSE`, `LICENSE.md`, `LICENSE.txt`, or `COPYING` in the repository root; GitHub API reports no SPDX id. [CONFIRMED] |
| Maturity | 383 stars, pushed 2026-11-04, 3 open issues |
| Cloud requirement | None — runs locally |
| Local gap | `local-abliterated-lab` is **not present** on this machine |

No licence means all rights reserved. The image, the Dockerfile, and the skills inside
cannot be copied, modified, or bundled into a shipped stack. The report recorded "NOT
FOUND" and then graded the item "friction only"; that reading is wrong. Absence of a
licence is a hard stop.

Even with a licence the item could not be queued, because the target project repository
does not exist locally.

### What is still usable

The **architecture** is public knowledge and is not copyrightable: boot a VM, run one
Chrome, expose port 9222, attach a CDP client. An operator can build that from a
licensed base image without touching this repository.

### Status

NO-GO. Reference for the containment pattern only. Do not copy files.

## Snippets

> License: NOT FOUND (no LICENSE file detected in repository).
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 19]

## Dead Ends

- **Treating a missing licence as friction.** It is a stop, not a cost.
- **Reusing the Dockerfile or skills.** Both are covered by default copyright.
