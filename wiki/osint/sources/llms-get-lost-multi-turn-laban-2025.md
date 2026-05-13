---
title: "LLMs Get Lost in Multi-Turn Conversation (Laban et al., Microsoft Research + Salesforce, arXiv May 2025)"
type: source
tags: [paper, llm-evaluation, multi-turn-conversation, underspecification, conductor-relevant, microsoft-research, salesforce, arxiv, k41]
keywords: [llms-get-lost, multi-turn-degradation, 39-percent-drop, aptitude-vs-unreliability, premature-commitment, underspecified-instruction, 200k-simulated-conversations, laban, hayashi, zhou, neville, claude-mem-cross-link]
related:
  - concepts/llm-agent-systems.md
  - concepts/reviewer-agent-inference-time-feedback.md
  - concepts/agent-trajectory-triage-signals.md
  - concepts/conductor-orchestrator.md
  - concepts/rlhf-critic-bias.md
  - concepts/verbalized-sampling-llm-diversity.md
  - concepts/claude-md-12-rule-template.md
  - concepts/llms-get-lost-mitigation-audit.md
  - entities/tools/claude-mem.md
maturity: validated
read_status: skimmed
created: 2026-05-13
updated: 2026-05-13
clusters: [llm-agents, methodology]
---

## Relations

- @concepts/llm-agent-systems.md — directly relevant: any multi-turn agent loop inherits the failure mode this paper measures
- @concepts/reviewer-agent-inference-time-feedback.md — K37 reviewer-agent's "Don't make the model do non-language work" + interception design is **partial mitigation** for premature-commitment: reviewer can flag when an action depends on an early-turn assumption the model has not re-examined
- @concepts/agent-trajectory-triage-signals.md — K37 signals' post-hoc trajectory triage is the **detection** counterpart to this paper's measurement: a signals trace can flag when a long trajectory shows the "loss of way" pattern (repeated reattempts that don't return to the original spec)
- @concepts/conductor-orchestrator.md — Conductor's checkpointing and re-prompting discipline directly addresses this paper's failure mode; structural validation for that architectural choice
- @concepts/rlhf-critic-bias.md — sibling preference-data failure mode (K40). Critic-bias = systematic negativity on evals. This paper = systematic over-commitment in multi-turn generation. Both data-level, both survive perfect reward models, both have inference-time mitigations.
- @concepts/verbalized-sampling-llm-diversity.md — sibling typicality-bias mode (K39). The three preference-data failure modes — typicality (VS) + asymmetric-penalty (Critic-Bias) + premature-commitment (this paper) — now form a complete-ish taxonomy
- @entities/tools/claude-mem.md — claude-mem's design (cross-session memory injection) is **direct industrial response** to the failure mode this paper measures. The paper measures the cost of state loss across turns; claude-mem's value proposition is reducing that cost. K40 session's single-day data-window anomaly investigation was, in this paper's framing, a measurement of how claude-mem handles state across turns.

## Raw Concept

- **Original title**: "LLMs Get Lost in Multi-Turn Conversation"
- **Authors**: Philippe Laban (Microsoft Research), Hiroaki Hayashi (Salesforce Research), Yingbo Zhou (Salesforce Research), Jennifer Neville (Microsoft Research)
- **Affiliations**: Microsoft Research (Laban, Neville); Salesforce Research (Hayashi, Zhou)
- **Publication**: arXiv 2505.06120v1, 9 May 2025
- **PDF location (post-scp)**: `cemini-librarian:/opt/cemini-bulk/research/2505.06120v1.pdf`
- **sha256**: `d77f8955d696beab...` (preingest verdict: NEW; intra-inbox duplicate copy also present)
- **Size**: 1,865,278 bytes, 36 pages
- **Read status**: skimmed (abstract + introduction)
- **Discovered via**: user drop into `research to be indexed/` 2026-05-13

## Narrative

### Headline finding

All major open- and closed-weight LLMs tested show **average 39% performance drop** in multi-turn conversations vs single-turn, across six generation tasks. Measured over **200,000+ simulated conversations**.

### Decomposition of the drop

Two components:

1. **Minor aptitude loss** (the ceiling moves down a little)
2. **Major unreliability increase** (the variance widens substantially)

The unreliability is the dominant effect. Models don't just get a little worse on average — they become **unpredictable**: sometimes near single-turn performance, sometimes catastrophically worse on essentially the same task.

### The mechanism

> "We find that LLMs often make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely. In simpler terms, we discover that when LLMs take a wrong turn in a c[onversation], they get lost and never recover." [Source: 2505.06120v1.pdf p.1]

Two related failure modes:

- **Premature commitment**: model latches onto an interpretation in turn 1, treats it as fixed
- **No recovery path**: even when later turns contradict the early commitment, the model's working state is already structured around it

### Why it matters for Cemini

This paper is the **strongest published evidence** for the failure mode Cemini's Conductor + claude-mem + reviewer-agent stack is designed to mitigate. Three direct mappings:

1. **Conductor's checkpoint discipline**: explicit re-prompt boundaries between turns force the model to re-read the spec rather than rely on an internalized (possibly wrong) early commitment
2. **claude-mem cross-session memory**: the paper measures intra-session state loss; claude-mem measures intra-session-plus-across-sessions retention. Same direction, broader scope.
3. **reviewer-agent inline gating**: catches actions whose justification depends on an early-turn assumption the model hasn't re-verified

### Operational signal for Cemini

- Single-turn benchmark numbers **systematically over-estimate** real-world LLM performance
- Any Cemini eval that uses single-turn benchmarks should carry a **multi-turn discount** in interpretation
- The "unreliability widening" is more important than "aptitude reducing" — a Cemini agent that fails 5% of the time catastrophically is a worse production system than one that fails 15% of the time gracefully
- **K41 X.docx Rule 10 parallel**: Forrest Chang's CLAUDE.md template Rule 10 ("Checkpoint after every significant step") is the operational discipline that this paper's data supports

### Three-mode preference-data failure taxonomy (cross-paper synthesis)

After K39 (Verbalized Sampling), K40 (RLHF Critic Bias), K41 (this paper), Cemini's working taxonomy of training-induced LLM failure modes:

| Mode | Mechanism | Effect | Training-free mitigation |
|------|-----------|--------|--------------------------|
| Typicality bias (K39 VS) | Annotators prefer familiar text | Mode collapse on generation | Distribution prompting |
| Asymmetric-penalty (K40) | Annotators punish false endorsement > false criticism | Systematic negativity on evals | Forensic scorecard + symmetric framing |
| Premature-commitment (K41, this) | Annotators reward decisive turn-1 responses | Multi-turn degradation, lost-way pattern | Checkpoint + re-prompt + memory injection |

All three are **data-level**, all three **survive perfect reward models**, all three have **inference-time mitigations**. Cemini's stack now has named papers for each.

## Snippets

> "Our experiments confirm that all the top open- and closed-weight LLMs we test exhibit significantly lower performance in multi-turn conversations than single-turn, with an average drop of 39% across six generation tasks." [Source: 2505.06120v1.pdf p.1]

> "Analysis of 200,000+ simulated conversations decomposes the performance degradation into two components: a minor loss in aptitude and a significant increase in unreliability." [Source: 2505.06120v1.pdf p.1]
