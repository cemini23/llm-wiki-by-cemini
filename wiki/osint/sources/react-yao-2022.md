---
title: "ReAct — Synergizing Reasoning and Acting in Language Models (Yao et al., Princeton + Google Brain, ICLR 2023)"
type: source
tags: [paper, llm-agents, tool-use, chain-of-thought, action-plan, princeton, google-brain, iclr-2023, arxiv, foundational, k41]
keywords: [react, reasoning-and-acting, interleaved-thought-action, chain-of-thought-extension, hotpotqa, fever, alfworld, webshop, yao, zhao, du, shafran, narasimhan, cao]
related:
  - concepts/llm-agent-systems.md
  - concepts/multi-agent-trading.md
  - sources/toolformer-schick-2023.md
  - concepts/conductor-orchestrator.md
  - concepts/reviewer-agent-inference-time-feedback.md
  - sources/generative-agents-park-2023.md
maturity: validated
read_status: skimmed
created: 2026-05-13
updated: 2026-05-13
clusters: [llm-agents, methodology]
---

## Relations

- @concepts/llm-agent-systems.md — ReAct is one of the two foundational papers (with @sources/toolformer-schick-2023.md) underlying Cemini's tool-using-agent architecture. ReAct introduced the *interleaved* reasoning-action trace format most agents now use.
- @concepts/multi-agent-trading.md — Cemini's LangGraph tradingagents trajectories are functional descendants of the ReAct loop: thought → action → observation → thought → action…
- @sources/toolformer-schick-2023.md — companion paper. ReAct = inference-time interleaved trace, Toolformer = training-time tool-call insertion. The two are usually deployed together (Toolformer-trained model running a ReAct-style trace).
- @concepts/conductor-orchestrator.md — Cemini's Conductor is a higher-level scheduler over what ReAct does for a single agent's inner loop
- @concepts/reviewer-agent-inference-time-feedback.md — K37 reviewer-agent operates on ReAct traces: critiques the proposed action *before* the action is taken, fitting between the model's "thought" and "action" emissions

## Raw Concept

- **Original title**: "ReAct: Synergizing Reasoning and Acting in Language Models"
- **Authors**: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- **Affiliations**: Princeton (Yao, Narasimhan); Google Research, Brain team (Zhao, Du, Yu, Shafran, Cao)
- **Publication**: ICLR 2023 (arXiv 2210.03629)
- **PDF location (post-scp)**: `cemini-librarian:/opt/cemini-bulk/research/react-yao-2022.pdf` (after rename from inbox)
- **sha256**: `f285b0971ae4a790...` (preingest verdict: NEW)
- **Size**: 633,805 bytes, 33 pages
- **Read status**: skimmed
- **Discovered via**: user drop into `research to be indexed/` 2026-05-12

## Narrative

### What ReAct is

A prompting technique that interleaves **reasoning traces** (free-form chain-of-thought) and **acting steps** (tool calls or environment actions) in a single output stream. Each thought step can update the action plan; each action step gathers information that feeds the next thought.

The trace format:
```
Thought 1: <free-form reasoning>
Action 1: <tool call or environment action>
Observation 1: <result>
Thought 2: <reasoning update>
...
```

### Why it works

Chain-of-thought alone is hallucination-prone: the model invents facts without grounding. Action-only agents lack the introspection to recover from errors. ReAct's contribution is that **reasoning supervises action and action grounds reasoning** — each side fixes the other's failure mode.

The paper shows ReAct on:
- HotpotQA (multi-hop QA): overcomes hallucination in chain-of-thought
- Fever (fact verification): same
- ALFWorld (text-based household): better task completion than action-only baselines
- WebShop (e-commerce navigation): same

### Cemini relevance

- **Trace format inheritance**: every LangGraph agent in Cemini's tradingagents pipeline emits ReAct-style traces internally. The `signals` field on close-out (@concepts/agent-trajectory-triage-signals.md, K37) is post-hoc analysis of ReAct traces.
- **Reviewer-agent insertion point**: K37 reviewer (@concepts/reviewer-agent-inference-time-feedback.md) intercepts between the Thought and Action emission steps of a ReAct trace. ReAct's interleaved format is what makes that insertion possible — you cannot review an opaque single-step generation the same way.
- **Hallucination + error propagation mitigation**: ReAct's own headline contribution (overcoming hallucination in CoT via grounding) is the *prior* layer of defense that Cemini's reviewer-agent and signals layers build on top of.
- **Foundational, not actionable**: like Toolformer, no implementation work derives from this. Documents the lineage of Cemini's agent stack.

## Snippets

> "While large language models (LLMs) have demonstrated impressive performance across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two." [Source: 2210.03629 / ReAct.pdf p.1]

> "On question answering (HotpotQA) and fact verification (Fever), ReAct overcomes prevalent issues of hallucination and error propagation in chain-of-thought reasoning by interacting with a simple Wikipedia API." [Source: 2210.03629 / ReAct.pdf p.1]
