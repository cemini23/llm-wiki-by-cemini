---
title: "Transient supercriticality in Hawkes processes (Sornette) — detecting n > 1 episodes"
type: source
tags: [source, arxiv, hawkes, criticality, risk]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Transient Supercriticality in Hawkes Processes: Detection, Identifiability, and Apparent Criticality |
| Authors | Didier Sornette — Institute of Risk Analysis, Prediction and Management, Southern University of Science and Technology (SUSTech), Shenzhen |
| arXiv | 2610.35159 |
| File | `arxiv-2610.35159-transient-supercriticality-in-hawkes-processes-d.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.35159 |
| Read status | skimmed (abstract + intro) |

## Narrative

The paper attacks a standing convention in Hawkes calibration. Self-exciting models are usually fitted with a branching ratio below one. The author states that this is a condition for stationarity, not for existence. A process with branching ratio above one grows exponentially but stays finite on any finite horizon.

The consequence is a measurement error with a name. When stationarity is imposed, brief episodes of supercritical growth appear as near-critical behaviour. The model reports "almost critical" when the record actually contains a transient excursion above the threshold.

The author reconstructs the latent genealogy of events. A single finite record can then show an excursion into a branching ratio above one and back out again. It can also date the onset and the end of that excursion.

Three identifiability results are given. Detectability depends on the excess over one, multiplied by the square root of the number of exposed parents. When the memory time of the triggering is unknown, the data still fix the growth rate during the episode almost as precisely as when memory is known. The same data reveal whether the ratio crossed one. The value of the ratio itself does need independent knowledge of the memory time. Letting the data choose between endogenous amplification and external forcing stops the two from being confused.

The worked example is the 2015 Korean MERS outbreak. The reconstruction shows that transmission through hospital cohorts had collapsed by 28 May. That is before the incidence peak, and two weeks before the instantaneous reproduction number fell below one. In real time the method establishes the collapse a few days earlier than the standard indicator.

The market reading is direct. Crisis episodes are short bursts of endogeneity inside a longer record. Fitting the whole record with a subcritical prior smooths the burst away. The paper supplies a way to see the burst and to date it.

All findings are single-source and are not independently verified here.

## Snippets

> "a process with n > 1 grows exponentially but remains finite on any finite horizon. Imposing stationarity is also misleading, because transient supercritical episodes then masquerade as near-criticality." [Source: `arxiv-2610.35159-transient-supercriticality-in-hawkes-processes-d.pdf` p.1 (arXiv 2610.35159), retrieved 2026-10-27]

> "Detectability is governed by the excess n − 1 times the square root of the number of exposed parents." [Source: `arxiv-2610.35159-transient-supercriticality-in-hawkes-processes-d.pdf` p.1 (arXiv 2610.35159), retrieved 2026-10-27]
