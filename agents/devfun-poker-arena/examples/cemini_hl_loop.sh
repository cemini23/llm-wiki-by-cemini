#!/usr/bin/env bash
# Cemini HL analyst loop: analyze → LLM brief → preflight → deploy
#
# Self-play (EP VPIP, regression spots) is a DEPLOY GATE — not the trainer.
# RL / overnight sweeps on egress are separate; do not conflate with this loop.
#
# Usage:
#   ./examples/cemini_hl_loop.sh                    # analyze + brief (stop for patch)
#   ./examples/cemini_hl_loop.sh --from-prod        # fetch latest prod analyze
#   ./examples/cemini_hl_loop.sh --report path.txt  # skip fetch, build brief only
#   ./examples/cemini_hl_loop.sh --preflight-only   # after you patched decide()
#   ./examples/cemini_hl_loop.sh --deploy           # preflight + rsync prod (SKIP_ENV/CREDS default)
#   ./examples/cemini_hl_loop.sh --full             # longer self-play gate (600 hands)
#
# Deploy convention (Cursor agent): always --deploy after HL patch; prod keeps .env + creds
# (CEMINI_SKIP_ENV=1 CEMINI_SKIP_CREDS=1 set in deploy_to_cemini_prod.sh).
#
# After step 2, open reports/hl-loop/latest_brief.md in Cursor and patch
# examples/cemini_decide.py per prompts/cemini_hl_analyst_prompt.md
set -euo pipefail

# Cross-project LLM routing (DeepSeek primary, OpenRouter fallback on quota).
_OSINT_ROOT="${CEMINI_OSINT_ROOT:-$HOME/Desktop/OSINT WORKSPACE}"
_LLM_SOURCE="$_OSINT_ROOT/scripts/source_llm_routing_env.sh"
if [[ -f "$_LLM_SOURCE" ]]; then
  # shellcheck disable=SC1090
  source "$_LLM_SOURCE"
fi

cd "$(dirname "$0")/.."
AGENT_DIR="$(pwd)"

HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
MATCH="${ARENA_LOBBY_COMPETITION_ID:-cmpy2qy65002ud9ej6b7jjq0l}"
TOP="${HL_ANALYZE_TOP:-15}"
ROUND="${HL_ROUND:-1}"
REPORTS="${AGENT_DIR}/reports/hl-loop"
ANALYZE_DIR="${AGENT_DIR}/reports/analyze"
LATEST_REPORT="${REPORTS}/latest_analyze.txt"
BRIEF="${REPORTS}/latest_brief.md"
STATE_FILE="${REPORTS}/state.json"
HL_RERUN_DELTA="${CEMINI_HL_RERUN_DELTA:-50}"
HANDLE="${CEMINI_AGENT_HANDLE:-cemini_wiki_poker}"

FROM_PROD=0
REPORT_ARG=""
PREFLIGHT_ONLY=0
DEPLOY=0
FULL_GATE=0
SKIP_BRIEF=0

usage() {
  sed -n '2,18p' "$0"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --from-prod) FROM_PROD=1; shift ;;
    --report) REPORT_ARG="${2:-}"; shift 2 ;;
    --preflight-only) PREFLIGHT_ONLY=1; shift ;;
    --deploy) DEPLOY=1; PREFLIGHT_ONLY=1; shift ;;
    --full) FULL_GATE=1; shift ;;
    --skip-brief) SKIP_BRIEF=1; shift ;;
    --round) ROUND="${2:-1}"; shift 2 ;;
    --match) MATCH="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

mkdir -p "${REPORTS}" "${ANALYZE_DIR}"

step_ok() {
  echo ""
  echo "✓ $1"
}

step_fail() {
  echo ""
  echo "✗ $1" >&2
  exit 1
}

fetch_hand_count() {
  if [[ "${FROM_PROD}" -eq 1 ]] || [[ "${DEPLOY}" -eq 1 ]] || [[ "${PREFLIGHT_ONLY}" -eq 1 && -z "${REPORT_ARG}" ]]; then
    ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"
export ARENA_LOBBY_COMPETITION_ID="${MATCH}"
export CEMINI_AGENT_HANDLE="${HANDLE}"
./venv/bin/python examples/cemini_hl_hand_count.py --match "${MATCH}"
REMOTE
    return
  fi
  uv run python examples/cemini_hl_hand_count.py --match "${MATCH}"
}

write_hl_state() {
  local phase="$1"
  local hands="$2"
  local round_num="$3"
  local rerun_at=$((hands + HL_RERUN_DELTA))
  mkdir -p "${REPORTS}"
  uv run python - <<PY "${STATE_FILE}" "${phase}" "${hands}" "${round_num}" "${rerun_at}" "${HL_RERUN_DELTA}" "${MATCH}" "${AGENT_DIR}"
import json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

path, phase, hands, round_num, rerun_at, delta, comp, agent_dir = sys.argv[1:9]
state_path = Path(path)
prev = {}
if state_path.is_file():
    try:
        prev = json.loads(state_path.read_text())
    except Exception:
        prev = {}
try:
    sha = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=agent_dir,
        stderr=subprocess.DEVNULL,
        text=True,
    ).strip()
except Exception:
    sha = prev.get("commit", "unknown")

state = {
    "round": int(round_num),
    "hands": int(hands),
    "rerun_at_hands": int(rerun_at),
    "rerun_delta": int(delta),
    "competition_id": comp,
    "phase": phase,
    "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "commit": sha,
}
if phase in ("deployed", "preflight"):
    state["last_deploy_hands"] = int(hands)
    state["last_deploy_round"] = int(round_num)
state_path.write_text(json.dumps(state, indent=2) + "\n")
PY
}

print_hl_hand_line() {
  local hands="$1"
  local round_num="$2"
  local rerun_at=$((hands + HL_RERUN_DELTA))
  local prev_hands=""
  local prev_round=""
  if [[ -f "${STATE_FILE}" ]]; then
    prev_hands="$(uv run python -c "import json; d=json.load(open('${STATE_FILE}')); print(d.get('last_deploy_hands', d.get('hands', '')))" 2>/dev/null || true)"
    prev_round="$(uv run python -c "import json; d=json.load(open('${STATE_FILE}')); print(d.get('last_deploy_round', d.get('round', '')))" 2>/dev/null || true)"
  fi
  echo ""
  echo "  HL round ${round_num} │ hands=${hands} │ rerun at hands≥${rerun_at} (+${HL_RERUN_DELTA})"
  if [[ -n "${prev_hands}" && -n "${prev_round}" && "${prev_round}" != "${round_num}" ]]; then
    echo "  (last deploy: HL R${prev_round} @ hands=${prev_hands})"
  fi
  echo "  state → ${STATE_FILE}"
}

print_hl_next_steps() {
  local round_num="$1"
  local hands="$2"
  local rerun_at=$((hands + HL_RERUN_DELTA))
  echo ""
  echo "────────────────────────────────────────────────────────────"
  echo "  NEXT: Open ${BRIEF}"
  echo "  Patch ONE leak in examples/cemini_decide.py"
  echo "  Then:  ./examples/cemini_hl_loop.sh --preflight-only --round ${round_num}"
  echo "  Deploy: ./examples/cemini_hl_loop.sh --deploy --round ${round_num}"
  print_hl_hand_line "${hands}" "${round_num}"
  echo ""
  echo "  Re-analyze when hands ≥ ${rerun_at}:"
  echo "    ./examples/cemini_hl_loop.sh --from-prod --round $((round_num + 1))"
  echo "────────────────────────────────────────────────────────────"
}

# ── Step 1: ANALYZE ─────────────────────────────────────────────────────────
fetch_analyze() {
  if [[ -n "${REPORT_ARG}" ]]; then
    cp -f "${REPORT_ARG}" "${LATEST_REPORT}"
    step_ok "Using analyze report: ${REPORT_ARG}"
    return
  fi

  if [[ "${FROM_PROD}" -eq 1 ]]; then
    echo "==> [1/4] Fetch analyze from ${HOST} (competition ${MATCH})"
    ssh "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"
export ARENA_LOBBY_COMPETITION_ID="${MATCH}"
./venv/bin/python examples/arena_monitor.py analyze --match "${MATCH}" --top "${TOP}" \
  --reports-dir "${REMOTE_DIR}/reports"
REMOTE
    REMOTE_LATEST="$(ssh "${HOST}" "ls -t ${REMOTE_DIR}/reports/analyze/*.txt 2>/dev/null | head -1")"
    if [[ -z "${REMOTE_LATEST}" ]]; then
      step_fail "No analyze report on prod"
    fi
    scp -q "${HOST}:${REMOTE_LATEST}" "${LATEST_REPORT}"
    step_ok "Prod analyze → ${LATEST_REPORT}"
    return
  fi

  echo "==> [1/4] Local analyze (competition ${MATCH})"
  if [[ ! -f "${AGENT_DIR}/.arena-credentials" ]] && [[ -z "${ARENA_API_KEY:-}" ]]; then
    step_fail "No .arena-credentials — use --from-prod or --report path.txt"
  fi
  uv run python examples/analyze.py --match "${MATCH}" --top "${TOP}" --out "${LATEST_REPORT}"
  step_ok "Local analyze → ${LATEST_REPORT}"
}

if [[ "${PREFLIGHT_ONLY}" -eq 0 ]]; then
  fetch_analyze

  # ── Step 2: BRIEF (LLM patch packet) ────────────────────────────────────────
  if [[ "${SKIP_BRIEF}" -eq 0 ]]; then
    echo ""
    echo "==> [2/4] Build HL analyst brief (OSINT shape → ${BRIEF})"
    uv run python examples/cemini_hl_brief.py \
      --report "${LATEST_REPORT}" \
      --out "${BRIEF}" \
      --round "${ROUND}" \
      --match "${MATCH}"
    step_ok "Brief ready — patch cemini_decide.py in Cursor, then re-run with --preflight-only"

    HANDS="$(fetch_hand_count || echo 0)"
    write_hl_state "analyze" "${HANDS}" "${ROUND}"
    print_hl_next_steps "${ROUND}" "${HANDS}"
    exit 0
  fi
fi

# ── Step 3: PREFLIGHT (gate) ──────────────────────────────────────────────────
echo ""
echo "==> [3/4] Preflight gate (pytest + EP VPIP self-play + dry-run)"
if [[ "${FULL_GATE}" -eq 1 ]]; then
  ./scripts/cemini_preflight.sh --full
else
  ./scripts/cemini_preflight.sh
fi
step_ok "Preflight PASS"

# ── Step 4: DEPLOY (optional) ─────────────────────────────────────────────────
if [[ "${DEPLOY}" -eq 1 ]]; then
  echo ""
  echo "==> [4/4] Deploy to ${HOST}"
  ./deploy/deploy_to_cemini_prod.sh
  step_ok "Deployed — monitor: ssh ${HOST} journalctl -u cemini-devfun-poker-lobby -f"
  HANDS="$(fetch_hand_count || echo 0)"
  write_hl_state "deployed" "${HANDS}" "${ROUND}"
  print_hl_hand_line "${HANDS}" "${ROUND}"
  echo ""
  echo "Re-analyze when hands ≥ $((HANDS + HL_RERUN_DELTA)):"
  echo "  ./examples/cemini_hl_loop.sh --from-prod --round $((ROUND + 1))"
else
  echo ""
  echo "==> [4/4] Deploy skipped (pass --deploy to rsync prod)"
  if [[ "${PREFLIGHT_ONLY}" -eq 1 ]]; then
    HANDS="$(fetch_hand_count || echo 0)"
    write_hl_state "preflight" "${HANDS}" "${ROUND}"
    print_hl_hand_line "${HANDS}" "${ROUND}"
  fi
fi

echo ""
echo "HL LOOP OK (round ${ROUND})"
