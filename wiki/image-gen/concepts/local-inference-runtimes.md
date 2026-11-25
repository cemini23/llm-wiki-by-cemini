---
title: "Local inference runtimes — OpenVINO and minimind as reference, not dependency"
type: concept
related:
  - "@osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - "@image-gen-wiki/entities/models/inkling-2-mini.md"
updated: 2026-11-24
maturity: draft
---

## Raw Concept

Two items in the 2026-11-24 batch concern local model execution: `openvino` (Context)
and `minimind` (Pass). The question this page answers: **what does a CPU/NPU inference
runtime buy over a GPU-first stack?**

Source: @osint-wiki/sources/2026-11-24-deep-research-link-eval-runtime-tooling.md.

## Narrative

### OpenVINO — Intel CPU and NPU

A runtime from Intel, **Apache-2.0**, with `openvino.genai` pipelines for Diffusion,
VLM, and Whisper.

The relevant claim is that inference runs on **CPU and integrated NPU**, without a
discrete GPU. For a laptop doing image work, that is a different power and thermal
profile from a CUDA path — it runs quieter and does not reserve the GPU.

Graded Context. Adding a native runtime to a project would break the stdlib-only and
pure-TypeScript constraints several projects carry, and the report is right that no
project needs it today.

### Where it would matter

If a Diffusion or VLM pipeline ever needs to run on a machine without a usable GPU,
OpenVINO is the path with the widest hardware support. That is a fallback, not an
optimization.

### minimind — Pass, and why

A small from-scratch language model, aimed at learning rather than production. Passing
it is correct: the federation does not train base models, and the educational value is
available without the repository.

### The pattern across both

Both items are **runtimes**, and runtimes are expensive to adopt — they pull native
libraries, toolchains, and platform-specific behaviour into a project that previously
had none. A runtime earns adoption only when it removes a dependency that is worse.

For Collectibles, that test currently passes for Inkling 2 Mini through Ollama or
llama.cpp — existing, already-installed paths — and fails for a new native runtime.

## Snippets

> Reference Intel CPU/NPU optimization and `openvino.genai` Diffusion/VLM/Whisper
> pipelines without adding native runtime dependencies.
> [Source: Multi-Wiki Link Revenue Evaluation.docx, URL 3]

## Dead Ends

- **Adding a native inference runtime to reach parity with an existing Ollama path.**
  It buys nothing and costs a build dependency.
