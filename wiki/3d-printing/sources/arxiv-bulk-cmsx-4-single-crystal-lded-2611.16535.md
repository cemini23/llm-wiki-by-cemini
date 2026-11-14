---
title: Bulk CMSX-4 Single-Crystal Builds via Laser-Directed Energy Deposition
type: source
tags: [paper, DED, metal, superalloy, single-crystal, industrial, background, weak-fit]
keywords: [CMSX-4, L-DED, epitaxial growth, stray grain, EBSD, IR thermography, solutionizing, thermoelectric]
related:
  - concepts/industrial-am-monitoring.md
  - sources/arxiv-track-height-control-am-2611.07704.md
updated: 2026-11-14
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Bulk CMSX-4 Single-Crystal Builds via Laser-Directed Energy Deposition: Epitaxial Stability and Microstructure Evolution |
| Authors | Divya Nalajala, Swapnil Bhure, R. Ajithkannan, Shubhang Galagali, Abhik Choudhury (Indian Institute of Science Bengaluru; IIT Madras; NITK Surathkal) |
| Type | arXiv preprint (cond-mat.mtrl-sci) |
| arXiv | 2611.16535v1, dated 12 November 2026 |
| Location | `research to be indexed/3d-printing/arxiv-2611.16535-bulk-cmsx-4-single-crystal-builds-via-laser-dire.pdf` |
| Retrieved | 2026-11-14 |
| Pages | 38 |
| Read status | read |

**Filing note.** The inbox filename reads `cmsx-4`. The correct alloy name is **CMSX-4**, a second-generation nickel-base single-crystal superalloy. It is not a thermoelectric material. There is no thermoelectric content in the paper.

## Narrative

**Weak fit for a Bambu P1S farm.** This is laser-directed energy deposition (L-DED) of a nickel superalloy, with powder feed, an 800 to 1200 W laser, and a substrate preheated to 1000 °C. No consumer printer does this. The value is the control pattern, not the process.

### The problem

A turbine blade wants one metal crystal, not many grains. A grain boundary is a weak point at high temperature. The traditional route is investment casting with directional solidification. That route gives coarse dendrites (200 to 500 µm primary arm spacing), heavy segregation, and a long solutionizing heat treatment.

Additive manufacturing could make the same part in one step with finer structure. But a layer-by-layer laser process keeps reheating the part. As the build grows, heat accumulates. The thermal gradient falls. Below a critical gradient-to-velocity ratio, stray grains nucleate, and the single crystal is lost. A constant laser power and scan speed therefore reaches only a limited height.

### What the paper adds

The authors print CMSX-4 rods, 10 mm diameter and 100 mm height, on a single-crystal CMSX-4 substrate, on a FormAlloy L-DED machine. They hold powder feed, layer height, hatch spacing, spot size and scan strategy constant, and vary only laser power and scan speed.

- **Thermal feedback in the loop.** An Optris PI05M infrared camera views the melt pool at 10 Hz. Its reading drives the laser power down as the build rises. The authors also extract melt-pool depth and thermal gradient from the same data and plot them against build height.
- **Simulation-guided cooling.** A process simulation identifies the height at which heat input and heat extraction balance. That result sizes an external cooling setup.
- **Result.** Dynamic power control alone extended epitaxial growth to about 55 mm, with stray grains appearing above that. Adding the external cooling held near-steady-state conditions, and the paper reports continuous single-crystal growth to nearly twice the height of process control alone. EBSD confirms the orientation.
- **Steady state, measured.** Primary dendritic arm spacing stays near constant over the build, which is the evidence that solidification conditions did not drift.
- **Heat treatment.** The finer as-built structure dissolves faster. Total solutionizing time falls by **47%** against the conventional schedule. After aging, the precipitate structure is close to the conventionally cast material.

### Why it is filed here

@concepts/industrial-am-monitoring.md is the hub for factory-tier metal AM. This paper is a good case study for one line on that page: a sensor reading, a model, and a controller in one loop, used to hold a microstructure rather than just a geometry. It is also the closest neighbour to @sources/arxiv-track-height-control-am-2611.07704.md, which treats DED track height as the control target.

### Limit

[TENTATIVE — one paper, one machine, one alloy, simple rod geometry] The authors say the result is promising "at the very least for simpler geometries." Blades have cooling channels and thin walls. Nothing in the paper shows single-crystal growth in a complex part.

## Snippets

> "This combined approach ensures optimal heat extraction during additive manufacturing, maintaining near-steady-state conditions at the solidification interface and extending continuous epitaxial growth to nearly twice the build height achievable through process control alone." [Source: arxiv-2611.16535-bulk-cmsx-4-single-crystal-builds-via-laser-dire.pdf p.1-2]

> "The results are promising for extending the use of L-DED in the single-crystal manufacturing of bulk samples, at the very least for simpler geometries." [Source: arxiv-2611.16535-bulk-cmsx-4-single-crystal-builds-via-laser-dire.pdf p.31]
