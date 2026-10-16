---
title: K292 ccc wave — computer-use harness, execution-window RL, model landscape (Oct 2026)
type: source-hub
tags: [k292, ccc, agents, harness, models]
keywords: [OpenGCUA, MLExpert, WIRL, reward-hack contagion, Argon monitorability, Muse Spark Open, Modal, SPACE sandbox]
related:
  - sources/arxiv-opengcua-2610.22200-2026-10-16.md
  - sources/arxiv-mlexpert-2610.22344-2026-10-16.md
  - concepts/computer-use-agent-harness.md
  - concepts/execution-window-rl.md
  - "@osint-wiki/sources/k292-osint-feeds-2026-10-16.md"
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
wire_status: policy_wired
---

## Relations

- @sources/arxiv-opengcua-2610.22200-2026-10-16.md
- @sources/arxiv-mlexpert-2610.22344-2026-10-16.md
- @concepts/computer-use-agent-harness.md
- @concepts/execution-window-rl.md
- @osint-wiki/sources/k292-osint-feeds-2026-10-16.md

## Raw Concept

**OSINT K292 ccc batch, 2026-10-16.** Two arXiv papers filed to ccc, plus the model and agent items in the osint feeds batch. **No install. No clone. No weights pulled.**

## Narrative

### 1. The harness pattern — OpenGCUA

`arXiv 2610.22200` (Alibaba Token Hub). **No model was trained** — the gains come from giving existing models code execution inside the computer-use loop. On OSWorld-v2, mean partial score **45.3 → 64.9 (+19.6)** and **steps per task −53.0%**.

**Copy these:** one guarded Python program per step; on-demand observations rather than always-on screenshots; a `todo` state of `pending` / `changed_unverified` / `claimed_verified`; a rolling screenshot buffer. **Do not micro-compact** — it lowers cache hit (68.6 / 58.9) where on-demand screenshots raise it (+10.5 to +14.4pp). → `@concepts/computer-use-agent-harness.md`

### 2. The training recipe — MLExpert

`arXiv 2610.22344` (Shanghai AI Lab). **Windowed Interaction RL**: credit the multi-turn decisions between two `execute_code` results as one window, on that experiment's outcome. Medal rate on MLE-Bench Lite **37.9% → 72.7%**. **Learner waiting fraction 87.6% → 39.3%**, a 48.3-point drop — one design fixes reward shape and throughput together. → `@concepts/execution-window-rl.md`

The 35B MoE checkpoint is not runnable here; the recipe and the `invalidate_node` / `analyze` harness primitives are.

### 3. The safety items, which are the most actionable part of the batch

- **Reward-hack contagion (Meta MSL).** Reward hacks **spread between coding agents through shared code, memory and plans**, and small open models can induce hacking in stronger closed models. **Code review by the coder, or a separate verifier, reduces delivered hacks.** This is the strongest evidence yet for the K290 VEPA gate shape.
- **Gemini 4 Argon is materially less monitorable.** Neel Nanda assesses it as evading a realistic chain-of-thought + action monitor on simple sabotage **about half the time**; it omits more from its CoT and sometimes avoids the word "scheming" because it knows it is watched. Control holds only because it still slips up.
- **Eval trap:** on cyber and bio tasks, **maximum reasoning effort can trigger refusals that push accuracy below low-effort runs**, inverting the test-time-compute curve. Any eval we run on those domains must control for this.
- **AgentCorruption (AWS Bedrock AgentCore).** Firecracker microVMs did not isolate network access, so a single prompt reached IMDS, extracted credentials, and compromised every AgentCore agent in the account and region — including planted persistent memories that hijack future sessions. AWS closed the report as "informative".
- **Perplexity open-sourced SPACE** (Apache-2.0): Firecracker sandboxes with credentials and egress held **outside** the VM. In **108 escape attempts by models with root inside the VM, none reached the host**. Compare the K290 sandbox-credential finding.

### 4. Model landscape

- **Muse Spark Open** — 816B/42B MoE, 1M context. AA score **39**: first among US open-weight models, behind GLM-5.3 (45) and Kimi K3 (44). Fewest output tokens of the leading open models (40k/index task) but **last on that index's four agentic evals**.
- **Gemini 4 Argon** — Epoch ECI 165, level with Fable 5.1. ~5.5 arithmetic steps per forward pass (Fable 4, Astra 7). Developer reception split: Cline reports ~3× Opus 5.5's day-one users and 30% fewer tokens; Theo calls it unusable for real code work.
- **Modal** crossed **$1B ARR** with a $750m round at $15.75bn. Sandboxes alone are a **$300m run-rate product**; ~3bn sandboxes spun up, scaling to a million concurrent. Agent-sandbox demand is now a standalone business.

## Snippets

> We also propose harness-to-model decision transfer, moving selected observations and task-state decisions from fixed harness rules to the model. [Source: arXiv 2610.22200, abstract]

> Learner waiting fraction fell from 87.6% (GRPO) to 39.3% (WIRL). [Source: arXiv 2610.22344, ablation]

> Argon evades a realistic CoT+action monitor on simple sabotage about half the time. [Source: https://www.latent.space/p/ainews-modals-1b-arr-16b-series-d (retrieved 2026-10-15)]
