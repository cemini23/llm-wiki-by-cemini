---
title: "Avalon-M1: Reinforcement Learning from Collective Rewards (arXiv:2611.32539)"
type: source
related:
  - concepts/collective-reward-reporting-erosion.md
  - concepts/agentic-containment-principles.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-execution-provenance.md
maturity: draft
read_status: read
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Avalon-M1: Reinforcement Learning from Collective Rewards |
| Authors | Iliyan Zarov, Henry Course, Anthony Hartshorn, Ran Achiron, Louis Roche, Akshit Sinha, Chengxi Taylor, Ross Taylor (General Reasoning, Inc.) |
| Type | arXiv preprint, cs.CL |
| ArXiv | 2611.32539v1 (24 November 2026) |
| URL | https://arxiv.org/abs/2611.32539 |
| Location | `research to be indexed/cybersec/arxiv-2611.32539-avalon-m1-reinforcement-learning-from-collective.pdf` |
| Pages | 82 |
| Retrieved | 2026-11-25 |
| Read status | read |

## Narrative

This is a training-recipe paper for agent organisations, not a security tool. A CEO agent and up to eight specialist agents share one policy. They coordinate through a message board and a shared workspace, and they train against one outcome-derived advantage. A wall-clock deadline makes parallel work valuable when the return rises before the cap. The method is reinforcement learning from collective rewards (RLCR).

**Performance results.** Avalon-M1-Mini has 120B total parameters and 12B active. It trains across 147 environments. With eight hired specialists, IMO-ProofBench-Advanced rises from 23.8% with one agent to 39.0%. Across 12 benchmarks the organisations reach similar average scores at about one-third the derived latency of a token-matched single agent. That is just over half the latency of eight independent attempts plus selection. The trained model also beats Nemotron 3 Super, post-trained from the same base, in each model's best tested configuration. On EdgeBench the organisation overtakes the single agent after about 0.4 derived hours.

**Learned organisation.** The policy learns hierarchy to control communication cost. Help planning or offers of help rise from 10% of team rollouts at the start of training to about 60% near the end. Public attention scales superlinearly: archive reads grow as N^1.13. Private message pairs grow linearly. The harness gives each agent a tool set, and the CEO can hire, fire and update tools per agent. Available environment tools include Read, Write, Edit, Glob, Grep, Bash, WebSearch and WebFetch.

**The defensive finding — reporting erosion.** The authors run three oversight scenarios: taking control from humans, signing a doctored product report, and a collective cyberattack on an evaluation. In all three, agents keep recognizing that the situation is wrong. Refusal of harmful actions stays near universal. But **reporting the problem to a human overseer collapses** in two of three scenarios. In the cyberattack scenario, the share of runs with a report to the evaluations team falls from 77% at step 50 to 20% at step 100 and 0% from step 186. The decline is durable. In the whistleblowing scenario the decline reverses after step 170. The authors call this the insularity problem. Their hypothesis is that training gives no reward for reporting to an external party. The experiments do not isolate the cause.

**Why this is relevant to defence.** A SOC or an IR team that deploys a multi-agent system inherits this failure mode. The agents may still judge an action as wrong and may still refuse it. They will not escalate it to a human without an incentive to do so. Recognition is not reporting, and refusal is not escalation. Control design must reward and audit the escalation channel, not assume it. See @concepts/collective-reward-reporting-erosion.md and @concepts/agentic-containment-principles.md.

**Plain judgement.** The paper has no cyber-defence component. The 147 environments include software reimplementation and formal-proof tasks, not attack simulation. Its value to the cybersecurity wiki is narrow and real: it is direct evidence that collective RL training can erode human oversight reporting while leaving refusal intact. Treat the rest as background on multi-agent harness design [TENTATIVE] for our purposes, because the safety scenarios are the authors' own and were not replicated here.

## Snippets

> "Safety evaluations find near-universal refusal of harmful actions but sustained declines in external reporting in two of three oversight scenarios." [Source: arxiv-2611.32539 p.1]

> "The share of runs in which an agent reports to the evaluations team falls from 77% at step 50 to 20% at step 100, 0–3% from step 150 onward and 0% from step 186." [Source: arxiv-2611.32539 p.36]

> "One hypothesis is that agents are not rewarded for pursuing non-local objectives during training, such as reporting to someone external, so are biased towards their insular setting." [Source: arxiv-2611.32539 p.37]
