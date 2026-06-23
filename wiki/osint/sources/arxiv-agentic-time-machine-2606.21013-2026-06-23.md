---
title: "Agentic Time Machine — future-event forecasting eval infrastructure (arXiv 2606.21013)"
type: source
tags: [source, arxiv, prediction-markets, polymarket, forecasting, multi-agent, k127]
keywords: [2606.21013, Agentic Time Machine, FutureX, Polymarket, planner-solver-aggregator, answer leakage, offline replay]
related:
  - concepts/agentic-time-machine-forecasting-eval.md
  - concepts/polymarket-bot-architecture.md
  - concepts/prediction-market-information-leakage-score.md
  - concepts/sports-prediction-consensus-agent.md
  - concepts/llm-agent-systems.md
  - sources/cemini-tool-evaluation-plan-62url-2026-06-23.md
  - sources/arxiv-garip-self-play-2606.22688-2026-06-23.md
  - sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md
maturity: draft
read_status: read
created: 2026-06-23
updated: 2026-06-23
clusters: [llm-agents, prediction-markets]
---

## Relations

- @concepts/agentic-time-machine-forecasting-eval.md — K127 synthesis
- @concepts/polymarket-bot-architecture.md — PM retail bot eval steal
- @concepts/prediction-market-information-leakage-score.md — leakage-control sibling framing

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agentic Time Machine as an Infrastructure for Future-Event Forecasting |
| **Authors** | Jingyi Chai, Bingyang Zheng, Xiangrui Liu, et al. (Shanghai Jiao Tong University) |
| **arXiv** | 2606.21013 (19 Jun 2026) |
| **sha256** | `fcc07e41d2a1c19540d180409452e212cb4dbb88520560a5db602312548982ef` |
| **Repo** | none public at ingest |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.21013-2606-21013v1-agentic-time-machine-as-an-infrastr.pdf` |
| **Retrieved** | 2026-06-23 (inbox) |
| **Read status** | read (abstract + §1–2 + Polymarket results table) |

## Narrative

Addresses the **Live vs Frozen** forecasting eval trade-off: live benchmarks (FutureX, Prophet Arena, ForecastBench) have dynamic web access but slow feedback; frozen replays are fast but static and unrealistic.

**Agentic Time Machine (TM):** LLM-based infrastructure that **filters post-cutoff / answer-revealing web content** during tool use, approximating the open web at a historical prediction timestamp — fast feedback + dynamic access without answer leakage.

**Planner-solver-aggregator MAS:** decompose each question into analytical angles → parallel evidence gathering → aggregate into single forecast. No training; same tools as single-agent baseline.

**Empirical claims [TENTATIVE — paper claims]:**

- TM substantially lowers scores vs unfiltered replay (leakage reduction works)
- Offline TM scores **correlate strongly** with live FutureX leaderboard performance
- Best on FutureX-Past + **Polymarket** subsets under TM vs closed-book, tool-augmented, and self-consistency baselines
- Live: FutureGPTv1 ranked #1 on FutureX eight-week overall leaderboard as of 2026-06-17

**Cemini posture:** **REFERENCE / steal-from** — PM/Kalshi bot offline eval harness pattern (temporal web filter + multi-angle decomposition). No public code → Phase-0 REFERENCE only. Pairs with `@concepts/prediction-market-information-leakage-score.md`.

## Snippets

> "By actively filtering post-cutoff or answer-revealing content from web tools, TM effectively simulates the open web as it stood at any chosen historical prediction point, preventing answer leakage during retrospective replay." [Source: arXiv:2606.21013 §1 (retrieved 2026-06-23)]

> "Offline scores achieved under the Time Machine correlate strongly with live leaderboard performance, establishing our infrastructure as a reliable proxy for real-world prediction testing." [Source: arXiv:2606.21013 abstract (retrieved 2026-06-23)]

> Polymarket subset under TM: multi-agent GPT-5.4 variant **65.0** vs best single-agent tool baseline **62.3** [Source: arXiv:2606.21013 Figure 1 (retrieved 2026-06-23)]

## Dead Ends

- FutureX / Polymarket leaderboard numbers are time-stamped — re-verify before citing in prod briefs.
- TM infrastructure ≠ Cemini CLOB executor — eval layer only, not order routing.
