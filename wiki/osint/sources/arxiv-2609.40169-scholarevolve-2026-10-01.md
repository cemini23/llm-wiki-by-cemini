---
title: "Learning from research: lifelong agent harness evolution (2609.40169)"
type: source
tags: [source, k277, agents, harness, self-evolution]
keywords: [k277, scholarevolve, literature, lifelong, no-clone]
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

| File | `arxiv-2609.40169-learning-from-research-toward-lifelong-agent-har.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.40169-learning-from-research-toward-lifelong-agent-har.pdf` |
| Archive | egress-fi 2026-10-01 |
| Retrieved | 2026-10-01 |
| Dual-ID | **OSINT K277** |
| sha256 | `c7481bd20b5713831796b5282a8c8ecfb2dc0adbcaa66d42d825faa9b941184f` |
| arXiv | 2609.40169 |
| Authors | Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang, Yaar Harari, Evgeniy Gabrilovich, Shiyu Chang (UCSB; Microsoft) |
| Repo | `https://github.com/UCSB-NLP-Chang/ScholarEvolve` |

## Narrative

The method, ScholarEvolve, evolves a harness by reading research papers instead of only learning from run feedback.

It splits the harness into five modules: tool, context, skills, memory, and workflow. It audits failures, turns each gap into a research query, retrieves papers, and uses topic modelling to group mechanisms into families. A coding agent then writes a paper-grounded mutation. Candidates are evaluated and recombined, with a validation gate on admission.

Results: on AppWorld Challenge, goal completion rose from 49.6% to 63.6%, and on Normal from 69.0% to 81.4%. On a telecom benchmark, pass at one rose from 72.7% to 81.9%. Module combinations beat the strongest single module. One model improved on 221 of 585 tasks against 57 regressions.

The authors admit residual failures in requirement tracking and evidence coverage. They warn that evolution gains can overfit when search tasks are reused, and they stress disjoint development, validation, and test splits.

This is a literature-grounded self-modification loop. It is the closest design to what a wiki ingest already does by hand. **Never auto-evolve our skills or rules from this paper.** The useful lesson is the gate, not the loop: mutations are admitted only after a validation check on a held-out split.

Repo SPDX is **null**, 0 KB, 0 stars (gh api 2026-10-01). A null SPDX records the pattern only. No clone. FILE only.
