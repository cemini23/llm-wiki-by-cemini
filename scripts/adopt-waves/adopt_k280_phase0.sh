#!/usr/bin/env bash
# OSINT K280 Phase-0 — HTR candidate audit + Monte Carlo row triage.
# Dual-ID: OSINT K280 = 3 Oct 2026 inbox (single eval docx, 20 rows).
#
# Operator directive: licences are less important than improving the stacks.
# For Atto specifically: do not stay on Transkribus by precedent. If a candidate
# wins on a measured task, adopt it. Evidence decides.
#
# This wave ran a real Phase-0 audit: clone + inspect + rank. See
# wiki/concepts/k280-atto-htr-wave.md for the verdict.
set -euo pipefail
echo "=== K280 Phase-0 ==="
echo "=== ATTO HTR CANDIDATES (evidence decides, not precedent) ==="
echo "mittagessen/kraken          engine   Apache-2.0  baseline segmentation, Apple Silicon  STRONGEST"
echo "githubharald/HTRPipeline    pipeline MIT         full-page layout + line detection"
echo "githubharald/SimpleHTR      model    MIT         minimal CRNN-CTC"
echo "KadenMc/PreprocessingHTR    preproc  unverified  Otsu/Sauvola binarization, deskew"
echo "HTR-United/cremma-medieval  data     CC-BY       medieval Latin ground truth + Kraken baselines"
echo "Intellindust-AI-Lab/HTR-VT  model    unverified  ViT, Watch"
echo "raphael-baena/DTLR          model    unverified  polygon line detection, Watch"
echo "him4318/Transformer-ocr     model    unverified  Context"
echo "=== CEMINIDFS ROWS (this wave DOES apply) ==="
echo "nchopin/particles           Extract  particle filter for live late-swap updating"
echo "neurotrader888/mcpt         Extract  permutation tests for overfitting"
echo "=== PASS (no domain hook) ==="
echo "MSM weights / collision-avoid / jmctf / monte-carlo-experiments / Probability-Simulation"
echo "=== DONE ==="
echo "No clone in this script. The audit agent cloned to a temp dir and reported."
echo "Nothing vendored. Do not swap /route. No auto-submit. No live order."
echo "A human still types the ticket."
