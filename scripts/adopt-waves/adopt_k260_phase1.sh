#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K260 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K260" .cursor/rules/osint-phase1-adopt-wires.mdc
test -f wiki/concepts/k260-harness-evolution-wave.md
test -f wiki/sources/arxiv-2609.11677-ecdysis-runtime-harness-2026-09-13.md
echo "0 Integrate GO. No skill auto-evolve. No LIVE Discord. No xsp/pm scp."
echo "=== DONE ==="
