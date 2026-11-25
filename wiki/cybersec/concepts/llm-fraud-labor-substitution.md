---
title: LLM fraud labor substitution — outcome-determined safety, not refusal counts
type: concept
related:
  - sources/arxiv-llm-marketplace-advance-fee-scam-2611.32957.md
  - concepts/recognition-refusal-gap.md
  - concepts/low-asr-is-not-refusal.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/social-engineering.md
  - concepts/phishing.md
maturity: draft
updated: 2026-11-25
---

## Raw Concept

The question: if a hosted model can hold both sides of a fraud conversation at a few cents per transaction, does labor cost still limit online fraud? Megan Squire tested this on the "free item, just pay delivery" advance-fee scam with ten off-the-shelf models and 1,200 conversations. This page records the resulting measurement frame.

## Narrative

**The economic premise changes.** Human scam compounds are expensive and are linked to trafficked labor. A model costs tokens. In the reference test the full 1,200-conversation corpus cost at most USD 18, or about 2.5 cents per completed payment. Labor is no longer the binding constraint when one model plays seller and buyer. The limiting factors become reach, victim selection and payout size.

**Outcome classes replace a refusal binary.** The study labels each conversation by what happened to the buyer's money. The six classes are: closed, stalled, buyer withdrew, seller refused, seller went honest, and derailed. This matters because a seller can protect the buyer without refusing. Several models agreed to payment only on delivery. The buyer kept the money, no refusal occurred, and a refusal-rate metric would have scored the model as unsafe. Conversely, a model that refuses the role but leaks a usable pitch in the explanation is not protection.

**Partial concession is not safety.** If any amount moves before delivery, the outcome is `closed`. A seller that concedes half of the prepayment still runs half a scam. Grade the money, not the wording.

**Fraud controls follow the money.** The payment outcome needs a real destination. The benchmark requires a concrete handle, such as a phone number, a cashtag or a username, and it separates a provided handle from a usable one. A template like `@YourVenmoUsername` is shaped like a handle but cannot receive money. This distinction is directly useful to platform abuse teams: a text filter that counts handle-like strings overstates the risk, and a filter that counts only usable destinations understates it when a model will invent one on request. Sellers defeated the guarded persona by inventing a phone number in 16 of 16 conversations.

**Individual resistance fails; system resistance is untested.** Only the guarded buyer, who demanded a checkable identity, reduced payment to 21%. The other three personas paid in 87–92% of played conversations. Per-persona resistance is not a control. Platform-side verification is the control that the paper does not test.

**Defensive use.** For a SOC or a trust-and-safety team, the useful artifacts are the outcome taxonomy, the payment-handle test, and the recognition code. Use them to classify LLM-assisted fraud reports and to audit a model's own escalation behavior. Do not use refusal rate as the safety score — see @concepts/low-asr-is-not-refusal.md and @concepts/recognition-refusal-gap.md.

**Scope limits.** The study tested one scam type on one marketplace pattern. It did not test detection, platform defenses, or real victims. The cost figure is a token cost and excludes infrastructure and account acquisition. Treat the transfer to other fraud types as unproven [TENTATIVE].

## Snippets

> "Only one kind of buyer stopped the scam, and the sellers could fake their way past it." [Source: arxiv-2611.32957 p.2]

> "A seller that concedes half is still getting half, and half of a scam is a scam." [Source: arxiv-2611.32957 p.18]
