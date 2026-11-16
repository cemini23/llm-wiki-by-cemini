---
title: "Clean Tickets, Wrong Orders: Catching Silent Errors with a Language Model in Your Browser Tab (2611.18284)"
type: source
maturity: draft
related:
  - concepts/silent-structured-output-errors.md
updated: 2026-11-16
---

## Raw Concept

- **Title:** Clean Tickets, Wrong Orders: Catching Silent Errors with a Language Model in Your Browser Tab
- **Authors:** Umar Ahmed, Maxim Dunaev, Mohammad Nour Al Awad, Sergey Ivanov, Ivan Khodnenko (ITMO University)
- **Type:** arXiv preprint, demo paper
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2611.18284-clean-tickets-wrong-orders-catching-silent-error.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18284
- **Read status:** skimmed (abstract + figure)

## Narrative

A small model that turns typed orders into structured output fails in two distinct ways. It can emit something malformed, which any parser rejects. Or it can emit a well-formed order that nobody placed — a silent error — which passes every structural check.

The demo runs a fine-tuned 0.8B model entirely in the browser tab via llama.cpp compiled to WebAssembly. No order text leaves the device. The page parses as the user types, scores each ticket with the PIZZA benchmark's own matcher ported to TypeScript, refuses off-menu items with "?" so the model faces open input safely, and lets visitors hunt for silent errors or try to cause one.

Fidelity: on all 1,357 PIZZA test orders, the in-browser model matches server evaluation for 99.0% and the same exact-match score, 0.882.

The lesson is not about pizza. A validator that checks schema will pass a confidently wrong order. Catching silent errors needs a semantic matcher, and it needs to be cheap enough to run on every interaction.

[Source: arxiv-2611.18284-clean-tickets-wrong-orders-catching-silent-error.pdf]

## Snippets

> "It can print something broken, which any system rejects. Or it can print a clean, well formed order that nobody placed."
