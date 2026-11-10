---
title: "Causal evaluation of interventions inside an agent trajectory"
type: concept
related:
  - sources/arxiv-knowing-when-to-intervene-2611.09792.md
  - concepts/streaming-trajectory-monitor-pre-execution-gate.md
  - concepts/subagent-orchestration.md
  - concepts/agent-completion-verification-gates.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: does a review gate at step k actually improve the outcome, and where should it fire?

Synthesised from `@sources/arxiv-knowing-when-to-intervene-2611.09792.md`.

## Narrative

A benchmark score says an agent succeeds or fails. It does not say whether a human or a stronger model should step in at a given step. The paper frames that as causal inference on a dynamic treatment.

The design is a **micro-randomized trial** inside each trajectory. At every eligible decision the harness logs the proposed action and history, randomly assigns intervention or control, then lets the agent continue. Only black-box access is required.

Three estimands:

1. **Blip, randomized continuation** — effect of intervening once, with later interventions still randomized. Estimated by cross-fitted AIPW.
2. **Blip, no-treatment continuation** — effect of intervening once and never again. Estimated with structural nested mean models and g-estimation.
3. **Policy gain** — off-policy value of an intervention policy against never intervening.

Per-group blip effects give a **decision impact score**, which orders decision types by the expected change in outcome.

Experimental results across tau-bench Retail, ToolSandbox, and ImpossibleBench:

- Tool-call review helped task success for several order-handling groups in tau-bench Retail.
- Effects varied across capabilities and agents in ToolSandbox.
- Adversarial feedback raised prohibited test edits in specific states, including near-completion states with contradictory tests.

### Why this changes gate design

A guardrail is a treatment with a sign, not a free safety win. Three consequences:

- **Placement matters more than existence.** The same review can help at one step and hurt at another.
- **Counterfactual record needed.** To learn the sign, the gate must sometimes *not* fire, and the run must be recorded. A gate that fires on every case generates no comparison group.
- **State-dependent rules beat uniform rules.** "Review every database write" is a weaker design than "review writes in order-handling states".

### Cemini fit

`step-gate` already classifies proceed, hold, or escalate before a tool call. The paper argues that its HOLD rule should be learned from recorded outcomes, not fixed by intuition. A cheap first step is to log the counterfactual: record the tool call that a HOLD blocked, and later check whether the final artifact would have been wrong. [OPEN QUESTION 2026-11-10]

## Snippets

> "The impact of an intervention during task execution depends on the current context and environment, as well as the agent's future behavior under its policy." [Source: arxiv-2611.09792-knowing-when-to-intervene-causal-evaluation-of-a.pdf p.2]
