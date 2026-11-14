---
title: Gradient-Free Inverse Design of 3D Nanophotonic Devices Using the Level-Set Method
type: source
tags: [paper, inverse-design, photonics, 2PP, background, weak-fit]
keywords: [level-set method, Gaussian RBF, differential evolution, Nevergrad, Meep, FDTD, connected-component, Y-splitter, 2PP]
related:
  - concepts/inverse-design-am-parts.md
  - concepts/printed-photonics-background.md
updated: 2026-11-14
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Gradient-Free Inverse Design of 3D Nanophotonic Devices Using the Level-Set Method |
| Authors | Oliver Kuster, Carsten Rockstuhl, Thomas Jebb Sturges (Karlsruhe Institute of Technology) |
| Type | arXiv preprint (physics.optics) |
| arXiv | 2611.15656v1, dated 11 November 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2611.15656-gradient-free-inverse-design-of-3d-nanophotonic.pdf` |
| Retrieved | 2026-11-14 |
| Pages | 7 |
| Read status | read |

## Narrative

**Weak fit for this wiki.** The paper concerns devices about 12 µm wide. A consumer FDM printer cannot make them. The printing step is two-photon polymerization (2PP) in a photoresist, not extrusion. Read it as design-method background only.

### Problem the paper solves

A 3D nanophotonic device is designed by inverse design: state the optical goal, then search the material distribution that meets it. The usual approach is density-based topology optimization with the adjoint method. Two things go wrong. First, the continuous density field must become a binary, fabricable shape. Second, some fabrication rules are discrete, not smooth. A connected structure is one example: a part is either connected or it is not. A gradient-based optimizer cannot use that rule directly. It needs a smooth approximation, and that approximation does not guarantee true connectivity.

### Method

The paper combines a level-set method (LSM) with gradient-free optimization.

- **Geometry** — a scalar field f(r) whose level set is the material boundary. The field is a sum of Gaussian radial basis functions on a fixed grid. Only the Gaussian amplitudes are free. A 12 × 8 × 4 grid gives 384 weights.
- **Solver** — any Maxwell solver, because no adjoint is needed. The paper uses the finite-difference time-domain (FDTD) solver Meep at 10 voxels/µm.
- **Optimizer** — differential evolution. The paper uses Nevergrad's "TwoPointsDE", which sets its own hyperparameters.
- **Constraint** — connected-component analysis on the binarized field. The design passes only if the material and the void each form one connected region. A failing design gets a figure of merit of zero.

Because the geometry is defined by the Gaussians and not by the solver grid, the same weight matrix can be re-checked on a finer grid. This lets the search run coarse and the final check run fine.

### Demonstrated result

Y-splitter on a glass substrate, design region 12 µm × 8 µm × 2 µm. Wavelength 1.55 µm in air, 1 µm in the polymer. Relative permittivity 1.552 for the polymer and 1.442 for the substrate. The design reaches **42.5% coupling efficiency** into the fundamental mode, with **more than 45% flux transmission** into one output waveguide. [TENTATIVE — one paper, one device]

Cost: 10 000 iterations, 8 parallel processes on an AMD EPYC 7413, about **75 hours**. [TENTATIVE — one paper]

Re-evaluation at 20 voxels/µm matched the 10 voxels/µm result, so the coarse search did not rely on grid error.

### Why gradient-free here

The authors are explicit that gradient-based design is far cheaper at large scale. They claim only a trade: gradient-free LSM accepts non-differentiable constraints, needs no adjoint code, and stays in a low-dimensional family of smooth shapes. For a small 3D device that is enough.

Code is public at `github.com/OlloKuster/gradient_free_LSM`; the paper states it uses Nevergrad, Meep and SciPy.

### Relevance to a Bambu P1S farm

None. The method could in principle optimize a printed polymer part of any size, but every number in the paper is at the micron scale and at optical frequency. The transferable idea is the constraint pattern, not the device: **if a fabrication rule is discrete, use an optimizer that can evaluate it directly.** That idea sits on @concepts/inverse-design-am-parts.md.
