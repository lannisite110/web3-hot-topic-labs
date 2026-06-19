// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title SessionKeyDemo — 受限会话密钥教学，仅测试网
contract SessionKeyDemo {
    address public owner;
    mapping(address => uint256) public sessionExpiry;

    constructor() {
        owner = msg.sender;
    }

    function grantSession(address sessionKey, uint256 ttlHours) external {
        require(msg.sender == owner, "not owner");
        sessionExpiry[sessionKey] = block.timestamp + ttlHours * 1 hours;
    }

    function isSessionValid(address sessionKey) external view returns (bool) {
        return sessionExpiry[sessionKey] > block.timestamp;
    }
}
