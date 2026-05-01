---
title: "more links 5_1.docx — Wave 5.1 link evaluation (12 URLs, agent-framework focused)"
type: source
tags: [cemini-internal, competitive-intelligence, link-evaluation, wave-5-1, k-series, may-2026, agent-frameworks]
keywords: [autogen, crewai, agno, smolagents, openhands, superagi, guidance, dspy, instructor, unsloth, llamafactory, langchain-elixir]
clusters: [llm-agents]
related:
  - sources/wave-5-1-link-eval-stacks.md
  - sources/wave-5-1-link-eval-even-more.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/scatter-gather-topology.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/fastmcp.md
  - entities/infrastructure/deepseek-api.md
  - entities/frameworks/dspy.md
maturity: draft
read_status: read
created: 2026-05-01
updated: 2026-05-01
---

## Relations

- @sources/wave-5-1-link-eval-stacks.md — sibling Wave 5.1 doc (25 URLs, systems-architecture focused)
- @sources/wave-5-1-link-eval-even-more.md — sibling Wave 5.1 doc (27 URLs, infra + data-engineering focused)
- @concepts/wiki-tooling-evaluation.md — same three-surface evaluation methodology
- @concepts/ip-sale-readiness.md — AGPL-3.0 license assessments (Unsloth), IP-sale readiness framing throughout
- @concepts/scatter-gather-topology.md — DSPy's GEPA optimization loops as orchestration-pattern extension
- @entities/frameworks/langgraph.md — LangGraph as the benchmark against which all agent frameworks are evaluated
- @entities/frameworks/fastmcp.md — Instructor's structured-output integration with FastMCP tool decorators
- @entities/infrastructure/deepseek-api.md — Instructor/DSPy integration surface with DeepSeek's OpenAI-compatible endpoint
- @entities/frameworks/dspy.md — Stanford prompt-programming framework; Wave 5.1 Adopt for offline-compilation pattern (GEPA-optimize on laptop → ship static strings to production)

## Raw Concept

- Original title: more links 5_1.docx (Word document, title "Cemini Stack & Wiki Stack — Link Evaluation Brief")
- Author(s): Cemini-internal (Claude-agent-authored link evaluation)
- Type: Word document (.docx)
- Location: cemini-librarian:/opt/cemini-bulk/research/more links 5_1.docx
- Retrieved: 2026-05-01
- Evaluation date: 2026-05-01
- Pages / length: ~306 paragraphs, ~70K chars
- Read status: read
- SHA256: 89c9988be2f2cf3e...

## Narrative

Wave 5.1 link-evaluation brief focused specifically on agent-framework and LLM-orchestration projects. Evaluates 12 software packages against the standard three-surface framework. This document is the most framework-dense of the three Wave 5.1 evaluations, covering the major Python agent-orchestration ecosystem: AutoGen (Microsoft), crewAI, Agno, smolagents (HuggingFace), OpenHands, SuperAGI, Guidance, DSPy (Stanford), LangChain-Elixir, Instructor, Unsloth, and LLaMA-Factory.

The evaluation reveals a clear architectural thesis: the Cemini production stack's LangGraph-based linear 4-node StateGraph is the non-negotiable foundation, and all framework evaluations are gated by compatibility with that architecture. This produces a consistent pattern — frameworks that propose alternative orchestration paradigms (AutoGen's conversational routing, crewAI's event-driven flows, Hermes's TUI-driven goal modification) are rejected or demoted to Steal-from, while tools that enhance LangGraph's existing capabilities (Instructor for structured outputs, DSPy for prompt optimization) are adopted.

### Recommendation distribution

**Adopt (2):** Instructor (Pydantic-native structured JSON outputs, patches DeepSeek client's response_model parameter, eliminates custom retry-loop boilerplate in agents/orchestrator.py), DSPy (offline prompt compilation — optimize prompt strings on laptop against historical datasets, ship static optimized strings to production; GEPA optimization loops as the key mechanism).

**Steal-from (1):** crewAI (agents.yaml + tasks.yaml configuration schema — decouple prompt engineering from Python execution logic without adopting the crewAI runtime).

**Defer (2):** Agno (AgentOS layer theoretically wraps LangGraph agents into REST APIs, but Cemini already has mature custom FastAPI routing — gated on deeper architectural review showing Agno's session management outperforms current implementation), Guidance (constrained LLM generation via token-masking, but compatibility with DeepSeek's restricted OpenAI-compatible endpoint unverified; license also needs clarification).

**Reference-only (3):** AutoGen (conversation-based memory architecture is structurally incompatible with LangGraph's explicit state transitions, but multi-agent reasoning topologies are worth studying), smolagents (CodeAgent generates + executes Python at runtime — too dangerous for production, and Claude Code already serves the local workflow), OpenHands (dual-license model with proprietary enterprise/ directory — license contamination risk; Claude Code already handles local dev tasks).

**Reject (4):** SuperAGI (abandonware — last significant architectural updates >1 year ago, predates modern agent protocols), LangChain-Elixir (complete Erlang VM / Python stack mismatch across all three surfaces), Unsloth (AGPL-3.0 poison pill + requires GPU — no compatible hardware), LLaMA-Factory (requires GPU accelerators + PyTorch ecosystem — no hardware viability, massive Docker image bloat).

### Cross-cutting themes

**The LangGraph firewall**: Every agent framework is evaluated against a single question — "does it integrate with or enhance the existing LangGraph StateGraph, or does it compete with it?" Competing frameworks are categorically rejected regardless of technical merit. This is the most explicit architectural boundary articulated across all Wave evaluations.

**Structured-output convergence**: Both Instructor and DSPy address the same underlying problem (LLM output reliability) from complementary angles — Instructor constrains outputs at the schema level (Pydantic validation + retry), DSPy optimizes prompts at the compilation level (GEPA optimization loops). The evaluation recommends adopting both, with DSPy running offline on the laptop and Instructor running inline in production.

**Hardware as a hard filter**: Three of four Reject decisions cite the absence of GPUs as a primary or contributing factor. The CPU-only Hetzner constraint is absolute.

## Snippets

### Instructor — Adopt rationale
"Instructor is a Python library built to guarantee strictly structured JSON outputs from Large Language Models by integrating deeply with Pydantic. By patching standard LLM client SDKs, it enables developers to pass a defined Pydantic class directly to the response_model parameter. If the model returns malformed JSON, Instructor's built-in retry logic autonomously re-prompts the API with the validation error context until a structurally valid object is produced." [Source: more links 5_1.docx]

### DSPy — Adopt rationale
"Integration into the Cemini production stack presents a massive opportunity for optimization. The concrete integration vector involves replacing static prompt strings within the services/llm_analyst modules. Instead of relying on hardcoded prompts, DSPy can compile and inject mathematically optimized prompt structures that maximize the accuracy of downstream Polars data extraction while minimizing token consumption." [Source: more links 5_1.docx]

### crewAI — Steal-from rationale
"The concrete integration vector involves adapting its separation of concerns — specifically decoupling agent definitions and task definitions into agents.yaml and tasks.yaml — into the solo developer's existing curation process. This pattern cleanly separates the 'what' (task specification) from the 'how' (Python execution), a structural improvement over the current monolithic script architecture." [Source: more links 5_1.docx]

### AutoGen — Reference-only
"AutoGen is a framework engineered to construct applications using multiple interacting agents that communicate to complete tasks. The architecture abstracts the underlying invocations to large language models, providing internal orchestration mechanisms that manage conversation-based memory and multi-agent turn-taking. Integration into the Cemini production stack is blocked by fundamental architectural dissonance — Cemini relies on a linear 4-node StateGraph managed by LangGraph to ensure absolute deterministic execution for financial algorithmic trading." [Source: more links 5_1.docx]

### SuperAGI — Abandonware rejection
"SuperAGI operates as a monolithic framework and accompanying graphical user interface designed for deploying, managing, and executing concurrent autonomous AI agents. Integration into the Cemini production stack is completely untenable. Implementing abandoned software in a critical, 24/7 financial trading environment presents catastrophic security and operational risks." [Source: more links 5_1.docx]
