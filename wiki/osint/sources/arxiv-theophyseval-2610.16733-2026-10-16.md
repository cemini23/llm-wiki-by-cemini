---
title: "TheoPhysEval — 50 unpublished theoretical-physics problems for AI agents (arXiv 2610.16733)"
type: source
tags: [eval, agents, benchmarks, source, k292]
keywords: [TheoPhysEval, Harbor, memorization, two-track harness, GPT-6 Astra, agent eval methodology]
related:
  - concepts/k292-osint-wave.md
  - concepts/agent-harness-verification-bottleneck.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @concepts/k292-osint-wave.md — K292 osint wave hub
- @concepts/agent-harness-verification-bottleneck.md

## Raw Concept

Title: TheoPhysEval: Assessing AI agents at autonomous theoretical physics problem solving
Authors: A. Ramesh Chandra et al. (~35 authors across 19 institutions; coordinators Praneeth Netrapalli and Suvrat Raju; Google DeepMind among them)
Type: arXiv 2610.16733v1 [hep-th], 56 pages, 9 Oct 2026
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/2610.16733v1.pdf`
Retrieved: 2026-10-16
Data: `huggingface.co/datasets/RameshChandra1/TheoPhysEval` · harness: Harbor (Zenodo 10.5281/zenodo.20953922)
Read status: read

## Narrative

**No finance content.** This is an AI-capability benchmark for theoretical physics. It is filed for one methodological reason, stated at the end.

**Design.** 50 **unpublished** research-level theoretical-physics problems with verifiable answers, graded as unguessable floating-point numbers so automated checking works. A typical problem is about a day's work for a world expert, longer for adjacent specialists. Run through the **Harbor** agent harness in two tracks:

- **Realistic** — web search plus local numerical and symbolic tools.
- **Isolated** — local tools only, no web, no background literature.

The **two-track design is the transferable idea**: it turns memory into a measurable quantity, because the gap between the tracks bounds how much of the score is recall rather than reasoning.

**Pass rates (of 50):**

| Agent | Realistic | Isolated |
|---|---|---|
| GPT-6 Astra in Codex | **98%** (49/50) | 92% |
| Opus 5.5 in Claude Code | 92% (46/50) | 92% |
| Gemini | 68% (34/50) | 62% |
| DeepSeek | 54% (27/50) | 50% |
| GLM | 42% (21/50) | 52% |

**The single problem no agent solved is §1b, an inverse problem.** One problem, so treat it as an anecdote, not a capability boundary.

**Cost and tokens.** Astra cost **$116.28** realistic / $95.20 isolated, about **$2.33 per problem**, on **24.5-37.4m tokens**. Opus cost $240.43 / $275.46 on **211-228m tokens**. Gemini spent $95.01 on **595-607m tokens**. DeepSeek was cheapest at $36-37. So the accuracy winner is also the token-efficiency winner by roughly an order of magnitude — the same shape as the K290 Muse Wonder result.

**Authors' headline claim:** accuracy changes **only slightly** when web search and background papers are denied. Their reading is **significant memorisation of the literature**. That is the most useful number here, and it is a caution about every "agent solves frontier problems" headline.

**Limitations they state.** Not an adversarial benchmark — they explicitly declined to maximise failure. Possible leakage (human experts used AI; one solution was published after the run). **Single run per agent**, so sampling noise is uncontrolled. Grading ambiguities on three problems. Topic distribution skewed by who participated.

### Why it matters here

Two things, both about **eval design**, none about physics:

1. **Run the same eval with and without retrieval.** The delta is a memorisation estimate. Any benchmark we build or cite for agents on quant tasks should carry both tracks, because a wiki-adjacent agent has a corpus and gains are easily recall.
2. **Distrust agent benchmark scores without a cost axis and a run count.** This paper reports both, and its own single-run caveat is the honest part.

The paper also carries a **citation warning**. Latent Space reported GPT-6 Astra scoring 49/50 and that **the benchmark's authors confirmed several reference solutions were wrong**. Any number quoted from this benchmark should be treated as moving.

**No trade. No scp.**

## Snippets

> On average, agents show only small changes in accuracy when denied web search and access to background research papers, suggesting significant memorization of the literature. [Source: arXiv 2610.16733, abstract]

> We comment on the broader implications of these findings and discuss possible explanations for the current lack of agent-led breakthroughs in theoretical physics despite their outstanding problem-solving abilities. [Source: arXiv 2610.16733, abstract]
