---
title: "Reimagining Enterprise RAG: A Knowledge Layer That Organizes Before It Retrieves"
type: source
tags: [source, arxiv, rag, multi-agent, ontology]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That Organizes Before It Retrieves |
| Authors | Garima Agrawal, Prasun Das, Akshay Sarvade, Priyanka L, Minisha N, Sravani Joshna, Hemath Manivannan, Lavanya Korada, Sambhrit Pattanayak, Srashti Gupta, Siddu R, Prasad Kalyanasundaram (Cognizant) |
| arXiv | 2610.32851 |
| File | `arxiv-2610.32851-reimagining-enterprise-rag-for-multi-agent-syste.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32851 |
| Read status | skimmed (abstract + intro) |

## Narrative

Enterprise agents need the behavioural logic of a system, not documentation written for stakeholders. A seven-agent reverse-engineering pipeline processed 241 repositories across 18 services into thousands of artifacts describing scope, journeys, business rules, and acceptance criteria.

Recovery is not usability. Business entities recur across an estate with a shared vocabulary — offer, eligibility, activation — where the words match but the rules differ per service. A single journey can touch over a thousand rules whose text is near-identical and must not be conflated.

**The failure mode:** flat vector retrieval returns a structurally identical rule from the wrong service, at high similarity, with no error signal. This is the most dangerous form of RAG failure, because the answer looks correct and is confidently wrong.

Content-level ontology is the traditional remedy, but building one over every entity occurrence costs more than the engagement and decays within a release cycle. The authors instead put the ontology at the **artifact level**, because the corpus is machine-generated and each artifact already carries its service provenance.

**Why it matters.** The same trap applies to a large multi-domain wiki. Two pages from different domains can share vocabulary and contradict each other. The portable lesson: attach scope and provenance to each chunk at write time, so retrieval can filter on them. Do not rely on similarity alone.

## Snippets

> "Flat vector retrieval fails here in its most consequential form, returning a structurally identical rule from the wrong service at high similarity and with no signal of error." [Source: `arxiv-2610.32851-reimagining-enterprise-rag-for-multi-agent-syste.pdf` p.1 (arXiv 2610.32851), retrieved 2026-10-27]
