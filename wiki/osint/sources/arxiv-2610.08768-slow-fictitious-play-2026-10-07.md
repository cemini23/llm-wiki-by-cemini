---
title: "Arbitrarily slow polynomial convergence of fictitious play (arXiv 2610.08768)"
type: source
tags: [source, k284, arxiv, game-theory, fictitious-play, poker, math]
keywords: [fictitious-play, convergence-rate, zero-sum, nash, karlin-conjecture, duality-gap]
related:
  - concepts/k284-arxiv-wave.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-arxiv-wave.md

## Raw Concept

| Title | Arbitrarily Slow Polynomial Convergence of Fictitious Play |
| Authors | Jacob Abernethy (Georgia Tech), John Lazarsfeld (GT / Google Research), Andre Wibisono (Yale) |
| Type | arXiv preprint (cs.GT) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.08768-arbitrarily-slow-polynomial-convergence-of-ficti.pdf` |
| Retrieved | 2026-10-07 |
| arXiv | 2610.08768v1 |
| Code | `github.com/awibisono/fictitious-play-experiments` |
| read-status | read |

## Narrative

**Fictitious play** is the oldest learning dynamics for games. This paper shows it can converge at **arbitrarily slow polynomial rates** in two-player zero-sum games — settling whether Wang's Θ(t^{−1/3}) rate was a fundamental limit. **It is not.**

### Construction

For every integer **k ≥ 2**, recursively build a skew-symmetric payoff matrix `Âk` with **n_k = (k+1)² − 5 actions per player** such that the duality gap

    Gap_{Âk}(z_t/t, z_t/t) = Θ(t^{−1/k})

Start from **rock-paper-scissors** and inductively "lift" an order-k game to order k+1 (keep one parent copy, add 2k+3 actions). After a prescribed setup action, every best response is **unique** (no tie-breaking games). A "clock" structure sets phase length Θ(σ^{k−1}) and height Θ(σ^{k−1}). For k ≥ 3 this gives **counterexamples to Karlin's O(t^{−1/2}) conjecture.** There is **no universal exponent γ**.

### The rate in dimension

    α_{n_k} = 1/k = 1/(√(n_k + 5) − 1),  i.e.  t^{−Θ(1/√n)}

n_k = 4, 11, 20, 31, 44, 59, 76 for k = 2…8. A separate 7×7 cubic construction is smaller than Wang's 10×10.

### Why it matters here

A **worst-case lower bound on convergence** for a core game-solving algorithm. Relevant when anyone claims a regret-matching/FP method "converges fast" — it can be arbitrarily slow. Ties to the poker/CFP lane (@sources/arxiv-2610.07686-bluffjax-2026-10-07.md). **No license stated.** AI-disclosure: ChatGPT 5.6 Sol / 6 Astra, Gemini 4 Pro.

## Snippets

> "For every integer k ≥ 2, a skew-symmetric payoff matrix with n_k = (k+1)² − 5 actions per player gives a duality gap Θ(t^{−1/k})." [Source: arxiv-2610.08768-arbitrarily-slow-polynomial-convergence-of-ficti.pdf]

> "For k ≥ 3 this gives counterexamples to Karlin's O(t^{−1/2}) conjecture." [Source: arxiv-2610.08768-arbitrarily-slow-polynomial-convergence-of-ficti.pdf]
