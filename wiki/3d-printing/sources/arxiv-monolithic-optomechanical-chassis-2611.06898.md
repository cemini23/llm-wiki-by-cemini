---
title: "3D Printed Monolithic Optomechanical Chassis for an Unbalanced Field-Widened Interferometer (arXiv:2611.06898)"
type: source
related:
  - concepts/precision-optomechanics-am.md
  - concepts/industrial-am-monitoring.md
maturity: draft
read_status: read
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | 3D Printed Monolithic Optomechanical Chassis for an Unbalanced Field-Widened Interferometer |
| Author | Ramy Tannous, Dogan Sinar, Sagar Patel, Tabitha D. Arulpragasam, Issa Rishmawi, Mark Kirby, Vlad Paserin, Mihaela Vlasea, Thomas Jennewein (University of Waterloo, Institute for Quantum Computing) |
| Type | arXiv preprint (physics.optics) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2611.06898-3d-printed-monolithic-optomechanical-chassis-for.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.06898-3d-printed-monolithic-optomechanical-chassis-for.pdf` |
| Read status | read |

## Narrative

The authors print a complete optomechanical chassis for a field-widened, unbalanced Mach-Zehnder interferometer. The part houses the optics, the flexure alignment stages, and the mounting pockets in one printed body. They call the chassis AMOC, and the combined instrument PORI.

### Process and material

- **Process:** laser powder bed fusion (L-PBF), on a Renishaw AM 400. Minimum feature size is about 35 µm.
- **Material:** Invar36. Its low coefficient of thermal expansion limits thermal phase drift.
- **Baseplate:** stainless steel.
- **Tolerances:** 0.25 mm on tight features, 0.3 mm on the rest. The authors state these are large against CNC practice and reflect both machine resolution and the tolerances of the commercial optics.

### Design rules the paper states

| Rule | Reason |
|---|---|
| Avoid unsupported overhangs above 45° from vertical | The melt pool collapses without support |
| Taper every support column (the "Loft Island") | Abrupt area changes cause print failure |
| Chamfer the tabletop at 35° from vertical | Removes the last unsupported overhang |
| Hollow each support column | Cuts mass while keeping the part monolithic |

The flexures give at least 3 mm of travel on the mirror optical axis and 1.5 mm on each perpendicular axis. A COMSOL model set a target safety factor of 1.3 against the bulk Invar36 yield strength of 276 MPa. Two set screws per axis drive the stage; the compliant beams act as springs.

### Results

| Requirement | Outcome |
|---|---|
| Reduced form factor | **13%** smaller footprint than COTS optomechanics with 2-inch optics; about **20%** smaller volume with 1-inch optics |
| Monolithic, assembly free | Met. Only support removal and screw insertion after printing |
| Adjustable mounts | Met. Flexures aligned the system to usable performance |
| Vibration and thermal stability | **Partly met.** Low-frequency flexure eigenmodes remain; added damping material only reduced the response |

Two results limit the claim. First, the 20-hour print **failed** before the end. The missing upper layers left the large spherical-mirror flexures incomplete, and the error was not specific to the design. Second, interference visibility reached **0.861 ± 0.025** for single-mode input and **0.878 ± 0.038** for multimode input. Earlier builds of the same optical architecture with conventional mounts reached **more than 98%**. The authors attribute the gap to the flexure vibration and to the incomplete print.

The honest reading: monolithic metal printing can replace an assembly, but a printed flexure is a spring with low-frequency modes, and low-frequency modes disturb an interferometer. [TENTATIVE] The visibility gap may narrow with a complete print and stiffer flexures; the paper does not demonstrate it.

## Snippets

> "To the knowledge of the authors, this work represents the first demonstration of a fully 3D printed monolithic optomechanical enclosure for an interferometer with built-in adjustable flexure mounts." [Source: arxiv-2611.06898-3d-printed-monolithic-optomechanical-chassis-for.pdf p.1]

> "The vibrational stability of the device could use some improvements as the flexures exhibited frequency eigenmodes in the low frequency regime." [Source: arxiv-2611.06898-3d-printed-monolithic-optomechanical-chassis-for.pdf p.10]

> "the resulting chassis was largely functional, though the missing upper layers introduced" [Source: arxiv-2611.06898-3d-printed-monolithic-optomechanical-chassis-for.pdf p.12]
