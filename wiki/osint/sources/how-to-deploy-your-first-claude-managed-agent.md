---
title: "Claude Managed Agents — The Complete Setup Guide"
type: source
tags: [docx, llm-agents, k49]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: read
created: 2026-04-23
updated: 2026-05-17
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: Claude Managed Agents – The Complete Setup Guide
- **Author(s)**: Anthropic (vendor practitioner guide; no individual byline)
- **Type**: DOCX
- **Location**: research for cemini/How to Deploy Your First Claude Managed Agent.docx
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: practitioner guide, 9 sections
- **Read status**: read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

**What it is.** A practitioner setup guide for Anthropic's Claude Managed Agents — cloud-hosted AI agents that run on Anthropic's infrastructure rather than on a user's machine. It is positioned as the "fully managed" end of a spectrum running from personal tools (Cowork, Claude Code), through self-hosted (Agent SDK), to Managed Agents, distinguished purely by who runs the infrastructure. Public beta; every request needs the `managed-agents-2026-04-01` beta header.

**Method / structure.** Four core concepts: an **Agent** (the reusable blueprint — name, model, instructions, tools), an **Environment** (the cloud container template the agent runs in), a **Session** (a running instance binding an agent to an environment), and **Events** (the SSE stream of agent messages, tool-use events, and status events). The quickstart is four steps: set up the `ant` CLI or Python SDK plus API key; create an agent; create an environment; start a session and stream a message. The `agent_toolset_20260401` toolset enables eight built-in tools (bash, read, write, edit, glob, grep, web_fetch, web_search). Later sections cover environment/container config, sessions and SSE streaming, security (vaults, permissions, networking guardrails), resources (files, GitHub, memory), and production hardening. Sessions persist context after going idle — follow-up messages reuse full history. Pricing is standard token pricing plus managed-infrastructure extras; idle time is free.

**Cemini relevance.** Managed Agents is a candidate deployment surface for always-on Cemini agents that today would otherwise need a laptop or a hand-managed Hetzner process — directly relevant to the conductor / CCC orchestration layer, where a 24/7 cloud-hosted agent could replace self-hosted infrastructure for routine librarian or ticker-research tasks. The Agent/Environment/Session/Events decomposition is a useful mental model to compare against the existing conductor design.

## Snippets

> "Managed Agents run on Anthropic's cloud. No servers to manage. No infrastructure to babysit. Currently in public beta. The idea in one sentence: You define the agent. Anthropic runs it." [Source: How to Deploy Your First Claude Managed Agent.docx p.1]

> "You created an Agent (the what and how) ... an Environment (the where) ... a Session (the when) ... and received Events (the communication). Everything in Managed Agents is a combination of these four pieces." [Source: How to Deploy Your First Claude Managed Agent.docx p.2]

> "The agent_toolset_20260401 enables all 8 built-in tools: bash, read, write, edit, glob, grep, web_fetch, and web_search." [Source: How to Deploy Your First Claude Managed Agent.docx p.2]
