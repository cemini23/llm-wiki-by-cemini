---
title: "TRINITY: An Evolved LLM Coordinator (Sakana AI, ICLR 2026)"
type: source
tags: [source, paper, rl-marl, llm-agents, ml-methods, iclr-2026, orchestration, evolutionary-strategy, sep-cma-es]
keywords: [trinity, sakana-ai, sep-cma-es, evolutionary-strategy, llm-coordinator, lightweight-coordinator, slm-coordinator, thinker-worker-verifier, livecodebench-sota, conductor-sibling, fugu-mini]
clusters: [rl-marl, llm-agents]
related:
  - concepts/rl-marl-research.md
  - concepts/llm-agent-systems.md
  - concepts/scatter-gather-topology.md
  - entities/infrastructure/deepseek-api.md
  - entities/frameworks/langgraph.md
  - entities/infrastructure/sakana-fugu.md
  - sources/sakana-conductor-rl-orchestration.md
  - concepts/ai-organisation-design.md
  - sources/omc-talent-container-paper.md
maturity: validated
read_status: read
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @concepts/rl-marl-research.md — primary cluster hub *with caveat*: Trinity sits in the broader trial-and-error-trained-orchestration family the rl-marl hub indexes, but its *training mechanism is explicitly anti-RL*. The paper argues REINFORCE gradients are low-SNR under binary rewards + weak parameter coupling (Section: Why Evolutionary Strategy?), and chooses **separable Covariance Matrix Adaptation Evolution Strategy (sep-CMA-ES)** as a derivative-free alternative. Trinity is the corpus's first ES-trained-coordinator entry and a useful counterweight to the rl-marl cluster's RL-default framing
- @concepts/llm-agent-systems.md — secondary cluster hub; the *application* layer is LLM agent orchestration (the Trinity coordinator selects which LLM to call + assigns it a Thinker/Worker/Verifier role); the workers compared in the OOD evaluation (Gemini 2.5-Pro, GPT-5, Claude-4-Sonnet) overlap with Conductor's worker pool and with the broader frontier-LLM zoo this hub indexes
- @concepts/scatter-gather-topology.md — direct architectural counterpart, *with a different mechanism than Conductor*. Where Conductor uses a 7B GRPO-trained meta-controller to design topologies, Trinity uses a 0.6B SLM + ~10K-param head trained with sep-CMA-ES to assign role-tagged delegations across multiple turns. Both are alternatives to the manually-designed LangGraph scatter-gather Cemini deploys; Trinity's compute envelope (<20K learnable parameters) is dramatically lighter than Conductor's, which matters for the open Option A/B/C P1 ticket on that page
- @entities/infrastructure/deepseek-api.md — Trinity's ablation tables benchmark against frontier closed-API models (Gemini 2.5-Pro, GPT-5, Claude-4-Sonnet) but the worker-pool composition is not as fully enumerated as Conductor's Table 3. The DeepSeek-family path is implicit (Conductor's worker pool included R1-Distill-Qwen-32B, and Trinity is a sibling paper from the same authors), but the explicit Trinity poster doesn't enumerate it. Cross-link kept lightweight
- @entities/frameworks/langgraph.md — same architectural-comparison framing as Conductor: Trinity replaces *design-by-hand* of LangGraph topologies with a *learned-by-ES* meta-controller. The Trinity-specific lift over Conductor: per-turn role assignment (Thinker/Worker/Verifier) is more structured than Conductor's free-form natural-language prompt design — easier to map onto LangGraph's typed-state-graph substrate, where each role becomes a typed-output schema
- @entities/infrastructure/sakana-fugu.md — **the commercial productization of this paper alongside the Conductor sibling**. Sakana's Fugu announcement (2026-04-24, `sakana.ai/fugu-beta/`) explicitly names *both* "Trinity and Conductor" as the underlying ICLR 2026 papers, with the two-tier API (Fugu Mini 🐟 latency-optimized / Fugu Ultra 🐡 full orchestration). Trinity's lightweight-coordinator + low-parameter-count framing strongly suggests it's the basis for **Fugu Mini**, while Conductor's heavier 7B-meta-controller framing fits **Fugu Ultra**. See that entity page for the productization narrative + the new Option C added to the @concepts/scatter-gather-topology.md P1 ticket (outsource orchestration to Fugu rather than build Send() topology in-house)
- @sources/sakana-conductor-rl-orchestration.md — **direct sibling paper**: same six authors (Stefan Nielsen, Edoardo Cetin, Peter Schwendeman, Qi Sun, Jinglue Xu, Yujin Tang — different lead ordering: Nielsen leads Conductor; Xu+Sun lead Trinity), same Sakana AI + UMich + Inst Sci Tokyo institutional mix, same ICLR 2026 venue, same arXiv release window (Conductor 2512.04388, Trinity 2512.04695 — neighboring submissions, same week of December 2025). The two papers are **methodologically complementary, not redundant**: Conductor = larger meta-controller + RL training + free-form natural-language topology design; Trinity = smaller meta-controller + ES training + structured Thinker/Worker/Verifier role assignment. Both productized as Fugu

## Raw Concept

- **Original title**: "TRINITY: An Evolved LLM Coordinator"
- **Subtitle (poster)**: "A Lightweight Coordinator Orchestrating Multiple LLMs via Evolutionary Strategy"
- **Authors**: Jinglue Xu (Sakana AI), Qi Sun (Sakana AI + Institute of Science Tokyo), Peter Schwendeman (University of Michigan), Stefan Nielsen (Sakana AI), Edoardo Cetin (Sakana AI), Yujin Tang (Sakana AI)
- **Lead authors**: Jinglue Xu + Qi Sun (joint first authors, marked `*` in poster)
- **Senior author**: Yujin Tang (Sakana AI)
- **Affiliations**: Sakana AI, Japan; University of Michigan, USA; Institute of Science Tokyo, Japan
- **Venue**: ICLR 2026 (conference paper, accepted)
- **arXiv**: 2512.04695 (cs.LG; v1 4 Dec 2025; v2 2 Mar 2026)
- **Type**: PDF (poster captured verbatim; full paper not yet pulled — 22 pages on arXiv)
- **Location**: not yet downloaded into `research for cemini/`; ingested 2026-04-28 from arXiv abstract + Sakana-hosted poster PDF (`https://sakana.ai/assets/fugu-beta/TRINITY_poster.pdf`)
- **Retrieved**: 2026-04-28 (user-authorized ingest as follow-up to Sakana Fugu cataloguing 2026-04-27)
- **Pages / length**: arXiv preprint listed as 10,638 KB (v2); poster is the read artifact at the moment, ~1 page dense ICLR poster format
- **Read status**: `read` — full poster captured verbatim including the four numerical results tables (sep-CMA-ES vs alternatives / in-distribution / OOD zero-shot transfer / ablations) + the abstract from arXiv. Full 22-page paper deferred — poster + abstract are sufficient for the librarian-side cataloguing pass; the academic depth a deep-read would add (the formal block-epsilon-separability theorem + the multi-turn dynamics analysis) is not the load-bearing axis for the Cemini-relevance read on this page.
- **Why it's in the corpus**: Surfaced via the 2026-04-24 Sakana Fugu announcement (`sakana.ai/fugu-beta/`) as the second of two ICLR 2026 papers the Fugu commercial API productizes. User-authorized ingest 2026-04-28 to close the productization-narrative coverage gap left open in the Conductor source page + the Sakana Fugu entity page (where Trinity was flagged as `[NEEDS VERIFICATION 2026-04-27]` in three places).

## Narrative

### One-paragraph abstract

Trinity is a **lightweight LLM coordinator** built from a 0.6B-parameter SLM plus a ~10K-parameter head — total **<20K learnable parameters** — trained with **separable Covariance Matrix Adaptation Evolution Strategy (sep-CMA-ES)** to orchestrate a heterogeneous pool of frontier LLMs. At each turn the coordinator reads the full multi-turn transcript, selects an LLM, and assigns it one of three roles: **Thinker** (strategize), **Worker** (execute), or **Verifier** (evaluate). The process halts when the Verifier accepts the solution. Trinity achieves **86.2% pass@1 on LiveCodeBench V6** — beating GPT-5 (83.8%) and Gemini 2.5-Pro (67.2%) — and **outperforms all single-model and multi-agent baselines on 8 benchmarks** (4 in-distribution: LCB, MATH, MMLU, RLPR; 4 zero-shot held-out: AIME, BCB, MT-B, GPQA — average 54.2 vs GPT-5's 51.1 and Gemini 2.5-Pro's 52.3). The headline methodological finding: **under high dimensionality + binary rewards + weak parameter coupling, sep-CMA-ES dominates RL (REINFORCE), supervised fine-tuning, and random search**, exploiting block-epsilon-separability of the parameter space. Conclusion: "engineering collaborative AI ecosystems rather than scaling monolithic models."

### Cemini-relevance read

Trinity is the **second paper in the Cemini corpus to propose training the orchestration layer itself**, alongside its sibling Conductor (`@sources/sakana-conductor-rl-orchestration.md`). The two papers share six authors and the Fugu productization, but make **methodologically complementary architectural choices** that together stake out the corner of the design space the Cemini scatter-gather topology lives in:

| Dimension | Conductor | Trinity |
|---|---|---|
| Coordinator size | 7B (Qwen2.5-7B base) | 0.6B SLM + ~10K head (<20K total learnable params) |
| Training method | GRPO (RL) | sep-CMA-ES (evolutionary strategy) |
| Topology output | Free-form natural-language prompts + worker assignment | Structured Thinker/Worker/Verifier role assignment per turn |
| Pool composition (paper) | Gemma3-27B + Qwen3-32B + R1-Distill-Qwen-32B + Claude Sonnet 4 + Gemini 2.5 Pro + GPT-5 | Compared to Gemini 2.5-Pro, GPT-5, Claude-4-Sonnet (full pool not enumerated in poster) |
| LCB result | 83.93 (in-distribution) | 86.2 (in-distribution V6) |
| Test-time scaling axis | Recursive Conductor (selects itself as worker) | Multi-turn dynamics + role re-assignment |
| Compute (training) | 2× H100 80GB, 200 iterations × 4 questions × 64 rollouts | ~1.5K–40K evaluations for ~10K parameters |
| Likely Fugu mapping | Fugu Ultra 🐡 (full orchestration) | Fugu Mini 🐟 (latency-optimized) |

For the Cemini stack, Trinity adds a **structured-output orchestration option** that Conductor doesn't directly provide. Cemini's existing analyst nodes return Pydantic-typed `StrategyRecommendation` objects, not free-form text — Conductor's free-form natural-language prompts would require an additional structured-output layer to slot into the LangGraph supervisor pattern, while Trinity's Thinker/Worker/Verifier role schema is **closer to a typed-state-graph contract**. The Verifier role specifically maps onto a class of guardrail/risk-checker subagents Cemini's prescribed scatter-gather topology already wants — Trinity formalizes this as a first-class role with explicit accept/reject semantics that halts the multi-turn loop.

The **Option C** Cemini-relevance read on `@entities/infrastructure/sakana-fugu.md` (outsource orchestration to Fugu rather than build Send() topology in-house) gets sharper with Trinity in the corpus: Fugu Mini (Trinity-based) gives a low-latency lightweight-coordinator path, Fugu Ultra (Conductor-based) gives a heavyweight full-orchestration path, and the Cemini operator can choose per-task without fine-tuning either coordinator.

### Methodology highlights

1. **0.6B SLM + 10K-param head** — the SLM is the encoder; its hidden states (after singular-value fine-tuning) feed a tiny MLP head that outputs the LLM-selection + role-assignment distribution. Total learnable parameters <20K — orders of magnitude smaller than the worker LLMs being coordinated.
2. **Three roles, multi-turn dynamics** — Thinker (high-level strategy), Worker (execution), Verifier (correctness check). The Verifier's accept-reject decision is the loop-termination signal. Ablation: removing the Tri-role decomposition costs **3.4 average points** (70.4 → 67.0).
3. **Singular-value fine-tuning of the SLM** — the SLM's parameters are not fully trained; only the singular values of selected weight matrices are adapted. Ablation: removing this costs **2.5 average points** (70.4 → 67.9). Keeps the learnable-parameter count low and preserves the SLM's pretrained representations.
4. **Hidden-state-based selection beats last-token** — the coordinator pools hidden states across the full transcript rather than reading off the last token. Ablation: switching to last-token costs **5.7 average points** (70.4 → 64.7). The most consequential ablation — suggests the rich-contextualization claim from the abstract is empirically load-bearing.
5. **Why ES beats RL/SFT/random search** — formal argument: the loss landscape exhibits block-epsilon-separability (parameters cluster into roughly-independent groups). sep-CMA-ES's diagonal covariance matches this structure; REINFORCE's policy-gradient suffers low-SNR under binary rewards + weak coupling; SFT requires `O(74·35)` multi-turn label generation per training question (combinatorially infeasible). Numerical comparison (LCB / MATH / MMLU / RLPR): REINFORCE 0.253 / 0.459 / 0.500 / 0.266 vs sep-CMA-ES **0.615 / 0.880 / 0.916 / 0.401**.
6. **Compute envelope** — only ~1.5K–40K function evaluations for ~10K parameters. Each evaluation is a full multi-turn LLM rollout (expensive in worker-API calls, not in coordinator gradient compute). Improvement scales linearly with iterations (vs. logarithmic for random search).

### Author / institutional read

- **Jinglue Xu + Qi Sun** are joint first authors. Both at Sakana AI; Sun also affiliated with Institute of Science Tokyo. Different lead-author pair than Conductor (where Stefan Nielsen leads).
- **Yujin Tang** is the senior author at Sakana — same as Conductor. Continued thread of Tang's small-model + clever-orchestration research lineage at Sakana (also includes evolutionary model merging, ShinkaEvolve, AB-MCTS).
- **Stefan Nielsen + Edoardo Cetin + Peter Schwendeman** are the connective-tissue co-authors across Conductor and Trinity. Suggests the two papers were developed in parallel as a methodologically-bifurcated research program rather than sequentially.

The lead-author shift (Nielsen → Xu+Sun) signals **distinct project ownership** even though the broader research program is shared. The arXiv submission dates are tightly clustered (2512.04388 vs 2512.04695, same week of December 2025), and the joint Fugu productization confirms they were always intended as a complementary pair.

### Productization context

Trinity's role in the Sakana Fugu commercial API (`@entities/infrastructure/sakana-fugu.md`):

1. **Fugu Mini 🐟** is most likely Trinity-based given Trinity's lightweight-coordinator + low-latency framing. The Sakana announcement explicitly names *both* Trinity and Conductor as the underlying ICLR 2026 papers; the two-tier API split (Mini latency / Ultra full-orchestration) maps cleanly onto the two papers' compute-envelope split (Trinity <20K params / Conductor 7B params).
2. **Forward-dated frontier benchmarks on Fugu** (vs Gemini 3.1 high / GPT 5.4 high / Opus 4.6 max) are *not* the same numbers as Trinity's poster (vs Gemini 2.5-Pro / GPT-5 / Claude-4-Sonnet). The Fugu benchmarks reflect "substantially further improved methods" per the Sakana announcement — the academic Trinity numbers are the ICLR-cited foundation, but the API surface is later/improved work.
3. **Open-source vs closed-source split**: the Conductor + Trinity papers are openly published on arXiv with full method descriptions. The Fugu API is closed-beta and the "substantially improved" methods underlying it are not (yet) academically released. The Cemini IP-sale narrative impact: an institutional buyer can read the academic Trinity + Conductor papers to understand the methodology family, but operationalizing it requires either (a) reproducing from the papers (engineer-weeks of work), (b) calling Fugu (commodity API, OpenAI-compatible), or (c) acquiring a stack that already ships LangGraph + Send() topology and treating it as a Fugu-replaceable component.

### Open questions / NEEDS-VERIFICATION items

- **[NEEDS VERIFICATION 2026-04-28]** Trinity's worker-pool composition is not enumerated in the poster the way Conductor's Table 3 enumerates its pool. Likely the same pool (Gemma3-27B + Qwen3-32B + R1-Distill-Qwen-32B + Claude Sonnet 4 + Gemini 2.5 Pro + GPT-5 — same six authors, same lab, same productization), but verifiable only by reading the full 22-page paper, which is deferred.
- **[NEEDS VERIFICATION 2026-04-28]** Trinity's open-source release status — codebase, training data, model checkpoints. Conductor and Trinity may have separate release statuses; the Sakana team's broader research lineage (ShinkaEvolve, etc.) is mixed open-source/closed.
- **[NEEDS VERIFICATION 2026-04-28]** Whether Trinity's structured-role schema (Thinker/Worker/Verifier) maps cleanly onto Pydantic-typed structured-output workers without additional architectural lift. The poster discusses natural-language LLM workers; integration with `function-calling` / structured-output endpoints is not directly addressed.

## Snippets

### S1 — Title block + venue + author affiliations (poster header)

> "TRINITY: An Evolved LLM Coordinator. A Lightweight Coordinator Orchestrating Multiple LLMs via Evolutionary Strategy. Jinglue Xu¹*, Qi Sun¹,³*, Peter Schwendeman², Stefan Nielsen¹, Edoardo Cetin¹, Yujin Tang¹. ¹Sakana AI, Japan ²University of Michigan, USA ³Institute of Science Tokyo. Published as a conference paper at ICLR 2026 | arXiv: 2512.04695"

*— Poster header, retrieved from `https://sakana.ai/assets/fugu-beta/TRINITY_poster.pdf` 2026-04-28. Confirms ICLR 2026 acceptance + arXiv ID + the joint-first-author marking on Xu and Sun.*

### S2 — Motivation (poster, page 1)

> "Scaling monolithic LLMs yields diminishing returns, and model merging is impractical across incompatible architectures and closed-source APIs. TRINITY adopts a macro-level approach: test-time model composition via coordination, fusing complementary strengths of multiple models without modifying their weights."

*— Poster Motivation & Key Contributions, page 1. Frames Trinity squarely against (a) monolithic-model scaling and (b) weight-level model merging — the two prior approaches. The "without modifying their weights" framing matches the architectural shape Cemini's deployed DeepSeek API + LangGraph stack would use.*

### S3 — Why Evolutionary Strategy (poster, central methodological argument)

> "Training the coordinator is challenging: each evaluation requires a full multi-turn LLM rollout (expensive), the reward is binary (correct/incorrect), and parameters exhibit weak mutual coupling — each has only a tiny influence on the scalar reward. RL fails: REINFORCE gradients are low-SNR under binary rewards and weak parameter correlations, yielding unstable learning. SFT is intractable: Multi-turn label generation scales as O(74·35) per question — prohibitively expensive. sep-CMA-ES works: Derivative-free, diagonal covariance matches the block-separable structure. Improvement grows linearly with iterations (vs. logarithmically for random search). Only ~1.5K–40K evaluations needed for ~10K parameters."

*— Poster Why Evolutionary Strategy section, page 1. The methodological core: a formal argument for why ES dominates RL + SFT + random search in this specific regime (high dimensions, binary rewards, weak parameter coupling). Useful counterweight in the rl-marl-research cluster's RL-default framing — Trinity is the corpus's first ES-trained-coordinator entry.*

### S4 — Coordination pipeline (Thinker / Worker / Verifier)

> "TRINITY processes queries over multiple turns. At each turn, a compact SLM reads the full transcript, and a lightweight head selects an LLM and assigns it one of three roles: Thinker (strategize), Worker (execute), or Verifier (evaluate). The process halts when the Verifier accepts the solution."

*— Poster Coordination Pipeline section, page 1. The structured-role schema is the key architectural distinction from Conductor (which uses free-form natural-language prompt design). Verifier-as-loop-termination is the cleanest mapping onto LangGraph's typed-state-graph supervisor pattern.*

### S5 — Training-method ablation (sep-CMA-ES vs alternatives, in-distribution)

> "Method | LCB | MATH | MMLU | RLPR
> REINFORCE | 0.253 | 0.459 | 0.500 | 0.266
> Random Search | 0.374 | 0.794 | 0.897 | 0.345
> SFT | 0.592 | 0.786 | 0.906 | 0.360
> sep-CMA-ES | 0.615 | 0.880 | 0.916 | 0.401"

*— Poster sep-CMA-ES Results table, page 1. Quantifies the methodological argument from S3: sep-CMA-ES dominates REINFORCE on every benchmark by 26–42 absolute points, dominates random search on MATH/MMLU/RLPR by 8–9 points, and edges out SFT on every benchmark. The REINFORCE collapse on LCB (0.253) is a reverse-direction extreme — the binary-reward + weak-coupling regime breaks REINFORCE entirely.*

### S6 — LiveCodeBench SOTA + frontier comparison

> "NEW STATE-OF-THE-ART. 86.2% pass@1 on LiveCodeBench. Surpassing GPT-5 (83.8%) and Gemini 2.5-Pro (67.2%)."

*— Poster New State-of-the-Art callout, page 1. Headline result. The 2.4-point lift over GPT-5 and 19-point lift over Gemini 2.5-Pro are unusually large for a coordinator-vs-frontier-monolith comparison. Note: Trinity's number is 86.2; Conductor's LCB number was 83.93 (in-distribution unconstrained, Section 4.2) — Trinity edges out Conductor on this specific benchmark.*

### S7 — Zero-shot OOD transfer (4 held-out benchmarks)

> "Model | AIME | BCB | MT-B | GPQA | Avg
> Gemini 2.5-Pro | 46.7 | 35.1 | 9.37 | 75.3 | 52.3
> GPT-5 | 46.7 | 33.8 | 9.35 | 72.7 | 51.1
> Claude-4-Sonnet | 35.3 | 35.8 | 9.28 | 67.3 | 46.1
> TRINITY | 50.0 | 35.8 | 9.60 | 76.8 | 54.2"

*— Poster Zero-Shot Transfer to Unseen Tasks table, page 1. Trinity wins on every OOD benchmark (AIME by 3.3 points, BCB tied with Claude, MT-B by 0.23, GPQA by 1.5). Average lift over Gemini 2.5-Pro is 1.9 points, over GPT-5 is 3.1 points. Important because OOD generalization is the strongest claim a coordinator can make — it shows the routing skill is general, not memorized to training-distribution tasks.*

### S8 — Ablation studies (every design choice contributes)

> "Method | LCB | MATH | MMLU | RLPR | Avg
> TRINITY (full) | 61.5 | 88.0 | 91.6 | 40.7 | 70.4
> w/o SV fine-tune | 55.7 | 85.9 | 90.1 | 39.8 | 67.9
> w/o Tri-role | 58.3 | 82.0 | 91.6 | 36.2 | 67.0
> w/ Last token | 50.9 | 87.0 | 82.2 | 38.6 | 64.7"

*— Poster Ablation Studies table, page 1. Three load-bearing components: (a) singular-value fine-tuning of the SLM (−2.5 avg if removed), (b) Thinker/Worker/Verifier role decomposition (−3.4 avg if removed), (c) hidden-state pooling vs last-token (−5.7 avg if switched). The last-token ablation is the most consequential — confirms the rich-contextualization claim from the arXiv abstract is empirically load-bearing.*

### S9 — Conclusion / thesis statement

> "TRINITY demonstrates that a lightweight coordinator (<20K learnable parameters) can orchestrate diverse LLMs to achieve state-of-the-art performance. The results suggest a promising path forward: engineering collaborative AI ecosystems rather than scaling monolithic models."

*— Poster Conclusion section, page 1. The thesis statement of the Sakana research lineage: orchestration-of-many-small-models > scaling-one-big-model. Aligns with Sakana's broader posture (evolutionary model merging, ShinkaEvolve, AB-MCTS) and provides the strongest one-line citation a Cemini IP-sale narrative could pull when arguing for the institutional buyer that the Cemini scatter-gather + LangGraph stack is a credible foundation for this research direction.*

### S10 — arXiv abstract (full)

> "Combining diverse foundation models is promising, but weight-merging is limited by mismatched architectures and closed APIs. Trinity addresses this with a lightweight coordinator that orchestrates collaboration among large language models (LLMs). The coordinator, comprising a compact language model (approximately 0.6B parameters) and a lightweight head (approximately 10K parameters), is optimized with an evolutionary strategy for efficient and adaptive delegation. Trinity processes queries over multiple turns, where at each turn the coordinator assigns one of three roles (Thinker, Worker, or Verifier) to a selected LLM, effectively offloading complex skill acquisition from the coordinator itself. Experiments show that Trinity consistently outperforms individual models and existing methods across coding, math, reasoning, and domain knowledge tasks, and generalizes robustly to out-of-distribution tasks. On standard benchmarks, Trinity achieves state-of-the-art results, including a score of 86.2% on LiveCodeBench. Theoretical and empirical analyses identify two main factors behind this performance: (1) the coordinator's hidden-state representations provide rich contextualization of inputs, and (2) under high dimensionality and strict budget constraints, the separable Covariance Matrix Adaptation Evolution Strategy offers advantages over reinforcement learning, imitation learning, and random search by exploiting potential block-epsilon-separability."

*— arXiv abstract `https://arxiv.org/abs/2512.04695` retrieved 2026-04-28. Companion Snippet to the poster S2–S9 collection — provides the formal academic-abstract framing of the paper for citation purposes. Note the explicit naming of "block-epsilon-separability" as the formal property sep-CMA-ES exploits — this is the most theoretical-machine-learning framing on the page and is the load-bearing claim of the academic contribution.*
