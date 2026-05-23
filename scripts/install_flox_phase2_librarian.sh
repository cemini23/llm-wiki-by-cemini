#!/usr/bin/env bash
# Install FLOX Phase 2 WS publisher on cemini-librarian (run from laptop with ssh).
set -euo pipefail

LIBRARIAN="${LIBRARIAN:-cemini-librarian}"
PROD="${PROD:-cemini-prod}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "==> Fetch prod REDIS_PASSWORD (read-only)"
REDIS_PASSWORD="$(ssh "$PROD" "grep '^REDIS_PASSWORD=' /opt/cemini/.env | cut -d= -f2-")"
[[ -n "$REDIS_PASSWORD" ]] || { echo "REDIS_PASSWORD missing on prod"; exit 1; }

echo "==> Prod: expose Redis on private net 10.0.0.3:6379"
ssh "$PROD" 'OVERRIDE=/opt/cemini/docker/compose.flox-phase2.override.yml
cat > "$OVERRIDE" <<EOF
# FLOX Phase 2 — librarian publishes intel keys to prod Redis over private net
services:
  redis:
    ports:
      - "10.0.0.3:6379:6379"
EOF
cd /opt/cemini && docker compose --env-file .env \
  -f docker-compose.yml -f docker/compose.flox-phase2.override.yml \
  up -d --force-recreate redis'

echo "==> Librarian: clone/pull Cemini-Financial-Suite + systemd"
ssh "$LIBRARIAN" bash -s <<REMOTE
set -euo pipefail
REPO=/opt/cemini-bulk/Cemini-Financial-Suite
if [[ ! -d "\$REPO/.git" ]]; then
  git clone --depth 1 https://github.com/cemini23/Cemini-Financial-Suite.git "\$REPO"
else
  git -C "\$REPO" pull
fi
/opt/cemini-bulk/.venv/bin/pip install -q redis websockets httpx pydantic requests aiohttp
cat > /opt/cemini-bulk/.flox_phase2.env <<EOF
REDIS_HOST=10.0.0.3
REDIS_PORT=6379
REDIS_PASSWORD=${REDIS_PASSWORD}
FLOX_PM_REDIS_TTL=120
FLOX_PM_PUBLISH_INTERVAL=5
FLOX_PM_SUBSCRIBE_REFRESH_SEC=300
EOF
chmod 600 /opt/cemini-bulk/.flox_phase2.env
REMOTE
scp "$SCRIPT_DIR/flox_phase2_librarian.service" \
  "$LIBRARIAN:/etc/systemd/system/flox-phase2-ws.service"

ssh "$LIBRARIAN" bash -s <<REMOTE
set -euo pipefail
systemctl daemon-reload
systemctl enable --now flox-phase2-ws.service
sleep 3
systemctl is-active flox-phase2-ws.service
tail -5 /var/log/flox-phase2-ws.log
REMOTE

echo "==> Verify Redis key from librarian"
ssh "$LIBRARIAN" 'set -a && source /opt/cemini-bulk/.flox_phase2.env && set +a
/opt/cemini-bulk/.venv/bin/python3 - <<PY
import json, os, redis
r = redis.Redis(host=os.environ["REDIS_HOST"], port=int(os.environ.get("REDIS_PORT", 6379)),
                password=os.environ.get("REDIS_PASSWORD"), decode_responses=True)
raw = r.get("intel:polymarket_flox_ws")
d = json.loads(raw) if raw else {}
v = d.get("value", d)
print("book_count", v.get("book_count"), "status", v.get("status"))
PY'

echo "==> Prod: enable FLOX_PHASE2_ENABLED when books present"
ssh "$PROD" bash -s <<'REMOTE'
set -euo pipefail
cd /opt/cemini
if grep -q '^FLOX_PHASE2_ENABLED=' .env; then
  sed -i 's/^FLOX_PHASE2_ENABLED=.*/FLOX_PHASE2_ENABLED=true/' .env
else
  echo 'FLOX_PHASE2_ENABLED=true' >> .env
fi
grep FLOX_PHASE2 .env
docker compose restart cemini_mcp 2>/dev/null || docker restart cemini_mcp 2>/dev/null || true
REMOTE

echo "Done. Check: ssh $LIBRARIAN journalctl -u flox-phase2-ws -f"
