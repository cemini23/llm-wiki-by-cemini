---
title: "Curbside chatbots — auditing the mental-health advice LLMs give"
type: source
tags: [source, arxiv, llm-safety, mental-health, audit]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Curbside Chatbots: Auditing the Mental Health Interventions Large Language Models Recommend to Clinicians, Caregivers, and Patients |
| Authors | Matthew Flathers, Jill Noorily, Phuong Anh Nguyen, and others (Beth Israel Deaconess Medical Center; Pontificia Universidad Javeriana; and others) |
| arXiv | 2611.12814 |
| Pages | 100 |
| Read status | skimmed (abstract) |

## Narrative

An audit of the **mental-health interventions** LLMs recommend, evaluated separately for three audiences: **clinicians, caregivers, and patients**.

That three-way split is the design decision. The same suggestion is appropriate coming from a clinician, risky from a caregiver, and dangerous from a patient — and most evaluations of medical LLM advice collapse the audiences into one.

The "curbside" framing is clinical shorthand for an informal consult: the advice you give a colleague in a corridor, which is different from a formal recommendation. An LLM asked a casual question is being used that way, and the paper evaluates it against that standard rather than against a textbook.

### Why it is filed here

Not for the clinical domain. It is the clearest example in this batch of an evaluation that **conditions on who is asking**, which is the axis almost every agent evaluation ignores — including this workspace's own. A tool that is fine for an operator is not fine for a customer.

The 100-page length and the author list — a digital-psychiatry division at a teaching hospital — also make it a reference for how to structure a safety audit with clinical input rather than model benchmarks alone.

**Caveat.** Abstract only. No finding, rate, or recommendation is reproduced.

## Snippets

> "Curbside Chatbots: Auditing the Mental Health Interventions Large Language Models Recommend to Clinicians, Caregivers, and Patients." [Source: arxiv-2611.12814 p.1]

## Dead Ends

- **Citing an audit finding.** Abstract only.
