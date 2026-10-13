---
title: QwenGyre — elastic RL for extremely long-horizon agents
type: entity
tags: [tools, rl, agents, training, infrastructure]
keywords: [qwengyre, elastic-scheduler, trajectory-processor, prefix-shared-trees, nl2repobench, qwen3-8, colocated-training]
related:
  - sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
  - concepts/k290-feeds-wave.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
---

## Relations

- @sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
- @concepts/k290-feeds-wave.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept

**What prompted this page:** the Latent Space AINews issue for 2026-10-10 to 2026-10-12. Released by the Qwen team. Paper **arXiv:2609.33848**.

## Narrative

An **RL framework for training agents on extremely long-horizon tasks**. Two mechanisms:

**Elastic Scheduler** — dynamically **reallocates GPUs between rollout and training without interrupting live executions**. Reported **up to 1.85× speedup** over colocated execution and **1.78×** over async.

**Trajectory Processor** — represents **branching agent executions** (compaction, sub-agents, retries) as **prefix-shared trajectory trees**, which **deduplicates and bounds training samples** and lets the trainer **score partial progress after timeouts**. This is the more interesting idea: it turns the messy branching of a real agent run into a **shareable structure** instead of a set of duplicated flat transcripts.

**Reported scale result:** on **Qwen3.8-2.4T-A95B** with ~**700K tokens per rollout**, **NL2RepoBench rose from 52.5% to 58.5% in 48 steps** with ~**44% less training time** than async.

**Why it matters here:** this wiki already tracks the agent-RL framing question — **how to attribute credit and score partial progress in branching agent executions**. The **prefix-shared trajectory tree** is a concrete answer, and it is the same data structure the wave's **Fork-and-Flush** result suggests (branch exploration beats single runs on long-horizon tasks). Community note: the paper repeatedly references **Qwen3.6-122B** (~14 mentions), an eagerly awaited but unreleased model.

## Snippets

> Qwen released QwenGyre, an RL framework for extreme-long-horizon agent training, with an Elastic Scheduler that dynamically reallocates GPUs between rollout and training without interrupting live executions, reporting up to 1.85× speedup over colocated execution. [Source: https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder (retrieved 2026-10-13)]
