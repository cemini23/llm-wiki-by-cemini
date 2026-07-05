#!/usr/bin/env bash
# K146 substrate steerability gate — enforceable checks before sandbox submit.
# AST projection (docs_cli) + optional ruff + forbidden-call scan.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

OUT_DIR="${1:-reports/researcher-round/substrate-latest}"
mkdir -p "$OUT_DIR"

echo "==> K146 substrate gate (docs_cli audit)"
if command -v uv >/dev/null 2>&1; then
  uv run python scripts/docs_cli.py audit --gate --out-dir "$OUT_DIR" | tee "${OUT_DIR}/substrate_gate.json"
else
  python3 scripts/docs_cli.py audit --gate --out-dir "$OUT_DIR" | tee "${OUT_DIR}/substrate_gate.json"
fi

echo "==> topology → ${OUT_DIR}/substrate_topology.txt"
echo "SUBSTRATE GATE OK"
