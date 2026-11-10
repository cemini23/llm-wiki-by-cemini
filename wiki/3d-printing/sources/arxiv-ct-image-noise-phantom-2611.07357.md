---
title: "Evaluation of Image Noise from Computed Tomography in an Organ-Specific Anthropomorphic Phantom (arXiv:2611.07357)"
type: source
related:
  - concepts/niche-fdm-applications.md
  - sources/2024-rotoo-canine-head-phantom-vet.md
maturity: draft
read_status: read
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Evaluation of Image Noise from Computed Tomography in an Organ-Specific Anthropomorphic Phantom |
| Author | Lucas McCullum, Mojtaba Zarei, Andy Tsai, Michael J. Callahan, Peng Sun, Da Zhang (Boston Children's Hospital, Harvard Medical School, GE HealthCare) |
| Type | arXiv preprint (medical physics) |
| Location | `research to be indexed/3d-printing/arxiv-2611.07357-evaluation-of-image-noise-from-computed-tomograp.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.07357-evaluation-of-image-noise-from-computed-tomograp.pdf` |
| Read status | read |

## Narrative

This study measures how two CT reconstruction methods change image noise as the operator changes the prescribed Noise Index. It uses a commercial adult anthropomorphic phantom.

### Important limit for this wiki

**The phantom is not printed.** It is a customised Kyoto Kagaku PBU-60 model, made by a vendor. No additive manufacturing appears in the paper. The page is filed here for one narrow reason: it is a worked example of a **phantom-based imaging QA study**, which is the same measurement pattern as the printed canine-head phantom already in this wiki (@sources/2024-rotoo-canine-head-phantom-vet.md).

### Method

- Scanner: GE HealthCare Revolution Apex, software 24MW10.61, 120 kVp.
- Noise Index values: 5, 7, 8, 9, 10, 13, 15, 17, 19, 21, 30.
- Two reconstructions from the same raw data: ASiR-V at 50% strength, and DLIR at medium strength.
- Organs contoured with TotalSegmentator 2.14.0 inside 3D Slicer 5.12.3, then reviewed and hand-corrected. This is the software tool called "3D Slicer", not a 3D printer.
- Noise metric: standard deviation of the difference between two repeat images, divided by the square root of two.

### Results

| Finding | Value |
|---|---|
| Volume CT dose index against Noise Index | power law, exponent **-2.23** |
| Largest potential absolute dose cut from DLIR | liver, **1.3 mGy** [1.0 to 1.8, 95% CI], about **22%** of the ASiR-V dose |
| Organ least affected by DLIR | spinal cord and gallbladder |
| Tube current repeatability | coefficient of variation below **0.4%** |

The authors are careful about the claim. They ran no task-based or observer assessment. They call the numbers **noise-matched projections**, not validated protocol recommendations. This is the correct reading: the study shows where the two reconstructions diverge, and it does not show that a lower dose keeps diagnostic quality.

## Snippets

> "Because no task-based or observer assessment was performed, these estimates are noise-matched projections rather than validated protocol recommendations" [Source: arxiv-2611.07357-evaluation-of-image-noise-from-computed-tomograp.pdf p.2]

> "A custom-built, adult-sized, anthropomorphic phantom from Kyoto Kagaku based on the PBU-60 model was used for all image acquisitions." [Source: arxiv-2611.07357-evaluation-of-image-noise-from-computed-tomograp.pdf p.6]
