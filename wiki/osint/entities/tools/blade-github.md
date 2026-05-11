---
title: "BLADE — Bayesian List-wise Alignment via Dynamic Estimation (GitHub repo)"
type: entity
tags: [github, ml-research, recommendation, list-wise-alignment, license-unknown, do-not-adopt-code, methodology-study-only, sigir-2026, k33]
keywords: [BLADE, RegionCh, listwise-alignment, GRPO, recommendation-research, bayesian-alignment, missing-license, default-copyright, stale-pre-publication]
related:
  - sources/blade-bayesian-listwise-alignment.md
  - concepts/llm-listwise-alignment.md
  - concepts/cemini-license-posture.md
  - sources/leworldmodel-2603.19312v2.md
maturity: draft
created: 2026-05-07
updated: 2026-05-11
---

## Relations

- @sources/blade-bayesian-listwise-alignment.md — the SIGIR '26 paper this repo accompanies.
- @concepts/llm-listwise-alignment.md — concept hub for the methodology this repo implements.
- @concepts/cemini-license-posture.md — falls into the "Unknown / no LICENSE → default copyright = REJECT pending upstream clarification" bucket.

## Raw Concept

The reference implementation accompanying @sources/blade-bayesian-listwise-alignment.md, published at `https://github.com/RegionCh/BLADE`. K33 verification snapshot recorded 2026-05-07.

## Narrative

### Repo status snapshot (2026-05-07)

| Field | Value | Source |
|---|---|---|
| URL | `https://github.com/RegionCh/BLADE` | paper |
| HTTP status | 200 OK | curl `-sIL` 2026-05-07 |
| Stars | 1 | GitHub API `/repos/RegionCh/BLADE` |
| Forks | 0 | same |
| Created | 2026-01-23 | same |
| Last push | 2026-01-27 | same |
| License | **None / unspecified** | same (`license: null` in API response) |
| Description | None | same |
| README | Unverified | not deep-checked |

### Adoption verdict: STUDY-METHODOLOGY ONLY (do not vendor)

Two compounding concerns:

1. **Missing LICENSE → default copyright.** Per @concepts/cemini-license-posture.md "Unknown / no LICENSE" bucket, the repo's code is fully copyrighted by RegionCh with no explicit grant of use. This is poison-pill mode #3 in Cemini's catalog. Even under the 2026-05-06 monetization-priority directive (softened auto-rejects for non-prod-codebase use), unlicensed code is not safe to vendor — if the repo is later given a restrictive license, any code Cemini copied retroactively becomes infringing.

2. **Stale relative to paper publication.** The paper was submitted to arXiv 2026-05-06; the repo's last push is 2026-01-27 — over **3 months before publication**. This is a pre-publication snapshot that may not reflect the final method as described in the paper. Risk: if Cemini study-replicates from the repo rather than the paper, the implementation diverges from the published method.

### Recommended path

The paper itself is **CC BY 4.0** (licensed for commercial reuse with attribution). Re-implement BLADE from the paper's mathematical description (Eqs. 5–7 + the Bayesian update procedure in §3, both derivable in 1–2 pages). GRPO implementation is widely available in DeepSeek-R1's open codebase and Cemini's intended Conductor backbone — no need to vendor any unlicensed code.

If Cemini ever wants to use BLADE-style alignment for ticker ranking, news ranking, or routing-policy training (per @concepts/llm-listwise-alignment.md application surfaces), the workflow is:

1. Read the paper's §3 carefully — the Bayesian fusion formula and the dynamic CDF update procedure.
2. Implement on top of an existing GRPO backbone (DeepSeek-R1's released training code, or a Cemini-internal port).
3. Validate against the paper's Table 1 NDCG@5 numbers on a recommendation benchmark before generalizing.
4. Do NOT clone or import code from `RegionCh/BLADE` until the upstream adds an explicit LICENSE.

### Re-verification triggers

Recheck repo state if:
- Cemini begins a serious BLADE-port workstream (then re-verify license, README quality, dependency tree, citation count).
- The paper gets accepted at SIGIR '26 (July 2026) — authors typically push final code at conference time.
- A GitHub `LICENSE` file appears at `RegionCh/BLADE` (then re-evaluate per @concepts/cemini-license-posture.md license catalog).

## Snippets

- API response 2026-05-07: `stars=1 fork=0 created=2026-01-23T11:04:40Z pushed=2026-01-27T03:48:19Z license=None desc=None`. [Source: GitHub API /repos/RegionCh/BLADE retrieved 2026-05-07]
