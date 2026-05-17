---
title: "Do Large Language Models Know What They Don't Know? Evaluating Epistemic Calibration via Prediction Markets"
type: source
tags: [pdf, k49, llm-agents, prediction-markets]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
  - concepts/prediction-market-historical-analysis.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus
- @concepts/prediction-market-historical-analysis.md — KalshiBench draws its 300 questions from Kalshi prediction markets

## Raw Concept

- **Original title**: Do Large Language Models Know What They Don't Know? Evaluating Epistemic Calibration via Prediction Markets
- **Author(s)**: Lukas Nel (Lotus AI). arXiv:2512.06030v1, Dec 2025.
- **Type**: PDF
- **Location**: research for cemini/kalshi 5 3:29.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 13p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, prediction-markets

## Narrative

This paper evaluates the **epistemic calibration** of frontier LLMs — whether a model claiming 80% confidence is actually correct 80% of the time. It introduces **KalshiBench**, a benchmark of **300 prediction-market questions from Kalshi** (a CFTC-regulated exchange) spanning 13 categories, all with verifiable real-world outcomes resolving *after* model training cutoffs. This temporal filtering closes two flaws in traditional benchmarks: **static-knowledge contamination** (a model can look calibrated by memorizing facts) and **lack of verifiable ground truth**.

Five frontier models are evaluated — Claude Opus 4.5, GPT-5.2, DeepSeek-V3.2, Qwen3-235B, Kimi-K2 — on accuracy/F1 and calibration (Brier score, ECE, reliability diagrams). Findings: **all models are systematically overconfident**. Accuracy varies modestly (64–69%) but Expected Calibration Error varies ~3× — best is Claude Opus 4.5 at ECE=0.120, while the reasoning-enhanced GPT-5.2-XHigh is *worst* at ECE=0.395 despite comparable accuracy. Models average a **27% error rate even when expressing >90% confidence**. **Only one model achieves a positive Brier Skill Score**, meaning most models forecast worse than simply predicting base rates. The headline conclusion: scaling and enhanced reasoning do **not** automatically confer calibration; epistemic calibration is a distinct capability needing targeted development.

**Cemini relevance**: directly relevant on two axes — (1) it benchmarks LLMs on **Kalshi prediction markets**, the exact instrument class CeminiSuite trades, and (2) it warns that any LLM feeding probability estimates into a trading or forecasting pipeline is likely overconfident and should be treated as needing post-hoc recalibration before its confidence is acted on.

## Snippets

> "We introduce KalshiBench, a benchmark of 300 prediction market questions from Kalshi, a CFTC-regulated exchange, with verifiable real-world outcomes occurring after model training cutoffs ... we find systematic overconfidence across all models." [Source: kalshi 5 3:29.pdf p.1]

> "Even the best-calibrated model (Claude Opus 4.5, ECE=0.120) shows substantial calibration errors, while reasoning-enhanced models like GPT-5.2-XHigh exhibit worse calibration (ECE=0.395) despite comparable accuracy. Critically, only one model achieves a positive Brier Skill Score, indicating most models perform worse than simply predicting base rates." [Source: kalshi 5 3:29.pdf p.1]
