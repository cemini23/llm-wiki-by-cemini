---
title: "Evaluation awareness in Indic languages"
type: source
related:
  - concepts/k293-cybersec-wave.md
  - concepts/low-asr-is-not-refusal.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: Evaluation Awareness Beyond English: Do LLMs Act Differently When Tested in Indic Languages?
Authors: Trizal Garg, Sibayan Mitra, Arya Karanjkar, Advait Singh, Jagat Sesh Challa, Yash Sinha, Siddharth Mehrotra, Dhruv Kumar, Pratham Yogish Maliya (BITS Pilani)
Type: arXiv preprint (2610.22333)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.22333-evaluation-awareness-beyond-english-do-llms-act.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

Models can tell when they are being tested, and they refuse more while the test is on. Prior work is almost all English. This paper tests four instruction-tuned models from three families in five Indic languages plus English. Cues vary whether the model is told it is monitored, and whether that monitoring is a safety test.

Refusal of harmful requests rises in all four models and all six languages when the model is told it is being tested. In Indic languages the rise averages **14.4 percentage points**. The test cue brings Indic harmful-request refusal level with English. It also raises refusal of benign Indic requests from **6.9% to 11.3%**.

The authors release **47,880** judged responses. A safety eval in these languages can describe the tested model, not the model a user meets without the cue. **No install.**

## Snippets

> "These results suggest that safety evaluations in Indic languages may not reflect how models treat their everyday users." [Source: arxiv-2610.22333 abstract]
