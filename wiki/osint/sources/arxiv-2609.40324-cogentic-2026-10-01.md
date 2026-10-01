---
title: "Cogentic: multi-agent orchestration for proof discovery (2609.40324)"
type: source
tags: [source, k277, agents, orchestration, verification]
keywords: [k277, cogentic, adversarial-verifier, verified-ledger, no-clone]
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

| File | `arxiv-2609.40324-cogentic-multi-agent-orchestration-for-automated.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.40324-cogentic-multi-agent-orchestration-for-automated.pdf` |
| Archive | egress-fi 2026-10-01 |
| Retrieved | 2026-10-01 |
| Dual-ID | **OSINT K277** |
| sha256 | `f19883ba88420612484e91caf49c8cf23f0c8a820024caca34937f9441a3d983` |
| arXiv | 2609.40324 |
| Authors | Yang Cai, Vineet Gupta, Yanchen Jiang, Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Di Wang (Google Research; Yale; DeepMind) |
| Project page | `https://sites.google.com/view/cogentic` |

## Narrative

A multi-agent harness that attacks open research problems in mathematics and theoretical computer science, from the problem statement alone.

The loop has four parts. An orchestrator assigns a population of independent provers to distinct directions. Each draft is read by **adversarial verifiers**, first individually and then side by side. Confirmed fragments move into a persistent **verified ledger**. A process advisor tunes the standing instructions across rounds. A final stage consolidates and audits one manuscript.

Provers see selective briefings written by a summarizer, not the full run history. That is the bounded-context idea from K276's meta-reasoning paper.

Results: five open problems resolved or improved, each verified by domain experts and written up separately. Examples include a first efficient and first proper O(d) regret bound for online inverse linear optimization, and an optimal 1.5 price of anarchy for a two-bidder autobidding auction. Cost was on the order of 100 model calls for most problems and 1,000 for the hardest.

The authors admit the problems sit in their own areas of expertise, that prose was verified by experts, and that results may outpace human reading. They suggest formalisation in a proof assistant may be needed to settle correctness mechanically.

The design lesson is the split: adversarial verification plus a persistent ledger of only-confirmed work. No GitHub URL found. No clone. FILE only.
