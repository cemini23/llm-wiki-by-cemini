---
title: "FishSense Lite — A Camera-Based, Single Laser Hardware Framework with Software System for In Situ Fish Length Measurement (arXiv:2611.08732)"
type: source
related:
  - concepts/fdm-research-tools.md
  - entities/materials/pla.md
maturity: draft
read_status: read
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | FishSense Lite: A Camera-Based, Single Laser Hardware Framework with Software System for In Situ Fish Length Measurement |
| Author | Christopher L. Crutchfield, Kyle Hu, Nathan Hui, Omair Qazi, Jennifer Loch, Alli Candelmo, Brice X. Semmens, Curt Schurgers, Ryan Kastner (UC San Diego, REEF, Scripps) |
| Type | arXiv preprint (cs.CV) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2611.08732-fishsense-lite-a-camera-based-single-laser-hardw.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.08732-fishsense-lite-a-camera-based-single-laser-hardw.pdf` |
| Read status | read |

## Narrative

FishSense Lite measures fish length underwater from a single photograph. A recreational diver aims a dive laser at a fish and presses the shutter. The laser dot in the image gives the range. The range turns the fish's pixel length into a metric length.

### The printed part

The hardware is deliberately commodity. The build is a consumer dive camera, its housing, a wide-angle wet lens, and a Class IIIA 5 mW dive laser pointer, plus **one 3D-printed mount**. The mount clamps the laser to the housing cold shoe through a printed taper, body, and cap, offset from the optical axis.

The mount is **1% of the unit cost**, against about **US$1,300** total at October 2026 retail prices. Every other part is bought. The printed mount is the only part that must be made, and the authors state a diver can print it in **PLA** or order it from an online print service. That keeps the "commodity components" design goal intact.

This is a clean, well-documented example of the pattern where the printed part is small, structural, and holds a sensor or tool in a fixed relationship to another sensor. It is also a real field-validated part, not a bench prototype.

### Accuracy

| Test | Result |
|---|---|
| Rigid targets of known length | every target recovered within **1.3%** |
| Frame-level error budget | **99%** of **1,055** frames within **15%** |
| Pool, per frame | median **-2.2%** |
| Against a stereo-imaging system, 7 wild fish | mean difference **+0.8%**, no detectable bias |
| Against stereo, overall | **8.9%** difference |
| Field deployment | **73** wild fish, **seven** open-water dives |

### The field protocol the errors imply

The authors derive a protocol from the measured error sources:

- Calibrate against a dive slate on **every** dive, because the laser extrinsics move with each mount.
- Photograph the fish within **15 degrees** of perpendicular.
- Work **beyond 1 m**.
- Take **at least ten frames** of each fish.

The last rule matters most. Single-frame error is large; the median across frames is usable. That is a general lesson for any printed sensor mount: the fixture sets the geometry, but the measurement still needs repeated samples.

## Snippets

> "The mount is the only part that cannot be bought off the shelf, but it requires no specialist manufacturing." [Source: arxiv-2611.08732-fishsense-lite-a-camera-based-single-laser-hardw.pdf p.7]

> "On rigid targets of known length, FishSense Lite recovered every target to within 1.3%, and 99% of 1,055 frames fell within a 15% error budget." [Source: arxiv-2611.08732-fishsense-lite-a-camera-based-single-laser-hardw.pdf p.1]

> "Laser mount | 3D printed from files released with the paper | No, printed | 1%" [Source: arxiv-2611.08732-fishsense-lite-a-camera-based-single-laser-hardw.pdf p.6]
