---
title: "Discovering formally verified quantum programs with AI agent teams"
type: source
tags: [source, arxiv, quantum, formal-verification, agents, out-of-scope]
keywords: [Lean, quantum Hoare logic, agent teams, shared wiki, program synthesis, quantum algorithms]
related:
  - concepts/corpus-overflow-out-of-scope.md
maturity: draft
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Discovering formally verified quantum programs with AI |
| Author | Sergey Shirobokov, Ben Jaderberg, Katerina Hristova, George Tsoukalas, Johannes Bausch, and others (Google DeepMind; Google Quantum AI) |
| Type | arXiv preprint (quant-ph) |
| arXiv | 2611.09822v1, 6 Nov 2026 (dated 9 November 2026) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2611.09822-discovering-formally-verified-quantum-programs-w.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.09822-discovering-formally-verified-quantum-programs-w.pdf` |
| Pages | 45 |
| Read status | read (abstract, introduction) |

## Narrative

**The problem.** Quantum algorithms cannot be tested at full scale, because classical computers can only simulate small instances. That limits automated discovery to the simulated regime. [Source: arxiv-2611.09822 p.1]

**The method.** The authors build a quantum program library in the **Lean** theorem prover, based on quantum Hoare logic. Researchers write a specification with a correctness and cost target. Teams of language-model agents then synthesise programs against that specification, and the Lean kernel rejects every program that does not prove. An independent comparator audits each proof against a frozen specification. [Source: arxiv-2611.09822 p.1-2]

**How the agents coordinate.** Teams share results, partial results, ideas and **dead ends through a shared wiki**. They also meet in scheduled cross-team virtual conferences. [Source: arxiv-2611.09822 p.1-2]

**Reported gains.** Up to **1.4×** on parallel search, **290×** on quantum arithmetic, **11×** on a fusion simulation, **8×** on a photochemistry simulation, and **2.5×** on a drug-metabolism simulation. [Source: arxiv-2611.09822 p.1]

### Relevance to SEO

**None.** This paper is quantum algorithm discovery. It holds no search, retrieval, content or marketing component, and nothing in it changes how an AI engine treats a web page.

Two mechanisms are interesting for other work, not for this wiki's domain.
- **A shared wiki as the coordination substrate for agent teams**, with dead ends published alongside results.
- **A frozen specification plus an independent verifier** as the gate that makes an agent claim acceptable.

Both belong to agent-workspace and verification work. They are noted here for routing honesty. They are not SEO findings, and this page makes no SEO claim.

## Snippets

> "Agent teams collaborate, sharing results and knowledge through wikis and discussing ideas at organized conferences." [Source: arxiv-2611.09822 p.1]

> "an independent verifier audits every proof against a frozen specification written in our library." [Source: arxiv-2611.09822 p.2]

> "Combining human and artificial intelligence at scale, under the rigor of mathematical proof, lets researchers design algorithms that today's classical and quantum computers cannot test." [Source: arxiv-2611.09822 p.1]

## Dead Ends

- **Looking for a content-lesson in the shared wiki.** The wiki there holds proofs and dead ends for agents. It is a coordination record, not a published knowledge base.
