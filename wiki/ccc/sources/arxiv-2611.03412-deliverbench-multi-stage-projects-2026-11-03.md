---
title: "DeliverBench — agents deliver projects, not tasks, and the difference breaks them"
type: source
tags: [source, arxiv, benchmark, agents, traceability, professional-work]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | DeliverBench: Benchmarking AI Agents on Delivering Realistic Multi-Stage Professional Projects |
| Authors | Yumou Liu, Mingju Chen, Zhoufutu Wen, Qianyu Yang, Zijie Wang, Yeqian Liu, Chenghao Yang, Tiliang Duan, Qiyu Cai, Yanglihong Xiao, Jiayun Dong, and others |
| arXiv | 2611.03412 |
| Pages | 23 |
| Read status | skimmed (abstract) |

## Narrative

Existing agent benchmarks test **one task at a time**. Professional work delivers **a project**: a package where one weak part limits the value of the rest.

DeliverBench closes that gap. **11 projects** across financial due diligence, legal contract drafting, and drug safety reporting, reconstructed with **13 domain experts** from real materials. Each chains **150 subtasks through 2–15 rounds** of new materials and client feedback.

The design choice that makes it hard: **no reference outputs are injected**, so agents inherit their own errors from one stage to the next.

### The results

| Measure | Best of seven model–harness systems |
|---------|-------------------------------------|
| Final delivery score | **65.0 / 100** |
| Subtasks passing at a 90-point threshold | **50.0%** |

And the failure pattern the authors name: **failures of carrying work forward**. In one audit project, all seven systems addressed the review findings, but **only one preserved traceability**.

### Why traceability is the finding

Every system could do the work. Almost none could show how the work connected across rounds. That is the compound failure: a project is not a set of deliverables, it is a chain of decisions where each stage must be able to justify itself against the previous one.

For this workspace that maps onto something already true — the wiki's citation and provenance discipline exists because a claim without its source is not reusable. DeliverBench measures the same property in agents and finds it largely absent.

### Caveat

Abstract only. Rubrics are expert-built; the 65.0 is not comparable to any other benchmark.

## Snippets

> "In one audit project, all seven systems addressed the review findings, but only one preserved traceability." [Source: arxiv-2611.03412 p.1]

> "Because no reference outputs are injected, agents inherit their own errors from one task to the next." [Source: arxiv-2611.03412 p.1]

## Dead Ends

- **Comparing 65.0 to another benchmark's score.** Different rubrics entirely.
