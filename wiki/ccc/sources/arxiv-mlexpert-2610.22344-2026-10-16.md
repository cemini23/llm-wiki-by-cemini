---
title: "MLExpert — a 35B agentic model for autonomous ML engineering, and the WIRL recipe (arXiv 2610.22344)"
type: source
tags: [agents, rl, ml-engineering, harness, source, k292]
keywords: [MLExpert, WIRL, execution window, MLE-Bench, outcome-guided SFT, experiment tree, Kaggle-MLE factory, reward shaping]
related:
  - concepts/execution-window-rl.md
  - concepts/k292-ccc-wave.md
  - concepts/agent-harness-verification-bottleneck.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @concepts/execution-window-rl.md — the transferable training recipe
- @concepts/k292-ccc-wave.md — K292 ccc wave hub
- @concepts/agent-harness-verification-bottleneck.md

## Raw Concept

Title: MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering
Authors: Shangheng Du, Jinxin Shi et al. (East China Normal University; Shanghai AI Laboratory)
Type: arXiv 2610.22344v1 [cs.AI], 23 pages, 15 Oct 2026
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.22344-mlexpert-towards-a-generalist-agentic-model-for.pdf`
Retrieved: 2026-10-16
Artifacts: code `github.com/InternScience/MLExpert` · weights `huggingface.co/InternScience/MLExpert`
Read status: read

## Narrative

A **35B MoE** agentic model trained to run long-horizon machine-learning experiments. **Here the model does the work** — and the paper shows the gain survives under a Claude Code harness, so it is not harness-only.

**The training problem it names:** one long MLE run contains many costly experiments, and the feedback from any experiment reflects several preceding decisions. Training must therefore select supervision from long trajectories and learn from intermediate outcomes as they arrive.

**Two stages.**

1. **Hierarchical agentic SFT** — general tool-use and coding first, then MLE plus literature-derived science, with **outcome-guided trajectory selection**.
2. **Windowed Interaction RL (WIRL)** — the multi-turn decisions between two successive `execute_code` results form an **execution window**, and the whole window receives **one shared reward** from that experiment's outcome. A local trend reward and token-level policy correction support asynchronous collection. **Infrastructure-error windows are not trained on.**

**The environment.** The **Kaggle-MLE Factory** builds executable tasks: 11,649 Meta-Kaggle entries reduced to **154 tasks**, plus 134 MLE-Dojo tasks and 164 Nature papers. Teacher trajectories: **636 trajectories → 5,539 input records, ~302.45M packed tokens, 1,173 sequences (mean 257,843 tokens), 8 epochs**, from GLM-5.2 and Qwen3.8-Max.

**Results.**

| Benchmark | Base (Qwen3.6-35B-A3B) | MLExpert | Frontier comparison |
|---|---|---|---|
| MLE-Bench Lite (22 tasks), medal rate | **37.9%** | **72.7%** | GLM-5.3 72.7, Kimi-K3 72.7, GPT-5.5 72.7, GPT-5.6 Sol 77.3 |
| Under Claude Code harness | 42.4% | 69.7% (+27.3) | — |
| NatureBench Lite, surpass-SOTA | 0.0% | **50.0%** | Kimi-K3 70.0 |
| AIME scaffold optimisation | 23.3 | **43.7** | GLM-5.3 48.1 |
| MLS-Bench-Lite mean reward | 0.322 | **0.425** (better on 10 of 12) | — |

**Stage ablation:** base 37.9 → +general SFT 47.0 → +MLE SFT 62.1 → **+WIRL 72.7**. **RL comparison:** GRPO 56.1, PPO 60.6, WIRL without trend 66.7, WIRL without policy correction 65.2, **WIRL 72.7**.

**The efficiency number is the striking one.** **Learner waiting fraction fell from 87.6% under GRPO to 39.3% under WIRL, a 48.3-point drop.** The window boundary is what makes asynchronous collection work: credit is assigned at a natural checkpoint, so the learner does not stall on a rollout that has not finished.

**The harness, which is separately usable.** A model-directed ReAct loop over an **experiment tree**. Each solution node is candidate code plus logs plus metadata, parent-linked for backtracking. The tool set is worth copying verbatim: `execute_code`, `patch_code` / `write_full_code`, `analyze` (a sub-agent with its own context that returns only a summary), `write_plan` / `edit_plan`, `list_nodes` / `select_node`, **`invalidate_node`** (exclude overfit or leaky candidates), `update_answer` / `get_current_answer`. Long-horizon organisation is: keep a running submission candidate, revise from execution feedback, compress early history.

**Limitations.** The paper prints **no limitations section**. Visible caveats: MLE-Bench Lite is only 22 tasks; frontier numbers are single runs while only same-scale and MLExpert get three runs; the Kaggle-MLE Factory uses an LLM pipeline with manual review; results rest on Kaggle data.

### Why it matters here

**The recipe transfers, the checkpoint does not.** A 35B MoE needs H200-class hardware, so we will not run it. What we can use:

1. **WIRL.** Assign reward at the **experiment boundary**, not per token and not per whole trajectory. This is the same instinct as the OpenGCUA `todo` state and the VEPA evidence gate — score at the checkpoint where the world answers back.
2. **`invalidate_node`.** An explicit action for marking a candidate as overfit or leaky, rather than silently keeping it. That is a harness primitive we do not have.
3. **The `analyze` sub-agent** that runs in its own context and returns a summary — the context-isolation pattern the K290 wave also landed on.
4. **Don't train on infrastructure errors.** An obvious-sounding rule that most pipelines get wrong.

**No install. No weights pulled. No trade.**

## Snippets

> Windowed Interaction RL (WIRL) treats the multi-turn decisions between successive experiment results as an execution window and assigns it a shared outcome-based reward. [Source: arXiv 2610.22344, abstract]

> On MLE-Bench Lite, MLExpert improves the average medal rate of the base model from 37.9% to 72.7%, achieving performance comparable to larger frontier models such as Kimi-K3 and GLM-5.3. [Source: arXiv 2610.22344, abstract]

> invalidate_node (exclude overfit/leaky candidates) [Source: arXiv 2610.22344, tool inventory]
