---
title: "Agent usage versus app usage — the commodity test for a SaaS product"
type: concept
related:
  - sources/newsletter-rss-latent-space-2026-11-19-why-linear-says-issue-tracking-is-dead-cristina.md
  - sources/newsletter-rss-latent-space-2026-11-19-scaling-linears-gtm-to-100m-arr-cristina-cordova.md
  - concepts/agent-pr-volume-exceeds-human.md
updated: 2026-11-26
maturity: draft
---

## Raw Concept

Question this page answers: when agents do most of the work inside a product, what stops the product
from becoming a commodity?

Synthesised from one interview: Cristina Cordova, COO of Linear, on Latent Space (2026-11-19). This is
a vendor's own argument, so treat the evidence as `[TENTATIVE]`.

## Narrative

**The claim.** An MCP server on top of a database is not a product strategy. If the agent workflows
inside the product are no better than the workflows outside it, nobody has a reason to open the app.
The company becomes a data source for someone else's agent.

**The test.** Cordova watches two lines together:

- **Agent usage** — how much work arrives through the MCP server or API.
- **App usage** — how much work humans still do in the product itself.

If agent usage climbs and app usage stays flat, the product is commoditising. If both climb, the app
still earns its place. Linear reports both rising. Agents create more than half of the issues, and
people still return to the app to see and coordinate the work.

**The mechanism that fails.** The temptation is to ship the MCP server and stop. That converts a
product into a backend for an agent that owns the user relationship. The user stops opening the app,
so the product stops learning from user behaviour, and pricing power moves to the agent layer.

**The counter-case in the same interview.** Linear is small enough to cannibalise itself. Cordova
names Google as the harder case: put an AI answer above every search result and fewer people see the
ads. The test applies to a company that can absorb the loss, not to one whose revenue is the app.

**Why CCC cares.** The workspace has a local wiki, a local harness and a set of agents. The
equivalent risk is a wiki that answers only through an agent and never gets read by a human. The
two-line test is a usable check on any local tool the workspace builds: measure agent reads and human
reads separately.

## Snippets

> "If the agent workflows inside your product aren't better than the ones outside it, nobody has a
> reason to open your app." [Source: `newsletter-rss-latent-space-2026-11-19-why-linear-says-issue-tracking-is-dead-cristina.md`]

> "So she watches two lines: agent usage and app usage. If agent usage climbs and app usage doesn't,
> you're becoming a commodity." [Source: same]
