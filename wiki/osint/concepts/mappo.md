---
title: MAPPO (Multi-Agent PPO)
type: concept
tags: [concept, reinforcement-learning, multi-agent, methodology]
keywords: []
related:
  - sources/3-29-11.md
  - sources/3-29-6.md
  - sources/3-19-ip-sale-research.md
  - sources/3-19-telegram-discord-research.md
  - entities/frameworks/torchrl.md
  - entities/frameworks/pettingzoo.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-29-11.md
- @sources/3-29-6.md
- @sources/3-19-ip-sale-research.md
- @sources/3-19-telegram-discord-research.md
- @entities/frameworks/torchrl.md
- @entities/frameworks/pettingzoo.md

## Raw Concept

Synthesized across 4 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

**MAPPO (Multi-Agent Proximal Policy Optimization)** is a CTDE
(centralized-training-decentralized-execution) extension of PPO. A
single centralized critic takes the joint observation of all agents to
reduce variance during training; each agent ships with its own
decentralized actor for deployment.

**[CONFIRMED — 2026-04-24 Track C audit] research-only** — MAPPO training stack exists as specified. **One correction**: the wiki claimed **"TorchRL + PettingZoo"** but the actual stack uses **plain PyTorch (hand-rolled MAPPO) + PettingZoo + Gymnasium** — TorchRL is not imported. Research-only posture is intentional; RL deps are not in `cemini_mcp` container (correct — training is a host-side process, not a deployed service). Evidence: `rl_training/` dir with 11 modules (`action_masking.py`, `checkpointing.py`, `config.py`, `data_loader.py`, `environment.py`, `integration.py`, `interpreter.py`, `policy.py`, `reward.py`, `training.py`, `__init__.py`); `rl_training/environment.py:1` docstring cites PettingZoo ParallelEnv (Step 7) with 5 agents; `rl_training/training.py:1-22` docstring cites MAPPO centralised critic + share_params=False + CPU-optimised + Yu et al. 2022; `rl_training/checkpoints/` dir exists; `tests/test_rl_training.py` covers. No ticket required. Gap memo: `briefs/track-c-walk-results.md`.

### Cemini's use
Research-grade only — MAPPO-trained policies over PettingZoo multi-
venue execution environments are positioned in the IP-sale bundle as
evidence of sophisticated R&D (optimal inter-venue routing, alpha-
decay-aware capacity allocation), not as shipped production policy.

### Why it matters in the IP-sale context
The 3-19 IP-sale research is explicit: an acquirer will evaluate the
RL track as **optionality**, not as revenue-generating code. The
**PyTorch (hand-rolled MAPPO) + PettingZoo + Gymnasium** stack (formerly described as "MAPPO + TorchRL + PettingZoo" — TorchRL is not actually imported; track-C-correction 2026-04-24) demonstrates the team can run
modern RL research on CPU-tractable problems with a reproducible
Pydantic-v2-typed observation/reward pipeline — a significant
multiplier on the final sale price even if no RL-trained policy ever
ships to production.

## Snippets

*(populate as source stubs are deep-read.)*
