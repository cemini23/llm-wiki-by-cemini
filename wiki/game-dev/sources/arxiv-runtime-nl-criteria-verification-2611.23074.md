---
title: VFM — runtime verification of many natural-language criteria (NeurIPS 2026)
type: source
related:
  - concepts/runtime-nl-criteria-verification.md
  - concepts/agent-harness-castle-project.md
  - sources/arxiv-agent-trust-infrastructure-2611.23202.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2611.23074
maturity: draft
created: 2026-11-22
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Runtime Verification of Multiple Natural Language Criteria for Agent Governance |
| Authors | Silviu Pitis, Parand A. Alamdari, Jessica Tang, Toryn Q. Klassen, Sheila A. McIlraith |
| Affiliation | University of Toronto, Vector Institute |
| Type | arXiv:2611.23074v1 [cs.CL], 17 November 2026, 27 pages; NeurIPS 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf` |
| Retrieved | 2026-11-22 |
| Read status | read |
| Code | https://github.com/spitis/vfm |

## Narrative

### The problem

An agent runs under hundreds of natural-language rules at once. The rules come from the developer, the deployer, a regulator, and the user. Rule compliance drops as the rule count and the context length grow. The paper cites a 2026 case where a coding agent deleted a production database against explicit system-prompt rules. [Source: arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf p.1]

Existing guards work one of two ways. Fixed-taxonomy guards are fast, but their rules are fixed at training time. Generative judges accept free-text rules, but each verdict costs a full generation, so they are too slow for a large rule set. [Source: arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf p.2]

### The method

The Verifier Foundation Model (VFM) encodes the shared context and target text once. It then scores N criteria as independent branches under a tree-attention mask. The shared prefix key-value cache is computed one time. Each branch returns a softmax over three labels: YES, NO, and N/A. [Source: arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf p.1-2]

The training corpus is CriteriaBank: 394K (context, target, criterion, verdict) tuples over 321K distinct criterion strings, from five data streams. [Source: arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf p.2]

### Results

| Benchmark | VFM-4B | Nearest baseline |
|-----------|--------|------------------|
| Synthetic governance, held-out accuracy | 88.8% | Direct-FT-4B 88.2%; GPT-5.4 low-reason 83.9% |
| Synthetic governance, transfer accuracy | 77.7% | Direct-FT-4B 75.3%; GPT-5.4 75.5% |
| INSURE-Dial, 50 real calls | 86.5% | Direct-FT-4B 87.0%; GPT-5.4 per-criterion 74.6% |
| DynaBench trace-level F1 | beats DynaGuard-4B | DynaGuard-4B |

[Source: arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf p.7-8]

Latency is the headline claim. On one H100, VFM-4B scores 1,000 criteria against a 4K-token prefix in 1.81 s, with peak VRAM under 11 GB. A size-matched generative judge needs an estimated 6.8 s for the same work at 78 GB. [Source: arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf p.9]

### Limits the authors state

The authors are direct about the gap to enforcement:

- On real insurance calls, the best fine-tuned verifier approves about 20% of the gold violations, mostly with high confidence.
- CriteriaBank labels are model-generated, so their errors carry into the model.
- The governance benchmark is synthetic.
- The model does not model dependencies between criteria.
- Robustness against an agent that is optimized against the verifier is untested.
- Evaluation is English-only and text-only.

The paper concludes that this class of verifier suits monitoring and escalation, not standalone enforcement. [Source: arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf p.9]

### Relevance to game dev

There is no game content in the paper. The link is the harness verify lane. A castle-sim agent session has a short rule set: no writes outside the project tree, no asset deletion, no licence violation. The VFM pattern shows how to check many such rules in one pass and to name the rule that failed.

Two costs are real. A 4B verifier needs a GPU with about 11 GB free, which is not a laptop default. And a 20% false-approval rate on real data is too high for a hard gate. The pattern is the interesting part, not the checkpoint. See @concepts/runtime-nl-criteria-verification.md.

## Snippets

> "On a single H100, VFM-4B evaluates 1,000 criteria against a 4K-token context in under 2s at <11 GB VRAM, making it suitable for runtime verification." [Source: arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf p.1]

> "VFM-style verification is therefore best suited to monitoring and escalation rather than standalone enforcement." [Source: arxiv-2611.23074-runtime-verification-of-multiple-natural-languag.pdf p.9]

## Dead Ends

- Do not use VFM output as the only merge gate. The measured false-approval rate on real calls is about 20%.
- Do not assume the tree-attention trick transfers to a consumer GPU. The 11 GB figure is for a 4B backbone.
