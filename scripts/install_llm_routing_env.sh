#!/usr/bin/env bash
# Install ~/.cemini/llm-routing.env from OSINT template (does not overwrite).
set -euo pipefail

_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
_REPO_ROOT="$(cd "$_SCRIPT_DIR/.." && pwd)"
_TEMPLATE="$_REPO_ROOT/config/llm-routing.env.example"
_TARGET="${CEMINI_LLM_ROUTING_ENV:-$HOME/.cemini/llm-routing.env}"

mkdir -p "$(dirname "$_TARGET")"
if [[ -f "$_TARGET" ]]; then
  echo "llm-routing: already exists — $_TARGET (not modified)"
else
  cp "$_TEMPLATE" "$_TARGET"
  echo "llm-routing: created $_TARGET"
fi

# Merge keys from repo .env when placeholders are empty (never prints values).
python3 - "$_REPO_ROOT/.env" "$_TARGET" <<'PY' 2>/dev/null || true
import re, sys
from pathlib import Path
src, tgt = Path(sys.argv[1]), Path(sys.argv[2])
if not src.is_file() or not tgt.is_file():
    raise SystemExit(0)
keys = ("DEEPSEEK_API_KEY", "OPENROUTER_API_KEY")
found = {}
for line in src.read_text().splitlines():
    if "=" not in line or line.strip().startswith("#"):
        continue
    k, _, v = line.partition("=")
    k, v = k.strip(), v.strip()
    if k in keys and v:
        found[k] = v
text = tgt.read_text()
for k, v in found.items():
    pat = re.compile(rf"^{re.escape(k)}=.*$", re.M)
    if pat.search(text):
        if not pat.search(text).group(0).endswith("=") and pat.search(text).group(0) != f"{k}=":
            if re.search(rf"^{k}=\s*$", text, re.M) or re.search(rf"^{k}=$", text, re.M):
                text = pat.sub(f"{k}={v}", text, count=1)
    else:
        text += f"\n{k}={v}\n"
tgt.write_text(text)
PY

echo "llm-routing: edit $_TARGET — set OPENROUTER_API_KEY if missing"
echo "Per session:  source $_REPO_ROOT/scripts/source_llm_routing_env.sh"
