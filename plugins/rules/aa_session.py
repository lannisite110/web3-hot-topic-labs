"""AA Session Key Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("session_ttl_hours", "24")
    return ok(
        "plugins/aa-session/contracts/SessionKeyDemo.sol",
        "solidity",
        "HOT_AA_SESSION_KEY_DEMO",
        ["session_ttl_hours=" + str(param), "plugin_id=edu.hot.aa-session"],
    )
