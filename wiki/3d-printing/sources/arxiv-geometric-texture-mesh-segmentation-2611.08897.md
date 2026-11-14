---
title: "Segmenting Geometric Textures of 3D Meshes (arXiv:2611.08897)"
type: source
related:
  - concepts/ai-design-tools.md
maturity: draft
read_status: read
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Segmenting Geometric Textures of 3D Meshes |
| Author | Weidan Xiong, Kaijie Qu, Shihao Feng, Shunqi Fan, Rongyu Xiong, Hui Huang (Shenzhen University, NetEase, NTU Singapore) |
| Type | Conference paper, Pacific Graphics 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2611.08897-segmenting-geometric-textures-of-3d-meshes.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.08897-segmenting-geometric-textures-of-3d-meshes.pdf` |
| Read status | read |

## Narrative

This is a computer-graphics paper. It segments a 3D mesh by **middle-level geometric texture**, not by semantic part and not by low-level curvature. Geometric texture here means high-frequency, repetitive surface detail, such as carved patterns and woven surfaces.

### Method

1. Render several views of the input mesh.
2. Segment texture regions in each rendered image with a visual segmentation model, fine-tuned on a new benchmark the authors built.
3. Extract DINO features from each segmented patch and cluster them into groups.
4. Fuse the 2D predictions into 3D with a weighted voting scheme.
5. Edit the mesh with a filter-based geometric operator.

The output is an interactive tool for texture enhancement, removal, and replacement, plus mesh retrieval by texture similarity.

### Fit for this wiki

**Weak.** The paper names 3D printing once, in the application list, and performs no print. The relevant content is upstream of printing: a scanned or sculpted model with surface texture becomes editable by texture region. A designer who prints decorative surface detail would use that capability. Nothing in the paper speaks to slicers, filament, tolerance, or support.

The one durable asset is the public dataset and benchmark at `github.com/ALingll/GTSeg`. If a textured mesh ever needs to be split into printable decorative regions, that is the first place to look. [OPEN QUESTION 2026-11-10] Whether the segmentation survives a remesh or a repair step, as a slicer would apply, is not tested.

## Snippets

> "Recognizing geometric texture patterns on 3D models is critical for applications such as heritage protection, model editing, and 3D printing." [Source: arxiv-2611.08897-segmenting-geometric-textures-of-3d-meshes.pdf p.1]

> "The datasets are publicly available at: https://github.com/ALingll/GTSeg" [Source: arxiv-2611.08897-segmenting-geometric-textures-of-3d-meshes.pdf p.2]
