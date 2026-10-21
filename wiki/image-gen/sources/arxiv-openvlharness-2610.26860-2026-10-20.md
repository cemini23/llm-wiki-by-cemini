---
title: "OpenVLHarness — visual agentic tool use with multimodal memory"
type: source
related:
  - concepts/k293-image-gen-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: OpenVLHarness: Real-World Visual Agentic Tool-Use with Multimodal Memory
Authors: Yu Zhou, Cheng-Fu Yang, Rui Sun, Di Wu, and colleagues (UCLA; Apple)
Type: arXiv preprint (2610.26860)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2610.26860-openvlharness-real-world-visual-agentic-tool-use.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)
Code: https://github.com/uclanlp/OpenVLHarness
Project: https://openvlharness.github.io

## Narrative

A controlled study on 22 benchmarks finds that a larger inference budget on the base multimodal model yields only modest gains. The tasks need perception, external knowledge, and measurements from tools, and those outputs have to stay readable across steps.

OpenVLHarness has two pieces. A capability layer gives one interface to different tool backends and renders their outputs as observations the model can read. A persistent multimodal memory keeps the images, structured data, and web references as addressable artifacts for the whole query. A coding interface runs generated programs over the stored data, so later steps can combine earlier tool results.

On 22 benchmarks and eight open and proprietary backbones, the harness improves average scores by **9.7–12.6** points over matched no-tool baselines. **REFERENCE. No clone. No install.**

## Snippets

> "Simply increasing the inference budget of the base model yields only modest gains." [Source: arxiv-2610.26860 abstract]
