---
title: "v10.11 skipped — no lane for these inbox PDFs"
type: source
related:
  - sources/eval-multi-wiki-link-revenue-v10.11-2026-11-03.md
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

Type: reject record for inbox PDFs with no Cemini lane.

| Field | Value |
|-------|-------|
| arXiv | 2610.42078, 2611.03530, 2611.00360 |
| Retrieved | 2026-11-03 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/<domain>/` |
| Read status | skimmed (title and abstract only) |

## Narrative

These arrived in the inbox because the digest query is global and the inbox is per domain. Filing the ids here makes the next `preingest_check.py` call them duplicates.

| arXiv | Inbox | Why it is skipped |
|---|---|---|
| 2610.42078 | ccc | **Embodied Movable Antennas.** Telecom architecture: use a robot's existing mechanical degrees of freedom to reposition an antenna, and derive a Fourier representation of the resulting multipath channel. Wireless engineering. Nothing in this workspace designs a radio link. |
| 2611.03530 | image-gen | **Generalizable Equivariant Diffusion Models for Non-Abelian Lattice Gauge Theory.** Physics. Diffusion models applied to lattice QCD field configurations; the diffusion machinery is incidental to the physics goal. No image-generation transfer without reading 28 pages of gauge theory. |
| 2611.00360 | osint | **Recurrence in Sequence Space: How Epistasis Mimics Shared Ancestry.** Molecular biology. Protein sequence correlations lower the intrinsic dimension of sequence space and make independent lineages look related. The word "ancestry" is the only overlap with this workspace, and it means phylogenetic ancestry, not human genealogy. **A title scan would wrongly route it to Atto.** |

**No install. No clone.** Three papers, three unrelated fields, one shared reason: the routing came from a global digest, not from fit.

## Snippets

> "We show that such correlations lower the intrinsic dimension dIN of sequence space, counteracting the concentration of measure and broadening the distribution of pairwise distances." [Source: arxiv-2611.00360 p.1]

## Dead Ends

- **Routing on the word "ancestry".** In 2611.00360 it is protein phylogenetics.
