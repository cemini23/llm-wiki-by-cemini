---
title: "A 3D measurement workflow for assessing replication quality and tool degradation in moulded microfluidic channels"
type: source
tags: [source, arxiv, metrology, microfluidics, injection-moulding, 3d-printed-tooling]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A 3D measurement workflow for assessing replication quality and tool degradation in moulded microfluidic channels |
| Authors | Mehmet Oğulcan Güngör, Jérôme Charmet, Ender Yıldırım |
| arXiv | 2610.39046 |
| Pages | 39 |
| File | `arxiv-2610.39046-a-3d-measurement-workflow-for-assessing-replicat.pdf` |
| Retrieved | 2026-11-01 |
| Read status | skimmed (abstract and first page) |

## Narrative

Mould-based replication with 3D-printed inserts needs a check of how faithfully a microchannel transfers from master to polymer replica. The common check takes a width or depth ratio from one cross-section. That method misses sidewall shape and depends on where the section is cut.

The paper presents a whole-channel workflow. It uses 3D scans of the master and the replica, so no sectioning is needed. The scans register to a common grid. Each height map becomes a map of local slope. The correlation of the two slope maps over the channel interior, written RQ_d, is the reported quality metric.

**Why this matters for printed tooling.** The paper treats the printed insert as a tool that wears. The metric therefore tracks two things at once: replication fidelity and degradation of the tool across moulding cycles. That is the failure mode a printed injection-mould insert actually has.

**Scope note.** The work is microfluidics. Channel dimensions are on the microscale, measured with optical profilometry and gradient correlation. The method is not a general dimensional-inspection recipe for large FDM parts. It transfers where surface form matters more than overall dimension.

## Snippets

> "Mould-based replication, such as injection moulding with 3D-printed inserts, needs a check of how faithfully microchannels are transferred from master to polymer replica." [Source: arxiv-2610.39046 p.1]

> "The scans are registered on a common grid, and each height map is converted into a map of local slope. The correlation of the two slope maps over the channel interior, RQ_d, is reported." [Source: arxiv-2610.39046 p.1]

## Dead Ends

- **Reading RQ_d as a general part-quality score.** The metric is defined over channel interiors on microscale scans. It does not measure large-part dimensional accuracy.
