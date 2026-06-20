"""DAO Vote Simulation Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    proposal_id = str(inp.params.get("proposal_id", "1"))
    try:
        yes_votes = max(0, int(inp.params.get("yes_votes", 0)))
        no_votes = max(0, int(inp.params.get("no_votes", 0)))
        quorum = max(1, int(inp.params.get("quorum", 100)))
    except (TypeError, ValueError):
        yes_votes, no_votes, quorum = 0, 0, 100

    total = yes_votes + no_votes
    turnout_pct = round(100 * total / quorum, 1) if quorum else 0
    if total == 0:
        status = "draft"
    elif yes_votes > no_votes and total >= quorum * 0.1:
        status = "passed"
    elif no_votes >= yes_votes and total >= quorum * 0.1:
        status = "rejected"
    else:
        status = "active"

    title = str(inp.params.get("proposal_title", f"教学提案 #{proposal_id}"))

    return ok(
        "plugins/dao/contracts/DaoVoteDemo.sol",
        "solidity",
        "HOT_DAO_VOTE_SIM",
        [
            f"proposal_id={proposal_id}",
            f"proposal_title={title}",
            f"yes_votes={yes_votes}",
            f"no_votes={no_votes}",
            f"quorum_target={quorum}",
            f"turnout_pct={turnout_pct}",
            f"proposal_status={status}",
            "plugin_id=edu.hot.dao",
        ],
    )
