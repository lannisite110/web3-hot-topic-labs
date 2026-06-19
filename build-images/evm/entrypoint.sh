#!/usr/bin/env bash
set -euo pipefail
# 用法: entrypoint.sh <command...>
# 示例: entrypoint.sh solc --version
LANG_GROUP="${EDU_LANG_GROUP:-evm}"
echo "==> EVM toolchain ready (lang-group=${LANG_GROUP}, testnet-only)"
exec "$@"
