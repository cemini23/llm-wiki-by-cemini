---
title: "How are AI agents used? Evidence from 177,000 MCP tools"
type: source
tags: [pdf, llm-agents, mcp, agent-ecosystem, ai-governance, empirical-study, k49]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: How are AI agents used? Evidence from 177,000 MCP tools (arXiv:2603.23802)
- **Author(s)**: Merlin Stein (UK AI Security Institute / University of Oxford)
- **Type**: PDF (arXiv preprint)
- **Location**: research for cemini/protocol 8 3:29.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 36p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

**Problem.** Developers, researchers and regulators lack large-scale evidence on how AI agents are actually used in the wild. Most usage studies track raw LLM usage, not agentic tool calls.

**Method.** The largest agent-tool dataset to date: **177,436 public MCP tools** harvested from MCP server repos on GitHub and Smithery, created 11/2024–02/2026 (16 months). Download data from NPM and PyPI approximates usage for 3,854 servers (42,498 tools). Each tool is classified along five action-space attributes: **direct impact** (perception / reasoning / action), **generality** (constrained vs unconstrained environments), **task domain** and **consequentiality** (via O*NET occupational mapping), geographic spread, and human- vs AI-authorship.

**Key results.** Tool availability grew **>10×** (≈4,888 tools in 01/2025 → 177,000 in 02/2026). **Software development dominates: 67% of tools, 90% of downloads.** The headline trend is a shift toward *action*: tools that modify environments (vs merely perceive) rose from **27% to 65% of total usage** over 16 months (21%→71% for tools from registered companies), driven by general-purpose unconstrained-environment tools (browser/computer control) — 94% of which carry action capabilities. Most action tools serve medium-stakes tasks (file editing), but **financial transactions are a fast-growing higher-stakes pocket** (e.g. Coinbase MCP). Usage is geographically concentrated: US ~50–57% of downloads, Western Europe ~20%, China ~5%. Strikingly, **AI-coauthored tools are rising fast**: AI assistance detected in 28% of servers / 36% of tools; the share of new servers built with AI help rose 6% (01/2025) → 62% (02/2026), 69% of those via Claude Code — i.e. agents are increasingly building tools for other agents. The paper proposes MCP-server monitoring as a governance method to extend regulatory oversight from model outputs down to the tool layer, illustrated by a trial with UK financial authorities, and flags structural risks including correlated "agent bank runs."

**Cemini relevance.** Macro context for the entire conductor/librarian MCP strategy: the action-tool surge and AI-authored-tool feedback loop are exactly the dynamics a Cemini MCP-based stack participates in. The financial-transaction-monitoring case study and "agent bank run" structural risk are directly germane to CeminiSuite's trading-agent threat model and to any OSINT work on AI-driven market structure.

## Snippets

> "the share of 'action' tools rose from 27% to 65% of total usage over the 16-month period sampled. While most action tools support medium-stakes tasks like editing files, there are action tools for higher-stakes tasks like financial transactions."
> [Source: protocol 8 3:29.pdf p.1]

> "Tool availability increased by more than an order of magnitude, from approximately 4,888 tools in 01/2025 to 177,000 tools in 02/2026."
> [Source: protocol 8 3:29.pdf p.34]

> "The share of new MCP servers created with AI assistance rose from 6% (01/2025) to 62% (02/2026), dominated by Claude Code (69% of AI-coauthored servers)."
> [Source: protocol 8 3:29.pdf p.2]
