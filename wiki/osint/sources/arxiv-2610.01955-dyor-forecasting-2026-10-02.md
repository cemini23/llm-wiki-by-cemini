---
title: "Do Your Own Research: learning to forecast by learning to search (2610.01955)"
type: source
tags: [source, k278, prediction-markets, agents, forecasting]
keywords: [k278, polymarket, grpo, brier, no-clone]
related:
  - concepts/k278-gambling-pm-wave.md
maturity: draft
created: 2026-10-02
updated: 2026-10-02
read_status: skimmed
---

## Relations

- @concepts/k278-gambling-pm-wave.md

## Raw Concept

| File | `arxiv-2610.01955-do-your-own-research-learning-to-forecast-by-lea.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.01955-do-your-own-research-learning-to-forecast-by-lea.pdf` |
| Archive | egress-fi 2026-10-02 |
| Retrieved | 2026-10-02 |
| sha256 | `b12f46d7b17d556238d28e960e0efa4c64da2db620ff729ac9a2a8e87429bd77` |
| Dual-ID | **OSINT K278** |
| arXiv | 2610.01955 |
| Authors | Yusuf Afifi, Artur Kiulian, Anton Polishko, Mykola Khandoga, Hamudi Naanaa, Alina Krasnobrizha (Future Principle) |
| Repo | `https://github.com/afifi-yusuf/prime-forecast` |

## Narrative

The paper folds research into the training loop. Earlier forecasting work froze the research context before training. This one trains a search-and-forecast scaffold end to end, so context acquisition is shaped by reward.

The environment, dataset, and harness come from **2,100+ resolved Polymarket questions**. The agent may search the web, read URLs, and read financial time series. Three leak filters restrict it: a domain blocklist, a heuristic date filter, and a per-result keep-or-drop judge. Training used GRPO over a single epoch with LoRA on a 35B model with 3B active parameters, under a Brier-score reward.

The headline result, over 265 held-out questions: a soft-Brier of **0.254**, against **0.256** for a frontier model. The margin over the frontier models tested ran 0.019 to 0.032. **Cost was about 5% of the frontier path: $0.011 against $0.24 per question.** Calibration error fell from 0.185 to 0.128, a 31% cut. Coverage rose from 79% to about 100%. Search attempts fell from 3.8 to 2.25 per rollout. On the uncertain subset of 104 questions, the margin widened to 0.007.

The authors admit the scope. The test is binary prediction markets only, on a modest sample. The Qwen evaluation used the training platform's own serving stack, while frontier models went through an API proxy. They also state plainly that no scaffold reliably beats the market without non-public information, which is why they withhold the market price.

Read that last point carefully. **A calibrated forecaster is not an edge.** The paper is a search-and-calibration result, not a trading result. The leak filters exist because the task is easy to win by cheating.

Result for the PM lane: the useful patterns are the three-layer leak filter and the Brier-score training signal. Both are reusable. Neither is a trade.

Repo license not yet verified by `gh api`. No clone. **No level to arm. No pm scp. Never auto-arm.**
