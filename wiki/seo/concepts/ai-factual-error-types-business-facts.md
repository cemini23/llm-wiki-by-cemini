---
title: "AI factual error types — the three ways an engine gets a business fact wrong"
type: concept
tags: [concept, geo-aeo, verification, audit, local]
keywords: [misattribution, numerical deviation, detail invention, HALUCHECK, fact audit, opening hours, hallucination class]
related:
  - sources/arxiv-halucheck-hallucination-benchmark-2611.08231.md
  - concepts/canonical-business-facts-geo.md
  - concepts/citation-verification-aeo.md
  - concepts/llm-reputation-signals-geo.md
  - concepts/generative-engine-optimization.md
  - sources/arxiv-2611.14382-learning-by-thinking-cognitive-map-2026-11-11.md
  - concepts/external-anchoring-generative-content-geo.md
maturity: draft
created: 2026-11-10
updated: 2026-11-14
---

## Raw Concept

**The question this page answers.** When an AI engine states a wrong fact about a shop, what kind of wrong is it, and how do you name it in an audit?

**Sources that synthesize into this page.** One source at present: @sources/arxiv-halucheck-hallucination-benchmark-2611.08231.md. The error taxonomy comes from that paper. The mapping to business facts is an inference, and it is tagged [TENTATIVE].

## Narrative

### The taxonomy

HALUCHECK derives its error classes from observed model failures, then injects them into clean passages by controlled perturbation. Three patterns cover the static-text case. [Source: arxiv-2611.08231 p.3]

| Error class | What changed | Business-fact example |
|-------------|--------------|-----------------------|
| **Misattribution** | The wrong entity receives the claim | A service the shop does not offer is listed under its name. A competitor's award is credited to it. |
| **Numerical deviation** | A number, date or quantity shifts | Saturday hours become 18:00 in place of 16:00. A price becomes £15 in place of £25. |
| **Detail invention** | A detail that never existed is added | A second location appears. A staff member who does not exist is named. |

The paper reports the highest error rates on entity expressions, and it names **numbers and dates** first. Entities about people and artefacts also fail more often than average. [Source: arxiv-2611.08231 p.3]

### The second taxonomy: agent faults

For an agent that browses on the customer's behalf, the paper adds three classes. [Source: arxiv-2611.08231 p.2, p.5]

| Agent class | What goes wrong |
|-------------|-----------------|
| **Planning** | The agent picks a wrong sequence of steps. It books the cheapest fare before it checks refundability. |
| **Perception** | The agent misreads a correct tool result. A paid invoice is reported as unpaid. |
| **Tool use** | The agent calls a wrong tool, or passes wrong arguments. |

These matter for local search when a customer asks an assistant to book or check something, not only to read something.

### How good is the check?

Fourteen models were tested. The best detection accuracy is about **84%**. Most models score between **50% and 70%**. Localisation of the wrong span, and the correction itself, are much worse than detection. Thinking, web search and supervised fine-tuning each help a little. None of them solves the problem. [Source: arxiv-2611.08231 p.1-2, p.6]

### How to use it as an audit

1. Ask an engine five questions with a known answer: hours, price, address, service list, staff.
2. Mark each answer as correct, or assign one of the three classes above.
3. Fix the **source** that fed the error, not the answer. @concepts/canonical-business-facts-geo.md holds the sync procedure.
4. Re-probe across several runs. Answer variance is real, and a single probe is one draw.

### The honest limits

- One paper supports the taxonomy. The mapping to a service business is this wiki's inference, not the paper's finding. [TENTATIVE]
- A 50-70% detector cannot certify a fact. Manual checking stays necessary.
- The taxonomy names the error. It does not tell you which source caused it. That needs the citation trail, which @concepts/citation-verification-aeo.md covers.

## Snippets

> "LLMs exhibit relatively high hallucination rates in expressions related to entities, especially for numerical entities such as numbers and dates." [Source: arxiv-2611.08231 p.3]

> "Supervised fine-tuning helps models recognize specific patterns of hallucination but cannot generalize stably to out-of-distribution data." [Source: arxiv-2611.08231 p.2]

## Dead Ends

- **Using the detector as the audit.** Detection is a model judging a model. The audit needs a human-checked answer key plus the citation trail.
