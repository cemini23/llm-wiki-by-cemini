---
title: "Agentic Harness Engineering — Observability-Driven Automatic Evolution of Coding-Agent Harnesses (arXiv 2604.25850, Fudan + PKU + Shanghai Qiji Zhifeng, 2026)"
type: source
tags: [paper, llm-agents, harness-engineering, coding-agents, automatic-evolution, observability, falsifiable-contracts, terminal-bench, swe-bench, fudan, peking-university, shanghai-qiji-zhifeng, cemini-relevant, preprint]
keywords: [agentic-harness-engineering, ahe, nexau-framework, agent-debugger, evolve-agent, component-observability, experience-observability, decision-observability, change-manifest, falsifiable-contract, terminal-bench-2, swe-bench-verified, codex-cli, ace, tf-grpo, self-evolving-agents, harness-decoupling, cross-model-transfer, deepseek-v4-flash, gpt-5-4, qwen-3-6, gemini-3-1-flash-lite, system-prompt, tools, middleware, long-term-memory, skills, sub-agents]
clusters: [llm-agents, infrastructure]
related:
  - sources/harness-4-5.md
  - sources/harness2-4-5.md
  - sources/claude-code-harness-chachamaru.md
  - sources/sentrux-ast-sensor.md
  - concepts/llm-agent-systems.md
  - entities/infrastructure/deepseek-api.md
  - sources/incompressible-knowledge-probes-li-2026.md
maturity: validated
read_status: read
created: 2026-04-29
updated: 2026-04-29
---

## Relations

- @sources/harness-4-5.md — Jiun Kim's 11p preprint **proposed** "harness engineering" as a named discipline in Feb 2026; this paper is the **empirical methodology prong** of that program (Kim was framing; this is implementation + measurement).
- @sources/harness2-4-5.md — Maynard's STS commentary on the "harness" metaphor; the paper this critiqued has now been formalized into a falsifiable optimization framework — the metaphor's engineering-content claim (per Maynard's preview) is what AHE delivers.
- @sources/claude-code-harness-chachamaru.md — chachamaru is a deployed instance of the same family (Claude Code harness with hooks); AHE is the academic generalization of the same concept (observability + auto-evolution).
- @sources/sentrux-ast-sensor.md — sentrux's AST analysis of Python codebases is one technique for Component-observability (the §3.1 pillar); AHE generalizes this to file-level commits across 7 component types.
- @concepts/llm-agent-systems.md — cluster hub; this paper is the highest-signal harness-engineering empirical contribution in the corpus to date.
- @entities/infrastructure/deepseek-api.md — paper uses deepseek-v4-flash as one of five cross-model transfer bases; AHE harness yields **+10.1pp pass@1 gain** on deepseek-v4-flash (largest cross-family gain measured), validating that AHE's harness-level evolution generalizes to DeepSeek-family models — directly relevant to Cemini.
- @sources/incompressible-knowledge-probes-li-2026.md — sibling 2026-04 arXiv preprint on LLM agent infrastructure (27 Apr 2026 vs. 28 Apr 2026 for this paper). Both quantify aspects of LLM systems Cemini's stack depends on: AHE measures *harness-level evolvability* (the orchestration substrate around the model); IKP measures *factual capacity* (the model's stored knowledge). Useful pairing for the "what should Cemini optimize: harness or brain?" decision — AHE shows the harness can deliver +10.1pp on a fixed base; IKP shows the brain's factual capacity cannot be compressed by the Densing Law and must scale with total parameters.

## Raw Concept

- **Original title**: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
- **Authors**: Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin (equal-contribution; interns at Shanghai Qiji Zhifeng); Shihan Dou, Xuanjing Huang (Fudan); Hang Yan, Zhenhua Han† (Shanghai Qiji Zhifeng); Tao Gui† (Fudan, corresponding) — †corresponding authors
- **Affiliations**: Fudan University, Peking University, Shanghai Qiji Zhifeng Co., Ltd
- **Type**: arXiv preprint (cs.CL, 40 pages)
- **arXiv ID**: 2604.25850v1
- **DOI**: 10.48550/arXiv.2604.25850
- **Submitted**: 28 April 2026
- **License**: arXiv non-exclusive distribution license 1.0 (paper); source code license at github repo to be verified separately [NEEDS VERIFICATION 2026-04-29]
- **Code release**: https://github.com/china-qijizhifeng/agentic-harness-engineering
- **PDF location**: cemini-librarian:/opt/cemini-bulk/research/Agentic Harness Engineering- Observability-Driven Automatic Evolution of Coding-Agent Harnesses.pdf (after this ingest's scp step)
- **Read status**: read (pages 1-12 + abstract + figures + tables + conclusion + limitations; appendices A-D not deep-read)
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, infrastructure

## Narrative

### What it claims

Coding-agent performance on long-horizon tasks is shaped substantially by the **harness** — system prompts, tools, middleware, skills, sub-agent configurations, long-term memory — that surrounds a fixed base model. Manual harness optimization is expensive and unscientific; existing automatic-optimization approaches edit only one component (typically the prompt) and leave the rest untouched.

The paper introduces **Agentic Harness Engineering (AHE)**: a closed-loop system where a separate **Evolve Agent** edits the full harness across rounds, with the central insight that *observability* across three dimensions is what enables stable joint evolution rather than trial-and-error:

**Pillar 1 — Component observability** (§3.1, "NexAU framework"): the harness `H` is decomposed into 7 orthogonal editable component types, each at a fixed file-level mount point in a single workspace:
1. System prompt
2. Tool description
3. Tool implementation
4. Middleware
5. Skill
6. Sub-agent configuration
7. Long-term memory

Decoupling means each failure pattern maps to one component class, and every edit is a single git commit with file-level diff and rollback granularity. The seed `H₀` is deliberately minimal (single shell tool, no middleware/skills/sub-agents) to force every component AHE adds to **earn its place against measured rollouts** rather than ride an already-fitted seed.

**Pillar 2 — Experience observability** (§3.2, "Agent Debugger"): millions of raw trajectory tokens are distilled into a layered evidence corpus:
- Raw traces (kept in case the Evolve Agent needs to verify a claim)
- Per-task analysis reports (root-cause classification + pass/fail)
- Benchmark-level overview (single-document entry point per iteration)

This is "progressive disclosure" [Rajasekaran et al. 2025] applied to agent debugging: the Evolve Agent reads the overview first and drills down only into specific failure clusters — token-efficient and decision-quality-improving.

**Pillar 3 — Decision observability** (§3.3, "change manifest"): every edit ships with a self-declared prediction:
- The failure evidence motivating the edit
- The inferred root cause
- The targeted fix
- A predicted impact set: expected fixes + at-risk regressions

The next round intersects the predicted-fix and predicted-regression sets with the observed task-level deltas to produce a **per-edit verdict**. Edits whose predictions don't materialize are reverted at file granularity. *This makes every edit a falsifiable contract between rounds, replacing rationale-driven self-justification with a measurable contract.*

### Empirical results (key findings)

**Main loop (Terminal-Bench 2, GPT-5.4 high, k=2 rollouts/task, 10 iterations, ~32 hours)**:

| Method | Pass@1 (89 tasks) |
|---|---|
| opencode (human-designed) | 47.2% |
| terminus-2 (human-designed) | 62.9% |
| ACE (self-evolving baseline) | 68.9% |
| NexAU₀ seed (bash-only) | 69.7% |
| Codex (human-designed) | 71.9% |
| TF-GRPO (self-evolving baseline) | 72.3% |
| **AHE** | **77.0%** |

AHE beats every human-designed harness and every self-evolving baseline.

**Cross-benchmark transfer (SWE-bench-verified, 500 tasks, no re-evolution)**: AHE achieves the highest aggregate success (75.6%) **at 12% fewer tokens than the seed** — the gain transfers, and encoding behavior in tools/middleware/memory rather than prompt avoids per-call re-derivation cost. ACE and TF-GRPO regress below the seed on this transfer (their playbook + trajectory distillation were terminal-bench-specific).

**Cross-model transfer (5 alternate bases, no re-evolution)**: all 5 produced positive gains, **largest on weaker bases**:
- deepseek-v4-flash: +10.1pp (51.7% → 61.8%) ← largest cross-family gain
- qwen-3.6-plus: +6.3pp (56.2% → 62.5%)
- gemini-3.1-flash-lite-preview: +5.1pp (36.5% → 41.6%)
- GPT-5.4 medium/xhigh: +2.3pp each (within-family gains attenuated by timeout-budget coupling)

Reading: weaker bases lean harder on harness-encoded coordination patterns; stronger bases re-derive coordination from prompt at low marginal cost. **AHE encodes general engineering experience, not benchmark-specific tuning.**

**Component ablation (where the gain lives)**: each "+ X only" row swaps a single AHE component into the NexAU₀ seed:

| Variant | Pass@1 vs NexAU₀ |
|---|---|
| + memory only | +5.6pp |
| + tools only | +3.3pp |
| + middleware only | +2.2pp |
| + system prompt only | **−2.3pp (regresses)** |
| AHE full | +7.3pp |

**The system prompt alone regresses.** The gain lives in **tools, middleware, long-term memory** — not prose.

**Self-attribution quality (RQ3b)**: the change manifest's predictions vs ground truth across 9 evaluation rounds:
- Fix-precision: 33.7% (5× random baseline 6.5%) ✅
- Fix-recall: 51.4% (5× random baseline 10.6%) ✅
- Regression-precision: 11.8% (2× random baseline 5.6%) ⚠
- Regression-recall: 11.1% (2× random baseline 5.4%) ⚠

**Insight**: the agent knows what it's about to fix but is largely blind to the regressions it's about to cause. This is the clearest direction for future work.

### Why this matters for Cemini

Several patterns map directly onto Cemini's analyst-orchestrator architecture:

1. **Component decoupling for the analyst stack**: Cemini's `agents/orchestrator.py` already orchestrates 4 analysts (`services/llm_analyst/deepseek_client.py`). Decoupling each analyst's surface (prompt + tools + middleware + memory) into 7 file-level mount points rather than one monolithic agent class would yield AHE-style attribution if Cemini ever wants to evolve analyst behavior.

2. **Falsifiable-contract pattern**: Cemini's claim-confidence tag system (`[CONFIRMED]` / `[TENTATIVE]` / `[NEEDS VERIFICATION]` / `[RETRACTED]`) is conceptually adjacent — claims get tagged, later verified, possibly retracted. AHE's manifest formalizes this with per-edit predicted impact + next-round verdict + automatic rollback. Cemini's wiki currently relies on human-mediated escalation (NEEDS VERIFICATION → Exa crawl → upgrade to CONFIRMED). The AHE pattern suggests a **machine-mediated escalation** path — predictions logged, observability re-checked, tags updated. Adjacent to but more sophisticated than the current K-series promotion-vs-snippets discipline.

3. **Cross-model transferability validates DeepSeek substitution risk**: the +10.1pp deepseek-v4-flash gain (vs NexAU₀ seed) provides empirical evidence that **harness-level engineering generalizes across LLM families**. If Cemini ever needs to swap brain providers (DeepSeek → Anthropic or others), a properly decoupled harness (per AHE's substrate) would carry the orchestration logic across without re-evolution. Reduces lock-in risk to any single LLM API.

4. **Operational priority signal**: the **−2.3pp regression on system-prompt-alone** is a counterintuitive finding worth internalizing. Cemini's current orchestrator improvements (when budget is constrained) should prefer **tools + middleware + long-term memory** investment over prompt-tuning. The "edit your prompt to be smarter" instinct is empirically wrong as a sole investment.

5. **Methodological scaffolding for librarian evolution**: this workspace's `wiki_lint.py` is a primitive Agent Debugger — it surfaces orphans, gaps, missing-references, stale tags. AHE's three-pillar framing (component / experience / decision observability) suggests where the librarian's lint script could go: every wiki edit could ship a self-declared prediction (e.g. "this ingest should reduce orphans by 3 and resolve 1 cited-unread stub"), and the next lint run would check the prediction against observed deltas. Currently lint is descriptive only; AHE-style would make it predictive + auditable.

### Risks & open questions

1. **Code license verification** [NEEDS VERIFICATION 2026-04-29] — paper is under arXiv non-exclusive license (paper-level, fine for citation). The github.com/china-qijizhifeng/agentic-harness-engineering code release license must be checked separately before any code is borrowed for Cemini. Critical for IP-sale-readiness — see `@concepts/ip-sale-readiness.md` poison-pill family A (copyleft).

2. **Compute cost** [TENTATIVE] — per the limitations section, AHE adds engineering + compute overhead vs one-shot prompting. Each iteration requires benchmark execution, trajectory analysis, and workspace management. Paper promises "the final paper will report these costs explicitly." Cemini's budget-bound deployment context (single Hetzner CPX21 + DeepSeek API) cannot afford GPT-5.4-high-style 32-hour evolution loops. Adapting the AHE substrate to a smaller-scale loop on Cemini-shaped tasks would require substantial scoping.

3. **Benchmark-specific tuning risk** [NEEDS VERIFICATION 2026-04-29] — AHE's transfer experiments show generalization to SWE-bench-verified and 4 alternate bases, but only within Terminal-Bench-style and SWE-bench-style coding tasks. **Generalization to financial-analysis tasks (Cemini's actual workload) is unmeasured.** This is the single biggest open question for Cemini's potential adoption.

4. **Regression blindness in self-attribution** [TENTATIVE] — regression-precision/recall are only 2× random baseline. If Cemini adopted AHE-style auto-evolution for the analyst orchestrator, the loop would reliably hit the targeted fixes but could silently introduce regressions at roughly random selection. Mitigation: hard-coded canary tasks that must pass after every edit (akin to CI smoke tests) would catch regressions the agent doesn't predict.

5. **NexAU framework dependency** [TENTATIVE] — AHE is built on NexAU [Nex-AGI 2025] — `https://github.com/nex-agi/NexAU`. Cemini's adoption would either require porting AHE off NexAU or adopting NexAU as a substrate. Adoption-cost not quantified yet.

6. **Equal-contribution authors are interns** — paper notes the 4 first authors did the work during internships at Shanghai Qiji Zhifeng. If those interns return to academic affiliations, ongoing maintenance of `china-qijizhifeng/agentic-harness-engineering` may slow. Worth tracking as a bus-factor concern over 6-12 months.

### Cemini-side adoption assessment

**Decision: Watch-and-validate**, not Adopt yet. The pattern is high-signal and the empirical results are strong, but:
- The gap between Terminal-Bench/SWE-bench (their domain) and financial-analysis tasks (Cemini's workload) is not bridged in this paper.
- The compute cost of an AHE evolution loop is unspecified but likely outside Cemini's single-VPS budget.
- The license on the github code is unverified.

**Concrete next steps if Cemini wanted to act**:
1. **Code license check** — clone the github repo, read the LICENSE file, classify per `@concepts/ip-sale-readiness.md` poison-pill families A & B. (~10 min)
2. **Read the appendices A-D** for the implementation detail and the per-round breakdown of regression-blindness. (~1 hour)
3. **Survey for follow-on work** — paper cites Lee et al. 2026 "meta-harness" (arXiv 2603.28052) as concurrent end-to-end harness optimization; check if that paper's methodology is more amenable to Cemini's scale. (~1 hour Exa)
4. **Brief evaluation** — could the Evolve-Agent / Agent-Debugger substrate be adapted to Cemini's analyst orchestrator at a 1-iteration-per-week cadence rather than 10-iterations-per-32-hours? (~half-day scoping; output: brief for cemini-prod-side execution decision).

### Citation

> Lin, J., Liu, S., Pan, C., Lin, L., Dou, S., Huang, X., Yan, H., Han, Z., & Gui, T. (2026). *Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses*. arXiv:2604.25850 [cs.CL]. https://arxiv.org/abs/2604.25850

## Snippets

> **The thesis — observability, not agent capability, is the bottleneck**
>
> "Our central insight is that this question is bottlenecked by **observability**, not by agent capability: once the evolution agent receives structured context over a clear action space, it can reliably converge on better harness designs." [Source: arXiv 2604.25850 §1, p.2]

> **The seven editable component types (NexAU substrate)**
>
> "We instantiate the harness H on the NexAU framework, which exposes seven orthogonal component types as explicit files at fixed mount points in a single workspace: system prompt, tool description, tool implementation, middleware, skill, sub-agent configuration, and long-term memory. The component types are loosely coupled, so adding a middleware does not require editing the system prompt, and adding a skill does not require touching any tool." [Source: arXiv 2604.25850 §3.1, p.3]

> **Falsifiable contracts — the decision observability core**
>
> "Each edit attaches a manifest entry that names the failure evidence, the inferred root cause, the targeted fix, and a predicted impact comprising both expected fixes and at-risk regressions; this manifest is the loop's evidence ledger. In the next round, the loop intersects the predicted-fix and predicted-regression sets with the observed task-level deltas to produce a per-edit verdict. Each edit thereby becomes falsifiable by the next evaluation, which replaces rationale-driven self-justification with a measurable contract between rounds." [Source: arXiv 2604.25850 §3.3, p.5]

> **The system prompt regresses alone — the counterintuitive empirical finding**
>
> "swapping in AHE's tools, middleware, or long-term memory alone yields +3.3, +2.2, and +5.6 pp, while the system prompt alone is −2.3 pp. The harness components ACE and TF-GRPO never edit are exactly where the gain lives." [Source: arXiv 2604.25850 §4.2, p.6-7]

> **Cross-family transfer — the load-bearing finding for general-experience claim**
>
> "Cross-family gains dominate within-family ones: deepseek-v4-flash moves +10.1 pp from 51.7% to 61.8%, qwen-3.6-plus +6.3 pp from 56.2% to 62.5%, and gemini-3.1-flash-lite-preview +5.1 pp from 36.5% to 41.6%, all above the +2.3 pp on GPT-5.4 medium and xhigh. We read this as bases further from saturation leaning more on the coordination patterns AHE has fixed inside tools, middleware, and long-term memory." [Source: arXiv 2604.25850 §4.3, p.7]

> **Self-attribution: knows fixes, blind to regressions**
>
> "The regression panel tells the opposite story: cross-iteration regression-precision of 11.8% and regression-recall of 11.1% sit only about 2x above their random baselines of 5.6% and 5.4%, so most upcoming regressions go unforeseen. The agent can justify why an edit should help, but it cannot reliably name the tasks the same edit is about to break, which is what produces the non-monotone steps in the evolution curve. Closing this gap is the clearest direction for future self-evolution loops." [Source: arXiv 2604.25850 §4.4.2, p.9]

> **Limitations — the paper's own self-disclosure**
>
> "AHE should be understood as an initial framework rather than a finished answer. Its value depends on whether evidence-driven harness evolution produces robust gains without collapsing into benchmark-specific tuning. […] AHE should be viewed as a controlled research prototype rather than a fully mature autonomous self-improvement system." [Source: arXiv 2604.25850 Conclusion + Limitations, p.9-10]
