#!/usr/bin/env bash
# Idempotent K103 Phase-0 laptop adoptions (2026-06-07).
# GO: pydantic-ai (pip).
# CONDITIONAL: asm clone reference; Polymarket_data sample only (manual).
# NO-GO skipped: application-skills, Poker-Query-Language.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k103-phase0}"
mkdir -p "$PHASE0"

echo "==> pydantic-ai (MIT) — GO"
if command -v pip3 >/dev/null 2>&1; then
  pip3 install --user -q "pydantic-ai" 2>/dev/null || pip3 install -q "pydantic-ai"
  python3 -c "import pydantic_ai; print('pydantic_ai OK')" || echo "WARN: import failed — check venv"
fi

echo "==> asm reference clone (CONDITIONAL-GO — do not symlink globally)"
ASM_DIR="$PHASE0/asm"
if [[ ! -d "$ASM_DIR/.git" ]]; then
  git clone --depth 1 https://github.com/luongnv89/asm.git "$ASM_DIR"
fi
echo "  clone: $ASM_DIR"

echo "==> Polymarket_data — manual sample only"
POLY_DATA="$PHASE0/Polymarket_data"
if [[ ! -d "$POLY_DATA/.git" ]]; then
  git clone --depth 1 https://github.com/SII-WANGZJ/Polymarket_data.git "$POLY_DATA"
fi
echo "  clone: $POLY_DATA (do not run full 107GB fetch without disk check)"

POLICY="$ROOT/.local/k103-phase0-adopt-notes.md"
if [[ ! -f "$POLICY" ]]; then
  mkdir -p "$ROOT/.local"
  cat >"$POLICY" <<'EOF'
# K103 Phase-0 adoptions — guardrails

- **pydantic-ai** — laptop typed-agent prototypes; prod via brief only; never install `pydantic-ai-gateway` (AGPL).
- **asm** — inspect clone under /tmp/k103-phase0/asm; isolated skill dirs only.
- **Polymarket_data** — sample ingest; librarian coordination before bulk.
- **pmxt** — no install here; prod brief staged after Phase-0 (CONDITIONAL-GO reaffirmed).
- **application-skills** — NO-GO (null repo license + Membrane lock-in).
- **Poker-Query-Language** — NO-GO for gambling/WC.
EOF
fi

echo "Done. Notes: $POLICY"
