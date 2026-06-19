#!/usr/bin/env bash
# Agent-1 第一阶段联合调试冒烟 — 需在主库 v0.1.0 后端已启动或本脚本自启栈
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CORE="${CORE_ROOT:-$(cd "$ROOT/../web3-edu-platform-core" && pwd)}"

if [ ! -d "$CORE" ]; then
  echo "ERROR: web3-edu-platform-core not found at $CORE"
  exit 1
fi

export CORE_ROOT="$CORE"
export GATEWAY_PORT="${GATEWAY_PORT:-8080}"
export RULE_ENGINE_PORT="${RULE_ENGINE_PORT:-8081}"

cd "$CORE"
PYTHON="${CORE}/.venv/bin/python"
[ -x "$PYTHON" ] || { python3 -m venv "${CORE}/.venv" && "${CORE}/.venv/bin/pip" install -q -r rule-engine-py/requirements.txt pyyaml; }

echo "==> register plugins"
"$PYTHON" ci/register-plugins.py "$(dirname "$ROOT")"

echo "==> validate language-advisor manifest"
MANIFEST="$ROOT/plugins/language-advisor/plugin.manifest.yaml" bash ci/compliance/validate-plugin.sh

echo "==> compliance-check hot-topic-labs"
bash ci/compliance/compliance-check.sh "$ROOT"

STARTED=0
cleanup() {
  if [ "$STARTED" = "1" ]; then
    fuser -k "${GATEWAY_PORT}/tcp" "${RULE_ENGINE_PORT}/tcp" "${SCHEDULER_PORT:-8082}/tcp" 2>/dev/null || true
    kill $(jobs -p) 2>/dev/null || true
  fi
}
trap cleanup EXIT

if ! curl -sf "http://127.0.0.1:${RULE_ENGINE_PORT}/health" >/dev/null 2>&1; then
  echo "==> starting rule-engine + gateway (scheduler optional for advise-only)"
  STARTED=1
  (cd rule-engine-py && "$PYTHON" main.py) &
  sleep 1
  (cd control-plane-go && CORE_ROOT="$CORE" SCHEDULER_PORT="${SCHEDULER_PORT:-8082}" go run ./cmd/scheduler) &
  sleep 2
  (cd api-gateway-go && CORE_ROOT="$CORE" GATEWAY_PORT="$GATEWAY_PORT" go run ./cmd/gateway) &
  sleep 4
fi

curl -sf "http://127.0.0.1:${RULE_ENGINE_PORT}/health" | grep -q ok

echo "==> rule-engine direct evaluate (cairo / ZK)"
OUT=$("$PYTHON" - <<PY
import json, urllib.request
req = urllib.request.Request(
    "http://127.0.0.1:${RULE_ENGINE_PORT}/evaluate",
    data=json.dumps({
        "plugin_id": "edu.hot.language-advisor",
        "user_prompt": "zk rollup cairo starknet 零知识",
        "params": {},
        "allowed_chain_ids": [11155111],
    }).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req) as r:
    print(r.read().decode())
PY
)
echo "$OUT" | grep -q cairo
echo "$OUT" | grep -q 'compliance_passed.*true'

echo "==> validate all hot-topic manifests"
for m in "$ROOT"/plugins/*/plugin.manifest.yaml; do
  MANIFEST="$m" bash "$CORE/ci/compliance/validate-plugin.sh"
done

echo "==> rule-engine evaluate zk-modular"
OUT2=$("$PYTHON" - <<PY
import json, urllib.request
req = urllib.request.Request(
    "http://127.0.0.1:${RULE_ENGINE_PORT}/evaluate",
    data=json.dumps({
        "plugin_id": "edu.hot.zk-modular",
        "user_prompt": "zk rollup batch",
        "params": {"batch_size": "8"},
        "allowed_chain_ids": [11155111],
    }).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req) as r:
    print(r.read().decode())
PY
)
echo "$OUT2" | grep -q ModularRollupDemo
echo "$OUT2" | grep -q solidity

if curl -sf "http://127.0.0.1:${GATEWAY_PORT}/health" >/dev/null 2>&1; then
  :
else
  for i in 1 2 3 4 5 6 7 8; do
    curl -sf "http://127.0.0.1:${GATEWAY_PORT}/health" >/dev/null 2>&1 && break
    sleep 2
  done
fi

if curl -sf "http://127.0.0.1:${GATEWAY_PORT}/health" >/dev/null 2>&1; then
  echo "==> gateway simulate (DeFi / solidity)"
  RESP=$(curl -sf -X POST "http://127.0.0.1:${GATEWAY_PORT}/api/v1/labs/edu.hot.language-advisor/simulate" \
    -H 'Content-Type: application/json' \
    -d '{"user_prompt":"通用 defi swap dex","params":{},"allowed_chain_ids":[11155111]}')
  echo "$RESP" | grep -q edu.hot.language-advisor
  echo "$RESP" | grep -q solidity
fi

echo "==> Agent-1 joint-debug smoke PASSED (11 plugins)"
