---
title: Inadvertent context leakage — secrets in benign LLM outputs (Fairoze et al., Meta FAIR)
type: source
tags: [privacy, agents, safety, covert-channel, alignment]
keywords: [inadvertent-leakage, suppression, predicate-inference, SSN, Opus-4.6, SPIFFE, context-window]
related:
  - concepts/inadvertent-context-leakage.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/agent-runtime-identity-adr.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
read_status: skimmed
---

## Relations
- @concepts/inadvertent-context-leakage.md
- @concepts/agent-safety-executable-evaluation.md
- @concepts/agent-runtime-identity-adr.md

## Raw Concept
- **title:** Inadvertent Context Leakage in Language Models
- **author:** Jaiden Fairoze, Neal Mangaokar, Kamalika Chaudhuri, Sanjam Garg, Saeed Mahloujifar (FAIR / Meta Superintelligence Labs; UC Berkeley; Google DeepMind)
- **type:** arXiv paper
- **location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.19857-inadvertent-context-leakage-in-language-models.pdf`
- **retrieved:** 2026-08-21
- **pages:** arXiv HTML (abstract, threat model, digit recon, suppression, SSN agent attack, discussion)
- **read-status:** skimmed

## Narrative
A model can refuse “what is the secret?” at 0% linguistic leakage and still encode the secret in benign outputs. The paper frames this as a predicate-inference game with a *model-specific adaptive* black-box decoder (text only; no logits). Linguistic judges that look for verbatim/paraphrased secrets miss the channel.

Controlled numeric secrets, eight proprietary models, ordinary templates: 2-digit reconstruction is near-perfect on Claude Opus 4.6 and Gemini 3.1 Pro; 4-digit exact match 82% on Opus 4.6 (adaptive conditioning nearly doubles 44%→82%); 8-digit per-digit 41% on Gemini 3.1 Pro vs 10% chance. A resistant tier (Grok 4.1 Fast, GPT-5.4 nano) stays at chance for N≥4. Stronger instruction-following leaks more.

Suppression — the model systematically avoiding the protected value — tracks leakage (Spearman ρ=0.95, p=0.0011). Verbose confidentiality instructions *increase* leakage on Opus (per-digit 0.054 terse → 0.643 verbose policy). OLMo-3-32B-Think channel entropy falls Base 2.91 bits → RLVR 1.37 bits.

Semantic predicates on CIMemories-style user memories: 0.319 advantage vs 0.058 for a linguistic judge. Active attack: RL (GRPO) injection encodes an SSN as exclamation-mark counts. Opus Phase-1 leading digit 97.1%, remaining eight 76.5%; Gemini 88.6% / 46.8%. Direct-request control never extracts the SSN from Gemini (0/70) and Claude often refuses in language while the covert channel still works. Architectural implication: secrets that share a context window with third-party-visible generation are not safe under refusal training.

OSINT steal: treat agent outputs as covert channels; do not put secrets in context that a third party can observe; pair with ADR telemetry and SPIFFE `act=agent`. No exploit recipes in this wiki — mechanism + policy only.

## Snippets
> We find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. [Source: arxiv-2608.19857-inadvertent-context-leakage.pdf p.1]

> We observe that more capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, suggesting leakage is a byproduct of capability as opposed to a patchable bug. [Source: arxiv-2608.19857-inadvertent-context-leakage.pdf p.1]

> Suppression … tracks leakage across the eight models (Spearman ρ=0.95, p=0.0011). [Source: arxiv-2608.19857-inadvertent-context-leakage.pdf p.1]

> An RL-trained adversary that extracts full Social Security Numbers from a production-style agent [by] decoding a predetermined output feature [exclamation-mark counts]. [Source: arxiv-2608.19857-inadvertent-context-leakage.pdf p.1 / §3.3]

Paper: https://arxiv.org/abs/2608.19857 [Source: URL (retrieved 2026-08-21)]
