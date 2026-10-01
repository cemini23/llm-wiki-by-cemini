---
title: "Turbo Harness: instance-adaptive harness optimization (2609.40330)"
type: source
tags: [source, k277, agents, harness, self-evolution]
keywords: [k277, turbo-harness, grpo, playbook, no-clone]
related:
  - concepts/k277-harness-evolution-wave.md
maturity: draft
created: 2026-10-01
updated: 2026-10-01
read_status: skimmed
---

## Relations

- @concepts/k277-harness-evolution-wave.md

## Raw Concept

| File | `arxiv-2609.40330-turbo-harness-instance-adaptive-harness-optimiza.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.40330-turbo-harness-instance-adaptive-harness-optimiza.pdf` |
| Archive | egress-fi 2026-10-01 |
| Retrieved | 2026-10-01 |
| Dual-ID | **OSINT K277** |
| sha256 | `992a40b21bfde0452cac82ff7b9d8ab52c3e6bc1a8be62c3e386018ec6a5715e` |
| arXiv | 2609.40330 |
| Authors | Tunyu Zhang, Hao Wang, Kai Xu, Dimitris N. Metaxas (Rutgers; Red Hat AI Innovation; MIT-IBM Watson AI Lab) |
| Repo | `https://github.com/Tyrion58/turbo-harness` |

## Narrative

The claim is that one globally optimized harness is the wrong target. Different tasks want different scaffolding.

The method has two parts. First, summarize a completed global harness search into a structured playbook. Second, train a small reinforcement-learning editor to patch the global harness per instance. The editor runs once per instance.

Results across seven benchmarks. On SWE-smith-MR the pass rate rose from 50.7% to 64.0% on one backbone and from 70.7% to 88.0% on another. On SWE-bench Verified, 38.4% to 54.4% and 56.7% to 59.3%. On one setting the run was 6.7 times cheaper: 8.7 steps against 23.1, and $0.046 against $0.310.

An ablation is worth noting: the reinforcement learning and the playbook are complementary. Neither alone beats the previous global method.

The authors admit the method depends on the quality of the completed global search, and that training the editor needs extra environment rollouts, which can be costly.

Repo SPDX is MIT, 7,783 KB, 3 stars (gh api 2026-10-01). This is a self-modifying harness. **Never auto-evolve our skills or rules from it.** No clone. FILE only.
