---
title: "The Last Human-Written Paper — Agent-Native Research Artifacts"
type: source
tags: [llm-agents, ml-methods, infrastructure, research-methodology]
keywords: [ARA, agent-native, research-artifacts, reproducibility, exploration-graph, live-research-manager, compiler, review-system, scientific-communication]
related:
  - concepts/coding-agents-alphazero.md
  - concepts/agent-memory-critique.md
  - concepts/agent-native-research-artifacts.md
  - concepts/evidence-withheld-verification.md
  - concepts/exploration-graph-dead-ends.md
  - concepts/typed-relation-dependencies.md
maturity: validated
read_status: deep-read
created: 2026-05-02
updated: 2026-05-11
---

## Raw Concept
- Original title: The Last Human-Written Paper: Agent-Native Research Artifacts
- Author(s): Jiachen Liu, Jiaxin Pei, Jintao Huang, Chenglei Si, Ao Qu, Xiangru Tang (Orchestra Research + Stanford, MIT, CMU, Meta, NVIDIA, Harvard, Yale + 19 others)
- Type: PDF (arXiv)
- Location: cemini-librarian:/opt/cemini-bulk/research/The Last Human-Written Paper- Agent-Native Research Artifacts.pdf
- arXiv: 2604.24658
- Retrieved: 2026-05-02
- Pages: 46
- Read status: deep-read

## Narrative

Proposes the **Agent-Native Research Artifact (ARA)** — a protocol that replaces the narrative paper with an agent-executable research package. The paper's central claim: scientific publication is a lossy compilation process that imposes two structural taxes. The **Storytelling Tax** discards failed experiments, rejected hypotheses, and branching exploration — 90.2% of agent compute dollars on RE-Bench are spent on dead ends that publication erases. The **Engineering Tax** leaves critical implementation details unwritten — only 45.4% of 8,921 PaperBench reproduction requirements are fully specified in PDFs (missing hyperparameters = 26.2% of gaps).

ARA structures research into four layers: `/logic` (Cognitive Layer — claims, algorithms, experiment specs with forensic bindings), `/src` (Physical Layer — executable code with full operational specifications), `/trace` (Exploration Graph — research DAG preserving dead ends, pivots, and decisions), and `/evidence` (Evidence Layer — raw outputs grounding every claim). Three mechanisms support the ecosystem: a **Live Research Manager** (agent skill capturing decisions/dead ends during development), an **ARA Compiler** (agent skill translating legacy PDFs + repos into ARA format), and an **ARA-Native Review System** (three-level Seal protocol: structural integrity → argumentative rigor → execution reproducibility).

Empirical results: ARA raises question-answering accuracy from 72.4% → 93.7% (+21.3pp across 450 paired outcomes) while consuming comparable tokens. Reproduction success rises from 57.4% → 64.4%, with the gap widening on harder tasks (+8.5pp on hard). On RE-Bench extension tasks, ARA accelerates first useful move on all 5 tasks via preserved failure traces — but can constrain a capable agent (Sonnet 4.6) from stepping outside the prior-run box, while a weaker agent (Sonnet 4.5) benefits from the same heuristics.

For this workspace: ARA formalizes the "structured knowledge over narrative" thesis our wiki/ already operates on. The Compiler pattern mirrors our ingest pipeline. The Live Research Manager connects directly to Conductor's agent-memory ambitions. The Seal Level 3 evidence-withholding verification design (agent receives code kernel but never reported numbers) is a reusable anti-fabrication pattern.

## Snippets

- "Scientific publication compresses a branching, iterative research process into a linear narrative, discarding the majority of what was discovered along the way." — Two structural costs: Storytelling Tax (failures, hypotheses, branching discarded) and Engineering Tax (gap between reviewer-sufficient prose and agent-sufficient specification). [p.1]
- "Failed runs account for 90.2% of total dollar cost (and 59.2% of tokens), with a median failed-to-success token ratio of 113×" — METR eval-analysis-public dataset, 24,008 agent runs. [p.2]
- "Only 45.4% [of 8,921 reproduction requirements] are fully specified. Code development is the most underspecified category (37.3% sufficient), and missing hyperparameters alone account for 26.2% of all gaps." [p.2]
- ARA four layers: "structured scientific logic that distills the paper's conceptual abstractions into queryable claims and dependency graphs; executable code with full operational specifications; an exploration graph preserving the branching research process; and grounded evidence binding every claim to its raw empirical outputs." [p.3]
- "Knowledge over Narrative — the organized, evolving knowledge produced during research is the primary scientific object; the narrative paper is a compiled view." [p.4]
- Live Research Manager is an agent skill: "a lightweight, natural-language specification that, when loaded into a general-purpose coding agent's context window, turns it into a domain-specialized [research manager]" — not a custom SDK. [p.6]
- ARA Compiler "performs forensic reconstruction, recovering the cross-layer forensic bindings from sources where lineage exists only implicitly — scattered across prose, figure captions, appendix tables, and code comments." [p.8]
- ARA Seal Level 3: "The verifying agent is isolated from the artifact's evidence layer: it receives only the code kernel and algorithm descriptions, never the reported numbers, preventing fabrication by copying expected outcomes." [p.10]
- Understanding results: ARA 93.7% vs baseline 72.4% accuracy (+21.3pp). Category C (failure knowledge, RE-Bench): ARA 81.4% vs baseline 15.7% (+65.7pp). [p.13]
- Reproduction: "The ARA advantage widens monotonically with difficulty (+4.9% easy, +5.6% medium, +8.5% hard), tracking the tiers where reproduction depends most heavily on configuration content the PDF underspecifies." [p.14]
- Extension results: "Across all five tasks the ARA agent reaches a useful first move earlier than the paper agent" — but on triton_cumsum and restricted_mlm the paper agent later overtakes via moves the trace does not name. "Selectively hiding or contextualising parts of the trace may matter when the agent's own bandwidth exceeds what the documented playbook records." [p.15-16]
- Rigor Auditor mutation benchmark: 100% detection on fabricated claims, rebutted-branch leaks, and over-claims; 91% on missing falsification criteria; only 22% on orphan experiments. [p.16]
- "(Human+AI)² network: "publishing becomes a Git-like operation, reviewers consume Seal-attested artifacts through their preferred surfaces, and downstream agents read ARAs as structured baselines, training environments, or starting points for new questions." [p.11]
