// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title GenericDeFiDemo — 教学模板，仅测试网
contract GenericDeFiDemo {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
}
