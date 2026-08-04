---
title: "arXiv 2608.02287 — SKT skill-use training via verified synthetic data"
type: source
tags: [arxiv, agents, skills, ccc, atto, k222]
keywords: [SKT, SkillEval, Agent Skills, Shanghai AI Lab, verified trajectories]
related:
  - sources/newsletter-rss-latent-space-2026-08-04-qwen-38.md
  - sources/arxiv-2608.02464-llm-agent-failure-detection-repair.md
  - concepts/llm-agent-failure-telemetry-monitors.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
read_status: deep-read
---

## Relations

- @sources/newsletter-rss-latent-space-2026-08-04-qwen-38.md

- @sources/arxiv-2608.02464-llm-agent-failure-detection-repair.md — complementary agent-runtime reliability
- @concepts/llm-agent-failure-telemetry-monitors.md
- @concepts/gpuology-genealogy-agent-kit.md — Atto skill packing awareness

## Raw Concept

| Field | Value |
|-------|--------|
| Title | SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation |
| Authors | Zelin Tan et al. (Shanghai AI Lab) |
| arXiv | 2608.02287 |
| Dataset | https://huggingface.co/datasets/Artemis0430/skilleval-v1 |
| sha256 | `9936944229d771cb8c327d13f3a83db320402116f03aeb2c45c2a91f79a031d7` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.02287-skt-skill-use-training-at-scale-via-verified-syn.pdf` |
| retrieved | 2026-08-04 |
| read_status | deep-read |

## Narrative

**SKT** builds skill-grounded tasks + executable trajectories from ~2,000 public Agent Skills; keeps only verified successes that use every required skill → 4,000 task packages / 27,164 trajectories + held-out **SkillEval**. SFT on SKT trajectories improves skill-use across harnesses; gains depend on verification quality and scale with skill coverage.

**Cemini:** CCC / Atto skill-harness patterns — **no Phase-0 code clone** (HF dataset only; do not download large SkillEval blobs into OSINT without size check). Steal: verified trajectory gate before treating a skill as “learned.”

## Snippets

> Together, these results establish verified data synthesis as an effective and scalable approach to skill-use training. [Source: arXiv 2608.02287]
