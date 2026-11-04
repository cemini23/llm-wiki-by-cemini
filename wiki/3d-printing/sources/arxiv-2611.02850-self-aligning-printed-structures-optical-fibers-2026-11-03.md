---
title: "Self-aligning 3D-printed structures on optical fibers — planar batch fabrication"
type: source
tags: [source, arxiv, two-photon, microfabrication, lab-on-fiber]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A plug-and-play platform for self-aligning 3D-printed structures on optical fibers |
| Authors | Lukáš Zezulka, Zdeněk Nováček, Martin Konečný, Milan Matějka, Štěpán Černý, Katarína Rovenská, Jiří Spousta, Tomáš Šikola |
| Affiliation | Brno University of Technology |
| arXiv | 2611.02850 |
| Pages | 26 |
| Read status | skimmed (abstract) |

## Narrative

Two-photon polymerization can print complex structures directly onto optical fibers, turning them into lab-on-fiber devices. Adoption is limited by **sequential, direct-on-fiber printing** — one device at a time, on a fiber, which is slow and awkward.

The paper's move is to **print on a planar substrate instead**, and put the alignment problem in the mechanical design rather than in the printer.

The mechanism: a compliant, spring-like socket that gives **passive self-alignment** and reversible fiber insertion. Device structures are printed flat, in parallel batches, on a substrate that then acts as a magazine. The fiber is pushed in and the socket centres it.

Post-processing happens while the devices are still on the substrate: plasma etching to sharpen tips, metallisation, and focused-ion-beam milling of an optical aperture.

Demonstration: exchangeable scanning probe microscopy tips used in situ inside a scanning electron microscope, validated by three-channel correlative imaging — AFM topography, secondary electron, and cathodoluminescence.

**Why the idea transfers beyond photonics.** Decoupling a part from the expensive substrate by moving alignment into a passive compliant feature is a general manufacturing pattern. The same reasoning applies wherever a small part must interface precisely with a much larger, awkwardly shaped body.

**Caveat.** This is two-photon polymerization at the micron scale, not FDM. Nothing here is a recipe for a desktop printer.

## Snippets

> "This platform features a compliant, spring-like socket that enables passive self-alignment and reversible fiber insertion, paired with a customizable frontal device. The shift to fabrication on planar substrates enables parallel batch processing and allows the substrate to serve as a functional magazine for device mounting." [Source: arxiv-2611.02850 p.1]

## Dead Ends

- **Reading this as an FDM technique.** Two-photon polymerization, micron scale.
