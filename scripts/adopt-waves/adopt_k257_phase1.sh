#!/usr/bin/env bash
# OSINT K257 Phase-1 verify. FILE only. No new ledger rows.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K257 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K257" .cursor/rules/osint-phase1-adopt-wires.mdc
test -f wiki/entities/tools/markitdown.md
test -f wiki/concepts/k257-eval-github-wave.md
echo "0 Integrate GO. markitdown FILE REFERENCE. Transkribus sole HTR."
echo "No skill auto-evolve. No LIVE Discord."
echo "=== DONE ==="
