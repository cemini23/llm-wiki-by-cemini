---
title: "MCPTrace — Volatility 3 plugin for MCP and JSON-RPC artefacts"
type: entity
related:
  - sources/newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md
  - concepts/mcp-security-posture.md
  - concepts/agent-execution-provenance.md
updated: 2026-11-14
---

## Raw Concept

What prompted this page: tl;dr sec #354 listed the tool in its quick links. This page records it as a DFIR reference. It is not evaluated here.

## Narrative

MCPTrace is a Volatility 3 plugin. It extracts MCP and JSON-RPC message candidates from Windows and Linux memory dumps.

The value is evidentiary. Agent traffic is often encrypted in transit and absent from disk. A memory image can still hold request and response buffers, which makes it one of the few sources for what an agent actually asked a tool to do.

### Where it fits

| Investigation question | How the plugin helps |
|---|---|
| Which MCP servers did this host talk to? | Recovers message candidates from memory |
| What tool arguments were sent? | Recovers JSON-RPC payload fragments |
| Did the agent act after a suspicious instruction? | Places messages in a timeline with other artefacts |

Treat recovered strings as candidates. Memory recovery is lossy, so each finding needs corroboration from a log or a filesystem artefact.

### Status

`[OPEN QUESTION 2026-11-14]` The plugin is not tested in this workspace. Maturity, output format, memory-profile coverage and Volatility 3 version support are unverified.

### Related work

`@concepts/agent-execution-provenance.md` covers the wider problem: an agent run leaves evidence across several layers, and the memory layer is the one most often skipped.
