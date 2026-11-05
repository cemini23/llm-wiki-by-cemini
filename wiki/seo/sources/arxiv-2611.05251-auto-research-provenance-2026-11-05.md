---
title: "auto_research — enforced provenance for agent-produced numbers"
type: source
tags: [source, arxiv, agents, provenance, verification, self-extension]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A semi-autonomous multi-agent pipeline for high-energy astrophysics research with enforced provenance and verifiable self-extension |
| Author | Fang Zhou (Washington University in St. Louis, Physics) |
| arXiv | 2611.05251 |
| Pages | 19 |
| Read status | skimmed (abstract) |

## Narrative

**The clearest statement of the problem this workspace has been circling for weeks.**

LLM agents now retrieve literature, reduce observations, and draft conclusions. Under pressure to complete a task, **such an agent can fabricate results, and the numbers it reports may not come from the analysis it ran.**

### The two checks

**1. Tools must be earned.** A new tool enters the toolkit only after passing automatic checks — repeated test runs, a scan for **phrases that accompany invented values**, and a **code review by a model from a different provider** — after which **a human decides whether to promote it to the trusted branch**.

**2. Numbers must be traceable.** A number in a report passes only if **a recorded output of a toolkit tool or the request contains it**. Otherwise it does not go in.

### Why check 2 is the one to steal

It is mechanically checkable and it is not a prompt instruction. The claim "this number came from the analysis" becomes a **lookup in the recorded outputs**, not a judgement about whether the model seems trustworthy.

That is the same discipline as `text.slice(start, end) === value` in the verbatim-extraction pattern, applied one level up: the value must be findable in the artefact that produced it.

### Why check 1 is the other half

Self-extension — an agent writing the tools it needs — is where this could go wrong silently. Three gates on that: it must **run repeatedly**, it must not use the phrasing that signals fabrication, and it must pass **review by a different model family**. Then a human promotes.

The cross-provider review is the specific idea. A model reviewing its own generated tool shares its blind spots; a different family does not.

**Caveat.** Abstract only; the scan's phrase list and the tool-promotion rubric are not in it.

## Snippets

> "Under pressure to complete a task, such agents can fabricate results, and the numbers they report may not come from the analysis they ran." [Source: arxiv-2611.05251 p.1]

> "A number in a report passes only if a recorded output of a toolkit tool or the request contains it." [Source: arxiv-2611.05251 p.1]

## Dead Ends

- **Treating provenance as a prompt instruction.** Here it is a lookup against recorded outputs.
