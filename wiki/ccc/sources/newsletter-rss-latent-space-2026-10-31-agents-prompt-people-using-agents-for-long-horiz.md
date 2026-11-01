---
title: "Agents Prompt People: Arca's harness for long-horizon financial work"
type: source
tags: [source, newsletter, agents, harness, long-horizon]
related: []
maturity: draft
read_status: read
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Agents Prompt People: Using Agents for Long-Horizon Financial Work |
| Source | Latent Space |
| File | `newsletter-rss-latent-space-2026-10-31-agents-prompt-people-using-agents-for-long-horiz.md` |
| Retrieved | 2026-11-01 |
| URL | https://latent.space/p/arca/ |
| Read status | read |

## Narrative

Latent Space reports a talk with Aman Singh, lead AI engineer at Arca. The conversation happened at AI Engineer New York. Arca is an AI-native firm that provides wealth management services. The file header dates the post to 2026-10-31.

The source says agents do most of the background work. Guardrails keep human advisors on the final decisions. Singh says the goal is for AI to guide the process, and that "agents prompt people more than people prompt agents." The source says Arca recently raised $48.5 Million. General Catalyst led the round. Index Ventures and Venrock took part. The $48.5 Million figure is a single-source claim.

Singh calls the work long-horizon, and he says it is not long-running. In his AIE presentation, agent tasks at Arca can take up to ten days. He describes the work as stop-start, with many actors, decision points, and handoffs. The ten-day figure is a single-source claim. Arca built an internal memory system with persistence for every client. The system tracks what has happened, what comes next, near-term actions, long-term items, and which person owns each action. Agents write into that memory.

Arca uses models from Anthropic and OpenAI. Claude is the primary model provider. Arca built its own harness. The harness selects a model for each task from the firm's internal benchmarks. The source says that owning the harness, rather than using a managed agent harness, lets Arca change model providers.

Singh limits an agent's role to analysis and proposed solutions. A human advisor handles trading and any other money movement. He says all safety restrictions are fully deterministic and take the decision off the agent. The agent may run some tools and tasks. It may not run tasks that put the client at risk. Arca also runs verification checks on known issues such as prompt injection.

The agent itself is not in a sandbox. Computation runs in sandboxes. Singh says Arca translates the code the agent wrote into a strict format, discards the code, and installs guardrails on that format before it reaches the back end. Agents then use code to query, aggregate, and reshape data, including for a financial plan. Advisor feedback and agent traces go to a meta-agent. That meta-agent suggests changes to the harness.

For a harness practitioner, the post is a field account of four design choices. The firm owns model routing. Client memory spans multi-day handoffs. Deterministic rules block client-risk actions. A code-to-format gate sits in front of the back end, and a meta-agent proposes harness edits from traces and staff feedback.

## Snippets

> "All of our safety restrictions are fully deterministic," he said. "And they take the decision making off the agent's hands." [Source: https://latent.space/p/arca/ (retrieved 2026-11-01)]
