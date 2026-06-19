"""MEV PBS Simulation Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("block_slots", "12")
    return ok(
        "plugins/mev/contracts/MevPbsSim.huff",
        "huff",
        "HOT_MEV_PBS_SIM",
        ["block_slots=" + str(param), "plugin_id=edu.hot.mev"],
    )
