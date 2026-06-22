---
title: NFL Coherence-Risk Feature Suite (ClarusC64)
type: concept
tags: [concept, nfl, dfs, ceminidfs, feature-engineering, gambling, k126]
keywords: [clarusc64, coherence-risk, playcall, pass-protection, nflverse, stage-2-features, ceminidfs]
related:
  - sources/links-6-22-tool-eval.md
  - concepts/active-project-research-routing.md
  - "@gambling-wiki/concepts/diy-nfl-dfs-model-architecture.md"
maturity: draft
created: 2026-06-22
updated: 2026-06-22
---

## Relations

- @sources/links-6-22-tool-eval.md — K126 tool eval URLs 30–39 (10× MIT ClarusC64 datasets + Karmane rest/travel sample)
- @gambling-wiki/concepts/diy-nfl-dfs-model-architecture.md — CeminiDFS canonical pipeline architecture (stage 2 projection layer); bidirectional K126 backlink

## Raw Concept

What prompted this page: K126 links.docx flagged **10 MIT Hugging Face datasets** from ClarusC64 measuring tactical **coherence risk** — structural breakdown signals absent from vanilla nflverse volume/usage projections.

## Narrative

ClarusC64 publishes a tabular suite (`*-coherence-risk-v0.1`) isolating situational breakdown markers:

| Dataset | Steal target |
|---------|--------------|
| playcall-defense-coherence-risk | OC/DC tendency mismatch under pressure |
| pass-protection-coherence-risk | OL breakdown → QB pressure → passing game downgrade |
| defense-motion-adjustment-coherence-risk | Pre-snap motion exploitation |
| route-timing-coherence-risk | WR separation quality vs coverage |
| qb-read-coverage-coherence-risk | QB processing vs shell complexity |
| drive-momentum-coherence-risk | Drive-level momentum shifts |
| player-workload-injury-coherence-risk | Workload → injury probability coupling |
| red-zone-playcall-coherence-risk | RZ efficiency divergence |
| fourth-down-decision-coherence-risk | Aggressiveness vs model expectation |
| nfl-rest-advantage-travel-spot (Karmane, CC-BY-4.0) | Rest/travel spot research sample |

**Posture:** Steal **methodology** — derive analogous features from nflverse PBP in CeminiDFS Python; do **not** add Hugging Face as runtime dependency. MIT license on ClarusC64 cards confirmed at ingest; Karmane requires CC-BY attribution if columns reused.

### CeminiDFS integration (P0 brief)

1. Audit each coherence dimension against existing `stage 2` projection features
2. Prototype 2–3 highest-variance signals (pass-protection + red-zone playcall first)
3. Backtest delta vs K125 nflverse-only baseline on 2024 slates
4. Document clean-room derivation in CeminiDFS ARCHITECTURE.md footnote

### Out of scope

- Importing HF parquet into prod pipeline without reproducible PBP derivation
- PM sports-bot repos from same eval batch

## Snippets

> "Advanced coherence risk markers fundamentally missing from the standard nflverse projection stage within CeminiDFS." [Source: links.docx URL 30]
