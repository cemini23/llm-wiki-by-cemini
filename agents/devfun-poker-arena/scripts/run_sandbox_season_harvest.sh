#!/usr/bin/env bash
# Pull full sandbox beta S1 dataset when PvP reaches target hands (default 10k).
#
# Captures everything needed for next-day tuning:
#   - All submission status snapshots (poll API)
#   - Leaderboard + agent-stats
#   - Full competition export (submissions per top agent + hero)
#   - Researcher trajectory axis summary
#   - Local gate copy + today's briefs manifest
#
# Usage:
#   bash scripts/run_sandbox_season_harvest.sh              # wait until 10k then harvest
#   bash scripts/run_sandbox_season_harvest.sh --now      # harvest immediately (partial OK)
#   bash scripts/run_sandbox_season_harvest.sh --poll-only  # status check, no export
#
# Env:
#   ARENA_RESEARCHER_COMP_ID  (default: cmqqqs05i1u7ppnu7stqbw7d8)
#   SANDBOX_TARGET_HANDS      (default: 10000)
#   SANDBOX_POLL_INTERVAL_S   (default: 300)
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${AGENT_DIR}"

PY=("${AGENT_DIR}/venv/bin/python")
if [[ ! -x "${PY[0]}" ]]; then
  PY=("$(command -v uv)" run python)
fi

COMP="${ARENA_RESEARCHER_COMP_ID:-cmqqqs05i1u7ppnu7stqbw7d8}"
HERO="${ARENA_HERO_HANDLE:-cemini_wiki_poker}"
TARGET_HANDS="${SANDBOX_TARGET_HANDS:-10000}"
POLL_S="${SANDBOX_POLL_INTERVAL_S:-300}"
MODE="wait"
SUBMISSION_IDS="${SANDBOX_SUBMISSION_IDS:-}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --now) MODE="now"; shift ;;
    --poll-only) MODE="poll"; shift ;;
    --competition-id) COMP="$2"; shift 2 ;;
    --target-hands) TARGET_HANDS="$2"; shift 2 ;;
  esac
done

TS=$(date -u +%Y%m%dT%H%M%SZ)
OUT_ROOT="reports/sandbox-season/${COMP}/${TS}"
mkdir -p "$OUT_ROOT"

poll_submissions() {
  export SANDBOX_TARGET_HANDS="$TARGET_HANDS"
  "${PY[@]}" - <<'PY' "$COMP" "$OUT_ROOT" "$SUBMISSION_IDS" "$AGENT_DIR"
import json, os, sys
from pathlib import Path
import httpx

comp, out_root, ids_env, agent_root = sys.argv[1], Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4])
root = agent_root
creds = json.loads((root / ".arena-credentials").read_text())
base = os.environ.get("ARENA_API_BASE", "https://arena.dev.fun/api/arena").rstrip("/")
h = {"x-arena-api-key": creds["apiKey"]}

ids = [x.strip() for x in ids_env.split(",") if x.strip()]
if not ids:
    ids = [
        "59e6c951-95ac-44f2-92ae-2794b9ed08ab",
        "1a945a9e-8140-45a9-9a27-fed6b46dd4a0",
        "308fdcbc-43b7-4ab2-ade7-0fb172e997f1",
    ]

snap = {"competitionId": comp, "submissions": []}
max_hands = 0
done = False
for sid in ids:
    try:
        r = httpx.get(f"{base}/submissions/{sid}", headers=h, timeout=60)
        if r.status_code != 200:
            snap["submissions"].append({"id": sid, "error": r.text[:200]})
            continue
        d = r.json()
        pvp = d.get("pvp") or {}
        ch = int(pvp.get("completedHands") or d.get("completedHands") or 0)
        th = int(pvp.get("targetHands") or d.get("targetHands") or 0)
        max_hands = max(max_hands, ch)
        snap["submissions"].append(d)
    except Exception as e:
        snap["submissions"].append({"id": sid, "error": str(e)})

lb = httpx.get(f"{base}/competition/leaderboard?competitionId={comp}&limit=50", headers=h, timeout=60)
snap["leaderboard"] = lb.json() if lb.status_code == 200 else {"error": lb.text[:300]}
me = httpx.get(f"{base}/agent/me", headers=h, timeout=30)
snap["agent_me"] = me.json() if me.status_code == 200 else {"error": me.text[:200]}

out_root.mkdir(parents=True, exist_ok=True)
(out_root / "arena_snapshot.json").write_text(json.dumps(snap, indent=2) + "\n")
print(json.dumps({"max_completed_hands": max_hands, "target": int(os.environ.get("SANDBOX_TARGET_HANDS", "10000"))}))
PY
}

wait_for_target() {
  echo "==> Waiting for hero PvP ≥ ${TARGET_HANDS} hands (poll every ${POLL_S}s)…"
  while true; do
  meta=$(poll_submissions)
  max_h=$(echo "$meta" | python3 -c "import json,sys; print(json.load(sys.stdin).get('max_completed_hands',0))")
  echo "    … max completed hands among tracked submissions: ${max_h} / ${TARGET_HANDS}"
  if [[ "$max_h" -ge "$TARGET_HANDS" ]]; then
    echo "==> Target hands reached."
    break
  fi
  sleep "$POLL_S"
  done
}

if [[ "$MODE" == "wait" ]]; then
  wait_for_target
else
  poll_submissions
fi

if [[ "$MODE" == "poll" ]]; then
  echo "Poll-only — snapshot → ${OUT_ROOT}/arena_snapshot.json"
  exit 0
fi

echo "==> Full competition export (mode=full, hero + top 50)…"
"${PY[@]}" examples/export_competition_hands.py \
  --match "$COMP" \
  --mode full \
  --top-agents 50 \
  --replays-top-agents 10 \
  --out-dir "${OUT_ROOT}/arena-export"

echo "==> Researcher trajectory summary…"
bash scripts/export_researcher_trajectory.sh \
  --competition-id "$COMP" \
  --out-dir "${OUT_ROOT}/trajectory-bundle"

echo "==> Copy today's local gate reports (if any)…"
GATES_DIR="${OUT_ROOT}/local-gates"
mkdir -p "$GATES_DIR"
if [[ -d reports/researcher-round ]]; then
  find reports/researcher-round -maxdepth 1 -type d -name 'gate-hu-*' -mtime -1 2>/dev/null \
    | head -5 | while read -r d; do
    cp -R "$d" "$GATES_DIR/"
  done
fi

MANIFEST="${OUT_ROOT}/harvest_manifest.json"
python3 - <<'PY' "$OUT_ROOT" "$COMP" "$HERO" "$TARGET_HANDS" "$MANIFEST"
import json, sys
from datetime import datetime, timezone
from pathlib import Path

out = Path(sys.argv[1])
comp, hero, target, manifest = sys.argv[2], sys.argv[3], int(sys.argv[4]), Path(sys.argv[5])
snap_path = out / "arena_snapshot.json"
snap = json.loads(snap_path.read_text()) if snap_path.is_file() else {}

def count_jsonl(p: Path) -> int:
    if not p.is_file():
        return 0
    return sum(1 for _ in p.open())

export_dir = out / "arena-export"
counts = {}
for name in ("submissions.jsonl", "agents.jsonl", "tables.jsonl", "replays.jsonl"):
    counts[name] = count_jsonl(export_dir / name)

doc = {
    "schema": "devfun.sandbox_season_harvest.v1",
    "harvested_at": datetime.now(timezone.utc).isoformat(),
    "competition_id": comp,
    "hero_handle": hero,
    "target_hands": target,
    "out_root": str(out.resolve()),
    "arena_snapshot": str(snap_path),
    "export_counts": counts,
    "trajectory_bundle": str((out / "trajectory-bundle").resolve()),
    "next_steps": [
        "Read trajectory-bundle/axis_summary.json + gate_failures",
        "Run export_regression_spots.py on hero worst chipDelta hands",
        "Compare arena-export/submissions.jsonl vs local gate maniac-audit",
        "Stage brief for tomorrow tune in briefs/",
    ],
}
manifest.write_text(json.dumps(doc, indent=2) + "\n")
print(f"Manifest → {manifest}")
PY

echo ""
echo "SANDBOX SEASON HARVEST OK → ${OUT_ROOT}"
echo "  arena_snapshot.json  — live TS / adj BB / submission status"
echo "  arena-export/        — submissions, agents, tables, replays"
echo "  trajectory-bundle/   — axis M₁–M₉ + export merge"
echo "  harvest_manifest.json — start here tomorrow"
