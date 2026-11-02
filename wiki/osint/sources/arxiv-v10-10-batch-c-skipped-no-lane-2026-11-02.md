---
title: "v10.10 batch C skipped — no lane for this inbox PDF"
type: source
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md
maturity: draft
read_status: skimmed
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Type: reject record for an inbox PDF with no Cemini lane.

| Field | Value |
|-------|-------|
| arXiv | 2610.40772v1 [hep-th], 29 Oct 2026 |
| Title | Efficient Genealogical Constraints from Sector-By-Sector Critical Point Counting |
| Authors | Giulio Crisanti, Luke Lippstreu, Andrew J. McLeod, Maria Polackova (Higgs Centre, University of Edinburgh) |
| Inbox basename | `arxiv-2610.40772-disckosky-efficient-genealogical-constraints-fro.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |
| Retrieved | 2026-11-02 |
| Read status | skimmed (title and abstract only) |

## Narrative

**The filename is a false lead.** "Genealogical constraints" here is a term in high-energy physics, not human genealogy. A title scan would route this to Atto. It has nothing to do with it.

DiscKosky is a **Mathematica package** for generating genealogical constraints on the sequential discontinuities of **Feynman integrals**. It tracks solutions to the critical-point equations of an integral, finds which critical points vanish in a given kinematic limit, associates each Landau singularity with a set of on-shell sectors, and applies the hierarchical principle to forbid sequential discontinuities across incompatible propagator sets.

Applications: two-loop five-point integrals with one and two massive legs, three-loop examples beyond the current computational frontier, and Euler integrals from cosmological correlators.

| arXiv | Why it is skipped |
|---|---|
| 2610.40772 | hep-th. Symbolic computation over Feynman integrals. No market, harness, safety, or product method. Overlap with this workspace is the word "genealogical" and nothing else. |

Filing the id here makes the next `preingest_check.py` call it a duplicate. **No install. No clone.**

## Snippets

> "We present DiscKosky, a new Mathematica package for efficiently generating genealogical constraints on the sequential discontinuities of Feynman integrals." [Source: arxiv-2610.40772 p.1]

## Dead Ends

- **Routing on the word "genealogical".** It is a physics term of art. The paper is about Feynman integrals.
