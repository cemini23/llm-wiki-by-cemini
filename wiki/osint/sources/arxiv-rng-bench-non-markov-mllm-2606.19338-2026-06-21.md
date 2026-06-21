---
title: "RNG-Bench — non-Markov MLLM evaluation — arXiv 2606.19338"
type: source
tags: [source, arxiv, benchmark, memory, mllm, k125]
keywords: [2606.19338, RNG-Bench, non-Markov, Memory Gap, Matching Pairs, 3D Maze, belief state]
related:
  - concepts/non-markov-belief-state-benchmarks.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/agentic-navigation-memory-strategy.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/llm-agent-systems.md
  - sources/arxiv-qwen-robotnav-2606.18112-2026-06-20.md
maturity: draft
read_status: read
created: 2026-06-21
updated: 2026-06-21
clusters: [llm-agents, benchmarks]
---

## Relations

- @concepts/non-markov-belief-state-benchmarks.md — K125 synthesis
- @concepts/poker-arena-multi-axis-cognitive-profile.md — hidden-state / session memory eval analog
- @concepts/agentic-navigation-memory-strategy.md — spatial belief-state sibling (K124 RobotNav)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Beyond the Current Observation: Evaluating Multimodal Large Language Models in Controllable Non-Markov Games |
| **Authors** | Shengyuan Ding, Xilin Wei, Xinyu Fang, Haodong Duan, Dahua Lin, Jiaqi Wang, Yuhang Zang |
| **arXiv** | 2606.19338 (17 Jun 2026) |
| **sha256** | `005a2a73b33ea9c1b6e89c55367b43db40bfc3fae52b9a57bfe7c13d7ceb56af` |
| **Repo** | none public at ingest |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.19338-beyond-the-current-observation-evaluating-multim.pdf` |
| **Retrieved** | 2026-06-21 (daily digest inbox) |
| **Read status** | read (abstract + benchmark design + Memory Gap + SFT transfer) |

## Narrative

**RNG-Bench** isolates **non-Markov** closed-loop control: optimal action depends on **observations no longer visible**. Two games — **Matching Pairs** (card identity recall) and **3D Maze** (egocentric map integration) — share a unified harness with controlled axes: grid scale, visual pattern, observation modality. **Head-to-head duel** protocol controls instance variance; **Memory Gap** metric separates **forgetting** from poor action selection.

**Findings [TENTATIVE — paper claims]:** frontier MLLMs collapse as latent state grows; image observations bottleneck more than text history length; hardest configs need ~128K tokens and ~350 images/episode; most residual error is **belief-state maintenance**, not decision quality given correct belief.

**SFT transfer:** Qwen3.5-9B fine-tuned on optimal + filtered rollout trajectories improves RNG-Bench and targeted spatial/memory benchmarks without large general-MMLU regressions.

**Cemini posture:** **REFERENCE / steal-from** — poker: F6 session memory ablation using Memory-Gap-style decomposition (forget vs mis-decide); castle-sim: playtest harness diagnostic for fog-of-war / haul-route recall. No public repo → REFERENCE.

## Snippets

> "We refer to this regime as Non-Markov: the current observation alone is insufficient for optimal action, so the model must infer the relevant hidden state from its history before acting." [Source: arXiv:2606.19338 §1 (retrieved 2026-06-21)]

> "Memory Gap analysis shows that most residual errors stem from forgetting earlier observations rather than from suboptimal decision making." [Source: arXiv:2606.19338 abstract (retrieved 2026-06-21)]

## Dead Ends

- Multimodal image-heavy benchmark ≠ symbolic NLHE — steal **Memory Gap diagnostic**, not Matching Pairs env install.
- MLLM fine-tuning path conflicts with Researcher track **no runtime LLM** posture — offline eval rubric only.
