"""ZK Modular Rollup Lab — 教学规则 evaluate。"""

from __future__ import annotations

import hashlib

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    try:
        batch_size = max(1, min(int(inp.params.get("batch_size", 8)), 64))
    except (TypeError, ValueError):
        batch_size = 8

    tx_count = batch_size * 12
    mock_root = "0x" + hashlib.sha256(f"edu-zk-batch-{batch_size}".encode()).hexdigest()[:40]

    return ok(
        "plugins/zk-modular/contracts/ModularRollupDemo.sol",
        "cairo",
        "HOT_ZK_ROLLUP_SIM",
        [
            f"batch_size={batch_size}",
            f"tx_count={tx_count}",
            f"mock_batch_root={mock_root}",
            f"verifier=mock-sepolia",
            f"batches_submitted={batch_size}",
            f"l1_anchor=sepolia-rollup-bridge-demo",
            "plugin_id=edu.hot.zk-modular",
        ],
    )
