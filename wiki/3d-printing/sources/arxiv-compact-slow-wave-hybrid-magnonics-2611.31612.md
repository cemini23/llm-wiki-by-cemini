---
title: Compact Slow-Wave Hybrid Magnonics on Ultrahigh-Permittivity Substrates
type: source
related:
  - concepts/printed-photonics-background.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|---|---|
| Title | Compact Slow-Wave Hybrid Magnonics on Ultrahigh-Permittivity Substrates |
| Authors | Yu Jiang, Haiyang Yun, Zixin Yan, Amin Pishehvar, Benyamin Davaji, Xufeng Zhang |
| Affiliation | Northeastern University — Electrical and Computer Engineering; Physics |
| Type | arXiv preprint, physics.app-ph |
| arXiv | 2611.31612v1 (23 Nov 2026) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2611.31612-compact-slow-wave-hybrid-magnonics-on-ultrahigh.pdf` |
| Retrieved | 2026-11-25 |
| Pages | 7 |
| Read status | read |

## Narrative

The paper is a microwave magnonics device study. It wants small slow-wave hybrid magnonic circuits that couple magnons in a YIG film to spoof surface plasmon polaritons (SSPPs). The additive part is a means, not the subject.

The printing method is **additively manufactured electronics (AME)**, done with a drop-on-demand piezoelectric inkjet printer. The machine has two print heads: one for silver-nanoparticle conductive ink and one for polymer dielectric ink. Minimum trace width and edge-to-edge spacing are 100 µm.

The workflow is a fixture trick, and this is the one transferable idea:

1. Print two L-shaped dielectric corner frames on a Kapton sheet held by the vacuum stage. The frames take 20 layers at 10 µm each, so about 200 µm tall. Cure at 120 °C with UV cross-linking.
2. Pause the job and drop a 0.5 × 25 × 25 mm ceramic substrate into the pocket. The frames hold it laterally only.
3. Print the silver SSPP pattern straight onto the ceramic over 18 layers at 1 µm each, for an 18 µm conductor. Cure at 160 °C with infrared after each pass. Nozzle standoff goes to 800 µm to clear the raised surface.
4. Lift the ceramic out of the pocket to release the part.

A manufacturer-supplied control extension exposes the layer sequence and allows a programmed pause. That pause keeps the printer coordinate frame, so the printed pattern stays registered to the substrate loaded mid-job. This is the key limitation the authors work around: the printer is a closed system with no native mode for an external substrate.

Results: six devices with finger lengths from 600 to 3000 µm, cutoff 2 to 11 GHz. Measured cutoff scales linearly with inverse finger length, as theory predicts. The high-permittivity substrate (ε = 140) shrinks the finger length about four times against a standard Rogers TMM10i board (ε = 9.8). Magnon-photon coupling rises from 0.65 GHz to 1.1 GHz, or g/fp ≈ 22%. The authors call this ultrastrong coupling, with a YIG film of 23 µm thickness.

**Relevance to a desktop FDM print farm: effectively none.** The machine is an industrial inkjet AME platform with silver nanoparticle ink at 1 µm layers and 100 µm features. No FDM printer, slicer, filament, or heat-setting applies. The fixture idea — print a registration pocket, pause, insert a foreign part, print again — maps in principle to a consumer printer that can pause on demand. That is a design pattern, not a measured result. [TENTATIVE — no desktop test exists]

## Snippets

> "The ceramic is thick and brittle, and conventional thin-film processes cannot easily pattern thick, low-loss conductors on it. We overcome this challenge with additively manufactured electronics (AME)."
[Source: arxiv-2611.31612-compact-slow-wave-hybrid-magnonics-on-ultrahigh.pdf p.1]

> "During the pause the build volume becomes accessible, so the ceramic substrate can be loaded without aborting the job or losing the printer coordinate frame, thereby preserving registration of the pattern to the substrate across the interruption."
[Source: arxiv-2611.31612-compact-slow-wave-hybrid-magnonics-on-ultrahigh.pdf p.3]
