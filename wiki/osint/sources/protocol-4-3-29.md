---
title: "FinMCP-Bench: Benchmarking LLM Agents for Real-World Financial Tool Use under the Model Context Protocol"
type: source
tags: [pdf, llm-agents, mcp, financial-agents, benchmark, tool-use, k49]
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

- **Original title**: FinMCP-Bench: Benchmarking LLM Agents for Real-World Financial Tool Use under the Model Context Protocol (arXiv:2603.24943)
- **Author(s)**: Jie Zhu, Yimin Tian, Boyang Li, Xianyin Zhang, Lifan Guo, Feng Chen, Chi Zhang (Qwen DianJin Team, Alibaba Cloud); Kehao Wu, Zhongzhi Liang, Yong Liu (YINGMI Wealth Management); Junhui Li (Soochow University)
- **Type**: PDF (arXiv preprint, submitted to IEEE)
- **Location**: research for cemini/protocol 4 3:29.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 9p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

**Problem.** LLMs are increasingly deployed as financial agents that interpret user requests, call external tools (stock trends, fund holdings, market analyses), and chain multi-step reasoning. Prior financial benchmarks test reasoning or final answers but not realistic tool use; no benchmark evaluates financial agents under the Model Context Protocol (MCP), the standardized tool-invocation schema.

**Method.** **FinMCP-Bench** contains **613 samples** across **10 main scenarios and 33 sub-scenarios** (largest categories: Market Analysis & Research, 141; Investment Planning & Allocation, 101), wired to **65 real financial MCP tools** from Yingmi Fund's Qieman MCP server. Samples are sourced from 10K anonymized production logs of the XiaoGu AI assistant, in three complexity types: single-tool (145), multi-tool (249, avg 7.32 tool calls / 5.72 steps, 73 with parallel calls), and multi-turn (219, avg 5.95 turns). Synthetic hard cases are generated via a chain-based method — build a 65-node/288-edge tool dependency graph, sample tool chains, generate matching queries — plus role-playing multi-turn dialogues. All samples pass a two-stage quality gate (automated validation + dual expert 5-point Likert review). Evaluation metrics are tool-centric: Tool Precision, Tool Recall, Tool F1, and a strict Exact Match Rate (EMR) on tool grouping.

**Key results.** Six models evaluated (Qwen3-4B/30B-A3B/235B-A22B-Thinking, DeepSeek-R1, GPT-OSS-20B, Seed-OSS-36B). The Qwen3 family leads overall, but **model size does not monotonically predict performance** — Qwen3-4B beats Qwen3-30B on EMR. **Multi-turn samples are hardest**, with near-zero EMR for most models (best ~4%), exposing weak long-conversation tool tracking. Single-tool queries suffer low precision because models over-call (predict extra tools). TF1 does not decline monotonically with difficulty — strong models actually improve Easy→Hard, leveraging richer multi-tool constraints.

**Cemini relevance.** The single most directly relevant paper in this batch — it is a *financial-agent* MCP benchmark. It provides a concrete evaluation template for any Cemini ticker-research or strategy agent that invokes financial tools via MCP, and its central finding (multi-tool/multi-turn orchestration is the bottleneck, over-calling hurts precision) is a direct warning for CeminiSuite's tool-augmented design.

## Snippets

> "FinMCP-Bench contains 613 samples spanning 10 main scenarios and 33 sub-scenarios, featuring both real and synthetic user queries ... It incorporates 65 real financial MCPs and three types of samples, single tool, multi-tool, and multi-turn."
> [Source: protocol 4 3:29.pdf p.1]

> "Multi-turn samples tend to yield the lowest scores overall, especially in EMR, indicating that handling longer conversations with multiple tool calls remains challenging."
> [Source: protocol 4 3:29.pdf p.7]

> "model size does not consistently correlate with performance: Qwen3-4B-Thinking achieves a higher EMR score than Qwen3-30B-A3B-Thinking."
> [Source: protocol 4 3:29.pdf p.7]
