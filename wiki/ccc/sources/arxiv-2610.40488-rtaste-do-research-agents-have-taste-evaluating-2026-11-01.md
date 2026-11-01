---
title: "RTaste: Do research agents have taste?"
type: source
tags: [source, arxiv, research-agents, experiment-judgment]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | RTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment |
| Authors | Art Kanke, University of Minnesota |
| arXiv | 2610.40488 |
| File | `arxiv-2610.40488-rtaste-do-research-agents-have-taste-evaluating.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.40488 |
| Read status | skimmed (abstract + intro) |

## Narrative

The paper asks whether research agents have taste. Taste is the judgment of which experiments are worth running before their outcomes are known. The introduction says agents already search the literature, implement work, run experiments, and write reports. It cites a METR risk assessment of agents inside four frontier labs. That assessment found no evidence that those labs relied on agents to set research agendas or make budget decisions. The paper treats that step as taste.

The study gives six frontier models seven recent NLP papers. Each model works as a research agent alone or as a team. The introduction says each model receives a seed paper with its text, figures, and code. It works once as a single researcher and once as a research team. It proposes five minimum viable experiments (MVEs). The abstract says the agent forecasts whether each MVE will pass a threshold it sets, and then ranks the MVEs. A separate executor attempts every MVE, including those ranked last. Three model auditors judge the results. The introduction names three stages: propose and register, forecast and rank, and run and assess.

Of 415 MVEs, 194 are judged sound, valuable and new. Fewer than half of these (73) are also judged beyond the seed paper and non obvious. These counts are single-source claims from this paper.

The agents' first choices match the auditors' most valued experiment more often than a random pick. Those first choices are not shown to improve on choosing the experiment written first. Forecasts beat a base rate. Forecasts are not measurably more accurate than those of a fresh instance of the same model given only the paper and registrations. Teams cost more without a clear overall improvement in proposal quality. These comparisons are single-source claims from this paper.

The paper says the agents produce many worthwhile experiments. It also says the evidence that their rankings improve the choice of which experiment to run remains limited. For a practitioner who builds agent harnesses, the released artifact is the evaluation harness and a dataset of all 415 MVEs, with forecasts and audited outcomes, at https://github.com/ArtKanke/rTaste. The harness runs the last-ranked MVEs as well as the first choices, and the auditors score the executed results.

## Snippets

> "Of 415 MVEs, 194 are judged sound, valuable and new, but fewer than half of these (73) are also judged beyond the seed paper and non obvious. The agents’ first choices match the auditors’ most valued experiment more often than a random pick, but are not shown to improve on choosing the experiment written first." [Source: `arxiv-2610.40488-rtaste-do-research-agents-have-taste-evaluating.pdf` p.1 (arXiv 2610.40488), retrieved 2026-11-01]
