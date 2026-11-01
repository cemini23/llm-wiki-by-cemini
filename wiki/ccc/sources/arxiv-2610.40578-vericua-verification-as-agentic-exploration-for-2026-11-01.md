---
title: "VeriCUA: Verification as Agentic Exploration for Computer-Using Agents"
type: source
tags: [source, arxiv, computer-using-agents, verification, agentic-exploration]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | VeriCUA: Verification as Agentic Exploration for Computer-Using Agents |
| Authors | Qiushi Sun et al., Google and The University of Hong Kong |
| arXiv | 2610.40578 |
| File | `arxiv-2610.40578-vericua-verification-as-agentic-exploration-for.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.40578 |
| Read status | skimmed (abstract + intro) |

## Narrative

Computer-using agents (CUAs) act across desktop, mobile, and web environments. The paper says that scaling them requires reliable task-completion verification for data curation, evaluation, and reinforcement learning. Typical automated checks prompt a vision-language model (VLM) to judge a trajectory, or they generate a program that inspects application state. The paper states that both checks use a partial view of a complex digital environment. A VLM judge is limited to the supplied observations. A generated program depends on accessible state. Those views can omit decisive evidence, or they can leave a completion judgment unsupported. Separate verifiers for each platform and access setting add engineering cost.

VeriCUA is a platform-agnostic framework for verification through agentic exploration. It treats verification as dynamic evidence gathering and assessment. One shared procedure covers online and offline settings, across platforms and observation modalities. The verifier inspects the available context and builds a task rubric. It selects GUI checks or code checks for requirements that remain unresolved. It combines those findings under explicit evidence rules.

The introduction states why a completion claim can be false. Success can depend on visual presentation, application records, or changes to persisted files. A trajectory can look successful when edits stay unsaved, or when an operation fails without a visible warning. An agent can also report completion after it fulfills only part of the instruction. Online verification uses the resulting machine state. Offline verification uses the retained trajectory. Evidence can come from rendered interfaces, structured observations, or artifacts such as files and database records. A fixed set of frames can omit a decisive effect. A generated query can target state that does not answer the verification question.

The abstract reports this experimental result in these words: improved agreement with reference labels over the compared baselines across these settings, with the largest offline gains on hard cases and stronger rejection of false completion claims online. Further analyses connect these gains to complementary evidence and test-time exploration. The abstract does not quote a numeric score. This result is a single-source claim.

An AI-agent and coding-harness practitioner uses completion labels to curate traces, score evaluations, and supply reinforcement-learning rewards. The paper presents VeriCUA as one shared procedure that gathers GUI evidence and code evidence when platform access and observation modality change. The text does not describe a harness implementation.

## Snippets

> "We present VeriCUA, a platform-agnostic framework for verification through agentic exploration. It treats verification as dynamic evidence gathering and assessment within a shared procedure for online and offline settings across platforms and observation modalities." [Source: `arxiv-2610.40578-vericua-verification-as-agentic-exploration-for.pdf` p.1 (arXiv 2610.40578), retrieved 2026-11-01]
