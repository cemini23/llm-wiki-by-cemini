---
title: "Coding harnesses are Living-off-the-Land platforms — security is architectural, not behavioural"
type: source
tags: [source, arxiv, agents, security, lotl, prompt-injection, harness]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | From Attack Surface to Defense Architecture: Compositional Security for Agentic Coding Harnesses |
| Authors | Simon Hegelich, Bard Prenkaj, Habiba Sarhan, Mohammadsadegh Shahrezaye, Kolja Hegelich, Christian Montag, Ralf Schneider, Erik Cambria |
| arXiv | 2611.13960 |
| Pages | 23 |
| Read status | skimmed (abstract) |

## Narrative

**The most important framing in this batch for anything that runs an agent with a shell.**

### The claim

A coding harness couples a language model to **shells, filesystems, and network sockets**. That coupling turns the harness into an **automated Living-off-the-Land platform**: once an adversary can inject instructions into retrieved content, **dual-use binaries such as `bash`, `curl`, and `find` become the payload** — they are not vulnerabilities to be separately exploited, they are the tool the agent is already trusted to run.

The paper's argument: **security in agentic systems is not an emergent behavioural property of individual language models, but a structural property of the cognitive architecture and its composition.**

### Why that is the right place to put the control

A behavioural control asks "will the model do the bad thing", and the answer varies by model, prompt, and luck. A structural control asks "what can this assembly reach", and the answer is fixed by the assembly.

The LoTL framing makes it concrete: an agent that can run `bash` and reach the network has already ceded the capability, and no amount of instruction makes that safe. The defence is in what the components are allowed to be composed into.

### Relevance here

This workspace runs agents with shell access against a repository, plus MCP servers with network reach, plus a git remote. That is the described platform exactly.

The paper supports a position already partly adopted here — permissions enforced outside the model, read-only surfaces where possible, a human merge gate. What it adds is the **name** for the pattern and the argument that it is not optional.

**Caveat.** Abstract only. The paper's proposed architecture and any evaluation are not in the extracted text.

## Snippets

> "That coupling turns the harness into an automated Living-off-the-Land (LotL) platform: once an adversary can inject instructions into retrieved content, dual-use binaries such as bash, curl, and find become the payload rather than a vulnerability to be separately exploited." [Source: arxiv-2611.13960 p.1]

> "Security in agentic systems is not an emergent behavioral property of individual language models, but a structural property of the cognitive architecture." [Source: arxiv-2611.13960 p.1]

## Dead Ends

- **Treating model-level safety training as the control.** The argument is that it cannot be.
