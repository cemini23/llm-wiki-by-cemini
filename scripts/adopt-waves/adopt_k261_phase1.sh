#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K261 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K261" .cursor/rules/osint-phase1-adopt-wires.mdc
test -f wiki/concepts/k261-eval-github-wave.md
test -f wiki/sources/eval-multi-wiki-stack-revenue-2026-09-15.md
echo "0 Integrate GO. No MCP. No skill evolve. No LIVE Discord. No xsp/pm scp."
echo "=== DONE ==="
