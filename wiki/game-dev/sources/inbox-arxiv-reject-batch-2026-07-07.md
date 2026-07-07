---
title: Inbox arXiv reject batch — 2026-07-07 (arXiv-API fallback mis-route: AV + graphics + quant)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, mis-route, autonomous-driving, backtesting]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-05.md
  - sources/inbox-arxiv-reject-batch-2026-07-04.md
  - sources/inbox-arxiv-reject-batch-2026-07-03.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
  - concepts/rts-networking-deferred.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-07
updated: 2026-07-07
---

## Raw Concept

Five PDFs from `2026-07-07-daily.md`. **All reject** — the `game-navmesh-dynamic` cluster fell back to the free arXiv API (Exa returned 0 game-dev hits) and pulled unrelated autonomous-driving, graphics, and quant-SE papers. No game-dev adoption; no Phase-0. The `2026-07-06-daily.md` sweep was empty (0 papers, 0 news).

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.04768 | Physics-Based Simulation of Contact-Induced Facial Wrinkling | **Reject** | ETH Zürich / Meta Reality Labs FEM skin sim; VFX/character graphics, not castle-sim 2D-iso/SH2 clone. Art-pipeline stays @image-gen-wiki |
| 2607.04770 | Cam2Sim (closed-loop AV sim) | **Reject** | Autonomous driving neural scenario reconstruction; out of scope |
| 2607.04803 | E-CoDrive (energy-critical AV co-sim) | **Reject** | Autoware AEV energy testing; out of scope (echoes CommonRoad AV re-drops) |
| 2607.04953 | Real-World Perturbation Testing of AV Systems | **Reject** | Autonomous driving robustness testing; out of scope |
| 2607.04958 | Look-Ahead-Freedom as Temporal Non-Interference | **Reject (route @osint-wiki)** | Quant backtesting / data-leakage correctness (TOSEM); type-and-effect verification. CeminiSuite backtest relevance, not game dev |

### Notes

- **2607.04958** is the only near-miss: "temporal non-interference over a time-indexed information lattice" is a formal correctness property for backtests/agentic pipelines. There is a *tangential* RTS analog — deterministic **lockstep replay** must never let a later tick's state influence an earlier tick's decision — but that is a Tier-N networking concern (@concepts/rts-networking-deferred.md), not a slice adoption. Primary home is @osint-wiki (CeminiSuite). No brief.
- **2607.04768** wrinkle sim could theoretically inform high-fidelity 3D character faces, but Fork B SH2 clone has no facial rig scope; if art ever needs it, route to @image-gen-wiki.

**No Phase-0:** none of the five ship a game-dev tool/engine repo for castle-sim.
**No new brief:** no adoption David should be using surfaced in this batch.

**Action:** Archive 5 PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW
Paper lane: game-navmesh-dynamic cluster used arXiv API fallback (Exa 0 hits) → mis-route
```

## Dead Ends

- Treating arXiv-API-fallback rows as game-dev candidates — fallback ignores the game-dev query intent; verify abstracts before ingest
