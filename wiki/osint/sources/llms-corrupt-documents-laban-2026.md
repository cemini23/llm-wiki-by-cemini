---
title: "LLMs Corrupt Your Documents When You Delegate (arXiv 2604.15597, Laban + Schnabel + Neville, Microsoft Research, 2026)"
type: source
tags: [paper, llm-agents, llm-evaluation, document-editing, delegation, vibe-coding, refutation-paper, microsoft-research, frontier-model-evaluation, governance, cemini-relevant, preprint, delegate-52]
keywords: [delegate-52, llm-corruption, delegated-work, round-trip-relay, backtranslation, vibe-coding, document-editing-benchmark, 52-professional-domains, frontier-model-degradation, gemini-3-1-pro, claude-4-6-opus, gpt-5-4, agentic-tool-use, distractor-context, philippe-laban, tobias-schnabel, jennifer-neville, microsoft-research, semantic-equivalence, domain-specific-parsing, llm-as-judge-fails]
clusters: [llm-agents, infrastructure]
related:
  - concepts/llm-agent-systems.md
  - concepts/high-signal-paper-patterns.md
  - entities/infrastructure/deepseek-api.md
  - sources/agentic-harness-engineering.md
  - sources/training-free-grpo-cai-2025.md
  - sources/upstash-context7.md
maturity: validated
read_status: read
created: 2026-04-29
updated: 2026-04-30
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub; this paper is the **caution-side complement** to AHE/TF-GRPO/IKP. Where those papers tell us how to make LLM agents better, LLMs-Corrupt tells us how unreliable they are at delegated long-horizon document editing — the empirical ceiling on what API-based delegation can do today.
- @concepts/high-signal-paper-patterns.md — rubric retrofit: refutation premium ("delegated work / vibe coding works as a paradigm" → wrong, even frontier models corrupt 25% of content), comprehensive prior-work integration, code release at github.com/microsoft/DELEGATE52, strong author lineage.
- @entities/infrastructure/deepseek-api.md — **directly Cemini-relevant**: Cemini delegates analyst tasks to DeepSeek-V4-flash; this paper's "natural language and niche" domain category (where degradation is worst) directly maps to Cemini's actual workload (earnings calls, regulatory documents, specialized financial reasoning). The paper provides empirical risk evidence for Cemini's analyst-delegation pattern.
- @sources/agentic-harness-engineering.md — **complementary frame**: AHE's harness-evolution improves agent performance on Terminal-Bench 2 (a *coding-agent* benchmark — programmatic domain, where this paper shows LLMs perform best). LLMs-Corrupt warns that the AHE result may NOT generalize to natural-language / niche domains (earnings, music notation, accounting). The two papers together: AHE for code-agent harness optimization; LLMs-Corrupt for "what's the ceiling on delegated work in non-code domains?"
- @sources/training-free-grpo-cai-2025.md — sibling LLM-agent-evaluation paper; both validate on DeepSeek-family or via API. TF-GRPO improves agent performance on math + web search; LLMs-Corrupt shows that even frontier models corrupt documents at 25%+ rates on broader delegated work. Useful pairing: TF-GRPO is the methodology to *improve* agents; LLMs-Corrupt is the methodology to *measure* the corruption rate.

## Raw Concept

- **Original title**: "LLMs Corrupt Your Documents When You Delegate"
- **Authors**: Philippe Laban, Tobias Schnabel, Jennifer Neville (Microsoft Research)
- **Type**: arXiv preprint (cs.CL, 36 pages) — under review
- **arXiv ID**: 2604.15597v1
- **Submitted**: 17 April 2026
- **License**: arXiv non-exclusive distribution license 1.0 (paper)
- **Code & dataset**: https://github.com/microsoft/DELEGATE52 + https://huggingface.co/datasets/microsoft/DELEGATE52
- **Author affiliations**: all three at Microsoft Research (Laban formerly Salesforce AI; Neville also Purdue)
- **PDF location**: cemini-librarian:/opt/cemini-bulk/research/llms-corrupt-documents-laban-2026.pdf (post-ingest scp)
- **Read status**: read (pages 1-5 covering abstract / introduction / methodology / benchmark construction / experimental setup; pages 6-36 contain detailed results, ablations, discussion not deep-read in this pass)
- **Discovered via**: User manual drop 2026-04-29
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, infrastructure

## Narrative

### What it claims

Recent LLM progress has enabled **delegated work** as a new interaction paradigm — knowledge workers supervise LLMs as they complete tasks (e.g., "vibe coding"). Crucially, the user delegating work may lack expertise or time to review the LLM's changes, and **must trust** that the LLM doesn't introduce silent errors. The paper asks: how trustworthy are current LLMs in delegated workflows, and across what range of professional domains?

**Three contributions**:

1. **DELEGATE-52** — a benchmark of 310 work environments across 52 professional domains: Code & Configuration (Python, JSON, Docker, Database, etc.), Science & Engineering (Aviation, Crystallography, Lean, Robotics, Quantum, Weather, Satellite, etc.), Creative & Media (Music Sheet, 3D Objects, Screenplay, Subtitles, etc.), Structured Records (Accounting, Calendar, Genealogy, Library Catalog, etc.), Everyday (Chess, Earnings Calls, Recipe, Transit, Job Board, etc.). Each environment uses real documents (no synthetic), ~15k tokens, with 5-10 complex editing tasks.

2. **Round-trip relay simulation** — a methodology for evaluating long-horizon delegated interaction without annotation or reference solutions. Each task `σ` is invertible (forward instruction + backward inverse `σ⁻¹`); applying both should return to the seed under a perfect model. Compose round-trips into longer workflows. Measure `RS@k = sim(s, ŝ_k/2)` after k interactions.

3. **A large-scale simulation with 19 LLMs**. Findings:
   - **Frontier models (Gemini 3.1 Pro, Claude 4.6 Opus, GPT-5.4) corrupt 25% of document content** by the end of 20 interactions
   - **Average across all 19 models: 50% degradation**
   - **Domain-dependent**: programmatic domains (Python, Database) far better than natural-language / niche (earnings calls, music notation, music sheet)
   - **"Ready" threshold**: 98% retention after 20 interactions. **Only Python passes for most models.**
   - **Compound effects**: document size + interaction length + distractor context all worsen degradation, and these effects compound over time (short simulations underestimate severity)
   - **Agentic tool use does NOT improve performance** on DELEGATE-52
   - **Generic similarity measures (incl. GPT-5.4-as-judge) fail** — they only correlate moderately with the paper's parsing-based domain-specific metrics, capturing at most 25% of the variance. Justifies the paper's substantial investment in 52 custom domain parsers.

### Methodological highlights — why this paper's framing is load-bearing

The **round-trip relay** is a clever methodology innovation:
- No reference annotations needed (cost reduction → 52-domain scale)
- Long-horizon evaluation without manually crafting multi-step task sequences
- Backtranslation from MT literature, repurposed for LLM consistency

The **domain-specific parsing** approach is the empirical foundation:
- Each domain implements a parser converting documents to structured representation
- A similarity function compares parsed structures
- Surface-level changes that don't matter semantically (e.g., "200g vs 0.2kg butter") don't affect the score
- Substantial changes (e.g., "200g vs 800g butter") strongly affect the score
- Generic LLM-as-judge fails to capture this nuance — paper validates with detailed correlation analysis (Appendix C)

### Why this matters for Cemini

Cemini's stack delegates analyst tasks to DeepSeek-V4-flash. **Most Cemini analyst work is "natural language and niche"** — exactly the worst-performing category in DELEGATE-52:

| Cemini analyst task type | DELEGATE-52 closest mapping | Expected reliability per LLMs-Corrupt findings |
|---|---|---|
| Earnings call interpretation + ticker note generation | EARNCALL (worst category) | Severe degradation expected over multi-step workflows |
| SEC 10-K / 10-Q regulatory document editing | Closest: Structured Records / specialized | High degradation expected |
| Multi-day debate trajectory persistence (cpr-pattern) | Long-horizon document editing | Compound degradation; severity grows with interaction length |
| Python code generation / orchestrator updates | Python (best category) | Better — most models reach 98% in this domain |

**Operational implications for Cemini**:

1. **Don't trust DeepSeek with multi-step analyst editing without verification gates**. The paper's finding that frontier models corrupt 25% of content over 20 interactions is the empirical ceiling. Cemini's `agents/orchestrator.py` should NEVER allow DeepSeek to do >5 consecutive document-editing steps without a human-or-LLM-judge verification checkpoint.

2. **Implement round-trip-relay-style verification on critical paths**. Cemini's regulatory-document-editing pipeline (when it lands) should periodically apply σ then σ⁻¹ on a known document and check semantic equivalence. If the round-trip score drops below threshold, alert. This is a direct application of the paper's methodology.

3. **Domain-specific parsers + similarity functions** are the right approach for evaluation, not LLM-as-judge. Paper proves LLM-as-judge captures only 25% of variance. For Cemini's specialized domains (ticker pages, regulatory documents, prediction-market analysis), build domain-specific evaluators rather than relying on a generic "is this good?" LLM call.

4. **Agentic tool use doesn't help** is a counterintuitive finding worth internalizing. The instinct of "give DeepSeek tools to handle long workflows" doesn't pay off on DELEGATE-52. **Cemini's agentic tool addition should NOT be motivated by "this will improve quality"** — the empirical evidence is that it won't. Tool use should be motivated by access (e.g., to data sources, calculators, search) — not delegation reliability.

5. **The paper's 19-model panel** includes GPT 4.1 / 5.x / o1 / o3 + Claude families + Gemini families + GPT OSS 120B. **Notably absent**: DeepSeek family. Open follow-on question: does DeepSeek-V4-flash perform similarly to other 671B-class models on DELEGATE-52? If similar: same caution applies. If much worse: Cemini's brain choice has a quality cost beyond what the paper measures.

### Risks & open questions

1. **Paper is "Preprint. Under review."** — methodologically rigorous Microsoft Research work but not yet peer-reviewed. Treat as preliminary; primary findings (25% corruption at frontier) are likely to hold but exact numbers may shift.

2. **DeepSeek not tested in the 19-model panel**. The paper's 19 models are from OpenAI / Anthropic / Google / Meta / open-weight families; DeepSeek absent. **Cemini-pre-deployment gate**: run DELEGATE-52 (publicly available at github.com/microsoft/DELEGATE52) against `deepseek-v4-flash` to measure the comparable corruption rate. ~half-day setup if the benchmark is reusable.

3. **Single-turn-per-step methodology** — paper notes each round-trip step is "an independent, single-turn session". Cemini's analyst orchestrator may use multi-turn dialogues. The relationship between single-turn corruption rates and multi-turn dialogues is open.

4. **Domain coverage gap for financial-analysis tasks**: DELEGATE-52 includes Accounting and Earnings-Call but not "stock research note", "ticker assessment", or "macro forecast". For Cemini-shape evaluation, may need to add custom domains.

5. **Microsoft AI affiliation = potential vendor framing** — though the methodology is general and the math doesn't favor Microsoft models specifically (Gemini 3.1 Pro and Claude 4.6 Opus also corrupt at 25%).

### Cemini-side adoption assessment

**Decision: Read + reproduce + integrate as monitoring**. Highest-priority recent ingest for production-deployment caution. Concrete next-steps:

1. **Read the appendices** (especially Appendix C on LLM-as-judge correlation, Appendix D on round-robin scheduling, Appendix K on environment construction). ~1.5 hours.
2. **Clone the github benchmark**: `git clone https://github.com/microsoft/DELEGATE52` + license check. ~15 min.
3. **Run DELEGATE-52 against deepseek-v4-flash** for the 5 most-Cemini-relevant domains (Python, JSON, Accounting, Earnings Call, Database). ~half-day. Compare results against the 19-model panel published numbers.
4. **Build a Cemini-shape extension**: 1-2 custom DELEGATE-52 domains for "ticker research note" and "regulatory document editing" using Cemini's actual sample documents. ~1-day.
5. **Wire round-trip relay verification into `agents/orchestrator.py`** as a deployment gate before letting any analyst do >5 consecutive editing steps. Brief to cemini-prod when ready. ~1-day brief drafting.

**This is the production-safety paper for Cemini's current stack.** Higher operational priority than AHE/IKP/TF-GRPO because it directly measures the failure mode of Cemini's existing pattern (delegate to DeepSeek; trust it; don't review).

### Citation

> Laban, P., Schnabel, T., & Neville, J. (2026). *LLMs Corrupt Your Documents When You Delegate*. arXiv:2604.15597 [cs.CL]. https://arxiv.org/abs/2604.15597 (Microsoft Research, preprint under review)

## Snippets

> **The headline empirical finding — the 25% number**
>
> "Even frontier models (Gemini 3.1 Pro, Claude 4.6 Opus, GPT 5.4) corrupt an average of 25% of document content by the end of long workflows, with other models failing more severely. Additional experiments reveal that agentic tool use does not improve performance on DELEGATE-52, and that degradation severity is exacerbated by document size, length of interaction, or presence of distractor files. Our analysis shows that current LLMs are unreliable delegates: they introduce sparse but severe errors that silently corrupt documents, compounding over long interaction." [Source: arXiv 2604.15597 abstract, p.1]

> **The "Python is the only ready domain" finding**
>
> "We define a model as 'ready' for delegated work in a domain if it achieves a score of 98% or higher after 20 interactions. Python is the only domain (out of 52) where most models are ready, highlighting the significant gap that remains." [Source: arXiv 2604.15597 §1, p.2]

> **The round-trip relay methodology — the load-bearing innovation**
>
> "Specifically, we assume every editing task is reversible, defined by a forward instruction and its inverse. Applying both in sequence forms a backtranslation round-trip that, under a perfect model, recovers the original documents exactly. This lets us evaluate performance by measuring document similarity before and after a round-trip. Round-trips can further be composed sequentially, forming a relay." [Source: arXiv 2604.15597 §1, p.2]

> **The LLM-as-judge failure mode — the methodological warning**
>
> "Implementing robust semantic equivalence for 52 domains is central to our methodology. In Appendix C, we show that generic similarity measures (including LLM-as-a-judge with GPT 5.4) fail to capture nuanced semantic differences, only moderately correlating with our parsing-based metric and capturing at most 25% of the variance." [Source: arXiv 2604.15597 §2.2.2, p.3]

> **The "agentic tool use doesn't help" counterintuitive finding**
>
> "We also find that using a basic agentic harness does not improve the performance of LLMs we test on DELEGATE-52, and that performance after... [page break]" [Source: arXiv 2604.15597 §1, p.2]

> **The compound-degradation finding — short simulations underestimate severity**
>
> "We confirm that known factors such as document size, interaction length, and distractor context contribute to degradation, but these negative effects compound over time, meaning short simulations underestimate their severity." [Source: arXiv 2604.15597 §1, p.2]
