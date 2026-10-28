---
title: "StateMirror: Pre-Execution Detection of Hallucinated Tool Calls"
type: source
tags: [source, arxiv, coding-agents, tool-hallucination]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | StateMirror: Pre-Execution Detection of Hallucinated Tool Calls in Coding Agents |
| Authors | Shiwen Shan, Yintong Huo, Zhiying Wu, Yuxin Su (Sun Yat-sen University; Singapore Management University) |
| arXiv | 2610.32648 |
| File | `arxiv-2610.32648-statemirror-pre-execution-detection-of-hallucina.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32648 |
| Read status | skimmed (abstract + intro) |

## Narrative

Coding agents propose actions that cannot run in the current environment. They open non-existent paths or import missing packages. The paper names this **hallucinated tool use**.

A study of 4,398 agent trajectories found the problem is pervasive and costly. Recovery takes a median of 3 extra interaction steps and 22.4K tokens.

Existing frameworks react after execution fails. **StateMirror** instead intercepts actions at the harness boundary before execution. It extracts state predicates with AST and command analysis, then validates them deterministically against the live repository.

Measured on 2,508 actions:

- Precision 0.940, F1 0.817.
- F1 is 35.3% above the strongest LLM judge.
- Median detection latency falls from 17.73 s to 1.50 ms.
- Detection uses zero tokens.

The pre-execution feedback also lets agents fix more than 95% of flagged actions before they run.

**Why it matters.** This is the cheapest known defence against a common, expensive failure mode. It costs no model tokens because it is a plain check against the filesystem. A harness that validates prerequisites before execution removes most of the recovery loop.

## Snippets

> "StateMirror intercepts actions at the harness boundary, extracts state predicates via AST and command analysis, and deterministically validates them against the live repository." [Source: `arxiv-2610.32648-statemirror-pre-execution-detection-of-hallucina.pdf` p.1 (arXiv 2610.32648), retrieved 2026-10-27]
