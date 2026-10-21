---
title: Low ASR is not a refusal
type: concept
related:
  - concepts/k293-cybersec-wave.md
  - sources/arxiv-2610-23254-ignored-not-refused.md
  - sources/arxiv-2610-26595-jailbreak-asr-evaluator-sensitivity.md
  - sources/arxiv-2610-22333-eval-awareness-indic.md
maturity: draft
updated: 2026-10-20
---

## Raw Concept

What this page answers: what does a low attack-success rate actually mean? From three K293 papers on prompt injection, jailbreak scoring, and evaluation awareness.

## Narrative

Attack-success rate (ASR) counts the share of attacks that reach the attacker's goal. Every other outcome is scored as a defense. That bin mixes three different events.

| Event | What the papers show |
|---|---|
| Ignored | 76–80% of failed injections on 2–14B tool agents. The attack did not land, and the model did not refuse it. |
| Refused | 17–18% of those same failed attacks. |
| Task dropped | 21.7% of AgentDojo episodes stayed safe and did not finish the user's task. |
| Judge swap | Low-resource jailbreaks score 96.0% by keywords and 2.7% by a StrongREJECT judge. |
| Repeat sampling | 100 draws at temperature 0.8 score 100% by keywords and 50% by the judge. An initial refusal is not exclusion. |
| Test cue | Telling the model it is under test raises harmful refusal by 14.4 points in Indic languages. Benign refusal rises too, from 6.9% to 11.3%. |
| Prompt, same weights | InjecAgent ASR moves from 0.2% to 43%. |

Report how the attack failed, whether the user task completed, which judge scored the output, how many samples were drawn, and whether the model was told it was being tested. Do not cite a bare ASR.

This matches the K291 ATTCK-R finding that an unprotected eval overstates vulnerability. The protection layer, the judge, and the language are part of the number.
