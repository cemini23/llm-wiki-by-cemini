---
title: "bot-browser — real Chrome with a human login handoff (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
maturity: draft
created: 2026-11-17
updated: 2026-11-17
---

## Raw Concept

Routed from
@osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md, URL 18,
during the 2026-11-17 ingest. Graded **Context**.

The question this page answers: **how does an agent use a logged-in browser without
ever holding the credential?**

## Narrative

A Node.js CLI and MCP server that drives a **real Chrome with a permanent profile**
over CDP, plus OS accessibility APIs. MIT, 13 stars, local only.

The design decision that matters: when a login is needed, the agent calls
`request_login` and a **human completes it**. The agent never reads the credential,
because the session is already authenticated in the profile.

That is the correct shape for any agent that needs a logged-in browser. The alternatives
are worse: storing a password for the agent, or extracting cookies into the agent's
context. Both put a secret inside the model's window.

Secondary details: stealth launch flags (no `--enable-automation`,
`navigator.webdriver` false), and a profile at `~/.bot-browser/profile` isolated from
the operator's daily browser.

Capped by the Workstation Harness Freeze. The pattern — human-gated session
establishment, agent-gated session use — is the extract. It is the same principle as
Atto's human gate, applied to credentials.

## Snippets

> A real Chrome with its own permanent profile for your coding agent.
> [`franciscobeccaria/bot-browser`, repository description, 2026-11-17]
