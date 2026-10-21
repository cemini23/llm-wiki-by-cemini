---
title: "SLIP — language effects on tool admission and post-retrieval safety"
type: source
related:
  - concepts/k293-cybersec-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: Disentangling Language Effects on Tool Admission and Post-Retrieval Safety
Authors: Aditya Nawal, Manit Baser, Mohan Gurusamy (National University of Singapore)
Type: arXiv preprint (2610.23093)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.23093-disentangling-language-effects-on-tool-admission.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

Same group as @sources/arxiv-2610-23071-tool-admission-before-retrieval.md. Here the language of the request, the retrieved page, and the required answer vary independently, in a URL-retrieval setting, across ten models and seven languages.

They name the gap Safety Loss through Interlingual Processing (SLIP). Non-English harmful requests raise mean tool admission from **46.9% to 67.4%**, with a positive change in every model. The pattern holds in an autonomous retrieval setup on all four models tested that way.

Requiring the answer in the page language raises pooled harmfulness on matched tool calls from **50.3% to 57.4%** across four closed-weight models, mainly in Chinese and Hindi. Translating the pages alone does not produce a consistent harm increase in eight models with comparable settings.

A non-harmful label can be a real refusal, a deflection that cites language trouble, or an unusable answer. Harmfulness alone cannot tell those apart. Measure admission and answer harm separately, and separate refusal from capability failure. **No PoC.**

## Snippets

> "Non-English harmful requests increase mean tool admission from 46.9% to 67.4%, with a positive mean change in every model." [Source: arxiv-2610.23093 abstract]
