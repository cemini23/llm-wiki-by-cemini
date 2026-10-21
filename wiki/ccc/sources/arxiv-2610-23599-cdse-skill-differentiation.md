---
title: "CDSE — four-part skills from trajectories"
type: source
related:
  - concepts/k293-ccc-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents
Authors: Yewei Zhao, Derong Xu, Wei Chen, Yin Xu, Peilun Zhou, Xiaohan Wang, Guojun Yin, Wei Lin, Mingjun Xiao (USTC; Meituan; City University of Hong Kong)
Type: arXiv preprint (2610.23599)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.23599-from-trajectories-to-differentiated-skills-cogni.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

Skill-evolution methods usually store one artifact per skill. The authors say a skill mixes jobs, and those jobs should update separately. Cognitive Differentiation in Skill Evolution (CDSE) keeps four parts: Meta, Experience, Tool, and Script. It pulls semantic gradients from successful and failed trajectories, files them by role, and updates each part with its own check.

An analysis of **500** top-ranked skill packages finds that **96.8%** contain knowledge in at least two of those roles. Across six benchmarks, three agent models, and two harnesses, CDSE is first in all **36** settings. It gains **7.6** points over the base agent and **2.6** points over the strongest other method in each setting.

This is the same family as EmbodiedEvo in the osint wiki: distill a skill from trajectories, do not replay the raw log. The new claim is that one blob is the wrong unit. **No install.**

## Snippets

> "CDSE achieves the highest scores in all 36 settings, improving over the Base agent by 7.6 percentage points and the strongest competing method in each setting by 2.6 points on average." [Source: arxiv-2610.23599 abstract]
