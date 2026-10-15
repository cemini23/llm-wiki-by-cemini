---
title: "Agent-Reflex — Teaching Language Agents to Act Reflectively"
type: source
tags: [arxiv, agent, reflection, training, robustness]
keywords: [reflection learning, success-failure pairs, ReSFT, ORPO, AgentNoiseBench, tool feedback]
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

Title: Agent-Reflex — Teaching Language Agents to Act Reflectively
Authors: Guanting Dong, Xinyu Yang, Jiajie Jin et al. (Renmin University of China, NUS)
Type: arXiv preprint (2610.17953)
Location: `research to be indexed/ccc/arxiv-2610.17953-agent-reflex-teaching-language-agents-to-act-ref.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The gap:** MCP tool services return noisy feedback and users intervene to correct agents, but existing methods give **little supervision for reflection and failure recovery**.

**Three stages, all built on Qwen3-8B:**

1. **Environment Reflection Skill Discovery (RSD)** — injects grounded tool-feedback perturbations, samples a capability-diverse LLM pool, mines **matched success–failure pairs**, and summarises reusable **reflection meta-skills**.
2. **Reflective SFT (ReSFT)** — turns each skill into supervision for self-reflection, skill recovery, and user-centric correction.
3. **On-Policy Reflective Policy Optimization (ORPO)** — agentic RL under noisy interactions, plus reflection-guided on-policy distillation.

**Results:** **58.6** overall across five long-horizon tool-use benchmarks; **29.1** on AgentNoiseBench — above strong environment-scaling and reflection baselines. Analysis reports improved robustness to noise with stable training dynamics.

**Why it is filed here:** reflection is **trained from contrastive success–failure pairs**, not from an instruction to reflect. The failure signal is the training data.

## Snippets

> "MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision for reflection learning and failure recovery." [Source: arxiv-2610.17953 p.1]

> "RSD ... mines matched success–failure pairs, and summarizes reusable reflection meta-skills." [Source: arxiv-2610.17953 p.1]

## Dead Ends

- Prompting an agent to "reflect more". The paper's supervision comes from paired successes and failures, not from instructions.
