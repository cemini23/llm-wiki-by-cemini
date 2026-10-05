---
title: "EvoRiskBench — evolving runtime security risks in workspace agents"
type: source
tags: [arxiv, agent-security, red-teaming, benchmark]
keywords: [2610.03153, workspace-agents, prompt-injection, runtime-risk, model-harness]
related:
  - concepts/k282-agent-eval-wave.md
maturity: draft
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- @concepts/k282-agent-eval-wave.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | EvoRiskBench: An Evolving Benchmark for Runtime Security Risks in Workspace Agents |
| Authors | Shiyi Kuang, Xuemei Luo, Kun Liu, Junhai Li, Rui Tian, Feng Shi, Bo Shen, Nianyu Li, Dehui Li, Ping Chen (Novo Ordo for AI; Fudan University; Zhongguancun Laboratory) |
| Type | arXiv paper |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.03153-evoriskbench-an-evolving-benchmark-for-runtime-s.pdf` |
| Retrieved | 2026-10-05 |
| arXiv | 2610.03153 |
| read-status | read |

## Narrative

The paper introduces EvoRiskBench, an executable benchmark for runtime security
risks in workspace agents. A workspace agent is a stateful Model × Harness system
that runs multi-step tasks through tools and external resources. The framework
links a risk entry point (EP) to a technical effect (EF) through an agent-mediated
path. It defines nine entry points (session memory, knowledge retrieval, command
execution, file I/O, network access, peer-agent communication, subagent delegation,
MCP service, skill invocation) and five effects (information disclosure,
unauthorized access, data tampering, system destruction, resource exhaustion).
A 20-participant study gives Fleiss' κ = 0.904 for entry points and κ = 0.723 for
effects.

The benchmark holds 450 adversarial tasks across six scenarios. The authors test
nine Model × Harness configurations using GPT-5.6 Sol, DeepSeek-V4-Pro-0813, and
Claude Opus 5, with Claude Code, Codex, and OpenClaw. Across 4,050 executions, the
aggregate attack success rate (ASR) is 37.46%. The worst configuration, DeepSeek
with Codex, reaches 68.44%. ASR spread across models (54.37 pp) dwarfs the spread
across harnesses (5.41 pp). Opus 5 averages 4.44%. The authors conclude that model
choice is the primary driver, but the harness still matters.

For this workspace: this directly targets agent harness security, which is the
workspace's core stack (Claude Code, Codex). It shows that indirect prompt
injection through MCP services, skills, and subagent delegation yields real
technical effects. The EP–Path–EF taxonomy and the runtime-verification design are
reusable for red-teaming local agent setups.

[Source: arXiv:2610.03153]

## Snippets

> "The most vulnerable configuration, Codex with DeepSeek-V4-Pro-0813, reaches a 68.44% attack success rate (ASR), indicating that configuration of workspace agent is insufficient to ensure secure autonomous execution."
[Source: arxiv-2610.03153-evoriskbench-an-evolving-benchmark-for-runtime-s.pdf p.1]

> "Among the 4,050 attack executions across all nine Model × Harness configurations, 1,517 successfully achieve their respective attacker-defined goals through workspace-agent execution, yielding an aggregate ASR of 37.46%."
[Source: arxiv-2610.03153-evoriskbench-an-evolving-benchmark-for-runtime-s.pdf p.8]

> "The aggregated ASRs of DeepSeek-V4-Pro-0813, GPT-5.6 Sol, and Claude Opus 5 are 58.81%, 49.11%, and 4.44%, respectively. The resulting 54.37-percentage-point model-level spread is substantially larger than the 5.41-percentage-point spread among the harness-level averages."
[Source: arxiv-2610.03153-evoriskbench-an-evolving-benchmark-for-runtime-s.pdf p.8]

> "ASR varies more across models than harnesses, and harness differences depend on the model."
[Source: arxiv-2610.03153-evoriskbench-an-evolving-benchmark-for-runtime-s.pdf p.1]
