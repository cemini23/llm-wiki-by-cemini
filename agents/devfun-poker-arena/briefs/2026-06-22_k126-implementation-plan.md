# K126 Implementation Plan — Kuhn Poker SFT Reference (REFERENCE-only)

## Target

`agents/devfun-poker-arena/` — offline reference tooling; wiki concept filing.

## Summary

Ship parse/compare utilities for HF Kuhn poker SFT trace format vs Arena `decide()` schema; **REFERENCE-only** (NO LICENSE on HF cards).

**Brief:** `briefs/2026-06-22_k126-kuhn-poker-sft-reference.md`  
**Regime:** Offline curriculum reference — **no HF training**, **no weight import**, **no runtime LLM decide()**.

## P0 deliverables

| # | Artifact | Purpose |
|---|----------|---------|
| 1 | `examples/kuhn_sft_format_reference.py` | Parse Kuhn SFT trace structure; compare vs Arena `decide()` schema; license gate |
| 2 | `tests/fixtures/kuhn_sft_samples.json` | Embedded HF row snippets (CI, no network) |
| 3 | `tests/test_kuhn_sft_format_reference.py` | Unit tests for parsers + format matrix |
| 4 | `references/kuhn-poker-sft-curriculum.md` | Human-readable steal matrix + regime disclosure |
| 5 | `scripts/run_kuhn_sft_reference_analysis.sh` | Offline runner → `reports/kuhn-sft-reference/summary.json` |

## P1 (optional spike, not blocking)

- `compare_to_regression_spot()` — map Kuhn “minimal decision” discipline to one `RegressionSpot` id (structural only, not action parity).
- HF live sample fetch (`datasets-server` API) behind `--live` flag; default uses fixtures.

## API design (`kuhn_sft_format_reference.py`)

```python
KUHN_SFT_DATASETS = [
    {"id": "the-acorn-ai/kuhn-poker-Qwen-QwQ-32B-5000-sft", "license": "NO LICENSE"},
    {"id": "spiral-rl/Spiral-Kuhn-Poker-Qwen3-32B-SFT", "license": "NO LICENSE"},
]

def parse_kuhn_messages(messages: list[dict]) -> KuhnTraceParsed
def arena_decide_schema() -> dict  # action, amount?, message, reasoning≤150
def format_comparison_matrix() -> list[dict]  # dimension, kuhn, arena, steal?
def analyze_trace(messages) -> dict  # boxed_action, thinking_chars, available_actions
def build_reference_report(samples) -> dict  # JSON-serializable summary
def assert_reference_only() -> None  # raises if TRAINING_MODE env set
```

### Parsing rules

- **User:** extract card (`Your card is: X`), `available actions` list `[check], [bet]`, round id.
- **Assistant:** extract `\boxed{[action]}`; measure `<think>` length; flag if no boxed answer.
- **Arena mapping:** Kuhn `[bet]` → `bet`/`raise`; `[check]` → `check`; amounts implicit (1-chip Kuhn) — document **not portable** to NLHE sizing.

### Steal matrix (document in reference md)

| Borrow | Skip |
|--------|------|
| Short YAML `reasoning` discipline (≤150) vs essay CoT | Long CoT in submit path |
| Explicit legal-action enumeration in prompt | `\boxed{}` action format |
| Step structure before action | Kuhn 3-card deck assumptions |
| Minimal-game curriculum ordering | Dataset weights / SFT corpus |

## Tests

1. `parse_kuhn_messages` on fixture JSON → boxed `[bet]` for Q-hand sample.
2. `format_comparison_matrix()` returns ≥8 rows with `steal` column.
3. `reasoning` length policy: arena max 150; kuhn samples exceed → documented gap.
4. License constants: both datasets `NO LICENSE`.
5. `build_reference_report` on fixtures produces `dataset_count`, `steal_candidates`.

## Out of scope (explicit)

- `huggingface_hub` download / training scripts
- Changes to `cemini_decide.py` or regression oracle actions
- Wiki ingest (separate OSINT session if user requests)

## Verification

```bash
uv run pytest tests/test_kuhn_sft_format_reference.py -q
bash scripts/run_kuhn_sft_reference_analysis.sh
```

## Parallel work split

- **Worker A:** Python module + fixtures + tests
- **Worker B:** `references/kuhn-poker-sft-curriculum.md` + shell runner + cross-link in `references/decide-function.md` (one line under Don't)

## Sources

- @agents/devfun-poker-arena/briefs/2026-06-22_k126-kuhn-poker-sft-reference.md
- [Source: https://huggingface.co/datasets/the-acorn-ai/kuhn-poker-Qwen-QwQ-32B-5000-sft (retrieved 2026-06-22)]
- [Source: https://huggingface.co/datasets/spiral-rl/Spiral-Kuhn-Poker-Qwen3-32B-SFT (retrieved 2026-06-22)]
