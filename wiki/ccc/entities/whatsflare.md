---
title: "whatsflare — WhatsApp gateway on Cloudflare Workers (MIT)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
maturity: draft
created: 2026-11-24
updated: 2026-11-24
---

## Raw Concept

Routed from
@osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md, URL 19,
during the 2026-11-24 ingest.

The question this page answers: **how do you hold one long-lived messaging session on
serverless infrastructure?**

## Narrative

A WhatsApp gateway built on Cloudflare Workers: `baileys` running inside a **Durable
Object**, exposed as a REST and WebSocket API. **MIT**, 5 stars, pushed 2026-11-21.

### Why this page exists

The 2026-11-24 evaluation graded it **UNAVAILABLE** — "This website is inaccessible" —
and skipped it. Direct checks return HTTP 200, and the GitHub API reports a live,
unarchived, MIT repository. [CONFIRMED — 2026-11-24]

This is the second consecutive batch with a false UNAVAILABLE verdict. The page records
the item so a skipped URL does not disappear silently.

### The pattern worth noting

A Durable Object is the right primitive for a single WhatsApp session: it gives one
stateful actor a serialised inbox, which is exactly what a long-lived socket needs.
Running the session object and the HTTP surface in the same deploy removes a relay tier.

That shape applies to any long-lived single-session connector, not only WhatsApp —
worth remembering if a GuruWatcher or PM-canary integration ever needs a persistent
socket rather than polling.

### Fit

None today. No Priority #1–#3 project sends WhatsApp messages, and the Workstation
Harness Freeze blocks new local tooling. Context reference only.

## Snippets

> WhatsFlare — WhatsApp gateway for Cloudflare Workers: baileys in a Durable Object, a
> REST + WebSocket API.
> [GitHub repository description, retrieved 2026-11-24]

## Dead Ends

- **Trusting an UNAVAILABLE verdict without a retry.** This URL was live both times it
  was checked.
