---
title: "Genealogical reinforcement in branching processes"
type: source
related:
  - concepts/k296-feeds-wave.md
  - concepts/genealogical-reinforcement-branching.md
  - concepts/computational-genealogy-archival-automation.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Genealogical Reinforcement in Branching Processes |
| Author | Alina Kochocki (Loyola Marymount University) |
| Type | arXiv preprint, q-bio.PE |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf` |
| Retrieved | 2026-11-10 |
| File | arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf (11 pages) |
| Read status | read |

## Narrative

The paper models a population where reproduction depends on the local family tree. Resource transfer follows genealogical distance, so a large local family gets more resource and produces more offspring. The author calls this **genealogical reinforcement**.

The model is a discrete-time branching process with three free parameters.

- Each individual has `ξ(v) ∈ {0, 1, 2}` offspring, drawn from a binomial with probability `p(v)`.
- `p(v) = 1 / (1 + exp(-β0 - β1 G(v)))`. When `β1 = 0` the process is an ordinary Galton–Watson process.
- `G(v) = Σ e^(-θ d(u,v))` sums the influence of living relatives within distance `2D`. The parameter `θ` sets how fast influence decays with distance, and `D` sets the depth of dependence.

[Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf pp.2-3]

### Statistical framework

The paper gives a maximum-likelihood estimator for `(β0, β1, θ)` when the tree is fully observed, and a likelihood-ratio test for the null of independent branching.

Two results matter for anyone who wants to fit this to data.

- **Identifiability needs depth and variation.** With `D ≥ 2`, the three parameters are globally identifiable if the sample shows at least two distinct non-zero genealogical distances and linearly independent relative-count vectors. With `D = 1` the parameters are degenerate. [Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf p.4]
- **The null distribution must be simulated.** `β1` sits on the boundary of the parameter space, and `θ` is unidentifiable under the null. Wilks' theorem does not apply. The paper simulates the null and reports 95th-percentile thresholds of **11.11 (D = 3)** and **12.11 (D = 5)**. Detection power rises sharply when deeper relationships are observed. [Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf p.6]

The final section identifies the process with a tree-valued multitype branching process on a finite type space. The number of tree types grows by the recurrence `ρ_D = (ρ_{D-1}+1)(ρ_{D-1}+2)/2`.

### Why it matters here

This is not an archival-genealogy paper. It is a population-dynamics paper. The word "genealogical" here means **kinship distance inside a reproducing population**, not civil records.

The transferable idea is the modelling shape: **local structure as a predictor of local growth**. That shape applies to any system where a node's success depends on the density and quality of its neighbourhood. Candidate uses are graph-based feature engineering and the sibling/kinship features in an entity-resolution pipeline.

The paper is honest about scope: it is a toy model for one mechanism, not a social model.

## Snippets

> "A large family structure at short genealogical distances is most likely to beget a locally large family. We refer to this concept as genealogical reinforcement." [Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf p.1]

> "If β1 = 0, independent branching is recovered, similar to a traditional Galton-Watson process." [Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf p.2]

> "The parameters β0, β1, and θ are globally structurally identifiable ... if the sample falls into at least one of the following two cases." [Source: arxiv-2611.08548-genealogical-reinforcement-in-branching-processe.pdf p.4]

## Dead Ends

- **Routing this to Atto by keyword.** "Genealogical" is a false lead here, as it was for arXiv 2610.40772 (DiscKosky). The paper has no archive, HTR, or record-resolution content.
- **Fitting the model to a partial pedigree.** The identifiability result needs observed local subtrees and several distinct genealogical distances. A sparse family tree will not identify the parameters.
