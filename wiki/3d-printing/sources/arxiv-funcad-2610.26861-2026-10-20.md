---
title: "FunCAD — agents that synthesize mechanisms and test them"
type: source
related:
  - concepts/k293-3d-printing-wave.md
  - concepts/self-improving-cad-generation-agents.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: Can It Actually Work? Synthesizing Functional CAD Mechanisms
Authors: Wenqian Zhang, Yangyi Huang, Zigeng Xu, Weiyang Liu, Zhen Liu (CUHK Shenzhen; CUHK)
Type: arXiv preprint (2610.26861)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2610.26861-can-it-actually-work-synthesizing-functional-cad.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract and contributions)
Project: https://thegenlab.ai/funcad/

## Narrative

LLM agents can emit a CAD assembly that looks plausible and does not perform the requested function. Functional CAD is the setting where the request is underspecified, and the agent must build a mechanism and revise it until a physical simulation passes. Two mechanisms can do the same job with different parts, controls, and motion, so a visual check is not enough.

FunCAD-Bench covers **46** mechanism families and a simulator for cheap physical checks. FunCAD-Harness derives requirements and abstract test templates from the user request, builds a test that fits the candidate, and feeds structured simulation results back into the next revision. The authors say a separate experiment still shows substantial task success when one piece is removed from the constructor. This skim did not extract that ablation's number, so it is not cited here.

The printed-prototype figure in the paper is an illustration of a cup-retrieval mechanism. It is not a Cemini print. **REFERENCE. No clone. No slicer change.**

## Snippets

> "While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions." [Source: arxiv-2610.26861 abstract]
