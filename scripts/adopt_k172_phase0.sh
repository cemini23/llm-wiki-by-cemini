#!/usr/bin/env bash
set -euo pipefail
echo "K172 Phase-0"
echo "No new Integrate/Extract installs this batch."
echo "OVERRIDE: xai-org/grok-build + plugin — CONDITIONAL (repo upload privacy incident Jul 2026)"
gh api repos/xai-org/grok-build --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★"' 2>/dev/null || true
echo "Lila Sciences: Watch/Context only — no clone"
echo "WasmForge / RAPTOR / harness-kit: cybersec Context — no OSINT adopt"
echo "Local adopts: none new. Prior .local/adopts/grok-build = reference only."
echo "Briefs: xsp+pm scp; TipDrop STOP; CCC halt; cybersec; gambling; poker no-fit"
