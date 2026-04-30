---
title: "Incompressible Knowledge Probes — Estimating Black-Box LLM Parameter Counts via Factual Capacity (arXiv 2604.24827, Bojie Li, Pine AI, 2026)"
type: source
tags: [paper, llm-evaluation, parameter-estimation, knowledge-capacity, factual-recall, mixture-of-experts, scaling-laws, densing-law-refutation, deepseek-relevant, frontier-model-estimation, single-author, pine-ai, cemini-relevant, preprint, cc-by-4-0]
keywords: [ikp, incompressible-knowledge-probes, factual-capacity, parameter-counting, log-linear-scaling, shannon-entropy, densing-law, allen-zhu-li-2025, morris-2025, knowledge-fingerprinting, hallucination-similarity, jaccard-overlap, gpt-5-5, claude-opus-4-7, gemini-3-1-pro, deepseek-v4-flash, deepseek-v4-pro-think, kimi-k2-6, qwen, mixture-of-experts, total-vs-active-params, openrouter-api, r-squared-0-917, leave-one-out-cv, landmark-tier-assignment, wikidata-probes, dblp-arxiv-researcher-probes]
clusters: [llm-agents, infrastructure]
related:
  - concepts/llm-agent-systems.md
  - entities/infrastructure/deepseek-api.md
  - sources/agentic-harness-engineering.md
  - concepts/high-signal-paper-patterns.md
  - sources/moe-efficiency-leverage-tian-2026.md
  - sources/moe-surpass-dense-equal-resource-li-2026.md
  - sources/thinking-with-visual-primitives-deepseek-2026.md
  - sources/platonic-representation-hypothesis-huh-2024.md
  - sources/sherry-ternary-quantization-tencent-2026.md
  - sources/shiyu-coder-kronos.md
maturity: validated
read_status: read
created: 2026-04-29
updated: 2026-04-30
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub; this paper provides the most rigorous black-box parameter-estimation methodology in the corpus, distinguishing procedural-capability scaling (compressible per Densing Law) from factual-capacity scaling (incompressible, Shannon-bounded).
- @entities/infrastructure/deepseek-api.md — **directly Cemini-relevant**: the calibration set (89 open-weight models, 19 vendors) includes `deepseek-v3`, `deepseek-v4-flash`, `deepseek-v4-flash-think`, and `deepseek-v4-pro-think` — i.e. Cemini's intended brain family. The IKP framework provides a quantitative basis for "how much factual recall can DeepSeek be expected to provide" without API spending on speculative testing.
- @sources/agentic-harness-engineering.md — sibling 2026-04 arXiv preprint on LLM agent infrastructure (28 Apr 2026 vs. 27 Apr 2026). Both quantify aspects of LLM systems Cemini's stack depends on: AHE measures harness-level evolvability, IKP measures factual capacity. Useful pairing for any future "what should Cemini optimize: harness or brain?" decision.

## Raw Concept

- **Original title**: "Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity"
- **Author**: Bojie Li (Pine AI) — single author
- **Type**: arXiv preprint (cs.LG, 79 pages including appendices)
- **arXiv ID**: 2604.24827v1
- **DOI**: 10.48550/arXiv.2604.24827
- **Submitted**: 27 April 2026
- **License**: CC BY 4.0 (paper); github code license to be verified [NEEDS VERIFICATION 2026-04-29]
- **Code**: https://github.com/19PINE-AI/ikp
- **Companion site**: https://01.me/research/ikp
- **PDF location**: cemini-librarian:/opt/cemini-bulk/research/Incompressible Knowledge Probes_ Estimating Black-Box LLM Parameter Counts via Factual Capacity.pdf (post-ingest scp)
- **Read status**: read (pages 1-8 covering intro / theoretical framework / methodology; appendices A-H not deep-read; results table from Figure 1 captured)
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, infrastructure

## Narrative

### What it claims

Closed-source frontier labs do not disclose parameter counts, and the existing alternative — inference economics ([Epoch AI, 2024], [Cai et al., 2025]) — carries 2× or more uncertainty due to confounds external to the model (hardware generation, batching, quantization, serving stack). Bojie Li proposes a tighter intrinsic bound from **information theory**: storing F facts requires at least F / (bits per parameter) weights, so measuring how much a model **knows** lower-bounds how many parameters it **has**.

The paper's three-pronged contribution:

1. **A theoretical framework** (Section 3) decomposing model parameters into N = N_fact + N_proc + N_ling. The **Densing Law** ([Huang et al., 2025], "capability density doubles every ~3.5 months") improves the efficiency of N_proc and N_ling — but N_fact is bounded below by Shannon entropy and **does not compress**. IKPs are designed to isolate N_fact from black-box API access.

2. **A benchmark + calibration**: 1,400 factual probes across 7 difficulty tiers (T1–T7), tier-assigned **empirically** by which of six landmark models (Qwen 2.5 0.5B / Qwen 2.5 7B / Qwen 3 32B / Qwen 3 235B / Kimi K2.5 / Gemini 3.1 Pro) answers correctly. Calibrated on **89 open-weight models from 19 vendors** spanning 135M–1,600B parameters: log-linear fit `R² = 0.917`. Leave-one-out cross-validation: **68.5% within 2× of true size, 87.6% within 3×**.

3. **A knowledge-fingerprinting technique** (Section 6): rare-fact Jaccard overlap **plus hallucination-similarity** (rate of agreement on **wrong** answers) yields a black-box test that distinguishes weight-sharing siblings, post-training lineages, and full retrains across closed-vendor families — without requiring model weights.

### Empirical highlights

**Frontier-model parameter estimates** (per Figure 1, derived by projecting proprietary IKP scores onto the open-weight calibration line):

| Model | Estimated total params |
|---|---|
| Claude Haiku 4.5 | ~65B |
| Gemini 2.5 Flash | ~207B |
| GPT-5 Mini | ~410B |
| Gemini 2.5 Pro | ~1.2T |
| Claude Sonnet 4.6 | ~1.7T |
| Claude Opus 4.6 | ~5.3T |
| GPT-5.5 | ~9.7T |

(Gemini 3.1 Pro is excluded from the calibration as a landmark; it sets T6 boundary by construction.)

**Heavily safety-tuned models receive lower bounds**: refusal policy can hide tens of percentage points of "refused but known" capacity, so Anthropic / OpenAI estimates may be conservatively biased downward by training-time refusal.

**MoE architectures**: total parameters predict knowledge (R² = 0.79) far better than active parameters (R² = 0.51). For Mixture-of-Experts model deployment, **the total parameter count is the relevant capacity measure** for factual recall — even though active params drive inference cost.

**The Densing Law refutation**: across 96 dated open-weight models (2024–2026), the time coefficient on IKP accuracy is **−0.0010/month** (95% CI [−0.0031, +0.0008]) — indistinguishable from zero, and rejecting the Densing-Law prediction of +0.0117/month at p < 10⁻¹⁵. **Factual capacity does not compress with newer training methods**; it tracks total parameter count log-linearly across generations and across vendors. Benchmark saturation on MMLU/HELM/etc is not evidence that scaling has ended; it is evidence that those benchmarks measure procedural capability, which is the part of scaling that **does** compress.

### Why this matters for Cemini

Several findings are directly operational for Cemini's stack:

1. **DeepSeek-family capacity is empirically calibrated**: the open-weight calibration set explicitly includes `deepseek-v3`, `deepseek-v4-flash`, `deepseek-v4-flash-think`, and `deepseek-v4-pro-think`. This means whenever Cemini's analyst orchestrator (`agents/orchestrator.py` → `services/llm_analyst/deepseek_client.py`) is asked a long-tail factual question, the IKP framework predicts the answer recall rate as a function of DeepSeek's parameter count. The "shrug → fall back to RAG" decision logic should be tier-calibrated: T1–T2 facts (common knowledge) DeepSeek will answer; T6–T7 (10–50 citation researchers, obscure entities) require explicit retrieval.

2. **Operationalizing the procedural-vs-factual split for cost optimization**: the workspace already considers swapping DeepSeek for cheaper models in the orchestration loop (per the `polygon_not_authorized_doctrine` memory + general API-cost discipline). The IKP finding suggests two distinct prompts/flows:
   - **Procedural tasks** (parsing 10-K filings, executing SQL, deciding which analyst to dispatch) — cheap models work fine; Densing Law applies; smaller faster models will catch up.
   - **Factual recall tasks** (which company owns this trademark? what was the GP-mortgage default rate in 2008?) — only big models work; Densing Law does NOT apply; switching to a smaller model degrades performance proportional to log(parameter ratio).

3. **Knowledge fingerprinting as a silent-swap detector**: if Cemini's DeepSeek API is ever silently quantized, replaced, or routed to a different model family by the vendor, the rare-fact-hallucination-similarity technique (Section 6) provides a daily detection signal. Cron a small IKP probe (say 50 questions from T5–T7) against the production endpoint; compare hallucination-similarity to a reference baseline; alert on drift > N standard deviations. **Low-effort instrumentation, high-leverage detection.**

4. **A black-box capacity estimate for any future API**: if Cemini ever evaluates Sakana Fugu, Anthropic, OpenAI, etc. for the analyst-orchestrator slot, running the IKP toolkit (`github.com/19PINE-AI/ikp`) against each candidate's API gives a parameter-count estimate without trusting vendor disclosures. **Vendor-independent capacity benchmarking** for procurement decisions.

### Methodology highlights for any reproduction

- **7 tiers (T1–T7)** assigned empirically: a probe is tier-k if the T_k landmark model answers correctly but T_{k-1} does not. Non-monotonic-correctness probes (~15%) are dropped as ambiguous.
- **Probe construction** combines two phases:
  - **Phase A** (T1–T2): LLM-generated candidates from GPT-5; ~82% land in T1–T2 regardless of difficulty prompting (an LLM cannot reliably generate probes beyond its own knowledge horizon — important constraint for any benchmark-design effort).
  - **Phase B** (T3–T7): corpus-grounded probes from Wikidata (557 probes, founding years + capital-style attributes) + DBLP/arXiv researchers (345 probes, ID a researcher's primary subfield AND name one verifiable artifact).
- **Quality filters**: exclude computable probes (e.g., IUPAC element naming) — these test reasoning not memorization. Exclude collision-prone names (Chinese 2-char, single-initial). Exclude ML/AI subfield researchers (training contamination). Embed grounding in the question template (every entity-naming question carries a discriminating Wikidata attribute extracted from a non-answer field) to avoid title-collision failures like "Madonna and Child" — which one?
- **Scoring**: temperature=0; Gemini 3 Flash Preview as judge; per-probe score in {+1.0, +0.5, 0, λ} where REFUSAL=0 and WRONG=λ. λ=−1.0 maximizes calibration R²; sensitivity sweep in Appendix B confirms this is the right wrong-answer penalty for the parameter-estimation use case.

### Risks & open questions

1. **Single-author paper** — Bojie Li (Pine AI) is the sole author. The literature review is comprehensive (15+ cited works; methodology builds on Allen-Zhu-Li 2025, Morris 2025, Kandpal 2023, Roberts 2020 — all peer-reviewed). The probe-set design is methodologically careful (10-round audit, monotonicity filter, evidence-required scoring). But solo-author work has a higher bar for replication; treat the specific frontier-model parameter estimates as **point estimates with the paper's stated 2x–3x uncertainty** rather than precise truth.

2. **License on the github toolkit** [NEEDS VERIFICATION 2026-04-29] — paper itself is CC BY 4.0 (clean), but `github.com/19PINE-AI/ikp` license needs verification before any code is borrowed. If Cemini wants to deploy a daily silent-swap detector, this is the gating check.

3. **Refusal-policy correction is asymmetric** — heavily safety-tuned models may receive estimates biased downward by tens of percentage points of "refused but known" capacity. The paper acknowledges this; the hallucination-similarity technique partially compensates but doesn't fully correct. **Anthropic and OpenAI estimates should be read as conservative lower bounds.**

4. **DeepSeek-think mode separation** — the calibration set distinguishes `deepseek-v4-flash` from `deepseek-v4-flash-think` and `deepseek-v4-pro-think` as separate data points, suggesting that the chain-of-thought / reasoning mode meaningfully changes IKP score. If Cemini's stack uses think-mode for complex analysis, the right capacity estimate is the think-mode estimate, not the flash estimate.

5. **The Densing-Law refutation argument depends on selecting only "incompressible" probes** — the paper makes a careful theoretical argument that factual recall of long-tail entities cannot be derived from general knowledge (Section 3.1). If a future architectural innovation provides a way to compress long-tail factual recall (e.g. better retrieval-augmented training), the argument could weaken. **The empirical finding is solid for current architectures; the theoretical argument is pre-emptive.**

### Cemini-side adoption assessment

**Decision: Watch-and-prototype**. The paper is high-signal, cleanly scoped, and the github code release lowers adoption friction substantially. Concrete next steps:

1. **Read appendices** A (probe-generation pipeline) + B (sensitivity sweep on λ) + H (the Hackergame anecdote thread) to fully internalize the methodology. ~1.5 hours.
2. **License-gate the github repo** via Exa `crawling_exa` against `github.com/19PINE-AI/ikp/blob/main/LICENSE` — same protocol as openclaude / agentic-harness-engineering. ~10 min.
3. **Empirical verification on DeepSeek**: install the IKP toolkit on the laptop, run 100-probe subset (T5–T7, the discriminating tiers) against `deepseek-v4-flash` via the existing API; compare to the paper's published results for the same model. Validates that Cemini's rate-limit envelope can absorb the cost (1,400 probes × $0.0001 input + $0.0004 output per 1k tokens × ~50 tokens/probe ≈ $0.04 — trivial). ~30 min.
4. **Decide on production swap-detector deployment** — if appendix A/B reading + license check + reproduction all clear, file a brief for cemini-prod-side execution: a daily 50-probe IKP cron against the production DeepSeek endpoint with hallucination-similarity drift alerting.

### Citation

> Li, B. (2026). *Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity*. arXiv:2604.24827 [cs.LG]. https://arxiv.org/abs/2604.24827

## Snippets

> **The intrinsic-bound thesis — why this approach matters**
>
> "We exploit a tighter intrinsic bound: storing F facts requires at least F/(bits per parameter) weights, so measuring how much a model **knows** lower-bounds how many parameters it **has**." [Source: arXiv 2604.24827 abstract, p.1]

> **The decomposition of model parameters — the load-bearing theoretical move**
>
> "We decompose model parameters into three functional roles: N = N_fact + N_proc + N_ling, where N_fact is the share devoted to storing specific factual associations (entity attributes, dates, names), N_proc is the share devoted to procedural skills (reasoning, parsing, instruction following, tool use), and N_ling is the share devoted to linguistic competence (syntax, morphology, vocabulary, register). The Densing Law improves the efficiency of N_proc and N_ling, freeing capacity for N_fact or allowing smaller total N. But N_fact is bounded below by the information content of stored facts. IKPs exclusively probe N_fact, which provides a lower bound on N." [Source: arXiv 2604.24827 §3.3, p.6]

> **The Densing-Law refutation — the headline empirical finding**
>
> "Across 96 dated open-weight models the time coefficient on IKP accuracy is −0.0010/month (95% CI [−0.0031, +0.0008]) — indistinguishable from zero, and rejecting the Densing prediction of +0.0117/month at p < 10⁻¹⁵. Benchmark saturation is therefore not evidence that scaling has ended — it is evidence that benchmarks have stopped measuring the part of scaling that cannot compress. Factual capacity continues to grow log-linearly with parameters as a function of total parameter count." [Source: arXiv 2604.24827 §1, p.2]

> **MoE total-vs-active rule — the operational finding for deployment**
>
> "For Mixture-of-Experts models, total parameters predict knowledge (R² = 0.79) far better than active parameters (R² = 0.51). … total (not active) parameters predict MoE knowledge capacity." [Source: arXiv 2604.24827 §1 contribution-4, p.3-4]

> **Knowledge fingerprinting — the silent-swap-detector primitive**
>
> "Combining rare-fact Jaccard overlap with **hallucination similarity** (the rate at which two models produce the same wrong answer on rare facts) yields a training-free test that distinguishes weight-sharing siblings, post-training lineages, and full retrains — including across closed-vendor version families — without requiring model weights." [Source: arXiv 2604.24827 §1 contribution-5, p.4]

> **The personal-anecdote framing — why factual capacity in particular matters to expert users**
>
> "In May 2024, GPT-4o knew the contest existed but invented fake challenge names when asked. Just nine months later, in February 2025, Claude 3.7 Sonnet listed nineteen verified Hackergame 2023 titles, verifiable against the official writeup repository. By April 2026, Kimi K2.6, Claude Opus 4.7 and Gemini 3.1 Pro list specific challenges from multiple consecutive years. … This is not a quirk of one event. Transformer feed-forward layers function as key-value memories for factual associations, with an empirical storage capacity of ~2–4 bits of factual knowledge per parameter." [Source: arXiv 2604.24827 §1 opening, p.1]

> **The "compressed image of expert discourse" framing**
>
> "Frontier foundation models have become compressed images of the expert discourse of their era. Human experts work in the open — papers, code, talks, documentation — and each successive training run distills more of that output into parameters. Over time, the useful knowledge of entire research communities (which ideas matter, who produced them, what artifacts they built) flows from the long tail of the open web into a handful of proprietary models." [Source: arXiv 2604.24827 §1, p.2]
