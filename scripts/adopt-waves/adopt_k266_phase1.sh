#!/usr/bin/env bash
# OSINT K266 Phase-1 verify — pages + mdc only. No clones, no network.
# Dual-ID: OSINT K266. 0 product Integrate GO. FILE only.
# Do not swap /route. No live desk. No xsp/pm scp. No LIVE Discord.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

echo "=== K266 Phase-1 verify ==="
python3 scripts/wire_ledger_check.py

test -f .cursor/rules/osint-phase1-adopt-wires.mdc
grep -q "OSINT K266" .cursor/rules/osint-phase1-adopt-wires.mdc

# Source pages
test -f wiki/sources/x-article-sydneyrunkle-harness-jev-2026-09-19.md
test -f wiki/sources/x-article-0xmovez-jev-engineering-2026-09-19.md
test -f wiki/sources/x-article-shreyanshpatni-agent-harness-2026-09-19.md
test -f wiki/sources/x-article-borjafat-internal-linking-2026-09-19.md
test -f wiki/sources/x-post-parcadei-jev-skill-classify-2026-09-19.md
test -f wiki/sources/x-article-buildwithpublic-0dte-2026-09-19.md

# Hubs
test -f wiki/concepts/k266-ccc-jev-x-wave.md
test -f wiki/concepts/k266-seo-x-voice-wave.md
test -f wiki/concepts/k266-finance-0dte-wave.md
test -f wiki/concepts/k266-ood-stub-wave.md

# Entity stub + index/log
test -f wiki/entities/tools/langchain-typesafe.md
grep -q "K266 ingest (2026-09-19)" wiki/index.md
grep -q "K266 wave" wiki/log.md

# Jev brief add + SEO voice brief
grep -q "K266 add" briefs/2026-09-19_jev-atto.md
grep -q "K266 add" briefs/2026-09-19_jev-guruwatcher.md
grep -q "K266 add" briefs/2026-09-19_jev-ceminidfs.md
grep -q "K266 add" briefs/2026-09-19_jev-ceminiparlays.md
test -f briefs/2026-09-19_k266-seo-voice.md

echo "0 product Integrate GO. FILE only. jev-mcp laptop WIRE unchanged. Do not swap /route."
echo "No live desk. No xsp/pm scp. No LIVE Discord. Never npx github:jkudish/jev-mcp."
echo "=== DONE ==="
