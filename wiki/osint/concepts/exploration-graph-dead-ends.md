---
title: "Exploration Graph & Dead-End Tracking — Preserving What Failed"
type: concept
tags: [research-methodology, wiki-infrastructure, agent-memory]
keywords: [dead-ends, exploration-graph, failure-tracking, negative-results, trace, ARA, knowledge-preservation]
related:
  - sources/agent-native-research-artifacts-2604.24658.md
  - concepts/agent-native-research-artifacts.md
  - concepts/agent-memory-critique.md
  - sources/leworldmodel-2603.19312v2.md
maturity: validated
created: 2026-05-02
updated: 2026-05-11
---

## Raw Concept

The ARA paper quantifies the cost: 90.2% of agent compute dollars are spent on dead-end exploration that publication discards. This workspace has the same failure mode — every time we re-evaluate a rejected tool, re-investigate a dead-end paper, or re-discover a workflow that doesn't work, we pay the Storytelling Tax. How do we preserve dead ends so they compound instead of being rediscovered?

## Narrative

The ARA exploration graph uses five typed nodes (question, decision, experiment, dead_end, pivot) to preserve the full research DAG. We adopt a simplified version: a **## Dead Ends** section on wiki pages.

**Format**: Each dead end entry records three fields:
- **What was tried** — the approach, tool, paper, or hypothesis
- **Why it failed** — the specific failure mode (license poison pill, hallucinated API, performance cliff, dependency conflict, domain mismatch)
- **What was learned** — the reusable lesson that prevents re-discovery

**Placement rules**:
- Source pages: `## Dead Ends` appears after `## Snippets`. Records rejected extraction angles, tools that failed during ingest, or claims that didn't hold up.
- Concept pages: `## Dead Ends` appears after `## Snippets`. Records abandoned approaches, rejected theses, or disproven assumptions.
- Entity pages: same placement. Records rejected data sources, failed integration attempts.

**When to write a dead end**:
- A tool evaluation results in Reject
- A paper is read but not promoted (negative ingest decision)
- A hypothesis is tested and disproven
- A workflow path is attempted and abandoned
- A license or TOS check kills an adoption candidate

**When NOT to write a dead end**: trivial one-line attempts that took under 5 minutes. The bar is "would someone else plausibly try this same thing and waste real time."

**Why this works**: Dead ends are written at the moment of rejection, when the failure mode is fresh. They're attached to the page where someone would look — a rejected tool's dead end lives on the source page that evaluated it. The format is telegraphic, not narrative: three bullets, not three paragraphs.

## Snippets

- "Failed runs account for 90.2% of total dollar cost (and 59.2% of tokens), with a median failed-to-success token ratio of 113× — agents without access to prior failure records must independently rediscover every dead end." [Source: agent-native-research-artifacts-2604.24658.pdf p.2]
- "The exploration graph promotes dead ends to first-class dead_end nodes with structured failure modes and claim cross-references, making negative knowledge machine-queryable rather than lost to narrative selection." [Source: agent-native-research-artifacts-2604.24658.pdf p.18]
