# Kuhn Poker SFT Curriculum Reference (K126)

## Relations

- @briefs/2026-06-22_k126-kuhn-poker-sft-reference.md
- @briefs/2026-06-22_k126-implementation-plan.md
- @references/decide-function.md
- @references/reasoning-yaml.md

## Purpose

This page is a **reference-only** note for minimal-game supervised
fine-tuning traces discovered in K126. It exists to document what is
worth stealing from Kuhn poker trace structure for offline curriculum
study, while making the regime mismatch explicit before anyone tries to
port patterns into Arena Starter Kit `decide()` logic.

## Regime Disclosure — Kuhn vs NLHE

Kuhn poker is a three-card toy game with a single betting round and
fixed 1-chip betting. Arena Starter Kit targets no-limit hold'em
(NLHE), where actions span multiple streets, hidden ranges are much
wider, and bet sizing is a core part of strategy.

What transfers:

- Minimal legal-action discipline
- Compact action-first reasoning structure
- Curriculum value of tiny-game traces for studying format

What does **not** transfer:

- Strategic priors from a 3-card deck
- Implicit 1-chip sizing assumptions
- Any claim that Kuhn action labels are equivalent to NLHE oracle play

## Dataset Table

| Dataset | HF id | Claimed role | License | Use posture |
|---|---|---|---|---|
| Acorn Kuhn SFT | `the-acorn-ai/kuhn-poker-Qwen-QwQ-32B-5000-sft` | Kuhn SFT traces | `NO LICENSE` | Reference-only; no training use |
| Spiral Kuhn SFT | `spiral-rl/Spiral-Kuhn-Poker-Qwen3-32B-SFT` | Kuhn SFT traces | `NO LICENSE` | Reference-only; no training use |

`NO LICENSE` means these datasets should be treated as blocked for corpus
training, weight derivation, or redistribution until the authors publish
clear terms.

## Steal Matrix

| Borrow | Skip |
|---|---|
| Explicit legal-action enumeration before the answer | `\boxed{}` output format in submit path |
| Short reasoning discipline that maps cleanly to YAML | Long chain-of-thought or essay traces |
| Minimal-game curriculum ordering for format study | Kuhn card/deck assumptions |
| Action-first traces that separate prompt from answer | Any implied 1-chip sizing semantics |
| Reference-only comparison against Arena schema | Weight import, SFT training, or corpus mixing |

## Kuhn Trace -> `decide()` Mapping

| Kuhn trace field | What to extract | Arena `decide()` field | Portability note |
|---|---|---|---|
| User prompt card line | Hero private card, e.g. `Your card is: Q` | `message` / offline analysis only | Arena hole cards are 2-card NLHE, not 1-card Kuhn |
| User prompt legal actions | Legal action set such as `[check], [bet]` | `action` candidate set | Good format discipline; menu shape differs in NLHE |
| Assistant `\boxed{[action]}` | Final chosen action token | `action` | Map structurally only; not a strategic oracle |
| Assistant reasoning text or `<think>` span | Concise rationale length + style | `reasoning` | Borrow compactness, not hidden CoT payloads |
| Kuhn fixed bet meaning | Implied one-chip wager | `amount` | No direct mapping; NLHE `amount` is required for bet/raise/all-in |
| Trace/game id metadata | Example grouping / curriculum bucket | `message` or report metadata | Useful for audits, not runtime decisions |

### Action-label notes

- Kuhn `[check]` is closest to Arena `check`.
- Kuhn `[bet]` most closely resembles an aggressive action, but in NLHE
  it may correspond to `bet` or `raise` depending on street context.
- There is no portable Kuhn analogue for Arena sizing ranges such as
  `betRange.min/max` or `raiseRange.min/max`.

## Why This Is Not `regression_spots.py`

`tests/fixtures/regression_spots.py` serves a different job: it encodes
NLHE Arena fixtures with **forbidden** and **required** actions so tests
can enforce oracle-style guardrails for real `table` states.

This Kuhn reference is narrower:

- It studies trace formatting and curriculum shape
- It does **not** define correct NLHE actions
- It does **not** replace regression fixtures or Arena decision tests

Use `regression_spots.py` when validating actual NLHE behavior. Use this
page when discussing whether a Kuhn SFT trace format teaches anything
useful about compact action/rationale structure.

## Out Of Scope

- Editing `cemini_decide.py`
- Training on either Hugging Face dataset while license is `NO LICENSE`
- Importing weights or prompts from Kuhn corpora into runtime submit path
- Claiming Kuhn traces are action labels for NLHE oracle play
- Replacing `tests/fixtures/regression_spots.py` with Kuhn examples
