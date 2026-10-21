---
title: "Jailbreak ASR depends on the judge, the budget, and the sample count"
type: source
related:
  - concepts/k293-cybersec-wave.md
  - concepts/low-asr-is-not-refusal.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: Concerns in Benchmarking Jailbreaks: An Empirical Study of Attack Success Rates
Authors: Leon Tu Nguyen, Rohan Menon, Rafael Tappe Maestro, Eric Aubinais, Chih-Hong Cheng (University of Oldenburg; Chalmers University of Technology)
Type: arXiv preprint (2610.26595)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.26595-concerns-in-benchmarking-jailbreaks-an-empirical.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

Eight jailbreak attacks, three open-weight models, three scoring procedures. The ranking is not a property of the attack alone.

Low-resource language attacks score a mean ASR of **96.0%** under keyword matching and **2.7%** under a Qwen3 evaluator that follows StrongREJECT instructions. Changing how many attempts are drawn, and in what order, **reverses the rank of DeepInception and rewriting**.

A separate test draws **100** responses to each unchanged request at Ollama's default temperature of **0.8**. Keyword matching scores **100%** ASR. The Qwen3 evaluator scores **50%**. Repeated sampling exposes unsafe text after an initial refusal. That is probabilistic suppression, not a hard exclusion.

The authors' reporting rule: state the success definition, match the response budget, use a validated evaluator, and report cumulative failure under repeated interaction. Do not publish a single-generation ASR. This page does not list the attacks. **No PoC.**

## Snippets

> "Low-resource language attacks achieve a mean ASR of 96.0% under keyword matching but 2.7% under a Qwen3 evaluator following StrongREJECT scoring instructions." [Source: arxiv-2610.26595 abstract]
