---
title: "Empirical Comparison of Agent Communication Protocols for Task Orchestration"
type: source
tags: [pdf, llm-agents, mcp, a2a, agent-protocols, benchmark, k49]
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

- **Original title**: Empirical Comparison of Agent Communication Protocols for Task Orchestration (UDC 004.89:004.75)
- **Author(s)**: Ivan Dobrovolskyi (Staff Software Engineer, Walmart Global Tech, Sunnyvale, CA)
- **Type**: PDF (journal article)
- **Location**: research for cemini/protocol 1 3:29.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 7p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

The first published head-to-head empirical benchmark of the two de-facto agent communication standards of 2025–2026: the **Model Context Protocol (MCP)**, Anthropic's tool-integration protocol (single agent calls tools within one context window), and **Agent-to-Agent (A2A)**, Google's inter-agent delegation protocol (a coordinator dispatches subtasks to specialist agents over HTTP/JSON-RPC). Before this paper the only comparison was a theoretical analysis (Chen et al.); practitioners had no data.

**Method.** Dobrovolskyi built an Open Source Health Analyzer querying four public APIs (GitHub, npm, OSV.dev, Stack Overflow) and implemented it three ways: MCP-only (single agent, 4 stdio tool servers), A2A multi-agent (coordinator + 4 FastAPI specialist agents), and Hybrid (a zero-LLM-cost keyword router that picks the protocol per query). 30 standardized queries across 3 complexity tiers, each run 5× per architecture = **450 controlled executions, zero failures**, all on Claude Sonnet 4. Statistics: bootstrap CIs, Mann–Whitney U with Bonferroni correction, Cliff's delta effect sizes.

**Key result — a statistically significant complexity-dependent crossover.** MCP is faster on simple queries (8.9s vs A2A 19.8s, p<0.0001, δ=−0.90) and medium queries, but A2A wins on complex multi-project queries (45.1s vs 51.8s). The driver is **context-window bloat**: for complex queries MCP accumulates 34,959 tokens in one window — **3.1× more** than A2A's 11,318 (distributed across lean specialist agents) — yielding a 39% cost reduction for A2A. The Hybrid router tracks the winner at every tier. Conclusion: the protocols are **complementary, not competing** — MCP as the agent-to-tool layer, A2A as the agent-to-agent orchestration layer.

**Cemini relevance.** Directly informs the conductor/librarian architecture: the conductor that routes wiki queries faces the same MCP-vs-delegation tradeoff. The crossover finding argues for a hybrid routing layer and quantifies the context-bloat cost of monolithic single-agent designs — a concrete decision framework for when to fan out to subagents.

## Snippets

> "A statistically significant crossover effect was discovered: the tool integration protocol is faster for simple queries, but the multi-agent protocol outperforms on complex multi-project comparisons while consuming substantially fewer tokens due to distributed context windows, resulting in markedly lower cost."
> [Source: protocol 1 3:29.pdf p.1]

> "For complex queries, MCP consumes 34,959 tokens, which is 3.1 times more than A2A (11,318 tokens; p < 0.0001, δ = +0.84). In the MCP single-agent architecture, every tool response is added to a single growing context window."
> [Source: protocol 1 3:29.pdf p.4]

> "These results imply that MCP and A2A are complementary rather than competing. MCP excels as a tool integration layer (agent-to-tool), while A2A excels as an orchestration layer (agent-to-agent)."
> [Source: protocol 1 3:29.pdf p.5]
