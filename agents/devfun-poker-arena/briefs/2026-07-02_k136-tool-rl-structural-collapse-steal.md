## Target

`agents/devfun-poker-arena/` — Researcher Round bundle MCP training + harness regression.

## Summary

Steal **Tool-RL structural collapse** diagnosis (arXiv 2606.26027): pure RL on multi-step `arena-tool` loops can degenerate control-token formats without losing poker reasoning — fix with **interleaved SFT** on golden trajectories before any RL fine-tune.

## Body

### Collapse modes

| Mode | Harness signal |
|------|----------------|
| **Polluted** | Irrelevant special tokens in MCP JSON / tool blocks |
| **Collapsed** | Invalid or empty tool-call structure; submit fails |

Root cause: RL amplifies specific **control tokens** — not missing poker logic.

### Training recipe (research lane only)

1. Collect SFT corpus from successful bundle dry-runs (`join_pve` → `get_game_state` → `submit_action`).
2. **Interleave** SFT with RL — do not rely on synchronous SFT-then-RL only.
3. Optional: **Process Reflection Supervision** from logged failure trajectories.
4. OOD-test: schema drift + new `reasoning_text` rubric after training.

### Pairing

| Layer | Paper |
|-------|-------|
| Runtime hazards | K131 ToolBench-X |
| Verifier scoring | K132 Fara triad |
| Training stability | K136 Tool-RL (this) |
| Policy | Pure-code `decide()` unchanged |

### P0

- Add collapse detector to private bundle regression (format validity gate).
- Read MIT `hypasd-art/Tool-RL-Box` before any bundle-agent RL experiment.

## Shipped (2026-07-02)

| Artifact | Role |
|----------|------|
| `examples/tool_rl_collapse_detector.py` | Polluted vs collapsed mode detection on `message` / `reasoning` / `reasoning_text` |
| `examples/sandbox_tri_verifier.py` | `tool_rl_collapse` dimension in `score_action()` + trajectory aggregates; fail-closed in `all_pass` |
| `tests/test_tool_rl_collapse_detector.py` | Hazard injection tests (polluted control tokens, MCP tool leakage, empty JSON stubs) |
| `scripts/run_sandbox_tri_verifier.sh` | CI runner includes collapse detector tests |

**Deferred:** interleaved SFT training recipe (research lane only); Tool-RL-Box Phase-0 before bundle-agent RL.

## Sources

- [Source: arXiv:2606.26027 (retrieved 2026-07-02)]
- @wiki/sources/brief-k136-tool-rl-collapse-steals-2026-07-02.md
- @wiki/sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
