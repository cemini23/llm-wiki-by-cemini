#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PYTEST_ARGS=(
  tests/test_sandbox_tri_verifier.py
  tests/test_sandbox_rubric_epoch.py
  tests/test_tool_rl_collapse_detector.py
)
if [[ -f tests/test_sandbox_mechanical_invariants.py ]]; then
  PYTEST_ARGS+=(tests/test_sandbox_mechanical_invariants.py)
fi

uv run pytest "${PYTEST_ARGS[@]}" -q
echo "==> K134 rubric epoch:"
uv run python examples/sandbox_rubric_epoch.py --print
uv run python examples/sandbox_rubric_epoch.py --holdout
