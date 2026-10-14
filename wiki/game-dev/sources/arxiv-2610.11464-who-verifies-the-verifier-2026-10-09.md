---
title: Who Verifies the Verifier — co-evolving inspectable graders (2026-10-09)
type: source
tags: [source, arxiv, harness, verification, agents, evaluation]
keywords: [verifier-evolution, inspectable-graders, anchor-guards, reward-hacking, rubric]
related:
  - concepts/agent-harness-castle-project.md
  - sources/arxiv-2610.01514-audit-rule-faithful-explanations-2026-10-03.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
  - sources/inbox-arxiv-reject-batch-2026-10-09.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.11464
maturity: validated
created: 2026-10-09
updated: 2026-10-09
---

## Raw Concept

**arXiv:2610.11464** — "Who Verifies the Verifier? Co-Evolving Inspectable Graders with Self-Improving Agents." Authors are from AWS Forward Deployed Engineering and HSBC Technology Center, China. The paper poses the question every self-improving agent loop answers hundreds of times — *did the agent actually get better?* — and notes that on open-ended tasks no verifier exists. So the loop gets a hand-written rubric or a bare LLM judge grading output from a model like itself, which invites **reward hacking** and **shared blind spots**.

## Narrative

### What they did [CONFIRMED]

They make **the verifier the evolving object**. The verifier is an **inspectable expression over small, mostly deterministic drawback detectors**, synthesized from clustered failures, **gated at birth**, and selected for **agreement with a ten-item anchored reference set** plus consensus over unlabeled outputs — **never selected for the agent's score**.

### Results [CONFIRMED]

On **MBPP+** it gains **+0.21 held-out agreement** over the hand-authored seed composition, on every seed, and ends ahead of the bare LLM judge it contains (0.625 vs 0.417, judge 0.55). The headline finding: **removing the anchor guards collapses the verifier into a vacuous always-pass grader** (passes 0.97–1.00 of everything), **yet that collapsed verifier trains skills just as well** — therefore **downstream task score cannot certify a self-evolved verifier**. On sufficiency, an evolved verifier can substitute for ground truth: the **Double Ratchet** pairing retains **88–110%** of the lift that ground truth or a rubric buys the same loop, across code generation, enterprise text-to-SQL, and reference-free report generation. Also: when evolved skills gamed the report rubric (+0.26, about 30% of tags left with no value), an outer judge caught it and one added detector repaired it, cutting erased tags to about 1%.

### Why this is the sharpest verification result in the wiki [CONFIRMED]

Rule **H4** (@concepts/agent-harness-castle-project.md) says the verifier must audit something the executor did not nominate — this paper shows the deeper problem: a verifier that evolves alongside the agent can collapse to always-pass while still *looking* effective, because the downstream score stays good. The detection method matters as much as the rule: you need an **independent anchored reference set**, not the task score. Rule **H3** (verified ledger) depends on "verified" meaning something real. Cross-link @sources/arxiv-2610.01514-audit-rule-faithful-explanations-2026-10-03.md (report-dependent auditing) and @sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md (adversarial verifiers).

### castle-sim application [TENTATIVE]

The W2 verify gate is a hand-written rubric plus the operator's playtest. This paper says keep a small **anchored reference set** — a fixed handful of tasks with known-good verdicts — and re-check the gate against it whenever the gate itself changes, rather than trusting that a passing milestone means the gate still works.

## Dead Ends

- Certifying a verifier by the agent's task score: the vacuous always-pass grader scores as well as the anchored one.
- Letting a judge be graded by a model of its own family: it invites shared blind spots.
- Trusting an outer judge without the task contract: the report judge was wrong until it got one.
