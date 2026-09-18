#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K264 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K264" .cursor/rules/osint-phase1-adopt-wires.mdc
test -f wiki/concepts/k264-eval-github-wave.md
test -f wiki/sources/eval-deep-research-url-stack-2026-09-18.md
rg -c '"jev"' .cursor/mcp.json
test -x scripts/mcp_jev.sh
echo "0 product Integrate GO. jev-mcp laptop WIRE. Transkribus sole HTR. No skill evolve. No LIVE Discord. No xsp/pm scp. No npx github."
echo "=== DONE ==="
