---
title: "MCP tool poisoning — a cross-framework measurement with real execution"
type: source
tags: [source, arxiv, mcp, prompt-injection, agent-security, supply-chain]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study |
| Authors | Farooq Shaikh, Biagio Montaruli (Dynatrace, Linz) |
| arXiv | 2611.03555 |
| Pages | 12 |
| Read status | skimmed (abstract) |

## Narrative

**The most directly actionable security paper in this batch**, because it measures something this workspace actually runs: MCP servers feeding tool descriptions into model context.

### The flaw it names

The Model Context Protocol carries **attacker-controlled content** direct into model context **without validation**:

- tool descriptions,
- schema fields,
- response data.

A malicious or compromised MCP server does not need to exploit a memory bug. It writes convincing text into the place where the model decides what to do next.

### What the paper adds over prior benchmark work

Three gaps in earlier work, each closed:

1. **Real tool execution**, not just model compliance. Prior benchmarks stopped at "did the model follow the poisoned instruction"; this one confirms the tool actually ran.
2. **Framework-layer contribution isolated.** It separates how much defence the agent framework itself provides.
3. **Vendor accountability documented.**

It presents a **25-class root-cause taxonomy** unifying prior classifications.

### Why it matters here

This workspace loads MCP servers — trading tools, search, browser, memory, and more — several of which are third-party. The attack does not require anyone to compromise this machine. It requires one dependency's tool description to say the wrong thing.

That makes the relevant control **not a scanner but a boundary**: what a tool can do must not be determined by what its description says. The description informs the model; the permission decides the capability.

Concretely, for anything in this estate:

- A tool's declared purpose is not evidence of its behaviour.
- Read-only tools should be enforced read-only outside the model.
- Response data from a tool is untrusted text, not instructions.

This is the same conclusion as the workspace's existing rule for external content, now measured on the MCP layer specifically.

**Caveat.** Abstract only. No detection rate, framework ranking, or taxonomy detail is reproduced here.

## Snippets

> "The Model Context Protocol (MCP) enables agentic AI frameworks to connect language models to external tool providers, yet its design carries attacker-controlled content, spanning tool descriptions, schema fields, and response data, directly into model context without validation." [Source: arxiv-2611.03555 p.1]

> "We present the first cross-framework measurement of MCP tool poisoning with real tool execution." [Source: arxiv-2611.03555 p.1]

## Dead Ends

- **Treating a described tool as a trusted tool.** The description is the attack surface.
