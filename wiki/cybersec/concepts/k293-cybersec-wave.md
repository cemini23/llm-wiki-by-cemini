---
title: K293 cybersec wave — low ASR is not a refusal (Oct 2026)
type: concept
related:
  - sources/arxiv-2610-23254-ignored-not-refused.md
  - sources/arxiv-2610-23071-tool-admission-before-retrieval.md
  - sources/arxiv-2610-23093-slip-interlingual-tool-safety.md
  - sources/arxiv-2610-26595-jailbreak-asr-evaluator-sensitivity.md
  - sources/arxiv-2610-22068-safe-pro-cross-modal.md
  - sources/arxiv-2610-26474-afriguard.md
  - sources/arxiv-2610-22333-eval-awareness-indic.md
  - concepts/low-asr-is-not-refusal.md
maturity: draft
updated: 2026-10-20
---

## Raw Concept

Cybersec K293, 2026-10-20. Seven papers that the digest dropped into osint, seo, or game-dev inboxes. They are safety evaluations. No install. No PoC. No payloads in the wiki.

## Narrative

The wave has one rule. **A low attack-success rate is not evidence of a defense.**

@concepts/low-asr-is-not-refusal.md collects three measurements:

- Failed prompt injections are mostly **ignored** (76–80%), not refused (17–18%). The same weights move InjecAgent ASR from **0.2% to 43%** when only the system prompt changes. @sources/arxiv-2610-23254-ignored-not-refused.md
- Keyword ASR on low-resource jailbreaks is **96.0%**. A Qwen3 StrongREJECT judge scores **2.7%**. One hundred samples at temperature 0.8 score **100%** versus **50%**. @sources/arxiv-2610-26595-jailbreak-asr-evaluator-sensitivity.md
- Telling a model it is being tested raises harmful-request refusal by **14.4** points in Indic languages, and also lifts benign refusal from **6.9% to 11.3%**. @sources/arxiv-2610-22333-eval-awareness-indic.md

Two papers from the same group split the tool decision from the answer. After a harmful request is admitted, the unweighted harm rate is **74.5%** across seven open models, and a written refusal still accompanies **33.6%** of those calls. @sources/arxiv-2610-23071-tool-admission-before-retrieval.md Non-English harmful requests raise tool admission from **46.9% to 67.4%**. @sources/arxiv-2610-23093-slip-interlingual-tool-safety.md

AfriGuard finds guard models under 60% F1 on African-language safety labels, and many "refusals" are unusable text rather than a refusal. @sources/arxiv-2610-26474-afriguard.md SAFE-PRO is a cross-modal ask-or-optimise framework. The skim did not take a headline accuracy. @sources/arxiv-2610-22068-safe-pro-cross-modal.md

The options-agent measurement lives in osint: @osint-wiki/sources/arxiv-options-agent-safeguards-2610.24289-2026-10-20.md. It is the same shape. Text in, order out, no check at the boundary.
