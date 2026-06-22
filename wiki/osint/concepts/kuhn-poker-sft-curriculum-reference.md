---
title: Kuhn poker SFT curriculum reference (K126)
type: concept
tags: [concept, poker, llm-training, curriculum, devfun, k126, reference-only]
keywords: [kuhn poker, SFT, huggingface, decide function, reasoning yaml, researcher track, NO LICENSE]
related:
  - sources/links-6-22-tool-eval.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/active-project-research-routing.md
  - entities/platforms/devfun-heads-up-pvp-s3.md
maturity: validated
created: 2026-06-22
updated: 2026-06-22
---

## Relations

- @sources/links-6-22-tool-eval.md — K126 HF URLs flagged NO LICENSE
- @concepts/devfun-poker-agent-challenge-2026.md — Researcher Round `decide()` + trajectory eval
- @concepts/poker-arena-multi-axis-cognitive-profile.md — axis gates on submit reasoning
- @concepts/active-project-research-routing.md — implementation lives in `agents/devfun-poker-arena/`

## Raw Concept

What prompted this page: K126 `links.docx` surfaced two Hugging Face Kuhn poker SFT corpora (the-acorn-ai, spiral-rl). Implementation pass (2026-06-22) built offline reference tooling in `agents/devfun-poker-arena/` — **no training, no weight import**.

## Narrative

Kuhn poker is a three-card toy HU game (J/Q/K deck, 1-chip betting). Two public HF datasets package Qwen-family SFT traces: long user prompts with `[GAME]` blocks and assistant replies with `<think>` plus `\boxed{[action]}`.

**License posture:** both HF cards list **NO LICENSE** — reference-only methodology study until authors publish terms. Do not download for SFT, mix into training corpora, or redistribute rows.

**Regime disclosure (Kuhn ≠ NLHE):** Arena Starter Kit targets no-limit hold'em via `decide(table) → {action, amount?, message, reasoning}`. Kuhn strategic priors, implicit 1-chip sizing, and three-card deck do **not** transfer. Borrow format discipline only.

### Datasets (REFERENCE-only)

| Dataset | HF id | Rows (approx) | License |
|---------|-------|---------------|---------|
| Acorn Kuhn SFT | `the-acorn-ai/kuhn-poker-Qwen-QwQ-32B-5000-sft` | ~28k | NO LICENSE |
| Spiral Kuhn SFT | `spiral-rl/Spiral-Kuhn-Poker-Qwen3-32B-SFT` | train split | NO LICENSE |

### Steal matrix (methodology)

| Borrow | Skip |
|--------|------|
| Explicit legal-action enumeration before answer | `\boxed{}` submit format |
| Short YAML `reasoning` discipline (≤150 chars) vs essay CoT | Long `<think>` chains in production |
| Minimal-game curriculum for **format** study | Kuhn card/deck assumptions |
| Step structure without runtime LLM | Dataset weights / SFT corpus |

Live HF preview (2026-06-22): both datasets use `messages[{role, content}]`; assistant traces exceed Arena `reasoning` cap; boxed actions use bracket tokens `[check]/[bet]/[call]/[fold]` not NLHE sizing.

### Implementation artifacts (devfun-poker-arena)

| Path | Role |
|------|------|
| `examples/kuhn_sft_format_reference.py` | Parse traces; compare vs `decide()` schema |
| `references/kuhn-poker-sft-curriculum.md` | Kit-local steal doc |
| `scripts/run_kuhn_sft_reference_analysis.sh` | Fixture report; `--live` HF first-row preview |
| `tests/test_kuhn_sft_format_reference.py` | CI without network |
| `briefs/2026-06-22_k126-kuhn-poker-sft-reference.md` | Operator brief |

Steal candidates flagged offline: `legal_action_enumeration`, `minimal_decision_structure`, `reasoning_length_discipline`, `message_channel`, `prompt_step_structure`.

Contrast with `tests/fixtures/regression_spots.py`: regression oracle encodes **NLHE** leak spots (forbidden/required actions), not Kuhn toy-game labels.

### Out of scope

- Runtime LLM in Arena `decide()` (Level 5 opt-in only)
- HF corpus training until license clarified
- Wiki does not host dataset blobs — fixtures are truncated snippets in agent repo tests

## Snippets

> "NO LICENSE means these datasets should be treated as blocked for corpus training, weight derivation, or redistribution until the authors publish clear terms." [Source: agents/devfun-poker-arena/references/kuhn-poker-sft-curriculum.md (2026-06-22)]

> "reasoning is YAML flow style capped at 150 chars" vs Kuhn "Long <think> chains often exceed 150 chars." [Source: K126 format comparison matrix — agents/devfun-poker-arena/examples/kuhn_sft_format_reference.py]
