---
title: Runtime verification of many natural-language rules — the VFM pattern
type: concept
related:
  - sources/arxiv-runtime-nl-criteria-verification-2611.23074.md
  - concepts/agent-harness-castle-project.md
  - concepts/npc-prompt-robustness.md
maturity: draft
updated: 2026-11-22
---

## Raw Concept

Opened on the 2026-11-22 ingest of @sources/arxiv-runtime-nl-criteria-verification-2611.23074.md. The question: how do we check an agent trace against many plain-text rules, and learn which rule failed, without a judge call per rule?

## Narrative

### The shape of the method

One shared prefix, many cheap branches. The verifier reads the context and the agent output one time. Each rule then runs as an isolated attention branch over the cached prefix. The output per rule is a three-way label: YES, NO, or N/A.

The N/A label matters. A rule set that mixes "no writes outside the project" with "cite a licence for each asset" has rules that do not apply to every step. A two-way pass/fail forces a false verdict on the inapplicable ones. [Source: arxiv-runtime-nl-criteria-verification-2611.23074.md p.2]

### Cost profile

| Regime | Cost | Practical meaning |
|--------|------|-------------------|
| 1,000 rules, 4K prefix, 4B model, one H100 | 1.81 s, under 11 GB VRAM | Fits inside one agent turn |
| Same work with a size-matched generative judge | about 6.8 s, about 78 GB | Does not fit a laptop |

[Source: arxiv-runtime-nl-criteria-verification-2611.23074.md p.9]

### The measured failure

The method is not a gate. On real insurance-benefit calls, the best fine-tuned model approved about 20% of the true violations, and it did so with high confidence. Confidence-based escalation recovers few of those errors. [Source: arxiv-runtime-nl-criteria-verification-2611.23074.md p.9]

A verifier that is wrong with confidence is worse than a slow verifier that is asked to explain itself. So the design rule is: use the fast verifier to find and localize, then send the flagged rule to a slower reasoning judge.

### Fit for the castle-sim harness

The harness rules that suit this pattern are the ones that are cheap to state and cheap to see in a trace:

- The session wrote only inside the project tree.
- The session did not delete or rename an asset without a log line.
- Each new external asset names a licence.
- The session did not run a command the operator did not approve.

These are close to the shape that the paper trains on: a short, positively phrased, atomic criterion that a human auditor could score from the trace. [Source: arxiv-runtime-nl-criteria-verification-2611.23074.md p.3]

Two constraints apply to a hobby project:

1. **No local 4B GPU.** The verifier must run as a batch step, or on rented hardware, not on the same laptop that runs Godot.
2. **No hard gate.** Pair the verdict with @concepts/godot-stagehand-ci-smoke-plan.md and with the operator playtest. The verifier adds a named rule violation to a failure report. It does not decide the merge.

### Contrast with the NPC acceptance test

@concepts/npc-prompt-robustness.md asks whether an NPC prompt is stable and responsive. That test needs a behavior sweep, not a rule check. This page asks a different question: did the agent break a stated rule? Both belong to the verify lane, and neither replaces the other.

## Dead Ends

- Treating an N/A verdict as a pass. N/A means the rule did not apply to that step, not that the agent obeyed it.
- Training a small verifier on labels from the same model that wrote the trace. The paper records the label noise as a known limit.
