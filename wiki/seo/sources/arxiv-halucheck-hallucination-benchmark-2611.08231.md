---
title: "HALUCHECK — the error classes an AI makes about a fact"
type: source
tags: [source, arxiv, hallucination, verification, geo-aeo, benchmark]
keywords: [HALUCHECK, hallucination detection, numerical deviation, misattribution, detail invention, span localisation, agent hallucination]
related:
  - concepts/ai-factual-error-types-business-facts.md
  - concepts/citation-verification-aeo.md
  - concepts/canonical-business-facts-geo.md
maturity: draft
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional Hallucinations? |
| Author | Hanyu Qiu, Ze Liu, Zhe Zhao, Kuang Xiong, Blaze Chen, Zhenxiang Yan, Renfen Hu (Beijing Normal University; Tencent AI Lab) |
| Type | arXiv preprint (cs.CL), benchmark |
| arXiv | 2611.08231v1, 5 Nov 2026 |
| Location | `research to be indexed/seo/arxiv-2611.08231-from-twisted-facts-to-rogue-agents-can-llms-reli.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.08231-from-twisted-facts-to-rogue-agents-can-llms-reli.pdf` |
| Pages | 22 |
| Read status | read (abstract, taxonomy, dataset tables, results) |

## Narrative

**The question.** Can a large language model detect a hallucination in its own output or in another model's output? The authors build a benchmark for the check that happens **after** generation.

**The benchmark.** HALUCHECK holds **42,980** annotated pairs in English and Chinese. Each instance supports four tasks: detection, span localisation, correction, and root-turn tracing in an agent trajectory. [Source: arxiv-2611.08231 p.1, Table 2]

**Two halves.** *HaluText* covers factual errors in static text. *HaluAgent* covers faithfulness errors in multi-turn agent behaviour, split into **planning**, **perception** and **tool-use** errors. [Source: arxiv-2611.08231 p.1-2]

**The three perturbation patterns.** The authors derive these from observed model errors, then inject them into Wikipedia passages and QA pairs. [Source: arxiv-2611.08231 p.3]

| Pattern | What it changes | Example |
|---------|-----------------|---------|
| Misattribution | The wrong entity gets the credit or the blame | A prize credited to Physics instead of Chemistry |
| Numerical deviation | A number, date or quantity shifts | 1957 becomes 1957-09-24 or 2020 becomes 2021 |
| Detail invention | A detail that never existed | A fabricated element name, "curionium" |

**Where the errors concentrate.** The paper reports high hallucination rates on **entity expressions**, and it singles out **numerical entities such as numbers and dates**. Entities about humans and artefacts also fail more often. [Source: arxiv-2611.08231 p.3]

**Reported results.** Fourteen models across six families were tested. The best detection accuracy is about **84%** (Gemini3.1-Pro). Most other models score between **50% and 70%**. Span localisation and correction are substantially worse than detection for almost every model. Agent hallucination is the hardest case, because most models fail at context integration and root-turn tracking. [Source: arxiv-2611.08231 p.6]

**What does not fix it.** Explicit thinking helps partly. Web search helps partly. Supervised fine-tuning teaches specific patterns but does not generalise out of distribution. The authors conclude that hallucination detection remains unsolved. [Source: arxiv-2611.08231 p.1-2]

### What this means for GEO

The three patterns are the exact error classes that a local business cares about. A wrong opening hour is a numerical deviation. A wrong service attributed to the shop is a misattribution. A service the shop never offered is detail invention. The benchmark gives an audit rubric: probe the answer, name the error class, then correct the source that fed it.

The weak point for practice is that the best model still misses about one error in six, and localisation is worse. A manual check stays necessary.

## Snippets

> "Models show basic sample-level detection ability, they struggle with fine-grained localization, correction, and agent hallucination detection." [Source: arxiv-2611.08231 p.1]

> "Explicit thinking and access to external knowledge can partially improve detection but are still limited by the models' inherent capabilities." [Source: arxiv-2611.08231 p.2]

> "LLMs exhibit relatively high hallucination rates in expressions related to entities, especially for numerical entities such as numbers and dates." [Source: arxiv-2611.08231 p.3]

## Dead Ends

- **Using the detector as the verifier.** The paper measures the detector against a known label. In production there is no label, so a 50-70% detector cannot certify a fact.
