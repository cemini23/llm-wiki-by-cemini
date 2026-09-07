#!/usr/bin/env bash
# OSINT K256 Phase-1 verify. FILE only. No new ledger rows.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K256 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K256" .cursor/rules/osint-phase1-adopt-wires.mdc
test -f wiki/entities/tools/magnitude.md
test -f wiki/entities/tools/refactor-platform.md
test -f wiki/entities/tools/trailofbits-skills.md
test -f wiki/entities/tools/cve-mcp-server.md
echo "0 Integrate GO. No xsp/pm scp. No skill auto-evolve."
echo "=== DONE ==="
