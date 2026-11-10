---
title: Precision Optomechanics — Additive Manufacturing and the Tolerance Budget
type: concept
related:
  - sources/arxiv-sharp-field-selector-system-2611.06332.md
  - sources/arxiv-monolithic-optomechanical-chassis-2611.06898.md
  - concepts/industrial-am-monitoring.md
  - concepts/fdm-printing.md
maturity: draft
updated: 2026-11-10
---

## Raw Concept

Opened on the 2026-11-10 ingest, from two papers that both build optical instrument hardware. One machines aluminium; one prints Invar36 by L-PBF. Together they define the tolerance and stability question that any printed optical mount must answer.

## Narrative

An optical instrument needs a mount that holds a lens or mirror in a known place, and keeps it there. Two things move it: mechanical play, and thermal expansion. Both papers quantify one of these.

### The two routes

| Route | Part | Process | Material | Error headline |
|---|---|---|---|---|
| Machined | SHARP field selector system | CNC plates, alignment pins, bolted joints | 6xxx or 7xxx aluminium | ±0.115° combined tilt from ±0.30 mm combined shift |
| Printed | PORI chassis | L-PBF, Renishaw AM 400 | Invar36 | Visibility 0.861 to 0.878 against more than 0.98 with conventional mounts |

### What the machined route tells us

@sources/arxiv-sharp-field-selector-system-2611.06332.md converts every mechanical error into an equivalent optical tilt, then propagates that tilt through a Zemax model. The result is a small one: 0.05 degrees of output tilt grows the spot radius by about 0.2 µm. So a millimetre-scale mechanical tolerance is tolerable in this design, if the optics and the model absorb it.

The useful message for a printed mount is the method, not the number. **Measure the mount motion, convert it to the units the optics care about, then judge.** A printed bracket that moves ±0.2 mm is fine or fatal depending only on what the following optics do with that motion.

### What the printed route tells us

@sources/arxiv-monolithic-optomechanical-chassis-2611.06898.md goes further and prints the flexure stages too. The design rules it states are the transferable content:

- Keep every surface within 45 degrees of vertical, or chamfer it at 35 degrees.
- Taper each support column so the cross-section never jumps.
- Hollow the columns to cut mass without a joint.
- Set tolerances to the machine limit plus the tolerance of the part being held, not to a CNC number.

The result is a working monolithic chassis with a 13% smaller footprint. It is also a system whose visibility dropped below the conventional build, because a printed flexure is a spring with low-frequency modes.

### The rule this page should carry

Printing replaces assembly. It does not remove dynamics or thermal drift. A printed flexure trades a bolted joint for an elastic mode. A printed Invar36 body lowers thermal drift only because of the alloy, not because of the process.

For a hobby printer, the practical read is narrow. L-PBF Invar36 is a lab process. The transferable idea is the tolerance chain: state the allowed motion at the optic, and derive the allowed motion at the mount. [TENTATIVE] No source in this wiki measures that chain on a consumer FDM part.

## Snippets

> "Printing replaces assembly. It does not remove dynamics or thermal drift." — synthesis note, this page

> "The vibrational stability of the device could use some improvements as the flexures exhibited frequency eigenmodes in the low frequency regime." [Source: arxiv-2611.06898-3d-printed-monolithic-optomechanical-chassis-for.pdf p.10]
