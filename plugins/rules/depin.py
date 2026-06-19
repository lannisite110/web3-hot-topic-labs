"""DePIN Node Simulation Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("node_count", "5")
    return ok(
        "plugins/depin/contracts/DepinNode.rs",
        "rust",
        "HOT_DEPIN_NODE_SIM",
        ["node_count=" + str(param), "plugin_id=edu.hot.depin"],
    )
