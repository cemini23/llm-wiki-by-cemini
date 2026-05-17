---
title: "shiyu-coder/Kronos — Foundation Model for Financial Markets (MIT, AAAI 2026, Decoder-Only Transformer on K-line/OHLCV)"
type: source
tags: [github, foundation-model, financial-time-series, k-line, ohlcv, transformer, mit, aaai-2026, steal-from-tier, gemini-dr-wave5a, status-change-defer-stealfrom, kronos-tokenizer, binary-spherical-quantization]
keywords: [kronos, kronostokenizer, financial-foundation-model, k-line, ohlcv, candlestick, decoder-only, two-stage-tokenizer, hierarchical-discrete-tokens, kronos-mini, kronos-small, kronos-base, kronos-large, neoquasar, qlib, pyqlib, aaai-2026, arxiv-2508-02739, mit-license, financial-llm, shiyu-coder]
clusters: [llm-agents, financial-modeling, infrastructure]
related:
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/microsoft-qlib.md
  - sources/incompressible-knowledge-probes-li-2026.md
  - sources/moe-efficiency-leverage-tian-2026.md
  - sources/moe-surpass-dense-equal-resource-li-2026.md
  - concepts/llm-agent-systems.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/quant-finance.md
  - entities/infrastructure/deepseek-api.md
  - concepts/high-signal-paper-patterns.md
maturity: validated
read_status: read
created: 2026-04-30
updated: 2026-05-17
---

## Relations

- @sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md — Wave 5A canonical brief; URL 3 of the 6-URL evaluation; promoted to dedicated page from Steal-from verdict (status change Wave 4A Defer → Wave 5A Steal-from)
- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A predecessor (URL 27 in that brief; Defer tier); the cross-wave reclassification rationale lives there (AAAI 2026 acceptance + 22k stars + 20 contributors)
- @sources/microsoft-qlib.md — operational pair: qlib provides data-prep + backtest harness; Kronos fits as foundation-model layer feeding qlib's signal pipeline. Both MIT-licensed, both Cemini-stack-aligned.
- @sources/incompressible-knowledge-probes-li-2026.md — knowledge-side MoE pairing: Kronos's 4.1M-499.2M dense-Transformer scale lives in a different architectural space (no MoE), but the IKP knowledge-capacity-vs-active-params framing can be extended to Kronos's tokenizer compression efficiency.
- @sources/moe-efficiency-leverage-tian-2026.md — compute-side MoE pairing: Kronos is a dense model so EL-doesn't-apply, but the compute-budget power-law informs whether Kronos-large's 499.2M params would have been more efficiently trained as a sparse MoE.
- @sources/moe-surpass-dense-equal-resource-li-2026.md — strict-equal-resource MoE pairing: same dense-vs-MoE framing — Kronos's dense architecture choice is a deliberate departure from the MoE trend that Cemini's brain (DeepSeek-V4-Flash) embraces.
- @concepts/llm-agent-systems.md — cluster hub; Kronos is a domain-specific foundation model (financial K-line) fundamentally different from Cemini's general-purpose brain (DeepSeek-V4-Flash). Pattern: domain-specific foundation models as auxiliary signal sources.
- @concepts/wiki-tooling-evaluation.md — adoption decision parent; Kronos is a textbook **Steal-from-the-tokenizer-not-the-model** pattern (extract KronosTokenizer; reject KronosPredictor for production).
- @concepts/ip-sale-readiness.md — MIT root is clean; pyqlib transitive deps need pre-adoption sweep.
- @concepts/quant-finance.md — domain anchor; Kronos's hierarchical OHLCV→discrete-token quantization is a paradigm shift in financial modeling.
- @entities/infrastructure/deepseek-api.md — Cemini's brain (DeepSeek-V4-Flash) is general-purpose MoE; Kronos is domain-specific dense Transformer. Different deployment lanes — Kronos as auxiliary signal source feeding DeepSeek's reasoning, not as a brain replacement.

## Raw Concept

- **Original title**: "Kronos: A Foundation Model for the Language of Financial Markets"
- **Authors (paper)**: Yu Shi, Zongliang Fu, Shuo Chen, Bohan Zhao, Wei Xu, Changshui Zhang, Jian Li
- **Repository**: https://github.com/shiyu-coder/Kronos
- **License**: MIT (file-level + repo-level confirmed via Exa `crawling_exa` 2026-04-30)
- **Primary language**: Python (81.9%) + HTML (17.7%) + Shell (0.4%)
- **Stars**: 22,172 (as of 2026-04-30) → "no longer bus-factor"
- **Forks**: 3,908
- **Contributors**: 20 (top: shiyu-coder, Luciferbobo, CharlesJ-ABu, AnMakc, randyy179, xxsunyxx, phaoer, dowithless, kuishou68, billconan2017)
- **Created**: 2025-07-01
- **Last push**: 2026-04-13
- **Paper**: arXiv:2508.02739 (Aug 2025)
- **Conference acceptance**: **AAAI 2026** (announced 2025-11-10)
- **Hugging Face Hub**: NeoQuasar/Kronos-Tokenizer-2k, NeoQuasar/Kronos-Tokenizer-base, NeoQuasar/Kronos-mini, NeoQuasar/Kronos-small, NeoQuasar/Kronos-base
- **Live demo**: BTC/USDT 24-hour forecast on https://shiyu-coder.github.io/Kronos-demo/
- **Read status**: read (README + license + model card hierarchy + AAAI announcement; deeper paper read pending if Cemini commits to the tokenizer extract)
- **Discovered via**: Wave 4A docx evaluation 2026-04-29 (URL 27, Defer); Wave 5A docx 2026-04-30 (URL 3, Steal-from after deeper evaluation)
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents, financial-modeling, infrastructure

## Narrative

### What it is

Kronos is the **first open-source foundation model for financial K-line / candlestick data**, pre-trained on 45+ global exchanges. Architecturally, it's a **two-stage decoder-only Transformer**:

1. **KronosTokenizer**: continuous OHLCV (Open / High / Low / Close / Volume) data → **hierarchical discrete tokens**. The docx evaluation cites this as Binary Spherical Quantization (continuous-to-discrete mapping). Tokenizer architecture confirmed by repo; specific BSQ claim [CONFIRMED 2026-05-17] — verified against arXiv:2508.02739 §3.1: "we adapt Binary Spherical Quantization (BSQ) (Zhao, Xiong, and Krähenbühl 2024), a variant of Look-up Free Quantization (LFQ)" for the K-line Tokenizer; the tokenizer is a Transformer-based autoencoder with an explicit BSQ layer (paper Figure 3), factorizing the k-bit code into n=2 coarse/fine subtokens.
2. **KronosPredictor**: autoregressive Transformer trained on the discrete-token sequence. Predicts next tokens (next price-volume action) given context.

The model family scales:

| Model | Tokenizer | Context length | Params | Open-source |
| --- | --- | --- | --- | --- |
| Kronos-mini | Tokenizer-2k | 2048 | 4.1M | ✅ |
| Kronos-small | Tokenizer-base | 512 | 24.7M | ✅ |
| Kronos-base | Tokenizer-base | 512 | 102.3M | ✅ |
| Kronos-large | Tokenizer-base | 512 | 499.2M | ❌ (not released) |

The Kronos-mini/small/base sizes (4.1M-102.3M params) fit CPU inference. Kronos-large (499.2M, withheld) presumably fits cleanly on a small GPU.

### Why this matters for Cemini

**Cemini production stack — ⚠️ Partial-fit / Steal-from**:
- Direct integration into LangGraph orchestrator (`agents/orchestrator.py`) as auxiliary market-prediction signal — Kronos-mini at 4.1M params is small enough for CPU inference at request time.
- BUT: the authors disclaim production-readiness ("provided fine-tuning pipeline is a 'simplified example and not a production-ready quantitative trading system'"). Deploying KronosPredictor as a primary brain violates trading determinism + audit-ability requirements.
- **Steal-from extract**: the **KronosTokenizer** — the continuous-OHLCV-to-discrete-token quantization architecture is the high-value pattern.
- License compatibility ✅: MIT confirmed file + repo level.

**Wiki / Librarian server — ❌ No-fit**:
- Hetzner CPX21 is a Karpathy-pattern markdown compiler + semantic search hub. Deploying a financial K-line foundation model on it violates the resource budget and architectural mandate.

**Workflow — ✅ Yes-fit**:
- The continuous-OHLCV-to-discrete-token tokenization pattern is the architectural blueprint. Even if Cemini doesn't deploy Kronos's actual model, **the tokenizer pattern itself** can inform Cemini's own time-series-as-language architectures (e.g., feeding into DeepSeek-V4-Flash's reasoning context).

### The status-change rationale (Wave 4A Defer → Wave 5A Steal-from)

Wave 4A flagged Kronos as Defer pending peer-reviewed evaluation + bus-factor concerns. Wave 5A's upgrade to Steal-from is justified by four cumulative signals discovered via deeper Exa cross-check:

1. **AAAI 2026 acceptance** (announced 2025-11-10) — high-prestige peer-reviewed signal directly addressing Wave 4A's "pending peer-review" objection.
2. **20 contributors** + **22,172 stars** — no longer the bus-factor concern Wave 4A raised. Active multi-contributor project.
3. **MIT license confirmed file + repo level** — clean for IP-sale-readiness target (was tentative in Wave 4A).
4. **Kronos-mini 4.1M params** fits CPU inference scenarios on Cemini's existing infrastructure — alternative deployment surface emerges that Wave 4A didn't fully consider.

This is a textbook **status-upgrade-on-deeper-evaluation pattern**, mirroring (in opposite direction) the Wave 4A Vibe-Trading downgrade. **Together they establish**: wave evaluations are not stationary — peer-review acceptance, star-growth, and contributor-base shifts within 1-2 weeks legitimately re-rank tier.

### Cross-paper / cross-tool synthesis

- **Pair with `@sources/microsoft-qlib.md`** (Wave 4A Adopt): qlib provides data prep (Qlib pipeline) + backtest harness. Kronos provides foundation-model layer. The natural Cemini integration: Qlib data → KronosTokenizer → discrete tokens → custom-trained downstream predictor (NOT KronosPredictor as-shipped).
- **Pair with the MoE economics 5-paper set** (`@sources/incompressible-knowledge-probes-li-2026.md`, `@sources/moe-efficiency-leverage-tian-2026.md`, `@sources/moe-surpass-dense-equal-resource-li-2026.md`): Kronos is a deliberate **dense** architecture choice in the financial-LLM space, departing from the broader MoE trend Cemini's brain embraces. The paper's design rationale (likely smaller domain → dense fits) is worth deep-reading once Cemini commits to the tokenizer extract.
- **Pair with `@concepts/quant-finance.md`**: Kronos's hierarchical OHLCV→discrete-token quantization is a paradigm shift in financial modeling — first open-source foundation model in this space.

### Risks & open questions

1. **Kronos-small CPU inference latency** [NEEDS VERIFICATION 2026-04-30] — measure P99 inference latency of 24.7M-param model on standard AMD EPYC vCPU with PyTorch CPU optimizations. Determines if the model can meet trading execution speed limits if used as auxiliary signal source.

2. **pyqlib transitive license audit** [NEEDS VERIFICATION 2026-04-30] — Kronos finetune pipeline depends on pyqlib. Audit transitive deps to ensure no copyleft contaminates the IP-sale readiness profile. Use `pip-licenses` or equivalent.

3. **Binary Spherical Quantization claim** [CONFIRMED 2026-05-17] — the docx evaluation cites BSQ specifically. Verified against arXiv:2508.02739 §3.1 + Figure 3: the K-line Tokenizer is a Transformer-based autoencoder using a Binary Spherical Quantization (BSQ) layer — a variant of Look-up Free Quantization — projecting continuous OHLCVA latents onto learnable hyperplanes into a k-bit binary code, factorized into n=2 coarse/fine subtokens. The docx claim is accurate.

4. **Authors' production-readiness disclaimer is load-bearing** — "simplified example, not a production-ready quantitative trading system" is the authors' own caveat. Steal-from is the right verdict; Adopt-and-deploy is not.

5. **AI-generated code comments warning** — README explicitly notes that "many of the code comments within the `finetune/` directory were generated by an AI assistant (Gemini 2.5 Pro) for explanatory purposes. While they aim to be helpful, they may contain inaccuracies." Trust the code, audit the comments.

6. **Kronos-large is withheld** — the strongest model variant (499.2M params) is not released. If Cemini's evaluation hits a ceiling on the open variants, there's no upstream upgrade path.

### Cemini-side adoption assessment

**Decision**: **Steal-from the KronosTokenizer pattern. Do not deploy KronosPredictor in the production execution stack.**

Concrete next-steps:

1. **Read the paper** (arXiv:2508.02739) for the full tokenizer architecture details. Confirm the BSQ claim from the docx evaluation. ~2 hours.
2. **Reproduce KronosTokenizer** on a Cemini-scoped sample (e.g., 5 tickers × 1 year of intraday OHLCV). Measure compression ratio and reconstruction fidelity. ~1 day.
3. **Profile Kronos-mini CPU inference** on a CPX21-class machine to determine latency feasibility for an auxiliary-signal deployment. ~4 hours.
4. **If tokenizer is a good fit**: integrate into Cemini's data pipeline as a feature-engineering layer, NOT as a brain replacement. Output discrete tokens as additional context for DeepSeek-V4-Flash reasoning.
5. **Re-evaluate at next wave touch** for Adopt status if Cemini's experiments confirm tokenizer value.

License + IP-sale-readiness disposition: **clean**. MIT is on the clean list; pyqlib transitive sweep is the only outstanding gate.

### Citation

> Shi, Y., Fu, Z., Chen, S., Zhao, B., Xu, W., Zhang, C., & Li, J. (2025). *Kronos: A Foundation Model for the Language of Financial Markets*. arXiv:2508.02739 [q-fin.ST]. https://arxiv.org/abs/2508.02739 (AAAI 2026)
>
> shiyu-coder. (2025). *Kronos repository*. GitHub. https://github.com/shiyu-coder/Kronos (License: MIT; retrieved 2026-04-30 via Exa `crawling_exa`)

## Snippets

> **The repo's identity statement**:
>
> "Kronos is the first open-source foundation model for financial candlesticks (K-lines), trained on data from over 45 global exchanges." [Source: github.com/shiyu-coder/Kronos README, retrieved 2026-04-30]

> **The two-stage tokenizer architecture**:
>
> "Kronos is a family of decoder-only foundation models, pre-trained specifically for the 'language' of financial markets — K-line sequences. … It leverages a novel two-stage framework: 1. A specialized tokenizer first quantizes continuous, multi-dimensional K-line data (OHLCV) into hierarchical discrete tokens. 2. A large, autoregressive Transformer is then pre-trained on these tokens, enabling it to serve as a unified model for diverse quantitative tasks." [Source: github.com/shiyu-coder/Kronos README, retrieved 2026-04-30]

> **The authors' production-readiness disclaimer (load-bearing for the Steal-from verdict)**:
>
> "**Disclaimer:** This pipeline is intended as a demonstration to illustrate the finetuning process. It is a simplified example and not a production-ready quantitative trading system. A robust quantitative strategy requires more sophisticated techniques, such as portfolio optimization and risk factor neutralization, to achieve stable alpha." [Source: github.com/shiyu-coder/Kronos README, retrieved 2026-04-30]

> **The AAAI 2026 acceptance signal (drives the Wave 5A status upgrade)**:
>
> "🚩 [2025.11.10] Kronos has been accpeted by AAAI 2026." [Source: github.com/shiyu-coder/Kronos News section, retrieved 2026-04-30]

> **Wave 5A Steal-from rationale (URL 3 evaluation excerpt)**:
>
> "Steal-from — Extract the continuous-to-discrete OHLCV tokenization architecture and the PyTorch implementation of the KronosTokenizer. Deploying the actual Transformer model into the production execution stack violates the stability and predictability requirements of the trading platform; the authors explicitly state within the repository documentation that the provided fine-tuning pipeline is a 'simplified example and not a production-ready quantitative trading system.'" [Source: Codebase Evaluation for Trading & Wiki 4_30.docx URL 3]
