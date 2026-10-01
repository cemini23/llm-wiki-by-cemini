---
title: "DynaHarness: a dynamic physical harness for robot agents (2609.40306)"
type: source
tags: [source, k277, agents, harness, robotics]
keywords: [k277, dynaharness, execution-contract, regression-gate, no-clone]
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

| File | `arxiv-2609.40306-dynaharness-a-dynamic-physical-harness-for-self.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.40306-dynaharness-a-dynamic-physical-harness-for-self.pdf` |
| Archive | egress-fi 2026-10-01 |
| Retrieved | 2026-10-01 |
| Dual-ID | **OSINT K277** |
| sha256 | `e07c7fd79a2e6690f64cbc07f501894bc96d07c9bc091a735a7ef403572ddd1d` |
| arXiv | 2609.40306 |
| Authors | Haoyuan Deng, Jiebin Liu, Tengxiao Zhang, Langning Yan, Hongye Cao, Ziwei Wang (NTU; Nanjing University) |
| Project page | `https://denghaoyuan123.github.io/Dynaharness_page/` |

## Narrative

A robot harness, not a text harness. The design keeps a slow planner and a fast referee in the same loop.

A slow brain proposes capabilities and arguments. A fast brain runs at 2 Hz and can ground, monitor, refuse, or substitute a command. A separate controller runs at 20 Hz over a frozen vision-language-action policy. An execution contract bounds what a command may do and records the evidence.

The interesting part is the revision rule. Failures are attributed offline, and every candidate revision must pass a **paired regression check** before admission. That is the same seal order we filed in K276 and K277: freeze the candidate, then let evidence decide.

Results: on 800 newly sampled states the harness reached 75.2% success against 17.5% for the frozen policy. Removing seven contact skills dropped success from 74.0% to 16.6%. Simple one-step replanning scored 63.9% against 74.0%.

The authors admit the post-selection test covers only new initial states of the same cells, not new task families. Planners retain only summaries in earlier rounds.

This is a robotics result. The transferable piece is the paired regression gate on every self-revision. No GitHub code URL found. No clone. FILE only.
