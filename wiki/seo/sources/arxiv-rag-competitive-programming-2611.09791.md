---
title: "RAG for hard problems — and the control that tests whether retrieval caused the gain"
type: source
tags: [source, arxiv, rag, retrieval, evaluation, measurement]
keywords: [RAG, competitive programming, random retrieval baseline, Min-K membership inference, memorisation, CodeContests]
related:
  - concepts/retrieval-vs-citation-visibility-geo.md
  - concepts/geo-visibility-measurement.md
maturity: draft
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Assessing the Impact of Retrieval-Augmented Generation on Algorithmic Problem-Solving |
| Author | Gabriel Souza Baggio, Gabriel Machado Lunardi, Guilherme Medeiros Machado, Subhankar Maity, Faiza Belbachir, José Palazzo Moreira de Oliveira |
| Type | arXiv preprint (cs.AI) |
| arXiv | 2611.09791v1, 6 Nov 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2611.09791-assessing-the-impact-of-retrieval-augmented-gene.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.09791-assessing-the-impact-of-retrieval-augmented-gene.pdf` |
| Pages | 25 |
| Read status | read (abstract, method, results) |

## Narrative

**The task.** Competitive programming problems punish a model that memorises. They need code plus algorithmic reasoning. The authors build a retrieval-augmented pipeline over the CodeContests corpus: 13,328 training problems form the knowledge base. Embedding similarity retrieves analogous problems, and a dynamic threshold cuts retrieval noise. [Source: arxiv-2611.09791 p.1, p.3]

**The three conditions are the useful part.** Each test problem runs three times. (i) The description alone. (ii) The description plus **randomly selected** training problems. (iii) The description plus **similar** problems from the retriever. [Source: arxiv-2611.09791 p.1, p.13]

**Reported results.** On 81 filtered problems and 6 models, mean pass@1 is **20.37%** with similar retrieval, **17.9%** zero-shot, and **17.28%** with random retrieval. Mean Elo is **1014** against **925** and **927**. [Source: arxiv-2611.09791 p.14-15]

**Two honest caveats from the paper.** First, the authors write that the models' inherent limits mattered more than the content of the examples. Second, random retrieval helped some models and hurt others: DeepSeek-R1 fell from 61.7% to 59.3% under random context, then rose to 64.2% under similar context. [Source: arxiv-2611.09791 p.15]

**The second control.** The authors run a **Min-K membership inference** check on the generated code. The check estimates whether a solution came from the model's pretraining data rather than from the retrieved context. The goal is to separate a genuine retrieval gain from recall of memorised code. [Source: arxiv-2611.09791 p.11]

### What this means for GEO

The topic is not SEO. The measurement design is transferable.

A GEO audit often reports that a brand's citations rose after a change. That rise can come from two places. The engine retrieved and used better content, or the engine already knew the brand from pretraining and the change was incidental. The random-context baseline is the cheap control: add irrelevant context and see whether the answer moves. If irrelevant context moves the answer as much as relevant context, the change did not act through retrieval.

**Thin link, stated plainly.** The paper measures code generation, not generative search. Use the control design only.

## Snippets

> "the inherent limitations of these models were a more significant factor than the content of the examples." [Source: arxiv-2611.09791 p.15]

> "RAG anchors outputs in external knowledge, while membership inference verifies their originality and data provenance." [Source: arxiv-2611.09791 p.3]

> "our RAG approach achieved a 20.37% success rate, outperforming both the zero-shot (17.9%) and random-retrieval (17.28%) approaches." [Source: arxiv-2611.09791 p.14]

## Dead Ends

- **Reading the 20.37% pass rate as a general RAG uplift figure.** It covers one hard benchmark, 81 problems, and six models. The authors state that model capability dominated the result.
