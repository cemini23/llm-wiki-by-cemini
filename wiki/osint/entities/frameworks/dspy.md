---
title: DSPy — Stanford Prompt-Programming Framework (Declarative, Compiling, GEPA-optimized)
type: entity
tags: [entity, framework, llm-prompting, prompt-optimization, offline-compilation, cemini-adopt]
keywords: [dspy, stanford, prompt-programming, signatures, gepa, offline-compilation, deepseek-api, prompt-optimization, Apache-2.0]
related:
  - sources/wave-5-1-link-eval-more.md
  - entities/frameworks/langgraph.md
  - entities/infrastructure/deepseek-api.md
  - concepts/scatter-gather-topology.md
maturity: draft
created: 2026-05-01
updated: 2026-05-01
---

## Relations

- @sources/wave-5-1-link-eval-more.md — Wave 5.1 Adopt-tier recommendation; primary evaluation source
- @entities/frameworks/langgraph.md — LangGraph provides the production execution surface; DSPy provides the offline prompt-compilation pipeline that feeds optimized strings into LangGraph nodes
- @entities/infrastructure/deepseek-api.md — DSPy's GEPA optimization loops run against the DeepSeek hosted API; compilation cost is the primary risk
- @concepts/scatter-gather-topology.md — DSPy's multi-prompt optimization patterns relate to scatter-gather decision-topology design

## Raw Concept

Surfaced as an Adopt-tier recommendation in Wave 5.1 link evaluation (@sources/wave-5-1-link-eval-more.md). DSPy (Stanford NLP) is a programming model that shifts LLM interaction from manual prompt engineering to declarative "Signatures" (input/output specifications) with algorithmic compilation of optimized prompts. Apache-2.0 license.

## Narrative

### What it is

DSPy functions as a programming model that abstracts LLM interaction away from manual prompt engineering. Instead of writing and tuning prompt strings by hand, developers declare "Signatures" — structured input/output specifications (e.g., "consume financial news and return market sentiment with confidence score") — and the framework algorithmically compiles optimized prompts using techniques like GEPA (Generate Evaluate Prompt Aggregate) optimization loops.

The key architectural insight: DSPy separates prompt *design* (the human's job — specifying what the model should do) from prompt *optimization* (the compiler's job — finding the most effective way to say it). This is analogous to how a C compiler separates algorithm design from register allocation.

### Cemini integration vector

**Offline compilation pattern** (the Wave 5.1 recommended path):

1. Install DSPy on the local macOS laptop (workflow environment)
2. Define Signatures for each LangGraph node's LLM call (sentiment extraction, signal classification, trade rationale generation)
3. Run GEPA optimization loops against historical datasets, using the DeepSeek API as the optimization backend
4. Extract the resulting optimized static prompt strings
5. Ship those strings directly into `agents/orchestrator.py` and `services/llm_analyst/` modules

This pattern delivers DSPy's optimization benefits without introducing the framework as a runtime dependency on the production Hetzner server. Production continues to execute static prompts via the existing DeepSeek client — no DSPy import, no compilation overhead, no additional dependency.

### Risks

**API cost**: GEPA optimization loops require repeated LLM calls during compilation. Running these against the DeepSeek hosted API (rather than a local model) incurs direct per-token costs. The number of optimization iterations and the evaluation-dataset size must be calibrated to keep compilation economically viable.

**Paradigm shift**: DSPy transitions prompt versioning from Git text diffs to a machine-learning optimization workflow. This complicates the CI/CD pipeline — prompt changes become the output of an optimization process rather than direct human edits.

**Evaluation dataset quality**: DSPy's optimizers require high-quality evaluation datasets. If the historical data used for compilation contains biases or noise, the optimized prompts will amplify those errors.

### License

Apache-2.0 — fully clean for IP-sale readiness. The offline-compilation pattern (laptop only) further isolates any license considerations from the production codebase.

## Snippets

### Wave 5.1 Adopt rationale
"DSPy functions as a programming model that shifts language model interaction away from manual prompt engineering by abstracting pipelines into imperative text transformation graphs. The framework utilizes 'Signatures' to declare required inputs and outputs and compiles mathematically optimized prompt structures. Rather than guesswork, the system runs structured optimization loops against historical datasets to determine which prompt phrasings maximize downstream accuracy." [Source: wave-5-1-link-eval-more.md]

### Integration vector
"The concrete integration vector involves replacing static prompt strings within the services/llm_analyst modules. Instead of relying on hardcoded prompts, DSPy can compile and inject mathematically optimized prompt structures that maximize the accuracy of downstream Polars data extraction while minimizing token consumption. The solo developer can utilize DSPy offline on the local laptop to algorithmically optimize the summarization prompts used during the deep-read process." [Source: wave-5-1-link-eval-more.md]

### Risk — API costs
"The specific compute API costs associated with running DSPy's intensive GEPA optimization loops against the DeepSeek hosted API, as repeated LLM calls during compilation can incur massive, unexpected charges." [Source: wave-5-1-link-eval-more.md]
