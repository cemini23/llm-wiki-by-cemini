---
title: "Scale-rich network metamaterials grow by local rules on a recursive cell division (arXiv 2611.16513)"
type: source
related:
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Scale-rich network metamaterials grow by local rules on a recursive cell division |
| Author | Alexei Vazquez (Nodes & Links Ltd, Cambridge) |
| Type | arXiv preprint, physics / network science |
| arXiv | 2611.16513v1, 13 Nov 2026 |
| Pages | 10 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.16513-scale-rich-network-metamaterials-grow-by-local-r.pdf` |
| Retrieved | 2026-11-14 |
| Read status | read |

## Narrative

### What the paper does

Both et al. introduced scale-rich mechanical metamaterials: planar ligament networks where length, thickness and connectivity span orders of magnitude. The authors attributed the degree distribution P(k) ~ k^-3 to spatial preferential attachment, because longer ligaments offer a larger target.

This paper tests that explanation. It shows the construction is Cowan's iterated cell division with area-weighted selection. In the dual graph, where ligaments are nodes and junctions are links, the growth rule is face-local: a new node joins two nodes on the boundary of one face.

### The two mechanisms

Both mechanisms produce the same exponent in two dimensions. They differ in the mechanism and in the fluctuations.

| | Mechanism A | Mechanism B |
|---|---|---|
| Rule | Preferential attachment on face incidences | Length as fitness, fixed at birth |
| Degree growth | k_i = 2 sqrt(t/i) | Same on average |
| Source of randomness | History of hits | Birth length |
| Fluctuations | Reinforcing; variance far above the mean | Poisson around the prediction |
| 3D exponent | 2.44 | 5/2 |

The measured dispersion of degree around each ligament's own prediction is 0.92 to 1.38, close to the Poisson value of 1. Under a topological surrogate that realises mechanism A, the variance at fixed age exceeds the mean by a factor of 10 to 91. The geometry therefore selects **fitness by birth length**, not reinforcement.

### Secondary results

- Cell areas follow the spacing law of uniform points; the cell genealogy is a random binary search tree, with split depth growing as 2 ln t.
- The corner-cut probability follows from integral geometry. For a square it is 2 ln 2 / π = 0.4413.
- The clustering spectrum is C(k) ≈ 2p/k, with mean clustering 0.38.
- Square-closing splits raise shortest-path multiplicity above the value for a randomised graph with the same degree sequence.
- No design parameter moves γ = 3 while the hit rate stays proportional to length and birth length stays proportional to local cell size.

### Why it is filed here

**This paper has no practical Cemini project link.** It is materials physics and network-growth theory. The only shared vocabulary is "preferential attachment", which appears in some market-microstructure and holder-concentration literature. That overlap is a word, not a method.

The paper is recorded because it arrived through the global digest into the osint inbox, and because the fitness-versus-reinforcement test is a clean, reusable identification argument. A reader who wants a template for telling a fitness model from a reinforcement model can read Section III. Nothing here should be wired into Atto, GuruWatcher, Basgiath, CeminiDFS, CeminiParlays, the XSP bot, or the PM/Kalshi retail bot.

[OPEN QUESTION 2026-11-14] No Cemini lane needs a network-growth model. Recorded as a possible future negative-test template only.

## Snippets

> "Length is a fitness assigned by the cell hierarchy, ℓ_i ∝ i^(-1/2), and the k^-3 tail follows." [Source: arxiv-2611.16513-scale-rich-network-metamaterials-grow-by-local-r.pdf p.1]

> "The reported per-ligament energy law cannot distinguish degree from length or age." [Source: arxiv-2611.16513-scale-rich-network-metamaterials-grow-by-local-r.pdf p.1]
