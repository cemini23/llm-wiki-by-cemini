#!/usr/bin/env bash
# K217 Phase-0 — OCR/HTR eval clones (SPDX-verified; total << 500MB)
# Policy: Transkribus remains sole product HTR. These are REFERENCE / pre-process / UI only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
clone() {
  local repo="$1" dest="$2"
  if [[ -d "$ADOPT/$dest/.git" ]]; then echo "exists $dest"; return; fi
  echo "clone $repo → $dest"
  git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dest"
}
# GO Extract / Integrate REFERENCE (size-capped)
clone Curiosity-Ai-BV/localOCR localOCR
clone baidu/Unlimited-OCR Unlimited-OCR
clone deepseek-ai/DeepSeek-OCR DeepSeek-OCR
clone githubharald/SimpleHTR SimpleHTR
clone ocrmypdf/OCRmyPDF OCRmyPDF
# skip franken_ocr (~219MB shallow) — wiki Watch only; MIT+OpenAI/Anthropic rider
clone MarkusNeusinger/kurrentschrift kurrentschrift
# EUPL — Reference-only (no product link)
clone AI-Riksarkivet/htrflow htrflow
# GPL-3.0 — isolate REFERENCE only (GuruWatcher ops UX; never link into proprietary)
clone trimstray/htrace.sh htrace.sh
# SKIP: PaddleOCR (~1.9GB), Umi-OCR (~275MB budget), EasyOCR (~158MB), GOT-OCR2.0 (null SPDX),
#       HTRPipeline (null SPDX), Nexdata Italian HTR dataset (null SPDX / commercial risk)
echo "=== sizes ==="
du -sh "$ADOPT"/* 2>/dev/null | sort -h
du -sh "$ADOPT"
