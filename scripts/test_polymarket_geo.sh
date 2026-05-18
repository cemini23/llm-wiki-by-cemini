#!/bin/bash
# Test whether current IP passes Polymarket geo-block
# Usage: bash scripts/test_polymarket_geo.sh

echo "=== Current IP info ==="
curl -s https://ipinfo.io/json | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'IP: {d[\"ip\"]}\nCountry: {d.get(\"country\",\"?\")}\nCity: {d.get(\"city\",\"?\")}\nOrg: {d.get(\"org\",\"?\")}')"

echo ""
echo "=== CLOB public reads ==="
for ep in time price; do
    code=$(curl -s -o /dev/null -w "%{http_code}" "https://clob.polymarket.com/${ep}")
    echo "GET /${ep}: HTTP ${code}"
done

echo ""
echo "=== POST /order (the geo-gate) ==="
response=$(curl -s -w "\nHTTP:%{http_code}" -X POST https://clob.polymarket.com/order)
echo "$response"

echo ""
echo "=== Gamma market data ==="
code=$(curl -s -o /dev/null -w "%{http_code}" "https://gamma-api.polymarket.com/markets?tag_id=1&active=true&limit=1")
echo "GET /markets: HTTP ${code}"
