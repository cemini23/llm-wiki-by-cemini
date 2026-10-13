---
title: "VEPA: verified evolving formal policy for lifelong LLM agent guardrails (arXiv 2610.12813)"
type: source
tags: [source, k290, arxiv, agent-guardrails, tool-call-security, formal-verification, agents]
keywords: [vepa, guardrails, symbolic-rules, typed-events, allow-refuse, conflict-free, beta-posterior, assbench, atbench, k290]
related:
  - concepts/k290-arxiv-wave.md
  - concepts/agent-tool-use-verification.md
  - concepts/k289-arxiv-wave.md
  - concepts/agent-harness-verification-bottleneck.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
read_status: read
---

## Relations

- @concepts/k290-arxiv-wave.md
- @concepts/agent-tool-use-verification.md
- @concepts/k289-arxiv-wave.md
- @concepts/agent-harness-verification-bottleneck.md

## Raw Concept

| Title | VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails |
| Authors | Duy Nguyen (UNC / Google Cloud AI Research), Lesly Miculicich, Bhavana Dalvi Mishra, Shuo Li, Krishnamurthy Dj Dvijotham, Mohit Bansal, Tomas Pfister, Long T. Le |
| Affiliations | Google Cloud AI Research; UNC Chapel Hill; Google DeepMind |
| Type | arXiv preprint (cs.AI), 33 pages |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.12813-vepa-verified-evolving-formal-policy-for-lifelon.pdf` |
| Retrieved | 2026-10-13 |
| Published | 2026-10-08 |
| arXiv | 2610.12813v1 |
| Code | none printed |
| read-status | read |

## Narrative

A **runtime guardrail** that decides **allow / refuse before an agent action runs** — and **keeps adapting** to new risks without giving up determinism.

### The mechanism

**Layer 1 — formal policy.** The guardrail is a finite set of rules `r = (φᵣ, dᵣ)`. The condition **φᵣ is a conjunction of typed predicates** over a fixed event schema; the decision **dᵣ ∈ {allow, refuse}**. Events are typed records `e = ⟨actor, action, data, recipient, purpose, authorization, context, tool⟩` with finite vocabularies (for example `data.sensitivity ∈ {public, confidential}`).

**This is not SMT/Z3.** Verification is **deterministic symbolic scope-overlap checking**: two opposite-decision rules conflict when their predicate scopes intersect over the schema domains, producing a witness event `e★`. A regression check re-runs the candidate policy over the accrued **correct set Cₜ**.

**Evolution.** Each round an LLM proposes **typed rule patches** (Add / Delete / Rewrite / Split / Merge) guided by the **failure set Fₜ** and the **correct set Cₜ**. A **deterministic verifier admits only well-formed and conflict-free** candidates. **MAP-Elites-style behaviour-density sampling** explores the **Pareto frontier** between failure repair and regression.

**Layer 2 — evidence-aware authority.** Each rule's error rate is modelled as `qᵣ ~ Beta(α₀, β₀)`, updated `Beta(α₀+cₜ, β₀+sₜ)`. **A rule activates only when its posterior risk quantile clears the deployment tolerance** — so **uncertain updates cannot change guardrail decisions**. If **no rule fires**, the system **abstains to an LLM fallback**.

### Results (cumulative prequential macro-F1, 5 seeds)

| Dataset | Size (allow/refuse) | VEPA | Strongest baseline |
|---------|--------------------|------|--------------------|
| ASSEBench-Safety | 1,476 (670/806) | **0.81** | +0.02 |
| ASSEBench-Security | 817 (408/409) | — | coverage **~89%** |
| ATBench | 1,000 (503/497) | **0.76** | **+0.09** |

Enforcement coverage grows to **~80% (Safety) / ~89% (Security) / ~88% (ATBench)**.

**Robustness:** mixed stream **~0.86** (AGrail 0.78, LiSA 0.80); **noisy feedback ρ=0.1 ~0.81** (AGrail 0.77, LiSA 0.76); 20-round **~0.87** (LiSA 0.83); 30-step **0.85±0.07** (LiSA 0.81). **Sparse feedback:** 5% → 0.79, 10% → 0.81, 25% → 0.83, 50% → 0.86. **Targeted adversarial (prompt-injection) labels: 0.68 → 0.83.**

**Ablations:** **No-Verifier −0.13 F1**; Greedy search −0.04; **No-Authority −0.03**. **Latency: 3-predicate rule evaluation ≈0.25 ms.**

### Limitations (stated by the authors)
Guarantees hold **only after parsing to a typed event** — **the upstream LLM parser is neural and can err or be adversarially manipulated**. **LLM fallback decisions sit outside the guarantee boundary.** The fixed schema and binary allow/refuse **cannot express temporal, relational, or multi-step requirements**.

### Why it matters here
This is the **strongest agent-guardrail artefact of the wave**. It is deterministic, auditable and **pre-action** — the exact shape of a `PreToolUse` gate. The **reusable pattern** is the split: **LLM proposes, a deterministic verifier disposes, and an evidence gate decides when a rule is trusted.** That maps directly onto **`@concepts/agent-tool-use-verification.md`** and onto the K289 ToFu lesson (tool arguments from a model are untrusted).

**Open risk to flag, not paper over:** the **neural parser sits outside the guarantee**. Post-parse determinism is **not** end-to-end determinism.

## Snippets

> VEPA represents the guardrail as a formal policy of executable symbolic rules over typed agent events. … a deterministic verifier only accepts policies that are structurally valid and conflict-free. [Source: arxiv-2610.12813-vepa-verified-evolving-formal-policy-for-lifelon.pdf p.1]

> an evidence-aware authority layer activates a verified rule only when it has enough supporting evidence, so uncertain updates cannot directly affect guardrail decisions [Source: arxiv-2610.12813-vepa-verified-evolving-formal-policy-for-lifelon.pdf p.1]

> No-Verifier −0.13 F1. [Source: arxiv-2610.12813-vepa-verified-evolving-formal-policy-for-lifelon.pdf — ablation table]
