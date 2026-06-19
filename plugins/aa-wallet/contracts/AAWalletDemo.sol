// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title AAWalletDemo — ERC-4337 风格 AA 钱包教学 mock，仅测试网
contract AAWalletDemo {
    address public owner;
    mapping(bytes32 => bool) public executedUserOps;

    constructor(address _owner) {
        owner = _owner;
    }

    function validateUserOp(bytes32 userOpHash) external view returns (bool) {
        return msg.sender == owner;
    }

    function executeUserOp(bytes32 userOpHash) external {
        require(validateUserOp(userOpHash), "invalid op");
        executedUserOps[userOpHash] = true;
    }
}
