---
title: "Davinci-Tool — Scaling Agentic Tool-Use Supervision with Verifiable Executable Environments"
type: source
tags: [arxiv, tool-use, agent, training-data, verification]
keywords: [tool-use model, execution-grounded data, verifiable environments, DPO, tau2-bench, MCP-Atlas]
related:
  - concepts/k291-ccc-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-ccc-wave.md — K291 ccc wave hub

## Raw Concept

Title: Davinci-Tool — Scaling Agentic Tool-Use Supervision with Verifiable Executable Environments
Authors: Xiaoyang Yuan, Ji Zhao, Xingyu Hu et al. (Tongji, Shanghai Innovation Institute, USTC, Southeast)
Type: arXiv preprint (2610.16867). Code: `github.com/MassLab-SII/Davinci-Tool`
Location: `research to be indexed/ccc/arxiv-2610.16867-davinci-tool-scaling-agentic-tool-use-supervisio.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The claim:** reliable agentic tool use needs training data that pairs multi-step workflows with **executable evidence the outcome was achieved**. Scaling trajectory coverage *or* verification alone is insufficient — new environments carry their own states, rules, and dependencies, which must appear in the success criteria too.

**Two pipelines:** **EGTS** derives verified demonstrations from independently authored systems; **EES** synthesises auditable environments, state-grounded tasks, and executable verifiers across single and coordinated domains.

**Scale:** 30,395 verified trajectories spanning **2,260 invoked tool names**. SFT first, then **outcome-grounded preference pairs** for DPO, reusing the EES states and verifiers.

| Benchmark | Qwen3-Coder-30B base | Davinci-Tool |
|---|---|---|
| τ2-bench | 52.4 | **88.2** |
| BFCL v4 multi-turn | 30.4 | **62.8** |
| MCP-Atlas | 16.9 | **56.2** |

Outperforms Qwen3-Coder-480B-A35B on all three **at 1/16 the total parameters**.

**Why it is filed here:** the **verifier must know the environment's success criteria**. A verifier that validates a stale definition of success is worse than none — it certifies the wrong outcome.

## Snippets

> "Scaling either trajectory coverage or verification alone is insufficient as new environments introduce distinct states, rules, and dependencies that must also be reflected in the success criteria." [Source: arxiv-2610.16867 p.1]

> "Davinci-Tool improves Qwen3-Coder-30B-A3B-Instruct from 52.4 to 88.2 on τ2-bench, from 30.4 to 62.8 on BFCL v4 multi-turn, and from 16.9 to 56.2 on MCP-Atlas." [Source: arxiv-2610.16867 p.1]

## Dead Ends

- Reading the benchmark gains as general capability. The model is trained against synthesised environments with executable verifiers; the gains are bound to that supervision.
