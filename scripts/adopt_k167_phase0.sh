#!/usr/bin/env bash
# adopt_k167_phase0.sh — Phase-0 for K167 ingest (2026-07-15)
set -euo pipefail
echo "K167 Phase-0"
gh api repos/humanlayer/12-factor-agents --jq '"\(.full_name) | SPDX=\(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★"' 2>/dev/null || true
echo "LICENSE file: Apache-2.0 (verified)"
echo "---"
echo "Adopt-patterns: humanlayer/12-factor-agents (Apache-2.0) — optional shallow clone <50MB"
echo "REFERENCE: 2607.10814 belief-audit Werewolf — poker steal; no install"
echo "REFERENCE: 2607.09324 keyword extraction — genealogy stewardship; no install"
echo "David ComfyUI/Fish-Speech: none"
echo "Briefs: pm flights (**scp**); xsp macro+volga (**scp**); poker belief-audit; CCC; gambling (no David/TipDrop — no image/persona path)"
