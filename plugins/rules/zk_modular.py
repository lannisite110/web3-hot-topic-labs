"""ZK Modular Rollup Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("batch_size", "8")
    return ok(
        "plugins/zk-modular/contracts/ModularRollupDemo.sol",
        "solidity",
        "HOT_ZK_ROLLUP_SIM",
        ["batch_size=" + str(param), "plugin_id=edu.hot.zk-modular"],
    )
