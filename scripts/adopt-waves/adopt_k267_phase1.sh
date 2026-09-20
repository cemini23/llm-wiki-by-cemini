#!/usr/bin/env bash
# OSINT K267 Phase-1 verify — pages + mdc + REFERENCE clones.
# Dual-ID: OSINT K267. 0 product Integrate GO. FILE only.
# Do not swap /route. No xsp/pm scp. No LIVE Discord. Never npx github.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

echo "=== K267 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py

test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K267" .cursor/rules/osint-phase1-adopt-wires.mdc

# Source pages
test -f wiki/sources/eval-multi-wiki-revenue-opportunity-2026-09-20.md
test -f wiki/sources/eval-repository-revenue-opportunity-2026-09-20.md
test -f wiki/sources/substack-rss-wublock-2026-09-20-asia-top10-2026-09-20.md

# Hubs
test -f wiki/concepts/k267-eval-github-wave.md
test -f wiki/concepts/k267-atto-wave.md
test -f wiki/concepts/k267-ccc-jev-wave.md
test -f wiki/concepts/k267-cybersec-wave.md
test -f wiki/concepts/k267-newsletter-macro-wave.md
test -f wiki/concepts/k267-ood-stub-wave.md

# New entities
test -f wiki/entities/tools/openjev-razorback.md
test -f wiki/entities/tools/winnow.md
test -f wiki/entities/tools/foreman.md
test -f wiki/entities/tools/typesafe-mcp.md
test -f wiki/entities/tools/pi-jev.md
test -f wiki/entities/tools/jev-desktop.md

# Index / log
grep -q "K267 ingest (2026-09-20)" wiki/index.md
grep -q "K267 wave" wiki/log.md

# Jev brief add
grep -q "K267 add" briefs/2026-09-19_jev-atto.md
grep -q "K267 add" briefs/2026-09-19_jev-guruwatcher.md
grep -q "K267 add" briefs/2026-09-19_jev-ceminidfs.md
grep -q "K267 add" briefs/2026-09-19_jev-ceminiparlays.md

# REFERENCE clones
test -d .local/adopts/openjev-razorback
test -d .local/adopts/winnow
test -d .local/adopts/foreman
test -d .local/adopts/typesafe-mcp
test -d .local/adopts/pi-jev
test -d .local/adopts/jev-desktop

# Live jev-mcp unchanged
rg -c '"jev"' .cursor/mcp.json
test -x scripts/mcp_jev.sh

echo "0 product Integrate GO. jev-mcp laptop WIRE unchanged. Transkribus sole HTR."
echo "No skill evolve. No LIVE Discord. No xsp/pm scp. Do not swap /route."
echo "Never npx github. Never auto-arm. Never auto-merge truth.ged."
echo "=== DONE ==="
