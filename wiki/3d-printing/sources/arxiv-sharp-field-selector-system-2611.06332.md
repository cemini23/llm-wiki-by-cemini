---
title: "Developing the Field Selector System for the SHARP Multi-IFU — Optomechanical Design and First Prototype Validation (arXiv:2611.06332)"
type: source
related:
  - concepts/precision-optomechanics-am.md
maturity: draft
read_status: read
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Developing the Field Selector System for the SHARP Multi-IFU: Optomechanical Design and First Prototype Validation |
| Author | H. Mahmoodzadeh, P. Saracco, I. Di Antonio, P. Conconi, D. Scaccabarozzi, B. Saggin, E. Molinari, and others (INAF, Politecnico di Milano, Universita di Padova) |
| Type | arXiv preprint (astronomical instrumentation) |
| Location | `research to be indexed/3d-printing/arxiv-2611.06332-developing-the-field-selector-system-for-the-sha.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.06332-developing-the-field-selector-system-for-the-sha.pdf` |
| Read status | read |

## Narrative

This paper describes a **Field Selector System** for VESPER, the multi-Integral Field Unit of the SHARP near-infrared spectrograph. SHARP is designed for the European Southern Observatory Extremely Large Telescope.

The system uses an array of movable light-collection probes. Twelve probes sit in two modules of six. Each probe is a prism with a powered entrance surface plus a collimator. Two 45-degree folding mirrors move by half the probe displacement. That ratio keeps the optical path constant, so several moving probes share one focal plane and form one contiguous strip for the image slicer.

### Important limit for this wiki

**No additive manufacturing is used.** The main structural box is a monolithic block machined from 6xxx or 7xxx aluminium plates. The paper cites strength per weight, machinability, and cryogenic thermal performance as the reasons. Parts join with precision alignment pins and bolted connections. The paper is filed here because it states the mechanical-tolerance budget that printed optomechanics must also meet.

### Measured prototype errors

A quarter-scale prototype was built from commercial off-the-shelf (COTS) bearings, guides, and lead screw. Tests ran at ambient temperature; cryogenic testing was deferred. The mechanism was driven by hand at 2 mm per handle turn, and the scan repeated five times in each direction.

| Error source | Forward | Backward |
|---|---|---|
| Local lateral shift dx | ±0.16 mm | ±0.10 mm |
| Local lateral tilt beta | ±0.061° | ±0.038° |
| Positioning shift dx (rail straightness) | ±0.23 mm | ±0.17 mm |
| Positioning tilt beta | ±0.088° | ±0.065° |
| Combined total beta | ±0.115° | — |
| Combined total theta | ±0.169° | — |

Two dominant causes were identified. First, mechanical clearance in the movable mount and rail causes a local tilt. Second, rail straightness error causes a position-dependent tilt. Vertical tilt stays below ±0.01 mm over most of the scan. It rises to ±0.22 mm only at the reversal point.

The authors convert each measured mechanical error into an equivalent optical tilt with a Zemax model, then propagate it into the VESPER optical model. The effect is small: the spot radius grows by about 0.2 µm for 0.05 degrees of output tilt. The authors conclude the concept is viable but needs improvement. They note the prototype is roughly three times faster than the real system, so the real angular deviations should be smaller.

## Snippets

> "The first one is a local tilt of the probe and folding mirrors assembly caused by the mechanical clearance present in the moveable mount and rail system. The second one is a position-dependent tilt resulting from imperfections in the straightness of the rail system" [Source: arxiv-2611.06332-developing-the-field-selector-system-for-the-sha.pdf p.7]

> "It is designed as a monolithic structure manufactured from aluminum alloy (series 6 or 7) plates, selected for their favorable strength per weight ratio, machinability, and thermal performance at cryogenic temperatures." [Source: arxiv-2611.06332-developing-the-field-selector-system-for-the-sha.pdf p.5]
