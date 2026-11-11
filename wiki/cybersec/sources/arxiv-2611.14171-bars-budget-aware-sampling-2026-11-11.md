---
title: "BARS — budget-aware sequential sampling with a refusal option"
type: source
tags: [source, arxiv, sampling, self-consistency, confidence, selective-prediction]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BARS: Budget-Aware Sequential Sampling with Refusal for Majority Identification under Unknown Distributions |
| Authors | Shenxi Liu, Yiwei Li, Mingyang Zhao, Yuzhang Tian, Kan Li (Beijing Institute of Technology; HK PolyU) |
| arXiv | 2611.14171 |
| Pages | 23 |
| Read status | skimmed (abstract) |

## Narrative

**Repeated sampling with majority vote** enforces self-consistency in LLMs. A recent variant stops early to save cost when the distribution is favourable.

The gap BARS names: **neither can produce a correct confidence estimate from the answer distribution.** Early stopping that saves cost without giving you a calibrated confidence is saving the wrong thing — you spend fewer samples and get a number you cannot act on.

BARS adds two things:

- **Budget awareness** — sampling decides how many draws it can afford.
- **Refusal** — the procedure can decline to identify a majority, rather than forcing one.

Under **unknown distributions**, with **anytime-valid confidence sequences** rather than a fixed-sample bound.

### Why refusal is the important addition

Majority vote always produces a majority. When the distribution is nearly flat, that majority is noise, and reporting it as an answer is the failure mode.

A method that can say **"this distribution has no clear majority"** is strictly more useful than one that must pick.

That is the same three-way structure as `jevals`' allow / block / **escalate** and the `ontographia` validate-or-error contract: the ability to abstain is what makes a confident answer meaningful.

**Caveat.** Abstract only. No budget, accuracy, or coverage figures reproduced.

## Snippets

> "Repeated sampling with majority selection is an effective means of enforcing self-consistency in large language models… But it still cannot yield a correct confidence estimate from the answer distribution." [Source: arxiv-2611.14171 p.1]

## Dead Ends

- **Citing a coverage number.** Abstract only.
