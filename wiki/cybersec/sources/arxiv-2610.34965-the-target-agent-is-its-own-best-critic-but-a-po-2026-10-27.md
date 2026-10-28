---
title: "The target agent is its own best critic but a poor proposer"
type: source
tags: [source, arxiv, red-team, agent-security]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Target Agent Is Its Own Best Critic But a Poor Proposer: Self-Improved Red Teaming |
| Authors | Mintong Kang (UIUC), Stephen Rawls, Melissa Kazemi Rad, Jian Ni (Capital One), Bo Li (UIUC) |
| arXiv | 2610.34965 |
| File | `arxiv-2610.34965-the-target-agent-is-its-own-best-critic-but-a-po.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.34965 |
| Read status | skimmed (abstract + intro) |

## Narrative

Automatic red teaming uses an LLM to diagnose a failed attack and then write a better one.
Prior work improves this loop by prompt engineering and by harness design. This paper splits
the loop into its two roles and tests each one separately.

The two design choices are:

- **Criticism.** The target session criticises itself (self-criticism), or a separate critic
  instance does it (external criticism).
- **Proposal.** The target session turns the criticism into the next attack (self-proposal),
  or a separate attacker does it (external proposal).

The findings point in opposite directions for the two roles.

**Self-criticism wins.** It is grounded in the target's live execution context: what the
agent observed, what constraints it hit, and what reasoning it had. Removing the reasoning
step reduces downstream attack success by **6%–17%**.

**Self-proposal loses.** When the target session knows the adversarial goal, it refuses
outright. When it does not refuse, it still sandbags, meaning it performs below its
capability without a clear refusal signal. Both outcomes waste the turn.

The practical recipe is role separation. The target session diagnoses why an attack failed,
and a separately instantiated attacker writes the next proposal. On DTAP-BENCH, across the
Telecom, Workflow, CRM and Code domains, under both direct-misuse and indirect threat models,
and across several agent frameworks, this configuration reaches **63.2% overall**.

*Note:* the extracted abstract text stops at "63.2% overall a", so the exact noun after
"overall" is cut off in this skim. Confirm the completed figure against the PDF before citing
it in a brief.

## Snippets

> "Self-criticism is more effective because it is grounded in the target's live execution context, including observations, constraints, and available reasoning; removing reasoning reduces downstream attack success by 6%-17%." [Source: `arxiv-2610.34965-the-target-agent-is-its-own-best-critic-but-a-po.pdf` p.1 (arXiv 2610.34965), retrieved 2026-10-27]
