---
title: "WebMCP — declaring browser tools for agents (W3C community spec)"
type: entity
tags: [tool, mcp, discoverability, agents, atto, spec]
keywords: [webmcp, browser tools, w3c community group, agent discoverability, read-only tools, ato]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md"
  - entities/tools/agent-desktop.md
  - "@osint-wiki/entities/tools/agentdiscoverability-track.md"
maturity: draft
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md, URL 12, **Extract** tier. Routed to Atto and the local-abliterated lab.

The question this page answers: **how does a website tell a browser agent what it can do?**

## Narrative

### What it is

A **W3C community specification** and a public directory at `webmcp.com`. Not a product, and not licensed software — it is a proposed protocol plus a registry.

The idea: a page declares a set of tools the visiting agent may call, in the browser, without the agent having to scrape the DOM or guess at the interface. The report points to `vercel-labs/wterm`'s Geistdocs implementation as the reference — read-only tools such as `search_docs` and `read_current_page`.

### Why it is the natural continuation of two earlier threads

This is the third link in a chain across three batches:

1. **v10.10 batch B** — @osint-wiki/entities/tools/agentdiscoverability-track.md describes *being picked* by an agent: Found → Picked → Positioned.
2. **v10.11** — WebMCP describes *being callable* by an agent once it arrives.

Discoverability gets the agent to the page. WebMCP gives it something to do there. Without the second, the first only buys a visit.

### The Atto case

Atto sells Concierge at $2,500 and above, and a $499–$899 kit range. If a buyer asks an assistant a genealogy question, the assistant choosing Atto is a sales channel — and a read-only WebMCP surface is a way to make Atto's public portal usable by that assistant without giving it write access.

**Read-only is the load-bearing constraint.** Atto's hard bans are about not letting anything mutate the vault, not letting Antenati images leave the machine, and not auto-merging `truth.ged`. A WebMCP surface that exposes lookup only, and nothing that writes, is consistent with all three. A surface that exposes *submission* is not.

### The security half

The report also routes this to the local-abliterated lab as an audit target, which is the right instinct. An agent-callable surface declared by a page is an **injection surface**: the tools, their descriptions, and their schemas all reach model context. That is the same attack class measured in `MCP Tool Poisoning in Agentic AI Frameworks` from this same inbox.

Any WebMCP implementation needs the same treatment: descriptions are untrusted input, and a tool's declared purpose is not evidence of its behaviour.

### Status

Extract. A spec to read and a registry to understand; nothing to install.

## Snippets

> "Adds a WebMCP browser-tool registration brief to /Users/claudiobarone/Projects/atto (modeled on wterm's read-only search_docs and read_current_page WebMCP contract) and an adversarial WebMCP audit brief to Cybersecurity wiki/briefs/" — report, URL 12

## Dead Ends

- **Treating this as a tool to adopt.** It is a specification and a directory.
- **Exposing any write path.** The bans are the boundary; lookup only.
