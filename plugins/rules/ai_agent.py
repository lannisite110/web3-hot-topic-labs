"""AI Agent Sandbox Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("max_actions", "3")
    return ok(
        "plugins/ai-agent/contracts/AgentSandbox.sol",
        "solidity",
        "HOT_AI_AGENT_SANDBOX",
        ["max_actions=" + str(param), "plugin_id=edu.hot.ai-agent"],
    )
