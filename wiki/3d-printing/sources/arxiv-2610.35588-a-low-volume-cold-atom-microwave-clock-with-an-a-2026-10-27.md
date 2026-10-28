---
title: "Additively manufactured microwave cavity in a compact cold-atom clock"
type: source
tags: [source, arxiv, additive-manufacturing, end-use-part]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A low-volume cold-atom microwave clock with an additively manufactured cavity |
| Authors | Samuel A. Smith, Sean Dyer, Peter Griffin et al., University of Strathclyde and University of Neuchâtel |
| arXiv | 2610.35588 |
| File | `arxiv-2610.35588-a-low-volume-cold-atom-microwave-clock-with-an-a.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.35588 |
| Read status | skimmed (abstract + intro) |

## Narrative

This paper matters to the additive-manufacturing domain for one reason: the microwave cavity is an **additively manufactured end-use part inside a working instrument**. It is not a bracket, a jig, or a prototype shell. The cavity is the component that interrogates the atoms, and the clock's measured performance depends on it.

The instrument is a compact microwave atomic clock built on laser-cooled rubidium-87. A micro-fabricated grating magneto-optical trap (gMOT) cools and traps the atoms. The additively manufactured cavity performs the microwave interrogation. The reported signal-to-noise ratio is **370 at 1 Hz bandwidth**, and the mid-term instability is **6.7 x 10^-14 at an averaging time of 3 x 10^4 s**.

One further detail is relevant to packaging. The authors added low-cost mu-metal foil to the vacuum chamber to reduce the quadratic Zeeman shift. That shift had been limiting stability beyond tau = 10 s. Magnetic shielding is a recurring print-farm and instrument-assembly problem, so the fix is worth recording.

The stated motivation is size, weight, and power (SWaP) reduction. Compact atomic clocks serve telecommunications, grid synchronisation, and navigation in GNSS-denied environments. Additive manufacturing enters as the route to a low-volume cavity that conventional machining makes expensive or slow.

Single source, abstract-level read. The material and the print process for the cavity are not recorded here; read the methods section before treating this as a process recommendation.

## Snippets

> "The clock utilizes a micro-fabricated grating magneto-optical trap (gMOT) to cool and trap atoms, and an additively manufactured microwave cavity for microwave interrogation." [Source: `arxiv-2610.35588-a-low-volume-cold-atom-microwave-clock-with-an-a.pdf` p.1 (arXiv 2610.35588), retrieved 2026-10-27]

> "We demonstrate a signal-to-noise ratio (SNR) of 370 at a 1 Hz bandwidth and mid-term instability of 6.7 x 10^-14 at an averaging time of tau = 3 x 10^4 s." [Source: `arxiv-2610.35588-a-low-volume-cold-atom-microwave-clock-with-an-a.pdf` p.1 (arXiv 2610.35588), retrieved 2026-10-27]
