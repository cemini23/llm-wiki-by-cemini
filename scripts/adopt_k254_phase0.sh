#!/usr/bin/env bash
# OSINT K254 Phase-0 — budget <500MB new clones (shallow, --depth 1).
# Dual-ID: OSINT K254 = 2 Sep 2026 inbox (7 arXiv + 3 eval docx + 5 newsletters + 1 SEO).
# Skip: Multi-Project URL Revenue Evaluation.docx (DUPLICATE → last30days-skill).
set -euo pipefail
export GIT_TERMINAL_PROMPT=0
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"

echo "=== SKIP (documented) — no verified paper-matched SPDX clone ==="
echo "2609.01437 HarnessDev — no official arXiv-matched repo"
echo "2609.01481 Harness-of-Harness — 16MB paper; no public repo"
echo "2609.01600 CordisBench — no public repo"
echo "2608.26263 SKILL.state — no public repo"
echo "2608.26133 Agent Seer — no public repo (unrelated SEER repos)"
echo "2609.00630 fading event — astronomy OOD stub"
echo "2609.01183 VRP nuclear/energy — quant wiki-only"
echo "Eval docx batches — URL lists only; SPDX spot-check at Integrate time"
echo "=== DUPLICATE fold ==="
echo "Multi-Project URL Revenue Evaluation.docx → @sources/last30days-skill-mvanhorn.md (archive only)"
echo "=== DONE — 0 new clones ==="
