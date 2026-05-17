---
title: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
type: source
tags: [pdf, llm-agents, k49]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?
- **Author(s)**: Thibaud Gloaguen, Niels Mündler (ETH Zürich), Mark Müller, Veselin Raychev (LogicStar.ai), Martin Vechev (ETH Zürich)
- **Type**: PDF (arXiv preprint 2602.11988v1, 13 Feb 2026)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/agents.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 18p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

This paper is the first rigorous study of whether repository-level context files (AGENTS.md, CLAUDE.md) — now present in 60,000+ public GitHub repos and strongly recommended by agent vendors — actually help coding agents solve real tasks. The authors evaluate four agent/model pairs (Claude Code + Sonnet-4.5, Codex + GPT-5.2 and GPT-5.1-mini, Qwen Code + Qwen3-30B-Coder) in three settings: no context file, LLM-auto-generated context file (via each agent's `/init`), and developer-committed context file. They build a new 138-instance benchmark, AGENTBENCH, mined from 5694 PRs across 12 niche Python repos that ship developer-written context files, complementing SWE-bench Lite (300 tasks, popular repos, no context files).

The headline result is counterintuitive: context files mostly do **not** help. LLM-generated files reduce success in 5 of 8 settings (−0.5% on SWE-bench Lite, −2% on AGENTBENCH on average), and developer-written files give only a marginal +4% gain. Crucially, every context file increases the number of agent steps and raises inference cost by 20–23% — partly via 14–22% more reasoning tokens. Trace analysis shows agents do follow context-file instructions (e.g. `uv` is used 1.6×/instance when mentioned vs. <0.01× otherwise), so the lack of gains is not an instruction-following failure: the extra instructions simply make tasks harder. Context files also fail as repository overviews — they do not speed up the agent's first contact with relevant files. The one exception: when all other documentation (`.md`, `docs/`) is stripped, LLM-generated files become net-positive (+2.7%), explaining anecdotal "AGENTS.md helped" reports in poorly-documented repos. Conclusion: omit auto-generated context files; human-written ones should state only minimal, repo-specific requirements (e.g. tooling).

**Cemini relevance**: directly bears on the CCC meta-wiki's CLAUDE.md authoring discipline — Cemini's own schema files are exactly the artifact studied here; the finding "minimal, repo-specific requirements only; avoid redundant overviews" is a concrete editing guideline for the workspace's CLAUDE.md and for agent-evaluation methodology across the conductor architecture.

## Snippets

> "Across multiple coding agents and LLMs, we find that context files tend to reduce task success rates compared to providing no repository context, while also increasing inference cost by over 20%." [Source: agents.pdf p.1]

> "Ultimately, we conclude that unnecessary requirements from context files make tasks harder, and human-written context files should describe only minimal requirements." [Source: agents.pdf p.1]

> "We conclude that context files, even developer-provided ones, are not effective at providing a repository overview." [Source: agents.pdf p.6]
