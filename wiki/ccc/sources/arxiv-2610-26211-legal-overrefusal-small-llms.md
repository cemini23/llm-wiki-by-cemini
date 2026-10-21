---
title: "Legal-role prefixes raise refusal on small on-prem models"
type: source
related:
  - concepts/k293-ccc-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: LLMs Prompted for Legal Context Refuse More: Overrefusal from Small On-Premises LLMs in Criminal Legal Context
Authors: Anastasiia Kucherenko, François Brouchoud, Dimitri Percia David, Andrei Kucharavy (HES-SO Valais-Wallis)
Type: arXiv preprint (2610.26211)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.26211-llms-prompted-for-legal-context-refuse-more-over.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

Small on-device models are used for summary, translation, and rewrite when the text cannot leave the machine. Users state a role, as ordinary prompting advice says to do. On four small open-weight models, and on benign legal prompts, authority prefixes such as "I am legal counsel" or "I'm a defense lawyer" raise refusal by **2–20×** versus no prefix. A known role-play jailbreak prefix is mixed: it raises refusal sharply in some models and barely moves others.

The operational reading: a role line in a system prompt is not free. On a small local model it can block ordinary work. Test the prefix on benign tasks before you ship it. **No install.**

## Snippets

> "Authority-style prefixes systematically increase refusal rates by 2–20x over the no-prefix baseline." [Source: arxiv-2610.26211 abstract]
