---
title: "Ignored, Not Refused — low prompt-injection ASR in small tool agents"
type: source
related:
  - concepts/k293-cybersec-wave.md
  - concepts/low-asr-is-not-refusal.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents
Authors: Farhan Zarif, Kazi Shahid Ahmed Galib, Synthia Akter Promi, Shabnam Sharmin Tarin, Ariyan Hossain Sadif, Ahmed Farig Yousuf Sadeque (BRAC University)
Type: arXiv preprint (2610.23254)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.23254-ignored-not-refused-what-low-prompt-injection-su.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract and introduction)

## Narrative

Indirect prompt injection hides an instruction in content a tool-using agent must read. Benchmarks such as InjecAgent and AgentDojo score security by attack-success rate. A failed attack counts as a defense.

The authors audit **33,000** trajectories from eleven open-weight agents (2–14B) on those two benchmarks. A label-blind judge finds that most failed attacks are **ignored (76–80%)**, not **refused (17–18%)**. With the same weights, a system-prompt change moves InjecAgent ASR from **0.2% to 43%**. Their Attack–Task Outcome Matrix shows that in **21.7%** of AgentDojo episodes the agent stayed safe and did not complete the user's task.

A low ASR mostly means the agent skipped the injection. It does not mean the agent refused it, and it does not mean the user task succeeded. The paper says it releases a labeled corpus, a judge prompt, and analysis code. This page does not copy either. **No PoC.**

## Snippets

> "A low ASR therefore mostly reflects agents silently ignoring injections, not refusing them." [Source: arxiv-2610.23254 abstract]
