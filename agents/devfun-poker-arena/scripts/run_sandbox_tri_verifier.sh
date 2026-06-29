#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

uv run pytest tests/test_sandbox_tri_verifier.py tests/test_sandbox_rubric_epoch.py -q
echo "==> K134 rubric epoch:"
uv run python examples/sandbox_rubric_epoch.py --print
uv run python examples/sandbox_rubric_epoch.py --holdout
