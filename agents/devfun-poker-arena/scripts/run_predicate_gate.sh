#!/usr/bin/env bash
# K149 ADVENT predicate gate — verified predicates must not fire (no live leak).
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

OUT="reports/predicates/gate-$(date -u +%Y%m%dT%H%M%SZ).json"
mkdir -p reports/predicates

echo "==> K149 predicate invention gate (verified predicates vs HU spots)"
if command -v uv >/dev/null 2>&1; then
  uv run python scripts/predicate_invention.py --gate --json-out "$OUT"
else
  python3 scripts/predicate_invention.py --gate --json-out "$OUT"
fi

echo "PREDICATE GATE OK → ${OUT}"
