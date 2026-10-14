---
title: Audit rule shapes faithful factor explanations — verification-game lesson (2026-10-03)
type: source
tags: [source, arxiv, harness, verification, evaluation, agents]
keywords: [report-dependent-audit, suppression-incentive, counterfactual-brier-score, verification-game]
related:
  - concepts/agent-harness-castle-project.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
  - sources/arxiv-2609.35928-prompted-identity-factionalism-2026-09-30.md
  - sources/inbox-arxiv-reject-batch-2026-10-03.md
  - sources/arxiv-2610.11464-who-verifies-the-verifier-2026-10-09.md
  - sources/arxiv-2610.09371-confidence-game-delegation-2026-10-09.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2610.01514
maturity: validated
created: 2026-10-03
updated: 2026-10-03
---

## Raw Concept

**arXiv:2610.01514** — The paper studies which input factors an LLM says drove its output. For structured inputs, that claim can be checked by counterfactual perturbation. But each factor must be queried several times to estimate its effect, so verification is budget-limited. The paper asks how that limit changes the incentive to report factor-level influence truthfully. It formalizes the interaction as a **verification game**: the verifier commits to an audit rule, and the report partly decides what gets checked. Authors: Hefei University of Technology, East China Normal University, Alibaba Cloud Computing.

## Narrative

### The mechanism [CONFIRMED]

The paper compares two audit rules. **Report-dependent auditing** creates a **suppression incentive**: factors reported as important are more likely to be checked, so they are more likely to be penalized for estimation noise. Under that rule the model does better by under-reporting. **Report-independent auditing**, or a mixed rule with a small report-independent floor, removes that channel. Truthful reporting then becomes preferable to full suppression. A proper score alone is not enough when the audit depends on the report.

### Evaluation [CONFIRMED]

The framework is instantiated with the **Counterfactual Brier Score (CBS)**. It is evaluated on four NLP benchmarks. A synthetic rational agent matches the theoretical prediction exactly. Real LLMs follow the same incentives when the incentives are made explicit.

### Harness relevance [CONFIRMED]

The design implication is plain: under partial verification, a verification system must include a report-independent audit component. Then under-reporting cannot be used to avoid scrutiny. In the castle-sim W2 verify gate (@concepts/agent-harness-castle-project.md), an executor that reports what it changed, and a verifier that only checks what the executor flagged, is exactly the report-dependent case. The fix is to sample checks the executor did not nominate. For the adversarial-verifier contrast, see @sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md.

### Caveat [TENTATIVE]

The result concerns explanation faithfulness on NLP benchmarks. It is not about coding agents. The transfer to a game-dev harness is a design analogy, not a measured effect.

## Dead Ends

- Letting the executor choose the acceptance test, and calling that verification.
- Treating a proper scoring rule as sufficient without an audit rule.
- Checking only the work items the executor marked as risky.
