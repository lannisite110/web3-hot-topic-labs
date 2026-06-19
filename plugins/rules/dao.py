"""DAO Vote Simulation Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("proposal_id", "1")
    return ok(
        "plugins/dao/contracts/DaoVoteDemo.sol",
        "solidity",
        "HOT_DAO_VOTE_SIM",
        ["proposal_id=" + str(param), "plugin_id=edu.hot.dao"],
    )
