#!/usr/bin/env bash
# K146/K148 substrate steerability gate — enforceable checks before sandbox submit.
# AST projection (docs_cli) + ruff E9/F* (required) + forbidden-call scan.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

OUT_DIR="${1:-reports/researcher-round/substrate-latest}"
mkdir -p "$OUT_DIR"

export CEMINI_SUBSTRATE_REQUIRE_RUFF="${CEMINI_SUBSTRATE_REQUIRE_RUFF:-1}"

echo "==> K148 substrate gate (docs_cli audit + ruff required)"
if command -v uv >/dev/null 2>&1; then
  uv run python scripts/docs_cli.py audit --gate --out-dir "$OUT_DIR" | tee "${OUT_DIR}/substrate_gate.json"
else
  python3 scripts/docs_cli.py audit --gate --out-dir "$OUT_DIR" | tee "${OUT_DIR}/substrate_gate.json"
fi

echo "==> topology → ${OUT_DIR}/substrate_topology.txt"
echo "SUBSTRATE GATE OK"
