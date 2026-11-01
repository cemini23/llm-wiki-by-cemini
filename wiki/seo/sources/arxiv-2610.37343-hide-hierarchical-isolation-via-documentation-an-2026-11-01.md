---
title: "HIDE: hierarchical LLM isolation of rustc bug source files"
type: source
tags: [source, arxiv, rustc, bug-isolation, llm]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | HIDE: Hierarchical Isolation via Documentation and Evidence for Rustc Bugs |
| Authors | Tianrong Zhang et al., Peking University Shenzhen Graduate School |
| arXiv | 2610.37343 |
| File | `arxiv-2610.37343-hide-hierarchical-isolation-via-documentation-an.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.37343 |
| Read status | skimmed (abstract + intro) |

## Narrative

Rustc bugs can stop a valid program from compiling, or they can produce incorrect compilation results. Repair needs the source files that cause the bug. The authors call this task compiler bug isolation.

The authors name three problems for a large language model on this task. Compiler work is spread across files, so the model must know what each file does and how files work together. The source tree is large, so a full pass over every file is costly. A prompt that holds documentation and source code for many files creates context overload, and the authors say this can reduce isolation accuracy.

HIDE is their hierarchical method. It takes a rustc revision and a bug context, then runs two stages. Layered Documentation Aggregation summarizes what each file does and how files with similar functions work together. Hierarchical Bug Isolation narrows the search. Hierarchical candidate selection cuts the number of files that need detailed analysis. Scoped Candidate Competition limits how many candidates enter each prompt. Evidence-Guided Code Slicing limits how much source code enters each prompt.

The authors evaluate HIDE on 160 reproducible rustc bugs. They compare it with Agentless, SoapFL, and GraphLocator. With GPT-5.4, they report 42.08% Accuracy@1 and 80.42% Accuracy@10. They report that these scores exceed the strongest baseline results by 5.83% and 6.04%, respectively. Those four numbers are single-source claims from this paper.

The subject is the Rust compiler, rustc. A local-SEO reader can take one method claim from the abstract. The authors report that too much documentation and source code in one prompt can reduce accuracy, and that HIDE limits both the candidate count and the code in each prompt. The paper reports that this limit, plus generated compiler documentation and hierarchical narrowing, supports rustc bug isolation on their test set.

## Snippets

> "With GPT-5.4, HIDE achieves 42.08% Accuracy@1 and 80.42% Accuracy@10, exceeding the strongest baseline results by 5.83% and 6.04%, respectively. These results demonstrate that generating compiler documentation, narrowing candidates hierarchically, and limiting analysis context enable effective rustc bug isolation." [Source: `arxiv-2610.37343-hide-hierarchical-isolation-via-documentation-an.pdf` p.1 (arXiv 2610.37343), retrieved 2026-11-01]
