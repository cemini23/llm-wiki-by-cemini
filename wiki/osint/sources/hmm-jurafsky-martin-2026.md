---
title: "Hidden Markov Models — Jurafsky & Martin, Speech and Language Processing (3rd ed., 2026)"
type: source
tags: [textbook, hmm, hidden-markov-models, forward-algorithm, viterbi, forward-backward, unsupervised-learning, quant-methods]
keywords: [hidden-markov-model, forward-algorithm, viterbi-decoding, forward-backward, baum-welch, markov-chain, regime-switching, sequential-data, unsupervised-learning, eisner-ice-cream-task]
related:
  - concepts/quant-finance.md
  - entities/tools/klaassen-magnus-elo.md
maturity: validated
read_status: deep-read
created: 2026-05-15
updated: 2026-05-15
clusters: [quant-finance, ml-methods]
---

## Relations

- @concepts/quant-finance.md — HMMs are a core technique for regime-switching models in quantitative finance
- @entities/tools/klaassen-magnus-elo.md — Klaassen-Magnus Elo uses HMM-inspired state estimation for match outcome prediction

## Raw Concept

- **Title**: Hidden Markov Models (Appendix A)
- **Authors**: Daniel Jurafsky & James H. Martin
- **Type**: Textbook chapter (draft)
- **Book**: Speech and Language Processing, 3rd Edition
- **Date**: Draft of January 6, 2026
- **Retrieved**: 2026-05-15
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Hidden Markov Models.pdf`
- **Pages**: 17
- **Read status**: deep-read

## Narrative

This is Appendix A from the 2026 draft of the 3rd edition of Jurafsky & Martin's Speech and Language Processing. It provides a self-contained, pedagogically clean treatment of the full Hidden Markov Model algorithm suite using Jason Eisner's ice-cream consumption task as a running example (inferring weather — Hot/Cold — from observed ice-cream counts 1/2/3).

### Structure

The chapter covers the three canonical HMM problems formalized by Rabiner (1989):

1. **Likelihood (Problem 1) — Forward Algorithm**: Given an HMM λ = (A, B) and observation sequence O, compute P(O|λ). Solved via dynamic programming in O(N²T) rather than the naive O(N^T). The forward trellis α_t(j) = P(o_1...o_t, q_t = j|λ).

2. **Decoding (Problem 2) — Viterbi Algorithm**: Given λ and O, find the most probable hidden state sequence Q*. Also O(N²T), using the Viterbi trellis v_t(j) = max_{q_1...q_{t-1}} P(o_1...o_t, q_1...q_{t-1}, q_t = j|λ). Backpointers recover the full path.

3. **Unsupervised Learning (Problem 3) — Forward-Backward / Baum-Welch**: Given O, learn λ = (A, B). EM algorithm: E-step computes forward (α) and backward (β) probabilities; M-step re-estimates A and B from expected counts. Converges to local maximum.

### Relevance to Cemini

Hidden Markov Models underpin **regime-switching models** used in quant finance — markets alternate between unobserved "regimes" (bull, bear, sideways) that generate observable returns. The Forward algorithm computes the likelihood of a return sequence under a given regime model; Viterbi decodes the most likely regime path; Baum-Welch learns regime parameters from unlabeled data. This chapter provides the clearest modern reference for the algorithmic foundations.

## Snippets

> "A Markov chain makes a very strong assumption that if we want to predict the future in the sequence, all that matters is the current state. The states before the current state have no impact on the future except via the current state." (p.1)

> "A hidden Markov model (HMM) allows us to talk about both observed events (like words that we see in the input) and hidden events (like part-of-speech tags) that we think of as causal factors in our probabilistic model." (p.2)

> "For an HMM with N hidden states and an observation sequence of T observations, there are N^T possible hidden sequences. For real tasks, where N and T are both large, N^T is a very large number, so we cannot compute the total observation likelihood by computing a separate observation likelihood for each hidden state sequence." (p.5)

> Rabiner's three problems: "Problem 1 (Likelihood): Given an HMM λ = (A, B) and an observation sequence O, determine the likelihood P(O|λ). Problem 2 (Decoding): Given an observation sequence O and an HMM λ, discover the best hidden state sequence Q. Problem 3 (Learning): Given an observation sequence O and the set of states in the HMM, learn the HMM parameters A and B." (p.3-4)
