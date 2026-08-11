#!/usr/bin/env bash
# K232 Phase-0 — SHE only (<500MB)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AD="$ROOT/.local/adopts"
mkdir -p "$AD"
cd "$AD"

if [ -d SHE/.git ]; then echo "HAVE SHE"; du -sh SHE; exit 0; fi
echo "CLONE RainbowQTT/SHE"
git clone --depth 1 https://github.com/RainbowQTT/SHE.git SHE
du -sh SHE
echo "=== SKIP ==="
echo "jzzh2004/TongGuOCR — NO_LICENSE (~9MB) NO-GO; Watch patterns only"
echo "Macaron-V1 / DiffCoop — no public SPDX clone this batch"
echo "Robot harness paper — wont_wire runtime"
echo "=== DONE ==="
