---
title: "ATTCK-R — Knowledge-Aware Long-Horizon Jailbreaking for Protected LLMs"
type: source
tags: [arxiv, red-team, jailbreak, evaluation, llm-security]
keywords: [jailbreak, multi-turn, protected systems, attack success rate, tactic curation, traceback]
related:
  - concepts/k291-cybersec-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-cybersec-wave.md — K291 cybersecurity wave hub

## Raw Concept

Title: ATTCK-R — Knowledge-Aware Long-Horizon Jailbreaking for Protected LLMs
Authors: Md Mushfiqur Rahman, Tobias Rohde, Rahul Tripathi, Khalil Elkhalil, Kevin Lybarger (George Mason University, Amazon)
Type: arXiv preprint (2610.16305)
Location: `research to be indexed/cybersec/arxiv-2610.16305-attck-r-knowledge-aware-long-horizon-jailbreakin.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The measurement finding is the headline.** Adding **one prompt-based safety protection** drops a strong multi-turn baseline's attack success rate from **0.896 to 0.608** — **32.1% relative**. Unprotected evaluations therefore **substantially overestimate** real-world vulnerability.

**The method (ATTCK-R)** treats jailbreaking as long-horizon trajectory optimisation against a **protected black-box** system:

- a structured **belief state** over the attack trajectory,
- **optimization-based tactic curation** abstracting reusable strategies from prior successes and failures,
- **informed traceback** that resumes from strategically meaningful states rather than restarting.

Evaluated across **9 LLMs** each behind a single prompt-based protection layer; ablations confirm long-horizon planning and tactic curation drive effectiveness, and adaptive traceback improves efficiency.

**Why it is filed here:** the wiki already treats an evaluation that scores a withheld response as unsound. This adds the complementary error — **an attack measure taken without the deployed protection measures attacks that do not exist in deployment.**

## Snippets

> "we show that the introduction of a prompt-based safety protection reduces the average attack success rate of a strong multi-turn baseline from 0.896 to 0.608 (32.1% relative), demonstrating that unprotected evaluations substantially overestimate real-world vulnerabilities." [Source: arxiv-2610.16305 p.1]

> "ATTCK-R models jailbreaking as a long-horizon trajectory optimization problem using a structured belief state." [Source: arxiv-2610.16305 p.1]

## Dead Ends

- Citing a jailbreak ASR without naming the protection layer. The same baseline moves 32% relative between protected and unprotected evaluation.
