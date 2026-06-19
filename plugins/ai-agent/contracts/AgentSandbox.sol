// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title AgentSandbox — AI Agent 受限权限沙箱教学，仅测试网
contract AgentSandbox {
    address public admin;
    uint256 public actionCount;
    uint256 public maxActions;

    constructor(uint256 _maxActions) {
        admin = msg.sender;
        maxActions = _maxActions;
    }

    function agentAction() external {
        require(msg.sender == admin, "sandbox only");
        require(actionCount < maxActions, "action limit");
        actionCount += 1;
    }
}
