## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox (HU curriculum reference).

## Summary

K126 links.docx surfaces **Kuhn poker SFT corpora** on Hugging Face (the-acorn-ai, spiral-rl) — useful as **offline curriculum reference** for minimal game LLM fine-tuning; **NO LICENSE** on HF cards blocks training use.

## Body

### Datasets (REFERENCE-only)

| Dataset | URL | License |
|---------|-----|---------|
| kuhn-poker-Qwen-QwQ-32B-5000-sft | the-acorn-ai/kuhn-poker-Qwen-QwQ-32B-5000-sft | NO LICENSE |
| Spiral-Kuhn-Poker-Qwen3-32B-SFT | spiral-rl/Spiral-Kuhn-Poker-Qwen3-32B-SFT | NO LICENSE |

### Steal (methodology only)

- Study trace structure for **minimal-game** HU decision formatting (action + reasoning YAML discipline)
- Compare against arena `decide()` regression fixtures — do not import weights

### Blockers

- No HF corpus training until license clarified with dataset authors
- Kuhn ≠ NLHE — regime disclosure on any borrowed prompt patterns

### Out of scope

- Runtime LLM decide() in arena submit path (Level 5 opt-in only)

## Sources

- [Source: links.docx (retrieved 2026-06-22)]
- @wiki/sources/links-6-22-tool-eval.md
