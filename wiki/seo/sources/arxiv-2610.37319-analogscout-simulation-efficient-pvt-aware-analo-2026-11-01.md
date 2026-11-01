---
title: "AnalogScout: simulation-efficient PVT-aware analog sizing with LLM agents"
type: source
tags: [source, arxiv, analog-sizing, llm-agents, pvt]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AnalogScout: Simulation-Efficient PVT-Aware Analog Sizing with LLM Agents |
| Authors | Yichen Long et al., College of Integrated Circuits and Micro-Nano Electronics, Fudan University |
| arXiv | 2610.37319 |
| File | `arxiv-2610.37319-analogscout-simulation-efficient-pvt-aware-analo.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.37319 |
| Read status | skimmed (abstract + intro) |

## Narrative

Analog device sizing must meet every specification at every process, voltage, and temperature (PVT) corner. A multi-corner SPICE run of each candidate dominates the sizing time and slows design iteration. Surrogate-based optimizers search the sizing space directly. Recent large language model (LLM) agents add circuit knowledge and still delegate the device sizes to a global optimizer. Both learn the circuit response from repeated multi-corner SPICE simulations. That search becomes expensive under a limited simulation budget.

The authors propose AnalogScout, a simulation-efficient PVT-aware sizing framework driven by an LLM agent. The framework combines elite-design reuse, analytic gm/Id local sizing, and global refinement under full-corner verification. The introduction says current agents re-submit identical designs, restart instead of refining a verified design, and lose most of the budget to simulation-driven local optimizers. The authors claim that reusable verified designs and analytic sub-block sizing can save most of that budget.

On three SKY130 OTAs of increasing complexity, the abstract claims AnalogScout reduces power by 43.3% relative to the evolution strategy CMA-ES at an equal budget of 16k simulations. It claims AnalogScout reaches the final CMA-ES power after 7.0% of that budget. It also claims lower power than Bayesian optimization on all three OTAs, and lower power than two re-implemented LLM-driven flows on the two OTAs where those flows were tested. Each of these figures is a single-source claim from this abstract.

The subject is analog chip sizing. The text does not mention local search, listings, or campaigns. A local-SEO and digital-marketing practitioner who runs LLM agents can still read the budget claim as the authors state it. They say an agent spends its budget on better designs when it reuses verified designs, sizes sub-blocks analytically, and verifies the result at every corner.

## Snippets

> "Combining elite-design reuse, analytic gm/Id local sizing and global refinement under full-corner verification, AnalogScout reduces power by 43.3% relative to the evolution strategy CMA-ES at an equal budget of 16k simulations on three SKY130 OTAs of increasing complexity, and reaches the final CMA-ES power after 7.0% of that budget. It also attains lower power than Bayesian optimization on all three OTAs and than two re-implemented LLM-driven flows on the two OTAs where they were tested." [Source: `arxiv-2610.37319-analogscout-simulation-efficient-pvt-aware-analo.pdf` p.1 (arXiv 2610.37319), retrieved 2026-11-01]
