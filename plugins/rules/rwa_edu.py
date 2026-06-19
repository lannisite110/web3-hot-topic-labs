"""RWA Education Simulation Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("asset_id", "DEMO-RWA-001")
    return ok(
        "plugins/rwa-edu/contracts/RwaMappingDemo.sol",
        "solidity",
        "HOT_RWA_EDU_SIM",
        ["asset_id=" + str(param), "plugin_id=edu.hot.rwa-edu"],
    )
