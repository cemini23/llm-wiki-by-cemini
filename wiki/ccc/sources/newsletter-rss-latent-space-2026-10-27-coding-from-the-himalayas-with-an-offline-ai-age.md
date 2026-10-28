---
title: "Coding From the Himalayas With an Offline AI Agent"
type: source
tags: [source, latent-space, local-models, coding-agents]
related: []
maturity: draft
read_status: read
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Coding From the Himalayas With an Offline AI Agent |
| Authors | Latent Space (guest post from a Principal Engineer at Thomson Reuters) |
| Feed | Latent Space (https://www.latent.space/feed) |
| File | `newsletter-rss-latent-space-2026-10-27-coding-from-the-himalayas-with-an-offline-ai-age.md` |
| Retrieved | 2026-10-27 |
| URL | https://latent.space/p/offline-coding/ |
| Published | 2026-10-27 |
| Read status | read |

## Narrative

A first-hand test of a fully local coding agent. The author is a Principal Engineer at Thomson Reuters who moved to the foothills of the Himalayas, where network and power outages are routine.

**Setup.** OpenCode is the agent. Ollama runs the model on the laptop. OpenCode keeps the workflow in the terminal, and its permission prompts let the author review commands and changes before they run.

**What works offline** — when the model, project dependencies, and test tools are already local:

- Explain an unfamiliar function.
- Investigate a failing test.
- Refactor a small piece of code.
- Help finish a feature.

**What still needs a connection:** downloading a new package, or looking anything up on the web.

**Why it matters.** This gives a concrete boundary for local-agent work. The dividing line is not task difficulty — it is whether the task needs a resource that is not on disk. Explain, diagnose, and small refactors are offline-safe. Dependency resolution and external lookup are not.

## Snippets

> "These tasks can run offline when the model, project dependencies and test tools are available locally. Downloading a new package or looking something up on the web will still need a connection." [Source: `newsletter-rss-latent-space-2026-10-27-coding-from-the-himalayas-with-an-offline-ai-age.md`, retrieved 2026-10-27]
