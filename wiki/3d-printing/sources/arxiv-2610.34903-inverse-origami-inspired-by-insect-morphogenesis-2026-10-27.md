---
title: "Inverse origami from insect morphogenesis — wrinkle structures that unfold into curved surfaces"
type: source
tags: [source, arxiv, shape-programming, deployable-structures]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Inverse origami inspired by insect morphogenesis: geometric design of wrinkle structures for curved surface formation |
| Authors | Kentaro Morikawa, Yuuki Shimizu, Nen Saito, Yasuhiro Inoue |
| arXiv | 2610.34903 |
| File | `arxiv-2610.34903-inverse-origami-inspired-by-insect-morphogenesis.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.34903 |
| Read status | skimmed (abstract + intro) |

## Narrative

Conventional origami starts with a flat sheet and folds it into a three-dimensional object. This paper reverses the direction. It starts with a target curved surface and derives the flat, wrinkled sheet that will unfold into it. The biological prompt is insect metamorphosis: a larva carries preformed wrinkle structures inside its body, and internal pressure unfolds them into the adult form.

The central design move is to treat a wrinkle structure as a **unidirectional stretching field**. That field states, at each point, how much stretch the structure produces when it unfolds. The authors derive the field from the geometry of the target surface, then translate the field into spatially varying wrinkle directions and spacing. The resulting designs approximate the intrinsic metric of the target surface.

The work reports three kinds of evidence: numerical construction of the designs, mechanical unfolding simulations, and 3D-printed prototypes. The last item is what makes the paper useful to a fabrication reader. The authors do not stop at a simulation. They print the wrinkle structures and unfold them.

For an FDM practitioner the relevant idea is shape programming. A flat print carries the information for a curved surface. The part deploys after printing rather than during it. This differs from printing a curved part directly, and it differs from multi-material or heat-shrink approaches, because the shape is encoded in the geometry of the wrinkle field. The paper is a design method, not a slicer feature, so applying it means generating the wrinkle geometry from a target surface yourself.

Single source, abstract-level read. The quantitative fit between design and target surface is not recorded here.

## Snippets

> "Whereas conventional origami produces three-dimensional objects by folding a flat sheet, this strategy produces curved surfaces by unfolding preformed wrinkle structures." [Source: `arxiv-2610.34903-inverse-origami-inspired-by-insect-morphogenesis.pdf` p.1 (arXiv 2610.34903), retrieved 2026-10-27]

> "We demonstrate the method on multiple target surfaces through numerical construction, mechanical unfolding simulations, and 3D-printed prototypes." [Source: `arxiv-2610.34903-inverse-origami-inspired-by-insect-morphogenesis.pdf` p.1 (arXiv 2610.34903), retrieved 2026-10-27]
