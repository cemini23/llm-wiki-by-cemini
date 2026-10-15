---
title: "SP2EC — Adaptive Self-Speculative Decoding for Vision-Language Models"
type: source
tags: [arxiv, inference, efficiency, vlm]
keywords: [speculative decoding, self-speculative, bandit, wall-time regret, VLM inference]
related:
  - concepts/k291-cybersec-wave.md
maturity: draft
read_status: skimmed
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-cybersec-wave.md — K291 cybersecurity wave hub

## Raw Concept

Title: SP2EC — Adaptive Self-Speculative Decoding for Vision-Language Models
Authors: Yuqi Huang, Xingyao Li, Yunlong Hou, Fengzhuo Zhang, Jiachun Pan, Vincent Y. F. Tan (NUS, Yale)
Type: arXiv preprint (2610.18735)
Location: `research to be indexed/cybersec/arxiv-2610.18735-sp-2-ec-adaptive-self-speculative-decoding-for-v.pdf`
Retrieved: 2026-10-14
Read status: skimmed

## Narrative

**Filed for completeness; lowest relevance in the wave.** No security content.

**The problem:** self-speculative decoding reuses part of the target VLM as its own drafter, keeping multi-modal capability, but its efficiency depends on choosing a suitable **draft configuration per prompt**.

**The method:** **SP2EC**, a training-free **bandit algorithm** that adapts the draft configuration during generation, exploiting the **single-peak throughput pattern** observed across SWIFT, KnapSpec, SpecVLM, and the authors' CosineSim. It minimises a novel notion of **wall-time regret** per query, with theoretical guarantees that the optimal draft configuration is exploited at negligible exploration cost.

**The result:** consistent improvements of up to **11%** over prior self-speculative methods on Qwen2.5-VL-7B-Instruct and LLaVA-NeXT-Mistral-7B.

**Why it is filed here:** inference-cost work sits in this wiki's infrastructure lane. The **bandit-over-configurations** framing — adapt a runtime parameter online, with regret bounds — is the only transferable idea.

## Snippets

> "SP2EC, a training-free bandit algorithm that adapts the draft configuration during generation." [Source: arxiv-2610.18735 p.1]

> "consistent improvements of up to 11% over the original self-speculative methods." [Source: arxiv-2610.18735 p.1]

## Dead Ends

- Reading this as a security paper. It was filed in the cybersec inbox but carries no security finding.
