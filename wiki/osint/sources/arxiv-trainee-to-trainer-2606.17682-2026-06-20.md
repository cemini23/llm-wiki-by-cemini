---
title: "Trainee-to-Trainer — LLM environment engineer for RL — arXiv 2606.17682"
type: source
tags: [source, arxiv, llm-agents, rl, curriculum, k124]
keywords: [2606.17682, environment engineer, MAPF, FrozenLake, GRPO, curriculum]
related:
  - concepts/llm-environment-engineer-rl-curriculum.md
  - entities/tools/trainee-to-trainer.md
  - concepts/llm-agent-systems.md
maturity: draft
read_status: read
created: 2026-06-20
updated: 2026-06-20
clusters: [llm-agents, rl-marl]
---

## Relations

- @concepts/llm-environment-engineer-rl-curriculum.md — K124 synthesis
- @entities/tools/trainee-to-trainer.md — Phase-0 entity
- @concepts/llm-agent-systems.md — agent harness corpus

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning |
| **Authors** | Chao Chen, Chengzu Li, Zhiwei Li, Yinhong Liu, Zhijiang Guo (LARK / Cambridge / HKUST) |
| **arXiv** | 2606.17682 (Jun 2026) |
| **sha256** | `cdccfb0c674d72fbdc6b9cc2ccf144587a8d6975a51764c6537ad36d0e2152e7` |
| **Repo** | https://github.com/LARK-AI-Lab/Trainee-to-Trainer |
| **Weights** | https://huggingface.co/LARK-Lab/Trainee2Trainer/ |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.17682-2606-17682v1-from-trainee-to-trainer-llm-designe.pdf` |
| **Retrieved** | 2026-06-20 (daily digest inbox) |
| **Read status** | read (abstract + §3 method + context ablation table) |

## Narrative

**LLM-as-Environment-Engineer:** after each RL round, the current policy checkpoint reads failure trajectories + validation stats and proposes the **next-stage environment configuration** (not just tasks/responses). Closed loop: train → validate → design → regenerate data.

**Testbed MAPF-FrozenLake:** multi-agent grid pathfinding with holes; generator config `C` controls map-size distribution, hole ratio, wait-action conflict density. Built on Conflict-Based Search.

**Key findings [TENTATIVE — paper claims]:** Qwen3-4B backbone beats larger proprietary LLMs and fixed-environment baselines on aggregate benchmarks; **current RL checkpoint** is a better environment engineer than the original base model; successful updates rely on **failure evidence** and preserving configs that already work.

**Context ablation:** six variants (V1–V6) adding failure breakdown, guidelines, history, training meta — failure breakdown + history with default config most informative.

**Cemini posture:** **CONDITIONAL-GO** — GitHub `license: NOASSERTION` at Phase-0 (2026-06-20); steal **environment-engineer loop pattern** for castle-sim playtest scenario generation and poker regression spot curation, not MAPF install.

## Snippets

> "The current RL checkpoint serves as a better environment engineer than the original base model." [Source: arXiv:2606.17682 abstract (retrieved 2026-06-20)]

> "Unlike static curriculum design, our framework forms a closed feedback loop in which the learner modifies the distribution of its future training environments as its weaknesses change." [Source: arXiv:2606.17682 §3.2 (retrieved 2026-06-20)]

## Dead Ends

- MAPF-FrozenLake domain ≠ poker or Godot — pattern steal only.
- No SPDX license on repo — do not pip install until license verified.
