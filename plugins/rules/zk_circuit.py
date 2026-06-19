"""ZK Circuit Compile Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("circuit_name", "demo_circuit")
    return ok(
        "plugins/zk-circuit/contracts/ZkCircuit.cairo",
        "cairo",
        "HOT_ZK_CIRCUIT_COMPILE",
        ["circuit_name=" + str(param), "plugin_id=edu.hot.zk-circuit"],
    )
