---
title: Agent-Safety Executable Evaluation — measuring violations, not just ASR
type: concept
tags: [concept, agent-safety, evaluation, red-teaming, k233, cyber]
keywords: [asr, executable-evaluation, service-sandbox, final-state, adjudication, agent-safety]
related:
  - sources/arxiv-2608.10669-redagentbench-2026-08-12.md
  - concepts/recognition-execution-gap.md
  - sources/newsletter-rss-tldrsec-2026-08-13-tldr-sec-341---hugging-face-incident-black-hat-t.md
maturity: draft
created: 2026-08-12
updated: 2026-08-13
---

## Relations

- @sources/arxiv-2608.10669-redagentbench-2026-08-12.md
- @concepts/recognition-execution-gap.md
- @sources/newsletter-rss-tldrsec-2026-08-13-tldr-sec-341---hugging-face-incident-black-hat-t.md — agent-identity/least-privilege + Beyond Zero = executable-safety evaluation surface

## Raw Concept

What this page answers: why a single attack-success-rate (ASR) number is a misleading safety metric for tool-using LLM agents, and how to measure violations faithfully. Synthesized from REDAgentBench (arXiv 2608.10669).

## Narrative

ASR collapses four distinct stages — **exposure** (attack reaches agent), **execution** (agent takes action), **observation** (effect is seen), **adjudication** (effect is judged harmful) — and conflates actual violations with evidence visibility. REDAgentBench's answer: **executable evaluation** — derive attacks from explicit safety constraints, run them in isolated service sandboxes, and verify harm from **service receipts and final-state changes**, not model text.

Findings that matter when building any agent-safety eval (including the local-abliterated-lab pentest harness):
- Macro-average ASR was 65.69% across 1,661 cases / five service surfaces / six models / three harnesses — but reported ASR **varies with harness and evidence view**, and **disclosing the eval context changes execution behavior** (the benchmark perturbs what it measures).
- A state-grounded diagnostic cohort showed ~1 in 5 confirmed violations with resolved action anchors occurs **after the agent states the constraint/risk** — i.e. knowing the policy does not prevent violating it.
- A **training-free policy reminder** cut confirmed violations by >70pp in matched replay — the cheapest effective intervention tested.

Steal: when evaluating Cemini/lab agent safety, (1) verify effects from external state, not output text; (2) report ASR *with* the evidence view; (3) bake a policy reminder into the system prompt as a near-free mitigation.

[Source: arXiv:2608.10669]
