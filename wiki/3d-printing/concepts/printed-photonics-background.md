---
title: Printed Photonics and Metamaterials — Background
type: concept
tags: [photonics, SLA, 2PP, THz, background, stub-hub]
keywords: [dielectric design, scintillator, Smith-Purcell, technomolecular, OPA]
related:
  - concepts/fdm-printing.md
  - concepts/volumetric-additive-manufacturing.md
  - sources/2025-adams-fdm-thz-em-vortices.md
  - sources/2026-taleb-helical-waveguide-2pp.md
  - sources/2026-passia-locabinaconn-dielectric-sla.md
  - sources/2026-moore-plastic-scintillators-sla.md
  - sources/2026-hamoudi-technomolecular-nanosheets.md
  - sources/2026-yue-lithium-tantalate-opa.md
  - sources/arxiv-gradient-free-inverse-design-3d-nanophotonics-2611.15656.md
  - concepts/inverse-design-am-parts.md
  - sources/arxiv-compact-slow-wave-hybrid-magnonics-2611.31612.md
maturity: draft
created: 2026-06-01
updated: 2026-11-25
---

## Relations

@concepts/fdm-printing.md @concepts/volumetric-additive-manufacturing.md @sources/2025-adams-fdm-thz-em-vortices.md @sources/2026-taleb-helical-waveguide-2pp.md @sources/2026-passia-locabinaconn-dielectric-sla.md @sources/2026-moore-plastic-scintillators-sla.md @sources/2026-hamoudi-technomolecular-nanosheets.md @sources/2026-yue-lithium-tantalate-opa.md

## Raw Concept

Ingest pass 14 — photonics / metamaterials papers. Only @sources/2025-adams-fdm-thz-em-vortices.md uses **commodity FDM**; rest is SLA/2PP/specialty materials.

## Narrative

**Etsy/store-ops relevance:** essentially none. Indexed so inbox is empty and cross-wiki queries don't false-positive on FDM pages.

Exception: planar FDM prints as **THz optics** (@sources/2025-adams-fdm-thz-em-vortices.md) — curiosity only.

### Design side (2026-11-14)

@sources/arxiv-gradient-free-inverse-design-3d-nanophotonics-2611.15656.md is the first page here about how a 2PP device gets its shape. It uses gradient-free level-set optimization to design a micron-scale Y-splitter while holding a discrete rule: the material and the void must each be connected. The method is background; the constraint pattern is on @concepts/inverse-design-am-parts.md.

### Additively manufactured electronics on a foreign substrate (2026-11-25)

@sources/arxiv-compact-slow-wave-hybrid-magnonics-2611.31612.md is an inkjet AME paper: silver-nanoparticle and polymer dielectric inks, 100 µm minimum feature, 1 µm layers. It prints microwave waveguides directly onto a brittle ceramic that a thin-film process cannot coat.

The pattern worth keeping is the pause-and-insert fixture. Print a dielectric pocket first, pause the job, drop an external part into the pocket, then print on top of it. The printer keeps its coordinate frame across the pause, so the pattern stays registered. This needs a control extension that exposes the layer sequence. It is not a stock feature.

Still not an FDM result. No desktop printer, filament, or slicer is involved. The fixture trick is a design pattern with no desktop measurement behind it. [TENTATIVE]

## Snippets

(none — synthesis page)
