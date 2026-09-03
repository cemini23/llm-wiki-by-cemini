#!/usr/bin/env bash
# OSINT K252 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K252 = 31 Aug 2026 inbox (8 arXiv + 6 newsletters).
# 0 new runtime Integrate GO. Verify SPDX via gh api before any Integrate.
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"

echo "=== SKIP (documented) — no verified public SPDX clone at Phase-0 ==="
echo "2608.28553 Logos — AAMAS 2027 paper; no official repo in preingest"
echo "2608.28363 EvoUndo — independent researchers; no public repo"
echo "2608.28433 Prove2Me — platform paper; google-research/prove2me 404"
echo "2608.28241 personalized skill routing — no repo in preingest"
echo "2608.28327 layered LLM defenses — policy only"
echo "2608.27575 bitcoin inverse options — quant paper only"
echo "2608.28397 GMMB riders — actuarial OOD stub"
echo "2608.28542 offline-verifiable accountability — policy K285 pattern only"
echo "maior/logosai-framework — different product; do not conflate with arXiv Logos paper"
echo "=== DONE — 0 clones ==="
