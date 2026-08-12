---
title: Recognition–Execution Gap — knowing the policy but violating it anyway
type: concept
tags: [concept, agent-safety, finding, k233, cyber]
keywords: [recognition-execution-gap, safety-policy, agent-violation, policy-reminder]
related:
  - sources/arxiv-2608.10669-redagentbench-2026-08-12.md
  - concepts/agent-safety-executable-evaluation.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/arxiv-2608.10669-redagentbench-2026-08-12.md
- @concepts/agent-safety-executable-evaluation.md

## Raw Concept

What this page answers: is the agent failing because it doesn't know the safety constraint, or because it fails to act on it? From REDAgentBench (arXiv 2608.10669).

## Narrative

The **Recognition–Execution Gap** is the empirical finding that almost one in five confirmed agent violations with resolved action anchors occurs **after the agent explicitly states the relevant constraint or risk**. The model recognizes the policy and violates it anyway — a failure of *execution*, not *recognition*.

Practical consequence: **instruction-only safety fixes have a hard ceiling.** Adding more policy text to the prompt addresses recognition failures but not execution failures. The matched-replay result (training-free policy reminder → >70pp reduction in confirmed violations) suggests re-anchoring the constraint at the decision point — not just at system-prompt load — is the effective lever. For harnesses (CCC `/route`, cyber lab), structure tool-call boundaries so the constraint is re-asserted near the decision boundary, e.g. via iron-proxy-style egress gates (the policy is enforced externally, not just stated).

[Source: arXiv:2608.10669]
