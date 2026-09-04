---
title: Deep-CFR-2025 — Deep CFR / SD-CFR with LightGBM advantages
type: entity
tags: [tool, k255, poker, cfr, mit, gambling]
keywords: [Deep-CFR-2025, LUGL, PokerRL, LightGBM, SD-CFR, milecdav]
related:
  - sources/arxiv-2609.03660-lugl-poker-games-2026-09-04.md
  - concepts/k255-poker-game-theory-wave.md
maturity: draft
created: 2026-09-04
updated: 2026-09-04
phase_0_verdict: CONDITIONAL-GO REFERENCE
harness_verb: FILE
wire_note: Laptop REFERENCE only; no Arena decide() path; no prod scp; untrusted pickles in trained_agents/
---

## Relations

- @sources/arxiv-2609.03660-lugl-poker-games-2026-09-04.md — LUGL paper (arXiv 2609.03660)
- @concepts/k255-poker-game-theory-wave.md — K255 poker / imperfect-information cluster

## Raw Concept

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/milecdav/Deep-CFR-2025 |
| **License** | MIT `[CONFIRMED]` gh api SPDX 2026-09-04 + `LICENSE` MIT (copyright Eric Steinberger 2019) |
| **Local** | `.local/adopts/Deep-CFR-2025` (~159MB, shallow `--depth 1`) |
| **Stars** | 0 (2026-09-04) |
| **Last push** | 2026-06-25 (`2c9356b` Removed PLAN file) |

K255 Phase-0 covering the LUGL poker wave. LUGL (arXiv:2609.03660) cites PokerRL / luglrl; no verified public LUGL runtime repo this session. This fork is the Deep CFR + LightGBM advantage lane that matches the paper’s non-incremental-learner claim.

## Narrative

**Pattern.** Scalable Deep CFR and Single Deep CFR (SD-CFR) on [PokerRL-2025](https://github.com/theGholland/PokerRL-2025). Fork of Steinberger / TinkeringCode Deep-CFR. Main addition: LightGBM backend for the advantage approximator (`DeepCFR/lightgbm_adv.py`, `--adv-model-type lightgbm`) versus a feedforward NN, with SLURM H2H matrices on Flop5Holdem and Leduc exploitability scripts. Checkpoints default to `~/poker_ai_data/`.

**Domain fit vs Cemini.** Poker Arena / gambling-wiki research only. Existing coverage: @entities/tools/rlcard.md (MIT offline CFR/NFSP baselines; gambling-wiki primary) and @entities/tools/pokerkit.md (Arena engine). K130 eval listed **PokerRL as reference-only** (@sources/eval-poker-github-repos-2026-06-26.md). Do not substitute this stack for PokerKit on the Arena `decide()` path. LUGL’s public `luglrl` runtime was not verified; this clone is the CFR REFERENCE stand-in.

**Failure-mode audit (research-RL / 0-star fork class).**

| Check | Result |
|-------|--------|
| License | MIT `[CONFIRMED]` |
| Maturity | **0 stars**; last push 2026-06-25 (~71d idle as of 2026-09-04) |
| Provenance | Clone is `milecdav/Deep-CFR-2025`; `pyproject.toml` Homepage is `theGholland/Deep-CFR-2025` `[TENTATIVE]` fork identity |
| Git dep | `PokerRL @ git+https://github.com/theGholland/PokerRL-2025.git` — extra clone, not SPDX-audited this session |
| Hardcoded path | `~/poker_ai_data/` for logs, checkpoints, TensorBoard |
| Stack | Python ≥3.12, `torch==2.8.0`, `ray[default]==2.48.0`, LightGBM, SLURM — Linux; Mac “not tested” |
| Pickles | `trained_agents/*.pkl` — do not unpickle untrusted agents |
| Arena overlap | Steal offline only — same dead-end as RLCard (latency + env mismatch) |

**Verdict rationale.** **CONDITIONAL-GO REFERENCE** (2026-09-04). MIT is clean and the LightGBM-vs-NN experiments match LUGL’s thesis. 0-star + 71-day idle + PokerRL git dependency + homepage mismatch keep this off Integrate. `harness_verb: FILE`. Laptop clone only. Re-check if LUGL publishes a verified `luglrl` repo. Route briefs to Poker Arena / gambling-wiki. **No prod scp.**

## Snippets

> "This repository is based on the original Deep-CFR implementation by Eric Steinberger, extended for our experiments comparing neural-network and LightGBM advantage approximators in SD-CFR on Flop5Holdem and Leduc." [Source: milecdav/Deep-CFR-2025 README.md (clone 2026-09-04)]

## Dead Ends

- Vendor DeepCFR into Arena `decide()` — env and latency mismatch vs PokerKit table dict (same as RLCard).
- `pip install .` on a shared laptop without an isolated venv — Ray / torch / `/dev/shm` footprint.
- Treat 0-star `milecdav` fork as the LUGL canonical runtime until `luglrl` SPDX is verified.
