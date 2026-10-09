---
title: "HarnessSQL (arXiv 2610.12274)"
type: source
tags: [source, k287, arxiv, agents, sql, harness]
keywords: [harnesssql, text-to-sql, spider, k287]
related:
  - concepts/k287-arxiv-wave.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
read_status: read
---

## Relations

- @concepts/k287-arxiv-wave.md

## Raw Concept

| Title | HarnessSQL: Harness-Native Training for SQL Agents in Realistic Database Environments |
| Authors | Haolin Yang, Jipeng Zhang, Zhiqiang Qian, Jian Xie, Shuaishuai Gong, Yike Guo, Sirui Han |
| Type | arXiv preprint |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.12274-harnesssql-harness-native-training-for-sql-agent.pdf` |
| Retrieved | 2026-10-09 |
| arXiv | 2610.12274v1 |
| Licence | CC BY 4.0 |
| read-status | read |

## Narrative

Text-to-SQL models are often trained to emit one static query. A live database agent inspects schema, runs probes, and revises. HarnessSQL keeps that loop in supervised fine-tuning and in reinforcement learning.

On Spider 2.0-SQLite the paper reports Qwen3-8B execution accuracy from 15.5 percent to 45.2 percent, and Qwen3-14B from 22.2 percent to 54.8 percent.

The desk does not add a training job. The rule does not change. No agent-wiki brief. No training wire.

## Snippets

> "The execution harness that mediates this interaction is introduced only at inference time." [Source: arxiv-2610.12274 PDF, abstract]
