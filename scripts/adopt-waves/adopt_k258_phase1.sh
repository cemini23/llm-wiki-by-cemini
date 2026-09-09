#!/usr/bin/env bash
# OSINT K258 Phase-1 verify. FILE only. No new ledger rows.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K258 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K258" .cursor/rules/osint-phase1-adopt-wires.mdc
test -f wiki/entities/tools/execcritic.md
test -f wiki/entities/tools/e2b.md
test -f wiki/concepts/k258-harness-evolution-wave.md
echo "0 Integrate GO. execcritic FILE REFERENCE. E2B FILE REFERENCE deferred runtime."
echo "No skill auto-evolve. No LIVE Discord. No xsp/pm scp."
echo "=== DONE ==="
