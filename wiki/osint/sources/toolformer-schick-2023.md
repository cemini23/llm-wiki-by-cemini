---
title: "Toolformer — Language Models Can Teach Themselves to Use Tools (Schick et al., Meta AI Research, Feb 2023)"
type: source
tags: [paper, llm-agents, tool-use, self-supervised, meta-ai, arxiv, foundational, k41]
keywords: [toolformer, tool-augmented-llm, self-supervised-tool-learning, api-call-prediction, calculator-qa-search-translation-calendar, schick, dwivedi-yu, dessi, raileanu, lomeli, zettlemoyer, cancedda, scialom]
related:
  - concepts/llm-agent-systems.md
  - concepts/multi-agent-trading.md
  - sources/react-yao-2022.md
  - concepts/conductor-orchestrator.md
  - sources/generative-agents-park-2023.md
maturity: validated
read_status: skimmed
created: 2026-05-13
updated: 2026-05-13
clusters: [llm-agents, methodology]
---

## Relations

- @concepts/llm-agent-systems.md — Toolformer is one of the two foundational papers (with @sources/react-yao-2022.md) underlying Cemini's tool-using-agent architecture
- @concepts/multi-agent-trading.md — tradingagents-style LangGraph pipelines rely on tool-use primitives Toolformer formalized
- @sources/react-yao-2022.md — companion ICLR 2023 paper; ReAct = reasoning + acting interleaved, Toolformer = self-supervised tool-call insertion training. Different mechanism, same goal (LLM-as-action-issuer)
- @concepts/conductor-orchestrator.md — Cemini's Conductor multiplexes between tools at inference time; Toolformer trained the *model* to do that selection. Cemini's posture is inference-time orchestration over Toolformer-style training, but both share the policy-over-tools framing

## Raw Concept

- **Original title**: "Toolformer: Language Models Can Teach Themselves to Use Tools"
- **Authors**: Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom
- **Affiliation**: Meta AI Research (Dessì also Universitat Pompeu Fabra)
- **Publication**: arXiv 2302.04761v1 (Feb 2023, no venue label on v1)
- **PDF location (post-scp)**: `cemini-librarian:/opt/cemini-bulk/research/2302.04761v1.pdf`
- **sha256**: `6d7483d94653008e...` (preingest verdict: NEW)
- **Size**: 657,966 bytes, 17 pages
- **Read status**: skimmed (abstract + §1 introduction; full read deferred)
- **Discovered via**: user drop into `research to be indexed/` 2026-05-12

## Narrative

### What Toolformer is

A self-supervised training procedure that teaches a language model to **insert API calls into its output stream and incorporate the results back into next-token prediction**. The model decides which API to call, when, with what arguments, and how to use the returned value.

Tool set in the paper: calculator, Q&A system (Atlas), Wikipedia search engine, translation system (NLLB), calendar. Five APIs is intentionally small; the contribution is the training method, not the tool count.

### Self-supervised training procedure

1. Sample candidate insertion points in a corpus of plain text
2. For each candidate, generate possible API calls (few-shot prompted from a handful of human-written demonstrations)
3. Execute the API call; check if the returned value **reduces the model's loss on the surrounding text**
4. Keep insertions that help, discard the rest
5. Fine-tune on the filtered, augmented corpus

The cleverness: no human labels for "should this call a tool here," only the **loss-reduction signal** on natural text. The corpus teaches itself.

### What Toolformer demonstrated

- Substantially improved zero-shot performance on tasks where tool-use helps (math, QA, multilingual)
- Performance competitive with **much larger** non-tool models on those tasks
- **Core language modeling abilities preserved** — Toolformer doesn't sacrifice general capability for tool-use

### Cemini relevance

- **Architectural ancestor**, not a direct drop-in. Cemini doesn't fine-tune; we orchestrate. But the framing — "LLM decides when to defer to deterministic API, then uses result for next token" — is the substrate Cemini's MCP-tool-marketplace + Conductor pattern inherits.
- **K41 X.docx Rule 5 parallel**: Forrest Chang's CLAUDE.md template Rule 5 ("Use the model only for judgment calls") is the operational sibling of Toolformer's training-time bet: deterministic code is more reliable than LLM-decided behavior for deterministic decisions. Toolformer trained that policy in; Cemini bakes it into prompts.
- **Foundational, not actionable**: this paper does not require any Cemini implementation work. It establishes the discourse Cemini's agent stack assumes.

## Snippets

> "We show that LMs can teach themselves to use external tools via simple APIs and achieve the best of both worlds." [Source: 2302.04761v1.pdf p.1]

> "Toolformer achieves substantially improved zero-shot performance across a variety of downstream tasks, often competitive with much larger models, without sacrificing its core language modeling abilities." [Source: 2302.04761v1.pdf p.1]
