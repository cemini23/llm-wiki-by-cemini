---
title: "Knowing when to intervene — causal evaluation of agent interventions"
type: source
related:
  - concepts/causal-intervention-evaluation.md
  - concepts/streaming-trajectory-monitor-pre-execution-gate.md
  - concepts/subagent-orchestration.md
  - concepts/agent-completion-verification-gates.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Knowing When to Intervene: Causal Evaluation of AI Agents |
| Author | Ayush Sawarni, Wenqian Xing, Tijana Zrnic, Ramesh Johari, Vasilis Syrgkanis (Stanford University) |
| Type | arXiv paper (cs.AI), 2611.09792 |
| Location | `research to be indexed/ccc/arxiv-2611.09792-knowing-when-to-intervene-causal-evaluation-of-a.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 35 |
| Read status | read |

## Narrative

A benchmark score says whether an agent succeeds. It does not say whether a human or a stronger model should step in at a given step. The authors frame that question as causal inference: what is the causal effect of an intervention at this decision on the final outcome?

The design is a **micro-randomized trial** inside each trajectory. At every eligible decision the harness records the proposed action and the observed history, randomly assigns intervention or control, and lets the agent continue. Only black-box input-output access is needed.

Three estimands follow:

- **Blip with randomized continuation** — the effect of intervening at one decision when later interventions stay randomized. Estimated by cross-fitted AIPW.
- **Blip with no-treatment continuation** — the effect of intervening when no later intervention occurs. Estimated with structural nested mean models and g-estimation.
- **Policy gain** — the off-policy value of a target intervention policy relative to never intervening.

The same data also produces a **decision impact score** per group of decisions. That score gives a safety leaderboard for audit prioritisation.

Experiments cover tau-bench Retail, ToolSandbox, and ImpossibleBench. Effects vary substantially across actions and states. In tau-bench Retail, tool-call review improved task success for several order-handling groups. In ImpossibleBench, adversarial feedback raised the probability of prohibited test edits in specific states, including near-completion states with contradictory tests.

The practical point for Cemini: a review gate is a treatment, not a free safety win. It can help or hurt, and the sign depends on where in the trajectory it fires. Randomised, recorded interventions are the only cheap way to learn which.

## Snippets

> "The value of such interventions is fundamentally a causal inference question, asking whether the causal effect of such an intervention is beneficial for the final outcome." [Source: arxiv-2611.09792-knowing-when-to-intervene-causal-evaluation-of-a.pdf p.1]

> "We find that intervention effects vary substantially across agent actions and states." [Source: arxiv-2611.09792-knowing-when-to-intervene-causal-evaluation-of-a.pdf p.1]
