---
title: "Towards Track Height Control in Additive Manufacturing on Porous Substrates (arXiv:2611.07704)"
type: source
related:
  - concepts/extrusion-control.md
  - concepts/industrial-am-monitoring.md
maturity: draft
read_status: read
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Towards Track Height Control in Additive Manufacturing on Porous Substrates: An Approach for System Identification and Controller Selection |
| Author | Amelie Schatull, Torge Kolditz, Simon Kleinschmidt, Annika Raatz, Jorg Seewig (RPTU Kaiserslautern-Landau, Leibniz University Hannover) |
| Type | arXiv preprint (eess.SY) |
| Location | `research to be indexed/3d-printing/arxiv-2611.07704-towards-track-height-control-in-additive-manufac.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.07704-towards-track-height-control-in-additive-manufac.pdf` |
| Read status | read |

## Narrative

The paper targets a metal process: laser-based directed energy deposition (DED-LB) on a substrate that has pores. The goal is to build a non-porous skin over a porous core. The control problem is the track height. When the melt pool meets a pore, the deposited track drops, and the part geometry departs from the plan.

### Important limit for this wiki

This is a **conceptual paper**. It reports no experimental control result. It compares controller classes and states which one fits the authors' machine. Do not read it as a validated recipe.

### Measurement setup

A Micro-Epsilon ScanControl3000-25/BL laser line triangulation sensor measures track height and width. It uses a 405 nm laser, a 2048 x 1088 sensor matrix, and a 25 x 15 mm field of view. The same sensor also maps the pore geometry before deposition. Feedstock is AISI 316L stainless steel powder.

### The three controller classes

| Class | How it works | Strength | Limit |
|---|---|---|---|
| Feedforward | Pre-measured pore depth plus target height sets a modified scan speed, written into the G-code in advance | No change to the machine interface; no sensor near the melt pool | Blind to any height change not in the pre-scan; correction cannot react during the build |
| Feedback | The sensor reads live track height; the error drives new parameters such as scan speed or laser power | Reacts to height, width and temperature changes during the build | Needs a real-time controller, an open PLC link (the paper names PROFINET), and a heat-resistant sensor |
| Lookup table | A design-of-experiments table maps parameter sets to track height; linear interpolation between points | Fast and simple; runs in real time | Accuracy depends on the table range; extrapolation is unsafe; a nozzle change needs a new table |

### System identification

The paper's main methodological point is a small one, and it is useful. Standard practice makes one track per parameter set. That gives steady-state values only. The authors propose **step changes in laser power and scan speed along a single track**. One track then yields both the steady-state response and the dynamic response. Sinusoidal and ramp inputs are named as the next step, because a step test cannot show all non-linear behavior.

### Recommendation for this machine

Feedforward first, because it needs no change to the communication interface. The knowledge gained then supports a feedback controller once the interfaces are open and the sensor is heat resistant. Combining feedforward with feedback is expected to cut response time and overshoot, as prior work reports.

**Transfer to FDM:** the three-class comparison maps cleanly onto consumer filament printing. Marlin and Klipper pressure advance is a feedforward term. A filament-width or flow sensor in a closed loop is feedback. A slicer flow table per filament is a lookup table. The paper gives no evidence about which wins on FDM. [OPEN QUESTION 2026-11-10] Which class is best for a Bambu P1S print farm is not answered by any source in this wiki.

## Snippets

> "a key challenge when working with porous substrates are geometrical distortions along the deposited tracks as they traverse multiple layers" [Source: arxiv-2611.07704-towards-track-height-control-in-additive-manufac.pdf p.2]

> "by varying the system's input in a step-wise manner ... the dynamics of the process can be enhanced and used in the process model" [Source: arxiv-2611.07704-towards-track-height-control-in-additive-manufac.pdf p.4]
