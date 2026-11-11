---
title: "AI Engineer Code Summit — OpenAI on new ways of working with Codex"
type: source
tags: [source, newsletter, coding-agents, codex, workflow]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AI Engineer Code Summit — OpenAI on New Ways of Working with Codex |
| Source | latent-space |
| Published | 2026-11-11 |
| Read status | skimmed (opening) |

## Narrative

Notes from the OpenAI workshop at the AI Engineer Code Summit, run by two Developer Experience engineers.

The observation with the most signal: **"the past year in coding agents has been one of constant product upgrades by all the frontier labs. But not all of these changes have gone smoothly. The shift to cloud, for example, is still confusing to many users of Codex, Claude and Antigravity."**

That is a vendor saying its own category's main architectural move has not landed cleanly. Cloud execution changes where the code runs, where the secrets are, and what the user can see — and the three major products have each modelled it differently.

Two newer patterns named:

- **Personal agents** — OpenAI's dots and Anthropic's Claude Duet, assisting between sessions.
- **Voice mode** as a way to steer coding tasks.

### Why the cloud-confusion line is the useful one

For this workspace the relevance is direct: everything here assumes local execution with a human merge gate. A product that is quietly shifting its default toward cloud changes the data path — the same class of hazard as `claude-video`'s Gemini default and `helix-foundry`'s key-triggered cloud call.

**The pattern is now unmistakable across five batches: the default is increasingly the hosted path, and the local path remains possible but undocumented.** Anyone running a local-first workflow has to check the default, not the capability.

**Caveat.** Workshop notes, one attendee, single source.

## Snippets

> "The shift to cloud is still confusing to many users of Codex, Claude and Antigravity." [retrieved 2026-11-11]

## Dead Ends

- **Reading this as product documentation.** It is one attendee's notes.
