---
title: "Librarian Agents — RL-trained anticipatory workspace curation (arXiv 2610.22273)"
type: source
tags: [agents, context, retrieval, wiki, source, k292]
keywords: [librarian agents, anticipatory curation, workspace construction MDP, GRPO, BrowseComp-Plus, BRIGHT, amortization, Claude Code harness]
related:
  - concepts/anticipatory-workspace-curation.md
  - concepts/k292-osint-wave.md
  - concepts/agentic-context-management.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @concepts/anticipatory-workspace-curation.md — the pattern this paper establishes
- @concepts/k292-osint-wave.md — K292 osint wave hub
- @concepts/agentic-context-management.md
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

Title: Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries
Authors: Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair (Stanford), Aviral Kumar (CMU), Chelsea Finn (Stanford)
Type: arXiv 2610.22273v1 [cs.LG], 24 pages, 15 Oct 2026
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.22273-librarian-agents-training-llms-to-curate-long-co.pdf`
Retrieved: 2026-10-16
Artifacts: `librarian-agents.github.io` · `github.com/teresaz05/librarian-agents`
Read status: read

## Narrative

**This paper names the thing this workspace is.** Its premise is an asymmetry in modern agentic harnesses, explicitly naming Claude Code: *agents navigate existing filesystems well, but are rarely trained to build reusable workspaces for future use.* A builder agent turns a flat corpus into a hierarchical filesystem of synthetic files plus reference links back to the raw documents — **before** any query arrives.

**Formulation.** Workspace construction is a finite-horizon **MDP**. Actions: `CreateFile`, `MergeFiles`, `Delete`, `Stop`. The builder is trained with **GRPO** to maximise a **frozen** downstream answering agent's accuracy. The reward is dense: **answerability probes every 8 turns**, plus terminal correctness. Raw documents are never deleted — provenance stays reachable.

**The RL is load-bearing, not the filesystem idea.** The authors say so directly, and the ablation supports it: a builder without fine-tuning reaches 0.28 accuracy where the trained builder reaches 0.77.

**Results.**

| Setting | Librarian | Best baseline |
|---|---|---|
| BrowseComp-Plus (Qwen3.5-4B answerer) | **0.75** | 0.44 (reranker), 0.42 (embedding) |
| BrowseComp-Plus (Gemini 3.1 Flash Lite) | **0.77** | 0.42 |
| BRIGHT zero-shot, unseen domains | pass@1 **0.52**, pass@3 **0.668** | BM25 19.0 / 26.2 |

**+33 points** over the strongest retrieval and precomputation baselines on BrowseComp-Plus; **+31 points** average on BRIGHT, zero-shot, on domains never trained on.

**Construction cost and amortisation** (the part that matters operationally):

| Method | Accuracy | Tokens |
|---|---|---|
| GraphRAG | 0.36 | 11,923 |
| AutoCompaction | 0.04 | 501,637 |
| Builder, no fine-tune | 0.28 | 127,683 |
| **Librarian** | **0.77** | **178,926** |

443 synthetic queries over 50 document sets (7-10 each). The answerer reads **26.90 files, 9,346 tokens per query**; at 20 queries per document set that is about **18K tokens per query**. End result: **33.8% fewer tokens per correct answer** (ratio 0.662, 95% CI [0.504, 0.836]). The upfront build pays back only across **repeated** queries.

**Structural signature of the trained policy:** 53.4 files, 45.4 clusters, 8.0 merges, against the base model's 4.8 files, 4.2 clusters, 0.6 merges. The trained agent builds **far more structure**, not less.

**Limitations they state.** Static corpora only — memory drift and updating are unsolved. The builder operates over a large file context, which limits scalability. **Compression may discard needle-in-a-haystack detail**, and *when to bypass the synthetic filesystem remains a challenge*.

### Why it matters here

1. **It validates the workspace's shape.** This wiki is a hand-built version of what the paper trains an agent to build: hierarchical files, reference links back to raw sources, organised for queries that have not been asked yet. The `related:` graph and the raw-source pointers in `## Raw Concept` are exactly the "reference links" the paper describes.
2. **The probe reward is the reusable mechanism.** Scoring an intermediate artefact by *how answerable it leaves future questions* is directly applicable to how we evaluate our own index and hub pages. It is the same instinct as this wiki's rule that an ingest must touch 3-15 pages.
3. **The amortisation numbers are the honest caveat.** A build costs about 179K tokens and pays back over roughly 20 queries. Below that, retrieval wins. The wiki is on the right side of that line only because queries repeat for years.
4. **The named gap is ours too:** *when to bypass the synthetic layer.* Our `[NEEDS VERIFICATION]` tags and `read_status` fields are an attempt at the same thing.

**No install. No clone. No trade.**

## Snippets

> We build on a key asymmetry in modern agentic harnesses (e.g., Claude Code): while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use. [Source: arXiv 2610.22273, abstract]

> Librarian Agents outperforms the strongest retrieval and precomputation baselines by 33 percentage points on BrowseComp-Plus, amortizes upfront construction costs across repeated queries, and generalizes zero-shot to unseen domains on BRIGHT with a 31-point average accuracy improvement. [Source: arXiv 2610.22273, abstract]

> Compression may discard needle-in-a-haystack details; when to bypass the synthetic filesystem remains a challenge. [Source: arXiv 2610.22273, limitations]
