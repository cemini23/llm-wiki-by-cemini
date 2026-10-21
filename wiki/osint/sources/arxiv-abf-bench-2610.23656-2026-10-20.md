---
title: "ABF-Bench — verifiable agentic blockchain forensics"
type: source
related:
  - concepts/k293-osint-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics
Authors: Xiaohang Yu, Hejia Geng, William Knottenbelt (Imperial College London; University of Oxford)
Type: arXiv preprint (2610.23656)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.23656-abf-bench-a-verifiable-benchmark-for-agentic-blo.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

Fund tracing on public ledgers is open-ended, but every recorded movement stays public. ABF-Bench turns that into a checkable agent task: every claimed movement must cite a ledger record the agent retrieved. Tasks stop where the records do not determine the next hop. The set includes multi-hop transfers, DeFi exchanges, cross-chain round trips, custodial and mixer deposits, and address poisoning.

The authors' harness, built around a working memory, reaches **75% edge recall**. Codex with the same model reaches **47%**. Claude Code reaches **10%**, and the paper's read is overconfidence: it cites records it left unretrieved. Against fixed-order tracers, the harness finds undisclosed custodial services that the tracers walk past (**89% versus 0%**) at **98% fidelity**. Agents still stop early on larger tasks, so final recall stays below the best tracer.

The lesson for this workspace is the citation rule, not a tracing product. A claim about a retrieved artifact must name the record that was actually read. **No install. No scrape.**

## Snippets

> "The harness reaches 75% edge recall, against 47% for Codex with the same model and 10% for Claude Code, which loses recall to overconfidence: it cites records it left unretrieved." [Source: arxiv-2610.23656 abstract]
