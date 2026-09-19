#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
echo "=== K265 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py
test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K265" .cursor/rules/osint-phase1-adopt-wires.mdc
test -f wiki/concepts/k265-eval-github-wave.md
test -f wiki/concepts/k265-ccc-jev-wave.md
test -f wiki/sources/eval-revenue-opportunity-url-2026-09-19.md
test -f wiki/sources/newsletter-rss-latent-space-2026-09-19-jev-clones-2026-09-19.md
rg -c '"jev"' .cursor/mcp.json
test -x scripts/mcp_jev.sh
echo "0 product Integrate GO. jev-mcp laptop WIRE unchanged. Transkribus sole HTR. No skill evolve. No LIVE Discord. No xsp/pm scp. Do not swap /route."
echo "=== DONE ==="
