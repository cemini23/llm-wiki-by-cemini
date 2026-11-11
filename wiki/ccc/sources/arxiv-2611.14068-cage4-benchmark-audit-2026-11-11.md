---
title: "CAGE 4 scores measure less than they are taken to measure"
type: source
tags: [source, arxiv, benchmark-audit, cyber-defense, evaluation-validity]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them |
| Authors | James Rice, Ji Hwan Park, Andres Kwasinski |
| arXiv | 2611.14068 |
| Pages | 47 |
| Read status | skimmed (abstract) |

## Narrative

CAGE Challenge 4 is the benchmark learned multi-agent cyber defenders are compared on. Its **scores and the counts reported beside them are read as measures of what a defender does.**

The authors reproduce both reference defenders in a pinned container — **KEEP at −191.34 against a published −193.68; H-MARL Expert at −131.34 against −129.53** — and then show that **three things read from this benchmark measure less than they are taken to measure.**

The first is specific and damning: the simulator **silently discards any action asserted for an agent while its previous action is still running** — no error — **charges the team one point for a discarded Restore as for one that ran**, and leaves the reported counts inflated accordingly.

### Why a reproduction paper is worth a page

The numbers reproduce. That is what makes the audit credible: the authors are not disputing the scores, they are showing what the scores are attached to.

A benchmark that **charges for actions it did not perform** produces a ranking that partly reflects how often an agent's actions collided, not how good the defence was. Any paper comparing defenders on this benchmark inherits that.

### The general lesson

**A benchmark's reported counts are a model of what happened, and the model can be wrong while the interface looks clean.** Here the failure mode is a silent discard with no error — the worst kind, because nothing in the output signals it.

This workspace has its own version of the problem: re-delivered papers counted as new arrivals, the same feed in two archive paths, duplicate `[CONFIRMED]` claims. All of them are counts that overstate.

**Caveat.** Abstract only; two of the three findings are not in the extracted text.

## Snippets

> "The simulator discards, by design and without an error, any action asserted for an agent while its previous action is still running, charges the team one point for a discarded Restore as for one that runs…" [Source: arxiv-2611.14068 p.1]

## Dead Ends

- **Reading this as a claim the scores are wrong.** The reference defenders reproduce; the argument is about what the scores mean.
