---
title: "TuneBench — agent benchmark for power-system model calibration"
type: source
tags: [source, arxiv, benchmark, agents, engineering, calibration]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | TuneBench: Benchmarking AI Agents for Power System Dynamic Model Calibration |
| Authors | Andrea Pomarico, Salvatore Tessitore, Giorgio Giannuzzi, Alberto Berizzi (Politecnico di Milano, Terna Rete Italia) |
| arXiv | 2611.04640 |
| Pages | 5 |
| Read status | skimmed (abstract) |

## Narrative

A **five-page benchmark** from a transmission-system operator and a university, evaluating agents on a real engineering workflow: **calibrating controller parameters so a model reproduces a target dynamic response**.

It reflects standard TSO practice — equivalent models used for Dynamic Security Assessment are calibrated against measurements from grid-code compliance tests, when proprietary models are unavailable. Two cases of increasing complexity: governor and (presumably) a second controller.

### Why it is worth a page despite the weak domain fit

This workspace does not do power systems. The value is **the shape of the task**:

- A **known ground truth** (the target response).
- A **continuous parameter search** with feedback.
- **Tool interaction and interpretation of results** in a loop.
- A **domain where wrong answers are expensive**, so the benchmark reflects a real workflow rather than a synthetic puzzle.

That is a much better template for evaluating a tuning agent than a multiple-choice set. It is the same structure as the DFS tuning loop this workspace has been designing: adjust parameters, run an evaluation, read the result, adjust again.

**A benchmark built from an actual operator's calibration procedure** is also a reminder that the strongest benchmarks come from work somebody already had to do.

**Caveat.** Abstract only, five pages. No results reproduced.

## Snippets

> "Controller parameters are adjusted to reproduce target dynamic responses… equivalent models used for Dynamic Security Assessment are calibrated against measurements from grid-code compliance tests when proprietary models are unavailable." [Source: arxiv-2611.04640 p.1]

## Dead Ends

- **Reading this as a power-systems source.** It is a benchmark-shape reference.
