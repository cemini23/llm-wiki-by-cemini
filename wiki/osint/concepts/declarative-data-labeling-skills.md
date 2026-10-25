---
title: "Declarative Data-Labeling Skills"
type: concept
tags: [concept, architecture-pattern, ingest-layer, data-labeling, agent-skills, reflection-loop]
keywords: [declarative labeling, dataframe labeling, agent skills, reflection loop, ground-truth refinement, ingest pipeline, semantic labeling]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - entities/tools/adala.md
  - entities/tools/finance-skills.md
  - concepts/curator-skills.md
  - concepts/agent-native-research-artifacts.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — pattern derived from URLs 14 + 15
- `@entities/tools/adala.md` — Adala is the autonomous-labeling reference implementation
- `@entities/tools/finance-skills.md` — finance-skills is the Agent-Skills-spec instance
- `@concepts/curator-skills.md` — skills-as-curation belongs to this family
- `@concepts/agent-native-research-artifacts.md` — labeled outputs are research artifacts

## Raw Concept

Declarative data-labeling skills name a pattern where each row of a structured dataset is annotated by an LLM via a small, declaratively-specified "skill" — a YAML/Markdown description of input schema, output schema, validation criteria, and (optionally) a reflection loop against ground-truth. The orchestrating framework handles batching, retries, schema validation, and learning.

## Narrative

### The problem

Trading and research stacks ingest large volumes of unstructured text:
- News events from GDELT
- SEC 10-K and 10-Q filings from EDGAR
- Earnings call transcripts
- Academic papers
- Social-intelligence feeds

To be useful in downstream signal generation, this text must be **labeled** — sentiment-scored, entity-extracted, factor-tagged, classified by topic. Hand-rolled Python loops over LLM calls work for prototypes but accumulate boilerplate:
- Batching and rate-limit handling
- Schema validation on LLM output (it lies about shape)
- Retry logic on transient errors
- Ground-truth comparison for prompt refinement
- Cost tracking per row

By the time a researcher has reimplemented this for the 3rd dataset, the boilerplate dominates the actual labeling logic.

### The pattern

A **skill** is a declarative artifact (YAML, Markdown, or registered Python decorator) that specifies:
1. **Input schema** — what a row looks like (text + metadata fields)
2. **Output schema** — what the label payload must contain (label + confidence + reasoning trace)
3. **Prompt template** — the LLM prompt (parameterized over input fields)
4. **Validation criteria** — assertions the output must pass before being committed
5. **(Optional) Ground-truth reference** — labeled examples for reflection-loop refinement

The orchestrating **framework** consumes skills and:
- Dispatches LLM calls in batches (with backoff)
- Validates outputs against schema; retries on shape failures
- Compares against ground truth (when provided) and rewrites the prompt iteratively
- Logs cost + latency per skill execution
- Persists labeled outputs to the data layer (Polars / PostgreSQL / pgvector)

### Instances catalogued

| Instance | Skill format | Reflection loop | Orchestrator |
|----------|--------------|:---------------:|--------------|
| **Adala** (HumanSignal) | Python class + Pandas df | Yes — iterates against ground truth | Native | 
| **finance-skills** (himself65) | Agent Skills spec (Markdown) | No (read-only data fetch) | npx-installed |

Adala's reflection loop is the harder + more powerful instance: skills *learn* by comparing outputs against ground truth and rewriting their internal prompts. finance-skills is simpler — it's read-only market data + sentiment fetch under the Agent Skills declarative format.

### Cemini significance

Cemini's ingest layer currently uses hand-rolled Python loops over DeepSeek API calls. Adopting Adala for batch labeling of GDELT events and EDGAR filings:
- Reduces ingest-layer boilerplate by ~hundreds of lines
- Introduces principled reflection-loop refinement (currently absent)
- Standardizes the labeling-skill format across all ingest sources

The Agent Skills spec (from finance-skills) provides the cross-tool format compatibility — Cemini-defined skills could in principle be portable to other Claude/Anthropic agent surfaces.

### Risks (pattern-level)

- **Abandonment risk on the orchestrator** — Adala v0.0.4 hasn't released in 2.5 years. Pattern dependence on a stale orchestrator is operational debt. Mitigation: fork to internal branch; accept maintenance burden.
- **Schema drift** — declarative outputs must stay forward-compatible as downstream consumers (Polars columns, PostgreSQL schema) evolve. Mitigation: schema versioning + migrations as first-class concerns.
- **Hidden coupling to Pandas / specific LLM SDK** — orchestrator may force serialization boundaries Cemini's Polars-native data plane has to absorb. Mitigation: chunked Pandas↔Polars casts at ingest boundary only.

### Anti-patterns

- **Don't write per-source labeling loops by hand** — once you have ≥3, lift to declarative skills
- **Don't embed labeling logic in the trading hot path** — labeling is batch ingest, not real-time trade signal
- **Don't skip the reflection loop on high-value labels** — sentiment/factor outputs that drive position sizing deserve the ground-truth refinement step

### Open questions

- Does Adala's `OpenAIChatRuntime` cleanly intercept the base URL for DeepSeek routing? [OPEN QUESTION 2026-05-10]
- What's the right ground-truth set size for Cemini sentiment skills — 50 hand-labeled examples? 500?
- Should Cemini's existing FastMCP `@mcp.tool` decorators be promoted to full Agent-Skills-spec skills for portability?

[Sources: Evaluating Code for Trading Stacks.docx URL 14 (Adala), URL 15 (finance-skills)]
