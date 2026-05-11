---
title: "Training-Free Group Relative Policy Optimization (arXiv 2510.08191, Cai et al, Tencent Youtu-Agent Team, 2025)"
type: source
tags: [paper, llm-agents, training-free-rl, grpo, experiential-knowledge, token-prior, semantic-advantage, deepseek-v3-1-terminus, tencent-youtu-agent, cemini-relevant, cc-by-4-0, ahe-baseline]
keywords: [tf-grpo, training-free-grpo, group-relative-policy-optimization, semantic-group-advantage, experiential-knowledge, token-prior, frozen-policy, add-delete-modify-keep, experience-library, deepseek-v3-1-terminus, aime24, aime25, web-search-tasks, mean-at-32, ace-baseline, agentic-rl-without-parameter-updates, dozens-of-training-samples, youtu-agent, cai-yuzheng, tencent]
clusters: [llm-agents, infrastructure]
related:
  - concepts/llm-agent-systems.md
  - concepts/high-signal-paper-patterns.md
  - entities/infrastructure/deepseek-api.md
  - sources/agentic-harness-engineering.md
  - sources/llms-corrupt-documents-laban-2026.md
  - sources/thinking-with-visual-primitives-deepseek-2026.md
  - concepts/policy-distillation.md
  - sources/deep-graphrag-2601-11144.md
  - sources/training-free-grpo-iclr-2026.md
maturity: validated
read_status: read
created: 2026-04-29
updated: 2026-05-11
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub; this paper is foundational for "agentic-RL-without-parameter-updates" — the methodology Cemini's API-bound stack can actually use (we cannot fine-tune DeepSeek; we CAN evolve experiential-knowledge token priors).
- @concepts/high-signal-paper-patterns.md — rubric retrofit: refutation premium (refutes "agentic RL needs parameter updates"), CC BY 4.0 license, code release, empirical validation on DeepSeek-V3.1-Terminus, multiple Tier-1 quality signals.
- @entities/infrastructure/deepseek-api.md — **directly Cemini-relevant**: TF-GRPO's primary empirical validation is on **DeepSeek-V3.1-Terminus** (an earlier sibling of Cemini's deepseek-v4-flash). The methodology applies to any frozen LLM accessed via API — exactly Cemini's deployment model.
- @sources/agentic-harness-engineering.md — **closes the AHE citation triangle**: AHE Section 4.2 cites this paper as the **72.3% Terminal-Bench-2 baseline** that AHE's full-harness evolution beat (77.0%). AHE characterizes TF-GRPO as "a trajectory-feedback variant of GRPO that reinforces successful tool sequences; ... neither [ACE nor TF-GRPO] opens the surrounding scaffolding to edits". The two papers are complementary halves of the agentic-RL-without-parameter-updates space: TF-GRPO evolves token-prior experience; AHE evolves the full harness (system prompt + tools + middleware + memory). With both indexed, the wiki now has the full empirical landscape.

## Raw Concept

- **Original title**: "Training-Free Group Relative Policy Optimization"
- **Authors**: Yuzheng Cai, Siqi Cai, Yuchen Shi, Zihan Xu, Lichao Chen, Yulei Qin, Xiaoyu Tan, Gang Li, Zongyi Li, Haojia Lin, Yong Mao, Ke Li, Xing Sun (Youtu-Agent Team, Tencent Cloud)
- **Type**: arXiv preprint (cs.CL, 23 pages)
- **arXiv ID**: 2510.08191v1
- **DOI**: 10.48550/arXiv.2510.08191
- **Submitted**: 9 October 2025
- **License**: CC BY 4.0 (paper) — clean for citation + reuse
- **Code**: https://github.com/TencentCloudADP/youtu-agent/tree/training_free_GRPO (branch on the Youtu-Agent repo)
- **Correspondence**: tristanli@tencent.com
- **PDF location**: cemini-librarian:/opt/cemini-bulk/research/training-free-grpo-cai-2025.pdf (post-ingest scp)
- **Read status**: read (pages 1-5 covering abstract / introduction / methodology / experiment setup; pages 6+ contain detailed results, ablations, and discussion not deep-read in this pass)
- **Discovered via**: User manual drop 2026-04-29 alongside other inbox items
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, infrastructure

### Recency note (per high-signal-paper-patterns rubric Filter 2)

Paper is from October 9, 2025 — older than the 30-day default Tier-2 sweep window, but ingested per Filter-2's "30-90 days acceptable if Filter 3 hits hard" clause. Filter 3 hits HARD via DeepSeek family direct relevance + AHE citation triangle. The retroactive ingest pattern is also documented in the rubric: "Only ingest as a retroactive discovery (cited by something we already have, or fills a known gap surfaced by `wiki_gap_detect.py`)" — TF-GRPO is cited by AHE, which we have; canonical retroactive discovery fit.

## Narrative

### What it claims

LLM agents perform well in general but underperform in specialized real-world domains. **Agentic RL** (Group Relative Policy Optimization, GRPO, and variants) addresses this gap — but at a steep cost: parameter updates require expensive compute, scarce annotated data, and produce models that overfit and fail to generalize. Worse, fine-tuning is typically restricted to <32B models for cost reasons, while production-quality LLMs (671B-class DeepSeek, Claude Opus 4.7, GPT-5.4) are API-only. There's a **cost-performance dilemma**: the models you can fine-tune are weaker than the API models you can't.

**Training-Free GRPO** (TF-GRPO) refutes the assumption that policy optimization requires parameters. Instead of gradient ascent in **parameter space**, TF-GRPO does iterative learning in **context space** — the LLM remains permanently frozen, and an external **experiential knowledge library E** evolves over multi-epoch learning. This `E` becomes a **token prior** that conditions the model's outputs at inference time, achieving the same distributional shift effect as parameter updates without modifying any weights.

### Methodology — the four moves

The vanilla GRPO procedure for each query q:
1. Generate G rollouts using the current policy
2. Score each rollout with a reward model
3. Compute numerical advantage `Â_i = (r_i - mean(r)) / std(r)`
4. Use PPO-clipped objective + KL penalty to update parameters θ via gradient ascent

TF-GRPO replaces this with:
1. Generate G rollouts using `π_θ(o_i | q, E)` — the policy conditioned on the **current experience library** (`θ` permanently frozen)
2. Score each rollout with the reward model (same as vanilla GRPO)
3. **Compute SEMANTIC group advantage** instead of numerical — the LLM introspects on the rollout group and extracts a natural-language experience `A_text` describing what actions led to high rewards (only when there's a winner-loser split; skipped if all rewards are equal)
4. **Update the experience library E** using LLM-generated operations on each `A_text`:
   - **Add** — append a new experience to E
   - **Delete** — remove a low-quality experience from E
   - **Modify** — refine an existing experience based on new evidence
   - **Keep** — leave E unchanged

After updating E, subsequent rollouts use the refreshed conditioning context. The frozen base model π_θ provides built-in stability (analogous to KL-divergence constraint in GRPO that prevents excessive deviation from the reference model).

**Critical methodological move**: the semantic advantage is what makes this work. Instead of "this output got reward 0.8, that one got 0.6, so increase log-probability of the first" (numerical), TF-GRPO produces "the first output succeeded because it used tool X before tool Y, the second failed because it skipped step Z" (semantic) — and this lesson lives in E as a natural-language entry that conditions all future rollouts.

### Empirical results

**Setup**: applied to **DeepSeek-V3.1-Terminus** (a frozen 671B model) on AIME24 + AIME25 mathematical reasoning + web search tasks. Multiple seeds; reports Mean@32 (mean Pass@1 over 32 independent runs per problem).

**Headline finding**: TF-GRPO surpasses fine-tuned 32B models in performance with **only dozens of training samples**, while consuming a small fraction of the computational resources. The frozen 671B + experience library beats the gradient-updated 32B at lower cost.

**Three additional contributions**:
1. **A new training-free RL paradigm** — shifting policy optimization from parameter space to context space using evolving experiential knowledge as token priors.
2. **Semantic group advantage** — replaces numerical group advantage with LLM-introspected natural-language experiences; enables continuous experience-library refinement across optimization steps.
3. **Superior generalization** — by leaving model parameters frozen and plugging in different token priors per task, TF-GRPO preserves the base model's full generalization power, eliminating the cost and complexity of deploying multiple fine-tuned specialists.

(Full results table + ablations span pages 6-15; not deep-read in this pass.)

### Why this matters for Cemini — directly operational

1. **Cemini cannot fine-tune DeepSeek** (API-only access). All RL-style methods that require parameter updates (vanilla GRPO, PPO, SFT-then-RL) are unavailable. **TF-GRPO is the methodology that fits Cemini's deployment constraint**.

2. **The `E` experience library maps cleanly onto Cemini's analyst orchestrator**. `agents/orchestrator.py` already maintains analyst-specific contexts; turning these into evolving experience libraries (with Add/Delete/Modify/Keep operations after each analyst run) would convert Cemini from "static-prompt-per-analyst" to "self-improving-prompt-per-analyst" without any model weight changes.

3. **Pairs cleanly with AHE's full-harness evolution**:
   - **AHE** (Lin et al, ICLR 2026): evolves the full harness — system prompt + tools + middleware + memory + skills + sub-agents.
   - **TF-GRPO** (this paper): evolves the experiential-knowledge token prior — a single context channel.
   - **AHE >> TF-GRPO on Terminal-Bench 2** (77.0% vs 72.3%) because AHE has more degrees of freedom.
   - **TF-GRPO is much cheaper** (dozens of samples; minimal compute) and applies to any frozen LLM, not just code-agent harnesses.
   - **For Cemini**: TF-GRPO is the right starting point given budget constraints; AHE-style full-harness evolution is the aspirational target if/when Cemini's compute budget grows.

4. **The Add/Delete/Modify/Keep operations are a usable concrete pattern**. Cemini's analyst-orchestrator code can implement this directly in Python:
   ```python
   # After each analyst run with reward signal:
   if rollout_group_has_winner_and_loser:
       semantic_advantage = llm_introspect(rollouts, current_experience_E)
       op = llm_decide_op(semantic_advantage, E)  # Add/Delete/Modify/Keep
       E = apply_op(E, op)
   ```
   This is a ~50-line addition to `agents/orchestrator.py`. Concrete deployment surface.

5. **The DeepSeek-V3.1-Terminus validation** is a strong proof point. V3.1 is the predecessor of V4-flash; the experiential-knowledge token-prior approach should transfer (and may improve) on V4-class models. **Pre-deployment gate**: reproduce on Cemini's actual DeepSeek-V4-flash endpoint before committing to the architectural pattern.

### Risks & open questions

1. **Reward model dependency**: TF-GRPO assumes a reward model `R(q, o_i)` that scores rollouts. Cemini's analyst tasks (research synthesis, ticker assessment, regulatory reading) often lack ground-truth rewards. **Pre-Cemini-deployment gate**: define the reward signal for each Cemini analyst type. Where ground truth is unavailable, "LLM-as-judge" fallback can work but introduces its own bias.

2. **Domain transfer to financial-analysis tasks is unmeasured**. Paper validates on AIME (math) + web search. Cemini's domain (financial analysis, regulatory reading, ticker research) is qualitatively different. Reproduction on a Cemini-shaped task is needed before committing to the architectural pattern.

3. **Experience library size + retention policy unspecified at scale**. After thousands of optimization steps, E can grow large. The Delete operation handles this but the policy for "when does Delete fire?" isn't deeply explored in the methodology section. **For long-running Cemini deployment**: would need a retention policy + token-budget cap on E.

4. **Tencent affiliation = potential vendor bias** — though the methodology is general (any frozen LLM API works) and the math doesn't depend on Tencent-internal infrastructure.

5. **The github code is on the `training_free_GRPO` branch of `youtu-agent`** — not the main branch. Stability of the branch over time is an open question. **Pre-adoption check**: clone main + branch; verify branch is referenced from main README; confirm license at the branch level (not just root).

### Cemini-side adoption assessment

**Decision: Read + reproduce-then-deploy** (highest priority among recent ingests for actual production wiring). Concrete next-steps:

1. **License + branch stability check** via Exa `crawling_exa(url='github.com/TencentCloudADP/youtu-agent/blob/training_free_GRPO/LICENSE')`. ~5 min.
2. **Read the appendices and full results section** (paper §3.2 onward + appendices) for AIME ablations + experience-library-size dynamics. ~1 hour.
3. **Define a Cemini-shaped reward signal** for one analyst type (e.g. ticker-research analyst — reward = post-publication-accuracy of the analyst's prediction at horizon T). ~half-day scoping.
4. **Empirical reproduction**: implement the experience-library + Add/Delete/Modify/Keep loop in a small Python prototype against `deepseek-v4-flash`. Run for one Cemini-shaped task. ~half-day.
5. **If reproduction works**: brief to cemini-prod for `agents/orchestrator.py` integration (replace static-prompts with experience-library-driven prompts). ~brief drafting.

**Pairs naturally with the AHE adoption brief** — both are agentic-RL-without-parameter-updates approaches. TF-GRPO is the cheaper starting point; AHE is the expensive aspirational target.

### Citation

> Cai, Y., Cai, S., Shi, Y., Xu, Z., Chen, L., Qin, Y., Tan, X., Li, G., Li, Z., Lin, H., Mao, Y., Li, K., & Sun, X. (2025). *Training-Free Group Relative Policy Optimization*. arXiv:2510.08191 [cs.CL]. https://arxiv.org/abs/2510.08191 (Tencent Cloud Youtu-Agent Team)

## Snippets

> **The fundamental research question — refutational framing**
>
> "Such limitations inherent in parameter tuning motivate a fundamental research question: Is applying RL in parametric space the only viable approach? Can we enhance LLM agent performance in a non-parametric way with lower data and computational costs? We answer this question affirmatively by proposing Training-Free Group Relative Policy Optimization." [Source: arXiv 2510.08191 §1, p.2]

> **The semantic-advantage move — the load-bearing methodological claim**
>
> "Vanilla GRPO computes a numerical advantage Â_i that quantifies each output o_i's relative quality within its group. Similarly, Training-Free GRPO performs an analogous comparison within each group but produces a group relative semantic advantage in the form of natural language experience." [Source: arXiv 2510.08191 §2, p.4]

> **The four operations on the experience library**
>
> "We update our experience library E using all semantic advantages A_text from the current batch. Specifically, given the existing experiences library E, we prompt the LLM to generate a list of operations based on all these A_text, where each operation could be: **Add** (directly append the experience described in A_text to the experience library E), **Delete** (based on A_text, remove a low-quality experience from the experience library E), **Modify** (refine or improve an existing experience in the experience library E based on insights from A_text), **Keep** (the experience library E remains unchanged)." [Source: arXiv 2510.08191 §2, p.4]

> **The frozen-base-as-stability-prior framing**
>
> "After updating the experience library E, the conditioned policy π_θ(y | q, E) produces a shifted output distribution in subsequent batches or epochs. This mirrors the effect of a GRPO policy update by steering the model towards higher-reward outputs, but achieves this by altering the context rather than the model's fundamental parameters. The frozen base model π_θ acts as a strong prior, ensuring output coherence and providing a built-in stability analogous to the KL-divergence constraint in GRPO." [Source: arXiv 2510.08191 §2, p.4]

> **The empirical headline — outperforming fine-tuned smaller models**
>
> "Experiments on mathematical reasoning and web searching tasks demonstrate that Training-Free GRPO, when applied to DeepSeek-V3.1-Terminus, significantly improves out-of-domain performance. With just a few dozen training samples, Training-Free GRPO outperforms fine-tuned small LLMs with marginal training data and cost." [Source: arXiv 2510.08191 abstract, p.1]

> **The cost-performance dilemma — the framing TF-GRPO breaks**
>
> "API-based or open-source larger LLMs often deliver better cost-performance ratios through scalability and continuous model updates. However, these general-purpose models underperform in specialized domains where fine-tuning is necessary, creating a cost-performance dilemma." [Source: arXiv 2510.08191 §1, p.2]
