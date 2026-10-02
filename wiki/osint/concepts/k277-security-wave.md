---
title: K277 Security Wave (Oct 2026)
type: concept
tags: [security, safety, k277, agents]
keywords: [k277, codemimicry, pagebreak, numbat, no-poc]
related:
  - concepts/k278-security-wave.md
  - concepts/k276-ood-stub-wave.md
  - sources/arxiv-2609.39902-codemimicry-2026-10-01.md
  - sources/newsletter-rss-tldrsec-2026-10-01-tldr-sec-348---googles-pagebreak-scanner-perplex.md
  - sources/newsletter-rss-latent-space-2026-10-01-ainews-gemini-4-argon-gdms-answer-to-astrafable.md
maturity: draft
created: 2026-10-01
updated: 2026-10-02
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k278-security-wave.md
- @concepts/k276-ood-stub-wave.md
- @sources/arxiv-2609.39902-codemimicry-2026-10-01.md
- @sources/newsletter-rss-tldrsec-2026-10-01-tldr-sec-348---googles-pagebreak-scanner-perplex.md
- @sources/newsletter-rss-latent-space-2026-10-01-ainews-gemini-4-argon-gdms-answer-to-astrafable.md

## Raw Concept

K277 cluster hub. Dual-ID **OSINT K277**.

## Narrative

One threat-class paper and one tooling newsletter. Threat class and mitigation table only. **No PoC.**

| Source | Contribution | Posture |
|--------|--------------|---------|
| 2609.39902 CodeMimicry | Safety training does not carry into the code domain | Threat class. No recipe |
| tl;dr sec #348 | PageBreak confirms bugs deterministically; Numbat blocks risky agent actions | Defensive names |

Two findings:

1. **Prompt-level defence does not cover the code domain.** CodeMimicry reports that a harmful request wrapped in valid code dodges refusal, at about 96% success across eight commercial models. Their own mitigation table is the useful part: prompt filters left 76% to 100% residual success, Representation Bending 38%, Circuit Breaker 8%, and SelfDefend 4% to 14%. Stripping comments also helped, because the method uses comments and docstrings as a side channel. The lesson for our own harness: prompt-level guards are not sufficient for code-carrying inputs.
2. **Confirm, then report.** Google's PageBreak agent validates a suspected bug against a running environment before reporting. That is the third appearance of this rule this week, after the K276 trace paper and the Klement summary item. Reported near-zero false positives and 500+ bugs since November 2025.

Numbat, from Perplexity, is an open-source suite that hooks into coding harnesses and blocks risky agent actions, with 52 built-in rules. Name only. Do not install from this note.

One item sits here from the model-release digest: a reported hidden-reasoning extraction campaign that one vendor attributes to individuals linked to another lab. Headline only.

**Cemini posture:** FILE. Defensive description only. **No PoC. No exploit steps. No address list.** **0 product Integrate GO.**
