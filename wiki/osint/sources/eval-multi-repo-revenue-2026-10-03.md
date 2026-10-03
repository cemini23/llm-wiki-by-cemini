---
title: "Multi-Repository Revenue Stack Evaluation — 20 rows (2026-10-03)"
type: source
tags: [source, k279, eval, dfs, parlays, tooling]
keywords: [k279, eval-docx, breakeven, pickem, technique-extract]
related:
  - concepts/k279-dfs-parlays-wave.md
  - concepts/k279-ood-stub-wave.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: skimmed
---

## Relations

- @concepts/k279-dfs-parlays-wave.md
- @concepts/k279-ood-stub-wave.md

## Raw Concept

| File | `Multi-Repository Revenue Stack Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Repository Revenue Stack Evaluation.docx` |
| Archive | egress-fi 2026-10-03 |
| Retrieved | 2026-10-03 |
| Dual-ID | **OSINT K279** |
| sha256 | `67661229a2794e865f4367f6003f1ca9c7a99e0bdca6201a8c5c54a9a4e33649` |
| Batch theme | AppSec payloads, mobile QA diagnostics, DFS and sports prop modelling, search benchmarks, agent prototypes |

## Narrative

Twenty rows. The operator directive for this wave: **stop auditing licenses; extract the technique.** What follows is what is actually usable, ranked by usefulness to the live projects.

### The one row worth acting on — pick'em breakeven structure

**`925Sports/mlb-prop-optimizer`** — tier Extract, primary fit **CeminiParlays**, overlap 0.80.

The technique: **formalise implied-probability breakeven thresholds across 2-pick through 6-pick multiplier cards, against sharp market lines.**

Why it matters. CeminiParlays already ranks operator-typed tickets against displayed American odds. The pick'em profile is the weaker half, because a fixed-multiplier card is not a price — it is a payout structure. To compare a 3-pick flex card against a sharp two-way line you need the breakeven hit rate for that card's multiplier and flex rules, not a de-vigged probability.

The concrete work:

| Card size | What you need |
|-----------|---------------|
| 2-pick | Breakeven hit rate per multiplier |
| 3-pick to 6-pick | Breakeven per size, per flex variant |
| Flex vs power play | Different settlement rules, so different breakevens |

The repo is small and the docx could not confirm its contents. **The technique is the value, not the code.** Deriving the breakeven table is arithmetic: for a fixed multiplier `m`, the breakeven probability is `1/m`. The work is building the table for each card size, each flex variant, and each platform's settlement rule, then wiring it as the pick'em scoring profile.

Unresolved and flagged in the docx: the specific breakeven weights used for Underdog flex slips versus standard power plays.

### The DFS rows — mostly noise

| Repo | Verdict | Why |
|------|---------|-----|
| `drgregmscott-tech/DFS_Optimizer` | Context | Linear-programming lineup construction. CeminiDFS already runs Phases 0-5 with multi-lineup generation, correlation stacking, and late swap. A second LP solver adds regression risk, not edge |
| `arthuro1234/London-Tube-AI-Search-DFS-BFS-UCS-Heuristics` | Pass | "DFS" here is depth-first search. It is a graph-traversal exercise. Irrelevant |
| `nukesim/nuke-dfs-hub` | Context | Name only |
| `uppprob-afk/fantasy-nfl-assistant` | Context | Standard projection tables. The nflverse pipeline already covers this |
| `kenyamojaq/score-prediction` | Pass | Basic regression. **Would degrade rigour** — it cannot beat a market-implied closing line, and it has no correlation structure |
| `Melvin-code-ux/Melvin-Football-Predictor` | Pass | Introductory script |
| `YangRuhao/football-analysis-platform` | Context | Soccer video tracking. Different sport, high compute, no alignment |

**Read the Pass rows as informative.** Two of them are Pass for the same reason: a naive score-regression model loses to the closing line. That is a standing argument for keeping CeminiParlays on de-vigged market lines rather than internal score models.

### The AppSec row

**`sh377c0d3/AppSec-Payloads`** — 9,501 stars, tier Extract, routes to the cybersecurity wiki. A curated injection dictionary set. Handled on the K279 security page; nothing here for the trading stack.

### Not adopted

Nothing from this docx is vendored. The pick'em breakeven table is derivable arithmetic, so there is no code to take.

**Cemini posture:** FILE. Zero clones. No install. **No automated board scraping. The operator types the displayed lines.**
