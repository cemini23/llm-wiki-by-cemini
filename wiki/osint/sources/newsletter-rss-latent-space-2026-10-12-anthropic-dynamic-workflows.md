---
title: "Latent Space — how Anthropic's dynamic workflows coordinate Claude agents (2026-10-12)"
type: source
tags: [source, k289, agents, orchestration, harness, ccc]
keywords: [dynamic-workflows, flows, claude-managed-agents, claude-console, dreaming, agent-rosters, orchestration-program, test-time-compute]
related:
  - concepts/k289-feeds-wave.md
  - concepts/k288-feeds-wave.md
  - concepts/agent-harness-auditing-a2e.md
  - concepts/typed-judgement-desk-pattern.md
maturity: draft
created: 2026-10-12
updated: 2026-10-12
read_status: read
---

## Relations

- @concepts/k289-feeds-wave.md
- @concepts/k288-feeds-wave.md — the decision-model category, one week earlier
- @concepts/agent-harness-auditing-a2e.md

## Raw Concept

| Title | How Anthropic's Dynamic Workflows Coordinate Claude Agents |
| Source | Latent Space (Substack) — from AI Engineer NYC |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-10-12-how-anthropics-dynamic-workflows-coordinate-clau.md` |
| Retrieved | 2026-10-12 |
| URL | https://www.latent.space/p/claude-dynamic-workflows |
| Tier | free (RSS) |
| cross_wiki | ccc-wiki |
| read-status | read |

## Narrative

Anthropic's **CJ Avilla** and **Harrison Stall** presented **dynamic workflows** ("flows") at AI Engineer NYC — a new Claude Managed Agents feature announced the Friday before.

### What flows are

> "a new type of multiagent orchestration, built for your most ambitious workloads."

The **lead agent writes a plan, then Claude writes an orchestration program** that launches agents, collects results, and manages information flow. **Claude chooses the topology.** Previously Managed Agents required a developer-configured coordinator + subagent roster; flows let Claude decide the organisation itself.

**The framing that lands:** the presenters invoked **Unix and Linux kernel maintainership** — as agents multiply, "a lot of us … might start to feel this feeling of being the bottleneck." Flows are the answer to being the breaking point in your own PR queue.

### The mechanism

- **Discrete, verifiable units of work** across phases, without the developer managing interconnections.
- **Pre-configured specialist sub-agents** can still be passed in via the agent config.
- **The demo pattern:** a stock watchlist scanner — a **scan phase distributing tickers to agents with isolated contexts**, then a **review phase**, then a report.
- **Subagents share a filesystem** and exchange information through it; there is **no direct API for one subagent to message another**.
- **Visibility:** Claude Console graphs every transition — "what did the lead agent actually pass to the sub-agent?"
- **"Dreaming"** (research preview): reads an existing memory store plus past session transcripts and **produces a reorganized memory store** — duplicates merged, stale/contradicted entries replaced, new insights surfaced.

### The Q&A (the candid part)

- **How many agents?** "The answer really is **evals and lower defaults**." Ambitious tasks need *explicit* encouragement to parallelize.
- **Does the lead agent know its budget?** **No.** Developers set a session budget; the model does not see it. Informing models of budgets "could make the agents a little bit anxious."
- **Can a flow improve itself?** Not built in — the presenters suggested **hill-climbing and dreaming** for that.
- **Cost:** flows cost **"much more"** than a single agent, but find more detail.
- **Ambition:** "Flows are basically a way to **throw test-time compute at hard problems** and get more capability faster."

### Why it matters here

This is the **vendor-side confirmation of the K288 pattern** (agent teams) and the K286/K288 harness thread — with the same caveats the wiki already holds: expensive, needs a budget set, and the model is a poor judge of its own parallelism. Directly relevant to `/route` and the harness lane. **No `/route` swap.**

## Snippets

> "Claude then writes an orchestration program, which launches agents, collects results, and manages information flow." [Source: newsletter-rss-latent-space-2026-10-12-anthropic-dynamic-workflows.md]

> "The answer really is evals and lower defaults." [Source: newsletter-rss-latent-space-2026-10-12-anthropic-dynamic-workflows.md]

> "Flows are basically a way to throw test-time compute at hard problems and get more capability faster out of the models." [Source: newsletter-rss-latent-space-2026-10-12-anthropic-dynamic-workflows.md]
