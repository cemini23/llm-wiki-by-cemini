---
title: Cogentic — orchestrator/prover/verifier harness with a verified ledger (2026-10-03)
type: source
tags: [source, arxiv, harness, agents, orchestration, verification]
keywords: [cogentic, verified-ledger, adversarial-verification, orchestrator, prover-verifier-loop]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/ccgs-workflow-extraction.md
  - entities/tools/claude-code-game-studios.md
  - sources/arxiv-2609.31076-abstraction-ladder-code-skills-2026-09-30.md
  - sources/inbox-arxiv-reject-batch-2026-10-03.md
  - sources/arxiv-2610.01514-audit-rule-faithful-explanations-2026-10-03.md
  - sources/arxiv-2610.04672-masbench-partial-observability-2026-10-07.md
  - sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md
  - sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md
  - sources/arxiv-2610.11464-who-verifies-the-verifier-2026-10-09.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.40324
maturity: validated
created: 2026-10-03
updated: 2026-10-03
---

## Raw Concept
**arXiv:2609.40324** — **Cogentic** is a multi-agent harness for automated proof discovery on open research problems, from Google Research. [CONFIRMED] Premise: single-shot generation is not enough for problems that need exploring competing conjectures, overcoming subtle obstructions, and retaining progress over a long horizon. [CONFIRMED] It uses an iterative prove–verify loop. An orchestrator allocates a population of independent provers across distinct proof directions, subject to adversarial verification. Confirmed intermediate results pass into a persistent verified ledger that later rounds build on. [CONFIRMED]

## Narrative

### Components [CONFIRMED]

- **orchestrator** — central controller. Tracks global state, partitions prover slots across directions, spawns summarizers that condense history into targeted briefings, evaluates verifier consensus, and manages ledgers and records. It does not do derivations itself.
- **literature reviewers** — retrieve definitions, theorems, and related work. Can be re-dispatched mid-run when attempts stall at the same step.
- **provers** — generate candidate proofs independently and in parallel from briefings that selectively summarize findings so far.
- **verifiers** — critique from complementary angles and scopes. They are adversarial: they begin by assuming the proofs are incorrect or incomplete.
- **advisor** — reads outputs across rounds. Helps the orchestrator adjust control, allocation, and per-prover instructions.
- **consolidation stage** — formats and audits the final manuscript.

### Workflow [CONFIRMED]
Work proceeds in rounds. A round produces a batch of candidate proofs, verifies each draft alone and then all drafts together, and writes into the record and the verified ledger that the next round starts from. Rounds continue until a draft clears verification or the budget runs out. Agents share a workspace on disk. The **record** tracks attempts and their verdicts; the **ledger** tracks verified intermediate results.

### Budget and results [CONFIRMED]
A deliberately low inference budget of O(100) to O(1000) Gemini calls per problem. Using Gemini as the base model, Cogentic produced novel results on five open problems across online learning, auction theory, and mechanism design. Domain experts verified each result independently, and companion papers develop each in full. Results: https://sites.google.com/view/cogentic

### castle-sim / W2 harness relevance [CONFIRMED]

Map component-by-component to the castle-sim W2 harness in @concepts/agent-harness-castle-project.md:

- Orchestrator -> the planner (Opus) that writes slice scope and assigns one subsystem per executor.
- Provers -> the parallel Codex swarm, each on one subsystem.
- Verifiers -> the adversarial reviewer plus the playtest gate. The adversarial stance (assume the work is wrong) is the important detail.
- Verified ledger -> the strongest idea for this project: promote only confirmed results into a durable artifact that later rounds build on, instead of re-deriving state each session.
- Record -> the attempt log and failure reasons.
- Advisor -> the operator reviewing across rounds.
- Literature reviewers -> the wiki itself.
Cross-link @concepts/ccgs-workflow-extraction.md and @entities/tools/claude-code-game-studios.md as the sibling role-graph sources.

### Phase-0 / adoption [CONFIRMED]

No public code repository — the artifact is a Google site only. There is nothing to clone-audit. Verdict: **STEAL-FROM** (pattern only, no artifact).

### Caveat [TENTATIVE]

The target domain is research mathematics and theoretical CS, and the projection step cost is justified by proof correctness. A game feature has a cheaper ground truth (the playtest), so the full verifier fan-out may not pay for itself.

## Dead Ends

- Running a full adversarial verifier population per hobby story.
- Promoting unverified intermediate results into the ledger.
