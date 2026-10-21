---
title: "CATCH — continuous adversarial training for honesty"
type: source
related:
  - concepts/k293-ccc-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honesty
Authors: Yuan-Chen Chang, Niklas Herbster, Gauthier Gidel, Tommaso Tosato (Tara Research; Mila; Technical University of Munich)
Type: arXiv preprint (2610.22292)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.22292-cat-alyzing-honesty-continuous-adversarial-train.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

CATCH (Continuous Adversarial Training for Consistent Honesty) trains a model toward an honest answer and away from a dishonest one, on the pattern of a refusal-training method. The targets are a few hundred self-report scenarios. The models are Llama-3.3-70B-Instruct and Qwen3-3.6-27B.

The abstract says the behaviour transfers. Dishonesty under pressure falls on MASK. Confessions rise in the multi-agent game Among Us. Hidden-behaviour discovery rises on AuditBench. CATCH beats prompting and supervised fine-tuning. It matches honesty activation steering on the honesty metrics and beats steering on utility, which the authors attribute to the choice of utility data.

This skim did not extract the per-benchmark deltas. Do not cite a point gain from this page. **No training run. No install.**

## Snippets

> "CATCH outperforms prompting and supervised fine-tuning in improving honesty, and it is on par with state-of-the-art honesty activation steering. However, CATCH surpasses honesty steering in maintaining utility." [Source: arxiv-2610.22292 abstract]
