---
title: "Jev as an LLM safety guardrail: input filtering, selective output review, over-refusal (arXiv 2611.08845)"
type: source
related:
  - concepts/external-filter-safety-utility-tradeoff.md
  - concepts/calibrated-decision-models-pentest-harness-jev.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/safety-budget-control-channel-calibration.md
  - sources/arxiv-safety-as-a-budget-2611.16628.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Jev as an LLM Safety Guardrail: An Empirical Study of Input Filtering, Selective Output Review, and Over-Refusal |
| Author | Olivia Cognetti; Bhaskar Krishnamachari (University of Southern California) |
| Type | arXiv preprint (cs.CR) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2611.08845-jev-as-an-llm-safety-guardrail-an-empirical-stud.pdf` |
| Retrieved | 2026-11-09 |
| File | `arxiv-2611.08845-jev-as-an-llm-safety-guardrail-an-empirical-stud.pdf` |
| Pages | 9 |
| Read status | read |

## Narrative

Jev is a probabilistic decision model. It returns a probability for a developer-specified judgement instead of a generated explanation. The paper asks a practical question. If an application puts Jev in front of a target model, how do the harmful-answer rate and the benign-refusal rate change?

The target is Qwen2.5-1.5B with greedy decoding. The filter is `jev-latest`. The evaluation holds 970 prompts: 520 from AdvBench, 200 unsafe prompts from XSTest, and 250 safe prompts from XSTest.

### Three configurations

| Config | Rule | Harmful prompts answered | Safe prompts refused |
|---|---|---|---|
| C1 — model alone | no filter | 527/720 (73.2%) | 3/250 (1.2%) |
| C2 — input gate | block if p ≥ 0.50 | 17/720 (2.4%) | 27/250 (10.8%) |
| C3 — tiered gate + review | block p ≥ 0.90; pass p < 0.30; review the middle | 40/720 (5.6%) | 10/250 (4.0%) |

C3 reviews 79 of 970 prompts (8.1%) with a second Jev call on the response alone.

### Results

**A strong trade-off.** A stricter input threshold lowers harmful answers and raises benign refusals. The slope depends on the dataset. AdvBench prompts score a mean harmfulness of 0.98, so the answer rate stays near zero across a wide threshold range. XSTest-unsafe scores 0.87 on average and is much more sensitive to the threshold. A filter evaluated on one benchmark can look better than it is.

**The tiered gate is not free.** C3 reduces benign refusal by 6.8 points against C2 at 0.50, and raises harmful answers by 3.2 points. The more complex policy does not dominate the simple gate at the chosen points.

**Output review has a real cost.** An ablation holds the input thresholds fixed and removes the output check. Harmful answers rise from 5.6% to 6.5%, and benign refusals fall from 4.0% to 1.6%. Of the 79 reviewed outputs, 13 were blocked: seven harmful and six safe. A manual audit found that 46.2% of the blocked responses were safe.

**Joint optimisation helps in-sample.** Joint tuning of the three thresholds raises macro-F1 from 0.9351 to 0.9512. Harmful answers fall to 27/720, benign refusals stay at 10/250, and review calls fall to 28 (2.9%).

**Matched budgets remove most of the gain.** At a common 4% benign-refusal budget, a retuned single gate answers 14.5% of XSTest-unsafe prompts. C3 answers 18.5%, and a jointly retuned C3 answers 12.5%. On a 40% holdout, both selected policies produced 2.8% pooled unsafe answers and 14% benign refusals. The held-out refusal rate exceeded the tuning budget.

### Defensive reading

The paper is a guardrail-calibration result. The useful artefact is not the Jev score. It is the reporting pattern: state the harmful-answer rate and the benign-refusal rate together, state the review call volume, and do not tune and evaluate on the same prompts.

The second lesson is about the measured object. A prompt-harmfulness threshold does not measure answer harmfulness. Six of 13 blocked outputs were safe, and some XSTest-unsafe prompts passed because their generated response scored low. Input filtering and output review measure different things.

## Snippets

> "Across 720 prompts labeled harmful (520 AdvBench and 200 XSTest-unsafe), the fraction recorded as answered decreases from 527/720 (73.2%) without filtering to 17/720 (2.4%) with input filtering. On 250 XSTest-safe prompts, however, non-answer/refusal increases from 3/250 (1.2%) to 27/250 (10.8%)." [Source: arxiv-2611.08845-jev-as-an-llm-safety-guardrail-an-empirical-stud.pdf p.1]

> "Among the 13 responses blocked by Jev's output reviewer in C3, seven (53.8%) contained harmful content, while six (46.2%) were safe responses that were unnecessarily blocked." [Source: arxiv-2611.08845-jev-as-an-llm-safety-guardrail-an-empirical-stud.pdf p.7]

> "Compared with C2 at τ = 0.50, this reduces benign refusal by 6.8 percentage points, while increasing harmful-prompt answer rate by 3.2 points. Thus, the more complex policy does not dominate the simple gate at the two selected operating points." [Source: arxiv-2611.08845-jev-as-an-llm-safety-guardrail-an-empirical-stud.pdf p.5]
