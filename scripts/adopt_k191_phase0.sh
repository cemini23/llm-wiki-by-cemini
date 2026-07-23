#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="${ROOT}/.local/adopts"
REPORT="${ROOT}/.local/reports/k191-phase0-$(date +%Y-%m-%d).md"
SIZE_MB=$(du -sm "$ADOPTS" | awk '{print $1}')
mkdir -p "$(dirname "$REPORT")"
cat >"$REPORT" <<R
# K191 Phase-0 — $(date +%Y-%m-%d)

## Extract GO
- stiggio/skills (MIT) → TipDrop entitlements skills
- sassman/license-guard-rs (Apache-2.0) → Atto Ed25519 offline reference

## Watch / fail
- ph4n70mr1ddl3r/aidlc — NOASSERTION; content = IT Department Manager (eval AI-DLC misfit)
- alexisfox7/PRO-LONG — GitHub 404
- LicenseSeat — commercial SaaS (no clone)

**Disk:** ~${SIZE_MB} MB (cap 500).
R
echo "Wrote $REPORT (${SIZE_MB} MB)"
du -sh "$ADOPTS"/{stiggio-skills,license-guard-rs,aidlc} 2>/dev/null
