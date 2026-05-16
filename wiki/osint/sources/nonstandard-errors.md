---
title: 'Nonstandard Errors in AI Agents'
type: source
tags: [pdf, llm-agents, k49]
keywords: [Nonstandard, Errors, AI agents, Claude Code, NYSE TAQ, market quality, researcher degrees of freedom, multiverse]
related:
  - concepts/llm-agent-systems.md
  - concepts/market-microstructure.md
clusters: [llm-agents]
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent systems in the Cemini corpus

## Raw Concept

- **Original title**: Nonstandard Errors in AI Agents
- **Author(s)**: Ruijiang Gao, Steven Chong Xiao (Naveen Jindal School of Management, University of Texas at Dallas)
- **Type**: PDF (arXiv 2603.16744)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/nonstandard errors.pdf
- **Retrieved**: 2026-04-27
- **Length**: 45p
- **Read status**: deep-read
- **Cluster**: llm-agents

## Narrative

Gao & Xiao ask whether state-of-the-art AI coding agents, given identical data and an identical research question, produce identical empirical results. They replicate the Menkveld et al. (2024) "nonstandard errors" (NSE) design — which showed 164 human research teams analyzing the same market-microstructure data produced estimates with an interquartile range comparable to a single estimate's standard error — but substitute 150 autonomous Claude Code agents (100 Sonnet 4.6, 50 Opus 4.6). Each agent independently tests six hypotheses about market-quality trends in NYSE TAQ millisecond data for SPY (2015–2024), exploring the data, writing code, and producing a full 2,000–4,000-word research report with no human intervention.

Key findings: AI agents exhibit sizable NSEs. For market efficiency (H1) the IQR of effect-size estimates is 2.43%/yr; for trading volume (H4) it is 10.69%/yr, driven entirely by agents picking dollar volume (~+6%/yr) vs. share volume (~−5%/yr); for price impact (H6) it is 10.34%/yr. The *structure* of AI NSE is distinctive: all 150 agents choose linear-time-trend regression as the estimation paradigm, so dispersion is concentrated almost entirely in measure-choice forks, not estimation-paradigm forks — the relative-change specification that drives human dispersion is entirely absent. Model families show stable "empirical styles" (Sonnet prefers autocorrelation 87%, Opus universally chooses variance ratio). In a three-stage protocol, AI peer review barely moves dispersion, but exposure to five top-rated exemplar papers collapses the IQR by 80–99% within converging measure families — convergence by imitation, not understanding (62 of 87 autocorrelation agents migrate to variance ratio).

**Cemini relevance**: directly relevant — it quantifies the reliability of LLM agents doing autonomous *financial empirical research*, bearing squarely on Cemini's LLM-automation roadmap and eval discipline; "convergence reflects imitation rather than understanding" is a concrete caution for any automated-research pipeline.

## Snippets

> "Deploying 150 autonomous Claude Code agents to independently test six hypotheses about market quality trends in NYSE TAQ data for SPY (2015–2024), we find that AI agents exhibit sizable nonstandard errors (NSEs), that is, uncertainty from agent-to-agent variation in analytical choices, analogous to those documented among human researchers." [Source: nonstandard errors.pdf p.1]

> "AI peer review has no effect on reducing dispersion: the IQR is essentially unchanged from S1 to S2. In contrast, exposure to top papers triggers dramatic convergence. For converging measure families, the IQR collapses by 80–99% from S1 to S3." [Source: nonstandard errors.pdf p.3]

> "Different model families exhibit stable 'empirical styles.' Sonnet 4.6 agents overwhelmingly prefer autocorrelation measures for market efficiency (87%) ... Opus 4.6 agents universally choose variance ratio measures (100%)." [Source: nonstandard errors.pdf p.4]
