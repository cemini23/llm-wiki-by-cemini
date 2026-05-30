---
title: "Learning to Orchestrate Agents in Natural Language with The Conductor (Sakana AI, ICLR 2026)"
type: source
tags: [source, paper, rl-marl, llm-agents, ml-methods, iclr-2026, orchestration, grpo]
keywords: [conductor, sakana-ai, grpo, llm-orchestration, recursive-topology, dynamic-worker-pool, rl-trained-orchestrator, qwen2.5-7b, mixture-of-agents, masrouter, scatter-gather-alternative]
clusters: [rl-marl, llm-agents]
related:
  - concepts/rl-marl-research.md
  - concepts/llm-agent-systems.md
  - concepts/scatter-gather-topology.md
  - entities/infrastructure/deepseek-api.md
  - entities/frameworks/langgraph.md
  - entities/infrastructure/sakana-fugu.md
  - sources/sakana-trinity-llm-coordinator.md
  - concepts/ai-organisation-design.md
  - sources/omc-talent-container-paper.md
  - sources/matching-accuracy-different-geometry-es-grpo.md
  - sources/sia-self-improving-ai-harness-weight-updates-2026-05-30.md
  - concepts/policy-distillation.md
  - sources/4-3-link-research.md
  - sources/co-evolving-policy-distillation-2604.27083.md
  - sources/eggro-evolution-strategies-hyperscale-2026.md
maturity: validated
read_status: read
created: 2026-04-27
updated: 2026-05-15
---

## Relations

- @concepts/rl-marl-research.md — primary cluster hub; the paper is fundamentally an RL-trained-orchestrator contribution (GRPO on Qwen2.5-7B base) and a heterogeneous-multi-agent-coordination contribution (variable worker pools, recursive self-extension); slots in among the rl-marl cluster's frontier-trading-relevant orchestration literature
- @concepts/llm-agent-systems.md — secondary cluster hub; the *application* layer is LLM agent orchestration (the Conductor designs communication topologies + prompt-engineers worker LLMs); the workers used (Gemma3-27B, Qwen3-32B, R1-Distill-Qwen-32B, Claude Sonnet 4, Gemini 2.5 Pro, GPT-5) are the same frontier-LLM zoo this hub indexes
- @concepts/scatter-gather-topology.md — direct architectural counterpart; **the Conductor offers an RL-trained alternative to manually-designed agentic workflows** like Cemini's prescribed LangGraph scatter-gather. Where the 3-19 source prescribes a hand-designed `Send()`-based fan-out + `operator.add` reducer + gather pattern, the Conductor *learns* topology design as a per-task decision; relevant to the open Option A vs Option B P1 ticket on that page (build Send() topology fresh vs. retain linear deployed StateGraph as IP-sale narrative)
- @entities/infrastructure/deepseek-api.md — the Conductor evaluates DeepSeek-R1-Distill-Qwen-32B as one of its open-source worker LLMs (Table 3, Section A.2); overlaps with Cemini's intended DeepSeek-family brain via the hosted API path. The Conductor framework would treat the Cemini DeepSeek client as a worker pool entry, not a per-node analyst
- @entities/frameworks/langgraph.md — the operative orchestration framework in the Cemini stack; the Conductor's contribution would replace the *design-by-hand* of LangGraph topologies with a *learned-by-RL* meta-controller that emits worker assignments + natural-language prompts at runtime. Compatible with LangGraph's typed-state-graph substrate but reframes the role of the supervisor node
- @entities/infrastructure/sakana-fugu.md — **the commercial productization of this paper** (announced `sakana.ai/fugu-beta/`, 2026-04-24 — three days after this source page was created and ~7 weeks after the paper's arXiv finalization 2026-03-01). Fugu wraps the Conductor methodology + the sibling ICLR 2026 *Trinity* paper behind an OpenAI-compatible chat-completions API in a two-tier lineup (Fugu Mini 🐟 latency-optimized / Fugu Ultra 🐡 full orchestration). Materializes the Cemini-relevance read on this source page from "research direction worth tracking" to "API surface that an institutional buyer will ask why Cemini didn't just call." See that page for the IP-sale narrative impact + the new Option C added to the @concepts/scatter-gather-topology.md P1 ticket
- @sources/sakana-trinity-llm-coordinator.md — **direct sibling paper** (ingested 2026-04-28). Same six authors, same Sakana AI + UMich + Inst Sci Tokyo institutional mix, same ICLR 2026 venue, neighboring arXiv submission (Trinity 2512.04695 vs Conductor 2512.04388 — same week of December 2025). Methodologically complementary: where this paper trains a 7B Qwen2.5-7B-base meta-controller with **GRPO (RL)**, Trinity trains a 0.6B SLM + ~10K-param head (<20K total learnable params) with **separable Covariance Matrix Adaptation Evolution Strategy (sep-CMA-ES)** — derivative-free, deliberately not RL. Trinity formalizes orchestration as Thinker/Worker/Verifier multi-turn role assignment (vs Conductor's free-form natural-language topology design); the Trinity poster reports REINFORCE collapses on LCB (0.253) under the binary-reward + weak-coupling regime where sep-CMA-ES dominates (0.615). Both papers jointly productized as Sakana Fugu — Trinity is the likely Fugu Mini basis (lightweight + low-latency), Conductor the Fugu Ultra basis (heavyweight + full-orchestration)

## Raw Concept

- **Original title**: "Learning to Orchestrate Agents in Natural Language with The Conductor"
- **Authors**: Stefan Nielsen, Edoardo Cetin, Peter Schwendeman, Qi Sun, Jinglue Xu, Yujin Tang
- **Affiliations**: Sakana AI; University of Michigan; Institute of Science Tokyo
- **Venue**: ICLR 2026 (conference paper, accepted)
- **arXiv**: 2512.04388v4 (1 Mar 2026)
- **Type**: PDF
- **Location**: `research for cemini/sakana-conductor-rl-orchestration-iclr-2026.pdf`
- **Retrieved**: 2026-04-27 (user-dropped into `research to be indexed/`, moved to canonical location during ingest)
- **Pages / length**: 39 pages (12 main + references + appendix A on training/evaluation/dataset details)
- **Read status**: `read` — abstract + introduction + methods (Sections 1–3.2) + experiments (Section 4.1–4.5) + related work + discussion + acknowledgements + author contributions + Appendix A.1 training setup + A.2 datasets + A.3 evaluation setup. Appendix beyond A.3 not yet read but covers extended ablations + per-task breakdowns.
- **Why it's in the corpus**: User-flagged as "really good worth a read" 2026-04-27. Direct architectural relevance to Cemini's scatter-gather LangGraph orchestration prescription; Sakana AI is a known frontier-research lab whose evolutionary-search + small-model methodology aligns with Cemini's own efficiency-first posture.

## Narrative

### One-paragraph abstract

The Conductor is a 7B-parameter LLM (initialized from Qwen2.5-7B) trained with **Group Relative Policy Optimization (GRPO)** to act as a meta-controller over a heterogeneous pool of frontier worker LLMs (Gemma3-27B, Qwen3-32B, DeepSeek-R1-Distill-Qwen-32B, Claude Sonnet 4, Gemini 2.5 Pro, GPT-5). At inference time, given a task prompt, the Conductor (a) selects which worker(s) to invoke, (b) designs the communication topology between them in natural language, and (c) prompt-engineers per-worker instructions. A **recursive Conductor variant** can select itself as a worker, unlocking a new test-time-scaling axis. Reported state-of-the-art results on **LiveCodeBench (83.93), GPQA-Diamond (87.5), AIME25 (93.3), MMLU (94.1), MATH500 (99.4), BigCodeBench (37.86)** — average **77.27 vs GPT-5's 74.78** in the unconstrained setting. Trained on **2× NVIDIA H100 80GB GPUs** for 200 iterations with 4 questions per iteration and 64 rollouts per question. The headline finding: **a small, RL-trained meta-controller can outperform the largest single frontier model in its worker pool by orchestrating it intelligently**, and this happens with modest training compute.

### Cemini-relevance read

The Conductor is the **first paper in the Cemini corpus to propose RL-training the orchestration layer itself, not the worker pool**. Cemini's existing rl-marl cluster (86 sources before this ingest, 87 after) is dominated by:

1. **MAPPO-on-trading-environments papers** — RL applied at the *trader-agent* layer (technical, fundamental, sentiment, risk subagents each carry an MAPPO-trained policy).
2. **Hand-designed orchestration scaffolds** — LangGraph supervisor patterns, scatter-gather topologies, mixture-of-agents (MoA) ensembles where the topology is fixed by the engineer.

The Conductor inverts this: keep the workers as off-the-shelf frontier LLMs (no fine-tuning of the worker pool), train *the meta-controller that decides worker assignment + topology design* with RL. For the Cemini stack this maps directly onto the open `@concepts/scatter-gather-topology.md` Option A vs Option B P1 ticket:

- **Option A (build Send() topology fresh per step83 spec)** — manually-designed, ~1–2 engineer-weeks. The Conductor approach would be a research-direction extension of Option A: train a small meta-controller to *emit* the Send() fan-out at runtime rather than hard-code it in `agents/orchestrator.py`.
- **Option B (retain linear 4-analyst StateGraph as IP-sale narrative)** — the Conductor result is **strong evidence that a learned orchestrator beats a hand-designed one**, which slightly weakens the "deployed-linear-is-fine-as-IP-sale-narrative" framing. An institutional buyer reading the Conductor paper would expect the acquired stack to support a Conductor-style learned-meta-controller as a future research thread, not just be locked into the deployed linear StateGraph.

**Compatibility with the deployed DeepSeek API path**: the Conductor framework treats heterogeneous worker LLMs as black-box pool entries (it natural-language-prompts each worker, then aggregates the natural-language responses). Cemini's hosted-DeepSeek client at `services/llm_analyst/deepseek_client.py` would be a worker pool entry in this framing, not an analyst node — the Conductor would *decide* whether to call DeepSeek-Reasoner, GPT-4.1, Claude, Gemini, etc. for each scatter-gather slice. This is more flexible than the deployed pattern (single shared DeepSeek client across all 4 analyst nodes) and is the kind of architectural lift an institutional buyer's GPU-cluster engineer would do post-acquisition.

### Methodology highlights

1. **GRPO formulation** — uses Group Relative Policy Optimization (Shao et al. 2024, the DeepSeekMath paper). Variant of PPO where rewards are normalized within a group of rollouts for the same question, eliminating the value-function critic and reducing memory.
2. **Adaptive worker pool** — workers can be added/removed without retraining. Demonstrated by **OOD few-shot prompting** (Table 4): when Conductor sees few-shot examples drawn from unseen tasks, performance *increases* (LiveCodeBench: 58.32 in-distribution → 64.29 OOD, MATH500: 88.20 → 89.33). Interpretation: the meta-controller learned a generalizable *task-routing skill*, not memorized task-specific dispatching.
3. **Recursive Conductor** — a second training stage (20 iterations on a 350-sample filtered subset of LCB+RLPR) lets the Conductor select **itself** as a worker. The recursive variant is given the previous worker's response as additional context. A discount factor of 0.25 scales rewards in the initial non-recursive round; rewards normalized across rounds. **AIME25: 66.67, BCB: 40.0, GPQA-D: 82.32** in the constrained-setting recursive variant (different table than the unconstrained headline — Sec 4.3).
4. **Constrained vs unconstrained** — two evaluation regimes: constrained = 4096 output tokens, minimum reasoning budgets (matches training); unconstrained = max reasoning budgets per worker (Table 3 shows GPT-5 at 128K tokens / "high" reasoning, Claude Sonnet 4 at 64K + 32K reasoning, etc.). The unconstrained-setting headline numbers (LCB 83.93, GPQA-D 87.5, AIME25 93.3, etc.) are what beats GPT-5's 74.78 average.
5. **Compute envelope** — Conductor training runs on **2× NVIDIA H100 80GB GPUs**. Modest by frontier standards. Inference cost is *higher* than single-model inference (multiple worker calls per task) but the per-task quality lift makes the cost-quality frontier favorable.

### Author / institutional read

- **Sakana AI** is the lead institution. Known for evolutionary model-merging research, Nature paper on LLM-driven scientific discovery (2024), and a small-model + clever-orchestration thesis that aligns with the Conductor result.
- **University of Michigan + Inst Sci Tokyo** are minor co-author affiliations (Schwendeman, Sun, Xu).
- **Yujin Tang** is the senior author at Sakana — known for prior work on neural cellular automata + RL for evolutionary algorithms.

The Sakana lineage matters for the Cemini IP-sale read: an institutional buyer's research-org would recognize Sakana's small-model + orchestration thesis as a credible long-term direction, and the Conductor is the kind of academic anchor a Cemini-derivative product line could legitimately cite.

### Productization (Fugu, 2026-04-24 closed beta) — added 2026-04-27

Three days after this source page was first written, Sakana announced **Sakana Fugu** at `sakana.ai/fugu-beta/` — the commercial productization of *both* the Conductor paper and a previously-unindexed sibling paper, **TRINITY: An Evolved LLM Coordinator** (Xu, Sun, Schwendeman, Nielsen, Cetin, Tang — same six authors as Conductor, different lead ordering). The full entity catalog is at `@entities/infrastructure/sakana-fugu.md`; the relevant impact-on-this-source items are:

1. **Time-to-product**: ~7 weeks from arXiv finalization (2026-03-01) to closed-beta API launch (2026-04-24). Suggests Sakana ran productization in parallel with the academic submission, not after — which compresses the typical "interesting research, but how do I use it" gap that kills most academic multi-agent results
2. **Two-tier API**: Fugu Mini 🐟 (latency-optimized) + Fugu Ultra 🐡 (full orchestration). The Mini variant acknowledges the latency cost of full pool fan-out; the Ultra variant is the full Conductor methodology
3. **Forward-dated frontier benchmarks**: Fugu beats Gemini 3.1 (high), GPT 5.4 (high), Opus 4.6 (max) on GPQAD (95.1 vs 94.4 best), LCBv6 (93.2 vs 92.4 best), SWEPro (54.2 vs 53.4 best). These are 2026-release-calendar models — not the GPT-5 / Claude Sonnet 4 / Gemini 2.5 Pro pool the original paper benchmarked
4. **Trinity sibling paper not yet in this corpus** — the Sakana publications list surfaces *TRINITY: An Evolved LLM Coordinator* as the second paper underlying Fugu. Likely arXiv 2512.04695 (range neighbor to Conductor's 2512.04388). The "evolved coordinator" framing suggests evolutionary search methodology — fits Sakana's broader research lineage (evolutionary model merging, ShinkaEvolve, AB-MCTS) and would close a coverage gap. Open ingest decision pending user confirmation
5. **OpenAI-compatible endpoint** = swap-out is ~5 lines of config from Cemini's existing DeepSeek client pattern. The Cemini-relevance read on this page is now operationally actionable, not just architecturally interesting

### Open questions / NEEDS-VERIFICATION items

- **[RESOLVED 2026-05-10 — NOT OPEN SOURCE]** Conductor codebase, training data, and model weights are NOT publicly released. arXiv v2 (2512.04388v2) stated "we share the codebase of our new framework with this submission" and "provide source code in the supplementary material along with our trained model weights in an anonymized external repository." However, arXiv v5 (latest, 2512.04388v5) drops this claim — reproducibility statement only says "Our base model and all datasets are publicly available." TechieTricks article (2026-05-07) confirms: "the 7B model described in the research paper was an exploratory blueprint and is not publicly available." No public Sakana AI GitHub repo for Conductor exists (sakanaai org has 46 repos, none for Conductor or Trinity). Direct experimentation path is closed; Fugu API remains the only access vector.
- **[NEEDS VERIFICATION 2026-05-10]** Whether the recursive-Conductor variant is competitive on time-budget vs sequential frontier-model invocation. Exa cross-check 2026-05-10: no latency benchmarks published. Table comparisons remain token-count + accuracy axes only.
- **[NEEDS VERIFICATION 2026-05-10]** Compatibility with structured-output / function-calling worker LLMs. Exa cross-check 2026-05-10: no new information. Cemini's analyst nodes return Pydantic-typed StrategyRecommendation objects, not free-form text. The paper's experiments are on math + code + multiple-choice — all natural-language-output tasks. Lifting to typed-output workers may require additional architectural work.
- **[RESOLVED 2026-04-28 — Trinity ingested]** Trinity sibling paper confirmed at arXiv 2512.04695 (Xu, Sun, Schwendeman, Nielsen, Cetin, Tang. *TRINITY: An Evolved LLM Coordinator*. ICLR 2026). Ingested as `@sources/sakana-trinity-llm-coordinator.md` 2026-04-28 with full poster captured verbatim + arXiv abstract + 10 Snippets + Cemini-relevance read mapping Trinity onto the Fugu Mini / Conductor onto Fugu Ultra. Sakana research lineage coverage now closes; Fugu-productization documentation is complete from both academic-paper sides.

## Snippets

### S1 — Headline result (paper abstract / Table 1, paraphrased from pages 1–6)

> Conductor (7B, RL-trained on Qwen2.5-7B) achieves average **77.27** across LiveCodeBench (83.93), GPQA Diamond (87.5), AIME25 (93.3), MMLU (94.1), MATH500 (99.4), and BigCodeBench (37.86) — outperforming GPT-5's average of **74.78** and beating every individual worker model in its pool, including Claude Sonnet 4, Gemini 2.5 Pro, R1-Distill-Qwen-32B, Qwen3-32B, and Gemma3-27B.

*— Section 4.2 (in-domain unconstrained results), pages 6–8. Conductor as meta-controller beats every frontier worker in its pool by orchestrating them.*

### S2 — Recursive Conductor extends test-time scaling (Section 3.2, page 5)

> The recursive Conductor variant allows the model to select itself as a worker, passing the previous round's worker response as additional context. Trained for 20 iterations on a 350-sample filtered subset (175 LCB + 175 RLPR) with a discount factor of 0.25 on the initial round and rewards normalized across rounds. Reaches **AIME25: 66.67, BCB: 40.0, GPQA-D: 82.32** in the constrained-setting (4096 tokens, minimum reasoning budgets).

*— Section 3.2 + Section 4.4 + Appendix A.1, page 5 + page 9 + page 15. The recursive variant unlocks a new test-time-scaling axis distinct from the worker-pool-size axis.*

### S3 — Adaptive worker pool via OOD few-shot prompting (Table 4, page 17)

> Conductor performance is *increasing* in the proportion of few-shot examples drawn from unseen tasks. LiveCodeBench: 58.32 (in-distribution) → 64.29 (OOD-only). MATH500: 88.20 → 89.33. MMLU: 92.31 → 93.14. Interpretation: the meta-controller learned a generalizable task-routing skill, not memorized task-specific dispatching.

*— Table 4 + Appendix A.3, page 17. Evidence the Conductor's worker-routing competence is OOD-generalizable.*

### S4 — Training compute envelope (Appendix A.1, page 15)

> "We train our Conductor on 2 NVIDIA H100 80GB GPUs."
> Setup: Qwen2.5-7B base, max completion length 1024, 200 iterations, 4 questions per iteration, 64 rollouts per question, AdamW optimizer (β1=0.9, β2=0.999, ε=0.2), base LR 1e-6 with cosine scheduling + 0.03 warmup ratio, no reference model sync, KL penalty disabled.

*— Appendix A.1 (Training Setup), page 15. Modest training compute by frontier standards — 2× H100 + 200 GRPO iterations.*

### S5 — Worker pool composition (Table 3 + Section 4.1, pages 6 + 15)

> Worker pool: **Gemini Pro 2.5** (65535 max tokens / 32768 reasoning), **Claude Sonnet 4** (64000 / 32768), **GPT-5** (128000 / "high" reasoning), **R1-Distill-Qwen-32B** (20480 tokens, no reasoning budget), **Gemma-3-27B-it** (20480), **Qwen3-32B (thinking)** (20480, thinking enabled), **Qwen3-32B** (non-thinking, 20480).

*— Table 3, page 15. The heterogeneous worker pool spans closed-frontier (GPT-5, Claude Sonnet 4, Gemini 2.5 Pro) + open-frontier (R1-Distill-Qwen-32B, Qwen3-32B, Gemma3-27B). Cemini's intended DeepSeek-Reasoner brain is the same model family as R1-Distill-Qwen-32B in Sakana's pool.*

### S6 — Multi-agent baselines compared (Section A.3 baselines, page 16)

> "Within the constrained setting, we evaluate against state-of-the-art multi-agent routing and scaffolding techniques, including **MasRouter** (Yue et al., 2025), **RouterDC** (Chen et al., 2024), **Smoothie** (Guha et al., 2024), and **MoA** (Wang et al., 2024)."

*— Appendix A.3 (Evaluation Setup), page 16. Conductor benchmarked against MoA (Mixture-of-Agents) and three learned-router baselines — these are the most direct prior-art comparisons; Conductor wins on every benchmark.*

### S7 — Commercial productization (Sakana announcement, 2026-04-24, ~7 weeks post arXiv finalization)

> "Sakana Fugu models are based on our ICLR 2026 papers (Trinity and Conductor), and we have substantially further improved the methods to increase the performance and user experience, to be offered as a commercial product."

*— `sakana.ai/fugu-beta/`, retrieved 2026-04-27. Direct vendor-side confirmation that the Conductor methodology in this source page is now (a) commercialized as a closed-beta API and (b) productized jointly with a sibling ICLR 2026 paper (Trinity) not yet in this corpus. Operationalizes the Cemini-relevance read above from "future direction" to "live API surface" — see `@entities/infrastructure/sakana-fugu.md` for the full productization page.*
